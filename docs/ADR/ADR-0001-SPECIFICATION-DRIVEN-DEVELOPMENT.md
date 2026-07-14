# ADR-0001 Specification Driven Development

**Version:** 0.1.0-alpha  
**Status:** Accepted  
**Purpose:** Establish Specification Driven Development as the required delivery methodology.

## Responsibilities

- Require product intent before architecture and implementation.
- Ensure decisions and interfaces are documented.
- Keep tests, examples, and documentation synchronized.

## Dependencies

- PRD framework
- RFC framework
- Testing standard

## Inputs

- Product requirements
- Architectural constraints
- Interface proposals

## Outputs

- PRDs
- ADRs
- RFCs
- Implementation plans

## Context

CareerForge OS includes AI systems that affect career outcomes, so behavior must be explainable, reviewable, and auditable.

## Decision

All major features follow: PRD → ADR → RFC → Implementation → Tests → Examples → Documentation → Release.

## Consequences

- Slower initial development.
- Better auditability, maintainability, and product coherence.

## Alternatives Considered

- Code-first delivery was rejected because it risks undocumented AI behavior and hidden coupling.

## Validation Rules

- Major feature PRs must reference their PRD, ADR, and RFC.

## Examples

- Career Kernel work begins with a kernel PRD, then ADRs for orchestration decisions, then RFC-100 contracts.

## Test Cases

- Verify feature PRs include specification links.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial accepted ADR. |
