# fullstack-blueprint · Fullstack Engineering Blueprint

A fullstack engineering design skill for AI coding assistants, with reusable conventions for frontend/backend design, module layering, API calls, configuration, logging, and documentation maintenance.

## Overview

For a new project, provide business goals, core workflows, permissions, and actual constraints to start from a consistent engineering baseline. Defaults fill only unspecified choices. For existing projects, preserve the stack, configuration/secret sources, API contracts, logging, and deployment conventions, applying engineering guidance within the requested scope.

- Start a fullstack project and establish its default stack, module responsibilities, and structure.
- Add pages, business modules, or APIs with clear frontend/backend calls and dependency directions.
- Refine module boundaries or review whether layers carry real responsibilities.
- Integrate middleware and maintain configuration, resource lifecycle, and logging.
- Check current documentation and examples against implementation when business behavior changes.

Implicit invocation covers design, implementation, refactoring, and engineering review. Questions that only explain the current scheduler, locate configuration, trace calls, or define a concept can be answered directly without this skill. Read-only architecture reviews still qualify. Explicit invocation keeps the requested scope: asking for an explanation does not authorize design or code changes.

## Quick Start

The shared skill consists of `SKILL.md` and `references/`. Keep them together when installing or packaging the skill. Each assistant uses its own installation and invocation mechanism.

The clone commands below assume the destination directory does not exist.

### Codex

With Git installed, clone the repository into the user-level skill directory:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/chenxin-coder/fullstack-blueprint.git ~/.agents/skills/fullstack-blueprint
```

For an existing installation, handle local changes before updating:

```bash
git -C ~/.agents/skills/fullstack-blueprint pull --ff-only
```

Invoke it with `$fullstack-blueprint`. The included metadata enables implicit invocation when the task matches the description. If the skill does not appear, restart Codex and check again. See the [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills#where-to-save-skills) for user-level directories and loading behavior.

### Claude Code

Clone the repository into Claude Code's personal skill directory:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/chenxin-coder/fullstack-blueprint.git ~/.claude/skills/fullstack-blueprint
```

Invoke it with `/fullstack-blueprint`, or let Claude select it when the task matches the description. See the [official Claude Code skill documentation](https://code.claude.com/docs/en/skills) for discovery and invocation behavior.

### WorkBuddy

From a local Git checkout of this repository, create a ZIP package of the committed skill files:

```bash
git archive --format=zip --prefix=fullstack-blueprint/ --output=../fullstack-blueprint.zip HEAD
```

In WorkBuddy, open the skills page, choose **Add Skill > Upload Skill**, and select the ZIP file. Keep `SKILL.md` and the complete `references/` directory in the package. After importing, locate the skill in the installed list, enable it, and ask WorkBuddy to use `fullstack-blueprint` for the task. See the [official WorkBuddy skill guide](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market) for local package import and management.

Marketplace publication follows the separate [WorkBuddy Open Platform requirements](https://open.workbuddy.cn/en/docs/skill), including its required listing metadata.

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

When Superpowers is installed, its applicable skills govern the current phase while this skill supplies engineering constraints and reuses existing design, plan, confirmation, and verification records. The skill also works independently without Superpowers.

## Core Conventions

The concrete stack, file names, API prefix/envelopes, and logging format below are defaults for new projects without user-specified conventions. Existing projects extend their current mechanisms; a difference from these defaults is not itself a review finding or a reason to migrate.

| Area | Convention |
|---|---|
| Default stack | React + TypeScript + Vite frontend; Python + FastAPI + Pydantic backend, using uv and uv.lock |
| Module layering | Organize by business capability and separate API, business, and data-access responsibilities as needed; start with one frontend and one modular backend |
| Frontend ownership | Keep feature UI, state, helpers, and private styles with the feature; use CSS Modules in new projects and put actual cross-feature capabilities in shared |
| API organization | Central API directory, split by business module, with paths, types, and named request functions; use a shared HTTP client and call named functions from pages |
| Frontend/backend calls | Browsers use same-origin `/api/v1/...`; development proxy and production Nginx gateway configuration own backend target addresses |
| Backend configuration | New-project default: validated application-root config.yaml, loaded at startup without environment overrides; existing applications retain their configuration/secret sources and activation rules |
| Middleware | Introduce for real business needs; bind settings and manage resources through the application's existing lifecycle, using config.yaml and component files for the default Python baseline |
| Logging | Structured JSON to stdout with stable identifiers and request_id; the responsible boundary logs each failure, with sensitive data filtered |
| Documentation consistency | Update affected current explanations and examples alongside behavior or convention changes, checking them against implementation and verification evidence |

Use the smallest sufficient structure. Simple features may use a few files and direct function calls; add abstraction, sharing, and independent services for actual needs. The complete rules live in [SKILL.md](SKILL.md) and its references.

## Contents

| File | Content |
|---|---|
| [SKILL.md](SKILL.md) | Scope, task deliverables, core constraints, and documentation consistency |
| [agents/openai.yaml](agents/openai.yaml) | Optional OpenAI-specific display metadata, default prompt, and invocation policy |
| [references/project-baseline.md](references/project-baseline.md) | Default stack and minimal structure for new projects |
| [references/architecture.md](references/architecture.md) | Business responsibilities, module interfaces, layering choices, and dependency directions |
| [references/frontend.md](references/frontend.md) | Feature modules, state, shared capabilities, and style ownership |
| [references/backend.md](references/backend.md) | Backend responsibilities, transactions, module collaboration, and middleware integration |
| [references/http.md](references/http.md) | Central API definitions, contracts, errors, timeouts, and duplicate submissions |
| [references/logging-config.md](references/logging-config.md) | Log fields, configuration validation, resource composition, and activation |
| [references/sources.md](references/sources.md) | Sources and scope of adopted ideas |
| [LICENSE](LICENSE) | MIT license terms |

[agents/openai.yaml](agents/openai.yaml) provides optional OpenAI-specific display metadata, a default prompt, and invocation policy. The engineering rules live in the shared files. See the [official metadata documentation](https://learn.chatgpt.com/docs/build-skills#optional-metadata) for the supported fields.

Update the relevant rule files during maintenance and synchronize affected explanations in this README. Verify within the change's scope and keep project-specific business rules out of the general skill.

## Evaluation

Run the dependency-free package checks with:

```bash
python3 -m unittest discover -s tests -v
```

These checks validate local documentation links/anchors and evaluation fixture structure. They do not measure model behavior. [Evaluation instructions](evals/README.md) cover the 15 routing cases, six behavior cases, before/after comparison, and evidence levels. The [current review record](evals/review-2026-11-05.md) distinguishes observed baseline behavior, source inspection, and unrun model evaluations. Evaluation files and tests are maintenance tooling; normal skill use loads only `SKILL.md` and relevant references.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
