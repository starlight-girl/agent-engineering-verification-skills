# Install / 安装

Two free editions share the same original contracts. Install one edition to avoid duplicate skill selection.

| Edition | Plugin ID | Language |
| --- | --- | --- |
| English | `agent-verification-en` | English workflows and reports |
| 中文版 | `agent-verification-zh` | 中文操作指南、中文报告，附完整英文原始契约 |

## Codex CLI / desktop

Use a current Codex build with `codex plugin` commands:

```sh
codex plugin marketplace add starlight-girl/agent-engineering-verification-skills --ref v1.2.0
codex plugin add agent-verification-zh@agent-engineering-verification
```

For English, replace the second command with:

```sh
codex plugin add agent-verification-en@agent-engineering-verification
```

Start a new chat after installation. In supported desktop clients, open the Plugins Directory and choose **Agent Engineering Verification** as the marketplace source. Client availability and workspace policy can affect installation.

安装后开启新聊天；支持本地市场的桌面客户端可在插件目录选择 **Agent Engineering Verification** 来源。使用前确认宿主工具能够读取你授权的文件，纯技能包不提供远程访问或额外权限。

## ZIP download / 离线下载

Download the English or Chinese ZIP plus `SHA256SUMS` from [Releases](https://github.com/starlight-girl/agent-engineering-verification-skills/releases/latest). Each ZIP contains one complete plugin directory including hidden compatibility metadata.

Windows verification:

```powershell
Get-FileHash -Algorithm SHA256 ./agent-verification-zh-1.2.0.zip
```

Compare the hash with `SHA256SUMS`. For local marketplace distribution, clone the tagged repository and run `codex plugin marketplace add <absolute-clone-path>`, then install the edition above. A bare ZIP is not an executable installer; use your host's supported plugin import facility where available.

下载后校验 SHA-256。完整仓库内置本地市场目录；可解压 GitHub 标签源码、注册其目录，再安装对应版本。ZIP 不是 EXE 安装器，普通聊天附件上传不等于安装插件。

## ChatGPT directory

This GitHub release does not by itself make the plugin searchable in the universal ChatGPT / Codex public directory. Directory publication requires a verified publisher, package scans, review, and a separate publish action. We will link an approved listing here when one exists. Supported desktop local marketplaces are a separate installation path; ordinary ChatGPT web/mobile access must not be assumed.

GitHub 公开发布与官方目录上架是独立状态。官方目录需发布者验证、扫描、审核与正式发布；获批后才提供目录安装链接。不要把下载成功视为官方上架或实际审计结果通过。

## Try it / 使用示例

- “请只读审计这个项目。冻结当前候选，检查测试全绿是否有真实证据，输出最小阻塞项。”
- “请验证正式用户入口是否自然产生执行记录，不要让测试手动制造成功。”
- “Audit the release evidence against the exact candidate and list stale or missing observations.”
- “Verify readiness, control, shutdown, and repeatability of this external process within my authorized scope.”

The host must have access to supplied evidence and authorized tools. Missing runtime access yields an unverified result; installation never grants permission to repair or approve gated actions.
