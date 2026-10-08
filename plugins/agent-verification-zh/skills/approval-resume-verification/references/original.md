# Approval / WAITING / Resume Verification

- **skill_id**: `agent.verify.approval-resume.v1`
- **type**: verifier
- **applicability**: Agent actions that require user/admin approval, consent, or a human interruption before execution

## Trigger

Invoke when an operation is gated and must resume after approval.

## Required inputs

- real gated request
- canonical lifecycle/state store
- approval and rejection decisions
- production trace/evidence

## Preconditions

The system can distinguish gated actions from immediately executable actions, and the original executable action can be persisted or reconstructed without test injection.

## Procedure

1. Submit a real gated request through the production entry.
2. Verify the same canonical work item transitions to a waiting state rather than a terminal failure.
3. Verify the original pending action is persisted by production code.
4. Approve the request.
5. Observe the same work item resume through the normal production dispatcher.
6. Verify natural Execution/Evidence/Verification/Trace or project-equivalent output.
7. Repeat with rejection and confirm the action does not execute.
8. Repeat with an execution failure and confirm approval does not force success.

## Required evidence

- unchanged canonical work-item identity
- persisted original action
- approval/rejection trace
- normal production execution evidence after approval
- truthful terminal state

## Failure signatures

- initial gated request becomes FAILED
- approval creates a replacement work item
- test injects the pending action
- approval directly writes SUCCESS
- rejection still executes the action

## Success criteria

The gated lifecycle is uninterrupted: same work item, same original action, normal production execution, truthful terminal outcome.

## Non-goals

This skill does not design the approval UI or grant blanket authorization.

## Handoff

If resume requires test-created state, production approval/resume behavior is not verified.

## Provenance boundary

Derived from verification of a same-work-item WAITING → APPROVE → resume-original-action chain. It does not prove arbitrary long-running workflow orchestration.
