---
name: fullstack-blueprint
license: MIT
description: Use when starting a fullstack project, or building, changing, designing, or reviewing application architecture, frontend pages/components, backend APIs/business modules, middleware integration, module layering, frontend-to-backend calls, application logging, YAML configuration, or consistency between business documentation and implementation. Excludes unrelated prose or typo-only edits, pure algorithms, standalone scripts unrelated to these concerns, and non-software tasks.
---

# Fullstack Engineering Blueprint

Apply a fullstack engineering blueprint for design, implementation, and review: defaults for new projects, module responsibilities, dependency directions, and engineering conventions.

Use the smallest sufficient structure to make responsibilities, dependencies, and failure handling explicit. Explicit user requirements take priority; otherwise, preserve project naming, public entry points, logging formats, and quality gates.

## Usage and Deliverables

Identify whether the request is design, review, or implementation, and determine its scope from the request and confirmed context. Ask only when missing information prevents correct work. Read applicable AGENTS.md files, relevant current documentation, implementation, contracts, and tests; load references using the table below. Distinguish facts, constraints, and recommendations, and state assumptions where evidence is incomplete.

| Task | Work and output |
|---|---|
| Design | Explain choices, necessary module responsibilities and dependencies, behavior contracts, and acceptance criteria; implement business code only as requested by the user |
| Review | Rank findings by impact and provide locations/evidence, consequences, and minimal recommendations; distinguish violations, optional improvements, and unverified concerns, and report honestly when there are no findings; do not edit files |
| Implementation | Complete authorized changes and check the affected responsibilities, dependencies, contracts, and failure handling; report actual changes, necessary tradeoffs, documentation updates or reasons none are needed, verification performed, and unverified areas |

Use the user's requested language, or the language of their request when unspecified. Follow established project language conventions for maintained documents, and preserve exact identifiers. A few sentences suffice for a local task; do not impose a full set of headings. Label relationships as runtime calls or source dependencies and show only relevant parts. Design and review do not by themselves authorize scaffolding, dependency installation, or code commits.

## Core Constraints

- Apply these conventions within the task's scope. Organize code by business ownership; add layers and directories for actual responsibilities. A few files, simple functions, and direct dependencies are valid. Share and abstract for real reuse or variation needs; select architecture patterns under their stated conditions.
- Frontend requests use same-origin `/api/v1/...`, forwarded by the development proxy and production gateway. Each backend loads and validates its application-root `config.yaml`; do not use environment variables, .env files, or override chains.
- When Superpowers is available, its applicable skills govern the current phase; this skill supplies relevant engineering constraints. Reuse design, plan, confirmation, and verification records, keeping code, documentation, and acceptance in the same task. Avoid duplicate workflows or confirmations, honor outstanding requirements, and do not force the entire pipeline. Without Superpowers, follow this skill without requiring another installation. Diagnose failures first, write tests before business behavior changes, and base completion claims on actual verification.

## Documentation and Business Logic Consistency

- Locate affected README sections, architecture/feature/API documentation, configuration/run examples, and code comments. Use confirmed requirements, rules, contracts, implementation, and tests to decide which side needs correction; old documentation or passing tests alone do not establish correctness.
- When behavior, responsibilities, calls, interfaces, permissions, state, errors, logging, configuration, or operation changes, update current explanations and examples in the same change. Add minimal documentation near the relevant material when needed. For internal changes that leave documented contracts intact, explain why no update is required.
- Mark plans as unimplemented. Preserve historical facts in past designs, reviews, and replay records, adding current guidance when needed.
- Check “change → implementation/test evidence → current documentation location” for fields, examples, boundaries, and run commands, and verify executable examples where appropriate. Do not report completion while affected material remains contradictory; state the actual review scope and unverified items.

## References on Demand

| Concern | Read |
|---|---|
| New project or project initialization | [project-baseline.md](references/project-baseline.md), then [architecture responsibilities](references/architecture.md) as required by the business |
| New module responsibilities/interfaces/dependencies, boundary refactoring, or layering review | [architecture.md](references/architecture.md) |
| Frontend pages, components, state, or styles | [frontend.md](references/frontend.md) |
| Backend modules, business rules, data access, transactions, or middleware integration | [backend.md](references/backend.md) |
| API additions/changes/review, integration, request failures, or duplicate submissions | [http.md](references/http.md) |
| Logging or exception recording | [logging-config.md: Logging Lifecycle](references/logging-config.md#logging-lifecycle) |
| Backend YAML configuration, middleware/proxy configuration, or application initialization | [logging-config.md: Configuration Lifecycle](references/logging-config.md#configuration-lifecycle) |

Read only relevant sections, choose verification by impact, and follow project checks. Local field, style, or log changes do not automatically require the architecture reference. Read [sources.md](references/sources.md) only when consulting the sources of these conventions.
