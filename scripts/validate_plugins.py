"""Inspect the released ZIP bytes, source parity, links, and package boundaries."""
import hashlib
import io
import json
from pathlib import Path
import re
import zipfile
from PIL import Image
from build_plugins import ROOT, VERSION, GUIDES

def validate():
    results = []
    catalog = json.loads((ROOT/'.agents/plugins/marketplace.json').read_text(encoding='utf-8'))
    assert len(catalog['plugins']) == 2
    index = json.loads((ROOT/'skill-index.json').read_text(encoding='utf-8'))
    originals = [x['path'] for group in ('skills','playbooks','roles') for x in index[group]]
    for entry in catalog['plugins']:
        name = entry['name']
        archive = ROOT/'dist'/f'{name}-{VERSION}.zip'
        with zipfile.ZipFile(archive) as z:
            assert z.testzip() is None
            names = z.namelist()
            assert len(names) == len(set(names))
            assert all(n.startswith(name+'/') and '..' not in Path(n).parts for n in names)
            assert not any(n.endswith(('.app.json','mcp.json','.exe','.dll','.env')) for n in names)
            manifest = json.loads(z.read(name+'/plugin.json'))
            overlay = json.loads(z.read(name+'/.codex-plugin/plugin.json'))
            assert manifest['name'] == name and manifest['version'] == VERSION
            assert overlay['interface'] == manifest['extensions']['com.openai']['interface']
            assert 'apps' not in overlay and 'apps' not in manifest['extensions']['com.openai']
            ui = manifest['extensions']['com.openai']['interface']
            assert len(ui['displayName']) <= 30 and len(ui['shortDescription']) <= 30
            assert len(ui['longDescription']) <= 4000
            assert all(0 < len(p) <= 128 and '\n' not in p for p in ui['defaultPrompt'])
            assert manifest['extensions']['com.openai']['publication']['countries'] == []
            assert manifest['extensions']['com.openai']['review']['commerce'] is False
            for field in ('websiteURL','supportURL','privacyPolicyURL','termsOfServiceURL'):
                assert ui[field].startswith('https://github.com/starlight-girl/')
            icon = Image.open(io.BytesIO(z.read(name+'/assets/icon.png')))
            assert icon.format == 'PNG' and icon.width == icon.height and 256 <= icon.width <= 4096
            assert len(z.read(name+'/assets/icon.png')) <= 5 * 1024 * 1024
            skills = [n for n in names if n.endswith('/SKILL.md')]
            assert len(skills) == 14
            for n in skills:
                text = z.read(n).decode('utf-8')
                slug = Path(n).parent.name
                assert text.startswith('---\nname: '+slug+'\ndescription: ')
                assert slug in GUIDES
                for link in re.findall(r'\]\(([^)]+)\)', text):
                    if not link.startswith(('https://','http://','#')):
                        target = (Path(n).parent/link).as_posix()
                        assert target in names, (n,target)
            for source in originals:
                slug = Path(source).stem
                assert z.read(name+'/skills/'+slug+'/source-contract.md') == (ROOT/source).read_text(encoding='utf-8').encode('utf-8')
            for row in z.read(name+'/SHA256SUMS').decode().splitlines():
                digest, path = row.split('  ',1)
                assert hashlib.sha256(z.read(name+'/'+path)).hexdigest() == digest
            results.append({'package': archive.name, 'skill_entrypoints':len(skills), 'files':len(names), 'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(), 'status':'PASS', 'scope':'ZIP integrity, metadata, original contract parity, icon and local links'})
    report = {'results':results, 'runtime_audit_behavior':'NOT_VERIFIED by static package checks', 'openai_directory':'NOT_SUBMITTED'}
    (ROOT/'validation-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    validate()
