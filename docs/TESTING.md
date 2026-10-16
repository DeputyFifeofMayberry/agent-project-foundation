# Testing

rpn-calc verification is the foundation gate (`scripts/verify.py --ci`) running the eight configured checks in `.foundation/project.json`. All checks are read-only-safe: nothing writes into the checkout.

## Test pyramid for this project

| Level | Scope | Where |
|---|---|---|
| unit | `app/core.py` semantics: operators, operand order, stack accumulation, every error class | `tests/test_unit_core.py` |
| integration | CLI + engine in-process: exit codes, stdout/stderr split, real engine invoked | `tests/test_integration_cli.py` |
| e2e | Real CLI in subprocesses: happy, compound, error, usage paths | `tools/e2e.py` (also `tests/test_e2e_cli.py`) |

## Static checks

- `lint` (`tools/lint.py`): AST rules — no `eval`/`exec`, no bare `except`, no unused or wildcard imports — over `app/`, `tests/`, `tools/`.
- `typecheck` (`tools/typecheck.py`): every function/method (dunder-exempt) fully annotated; this is the project's real type contract.
- `security` (`tools/security.py`): secret-pattern and dangerous-call/import scan of `app/`.
- `architecture` (`tools/architecture.py`): dependency rules from `ARCHITECTURE.md`.
- `build` (`tools/build.py`): zipapp artifact built and smoke-run in a temp dir.

## Rules

1. Every bug fix lands with a regression test at the lowest level that can observe it (`docs/PRODUCT.md` quality bar).
2. Engine changes require operand-order coverage; CLI changes require exit-code coverage.
3. Checks must fail on real defects, not on style taste: when a rule fires, it names file and line.
4. The intentional-regression acceptance from `docs/ADOPTION.md` step 1 (configuring an adopter) is re-demonstrated whenever `tests/` layout changes: break `evaluate`'s operand order, watch `unit` go red, revert.
