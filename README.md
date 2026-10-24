# fullstack-blueprint · Fullstack Engineering Blueprint

A fullstack engineering design skill for AI coding assistants, with reusable conventions for frontend/backend design, module layering, API calls, configuration, logging, and documentation maintenance.

For a new project, provide business goals, core workflows, permissions, and actual constraints to start from a consistent engineering baseline. For existing projects, apply relevant conventions within the task's scope and let the structure grow with real responsibilities.

## When to Use

- Start a fullstack project and establish its default stack, module responsibilities, and structure.
- Add pages, business modules, or APIs with clear frontend/backend calls and dependency directions.
- Refine module boundaries or review whether layers carry real responsibilities.
- Integrate middleware and maintain configuration, resource lifecycle, and logging.
- Check current documentation and examples against implementation when business behavior changes.

## Core Conventions

| Area | Convention |
|---|---|
| Default stack | React + TypeScript + Vite frontend; Python + FastAPI + Pydantic backend, using uv and uv.lock |
| Module layering | Organize by business capability and separate API, business, and data-access responsibilities as needed; start with one frontend and one modular backend |
| Frontend ownership | Keep feature UI, state, helpers, and private styles with the feature; use CSS Modules in new projects and put actual cross-feature capabilities in shared |
| API organization | Central API directory, split by business module, with paths, types, and named request functions; use a shared HTTP client and call named functions from pages |
| Frontend/backend calls | Browsers use same-origin `/api/v1/...`; development proxy and production Nginx gateway configuration own backend target addresses |
| Backend configuration | Each backend uses its application-root config.yaml as its only configuration source, validates it strictly, and restarts after edits; no environment variables or .env loading |
| Middleware | Introduce for real business needs, with separate sections in the same config.yaml; each component has its own file for settings/resource classes, assembled and released by the entry point |
| Logging | Structured JSON to stdout with stable identifiers and request_id; the responsible boundary logs each failure, with sensitive data filtered |
| Documentation consistency | Update affected current explanations and examples alongside behavior or convention changes, checking them against implementation and verification evidence |

Use the smallest sufficient structure. Simple features may use a few files and direct function calls; add abstraction, sharing, and independent services for actual needs. The complete rules live in [SKILL.md](SKILL.md) and its references.

## Installation

The reusable instructions live in `SKILL.md` and `references/`. Install the skill folder through your coding assistant's skill mechanism.

### Codex Example

With Git installed, clone the repository into the user-level skill directory:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/chenxin-coder/fullstack-blueprint.git ~/.agents/skills/fullstack-blueprint
```

Use these commands only when the target directory does not exist. For an existing installation, handle local changes before updating:

```bash
git -C ~/.agents/skills/fullstack-blueprint pull --ff-only
```

Codex discovers the skill in this directory. If it does not appear, restart Codex and check again. See the [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills#where-to-save-skills) for user-level directories and loading behavior.

## Usage

Ask your coding assistant to apply `fullstack-blueprint` to the task, for example:

```text
Use fullstack-blueprint to design an equipment borrowing system with request, approval, and return workflows.
```

```text
Use fullstack-blueprint to add an order query page and API to the current project, following existing module boundaries and updating affected documentation.
```

```text
Use fullstack-blueprint to review the project's frontend/backend layering, API calls, configuration, and logging. Report only findings supported by evidence.
```

In Codex, [agents/openai.yaml](agents/openai.yaml) sets `allow_implicit_invocation: true`, allowing automatic selection when the task matches the skill description. Use `$fullstack-blueprint` for explicit invocation in Codex.

When Superpowers is installed, its applicable skills govern the current phase while this skill supplies engineering constraints and reuses existing design, plan, confirmation, and verification records. The skill also works independently without Superpowers.

## Contents

| File | Content |
|---|---|
| [SKILL.md](SKILL.md) | Scope, task deliverables, core constraints, and documentation consistency |
| [agents/openai.yaml](agents/openai.yaml) | Codex display metadata, default prompt, and implicit-invocation policy |
| [references/project-baseline.md](references/project-baseline.md) | Default stack and minimal structure for new projects |
| [references/architecture.md](references/architecture.md) | Business responsibilities, module interfaces, layering choices, and dependency directions |
| [references/frontend.md](references/frontend.md) | Feature modules, state, shared capabilities, and style ownership |
| [references/backend.md](references/backend.md) | Backend responsibilities, transactions, module collaboration, and middleware integration |
| [references/http.md](references/http.md) | Central API definitions, contracts, errors, timeouts, and duplicate submissions |
| [references/logging-config.md](references/logging-config.md) | Log fields, configuration validation, resource composition, and activation |
| [references/sources.md](references/sources.md) | Sources and scope of adopted ideas |

Update the relevant rule files during maintenance and synchronize affected explanations in this README. Verify within the change's scope and keep project-specific business rules out of the general skill.
