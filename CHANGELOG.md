# Changelog

Template status is distinct from a real application release history.

Use release-oriented entries, not commit-by-commit duplication. Git records exact file history; ADRs document why important design decisions were made.

## Unreleased

_Nothing yet._

## v2.2 — 2026-10-15

### Changed

- P1-1 — preflight disposable staging/commit test made data-safe (`docs/CHECKLISTS.md`): empty-staging precondition (`git diff --cached --quiet`), path-limited probe commit, recorded `orig_ref` return instead of `checkout -`, and a per-safeguard failure-mode explanation.
- P1-2 — mandatory-doc gate reconciled to 19 enforced documents (adds `CHANGELOG.md`, `docs/RUNBOOKS.md`, `docs/REVIEW_EVIDENCE.md`, `docs/TECH_DEBT.md`); `docs/COMPONENTS.md` "Required for every project" matches `MANDATORY_DOCS` exactly; ADOPTION/COMPONENTS/STACKS/HARNESS_MAINTENANCE reclassified as adoption-time inventory, not gate-enforced.
- P2-1 — `docs/INDEX.md` permanent-standards table gains row 11: Git-workspace preflight (eight environment checks) before implementation, owned by `CHECKLISTS.md`.
- P2-2 — ZIP deliverable model retired: `INTERNAL_AUDIT_PROMPT.md` section F returns reports and corrected files via the `HARNESS_MAINTENANCE` release path; `AUDIT_REPORT.md` ZIP lines marked historical.
- P2-3 — `README.md` step 1: new repositories keep the copy instruction; existing repositories must not copy-paste and instead run the inspect-first procedure in `docs/ADOPTION.md`.
- P2-4 — `docs/ADOPTION.md`: one ordered inspect-first procedure is the single source for existing projects; the checklist-only Paperclip-gating item folded in as a step-8 note; exactly one readiness condition.
- P2-5 — `docs/STACKS.md`: one concrete minimum architecture-check command per stack section, labeled minimums and read-only-safe per `docs/CHECKLISTS.md`.
- P2-6 — two-attempt escalation rule owned canonically by `docs/agents/DEBUGGING.md`; the six other sites keep the rule and reference it as owner.
- P2-7 — `docs/agents/IMPLEMENTER.md` handoff template replaced by a pointer to `docs/agents/HANDOFF.md`; HANDOFF gains the unique fields (spec/PR link, rollback).
- P3-1 — `.github/CODEOWNERS.example` covers `/docs/CHECKLISTS.md`.
- P3-2 — `docs/INDEX.md`: foundation-meta row (SETUP_PROMPT, INTERNAL_AUDIT_PROMPT, AUDIT_REPORT, RESEARCH_DECISION, examples/) pointing at the COMPONENTS optional table, plus a CHECKLISTS.md domain row.
- P3-3 — journey counts phrased as one ramp: start 3–5 smoke journeys, grow to the 5–10 essential flows in `docs/PRODUCT.md` (PRODUCT/ADOPTION/RUNBOOKS aligned).
- P3-4 — `README.md` step 1 lists the foundation-meta files adopters should not copy (AUDIT_REPORT.md, INTERNAL_AUDIT_PROMPT.md, RESEARCH_DECISION.md, examples/).
- P3-5 — `docs/ADOPTION.md` step 2: one sentence on merging an existing `AGENTS.md`/`CLAUDE.md` (project rules win; foundation files linked from the project entry file).
- P3-7 — `docs/FRONTEND.md` and `docs/TESTING.md`: optional note that a bootable app per worktree (agent drives the real flow) is the preferred UI verification posture where feasible.
- P3-8 — `docs/CHECKLISTS.md` preflight provenance generalized to production-incident phrasing; organization-internal ticket IDs stay in this changelog only.
- P3-9 — `docs/RUNBOOKS.md` existing-app adoption reduced to a two-line summary pointing at `docs/ADOPTION.md`.
- P3-10 — no-op denylist documented honestly as a heuristic in `docs/CHECKLISTS.md`/`docs/TESTING.md` (documentation only; `scripts/verify.py` unchanged).

### Added

- P1-3 — fail-closed `not_applicable` mechanism in `.foundation/project.json` for `docs/DESIGN.md` and `docs/FRONTEND.md` (path→non-empty reason; whitelist-enforced, no schema bump), surfaced in `--list`/CI and covered by negative selftest fixtures; explained in `docs/COMPONENTS.md`, `docs/STACKS.md`, and `README.md`.
- Git-workspace preflight standard (board comment 719b0a4d; LOC-13 phases 18–19): eight permanent environment checks (valid HEAD; workspace exists; workspace writable; git administrative directories writable; staging and committing proven, not assumed; committed results persist outside temp workspaces; synchronization never discards modifications; isolated agents cannot overwrite each other's uncommitted work), a disposable staging/commit test procedure, and a stop-and-report-environment-blocker rule, codified in `docs/CHECKLISTS.md` after LOC-33 proved a read-only git metadata mount silently blocks staging (`index.lock` EROFS).

## v2.1

### Changed

- v2.1 finalization — ten permanent engineering standards codified into their owning documents (mapped in `docs/INDEX.md`): valid writable execution workspace before implementation; canonical preservation with changes in authorized isolated workspaces; version-controlled, independently maintained foundation content; implementation distinguished from verified application behavior; evidence tied to the exact tested content or commit; failed/unavailable tests never reported as passing; independently confirmed CI enforcement and branch protection; independent review + QA before foundation releases; recorded installed version and adaptations for every adoption; lessons evaluated for future foundation releases. Foundation released as tagged v2.1 from its dedicated version-controlled repository.
- v2.1 foundation improvement pass — encoded first-adoption lessons across the seven board areas: (a) component inventory with required/stack-conditional/optional classes (`docs/COMPONENTS.md`); (b) stack-adaptive new-project initialization procedure in `SETUP_PROMPT.md`; (c) inspect-first existing-project adoption procedure with per-step exit criteria in `docs/ADOPTION.md`; (d) verification-by-design rules (acceptance criteria first, risk-based selection, read-only checkout rule, app-vs-infrastructure split, no weakening to pass) in `docs/CHECKLISTS.md` and `docs/BASELINE.md`; (e) stack-specific minimum verification sets (`docs/STACKS.md`); (f) persistent-knowledge documentation standards in `docs/INDEX.md`; (g) reusable-lessons process in `docs/HARNESS_MAINTENANCE.md`.
- v2.0 audit: hardened verifier schema and self-tests, refreshed CI action versions, expanded user/onboarding/review guidance, corrected Paperclip security/retry assumptions, documented unresolved controls.

### Added

- Agent Project Foundation scaffold, verification contract, and adoption guides (not yet configured for a target application).
