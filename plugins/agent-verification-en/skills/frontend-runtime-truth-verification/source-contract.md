# Frontend Runtime Truth Verification

- **skill_id**: `agent.verify.frontend-runtime-truth.v1`
- **type**: verifier
- **applicability**: products where a frontend/renderer communicates with a backend/runtime through IPC, bridge, preload, RPC, or equivalent boundary

## Trigger

Invoke when the frontend claims to display live backend/runtime truth.

## Required inputs

- production frontend entry or a clearly bounded reality harness
- real bridge/preload/RPC layer
- backend/runtime endpoint
- expected identity/revision/state
- page/DOM evidence if display itself is in scope

## Preconditions

Mock and production modes must be distinguishable.

## Procedure

1. Launch a real frontend/renderer boundary.
2. Invoke the real bridge/API from that boundary.
3. Observe dispatch through the production backend/runtime path.
4. Compare the returned payload identity/state with the authoritative backend source.
5. If the requirement includes rendering, verify the page/DOM/screenshot projection of that same payload.
6. Record any substituted test harness boundary and do not claim beyond it.

## Required evidence

- runtime invocation trace
- frontend-observed payload
- authoritative backend identity/revision or equivalent
- display evidence only when display is part of the requirement

## Failure signatures

- source-string check treated as frontend proof
- mocked bridge/context
- direct backend call with hand-written frontend mapping
- independent stale frontend store presented as backend truth

## Success criteria

The frontend observation is demonstrably derived from one authoritative backend/runtime truth for the claimed scope.

## Non-goals

Visual-design quality unless explicitly required.

## Handoff

If only IPC primitive coverage exists, report that exact boundary. Do not upgrade it to full product-page correctness.

## Provenance boundary

Derived from correction of source-string/mock bridge false greens. The source evidence proved a real frontend-to-runtime primitive, not every product page or visual state.
