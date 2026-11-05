# Review: Beginner New-Project Standard

Date: 2026-11-05 (Asia/Shanghai). Starting revision: `1a8f68e`; this review covers the local new-project-focus changes.

## Scope

The skill now helps beginners design/build a new React/Python project and continue it under the same standards. The assistant owns technical choices; the user supplies business goals, workflow and permissions. Arbitrary existing-project adaptation is outside implicit scope. Explicit user requirements and existing authorization boundaries still apply.

The short workflow connects business intent, the baseline, necessary structure, a real feature and first-run acceptance. References preserve feature ownership, layering, central APIs, YAML, logs, middleware lifecycle and current-document consistency, without multi-stack adaptation branches. Advanced patterns remain conditional.

Replacement evaluation cases focus on the actual beginner tasks. Workspace policies distinguish read-only work, design documents and implementation, avoiding the former assumption that every design output must leave the workspace unchanged.

## Verification

- The fixture contract was extended first to require an allowed workspace policy. It rejected the six old cases without that field; the replacement cases then passed the two dependency-free package checks. Isolated negative controls confirmed that missing and unknown policies are rejected.
- Skill frontmatter validation, metadata parsing, display-title agreement, README shell syntax and local documentation links/anchors passed. `git diff --check` found no whitespace errors.
- An independent read-only review found no supported scope conflict, lost required engineering constraint or authorization regression. It also ran the two package checks successfully.
- One independent beginner design task used an empty target directory and the supplied skill/references, without the expected checks. It recommended React/TypeScript/Vite, Python/FastAPI/Pydantic, npm/uv and SQLite for the small borrowing workflow; explained component responsibilities in ordinary language; and described future YAML/API/logging and first-run acceptance. The observed workspace contained one design Markdown document and no application scaffold. It did not introduce unrelated product names, table conventions or check commands. Reference reads and absence of dependency installation are agent-reported; the final document and workspace contents were independently inspected.
- The local Codex discovery API, with force reload in a neutral directory, returned exactly one enabled user skill with the updated description, display metadata and prompt, without discovery errors. The installed symlink still resolves to the source repository.
- B02 was subsequently executed once from an empty directory with the frozen local skill using gpt-6.1-sol/high. It generated a React/TypeScript/Vite + FastAPI/Pydantic + SQLite notes app. A separate clean source copy successfully repeated README installation, YAML preparation, 16 backend tests, the real process-restart helper, frontend production build, Chromium setup and five browser tests. Independent system-Chrome interaction confirmed a real save/list/reload and retention across a different backend process; desktop and 375px layouts were inspected. Four HTTP validation cases, six YAML/import/path/environment probes, and JSON-log/correlation/synthetic-content checks passed. Source and lockfiles remained unchanged during independent rehearsal. Verification reports, logs and screenshots are retained locally. After validation, the generated application, clean rehearsal copy, dependencies and synthetic database were removed at the owner's request; no application source was added to this skill repository.

## Limits

This is scoped authoring verification, one design forward check and one completed B02 first-run sample, not a repeated model benchmark. The previous broader-scope model runs are not results for these replacement cases. B03–B06 and repeated current/before/no-skill comparisons remain unrun. B02 was tested on macOS with its generated toolchain; other platforms, missing-tool installation branches and production deployment were not exercised. One upstream deprecation warning did not fail the tests. Independent rehearsal needed no application fixes; browser connection and service-control issues were confined to the evaluation harness. No general success rate or causal improvement claim is inferred. Skill discovery confirms availability, not future implicit invocation accuracy.
