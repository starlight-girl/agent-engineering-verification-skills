# Artifact and Evidence Integrity

- **skill_id**: `agent.verify.artifact-integrity.v1`
- **type**: verifier
- **applicability**: stage sign-off, release candidate validation, independent audit, handoff

## Trigger

Invoke when a report or release decision depends on an acceptance artifact.

## Required inputs

- exact candidate manifest or equivalent identity
- per-requirement results
- raw command/process outputs
- environment/run metadata
- timestamps or build identities

## Preconditions

A candidate must be identifiable without relying on “latest folder” or an ambiguous moving working tree.

## Procedure

1. Lock the candidate identity and acceptance artifact identity.
2. Confirm the run completed normally: start, per-item execution, completion, summary/report.
3. Build a mapping:
   Requirement → Test → Structured Result → Raw Log → Persisted Evidence.
4. Inspect every REQUIRED item individually.
5. Compare source/build modification times or identities against the artifact time.
6. Check that summary counts equal the per-item results.
7. Verify handoff/release pointers reference the same candidate and artifact.

## Required evidence

- manifest or equivalent candidate identity
- per-check structured results
- raw stdout/stderr or equivalent
- environment/run metadata
- completion event
- freshness evidence

## Failure signatures

- targeted PASS presented as full-suite PASS
- incomplete/interrupted run selected because it is newest
- manifest points to stale artifact
- production files changed after acceptance
- report has only aggregate numbers with no per-item evidence

## False-positive traps

A polished report is not sufficient evidence if its source artifact is stale, incomplete, or mismatched.

## Success criteria

Every REQUIRED claim is traceable to current evidence, aggregate counts match, and there is no post-acceptance drift.

## Non-goals

This skill does not review code quality or decide whether the requirements themselves are good.

## Handoff

If artifact identity is ambiguous, freeze a new candidate and rerun the required acceptance scope.

## Provenance boundary

Derived from real candidate/artifact drift, interrupted acceptance runs, and final manifest-to-artifact locking.
