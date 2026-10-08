# Candidate Identity Verification

- **skill_id**: `agent.verify.candidate-identity.v1`
- **type**: verifier
- **applicability**: final audit, release, handoff, dirty-tree acceptance

## Trigger

Invoke when evidence must be tied to an exact build/source candidate.

## Required inputs

- candidate manifest or equivalent identity record
- VCS/working-tree state
- artifact directory or immutable run reference
- build identity, timestamps or hashes
- handoff/release pointer

## Preconditions

There is an explicit freeze point.

## Procedure

1. Resolve the exact candidate identity.
2. Resolve the exact acceptance artifact tied to it.
3. Compare manifest counts and identities with artifact contents.
4. Classify every dirty/uncommitted file relevant to the candidate.
5. Detect source or build changes after the acceptance run.
6. Verify handoff/release documents point to the same candidate.
7. Reject “latest folder” or moving HEAD as a substitute for explicit identity when they are ambiguous.

## Required evidence

Machine-readable candidate identity plus a complete acceptance artifact.

## Failure signatures

- HEAD used to represent uncommitted source content
- newest directory assumed to be final
- artifact predates relevant source changes
- dirty files are unclassified
- handoff points to superseded artifact

## Success criteria

One unambiguous candidate maps to one complete, current evidence package.

## Non-goals

This skill does not validate feature behavior itself.

## Handoff

If identity is ambiguous, freeze a new candidate and rerun acceptance.

## Provenance boundary

Derived from real candidate-identity ambiguity and an explicit candidate-manifest freeze process.
