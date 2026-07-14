# RFC-100 Career Kernel

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define the Career Kernel control-plane contract.

## Responsibilities

- Intent detection
- Workflow planning
- Context management
- Memory coordination
- Knowledge routing
- Reasoning orchestration
- Validation and quality gates
- Output approval

## Dependencies

- PRD-100 Career Kernel
- ADR-0001 Specification Driven Development
- Quality Gates Standard

## Inputs

- `KernelRequest`: user intent, session context, verified facts, constraints.
- `KnowledgePacket`: reusable knowledge objects and ontology references.
- `AgentManifest`: identity, capabilities, permissions, lifecycle, memory, events.
- `GatePolicy`: required validation gates for output type.

## Outputs

- `WorkflowPlan`: ordered steps, dependencies, tools, engines, and agents.
- `KernelEvent`: auditable lifecycle events.
- `ValidationReport`: gate outcomes and remediation guidance.
- `ApprovedOutput`: final artifact plus explanations and provenance.

## Validation Rules

- Agents communicate only through Kernel events and requests.
- Each recommendation must cite supporting facts or be labeled as a suggestion.
- Output approval requires successful required gate checks.
- Kernel contracts must not expose provider-specific model details.

## Examples

```json
{
  "request_type": "resume.optimize",
  "facts_policy": "verified_only",
  "required_gates": ["truthfulness", "formatting", "ats", "recruiter"]
}
```

## Test Cases

- Direct agent-to-agent event is rejected.
- Provider adapter swap preserves Kernel request and response schemas.
- Missing evidence produces a clarification question instead of a fabricated claim.

## Compatibility

Kernel contracts are versioned and must support backward-compatible additions where possible.

## Security Considerations

The Kernel enforces least-privilege agent permissions and prevents unapproved memory writes.

## Explainability Considerations

Workflow plans and validation reports must preserve reasoning summaries and provenance without exposing private chain-of-thought.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial Sprint 1 Kernel RFC draft. |
