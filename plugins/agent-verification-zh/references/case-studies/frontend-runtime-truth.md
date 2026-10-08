# Case Study: Source-Level Frontend Checks Produced a False Green

## Incident

A frontend acceptance check passed because expected source strings and mock bridge behavior existed. The test did not prove that a real rendered user action traversed the production frontend bridge and reached the authoritative runtime/backend path.

## Correction

The verification path was changed to observe the real runtime chain:

`rendered interaction → frontend bridge → host/main process → runtime/backend → authoritative state → read-back`

## General Rule

Source presence and mocks are useful implementation checks, but they are not sufficient evidence for a production frontend claim.

## Boundary

This pattern proves the runtime path for the scoped interaction. It does not automatically prove every page, visual state, accessibility property, or user journey.
