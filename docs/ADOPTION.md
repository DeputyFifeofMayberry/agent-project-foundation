# Adoption checklist

Every adoption records the installed foundation version (see `../CHANGELOG.md`) and the project-specific adaptations it made, so audits and future upgrades know exactly what was installed and how it diverges.

## New application

- [ ] Define a minimal product and first five acceptance journeys.
- [ ] Choose stable, supported language, framework, package manager and runtime.
- [ ] Fill project-specific docs, observed baseline (`docs/BASELINE.md`), and schema-v2 `.foundation/project.json`.
- [ ] Implement real checks for all eight required categories or keep onboarding marked BLOCKED.
- [ ] Run `python scripts/selftest_verify.py` and confirm app `--ci` fails on an intentional regression.
- [ ] Set protected-branch rules before agents merge changes.
- [ ] Record the installed foundation version and the project-specific adaptations in `docs/BASELINE.md`.
- [ ] Add a task using `docs/agents/TASK_INTAKE_CRAFT.md`.

## Existing application

- [ ] Branch from the last known working commit; do not overwrite the existing repo.
- [ ] Inventory its actual framework, architecture, tests, package scripts, environment secrets and critical workflows.
- [ ] Record current passing and failing tests separately in `docs/BASELINE.md`; do not represent legacy failures as new regressions.
- [ ] Add only the foundation docs that provide immediate value, merge existing project instructions carefully.
- [ ] Establish all required gate categories without replacing missing coverage with no-op commands. If not ready, keep CI red and adoption incomplete.
- [ ] Add regression coverage for frequently broken features first.
- [ ] Record the installed foundation version and the project-specific adaptations in `docs/BASELINE.md`.
- [ ] Wire Paperclip only after a direct coding-agent run reliably builds and tests the app.

## Inspect-first adoption procedure (existing projects)

Template copy-paste is prohibited for existing repositories. Run these steps in order and do not start the next step until the previous step's exit criterion holds; record the evidence named per step.

1. **Inventory (read-only).** From a read-only checkout, enumerate the actual stack, modules, scripts, tests, CI, deployment targets, existing agent instructions, and critical user journeys; capture current Git status. Record in `docs/BASELINE.md`. *Exit:* every inventory line cites a real file or command; nothing invented.
2. **Conventions and functioning docs.** Identify existing conventions (naming, structure, test layout) and which existing documents already work. *Exit:* a written keep-as-is list with reasons; conflicts with foundation docs named explicitly.
3. **Known baseline.** Record observed passing/failing checks and known defects in `docs/BASELINE.md`, separating pre-existing failures from anything introduced later. *Exit:* baseline commit SHA recorded; legacy failures labeled as legacy.
4. **Safe workspace.** Move into an isolated writable branch/worktree created from the last known working commit; never edit a shared primary checkout directly. (If the repository has no VCS, use an isolated writable copy and schedule VCS initialization as the first rollout item.) *Exit:* workspace writable with valid HEAD (or, for no-VCS repos, an isolated writable copy); pre-existing changes preserved and listed.
5. **Gap matrix.** Compare the repository against the foundation component inventory (`docs/COMPONENTS.md`) and classify every component: **Adopted** (installed and configured), **Adapted** (merged with an existing equivalent), **Present-sufficient** (repo equivalent already works; foundation copy skipped, pointer recorded), **NA-justified** (not applicable to this stack, reason recorded), or **Missing** (required and absent — must be scheduled). Record the installed foundation version alongside the gap matrix. *Exit:* every inventory row classified; installed foundation version and project-specific adaptations recorded; no row silently skipped.
6. **Severity-prioritized incremental rollout.** Order Missing/Adapted work by risk to critical journeys and adopt in small, independently verifiable increments; each increment configures real checks, runs the gate, and records evidence. *Exit:* rollout plan documented; first increment verified end-to-end.
7. **Commit gating.** Commits, merges, and pushes are human-approved. The agent deliverable is a documented exact commit plan (files, order, messages), not an executed integration into shared branches. *Exit:* commit plan approved through the authorized path before integration.

**Readiness condition:** required markers replaced, commands configured, negative test verified to fail, branch ruleset independently verified, installed foundation version and adaptations recorded.
