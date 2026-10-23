# Frontend-Backend Calls and Contracts

## Call Chain and Responsibilities

Runtime: `user action → page/business function → endpoint function → HTTP client → same-origin proxy → backend API → business logic → data access`. Simple features may omit a separate frontend business wrapper while keeping responsibilities explicit.

The HTTP client owns transport mechanics; endpoint functions own API types and paths; pages or business operations own user feedback and refreshes. The client must not directly manipulate a page's form, dialog, or cache. The server verifies authorization and business facts; the frontend never accesses databases or server secrets directly.

## Centralized API Definitions

Keep APIs in a central directory, split by business module so they are easy to find. Minimal example:

```text
src/api/
  client.ts     # Shared HTTP mechanism
  orders.ts     # Order paths, API types, and named request functions
  users.ts      # User paths, API types, and named request functions
```

Browsers use same-origin `/api/v1/...` relative paths. The development proxy and production Nginx gateway route requests to the owning business services. Keep backend target addresses in proxy/gateway configuration; the client accepts only relative paths. See the [configuration lifecycle](logging-config.md#configuration-lifecycle) for configuration and activation.

Keep each API module's relative paths, HTTP methods, request/response types, and request functions together, with one authoritative definition per endpoint. Generate dynamic resource paths in the corresponding function. Pages call named functions such as `orders.list()` and `orders.detail(id)` instead of concatenating domains or repeating paths. API modules must not import page state or UI types. A separate global URL-constant table is unnecessary, and all business APIs must not accumulate in one large file. A few endpoints may start in one file and split as real business responsibilities grow.

## Contract Maintenance

When adding or changing an API, follow the existing contract and specify:

- Method, path, authentication, and authorization scope.
- Request/response types, required fields, nullability, time formats, and pagination/sorting semantics.
- Error codes, HTTP statuses, user-visible information, and retryability; distinguish business rejection, expired authentication, network failure, and an unknown outcome.
- Duplicate-submission semantics for writes and the data to refresh after success.

With existing OpenAPI/code generation, change the authoritative schema first and regenerate frontend artifacts with existing commands; do not hand-edit generated code. Small projects without generation may maintain clear types and contract tests; introduce generation as API size or drift costs warrant it. Static types do not replace server input validation. Validate unreliable external responses at runtime at an appropriate boundary.

Return the contract's DTO directly on success, without a uniform data wrapper. Error responses contain `code/message/request_id`, with HTTP status matching the error semantics. Optional `details` hold safe field-validation information only. Do not expose stack traces, SQL, or internal addresses to browsers.

## Timeouts and Retries

- A write timeout means the client did not receive a result in time; the write may have succeeded. Show a pending-confirmation outcome, preserve the business intent, and confirm it through a status query or safe replay. Do not declare failure and create a new operation. A read timeout is a read failure.
- Set explicit client timeouts and cancellation; control server operation deadlines separately. Canceling a browser request does not imply server-side business rollback.
- Transient read failures may use bounded retries with backoff and respect for server rate-limit signals. Retry writes automatically only when safe repetition is established. Do not automatically retry business-validation or permission rejections. Safety depends on actual side effects, not the HTTP method name alone.

## Choose Duplicate Protection by Operation Semantics

| Operation condition | Smallest sufficient approach |
|---|---|
| Read-only | No write-idempotency infrastructure |
| Set a definite value on a definite resource without extra side effects on repetition, such as a theme | Update atomically by resource identity to preserve natural idempotency; no added idempotency key or result table |
| Creation already has a unique key representing the same business intent, such as a business order number | Use database uniqueness and transactions to create once; define whether duplicates return the existing result or a conflict, without requiring an extra idempotency table |
| These approaches cannot remove repeated side effects, and safe resubmission or result replay is needed, such as debits, increments, or creation without a business unique key | Use an idempotency key with reliable result records, or reuse an existing facility that meets the requirements |

Disabling the frontend submit button improves usability; the server guarantees correctness using the selected approach. Natural idempotency does not prevent an old intent's retry from overwriting a newer one. For concurrent edits or out-of-order writes, use existing version conditions or restrict automatic retries and define conflict handling. A business unique key prevents duplicates but does not necessarily replay the original response; add that capability only when exact replay is needed.

**When using idempotency keys:** Reuse one key for the same business intent and its retries. The backend binds the key to the actor/operation scope, a normalized request digest, and a durable result. The same key with different content conflicts; the same key and content returns the original result or an explicit processing state. Atomically associate the record with business writes and define retention. For external side effects, also define external idempotency or outcome reconciliation; single-process in-memory deduplication does not guarantee correctness across processes.

Follow the API contract's authentication mechanism. For cookies, check CSRF and credential policies. Route browser requests through the same-origin entry point rather than relaxing CORS or permissions to make integration work.

## Creation Example Requiring Result Replay

Create an order with `POST /api/v1/orders`. `OrderCreate` preserves input, generates a business-intent identifier, and calls `orders.create()`; the client adds the existing authentication and idempotency headers. The backend validates authorization and quantity, and the business function saves the order and idempotency result in one database transaction. Return the order and refresh the order list on success. If the response is lost, confirm with the original key. Changing quantity with the same key conflicts; use a new key only after the user confirms a new intent.

Choose verification for the actual approach. Common checks cover normal results, business rejection, authorization, failure feedback, and relevant cache updates. For natural idempotency, check repeated identical values and required out-of-order conflicts. For business unique keys, check concurrent duplicate creation. For idempotency keys, additionally check concurrent identical keys, different-content conflicts, and replay after a lost response. Do not add result tables for read-only or naturally idempotent operations.
