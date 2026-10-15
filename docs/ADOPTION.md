# Adoption checklist

Every adoption records the installed foundation version (see `../CHANGELOG.md`) and the project-specific adaptations it made, so audits and future upgrades know exactly what was installed and how it diverges.

## New application

- [ ] Define a minimal product and the first 3–5 acceptance journeys — the start of the journey ramp that grows to the 5–10 essential flows in `docs/PRODUCT.md`.
- [ ] Choose stable, supported language, framework, package manager and runtime.
- [ ] Fill project-specific docs, observed baseline (`docs/BASELINE.md`), and schema-v2 `.foundation/project.json`.
- [ ] Implement real checks for all eight required categories or keep onboarding marked BLOCKED.
- [ ] Run `python scripts/selftest_verify.py` and confirm app `--ci` fails on an intentional regression.
- [ ] Set protected-branch rules before agents merge changes.
- [ ] Record the installed foundation version and the project-specific adaptations in `docs/BASELINE.md`.
- [ ] Add a task using `docs/agents/TASK_INTAKE_CRAFT.md`.

## Inspect-first adoption procedure (existing projects)

The single ordered source for adopting the foundation into an existing repository; no separate existing-project checklist exists. Template copy-paste is prohibited for existing repositories. Run these steps in order and do not start the next step until the previous step's exit criterion holds; record the evidence named per step.

1. **Inventory (read-only).** From a read-only checkout, enumerate the actual stack, modules, scripts, package scripts, tests, CI, deployment targets, environment secrets, existing agent instructions, and critical user journeys; capture current Git status. Record in `docs/BASELINE.md`. *Exit:* every inventory line cites a real file or command; nothing invented.
2. **Conventions and functioning docs.** Identify existing conventions (naming, structure, test layout) and which existing documents already work. If an `AGENTS.md` or `CLAUDE.md` already exists, merge foundation rules into it rather than replacing it — project rules win, and foundation files are linked from the project's entry file. *Exit:* a written keep-as-is list with reasons; conflicts with foundation docs named explicitly.
3. **Known baseline.** Record observed passing/failing checks and known defects in `docs/BASELINE.md`, separating pre-existing failures from anything introduced later. *Exit:* baseline commit SHA recorded; legacy failures labeled as legacy.
4. **Safe workspace.** Move into an isolated writable branch/worktree created from the last known working commit; never edit a shared primary checkout directly. (If the repository has no VCS, use an isolated writable copy and schedule VCS initialization as the first rollout item.) *Exit:* workspace writable with valid HEAD (or, for no-VCS repos, an isolated writable copy); pre-existing changes preserved and listed.
5. **Gap matrix.** Compare the repository against the foundation component inventory (`docs/COMPONENTS.md`) and classify every component: **Adopted** (installed and configured), **Adapted** (merged with an existing equivalent), **Present-sufficient** (repo equivalent already works; foundation copy skipped, pointer recorded), **NA-justified** (not applicable to this stack, reason recorded), or **Missing** (required and absent — must be scheduled). Record the installed foundation version alongside the gap matrix. *Exit:* every inventory row classified; installed foundation version and project-specific adaptations recorded; no row silently skipped.
6. **Severity-prioritized incremental rollout.** Order Missing/Adapted work by risk to critical journeys and adopt in small, independently verifiable increments. Add only foundation components that provide immediate value; merge existing project instructions carefully rather than overwriting them; add regression coverage for frequently broken features first. Each increment configures real checks, runs the gate, and records evidence; never replace missing coverage with no-op commands — if not ready, keep CI red and adoption incomplete. *Exit:* rollout plan documented; first increment verified end-to-end.
7. **Commit gating.** Commits, merges, and pushes are human-approved. The agent deliverable is a documented exact commit plan (files, order, messages), not an executed integration into shared branches. *Exit:* commit plan approved through the authorized path before integration.
8. **Paperclip gating (note).** Wire Paperclip only after a direct coding-agent run reliably builds and tests the app in the adopted repository; orchestration tooling comes after that baseline exists, not before.

**Readiness condition:** required markers replaced, commands configured, negative test verified to fail, branch ruleset independently verified, installed foundation version and adaptations recorded.
