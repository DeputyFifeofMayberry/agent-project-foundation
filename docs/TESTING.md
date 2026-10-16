# Testing strategy

Risk levels: the single risk class for greeter is output-contract regressions (wrong greeting string or wrong exit codes).

| Risk | Checks | Automated test |
| --- | --- | --- |
| Greeting string contract | unit | `tests/test_greeter.py` (4 cases) |
| CLI wiring + happy path | integration | `tests/integration_check.py` |
| Real invocation, negative case | e2e | `tests/e2e_check.py` |
| Distribution artifact usable | build | `scripts/build_check.py` |
| No credentials in sources | security | `scripts/security_scan.py` |
| Import allowlist respected | architecture | `scripts/arch_check.py` |

Acceptance criteria are written in `docs/specs/greet.md` before feature changes; lint and typecheck guard syntax/typing hygiene (`python3 -m compileall -q`, `python3 -m py_compile` on first-party files).
