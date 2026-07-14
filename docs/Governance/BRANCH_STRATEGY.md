# Branch Strategy

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define branch naming and flow.

## Responsibilities

- Isolate work by purpose.
- Support stable releases and parallel development.

## Dependencies

- Release strategy
- Versioning standard

## Inputs

- Feature work
- Release preparation
- Hotfixes

## Outputs

- Mainline commits
- Feature branches
- Release branches

## Validation Rules

- `main` contains stable released history.
- `develop` integrates approved upcoming work.
- `release/*` prepares release candidates.
- `feature/*` contains scoped feature work.

## Required Initial Branches

- `main`
- `develop`
- `release/v0.1.0-alpha`
- `feature/bootstrap`
- `feature/kernel`
- `feature/ontology`
- `feature/sdk`
- `feature/resumeforge`

## Examples

- `feature/kernel` contains Sprint 1 kernel specification work.

## Test Cases

- Verify branch names match the allowed prefixes.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial branch strategy. |
