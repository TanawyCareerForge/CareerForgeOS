# PRD-100 Career Kernel

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define product requirements for the Career Kernel.

## Responsibilities

- Detect user intent.
- Plan workflows.
- Manage context and memory.
- Route knowledge and engine calls.
- Coordinate reasoning, validation, quality gates, and output approval.

## Dependencies

- Architecture
- Quality gates standard
- Agent protocol RFC
- Ontology specification

## Users

- End users
- Developers
- Enterprise integrators
- Plugin authors

## Inputs

- User request
- Verified user facts
- Career ontology objects
- Agent capabilities
- Engine contracts
- Quality-gate policies

## Outputs

- Workflow plan
- Agent and engine invocation requests
- Validation results
- Approved career intelligence artifact
- Explanation and audit trail

## Functional Requirements

- The Kernel must be the only communication path between agents.
- The Kernel must separate facts, assumptions, suggestions, and external context.
- The Kernel must approve outputs only after required validation gates complete.
- The Kernel must expose model-agnostic interfaces.

## Non-Functional Requirements

- Deterministic audit trails for all orchestration decisions.
- Provider-neutral model adapter boundary.
- Extensible plugin registry.

## Validation Rules

- Reject direct agent-to-agent communication.
- Block fabricated user facts.
- Require explanation metadata for recommendations.

## Examples

- For a resume optimization request, the Kernel detects intent, loads verified experience facts, routes work to the resume engine, runs truthfulness and formatting gates, and returns approved suggestions.

## Test Cases

- Verify unknown facts are marked as assumptions or questions.
- Verify failed truthfulness gate prevents output approval.
- Verify replacing a model provider does not change workflow contract shape.

## Success Metrics

- 100% of agent invocations pass through Kernel contracts.
- 100% of approved AI recommendations include explanations.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial Sprint 1 kernel PRD. |
