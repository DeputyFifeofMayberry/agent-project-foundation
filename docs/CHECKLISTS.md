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

## Git-workspace preflight (permanent standard)

Established after LOC-33/LOC-34 (fifecode-ios): a workspace whose working tree is writable but whose git metadata sits on a read-only mount silently blocks staging (`index.lock: Read-only file system`), so "files written" is not evidence that a commit is possible. Run all eight checks **before** implementation, and re-run whenever the workspace, its mount, or host environment changes:

1. **Valid HEAD** — `git rev-parse HEAD` resolves to a real commit; record the SHA and expect it to match the task's authorized baseline.
2. **Execution workspace exists** — the assigned workspace path is the intended checkout/clone (not an empty default agent directory); confirm the intended branch.
3. **Workspace writable** — create and remove a probe file in the working tree.
4. **Git administrative directories writable** — create and remove a probe file **inside `.git`** (this is where `index.lock` and other locks live; a read-only mount fails here even when checks 1–3 pass). Record the filesystem state, e.g. `findmnt -T <repo>` showing `rw`.
5. **Staging and committing supported** — prove the full write path with the disposable test below; never assume it from checks 3–4.
6. **Committed results persist outside temporary workspaces** — the repository (`.git` and working tree) lives in persistent storage (project or agent-home data), not a recreated-per-run temp workspace, so commits survive workspace recycling.
7. **Workspace synchronization will not discard modifications** — before any tooling-driven sync, clean, rebase, or checkout, confirm from current evidence (`git status --porcelain`) that uncommitted work survives it; destructive resets/cleans/force-checkouts over dirty state are prohibited without explicit authorization.
8. **Isolated agents cannot overwrite each other's uncommitted work** — each agent works in its own isolated worktree/clone; before touching a workspace, confirm any dirty state belongs to you (or is preserved untouched); never overwrite another agent's changes.

### Disposable staging/commit test

Prove staging and committing on a disposable branch (or a disposable clone when the target branch is protected/shared), record the outputs, then discard the probe. Preconditions: proceed only when the working tree is clean or the dirty state is explicitly recorded and restored after the probe, and require an empty staging area via `git diff --cached --quiet`; otherwise abort **BLOCKED** instead of running the probe. Record the branch `HEAD` refers to before creating the probe branch and abort if `HEAD` is detached:

```bash
git diff --cached --quiet || { echo 'BLOCKED: staging area not empty' >&2; exit 1; }
orig_ref=$(git rev-parse --abbrev-ref HEAD) || { echo 'BLOCKED: detached HEAD' >&2; exit 1; }
git checkout -b preflight-probe
echo probe > PROBE.txt
git add PROBE.txt && git commit -m "preflight probe" -- PROBE.txt   # path-limited commit; must succeed; record SHA
git checkout "$orig_ref" && git branch -D preflight-probe           # discard probe; workspace returns to baseline
```

Each safeguard prevents a specific failure mode. The empty-staging precondition (plus explicitly recording any dirty state and restoring it afterward) prevents the probe from sweeping pre-existing staged or unstaged work into its commit or deleting it with the probe branch. The path-limited `-- PROBE.txt` commit ensures pre-staged work can never be swallowed by the probe commit even if the precondition check was skipped. Recording `orig_ref` up front and returning via `git checkout "$orig_ref"` — never `git checkout -` — prevents the workspace from being left on the probe branch or on whichever branch `-` happens to resolve to, and the detached-HEAD abort prevents a probe that has no defined return point.

Use a designated persistent scratch location for any disposable clone (never a read-only or per-run temp path). A probe that succeeds elsewhere does not certify the target workspace — checks 3–4 must still pass there.

### Preflight failure is an environment blocker

If any check fails: **stop**. Do not implement, do not work around with destructive git operations, and do not report partial success. Record the exact command, the exact error (e.g. `index.lock: Read-only file system`), the filesystem evidence, and the next action on the assigned issue, classified **BLOCKED**; wait for an authorized resolution (e.g. a persistent writable repository) before continuing.
