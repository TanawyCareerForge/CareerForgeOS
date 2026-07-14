# ADR-0002 Kernel-Mediated Agents

**Version:** 0.1.0-alpha  
**Status:** Accepted  
**Purpose:** Decide that all agents communicate only through the Career Kernel.

## Responsibilities

- Prevent hidden coupling between agents.
- Centralize permission checks, validation, memory, and audit trails.

## Dependencies

- RFC-100 Career Kernel
- Agent protocol
- Quality gates standard

## Inputs

- Agent events
- Agent capability declarations
- Kernel workflow plans

## Outputs

- Audited Kernel-mediated agent invocations
- Validation reports

## Context

CareerForge OS will support many independent agents and plugins. Direct agent communication would make security, explainability, and validation difficult to enforce.

## Decision

Agents must communicate only by emitting events to and receiving tasks from the Career Kernel.

## Consequences

- Stronger governance and auditability.
- Slightly more orchestration overhead.
- Easier plugin isolation and permission enforcement.

## Alternatives Considered

- Direct agent message bus was rejected because it weakens validation and audit controls.

## Validation Rules

- Agent manifests must not declare direct peer channels.
- Tests must reject direct agent-to-agent invocation attempts.

## Examples

- Interview agent requests resume context through the Kernel, not from the resume agent.

## Test Cases

- Verify peer-to-peer agent events are invalid.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial accepted ADR. |
