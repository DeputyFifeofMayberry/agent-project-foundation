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
