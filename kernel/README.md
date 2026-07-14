# Career Kernel

**Version:** 0.1.0-alpha  
**Status:** Sprint 1 Active  
**Purpose:** Define the Career Kernel contract package for orchestration, validation, and output approval.

## Responsibilities

- Provide the control-plane boundary for CareerForge OS workflows.
- Convert user requests into auditable workflow plans.
- Route all agent and engine activity through Kernel-mediated events.
- Enforce quality gates before career intelligence artifacts are approved.

## Dependencies

- [PRD-100 Career Kernel](../docs/PRD/PRD-100-CAREER-KERNEL.md)
- [RFC-100 Career Kernel](../docs/RFC/RFC-100-KERNEL.md)
- [ADR-0002 Kernel-Mediated Agents](../docs/ADR/ADR-0002-KERNEL-MEDIATED-AGENTS.md)
- [Quality Gates Standard](../docs/Standards/QUALITY_GATES.md)

## Inputs

- User requests and session context.
- Verified user facts and external context.
- Agent manifests and engine contracts.
- Gate policies for the requested output type.

## Outputs

- Kernel requests.
- Workflow plans.
- Kernel events.
- Validation reports.
- Approved outputs with explanation and provenance metadata.

## Validation Rules

- Kernel contracts must remain provider-neutral and must not include model-specific fields.
- Agent invocations must be represented as Kernel events or workflow steps.
- Output approval requires a passed validation report for all required gates.
- Unknown or unsupported facts must be labeled as assumptions, suggestions, or clarification questions.

## Examples

- A resume optimization request becomes a `KernelRequest`, then a `WorkflowPlan`, then one or more `KernelEvent` records, and finally an `ApprovedOutput` only after validation gates pass.

## Test Cases

- Validate all Kernel JSON Schemas are syntactically valid JSON.
- Verify Kernel schema identifiers use the `careerforge.kernel` namespace.
- Verify approved output schemas require provenance and validation metadata.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Started Sprint 1 Kernel contract package. |
