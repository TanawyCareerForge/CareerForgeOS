# Resume Intelligence Engine

**Version:** 0.1.0-alpha  
**Status:** Specification Draft  
**Purpose:** Define the future Resume Intelligence engine boundary for truth-first, explainable resume artifacts.

## Responsibilities

- Consume Career Kernel requests and Career Ontology facts.
- Generate resume draft sections, recommendations, and gap questions.
- Preserve provenance, fact state, sensitivity, and explanation metadata.
- Prepare artifacts for Kernel quality gates before output approval.

## Dependencies

- [PRD-300 Resume Intelligence](../../docs/PRD/PRD-300-RESUME-INTELLIGENCE.md)
- [RFC-300 Resume Intelligence](../../docs/RFC/RFC-300-RESUME-INTELLIGENCE.md)
- [RFC-100 Career Kernel](../../docs/RFC/RFC-100-KERNEL.md)
- [RFC-200 Career Ontology](../../docs/RFC/RFC-200-ONTOLOGY.md)

## Inputs

- Kernel workflow plan
- Ontology entities and relationships
- Existing resume evidence
- Target role and user constraints

## Outputs

- Resume draft section objects
- Resume recommendation objects
- Gap questions for missing evidence
- Validation-ready resume artifacts

## Validation Rules

- Verified claims require source ontology entities and provenance references.
- Recommendations must include rationale, expected impact, and source entity IDs.
- Missing facts must become gap questions instead of fabricated resume content.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial Sprint 3 Resume Intelligence engine specification package. |
