# RFC-300 Resume Intelligence

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define the Resume Intelligence specification framework for truth-first resume artifacts.

## Responsibilities

- Standardize resume draft sections, recommendations, gap questions, validation metadata, examples, and JSON Schema references.
- Connect resume content to Career Ontology entities and Kernel quality gates.
- Support explainable resume improvement without fabricating user facts.

## Dependencies

- RFC-100 Career Kernel
- RFC-200 Career Ontology
- Documentation standard
- Schema registry

## Inputs

- Kernel workflow requests
- Career ontology entities and relationships
- Existing resume evidence
- Target role and job description context
- User constraints and preferences

## Outputs

- Resume draft schema objects
- Resume recommendation schema objects
- Gap questions for missing evidence
- Validation-ready resume artifacts

## Validation Rules

- Every verified resume claim requires source ontology entities and provenance references.
- Suggested wording must not change the underlying fact state.
- Assumptions must be clearly labeled and routed for user confirmation before approval.
- Recommendations must include explanation metadata and an improvement category.

## Examples

- A bullet can be rewritten for clarity only when the source claim remains tied to the same verified ontology entity.
- If a job description requests a certification absent from verified facts, the engine should identify a gap rather than claim the certification.

## Test Cases

- Verify verified draft sections cannot omit provenance references.
- Verify recommendation objects include source entity IDs, recommendation type, rationale, and expected impact.

## Compatibility

Resume schemas are versioned and should prefer additive changes during the `0.1.x` line.

## Security Considerations

Resume artifacts may contain personal and sensitive personal data. Implementations must retain sensitivity classifications and avoid unnecessary disclosure.

## Explainability Considerations

Every generated section and recommendation must provide a trace from output text to source facts, evidence, and rationale.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial Sprint 3 resume intelligence RFC draft. |
