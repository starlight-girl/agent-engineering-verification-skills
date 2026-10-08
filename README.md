# Agent Engineering Verification Plugins v1.2.0

Free, open-source **ChatGPT / Codex compatible skills-only plugins**, with separate English and Chinese editions. Based on the original v1.1 operational contracts below.

免费开源的智能体工程质检插件，提供中文和英文两个独立版本。每版包含 11 项技能、2 份流程手册和 1 个项目工程质检员入口。中文版本提供中文操作指南和报告，保留完整英文原始契约。

[Download / 下载](https://github.com/starlight-girl/agent-engineering-verification-skills/releases/latest) · [Install / 安装说明](INSTALL.md) · [使用支持 / Support](SUPPORT.md) · [Privacy / 隐私](PRIVACY.md) · [Terms / 条款](TERMS.md)

```sh
codex plugin marketplace add starlight-girl/agent-engineering-verification-skills --ref v1.2.0
codex plugin add agent-verification-zh@agent-engineering-verification
```

For English: `codex plugin add agent-verification-en@agent-engineering-verification`.
Start a new chat after installing. Current hosts with plugin marketplace support are required.

**Publication status:** GitHub downloads and local marketplace distribution are separate from the universal OpenAI public directory. No approved directory listing is claimed. See [installation boundaries](INSTALL.md).

## Original skill pack v1.1

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
