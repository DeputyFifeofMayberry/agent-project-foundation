# Baseline

rpn-calc 1.0.0 baseline, established on adoption of the agent project foundation.

## Verified at baseline

| Check | Command | Status at baseline |
|---|---|---|
| lint | `python3 tools/lint.py` | green (AST rules: no eval/exec, no bare except, no unused/wildcard imports) |
| typecheck | `python3 tools/typecheck.py` | green (full annotation coverage in `app/` and `tools/`) |
| unit | `python3 -m unittest discover -s tests -p "test_unit_*.py" -t .` | green (engine semantics incl. division by zero, invalid tokens, operand underflow) |
| integration | `python3 -m unittest discover -s tests -p "test_integration_*.py" -t .` | green (CLI + engine in-process) |
| e2e | `python3 tools/e2e.py` | green (real subprocess invocations, happy/compound/error/usage paths) |
| build | `python3 tools/build.py` | green (zipapp artifact smoke-run in temp dir) |
| security | `python3 tools/security.py` | green (no secret patterns, no dangerous calls/imports in `app/`) |
| architecture | `python3 tools/architecture.py` | green (dependency rules in `ARCHITECTURE.md` hold) |

## Baseline regressions to guard

- Subtraction/division operand order (`left OP right`, not reversed) — covered by `test_subtraction_order` and the e2e compound expression.
- Exit-code contract `0`/`2` — covered by integration and e2e error paths.
- Read-only checkout: checks never write into the repository (`docs/STACKS.md`).

## Known limitations (recorded, not defects)

- No `%`/`^` operators, no REPL, no localization (see `docs/PRODUCT.md` non-goals).
