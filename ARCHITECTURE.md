# Architecture contract

**Status:** verified against the actual repository (greeter v0.1.0).

## System map

- Entry points: `greeter.py` (`main()` CLI entry via `python greeter.py --name X`; zipapp entry `greeter:main` in `dist/greeter.pyz`)
- Main services/modules: single module `greeter.py` exposing `greet(name, punctuation)`; helper scripts in `scripts/`; checks in `tests/`
- Storage and schemas: none (stateless CLI; no persistence)
- External APIs and trust boundaries: none; CLI arguments are the only untrusted input (validated non-empty after strip)
- Deployment environments: local WSL Linux (Ubuntu, Python 3.12); distributable artifact `dist/greeter.pyz`
- Runtime observability and logs: stdout result line; stderr `error:` messages; exit codes 0 success / 2 invalid name / argparse errors

## Dependency rules

Single-module design: `greeter.py` imports only stdlib (`argparse`, `sys`). `tests/` and `scripts/` may import `greeter` plus an allowlisted stdlib set. Nothing imports third-party packages. Machine-enforced by `scripts/arch_check.py` (AST import allowlist), wired as the `architecture` verification category.

## Change control

- Public API changes to `greet()` require a unit-test update and CHANGELOG entry before merge.
- New third-party dependencies are prohibited without an ADR in `docs/decisions/` plus `scripts/arch_check.py` allowlist update.
- The exit-code contract (0/2) is an invariant; `tests/e2e_check.py` asserts it.
