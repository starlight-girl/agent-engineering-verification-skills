# Standard Skill Contract

Every reusable skill in this pack follows the same operational shape.

## Required fields

- **skill_id** — stable identifier
- **type** — verifier / diagnostic / builder
- **applicability** — where the skill is valid
- **trigger** — when to invoke it
- **required_inputs** — facts or artifacts needed before execution
- **preconditions** — conditions that must be known or frozen first
- **procedure** — ordered execution steps
- **required_evidence** — what must exist before a positive claim is allowed
- **failure_classification** — how unsupported or contradictory outcomes are represented
- **false_positive_traps** — common ways a test can appear green without proving the claim
- **success_criteria** — explicit completion gate
- **non_goals** — what the skill does not prove
- **handoff** — what to do next if the skill cannot conclude
- **provenance_boundary** — what was actually supported by the source evidence

## Design rules

1. A skill must be operational, not motivational prose.
2. A skill must not invent facts that are unavailable from the system under test.
3. A verifier must not become the co-executor of the production behavior it is trying to prove.
4. Project-specific implementation names belong in provenance or case studies, not in the generic procedure.
5. Missing evidence fails closed to an honest status such as `NOT_VERIFIED`, `BLOCKED`, `DEPENDENCY_MISSING`, or the project’s frozen equivalent.
6. A skill may be deterministic in procedure while still depending on runtime observation.
7. A project may map the generic statuses into its own canonical vocabulary, but must preserve the semantic distinctions.
