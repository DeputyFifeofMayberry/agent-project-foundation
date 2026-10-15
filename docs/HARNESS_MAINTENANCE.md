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

## Foundation as a maintained product

The foundation itself is reusable content, independently maintained in its own dedicated version-controlled repository — never as untracked files inside an adopting project, and never by editing the canonical/shared source in place. Changes are made in authorized isolated workspaces; the canonical source stays untouched.

A foundation release exists only after the proposed changes pass independent review and appropriate QA; the reviewed, verified state is then committed and tagged (annotated version tag matching `CHANGELOG.md`). Adoption and upgrade instructions state how new and existing projects adopt from that repository, and every adoption records the installed version (see `docs/ADOPTION.md`). Until a change completes that review-and-release path, the previous tagged version remains the last releasable state.
