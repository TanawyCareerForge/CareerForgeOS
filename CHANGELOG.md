# Changelog

All notable changes to CareerForge OS will be documented in this file.


**Version:** 0.1.0-alpha  
**Status:** Active  
**Purpose:** Track notable repository, specification, governance, and release changes.

## Responsibilities

- Record notable changes by release.
- Support release auditability.
- Identify documentation, governance, and specification additions.

## Dependencies

- Release strategy
- Versioning standard

## Inputs

- Merged commits
- Release scope
- Maintainer release notes

## Outputs

- Release change summary
- Historical audit record

## Validation Rules

- Released changes must be grouped by version and date.
- User-visible and governance changes must be recorded.

## Examples

- Sprint 0 bootstrap changes are grouped under `0.1.0-alpha`.

## Test Cases

- Verify the current release has a dated changelog section.


## [0.1.0-alpha] - 2026-07-14

### Added

- Bootstrapped CareerForge OS repository structure.
- Added project vision, mission, architecture, and roadmap.
- Added repository governance, contribution, security, code of conduct, branch, and release strategy documents.
- Added GitHub issue and pull request templates.
- Added RFC, ADR, and PRD frameworks with Sprint 0 bootstrap PRD.
- Added documentation, naming, testing, versioning, and quality gate standards.
- Added Sprint 1 Career Kernel PRD, RFC, and kernel-mediated agents ADR.
- Added initial Sprint 2 Career Ontology RFC draft.
- Added v0.1.0-alpha release manifest.

- Started Sprint 1 by adding the Career Kernel contract package.
- Added provider-neutral KernelRequest, WorkflowPlan, and ApprovedOutput JSON Schemas.
- Added schema validation tests for Kernel namespace, provider neutrality, and approved-output metadata.

- Started Sprint 2 by adding the Career Ontology specification package.
- Added Sprint 2 Career Ontology PRD.
- Added provider-neutral OntologyEntity and OntologyRelationship JSON Schemas.
- Added schema validation tests for Ontology versioning, provenance, and explanation metadata.

- Started Sprint 3 by adding the Resume Intelligence specification package.
- Added Sprint 3 Resume Intelligence PRD and RFC drafts.
- Added provider-neutral ResumeSection and ResumeRecommendation JSON Schemas.
- Added schema validation tests for Resume provenance, source references, explanations, and provider neutrality.


## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial Sprint 0 changelog. |
