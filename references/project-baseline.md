# Default Baseline for New Projects

Use this starting standard when building a new project for a beginner. Recommend the baseline directly and explain choices through the business task. Explicit user requirements take precedence; do not reopen settled choices. Continue using the same project conventions as features grow. Scope instructions to the target project and incorporate the work into the current Superpowers phase when available.

## Default Starting Point

| Area | Convention |
|---|---|
| Frontend | React + TypeScript + Vite; use npm and commit package-lock.json; organize pages by feature, use CSS Modules for private styles, and maintain shared visual tokens centrally |
| Backend | Python + FastAPI + Pydantic; manage dependencies with uv and commit uv.lock; select and pin runtime and dependency versions at project creation |
| Application structure | One frontend and one backend organized by business module; modules collaborate in-process through public operations |
| Database tables | When persistence is needed, follow the [database key convention](backend.md#database-keys): generated integer `id` primary key, with business identifiers kept separately |
| Expansion | Choose persistence and middleware for actual business needs; split independent services only for concrete deployment or isolation requirements, using the [architecture reference](architecture.md#choose-the-smallest-sufficient-pattern) |

## Minimal Project Structure

```text
frontend/
  package.json
  package-lock.json
  src/
    app/                         # Routing and page composition
    features/<feature>/          # Feature UI, state, helpers, and local styles
    api/                         # Shared client and API files by business module
    shared/                      # UI, tools, and visual tokens reused across features
backend/
  config.yaml                    # Separate application, logging, data, and middleware sections
  config.example.yaml            # Committable example with invalid credential placeholders
  pyproject.toml
  uv.lock
  src/<app>/
    main.py                      # Resource composition and lifecycle
    modules/<feature>/           # API, business logic, data access, and contract models
    infrastructure/
      settings.py                # Configuration models and YAML section bindings
      logging.py                 # Logging initialization
      middleware/<component>.py  # Component settings and resource classes, only as needed
  tests/
README.md
AGENTS.md
```

Create files for actual responsibilities; do not prebuild empty directories, forwarding-only services, or a generic middleware framework. See the [backend reference](backend.md#separate-responsibilities-before-directories) for module internals and the [frontend reference](frontend.md#responsibilities-and-dependencies) for dependencies and style ownership.

## Design and Implementation Outcomes

Explain the main operation, the few modules that own its rules and data, and how the page reaches the backend. Distinguish runtime calls from source dependencies when describing a boundary. The assistant selects the smallest sufficient structure; users need not choose DDD, ports/adapters, or service boundaries. Follow the [HTTP reference](http.md) and [logging and configuration rules](logging-config.md) for their respective concerns.

Once implementation is authorized, establish configuration validation, logging, and resource lifecycle first. Then connect a real feature's page, API, business logic, and data access, verifying normal results, rejection, and failures. A design-only task delivers a proposal. Add middleware under the [integration rules](backend.md#middleware-integration), with all configuration in the same `config.yaml`.

## First-Run Acceptance

For a requested implementation, hand over a working feature and instructions that a beginner can follow from a fresh checkout:

- State the required Python, Node.js, uv and frontend package-manager versions. Pin dependencies with the generated project's lockfiles and keep installation consistent with them. Give installation guidance for missing tools rather than assuming they exist.
- Document the exact working directory and copyable commands to install frontend/backend dependencies, create the local `config.yaml` from its example, and prepare only persistence or middleware actually required. A local example should work without production credentials; external services need explicit setup instructions and safe placeholders.
- Provide frontend/backend startup commands, ports, browser URL and a stop/restart method. Keep backend addresses in the development proxy; the browser uses relative API paths.
- Walk through one real user operation and its expected visible result. Verify that it reaches the backend and, where the feature requires persistence, survives the relevant reload/restart. Identify test data or actual service requirements clearly; do not present a mock as a working integration.
- Run the documented checks, relevant behavior tests and frontend production build. Rehearse the setup/start steps in an isolated environment where feasible; distinguish commands actually run from instructions not yet exercised. Missing dependencies or services are explicit blockers, not a successful handoff.
- Explain common first-run failures using the actual setup: missing/invalid YAML, occupied ports, or unavailable required services. Include safe recovery steps and where request IDs/logs can help.

Keep these instructions in README alongside the project purpose. Keep only target-project boundaries and quality requirements in AGENTS.md, and follow the project's document language. Design-only tasks describe these future acceptance criteria without claiming a runnable application. Later feature changes update the same instructions when their behavior or setup changes.
