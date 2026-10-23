# Sources and Scope

Sources consulted: 2026-10-23. The following summaries draw design ideas from primary repositories and restate them as this skill's own conventions, without copying implementations, third-party prompts, or complete templates. Branch links may change upstream; this skill does not claim continuous synchronization.

| Source | Adopted idea | Choices in this skill |
|---|---|---|
| [Bulletproof React: project structure](https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md) | Group by business capability, use one-way dependencies, and create only needed directories | No fixed full feature subdirectory tree; existing public-entry-point rules take priority over the source's direct-import policy |
| [Bulletproof React: API layer](https://github.com/alan2207/bulletproof-react/blob/master/docs/api-layer.md) | Shared client, explicit endpoint types, and request definitions | Add query hooks for actual state/caching needs rather than empty wrappers around individual requests |
| [FastAPI full-stack template: frontend](https://github.com/fastapi/full-stack-fastapi-template/blob/master/frontend/README.md) | Synchronize backend OpenAPI and generated clients | Keep OpenAPI and frontend types aligned without adopting the template's other technology choices |
| [FastAPI full-stack template: configuration](https://github.com/fastapi/full-stack-fastapi-template/blob/master/backend/app/core/config.py) | Typed configuration and validity checks | Adopt validation principles with YAML as the only source; omit environment loading, import-time instantiation, and ignored extra fields |
| [Node Best Practices: layering](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/projectstructre/createlayers.md) | Separate transport, business logic, and data access | Use these responsibilities to guide design without requiring three directories or wrappers on every call |
| [Node Best Practices: logging](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/production/smartlogging.md) | Meaningful events, structured context, and correlation identifiers | Apply as needed without automatically adding a logging library, APM, or centralized logging cluster |
| [Node Best Practices: configuration](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/projectstructre/configguide.md) | Group configuration, isolate secrets, and validate early | Use YAML loading without file/environment merging or environment override chains |
| [Anthropic: Skill Creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Short entry point, on-demand references, and realistic task validation | Keep the skill self-contained without mandatory network, plugin, or other skill dependencies |

## Personal Conventions from the Original Project

Use the [personal default baseline](project-baseline.md) for new projects. Keep responsibilities clear, write tests first, target the current contract directly, and abstract for actual needs. Initialize logging first and record only safe identifiers. Frontend calls use same-origin APIs through the development proxy and production Nginx gateway. Each backend reads its application-root `config.yaml`, with separate middleware sections in the same file. Do not use environment variables or override chains for configuration.

Sphere's four-layer decision model, shared database account, specific schemas/table names, application splits, and offline evaluation authority belong to the original project. This skill does not carry those domain rules or impose Sphere naming on new projects. Read the current repository's latest AGENTS.md and actual check entry points when applying it.
