# External Application Safe Startup & Recovery

- **skill_id**: `agent.build.external-app-safe-startup.v1`
- **type**: builder + diagnostic
- **applicability**: external desktop/server applications controlled by an Agent through a protocol, socket, API, or automation surface

## Trigger

Invoke when the Agent must start an external application whose readiness, environment, connection, or shutdown is unreliable.

## Required inputs

- executable/application identity
- configuration/profile location where relevant
- environment/dependency state
- readiness endpoint/probe
- reversible control action
- graceful close/shutdown mechanism

## Preconditions

Preserve user configuration. Know which environment changes are process-scoped versus global.

## Procedure

1. Validate required executable/resources/dependencies.
2. Start the application with the smallest necessary **process-scoped** environment.
3. Wait for protocol/application readiness rather than PID existence.
4. Connect through the intended control surface.
5. Read state before acting.
6. Perform a reversible control action and verify read-back where available.
7. Disconnect/close gracefully and wait for close completion.
8. Verify process/port/socket cleanup.
9. Retry from a clean state to prove repeatability.
10. If startup fails, use Environment-vs-Code Diagnosis before changing production code.

## Required evidence

- process/application identity
- readiness observation
- protocol/control handshake
- reversible action/read-back
- graceful shutdown/cleanup evidence
- retry result

## Failure signatures

- process alive but control endpoint unavailable
- environment-specific initialization error
- stale crash/recovery state
- dangling socket/session from previous run
- global workaround applied without isolation

## Recovery

Prefer:
1. diagnose the specific startup/readiness failure,
2. apply the smallest scoped correction,
3. restart cleanly,
4. verify readiness and control again,
5. restore reversible state.

## Success criteria

The application becomes ready, is controllable through the intended interface, closes cleanly, and can repeat the sequence.

## Non-goals

Application-specific configuration recipes, arbitrary plugin maturity claims, or global machine mutation.

## Provenance boundary

Generalized from a real external-application integration incident plus process-lifecycle and environment-diagnosis rules. Application-specific environment and connection details are not universalized.
