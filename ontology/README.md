# Career Ontology

**Version:** 0.1.0-alpha  
**Status:** Sprint 2 Active  
**Purpose:** Define reusable career knowledge entities, relationships, provenance rules, and JSON Schema contracts.

## Responsibilities

- Maintain the canonical entity and relationship vocabulary for CareerForge OS.
- Preserve truth-first provenance for user-specific career facts.
- Support explainable relationship paths between career data, recommendations, and source evidence.

## Dependencies

- [PRD-200 Career Ontology](../docs/PRD/PRD-200-CAREER-ONTOLOGY.md)
- [RFC-200 Career Ontology](../docs/RFC/RFC-200-ONTOLOGY.md)
- [RFC-100 Career Kernel](../docs/RFC/RFC-100-KERNEL.md)
- [Documentation Standard](../docs/Standards/DOCUMENTATION_STANDARD.md)

## Inputs

- Verified user facts
- Suggested facts awaiting confirmation
- External labor-market context
- Career goals and constraints

## Outputs

- Versioned ontology schemas
- Entity and relationship validation contracts
- Explanation-ready knowledge graph records

## Validation Rules

- Verified entities require provenance.
- Suggested facts must remain distinct from verified facts until user confirmation.
- Relationships must include evidence and explanation metadata.

## Examples

- A `skill` entity for Python can be connected to an `experience` entity using a `demonstrated_by` relationship.

## Test Cases

- Validate ontology schemas as JSON Schema draft 2020-12 documents.
- Validate fact-state and provenance requirements.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Started Sprint 2 ontology package. |
