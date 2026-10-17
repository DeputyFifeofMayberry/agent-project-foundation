# Changelog

Template status is distinct from a real application release history.

Use release-oriented entries, not commit-by-commit duplication. Git records exact file history; ADRs document why important design decisions were made.

## Unreleased

_Nothing yet._

## v2.2.2 — 2026-10-16

Correction release for required-check validator scoping (observed failure: an unrelated workflow file that uses GitHub features outside the validator's supported subset — for example an adopter-owned workflow with a step-level `env:` block mapping secrets — failed the whole required-check gate even though it implemented none of the configured required checks, so adopters' own workflows broke the template's validation).

### Fixed

- `scripts/check_required_checks.py` now parses workflow files independently and validates only the workflows that implement the configured required checks (matched by job id or job name from the check context); unrelated workflow files are left unvalidated, reported with a `NOTE` line instead of failing the gate. Fail-closed semantics are preserved: a required check that no parsable workflow implements still fails through the normal no-match path, and a workflow file that declares a configured required check but cannot be validated fails immediately.
- Required-check classification respects explicit job display names and inline YAML comments, and fails closed on unreadable workflows: a job id that matches a required check but declares a different display name (e.g. `verify:` plus `name: Deploy previews`) is no longer recorded as that required check; `name: verify # comment` compares as `verify` in both parsed and unparsed classification; a workflow file that cannot be read is an immediate validation failure instead of an empty unrelated classification.

### Added

- Regression coverage in `scripts/selftest_verify.py`: an unrelated workflow with a step-level secrets `env:` block no longer fails the required-check gate, while a required-check workflow with the same content still fails closed.
- Regression coverage in `scripts/selftest_verify.py` for the classification edge cases above: display-name mismatch not recorded as the required check, inline-comment job name matched, and unreadable workflow file fails closed.
- `docs/ADOPTION.md`: CRLF-safe adoption packaging guidance — regenerate the delta on the canonical LF base and verify tree equivalence before delivery — for adopters whose local histories store CRLF line endings.
- `docs/RUNBOOKS.md`: strict-protection merge-cascade runbook step — branches fall behind after each protected merge, dependent branches are updated in waves, and `--admin` merges never substitute for correcting the cascade.

## v2.2.1 — 2026-10-15

Correction release for the required-check guidance (observed failure: the hosted `main` protection required the `verify` status check, which is intentionally fail-closed red until an adopting project configures real checks, so the foundation home deadlocked — no ordinary maintenance change could merge through the protected workflow — and the misconfiguration was masked by a bypass instead of corrected; one-sided enforcement evidence, a blocked failing PR alone, had been accepted as verification). Rules that prevent recurrence, owned canonically by `docs/RUNBOOKS.md` (GitHub setup): required checks must validate the repository's actual purpose (foundation home: `maintenance`; adopting application: its configured `verify` check after adoption), enforcement is verified only with both a successful and a failing change, and any bypass requires explicit authorization, documented rationale, restoration evidence, and defect evaluation — a bypass never proves the normal workflow functions.

### Changed

- `docs/RUNBOOKS.md` GitHub setup is the single canonical owner of the required-check rule, the foundation-vs-adopter distinction, both-path enforcement verification, and the bypass policy; other documents reference it instead of restating it. GitHub setup step 3 no longer mandates the `verify` check for every repository, and `docs/HARNESS_MAINTENANCE.md` step 7 (Publication) requires `maintenance` for the foundation home rather than hard-coding `verify`.
- `docs/CHECKLISTS.md`, `docs/ADOPTION.md`, and `docs/REVIEW_EVIDENCE.md` aligned by reference: release evidence must show invalid changes blocked, valid changes merging through the normal protected workflow, no dependence on bypassing controls, exact required checks matching configured workflows, and checks remaining functional after publication.
- `README.md`: stale v2.1 heading updated to the current version; start-here step 8 points at the canonical rule instead of a universal `verify` requirement.

### Added

- `scripts/check_required_checks.py`: fail-closed local validation that each required check name matches exactly one configured workflow job and that the job's run steps pass on the current tree; nonexistent names, ambiguous matches, failing jobs, matrix/conditional/otherwise locally-unverifiable jobs, and unsupported workflow content all fail closed.
- Permanent lightweight regression coverage in `scripts/selftest_verify.py` for protected-branch scenarios (c) unconfigured adopter fails closed, (d) configured adopter passes, (f) nonexistent required check fails, (g) red required check fails release readiness; hosted scenarios (a), (b), and the merge-block half of (e) are documented in `docs/RUNBOOKS.md` (GitHub setup step 6) and mapped per scenario in `docs/TESTING.md`.
- Agent-contract additions: `docs/agents/IMPLEMENTER.md` (confirm required checks match the intended workflow, demonstrate successful integration without a bypass, escalate workflow defects), `docs/agents/REVIEWER.md` (independently confirm effective protections and required checks on both paths, reject one-sided evidence), `docs/agents/ORCHESTRATOR.md` (acceptance covers operational success and failure, cross-component configuration reviewed as one system, no acceptance while a workaround conceals a defect, corrections must address the original failure), and QA duties in `docs/TESTING.md` (positive and negative protected-branch integration tests on the actual release workflow; flag bypass-dependent releases).

Backward compatible: documentation plus additive local coverage only; no `MANDATORY_DOCS`, schema, or gate-behavior changes. CI architecture confirmed unchanged: one workflow, two jobs — the foundation home requires the green `maintenance` job; the `verify` job stays fail-closed red until an adopter configures real checks and only adopters require it.

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
- `.gitignore` expanded from minimal exclusions to curated coverage of supported tooling (Python, Node.js, Swift/Xcode), operating-system artifacts, editor local state with shared configuration preserved, local agent/orchestration runtime state, and secret material; lockfiles and `.env.example` remain tracked.
- Maintenance documentation updated for the public operating model: the publication home is the public repository `DeputyFifeofMayberry/agent-project-foundation` with enforced `main` protection (pull-request-only integration, required `verify` check, no force pushes or deletions, administrators included) and protected `v2.*` release tags.

### Added

- P1-3 — fail-closed `not_applicable` mechanism in `.foundation/project.json` for `docs/DESIGN.md` and `docs/FRONTEND.md` (path→non-empty reason; whitelist-enforced, no schema bump), surfaced in `--list`/CI and covered by negative selftest fixtures; explained in `docs/COMPONENTS.md`, `docs/STACKS.md`, and `README.md`.
- Foundation-maintenance CI job `maintenance` in `.github/workflows/verify.yml`: runs the verifier self-test (positive and negative fixtures) and configuration sanity, giving the repository a green, meaningful gate for the reusable foundation itself; adopter-application verification (`verify`) remains fail-closed until real project checks are configured.
- Git-workspace preflight standard (board comment 719b0a4d; LOC-13 phases 18–19): eight permanent environment checks (valid HEAD; workspace exists; workspace writable; git administrative directories writable; staging and committing proven, not assumed; committed results persist outside temp workspaces; synchronization never discards modifications; isolated agents cannot overwrite each other's uncommitted work), a disposable staging/commit test procedure, and a stop-and-report-environment-blocker rule, codified in `docs/CHECKLISTS.md` after LOC-33 proved a read-only git metadata mount silently blocks staging (`index.lock` EROFS).

## v2.1

### Changed

- v2.1 finalization — ten permanent engineering standards codified into their owning documents (mapped in `docs/INDEX.md`): valid writable execution workspace before implementation; canonical preservation with changes in authorized isolated workspaces; version-controlled, independently maintained foundation content; implementation distinguished from verified application behavior; evidence tied to the exact tested content or commit; failed/unavailable tests never reported as passing; independently confirmed CI enforcement and branch protection; independent review + QA before foundation releases; recorded installed version and adaptations for every adoption; lessons evaluated for future foundation releases. Foundation released as tagged v2.1 from its dedicated version-controlled repository.
- v2.1 foundation improvement pass — encoded first-adoption lessons across the seven board areas: (a) component inventory with required/stack-conditional/optional classes (`docs/COMPONENTS.md`); (b) stack-adaptive new-project initialization procedure in `SETUP_PROMPT.md`; (c) inspect-first existing-project adoption procedure with per-step exit criteria in `docs/ADOPTION.md`; (d) verification-by-design rules (acceptance criteria first, risk-based selection, read-only checkout rule, app-vs-infrastructure split, no weakening to pass) in `docs/CHECKLISTS.md` and `docs/BASELINE.md`; (e) stack-specific minimum verification sets (`docs/STACKS.md`); (f) persistent-knowledge documentation standards in `docs/INDEX.md`; (g) reusable-lessons process in `docs/HARNESS_MAINTENANCE.md`.
- v2.0 audit: hardened verifier schema and self-tests, refreshed CI action versions, expanded user/onboarding/review guidance, corrected Paperclip security/retry assumptions, documented unresolved controls.

### Added

- Agent Project Foundation scaffold, verification contract, and adoption guides (not yet configured for a target application).
