# Case Study: Exit Code 0 Without Structured Reality Evidence

## Incident

An acceptance wrapper treated a child process exit code of `0` as a capability PASS even when the child emitted no structured acceptance result.

That proved only that the process exited successfully. It did not prove that the required capability had actually been observed.

## Failure Mode

- process exit code: `0`
- structured result: absent
- direct capability evidence: absent
- previous classification: PASS

## Correction

The wrapper was changed so that an evidence-bearing capability check becomes `NOT_VERIFIED` when the required structured observation is missing, unless the frozen contract explicitly permits exit-code-only verification (for example, a pure build/typecheck check).

## General Rule

> Process success is not capability success.

For evidence-bearing checks, PASS must be traceable to the observation required by the contract.
