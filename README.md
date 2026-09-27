# Agent Engineering Verification Skill Pack v1.1

A reusable, evidence-grounded skill pack for building and independently verifying tool-using AI agents.

The public edition is anonymized and normalized so that the **core skills do not depend on any private project name, repository path, class name, capability ID, or product-domain assumption**.

## What this pack is

It is a set of operational contracts that an engineering Agent, auditor Agent, QA Agent, or human engineer can apply directly.

It is **not**:
- a runtime Skill registry,
- an autonomous Agent framework,
- a replacement for project-specific requirements,
- a guarantee that a generic rule applies outside its stated boundary.

## Classification

### Core universal skills

1. `agent.verify.reality-grounded-acceptance.v1`
2. `agent.verify.false-green.v1`
3. `agent.verify.production-path.v1`
4. `agent.verify.artifact-integrity.v1`
5. `agent.verify.approval-resume.v1`
6. `agent.verify.process-lifecycle.v1`
7. `agent.verify.dependency-truth.v1`
8. `agent.verify.candidate-identity.v1`
9. `agent.diagnose.environment-vs-code.v1`

### Conditional skills

10. `agent.verify.frontend-runtime-truth.v1` — use when a frontend/bridge/runtime chain is in scope.
11. `agent.build.external-app-safe-startup.v1` — use when an Agent controls an external process/app with readiness and shutdown semantics.

### Playbooks

- Final Candidate Freeze
- Independent Audit Adjudication

### Composite verifier role

- Agent Engineering Inspector / 项目工程质检员

## Core principle

> Test Execution ≠ Observed Reality ≠ Requirement Status

A test process that exits successfully has only proved that the test process exited successfully. Capability claims must be derived from direct evidence at the level required by the frozen contract.

## Recommended use

For a new project:

1. Freeze the exact requirement and candidate identity.
2. Select only the skills whose applicability conditions match the project.
3. Run the skill procedure without modifying the system under test merely to make the test pass.
4. Collect the required evidence.
5. Classify unsupported claims conservatively.
6. Use the Inspector role to combine multiple skills into an audit.

See:
- `STANDARD_SKILL_CONTRACT.md`
- `SKILL_CLASSIFICATION.md`
- `skill-index.json`
- `roles/agent-engineering-inspector.md`

## Evidence boundary

The pack deliberately does **not** claim universal coverage for:
- what counts as a sufficient POC,
- full visual correctness of every product UI,
- restart persistence of a complete multi-tool workflow,
- a universal recovery algorithm,
- arbitrary provider/plugin production maturity.

Those were not fully proven by the source evidence and remain project-specific or future work.
