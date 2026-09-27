# Environment vs Code Diagnosis

- **skill_id**: `agent.diagnose.environment-vs-code.v1`
- **type**: diagnostic
- **applicability**: capabilities that depend on external software, devices, services, configuration, ports, drivers, or machine state

## Trigger

Invoke when a capability is unavailable, fails before meaningful work, or behaves differently across environments.

## Required inputs

- dependency inventory
- process/service state
- configuration/device state
- runtime logs
- minimal reproduction probe

## Preconditions

Do not perform destructive repair during diagnosis. Change one variable at a time.

## Procedure

Check in this order:

1. **Installed / present?**
2. **Started / connected?**
3. **Ready / responding?**
4. **Correctly configured / accessible?**
5. **Minimal direct API or capability probe succeeds?**
6. Only after the environment passes the above checks, investigate the application code path.

When applying a suspected environment correction:
7. Scope it as narrowly as possible.
8. Rerun the same probe before and after the change.
9. Use the differential result to support the root-cause classification.

## Required evidence

Observed state plus a reproducible before/after or differential probe.

## Failure signatures

- source patch proposed before reproduction
- any exception mapped to “dependency missing”
- global workaround used as proof of root cause
- multiple variables changed simultaneously

## Failure classification

Use a supported diagnosis such as:
- `ENVIRONMENT_ISSUE`
- `CODE_ISSUE`
- `MIXED`
- `UNKNOWN`

Do not force a binary classification if evidence does not support it.

## Success criteria

Root-cause class is supported by differential evidence, and the same probe changes as predicted when the isolated cause is changed.

## Non-goals

Silent dependency installation or permanent global machine-policy modification.

## Handoff

If the environment is proven healthy but production still fails, pass the exact reproduction to implementation debugging or Production-Path Verification.

## Provenance boundary

Derived from real incidents involving missing dependencies, configuration issues, external-process readiness, and a machine-specific environment startup failure.
