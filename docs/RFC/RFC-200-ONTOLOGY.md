# RFC-200 Career Ontology

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define the ontology framework for reusable career knowledge objects.

## Responsibilities

- Standardize entities, properties, relationships, validation rules, examples, and JSON Schema references.
- Support Person, Resume, Experience, Skill, Competency, Project, Achievement, Certification, Employer, Industry, Role, Interview, Job, Salary, Language, Technology, Education, KPI, and Career Goal entities.

## Dependencies

- RFC-100 Career Kernel
- Documentation standard
- Schema registry

## Inputs

- Verified user facts
- External labor-market context
- Career goals

## Outputs

- Versioned ontology entities
- JSON Schemas
- Knowledge graph nodes and relationships

## Validation Rules

- Every entity requires an ID, properties, relationships, validation rules, examples, and JSON Schema.
- User-specific facts require provenance.
- Suggested facts must not be stored as verified facts until confirmed.

## Examples

- `skill:python` relates to `competency:data-analysis` and `experience:exp-001`.

## Test Cases

- Verify an entity without provenance fails validation when marked verified.

## Compatibility

Ontology schemas are versioned and should prefer additive changes.

## Security Considerations

Sensitive personal data must have explicit classification and retention controls.

## Explainability Considerations

Relationships must support explanation paths from recommendation to source facts.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial Sprint 2 ontology RFC draft. |
