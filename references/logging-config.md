# Logging and Configuration

## Logging Lifecycle

The startup entry point loads and validates configuration, configures logging, then creates business dependencies and runs business behavior. Modules obtain loggers without adding their own handlers. Check framework logger handlers and propagation; repeated initialization must not duplicate output. Follow existing lifecycle conventions for resource cleanup and application shutdown.

Use JSON business logs with the fixed base fields `timestamp/level/service/module/event/request_id`; add duration, status, and stable business identifiers per event. Use timezone-aware ISO 8601 timestamps and null request_id for non-request events. Configure Python's standard logging centrally; modules only obtain loggers.

| Level | Use |
|---|---|
| DEBUG | Controlled diagnostics, still subject to sensitive-data restrictions |
| INFO | Key business outcomes, startup/shutdown, and necessary operation summaries |
| WARNING | Degradation, unusual business conditions, or exhausted retries requiring attention |
| ERROR | Unexpected failures or system operations that cannot complete, with safe stack traces when needed |

Log a failure once at the boundary responsible for handling it. Inner layers add context or raise errors rather than logging the same stack trace at every layer. Expected field-validation failures need not all become system errors. Avoid noisy business logs from health checks and frequent polling.

Allowlist safe event fields, stable identifiers, error codes, status, and duration instead of serializing entire objects. Exclude Authorization, Cookie, passwords, tokens, connection strings, raw request bodies, and business details. Prefer route templates in access logs and filter query strings. HTTP-client debug logs, exception messages, and stack traces can also leak data; inspect and filter them. Redacting dictionary fields alone does not protect raw exception strings.

Generate a request ID at the boundary or validate an incoming one, and propagate it downstream and into error responses. Limit external input length and characters to prevent log injection. The frontend displays safe explanations and the correlation ID without logging authentication data. Do not add a telemetry SDK by default where none exists.

Write logs to stdout; the deployment environment handles collection, rotation, and retention. If business auditing requires persistence, design for its actual authorization and reliability needs rather than relying solely on ordinary rotating logs.

## Configuration Lifecycle

1. **Backends read config.yaml:** Each backend loads its application-root `config.yaml`, validates types, ranges, required fields, and field combinations, and produces an explicit settings object. Invalid required configuration fails startup; errors expose only safe field names and reasons. Give safe diagnostics for missing or unreadable files.
2. **Fixed path, single source:** Resolve the configuration path relative to the application directory, independently of the launch working directory. Do not read environment variables or .env files, or provide environment overrides, variable interpolation, or fallback chains. Application, logging, data sources, and middleware use separate sections in the same `config.yaml`. Name middleware sections by component; keep them out of business functions and separate configuration files.
3. **Separate configuration binding from resource composition:** `infrastructure/settings.py` collects configuration models and binds component YAML sections to their settings classes; see [middleware integration](backend.md#middleware-integration) for file ownership. Business modules receive injected objects or required parameters; the startup entry point creates and closes resources. Module imports must not read YAML or establish connections.
4. **Keep examples and validation synchronized:** Use separate strict models for configuration sections and reject unknown fields. For every new field, maintain its type, default/required status, range, example, and corresponding tests together. Create and validate sections only for middleware actually used. Defaults must be safe and semantically stable; credentials must not have working production defaults.
5. **Protect secrets in YAML:** Keep real credentials in private server-side or deployment-mounted YAML files, restrict file permissions, and exclude them from version control. Committable examples use invalid placeholders. Use safe settings representations without exposing original values. Do not turn secrets into environment variables or print full configuration.
6. **Frontend requests use a same-origin proxy:** Browser business API calls use only `/api/v1/...` relative paths. The development proxy and production Nginx gateway maintain backend target addresses and route by API ownership. Browsers access business services through the same site entry point without loading deployment configuration. Keep backend YAML server-side; database passwords, signing keys, and server tokens must not enter browser artifacts.
7. **State when changes take effect:** Backends read `config.yaml` at startup; restart the owning application after edits. Restart the development server after proxy changes. Validate production Nginx configuration before reloading it.

## Verification Targets

For logging changes, verify JSON base fields, repeated initialization, a single log per handled failure, correlation IDs, and absence of sensitive values in access logs and third-party exceptions. For backend configuration, cover valid, missing, invalid, and unknown fields, the fixed YAML path, and the inability of environment variables to change settings. For middleware, verify separate configuration sections and resource startup/shutdown; examples should load under explicit test conditions. For the frontend, check same-origin requests, alignment of proxy routes with backend contracts, and absence of server secrets in browser artifacts. Retain relevant business regression coverage; format-string matching alone is insufficient acceptance evidence.
