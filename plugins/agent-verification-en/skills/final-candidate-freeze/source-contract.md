# Playbook: Final Candidate Freeze

## Purpose

Convert “the current code appears to pass” into an independently selectable, evidence-bound candidate.

## Procedure

1. Stop drift and record source/build/environment identity.
2. Run the complete frozen gate. Targeted tests are repair feedback, not final acceptance.
3. Preserve per-item structured results and raw outputs.
4. Classify all relevant working-tree changes.
5. Generate a manifest or equivalent immutable candidate record.
6. Cross-check manifest, summary, report, and handoff identities/counts.
7. Run independent audit against only that candidate.
8. Create a freeze index that states what must not be casually reopened.

## Required gate

Freeze only when:
- required failures are zero under the frozen contract,
- all required evidence is complete,
- conditional dependencies are represented truthfully,
- no relevant post-run drift exists,
- candidate identity is unambiguous.

## Anti-patterns

- moving VCS HEAD used as the only identity for dirty content
- “latest folder” used instead of an explicit artifact pointer
- targeted PASS promoted to full-stage READY
- handoff still references superseded evidence

## Skills used

- Candidate Identity Verification
- Artifact and Evidence Integrity
- Dependency Truth Verification
- Reality-Grounded Acceptance
