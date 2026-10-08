# Dependency Truth Verification

- **skill_id**: `agent.verify.dependency-truth.v1`
- **type**: verifier
- **applicability**: external executables, drivers, services, devices, SDKs, optional providers, third-party applications

## Trigger

Invoke when a capability is unavailable or a dependency is reported missing.

## Required inputs

- frozen requirement gate: REQUIRED / CONDITIONAL or project-equivalent
- dependency probe result
- path/version/connection/error evidence
- Test Execution, Observed Reality, Requirement Status

## Procedure

1. Prove that the missing/unavailable item is a specific external dependency rather than a code defect or wrong path.
2. Check the frozen gate semantics.
3. Record the three dimensions separately.
4. A missing REQUIRED dependency blocks/fails the requirement according to contract.
5. A missing explicitly CONDITIONAL dependency may be non-blocking for the overall stage, but the capability itself must not be reported as PASS.
6. Preserve probe commands, errors, paths, and run identity.
7. If the dependency later becomes available, rerun Reality verification.

## Required evidence

Concrete dependency detection evidence, not only a human statement such as “not installed.”

## Failure signatures

- dependency missing converted to capability PASS
- every inconvenient dependency reclassified as conditional
- arbitrary exception caught and mislabeled dependency missing
- old missing result reused after dependency installation

## Success criteria

Dependency facts, requirement gate semantics, and stage aggregation are mutually consistent.

## Non-goals

This skill does not install the dependency or decide whether a product should bundle it.

## Handoff

If the root cause cannot be isolated, invoke Environment-vs-Code Diagnosis before classifying dependency truth.

## Provenance boundary

Derived from a real conditional-dependency incident in which an absent optional application was not falsely counted as capability PASS.
