# Case Study: Approval Test Initially Manufactured Its Own Waiting State

## Incident

An approval/resume test initially created the waiting work item and pending action itself. That made the test a co-executor and allowed it to "prove" a state the production path had never naturally produced.

## Correction

The test was converted into an observer of the real flow:

`real gated request → same canonical work item WAITING → pending action persisted → approval → original action resumed → normal production execution → terminal evidence`

## General Rule

Approval/resume verification must prove continuity of the original work item and original pending action. Reconstructing equivalent state inside the test is not evidence that production behavior works.

## Boundary

This verifies approval-gated resume semantics for the scoped workflow. It does not by itself prove arbitrary long-running workflow recovery.
