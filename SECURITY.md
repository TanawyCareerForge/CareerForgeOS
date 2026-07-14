# Security Policy

**Version:** 0.1.0-alpha  
**Status:** Draft  
**Purpose:** Define responsible disclosure and security expectations.

## Responsibilities

- Protect user career data and sensitive professional information.
- Report vulnerabilities responsibly.
- Design for auditability, least privilege, and secure defaults.

## Dependencies

- Governance framework
- Agent protocol
- Kernel validation model

## Inputs

- Vulnerability reports
- Threat models
- Dependency alerts

## Outputs

- Security advisories
- Patches
- Disclosure notes

## Validation Rules

- Do not disclose exploitable vulnerabilities publicly before maintainers can triage.
- Sensitive user data must not be committed to the repository.
- Agents must operate under explicit permissions.

## Examples

- Report prompt-injection bypasses that can alter validated career facts.

## Test Cases

- Verify security issues are triaged and linked to remediation commits.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial security policy. |
