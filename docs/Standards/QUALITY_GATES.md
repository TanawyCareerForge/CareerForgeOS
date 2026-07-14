# Quality Gates Standard

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define the quality gates every CareerForge OS output may pass through.

## Responsibilities

- Protect users from false, confusing, or harmful outputs.
- Provide explainable validation results.

## Dependencies

- Career Kernel
- Testing standard
- Ontology schemas

## Inputs

- Candidate output
- Source facts
- Target context
- Applicable policies

## Outputs

- Gate decisions
- Findings
- Remediation guidance

## Validation Rules

- Truthfulness gate must block fabricated user claims.
- Consistency gate must detect contradictions across artifacts.
- Compliance gate must flag policy and legal concerns.
- Formatting gate must ensure target-specific structure.

## Examples

- A resume bullet claiming a quantified result without source evidence is marked as a suggestion requiring user confirmation.

## Test Cases

- Verify unverifiable claims are not approved as facts.
- Verify failed gates return actionable explanations.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial quality gates standard. |
