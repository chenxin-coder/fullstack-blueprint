# Skill Evaluation

Evaluate whether a beginner can get a small project built and run it using the supplied instructions. Cases in [cases.json](cases.json) cover new-project design/build and continued work under the same blueprint. They are maintenance fixtures, not runtime instructions.

## Routing

For metadata classification, give the evaluator only the skill name, description and one candidate prompt, without the expected invoke value or rationale. Use independent contexts and record each decision. This measures applicability judgment, not actual host loading. Test native implicit invocation separately with competing skills and real skill-load traces. Explicit invocation keeps the user's requested scope. Unrelated existing-project adaptation is a negative case.

## Behavior and Workspace Policy

Give the execution model the task, minimum real project artifacts, the skill and the case's resource/workspace policy; withhold the checks and prior conclusions. Load references normally. Each behavior case declares what writes are allowed:

| Policy | Allowed changes |
|---|---|
| `read_only` | No workspace file changes; collect the answer outside it |
| `design_documents_only` | The requested proposal/design documents; no application scaffold, dependencies or business implementation |
| `implementation` | Files needed for the authorized implementation, tests and current documentation |

Communicate the policy as an execution boundary, not an expected answer. A design document is a valid design deliverable when allowed; do not classify its creation as application implementation. Compare before/after manifests and inspect actual artifacts, not only the model's final claims.

Use a genuinely isolated working directory and target-scoped instructions. Exclude a run contaminated by another project's product names, tables or quality commands, preserve its evidence, and rerun with the unrelated context removed. Do not count such contamination as a skill defect without isolation evidence.

## First-Run Rehearsal

B02 is an executable acceptance case, not a design review. Provide the declared tools/dependency access, then follow the generated README in a fresh checkout: install from lockfiles, prepare safe YAML, start both services, open the documented address, create/list a note and restart the backend to check persistence. Run the documented tests and frontend build. Use browser interaction when available; state explicitly when only API or source behavior was checked. Record missing tools/services and commands that failed; they cannot support a successful first-run claim.

B03 checks a small continuation, B04 YAML startup behavior, B05 needed middleware lifecycle, and B06 approved continuation with documentation consistency. Use synthetic secrets and fake SDKs; state where real integration remains unverified. Git tests, if requested, use a local bare remote. No live systems or user global configuration need modification.

For B02's database-key check, inspect the created table constraints and insert real rows without supplying `id`; an ORM declaration alone is insufficient. Verify generated integer keys and business/replay uniqueness separately. Earlier B02 runs predate this added check and do not establish its result.

## Comparison and Evidence

Use the same model and settings for no-skill and before/after comparisons in fresh contexts. Repeat each case at least five times before reporting selection rates or wording reliability. Keep actual inputs, outputs, tool traces when available, file differences, commands and every violated check. A single round is a smoke observation, not a stable success rate or proof of improvement.

- **Package validation:** Local links/anchors and fixture fields, identities, types and workspace policies. This does not measure model behavior.
- **Author review:** Source inspection against the intended beginner workflow, not an independent execution.
- **Model evaluation:** Actual selection, actions and generated artifacts. Separate independent observations from model-reported commands/read inventories and mark unrun cases clearly.

The [new-project focus review](review-2026-11-05-new-project-focus.md) records current verification. The [earlier review](review-2026-11-05.md) concerns the previous broader scope and does not establish results for these replacement cases.
