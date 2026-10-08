# Generalization Decisions

This public pack was distilled from real tool-using-agent engineering incidents and then anonymized and normalized for cross-project use.

## Promoted to universal core

A source pattern was promoted only when:

- its procedure did not depend on a project-specific class, path, capability ID, or product domain;
- its required evidence could be expressed in generic runtime terms;
- its false-positive traps were observed in real engineering work;
- its applicability boundary could be stated without overclaiming.

## Kept conditional

Frontend runtime truth verification is conditional because not every agent has a frontend/bridge/runtime chain.

External application safe startup/recovery is conditional because not every agent controls a separate process with readiness and shutdown semantics.

## Kept as playbooks

Final candidate freeze and independent audit adjudication coordinate multiple checks rather than acting as single atomic verification skills.

## Not generalized

The public pack deliberately does not define:

- a universal recovery algorithm;
- a universal proof-of-concept threshold;
- a universal persistence/repository architecture;
- product-specific plugin/provider maturity rules;
- full visual correctness for arbitrary UIs;
- complete restart persistence for arbitrary multi-tool workflows.

Those claims require project-specific contracts or broader evidence than the source incidents provide.
