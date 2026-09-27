# Process Lifecycle Verification

- **skill_id**: `agent.verify.process-lifecycle.v1`
- **type**: verifier
- **applicability**: child processes, servers, sockets, browser sessions, workers, native hosts

## Trigger

Invoke whenever a capability depends on starting and controlling an external process or connection.

## Required inputs

- process/session identity
- readiness probe
- meaningful control probe
- shutdown/close API
- orphan/port/handle observations where available

## Preconditions

Expected parent-child ownership and graceful shutdown semantics are known.

## Procedure

1. Start the process through the production mechanism.
2. Wait for **readiness**, not merely PID creation.
3. Perform a meaningful control action and, where possible, read back state.
4. Request graceful shutdown/connection close.
5. Wait for the protocol/process close event with a bounded timeout.
6. Verify child processes, sockets, ports, and handles are released.
7. Run the operation again to prove repeatability.

## Required evidence

- readiness confirmation
- control result/read-back
- close/exit observation
- cleanup/orphan/port check
- second-run repeatability when relevant

## Failure signatures

- PID exists but service is not ready
- assertions pass but runner hangs
- parent exits while child remains
- socket/port remains bound after shutdown
- `close()` called but close completion never observed

## Recovery

Attempt graceful close first. After a bounded timeout, perform scoped forced cleanup and capture evidence. Do not mutate global machine state merely to make the test exit.

## Success criteria

The capability becomes ready, accepts meaningful control, shuts down cleanly, leaves no relevant leaked ownership, and can run again.

## Non-goals

Global process killing, global environment mutation, or application-specific workaround logic.

## Provenance boundary

Derived from real external-process and socket lifecycle evidence. Application-specific startup workarounds are case-study details, not universal rules.
