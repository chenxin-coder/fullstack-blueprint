# fullstack-blueprint · Fullstack Project Blueprint

A skill for AI coding assistants that helps beginners turn business ideas into small, runnable React/Python projects. It packages practical standards for frontend/backend design, module ownership, API calls, configuration, logging, and documentation.

## Overview

Describe what the application should do, who uses it, and its main workflow. The assistant recommends the technical foundation, creates only necessary structure when building is requested, and provides a working feature with first-run instructions. Users do not need to select architecture patterns.

The main path is **business goal → recommended foundation → minimal structure → real feature → verified startup and handoff**. Start with one frontend and one modular backend, then extend them with the same standards as requirements grow.

- New projects use React + TypeScript + Vite and Python + FastAPI + Pydantic, with npm and uv lockfiles.
- Each feature keeps its UI, state, helpers and private styles together; API definitions and shared transport stay easy to find.
- Backend YAML settings, logging and resource lifecycle are established before business behavior.
- The handoff includes prerequisites, copyable commands, the browser address, one concrete user operation and actual verification results.
- Later features keep current documentation, configuration examples and behavior consistent.

Implicit invocation covers new-project design/build and continued work in projects already using this blueprint. Unrelated existing-project refactoring and current-code explanations are outside that automatic scope. Explicit invocation respects the requested task. Explicit user requirements take precedence over defaults; existing files and agreed contracts are not silently replaced.

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
Use fullstack-blueprint to design a small equipment borrowing app with request, approval, and return. Explain the recommended structure; do not implement it yet.
```

```text
Use fullstack-blueprint to build a small personal notes app. I need to add and list notes, keep them after restart, and follow the README to run it locally.
```

```text
This project was built with fullstack-blueprint. Add a search filter to the notes page and API, and update the affected tests and documentation.
```

When Superpowers is installed, its applicable skills govern the current phase while this skill supplies engineering constraints and reuses existing design, plan, confirmation, and verification records. The skill also works independently without Superpowers.

## Core Conventions

These are the recommended starting standards. The assistant applies them to the actual business need and explains necessary choices in plain language. Explicit user requirements take precedence.

| Area | Convention |
|---|---|
| Default stack | React + TypeScript + Vite with npm/package-lock.json; Python + FastAPI + Pydantic with uv/uv.lock |
| Module layering | Organize by business capability and separate API, business, and data-access responsibilities as needed; start with one frontend and one modular backend |
| Frontend ownership | Keep feature UI, state, helpers, and private styles with the feature; use CSS Modules in new projects and put actual cross-feature capabilities in shared |
| API organization | Central API directory, split by business module, with paths, types, and named request functions; use a shared HTTP client and call named functions from pages |
| Frontend/backend calls | Browsers use same-origin `/api/v1/...`; development proxy and production Nginx gateway configuration own backend target addresses |
| Backend configuration | Validated application-root config.yaml, loaded at startup; edits take effect on restart, without environment overrides or .env loading |
| Middleware | Introduce for real business needs; use separate sections in config.yaml and one settings/resource file per component, assembled and released by the application lifecycle |
| Logging | Structured JSON to stdout with stable identifiers and request_id; the responsible boundary logs each failure, with sensitive data filtered |
| First-run handoff | Document tools, exact setup/start/check commands, browser address, expected feature result and safe recovery from common setup errors |
| Documentation consistency | Update affected current explanations and examples alongside behavior or convention changes, checking them against implementation and verification evidence |

Use the smallest sufficient structure. Simple features may use a few files and direct function calls; add abstraction, sharing, and independent services for actual needs. The complete rules live in [SKILL.md](SKILL.md) and its references.

## Contents

| File | Content |
|---|---|
| [SKILL.md](SKILL.md) | Project scope, beginner workflow, engineering rules, and documentation consistency |
| [agents/openai.yaml](agents/openai.yaml) | Optional OpenAI-specific display metadata, default prompt, and invocation policy |
| [references/project-baseline.md](references/project-baseline.md) | Default stack, minimal structure, and first-run acceptance criteria |
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

These checks validate local documentation links/anchors and evaluation fixture structure, including allowed workspace changes. They do not measure model behavior. The [evaluation instructions](evals/README.md) cover 15 routing cases and six behavior cases focused on new-project design, runnable setup, incremental features, YAML, middleware and continued implementation. The [current review record](evals/review-2026-11-05-new-project-focus.md) records this scope and its actual verification. Evaluation files are maintenance tooling; normal skill use loads only `SKILL.md` and relevant references.

## License

Licensed under the MIT License. See [LICENSE](LICENSE).
