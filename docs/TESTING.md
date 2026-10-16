# Test and verification strategy

## Required baseline (configure commands)

- Code formatting / lint: TODO_REQUIRED
- Static type checks (if typed language): TODO_REQUIRED
- Unit tests: TODO_REQUIRED
- Integration or contract tests: TODO_REQUIRED
- Critical-path E2E tests: TODO_REQUIRED
- Production build or platform build: TODO_REQUIRED
- Architecture/security static checks: TODO_REQUIRED

These eight required categories are enforced by `scripts/verify.py` reading schema v2 `.foundation/project.json`; removing a category from the config is invalid. Disabled or missing checks are treated as incomplete during `--ci`. Only configure real commands that fail on defective behavior. The verifier rejects apparent no-ops with a heuristic denylist — it is not exhaustive, and passing it does not establish that a test is meaningful; reviewers must examine test behavior. Do not replace tests with `echo pass` or equivalent.

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

## Protected-branch regression scenarios

The foundation keeps permanent lightweight coverage for the seven required protection scenarios. `docs/RUNBOOKS.md` (GitHub setup) owns the rule, the required-check distinction, and the hosted procedure; this table maps each scenario to its standing verification:

| Scenario | Standing verification |
| --- | --- |
| (a) Valid foundation-maintenance PR: checks pass, merge permitted | Hosted procedure (`docs/RUNBOOKS.md` GitHub setup step 6) |
| (b) Invalid foundation-maintenance PR: check fails, merge blocked | Hosted procedure (`docs/RUNBOOKS.md` GitHub setup step 6) |
| (c) Unconfigured adopter application: verification fails closed | `scripts/selftest_verify.py`; `scripts/check_required_checks.py` |
| (d) Properly configured adopter application: verification passes | `scripts/check_required_checks.py` |
| (e) Deliberately failing adopter test: verification fails, merge blocked | Local: both scripts; hosted merge block: `docs/RUNBOOKS.md` step 6 |
| (f) Incorrect or nonexistent required check: validation reports failure | `scripts/check_required_checks.py` |
| (g) Bypass required for ordinary changes: release-readiness failure | `scripts/check_required_checks.py` |

Adopting projects record their own execution of the applicable scenarios in the test inventory above.

QA of a protected-branch release includes both the positive and the negative protected-branch integration scenarios on the actual release workflow (hosted procedure: `docs/RUNBOOKS.md`, GitHub setup step 6) and flags any release whose evidence depends on bypassing branch protections instead of demonstrating them (`docs/RUNBOOKS.md`, GitHub setup step 7, owns the bypass policy).
