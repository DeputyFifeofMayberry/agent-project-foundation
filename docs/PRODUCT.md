# Product specification

- Project: greeter — minimal CLI greeting utility (foundation-validation reference app)
- Target users: developers validating the Agent Project Foundation initialization flow
- Problem and intended outcome: provide a deterministic, dependency-free greeting command whose behavior is fully covered by automated checks; outcome: a trustworthy reference for verifying the foundation gate
- Non-goals: localization, i18n, persistence, network access, GUI
- Platforms and minimum supported versions: Python 3.10+ (stdlib only), WSL Linux; no other platforms declared

## Critical user journeys

| ID | User flow | Expected result | Failure/empty state | Test path | Last verified |
| --- | --- | --- | --- | --- | --- |
| UJ-001 | Run `python greeter.py --name Ada` | prints `Hello, Ada!`, exit 0 | non-zero exit with stderr message | `tests/e2e_check.py` | 2026-10-16 |
| UJ-002 | Run `python greeter.py` without `--name` | argparse usage error, exit != 0 | same (missing required arg) | `tests/e2e_check.py` negative case | 2026-10-16 |
| UJ-003 | Blank/whitespace name passed | `error: name must be a non-empty string` on stderr, exit 2 | same | `tests/test_greeter.py::test_empty_name_raises` | 2026-10-16 |

## Functional contract

The full functional contract for `greet()` is specified in `specs/greet.md`. Greeting format: `Hello, <trimmed name>!<default punctuation>`; empty-after-trim names are rejected.

## Constraints

- Privacy/data retention: no data collected or persisted
- Supported device sizes/input modes: CLI text only
- Accessibility expectations: n/a (headless CLI); plain-text output
- Performance expectations: single invocation < 1s on reference environment

## Acceptance principle

Passing tests alone do not establish owner intent; acceptance of significant changes is recorded separately in `docs/REVIEW_EVIDENCE.md`.
