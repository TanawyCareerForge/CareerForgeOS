# PRD-300 Resume Intelligence

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define product requirements for the Resume Intelligence engine.

## Responsibilities

- Transform verified career ontology facts into resume-ready draft sections.
- Preserve truth-state labels, provenance, and explanation metadata for every recommendation.
- Separate content extraction, resume structuring, optimization suggestions, and approval readiness.
- Provide provider-neutral schema contracts for Kernel-mediated resume workflows.

## Dependencies

- RFC-100 Career Kernel
- RFC-200 Career Ontology
- RFC-300 Resume Intelligence
- Quality gates standard
- Documentation standard
- Schema registry

## Users

- End users
- Developers
- Resume engine authors
- Enterprise integrators
- Recruiter and ATS intelligence engines

## Inputs

- Verified ontology entities and relationships
- User-selected target role, seniority, geography, and constraints
- Existing resume text or uploaded document evidence
- External job description context
- Kernel workflow request and facts policy

## Outputs

- Versioned resume draft sections
- Resume recommendations with rationale and source facts
- Gap questions for missing or unverifiable information
- Validation-ready artifacts for truthfulness, consistency, formatting, ATS, recruiter, and grammar gates

## Functional Requirements

- The Resume Intelligence engine must consume ontology entities instead of unstructured user claims when verified facts are required.
- The engine must label each draft section as `verified`, `suggested`, `assumption`, or `external_context`.
- The engine must require provenance references for verified resume claims.
- The engine must produce recommendations without fabricating employers, dates, credentials, metrics, or responsibilities.
- The engine must explain why each recommendation improves clarity, relevance, impact, or formatting.
- The engine must produce gap questions when required facts are missing.

## Non-Functional Requirements

- Resume schemas must remain provider-neutral and compatible with Kernel workflows.
- Draft outputs must be deterministic enough for audit and review.
- Resume artifacts must support additive schema evolution during `0.1.x` iterations.
- Sensitive personal data must retain ontology sensitivity classifications.

## Validation Rules

- Reject verified resume claims that do not reference ontology entities and provenance.
- Reject draft sections without a section type, fact state, content, source entity references, and explanation metadata.
- Reject recommendations that introduce unverified facts without labeling them as assumptions or questions.
- Reject approved resume artifacts until required Kernel quality gates pass.

## Examples

- A verified `experience:exp-001` entity can generate a work-experience bullet when its employer, role, date range, and evidence are preserved in the draft section metadata.
- A missing metric should create a gap question instead of inventing quantified impact.

## Test Cases

- Verify all Resume schemas use `careerforge.resume.v0.1`.
- Verify verified resume sections require at least one provenance reference.
- Verify resume recommendations include explanations and source entity IDs.
- Verify schema text remains provider-neutral.

## Success Metrics

- 100% of verified resume claims reference ontology source entities.
- 100% of recommendations include rationale and improvement category.
- 0 fabricated employers, dates, credentials, or metrics in approved resume artifacts.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial Sprint 3 resume intelligence PRD. |
