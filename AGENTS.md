# Agent instructions: start here

This file is a map, not an encyclopedia. The source of truth lives in the repository and `docs/INDEX.md`. Read only task-relevant files, but **always** apply the gates below.

## Non-negotiable rules

1. Before editing: inspect repository status, read `README.md`, relevant specs, `docs/BASELINE.md`, architecture, and test guidance; establish a baseline. Preserve unrelated user or agent changes. Never reset, overwrite, or force-push them.
2. For each nontrivial task, write acceptance criteria describing observable behavior and unchanged behavior; use `docs/specs/SPEC_TEMPLATE.md`. On uncertain product decisions or destructive changes, request approval.
3. Work in a separate branch/worktree when available. Keep diffs small, avoid opportunistic refactors, and do not silently change public contracts, persistence formats, authentication, or security boundaries.
4. For bug fixes: reproduce the issue first; add a regression test that fails before the fix when feasible. After two failed attempted fixes, stop patching and use `docs/agents/DEBUGGING.md`, the canonical owner of this two-attempt rule.
5. Use structured validation at external boundaries, least privilege, no secrets in source/logs, and no undocumented destructive data migrations. Follow `docs/SECURITY.md`.
6. Execute `.foundation/project.json` checks via `python scripts/verify.py --ci`. Do not mark tasks complete if required checks fail, are skipped, or are unconfigured. The template is deliberately unconfigured: onboarding must be completed first. Record exact command, result, and relevant runtime evidence.
7. For UI tasks verify the real user flow, failure state, and target device/screen; browser compilation alone is not acceptance. See `docs/FRONTEND.md`.
8. Do not edit, remove, or weaken tests, CI, verification scripts, or their configuration just to make a failure pass. Such changes need explicitly justified human approval.
9. Update affected product docs, ADRs, plans, `CHANGELOG.md` when release-visible, and `docs/TECH_DEBT.md` when deferring known issues. Don't claim unseen code or unrun tests are verified.
10. Deliver a concise change summary: files changed, behavior verified, exact pass/fail evidence, unresolved risks, and rollback path. A reviewer independent of the implementation must approve substantive work; product acceptance is separate. Follow `docs/REVIEW_EVIDENCE.md`.

## Find context

- Scope/user intent: `docs/PRODUCT.md`, `docs/PRODUCT_SENSE.md`, `docs/specs/`
- System design: `ARCHITECTURE.md`, `docs/decisions/`
- UI: `docs/DESIGN.md`, `docs/FRONTEND.md`
- Quality: `docs/TESTING.md`, `docs/RELIABILITY.md`, `docs/SECURITY.md`, `docs/QUALITY_SCORE.md`, stack check minimums: `docs/STACKS.md`
- Task workflow: `docs/agents/`, `docs/plans/`, `docs/CHECKLISTS.md`
- Orchestration: `docs/orchestration/`, `docs/agents/ORCHESTRATOR.md`
- Owner instructions: `docs/USER_GUIDE.md`; current baseline: `docs/BASELINE.md`; maintenance: `docs/HARNESS_MAINTENANCE.md`

These instructions apply whether the agent is launched from OpenCode, Codex, Paperclip, Symphony, or manually. Orchestrator status is not equivalent to repository verification or user acceptance.
