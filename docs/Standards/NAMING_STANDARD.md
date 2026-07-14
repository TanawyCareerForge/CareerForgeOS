# Naming Standard

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define names for files, directories, branches, specifications, and modules.

## Responsibilities

- Keep names predictable.
- Make generated and human-authored assets easy to locate.

## Dependencies

- Branch strategy
- RFC framework

## Inputs

- Module names
- Specification numbers
- Release versions

## Outputs

- Consistent repository names
- Consistent specification identifiers

## Validation Rules

- Directories use lowercase kebab-case only when new multiword directories are needed.
- RFC files use `RFC-NNN-TITLE.md`.
- ADR files use `ADR-NNNN-TITLE.md`.
- PRD files use `PRD-NNN-TITLE.md`.
- Branches use `feature/*`, `release/*`, `hotfix/*`, `docs/*`, or approved long-lived names.

## Examples

- `docs/RFC/RFC-100-KERNEL.md`
- `feature/ontology`

## Test Cases

- Verify new specification file names match their pattern.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial naming standard. |
