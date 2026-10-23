# Default Baseline for New Projects

Start new projects with the following personal engineering conventions. The user supplies business goals, core workflows, permissions, and other actual constraints. Incorporate business design into the current Superpowers phase; do not ask again about settled engineering choices. For local changes, load only relevant conventions.

## Fixed Starting Point

| Area | Convention |
|---|---|
| Frontend | React + TypeScript + Vite; organize pages by feature, use CSS Modules for private styles, and maintain shared visual tokens centrally |
| Backend | Python + FastAPI + Pydantic; manage dependencies with uv and commit uv.lock; select and pin runtime and dependency versions at project creation |
| Application structure | One frontend and one backend organized by business module; modules collaborate in-process through public operations |
| Expansion | Choose persistence and middleware for actual business needs; split independent services only for concrete deployment or isolation requirements, using the [architecture reference](architecture.md#choose-the-smallest-sufficient-pattern) |

## Minimal Project Structure

```text
frontend/
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

Describe core operations, invariants, module ownership, interfaces, and data ownership. List runtime calls and source dependencies separately. Follow the [HTTP reference](http.md) for same-origin calls and error responses, and the [logging and configuration rules](logging-config.md) for configuration loading and log fields; do not select a second set of conventions.

Once implementation is authorized, establish configuration validation, logging, and resource lifecycle first. Then connect a real feature's page, API, business logic, and data access, verifying normal results, rejection, and failures. A design-only task delivers a proposal. Add middleware under the [integration rules](backend.md#middleware-integration), with all configuration in the same `config.yaml`.

Record project purpose, startup commands, and check commands in README. Keep only project-specific boundaries and quality requirements in AGENTS.md rather than copying the entire skill. Write design and feature documentation in Chinese. Run type checks, relevant tests, and builds, and report actual results.
