---
name: fullstack-blueprint
license: MIT
description: Use when starting, designing, or building a new fullstack project, or adding features or checking engineering conventions in a project already using this blueprint. Provides a recommended React/Python starting standard for beginners. Excludes unrelated existing-project refactoring or framework adaptation, current-code explanations, prose-only edits, and standalone scripts or algorithms. Explicit invocation keeps the user's requested scope.
---

# Fullstack Project Blueprint

Help a beginner turn a business idea into a small, runnable fullstack project using reusable engineering experience. Use one recommended React/Python baseline; let real business responsibilities determine how much structure is needed. The user supplies business intent; the assistant handles technical choices and explains their practical effect.

## Scope and Working Context

Apply this skill to new projects and continued work in projects already built with this blueprint. Confirm that relationship from the request or target-project evidence. An unrelated existing repository is not an implicit trigger. Explicit invocation for an explanation or review stays within that request and does not authorize migration or implementation.

Read instructions and evidence for the target directory only. When creating a separate project, do not carry over another project's naming, tables, runtime versions, or check commands. Explicit user requirements take precedence over defaults; raise conflicts that prevent correct work rather than silently overwriting files or changing agreed contracts.

## From Idea to a Working Feature

Use the stages relevant to the requested deliverable. Design ends with a proposal and future acceptance criteria; review checks evidence without implementing.

1. **Understand the business:** Establish who uses the application, the main operation, necessary permissions, and what successful completion means. Ask only blocking questions; label other assumptions. Do not require a beginner to choose architecture patterns or middleware.
2. **Recommend the foundation:** Use [project-baseline.md](references/project-baseline.md). Explain the relevant modules and frontend/backend calls in plain language. Start with one frontend and one modular backend; advanced patterns are considered only for demonstrated needs.
3. **Build the minimum structure:** When implementation is requested, establish configuration validation, logging, and resource lifecycle, then add only files needed for the first feature. A design-only request delivers a proposal, optionally in a design document; it does not authorize application scaffolding, dependencies, or business code. A review-only request leaves files unchanged.
4. **Connect a real feature:** During implementation, connect one user operation through the page, named API function, backend business operation, and required persistence. Write tests before business behavior changes; verify success, rejection, and relevant failures. Health endpoints and static mock pages alone do not complete a requested working application.
5. **Make it usable:** For an implementation handoff, follow the [first-run acceptance criteria](references/project-baseline.md#first-run-acceptance). Provide prerequisites, copyable setup/start/check commands, the browser address, a concrete operation with its expected result, and verified results or actual blockers. When adding later features, check only affected behavior and update the same project instructions.

Scale output to the task: a short design for a small idea, focused changes for one feature, and evidence-backed findings for a review. Keep necessary engineering reasoning available without presenting a catalogue of patterns or a long questionnaire to the user. Use the user's requested language, or the request's language when unspecified; follow maintained-document conventions and preserve exact identifiers.

## Engineering Rules

- Organize by business capability. Keep feature UI, state, helpers and private styles together; share only actual cross-feature capabilities. Give each layer a real responsibility; simple functions and concrete dependencies are valid.
- Use the baseline's central API directory and shared client, same-origin `/api/v1/...`, strict backend inputs, YAML configuration, logging, and explicit resource lifecycle. Read the relevant reference before changing that concern. Add persistence and middleware only for a business need, and explain the choice.
- Keep permissions, state rules, transaction ownership, failure handling and frontend feedback consistent across a feature. Describe runtime calls separately from source imports when explaining a boundary. Use the [architecture reference](references/architecture.md) for boundary decisions or actual complexity, rather than for every local edit.
- When Superpowers is available, its applicable skills govern the current phase; this skill supplies the project standards. Reuse settled business decisions, approved plans and verification records, honor outstanding gates, and avoid duplicate workflows or confirmations. Without Superpowers, this skill works independently. Diagnose failures before fixing them and base completion claims on actual checks.

## Documentation and Implementation Stay Together

Locate affected README sections, design/API explanations, configuration examples and comments. Resolve discrepancies using confirmed requirements, contracts, implementation and tests; neither old documentation nor passing tests alone establishes correctness. Update current explanations in the same change when behavior, boundaries, interfaces, permissions, errors, configuration, logging or startup changes. For an internal-only change, explain why current instructions remain accurate.

Mark proposed designs as unimplemented and preserve historical facts when adding current guidance. Check each change against implementation/test evidence and the current documentation location, including executable examples where appropriate. Report real verification limits; do not call a feature complete while its current instructions contradict it. Commits and external publication require authorization from the task.

## References on Demand

| Concern | Read |
|---|---|
| New-project starting point and first-run handoff | [project-baseline.md](references/project-baseline.md) |
| Module ownership, dependency boundaries, or complex rules/transactions | [architecture.md](references/architecture.md) |
| Pages, components, state, or styles | [frontend.md](references/frontend.md) |
| Python business modules, data access, transactions, or middleware | [backend.md](references/backend.md) |
| API definitions, integration, failures, or repeated submissions | [http.md](references/http.md) |
| Backend calls to third-party APIs, including response-code-based retries | [Third-Party API Retries](references/http.md#third-party-api-retries) |
| Logs and exception recording | [logging-config.md: Logging Lifecycle](references/logging-config.md#logging-lifecycle) |
| YAML settings, startup, or proxy configuration | [logging-config.md: Configuration Lifecycle](references/logging-config.md#configuration-lifecycle) |

Read only sections needed for the task. A local style or field change does not require the whole architecture or startup guide. Read [sources.md](references/sources.md) only for provenance.
