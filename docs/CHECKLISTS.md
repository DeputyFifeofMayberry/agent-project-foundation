# Change checklists

## Before work

- [ ] Baseline branch, commit, and existing tests observed; `docs/BASELINE.md` updated
- [ ] Task scope, non-goals, acceptance criteria, unchanged behavior recorded
- [ ] Dependencies, integration points, security/data impact inventoried
- [ ] Valid, writable execution workspace established and verified **before** implementation (isolated branch/worktree with a valid HEAD, or an authorized isolated copy); canonical/shared sources preserved untouched; no unrelated changes touched
- [ ] Test strategy selected before implementation

## Definition of done

- [ ] All acceptance conditions demonstrated with evidence
- [ ] Real `python scripts/verify.py --ci` passed; log/output retained
- [ ] Appropriate regression, integration, E2E and negative-path checks ran
- [ ] No unauthorized weakening of tests, lint, CI, or security checks
- [ ] Runtime UI/device behavior exercised where applicable
- [ ] Security, performance, compatibility and migrations considered
- [ ] Docs, decision records, known debt and changelog updated as applicable
- [ ] Independent review completed with `docs/REVIEW_EVIDENCE.md` and product-owner approval where required
- [ ] Rollback path stated; no unresolved blocker disguised as success

## Reviewer rejection conditions

Unverified assumptions; insufficient test coverage; failure of mandatory checks; nonreproducible claimed fix; unrelated files changed; broken existing contracts; invented documentation; unapproved data/CI/security changes; visual evidence inconsistent with actual application; silent untested skips.

## Verification by design

- Acceptance criteria are written **before** implementation and describe observable behavior plus unchanged behavior (`docs/specs/SPEC_TEMPLATE.md`).
- Test selection is risk-based and tied to the documented risk level of the change (`docs/TESTING.md`), never to a fixed test count; justify the selection in the task record.
- Every gate maps to an executable command recorded in `.foundation/project.json`. "Verified" means the exact command, its revision, and the exit code are recorded (`docs/REVIEW_EVIDENCE.md`); evidence must be independently reproducible from the recorded commands, not dependent on attachments or screenshots alone.
- Evidence is tied to the reviewed revision: record the commit SHA with every result and re-run checks if the revision moves. When the tested state has no commit (adopted copies, artifact-only deliveries), record the exact content identity instead (source tree path plus a `sha256` manifest) so the tested content is unambiguous.
- Outcomes are classified explicitly: **PASS** (executed, expected result), **FAIL** (executed, failed), **NOT RUN**, **BLOCKED** (a missing prerequisite or permission — a blocker, never a pass), **SKIP with reason** (a skip never counts as success). The gate fails closed. A failed or unavailable check is never represented as passing in any report, handoff, status claim, or summary.
- Implementation is not verification: written or merged code is a claim, not a demonstrated behavior. Distinguish "the code was implemented" from "the application behavior was verified" in every status, report, and handoff; only executed checks on the actual behavior establish the latter (see the app-vs-infrastructure split below).
- CI enforcement and branch protection are confirmed independently of repository content — by observing actual enforcement (a rejected direct push, a PR blocked on the required check) or the platform's effective settings — never inferred from the presence of workflow files, templates, or documentation.
- Read-only checkout rule: verification must pass on a read-only checkout. Checks must not write bytecode, caches, or artifacts into the source tree (disable bytecode writing or route outputs to designated untracked paths). A check that cannot run in read-only mode is FAIL/BLOCKED, never success.
- App-vs-infrastructure split: classify every check as validating the **application** or the **foundation infrastructure**. A green gate proves infrastructure health only and is never application verification. Stack-specific verification must not be satisfiable by infrastructure-only checks (see `docs/STACKS.md`; for native iOS/macOS, Linux-runnable checks alone never verify the app).
- No weakening to pass: tests, lint, CI, verifier configuration, or their expected results must not be edited, removed, skipped, downgraded to warnings, or loosened to obtain a passing outcome. Such changes require explicit human approval and their own review evidence.
