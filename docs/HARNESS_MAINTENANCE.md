# Harness maintenance and drift prevention

Once per release (or monthly for actively changing projects):

1. Check documentation against actual code and runtime behavior. Update stale module links and the baseline.
2. Audit test coverage against the current five most important product journeys. Add tests for escaped defects.
3. Review repository checks, action versions, lockfiles, dependency security, and any flaky test trends.
4. Review `docs/TECH_DEBT.md` and `docs/QUALITY_SCORE.md`; retire obsolete exceptions or narrow architecture debt in a focused PR.
5. Test the gate itself with a deliberate failing test in a disposable branch (never merge it).
6. Review Paperclip adapter permissions, timeouts, unexpected tool access, pending subagents, failed runs, and evidence gaps.
7. Record changes to the harness and rationale in an ADR if they affect its enforcement model.

Never allow the maintenance agent to bypass product-owner approval for workflow, test, or security gate relaxation.

## Lessons process

Classify every failure, review finding, or friction observed during real work before any rule changes:

- **Task-specific:** caused by one task's content. Fix the task; change no harness rules.
- **Repo-specific:** caused by this repository's setup. Fix it in this repo's docs/config only.
- **Reusable:** likely to recur in other projects or future adoptions. Candidate for a foundation change.

A reusable lesson becomes a foundation change only with all three of: (1) documented rationale naming the observed failure and the rule that prevents it, (2) independent review of the proposed change, and (3) a `CHANGELOG.md` version entry. Workarounds improvised during a task are never auto-promoted to universal rules; a workaround must pass through this classification and review before it changes the harness. Lessons learned are re-evaluated at each release for incorporation into future foundation releases; a lesson deferred is recorded, not discarded.

## Improvement-to-release process

How a foundation change moves from request to published release:

1. **Submission.** Improvement requests are filed as scoped issues against the foundation repository, by the board, an adopting project, or an agent. Each request states the observed problem (failure, friction, or drift), the affected documents or checks, and the proposed change.
2. **Evaluation and priority.** Each request is classified with the lessons process above. Reusable requests are prioritized by risk: security and fail-closed verification first, then enforcement gaps and documentation drift, then convenience.
3. **Implementation assignment.** An approved request is assigned to one implementing agent as a scoped task with acceptance criteria. Implementation happens in an authorized isolated workspace on a release branch, never by editing canonical `main` in place (`docs/CHECKLISTS.md`; `docs/agents/IMPLEMENTER.md`).
4. **Independent review.** Every change is reviewed by someone other than its implementer, with appropriate QA, before it can merge or release (see "Foundation as a maintained product" below). An implementer never self-approves.
5. **Required tests before merging.** `scripts/selftest_verify.py` passes, the affected `scripts/verify.py` scenarios are demonstrated (positive and negative, in a disposable copy), documentation links and configuration validate, and CI is green; evidence is recorded per `docs/REVIEW_EVIDENCE.md`.
6. **Version and changelog.** Every merged change carries a `CHANGELOG.md` entry under `Unreleased`. Cutting a release moves the released items under a dated version heading and leaves only genuinely post-release items in `Unreleased`; the release is tagged with an annotated tag whose name matches the changelog version.
7. **Publication.** Releases are published to the public GitHub home: repository `DeputyFifeofMayberry/agent-project-foundation` with protected `main` — pull-request-only integration with the required `maintenance` status check (strict), the foundation-validity check; no force pushes, no deletions, enforced for administrators — and protected release tags (`v2.*` cannot be deleted or force-updated). One annotated tag per release. The canonical required-check rule — including the foundation-vs-adopter distinction and the bypass policy — is owned by `docs/RUNBOOKS.md` (GitHub setup); adoption repositories require their configured `verify` check instead. Publication is a governed action taken only after review, QA, and any required human approval — never directly from an implementation task. Independent Paperclip review and human acceptance are procedural gates; GitHub itself enforces the PR requirement and status checks, not reviewer approvals (single-administrator repository).
8. **Breaking changes.** A change is breaking when adopters must modify their repositories or workflows: an enforced document added, removed, or renamed; `MANDATORY_DOCS` or the `.foundation/project.json` schema changed; or gate behavior altered in a way that fails previously passing repositories. Breaking changes are stated in the changelog entry, bump the major version, and describe the upgrade path.
9. **Adopter updates.** Adopting projects learn about updates through the repository's annotated tags and this changelog. `docs/ADOPTION.md` is the upgrade procedure for existing projects, and every adoption records the installed version and project-specific adaptations.

## Foundation as a maintained product

The foundation itself is reusable content, independently maintained in its own dedicated version-controlled repository — never as untracked files inside an adopting project, and never by editing the canonical/shared source in place. Changes are made in authorized isolated workspaces; the canonical source stays untouched.

A foundation release exists only after the proposed changes pass independent review and appropriate QA; the reviewed, verified state is then committed and tagged (annotated version tag matching `CHANGELOG.md`). Adoption and upgrade instructions state how new and existing projects adopt from that repository, and every adoption records the installed version (see `docs/ADOPTION.md`). Until a change completes that review-and-release path, the previous tagged version remains the last releasable state.
