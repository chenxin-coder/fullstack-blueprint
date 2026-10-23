# Frontend Design and Module Ownership

## Start with the User Task

Explain what the user accomplishes on the page, its primary action, and the next step. Prefer existing controls, routes, and visual tokens. Define feedback for loading, empty data, denied access, read failure, submission in progress, submission failure, and success; preserve user input and offer actionable recovery.

Distinguish field errors from system errors in forms. Base confirmation for dangerous or hard-to-reverse operations on actual consequences. Follow project responsive conventions and check narrow screens, long text, keyboard use, form labels, and focus. New interactions must communicate state beyond color alone.

## Responsibilities and Dependencies

| Responsibility | Ownership | Extraction criterion |
|---|---|---|
| Routes, Providers, page composition | Entry point or app | Keep business rules in their feature |
| Pages and private components | Page or business feature | Split components with an independent interaction responsibility |
| Business operations and data update coordination | Functions or hooks in the owning feature | Extract for complex interactions or multiple callers |
| HTTP mechanism | Shared client | Centralize addressing, authentication mechanics, timeouts, and error parsing |
| Business endpoint definitions | Central API directory, split by business module | Keep paths, request/response types, and request functions together; see [centralized API definitions](http.md#centralized-api-definitions) |
| Shared UI and tools | Existing shared/common directory | Reused by multiple features without page-specific business rules |

The default import direction is page/feature → corresponding API module → HTTP client. Pages/features may also depend on shared UI and tools; API and shared capabilities must not import page or feature internals. Prefer the composition layer to coordinate two features, and honor existing public-entry-point rules. Do not bulk-add or remove index.ts files to match an external template.

In a small project, a page may call named API request functions directly; a hook/service wrapper for every request is unnecessary. Keep private UI, state, helpers, styles, and tests with the feature. Keep API DTOs and request tests with the API module, and only cross-feature capabilities in shared code. Avoid concentrating all business logic in utils, a global store, or App.

## State Ownership

- Manage server data with the existing query mechanism. Simple requests and local state suffice without caching needs; introduce a query library only for a real requirement.
- Keep form edits, dialogs, selections, and similar state near their consumers. Prefer URL state for shareable filters and pagination.
- Include user or tenant identity in protected-query cache keys; clear affected caches on logout or identity changes.
- After writes, update or invalidate only affected data. Define rollback for optimistic updates; stale request results must not overwrite newer searches or selections.
- Client-side permissions improve the interface; the server must still verify access and operation permissions.

## Styles and Verification

Follow the project's CSS Modules, styling system, or utility-class conventions. Keep page styles local and cross-page tokens centralized, avoiding accumulated global overrides.

Verify new interactions through user behavior: loading/failure/success, repeated clicks, and relevant permission or identity changes. Use integration or end-to-end checks where a workflow crosses APIs; passing type checks does not verify interaction behavior. Reuse architecture tests or lint rules when changing boundary constraints rather than creating a duplicate rule system.
