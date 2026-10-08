# Skill Classification

## Universal core

These skills are broadly reusable across tool-using Agent projects:

- Reality-Grounded Acceptance
- False-Green Detection
- Production-Path Verification
- Artifact/Evidence Integrity
- Approval/Resume Verification
- Process Lifecycle Verification
- Dependency Truth Verification
- Candidate Identity Verification
- Environment-vs-Code Diagnosis

They still require project-specific requirements, identity fields, and evidence sources.

## Conditional generic

These are reusable only when the relevant architecture exists:

- Frontend Runtime Truth Verification — for renderer/UI → bridge → backend/runtime chains.
- External Application Safe Startup & Recovery — for external processes/apps controlled by the Agent.

## Playbooks, not atomic skills

- Final Candidate Freeze
- Independent Audit Adjudication

These coordinate multiple skills and release/audit steps. They are intentionally not registered as runtime capabilities.

## Case studies, not skills

The source incidents remain evidence and examples. They should not be imported as generic rules without the applicability boundary.

## Not generalized

The source evidence was insufficient to create the following as universal skills:

- Universal POC sufficiency criteria
- Full product-page visual verification
- Complete multi-tool restart-persistence verification
- Universal workflow recovery
- Universal provider/plugin production-whitelist criteria
- a project-specific repository/persistence model as a universal architecture

Keeping these out is intentional. The pack prefers an explicit gap over fake generalization.
