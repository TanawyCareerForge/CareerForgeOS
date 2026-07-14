# Repository Governance

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define governance for maintainers, decisions, reviews, and releases.

## Responsibilities

- Maintain specification quality.
- Enforce review and quality gates.
- Protect the architecture from unapproved coupling.

## Dependencies

- Contributing guide
- Standards
- RFC, ADR, and PRD frameworks

## Inputs

- Issues
- Pull requests
- RFCs
- ADRs
- PRDs

## Outputs

- Accepted changes
- Rejected changes with rationale
- Release approvals

## Validation Rules

- Architectural decisions require ADR coverage.
- Protocol or contract changes require RFC coverage.
- Product behavior changes require PRD coverage.

## Examples

- A model-provider adapter contract change requires an RFC and ADR.

## Test Cases

- Verify every major change links to the correct specification type.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial governance document. |
