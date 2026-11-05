# Skill Evaluation

These cases test discovery boundaries and application behavior. They are maintenance fixtures, not additional runtime skill instructions. The prompts and checks are in [cases.json](cases.json).

## Routing

Give an evaluator the skill's name and description alongside the candidate prompt, before revealing the expected `invoke` value or rationale. Check implicit selection separately from explicit invocation. Read-only engineering reviews are positive cases; existing-code explanations without a design or review request are negative cases. An explicit invocation loads the skill but does not expand the requested work.

## Behavior

Give an evaluator the full skill, only the repository artifacts described by the case, and the prompt. Load references through the skill's normal routing. Assess the resulting actions and artifacts against each check, not whether the answer repeats the skill's wording. Explanations and design-only cases must leave the fixture workspace unchanged.

For model-based comparison, use the same model and settings, record the skill revision, and run a no-skill control plus the before/after variants in fresh contexts. Repeat each case at least five times when reporting selection rates or wording reliability. Keep raw outputs and record every violated check, including failures that keyword matching misses. Use isolated fixture workspaces; commit/push behavior may be simulated with local bare remotes rather than a live repository.

## Evidence Levels

- **Package validation:** Frontmatter, metadata, JSON fixtures, local links, and Markdown anchors can be checked deterministically. This does not test model selection or compliance.
- **Author review:** Inspect the actual rules against the cases and record conflicts or resolutions. This is not an independent behavioral run.
- **Model evaluation:** Record actual selection, actions, and outputs from fresh-context runs. Report results only for runs that took place; unavailable evaluations remain unrun.

The [2026-11-05 review](review-2026-11-05.md) records the baseline findings, changes, checks, and limitations for this revision.
