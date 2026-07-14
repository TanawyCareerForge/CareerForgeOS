# PRD-200 Career Ontology

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define product requirements for the Career Ontology knowledge model.

## Responsibilities

- Define reusable career entities and relationships.
- Preserve provenance for user-specific facts.
- Separate verified facts, suggested facts, assumptions, and external context.
- Provide schema contracts that can be used by Kernel-mediated engines and agents.

## Dependencies

- RFC-100 Career Kernel
- RFC-200 Career Ontology
- Documentation standard
- Schema registry

## Users

- End users
- Developers
- Enterprise integrators
- Agent and engine authors

## Inputs

- Verified user facts
- User-confirmed career goals
- External labor-market context
- Kernel workflow requests

## Outputs

- Versioned ontology entities
- Validated JSON objects
- Relationship edges with explanation paths
- Provenance records for user-specific facts

## Functional Requirements

- The Ontology must expose provider-neutral JSON Schema contracts.
- The Ontology must require provenance for every entity marked as `verified`.
- The Ontology must distinguish `verified`, `suggested`, `assumption`, and `external_context` fact states.
- The Ontology must support relationship edges between entities without embedding model-provider details.
- The Ontology must include sensitivity classification for personal data.

## Non-Functional Requirements

- Schemas must prefer additive changes during `0.1.x` iterations.
- Entity identifiers must be stable within a user workspace.
- Relationship metadata must support explainability and audit trails.

## Validation Rules

- Reject verified user-specific facts without provenance.
- Reject ontology entities without an ID, entity type, schema version, fact state, and sensitivity classification.
- Reject relationships that do not include source, target, relationship type, and evidence metadata.

## Examples

- `skill:python` relates to `experience:exp-001` through a `demonstrated_by` relationship supported by resume evidence.

## Test Cases

- Verify all Ontology schemas use `careerforge.ontology.v0.1`.
- Verify verified entities require at least one provenance entry.
- Verify relationship schemas include explanation metadata.

## Success Metrics

- 100% of user-specific verified ontology entities include provenance.
- 100% of ontology relationships provide evidence suitable for explanation paths.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial Sprint 2 ontology PRD. |
