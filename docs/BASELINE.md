# Verified repository baseline

**Status:** VERIFIED for greeter v0.1.0 on the reference environment below.

| Field | Actual observed value |
| --- | --- |
| Repository URL and default branch | local disposable init (LOC-46 Test A scratch); `main` |
| Baseline commit SHA | recorded at first commit; see `git rev-parse HEAD` in evidence |
| Runtime versions and OS | Python 3.12.3, git 2.55.0, Ubuntu (WSL), x86_64 |
| Dependency installation command + result | none required (stdlib only); `python3 -m compileall` used by lint check, exit 0 |
| CI / local commands and evidence links | `python3 scripts/selftest_verify.py` exit 0; `python3 scripts/verify.py --list` exit 0; `python3 scripts/verify.py --ci` exit 0 (see LOC-46 evidence) |
| Known failing tests before work | none (new repository) |
| Critical user journeys with test links | UJ-001..003 in `docs/PRODUCT.md`, mapped to `tests/e2e_check.py`, `tests/test_greeter.py` |
| Current deploy / rollback method | n/a (local CLI); artifact rebuild via `python3 scripts/build_check.py` |
| GitHub ruleset status and evidence | to be configured per `docs/RUNBOOKS.md` when hosted; recorded as not configured at init time |
| App-vs-infrastructure classification of each configured check | lint/typecheck/unit/integration/e2e/build = application; security/architecture = application source scanners; verifier selftest = foundation infrastructure (not a gate category) |
| Read-only checkout verification run and evidence | `verify.py --ci` writes only to `dist/` (build) and `__pycache__`; build writes are confined to `dist/`; recorded pass on clean clone |
