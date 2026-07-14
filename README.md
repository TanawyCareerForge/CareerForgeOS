# CareerForge OS

**Version:** 0.1.0-alpha  
**Status:** Sprint 0 Bootstrap  
**Purpose:** CareerForge OS is an AI-native Career Intelligence Operating System for explainable, truth-first professional intelligence.

CareerForge OS is not a resume generator. It is a model-agnostic open-source ecosystem for career intelligence, including resume intelligence, ATS intelligence, recruiter intelligence, LinkedIn intelligence, cover letter intelligence, interview intelligence, career coaching, skill-gap analysis, Career DNA, Career Twin, knowledge graph, enterprise APIs, AI agents, SDKs, and a plugin marketplace.

## Principles

- **Truth First:** Never fabricate user information.
- **Explainable AI:** Every recommendation must be traceable and explainable.
- **Human First:** Optimize for humans first, ATS second, recruiters third.
- **Modular Design:** Every engine is independent and every agent is a plugin.
- **Enterprise Maintainability:** Single responsibility, documented interfaces, versioned specifications.

## Repository Structure

```text
careerforge/
  docs/                 Specifications, governance, standards, RFCs, ADRs, PRDs
  kernel/               Career Kernel specifications and future implementation
  ontology/             Career ontology specifications and schemas
  agents/               Agent protocol and plugin agents
  engines/              Independent intelligence engines
  sdk/                  Developer SDKs
  knowledge/            Reusable knowledge objects
  schemas/              JSON Schemas and validation contracts
  templates/            Document and output templates
  tests/                Specification, validation, and future code tests
  examples/             Reference examples
  benchmarks/           Evaluation benchmarks
  api/                  Enterprise API contracts
  cli/                  Command-line interface
  ui/                   User interfaces
  releases/             Release manifests and notes
```

## Development Methodology

CareerForge OS uses Specification Driven Development:

**PRD → ADR → RFC → Implementation → Tests → Examples → Documentation → Release**

## Sprint Roadmap

- **Sprint 0:** Repository bootstrap, governance, standards, and specification framework.
- **Sprint 1:** Career Kernel specification.
- **Sprint 2:** Career Ontology specification.
- **Sprint 3:** Resume Intelligence specification.

## Model Agnosticism

CareerForge OS must remain compatible with Claude, GPT, Gemini, Llama, Mistral, DeepSeek, Qwen, and future models through provider-neutral interfaces.

## License

MIT License. See [LICENSE](LICENSE).


## Responsibilities

- Provide the top-level entry point for CareerForge OS contributors, users, and evaluators.
- Summarize the operating system vision, principles, repository layout, and delivery methodology.

## Dependencies

- [VISION.md](VISION.md)
- [MISSION.md](MISSION.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [ROADMAP.md](ROADMAP.md)

## Inputs

- Project vision
- Engineering principles
- Repository standards
- Sprint roadmap

## Outputs

- Contributor orientation
- Repository navigation guidance
- Links to governance and standards

## Validation Rules

- README content must remain aligned with architecture, roadmap, and governance documents.
- Claims about capabilities must distinguish current repository state from future roadmap goals.

## Examples

- A contributor starts with this README, then follows the PRD, ADR, and RFC workflow before implementing a feature.

## Test Cases

- Verify listed top-level directories exist.
- Verify linked governance and standards documents exist.

## Revision History

| Version | Date | Notes |
| --- | --- | --- |
| 0.1.0-alpha | 2026-07-14 | Initial Sprint 0 README. |
