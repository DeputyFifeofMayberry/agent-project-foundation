# Test and verification strategy

## Required baseline (configure commands)

- Code formatting / lint: TODO_REQUIRED
- Static type checks (if typed language): TODO_REQUIRED
- Unit tests: TODO_REQUIRED
- Integration or contract tests: TODO_REQUIRED
- Critical-path E2E tests: TODO_REQUIRED
- Production build or platform build: TODO_REQUIRED
- Architecture/security static checks: TODO_REQUIRED

These eight required categories are enforced by `scripts/verify.py` reading schema v2 `.foundation/project.json`; removing a category from the config is invalid. Disabled or missing checks are treated as incomplete during `--ci`. Only configure real commands that fail on defective behavior. The verifier detects obvious no-ops but cannot establish test meaningfulness automatically; reviewers must examine test behavior. Do not replace tests with `echo pass` or equivalent.

## Test design

Prefer observable behavior and contracts over implementation coupling. For each prior regression, preserve a test reproducing the failure unless technically impossible and explicitly documented. Isolate external integrations using deterministic fixtures; add a smaller number of controlled end-to-end smoke tests against real integrations when warranted.

Optional for UI projects: where feasible, the preferred verification posture is a bootable app per worktree — each isolated worktree can build and launch the real application so an agent can drive the actual user flow rather than reasoning over mocks (`docs/FRONTEND.md`).

## Test inventory

| User journey / invariant | Test file | Layer | Failure reproduced | Last run |
| --- | --- | --- | --- | --- |
| TODO_REQUIRED | TODO_REQUIRED | TODO_REQUIRED | TODO_REQUIRED | Not verified |

## Change risk levels

- Low: docs/nonbehavioral edits, docs/link checks, focused review.
- Medium: functional change, all standard configured checks + relevant interaction test.
- High: authentication, storage/schema, billing, secrets, migrations, multi-module refactor, external service or destructive operation. Requires integration/E2E, rollback/restore evidence, human acceptance.

CI runs the required baseline regardless of an agent's subjective risk classification. Additional high-risk checks must be documented in task acceptance and PR evidence. No silent skipping; environment limitations are blockers, not passes.
