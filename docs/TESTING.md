# Test and verification strategy

## Required baseline (configure commands)

- Code formatting / lint: CI validation project (disposable)
- Static type checks (if typed language): CI validation project (disposable)
- Unit tests: CI validation project (disposable)
- Integration or contract tests: CI validation project (disposable)
- Critical-path E2E tests: CI validation project (disposable)
- Production build or platform build: CI validation project (disposable)
- Architecture/security static checks: CI validation project (disposable)

These eight required categories are enforced by `scripts/verify.py` reading schema v2 `.foundation/project.json`; removing a category from the config is invalid. Disabled or missing checks are treated as incomplete during `--ci`. Only configure real commands that fail on defective behavior. The verifier detects obvious no-ops but cannot establish test meaningfulness automatically; reviewers must examine test behavior. Do not replace tests with `echo pass` or equivalent.

## Test design

Prefer observable behavior and contracts over implementation coupling. For each prior regression, preserve a test reproducing the failure unless technically impossible and explicitly documented. Isolate external integrations using deterministic fixtures; add a smaller number of controlled end-to-end smoke tests against real integrations when warranted.

## Test inventory

| User journey / invariant | Test file | Layer | Failure reproduced | Last run |
| --- | --- | --- | --- | --- |
| CI validation project (disposable) | CI validation project (disposable) | CI validation project (disposable) | CI validation project (disposable) | Not verified |

## Change risk levels

- Low: docs/nonbehavioral edits, docs/link checks, focused review.
- Medium: functional change, all standard configured checks + relevant interaction test.
- High: authentication, storage/schema, billing, secrets, migrations, multi-module refactor, external service or destructive operation. Requires integration/E2E, rollback/restore evidence, human acceptance.

CI runs the required baseline regardless of an agent's subjective risk classification. Additional high-risk checks must be documented in task acceptance and PR evidence. No silent skipping; environment limitations are blockers, not passes.
