# False-Green Detection

- **skill_id**: `agent.verify.false-green.v1`
- **type**: verifier
- **applicability**: surprising PASS results, aggregate green dashboards, audits, POCs, integration tests

## Trigger

Invoke when a result looks green but the supporting evidence may be weaker than the claim.

## Required inputs

- frozen requirement scope
- exact candidate identity
- test source or execution definition
- raw logs
- structured result
- persisted/runtime evidence where applicable

## Procedure

1. Take each PASS claim and trace it backward to the exact observation that supports it.
2. Identify **who created the evidence**: production runtime, test harness, mock, fixture, or human.
3. Compare asserted success against the real terminal state.
4. Check whether the evidence covers the full claimed scope or only a partial subset.
5. Check readiness, control, and cleanup for process-based claims.
6. Downgrade any claim whose evidence is below the required level.

## Required evidence

A positive claim must link to direct observation and provenance, not merely an assertion.

## Failure signatures

- caught exception but test still increments a PASS count
- partial coverage labeled VERIFIED
- PID/process existence treated as functional control
- source-string search treated as runtime execution
- mock/stub output treated as production evidence
- test manually inserts success records
- assertions pass but process never terminates cleanly

## Failure classification

Use the narrowest honest status supported by the project contract, such as:

- `NOT_VERIFIED`
- `PARTIAL`
- `BLOCKED`
- `FAIL`

Do not upgrade uncertainty to PASS.

## False-positive traps

A green summary is not evidence by itself. Aggregate counts must be traceable to per-requirement evidence.

## Success criteria

Every green claim has direct evidence of the required scope and no stronger interpretation than the evidence supports.

## Non-goals

This skill does not fix the implementation and is not a general security review.

## Handoff

If a green claim fails provenance review, identify the smallest missing Reality probe needed to verify it.

## Provenance boundary

Derived from real false-green findings involving exit codes, source strings, mock frontend bridges, manually manufactured persistence truth, and process lifecycle leaks.
