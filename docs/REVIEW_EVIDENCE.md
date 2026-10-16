# Review evidence contract

For any substantive task, produce a PR note or durable file that names:

- Issue/spec ID, baseline commit, branch/worktree, final commit.
- Acceptance criterion IDs and evidence for each (tests, reproduction before/after, console traces, screenshots/videos where applicable).
- Exact verification command(s), platform/runtime, exit codes, CI URL, and checks not run.
- Before/after behavior for affected critical journeys, including failure paths and persistence.
- Security, dependency, compatibility, migrations, and rollout/rollback impact.
- Independent reviewer decision (APPROVE / REQUEST_CHANGES / BLOCKED), with unresolved concerns.
- Product owner acceptance (separate from reviewer approval), when required.

An orchestrator run ending with exit code zero is *not* acceptance evidence. A local success does not replace protected CI, and an agent's generated screenshot must represent the actual tested app and commit.

## Release evidence (protected repository releases)

Releasing to a protected repository additionally requires evidence, for the exact released revision, that:

- Invalid changes are blocked by the required check.
- Valid changes proceed through the normal protected pull-request workflow and merge.
- Neither demonstration depends on bypassing branch protections; any bypass follows the authorization, rationale, restoration, and defect-evaluation policy in `docs/RUNBOOKS.md` (GitHub setup, canonical owner) and never substitutes for either demonstration.
- The exact required check names match the repository's configured workflow jobs and validate the repository's actual purpose (foundation home: `maintenance`; adopting application: configured `verify`).
- The same checks remain functional after publication.

`python scripts/check_required_checks.py --required <name>[,<name>...]` supplies the local part (names match workflow jobs and pass on the tree); hosted enforcement is confirmed with the procedure in `docs/RUNBOOKS.md` (GitHub setup step 6).
