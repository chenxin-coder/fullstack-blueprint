# Backend Responsibilities and Layering

## Separate Responsibilities Before Directories

The API layer handles transport and validation, business logic owns business rules, and data access handles databases and external systems. Organize new projects using the [default baseline](project-baseline.md#minimal-project-structure). Create `api.py`, `service.py`, `data_access.py`, and `schemas.py` within modules according to actual responsibilities; do not add layers without behavior.

| Responsibility | Owns | Must not own |
|---|---|---|
| Startup/composition | Configuration loading, logging initialization, dependency creation, route registration, resource shutdown | Specific business workflows |
| API | Request parsing, authentication entry, parameter validation, use-case calls, response/error mapping | SQL, core calculations, duplicated business rules |
| Business logic | Permissions and business conditions, state transitions, workflows, transaction semantics | HTTP Request/Response objects or HTTP status codes |
| Data access | Parameterized queries, persistence, external-service requests, technical error translation | Business decisions outside its module |

Simple queries need not pass through a service that only forwards arguments; a thin API may call a clearly defined query function. Centralize calculations, authorization scope, and state transitions in business logic. Extract complex rules into ordinary functions or domain modules without first building a domain framework.

Typical runtime calls: `route → business function → data-access function`. With lightweight layering, business logic may depend directly on concrete data-access functions. To isolate external side effects, first pass existing dependencies explicitly; introduce ports and adapters when real multiple implementations require shared calling semantics. Keep pure rule modules independent of HTTP, ORM, and configuration loading. Honor existing domain/ports/adapters constraints. For pattern choices or dependency changes, state source import directions using the [architecture reference](architecture.md#distinguish-calls-from-source-dependencies); do not infer imports from runtime call order.

## Modules and Packages

- Group business code by owning module and expose only operations callers need. Use public capabilities rather than another module's internal state.
- Keep code with only one actual consumer in that feature. Shared packages need real consumers, a clear responsibility, and independent dependencies. Do not route imports back into application internals through a shared package.
- Distinguish API DTOs, internal business models, and database models when they have different reasons to change. Identical fields and semantics without independent variation do not justify copying objects for every layer.
- Pass configuration, database connections, and replaceable external dependencies explicitly. Do not read global configuration and create connections inside business functions.

## Correctness Ownership

Use strict Pydantic input validation and reject unknown fields; specify required, nullable, and default values. The server verifies resource ownership and operation permissions. Client-supplied identity, amounts, status, or path identifiers do not establish authorization.

The use case defines the transaction around a business operation that must be atomic. Data access receives its transaction context and does not commit early on its own. Enforce uniqueness with database constraints; check-then-write alone does not handle concurrency. External HTTP operations are not undone by database rollback. When a change includes such side effects, explain resulting states and responsibility for retries or compensation after failures.

Represent expected business errors with stable error types and map them at the API boundary to the [standard error response](http.md#contract-maintenance). Return safe information and request_id for unknown errors; the boundary responsible for handling them owns the log entry.

## Middleware Integration

- Choose and add middleware for actual caching, asynchronous work, search, or object-storage needs, and explain its responsibility. Without a corresponding requirement, do not install dependencies or create configuration sections.
- Keep all configuration in the application's own `config.yaml`, with a separate section for each component, such as `middleware.redis` or `middleware.rabbitmq`. See the [configuration lifecycle](logging-config.md#configuration-lifecycle) for fields, examples, and validation.
- Give each component one `infrastructure/middleware/<component>.py` file containing its settings class and resource class, for example `RedisSettings` and `RedisResource` in `redis.py`. The settings class only declares strict fields and validation. The resource class accepts that settings object and encapsulates the client/connection pool, SDK operations, and protocol translation.
- `infrastructure/settings.py` explicitly imports the settings classes for components in use and binds their YAML sections into the root Settings model, for example `middleware.redis → RedisSettings`, for unified loading and validation. Component files must not import the root Settings model or business modules.
- The application lifecycle in `main.py` explicitly creates resource instances and injects business dependencies; each process reuses its own instances. Release already-created resources if startup fails and close resources centrally on shutdown. Business modules use injected operations rather than reading configuration, creating connections, or registering resources.
- Specify addresses, authentication, connection/operation timeouts, and required pool parameters. Choose retries based on business side effects. Verify initialization and cleanup, unavailability/timeouts, and the operations actually used. For duplicate message delivery, verify idempotency and failure recovery.

## Verification

Verify rules and error mapping through business functions and HTTP entry points first. Cover the change's key transactions, queries, and constraints in data-access checks. Reuse existing architecture checks. Write tests that exercise new or changed behavior before implementation; use actual project commands to establish type-check, test, and build coverage.
