# Final audit report — Agent Project Foundation v2.0

**Audit date:** October 14, 2026. **Scope:** all original files and newly introduced components; no user's live application or cloud permissions were modified.

## Result

**Template readiness: APPROVED FOR ADOPTION / NOT APPROVED AS AN ALREADY CONFIGURED APPLICATION.** The code and guidance were reviewed and strengthened. The starter intentionally fails full application verification until it has been installed, customized, and paired with real tests and active branch protection. No evidence supports claiming the foundation or Paperclip is production-proven for the user's codebase.

## Critical findings and corrections

| Severity | Finding from v1 | Correction in v2 | Remaining limitation |
| --- | --- | --- | --- |
| Critical | Paperclip correction loop described as inherently bounded | Clarified published execution policy loops until approval; separate operator/controller cap required | Not runtime-enforced by these files |
| Critical | Paperclip unattended OpenCode permission default overlooked | Documented the adapter's `dangerouslySkipPermissions` default and safer isolated, least-privilege pilot | Must confirm effective permissions in actual installation |
| High | Agent could remove gate categories from `required_ci_checks` | Eight mandatory checks fixed in `verify.py`, schema v2 validates exact categories | Agent can still edit verifier/CI unless external GitHub approvals prevent it |
| High | No verifier timeouts; insufficient negative-case coverage | Per-check bounded timeouts plus adversarial self-tests | Descendant process cleanup and platform execution still need real-world test |
| High | No verified starting commit/test baseline or owner operating guide | Added `docs/BASELINE.md`, `docs/USER_GUIDE.md` | Must populate from actual repository |
| High | Agent completion could be mistaken for commit-specific evidence | Added review contract, independent decision, acceptance-state definitions, task/commit links | Actual app tests and owner judgment still required |
| Medium | Original CI referenced older action majors | Updated GitHub checkout/setup-python to documented v7 and disabled persisted checkout credentials | Action SHA pinning and GitHub-hosted CI execution not verified here |
| Medium | Documentation checks were limited | Added required docs/placeholder checks and bounded local Markdown link integrity | Cannot semantically prove docs reflect real code |
| Medium | Harness hygiene and escalation were underspecified | Added maintenance protocol, orchestrator contract, debugging escalation | Scheduling and enforcement require your deployment configuration |

## End-to-end workflow audit

| Step | Foundation entry point | Status |
| --- | --- | --- |
| 1. Inspect working tree, establish known baseline | `AGENTS.md`, `docs/BASELINE.md` | Defined; actual baseline unverified |
| 2. Specify product and unchanged behavior | `docs/PRODUCT.md`, `docs/specs/SPEC_TEMPLATE.md` | Defined; actual app content incomplete |
| 3. Plan risky/multistep work | `docs/plans/PLAN_TEMPLATE.md` | Defined |
| 4. Isolate and assign task | `docs/agents/ORCHESTRATOR.md`, Paperclip/Symphony docs | Defined; runtime not connected |
| 5. Implement and diagnose failures | `docs/agents/IMPLEMENTER.md`, `DEBUGGING.md` | Defined |
| 6. Verify with tests and runtime evidence | `scripts/verify.py`, `docs/TESTING.md`, `FRONTEND.md` | Verifier tested; actual app checks unconfigured |
| 7. Independent reviewer evaluates actual commit | `docs/agents/REVIEWER.md`, `docs/REVIEW_EVIDENCE.md` | Contract defined; no real review performed |
| 8. Block bad merges with CI/branch rules | `.github/workflows/verify.yml`, `docs/RUNBOOKS.md` | CI file exists; protected settings unverified |
| 9. Product owner accepts, changelog/ADR updated | `docs/USER_GUIDE.md`, `CHANGELOG.md`, `docs/decisions/` | Defined; owner acceptance not performed |
| 10. Release/recovery and drift maintenance | `docs/RUNBOOKS.md`, `docs/HARNESS_MAINTENANCE.md` | Defined; live deployment not tested |

## Verification performed locally

- `python -m py_compile scripts/verify.py scripts/selftest_verify.py`: **PASS**.
- `python scripts/selftest_verify.py -q`: **13 synthetic tests PASS**. Includes successful configured command, intentional command failure, missing/removed required check, duplicate required check, missing document, unconfigured document, broken Markdown link, timeout, obvious no-op, inline no-op, outdated config schema, and pre-initialization listing.
- `python scripts/verify.py --list`: **PASS**; eight categories displayed as unconfigured.
- `python scripts/verify.py --ci` on the unconfigured starter: **INTENTIONAL FAIL**, code 2 because `project_name` is still `CI validation project (disposable)`. The template must not be reported as an application that passes CI.
- `.foundation/project.json` and example config: parsed as JSON, use schema v2 and eight check categories.
- `.github/workflows/verify.yml`: parsed as YAML and contains independent verifier-selftest and application-verification steps. **It has not been run on GitHub.** Note: PyYAML YAML 1.1 parses an unquoted `on` as Boolean `true`, while GitHub Actions interprets `on` as its event keyword.
- Local Markdown references: validator executed on template and reported no broken local Markdown paths apart from the deliberately incomplete application documents.
- Zip archive integrity: verified after archive creation (see packaging log in final response).

## Open blockers before calling any application trustworthy

1. Complete application-specific `CI validation project (disposable)` entries; never fabricate architectural assertions.
2. Install real project dependencies and commands for all eight checks. Configure native Windows/macOS/iOS runners where needed; Ubuntu alone is insufficient.
3. Exercise E2E tests of critical journeys, persistence, negative paths, and the real target device.
4. Configure, activate, and *test* GitHub ruleset, required CI status, CODEOWNERS review, and non-bypass privileges. None are remotely configured by these files.
5. Pin Paperclip/OpenCode adapter, configure per-issue review, restrict permission defaults, set timeouts, verify subagent join and reject failing changes. A retry cap requires separate enforcement.
6. Compare accepted tasks and real regressions against your current workflow before claiming Paperclip or Symphony improves outcomes.

## File-by-file audit ledger

All items below were inspected for purpose, consistency, and project-template suitability. `Retained` means no text change was necessary; it does not mean a particular application has been verified.

| File | Disposition | Audit determination |
| --- | --- | --- |
| `.editorconfig` | Retained | Whitespace and encoding defaults |
| `.foundation/project.json` | Updated | Fail-closed, schema-v2 gate configuration; intentionally unconfigured |
| `.github/CODEOWNERS.example` | Updated | Human-review protection model; requires activation externally |
| `.github/PULL_REQUEST_TEMPLATE.md` | Updated | Commit-bound evidence checklist |
| `.github/workflows/verify.yml` | Updated | PR quality checks and verifier self-test; application deps must be installed |
| `.gitignore` | Retained | Local/secrets/build artifacts excluded |
| `AGENTS.md` | Updated | Compact mandatory agent navigation and constraints |
| `ARCHITECTURE.md` | Retained | System map and architectural constraints; project-specific |
| `AUDIT_REPORT.md` | Added | Report itself, explains findings, evidence, and limitations |
| `CHANGELOG.md` | Updated | Human-readable release-oriented change history |
| `INTERNAL_AUDIT_PROMPT.md` | Added | The CRAFT audit instructions used for this review |
| `README.md` | Updated | First-run procedure, file map and limitations |
| `RESEARCH_DECISION.md` | Updated | Source-grounded Paperclip/Symphony decision and uncertainty |
| `SETUP_PROMPT.md` | Updated | CRAFT prompt to adopt foundation in a real repository |
| `docs/ADOPTION.md` | Updated | New and existing codebase adoption criteria |
| `docs/BASELINE.md` | Added | Observed commit/test/deployment facts; intentionally blank |
| `docs/CHECKLISTS.md` | Updated | Change Definition of Done and blocker checklist |
| `docs/DESIGN.md` | Updated | Visual specification and acceptance; project-specific |
| `docs/FRONTEND.md` | Updated | Runtime/mobile/e2e testing guidance; project-specific |
| `docs/HARNESS_MAINTENANCE.md` | Added | Periodic documentation/test/architecture housekeeping |
| `docs/INDEX.md` | Updated | Index, document ownership and revision triggers |
| `docs/PRODUCT.md` | Updated | Users, product outcomes, critical flows; project-specific |
| `docs/PRODUCT_SENSE.md` | Updated | Product scope and decision principles; project-specific |
| `docs/QUALITY_SCORE.md` | Updated | Evidence-backed quality scorecard; project-specific |
| `docs/RELIABILITY.md` | Updated | Operations, recovery, observability and reliability; project-specific |
| `docs/REVIEW_EVIDENCE.md` | Added | Proof contract for independent code/product review |
| `docs/RUNBOOKS.md` | Updated | Branch ruleset, release and incident procedures |
| `docs/SECURITY.md` | Updated | Trust boundaries, credentials, data safety; project-specific |
| `docs/TECH_DEBT.md` | Updated | Known defects and debt register |
| `docs/TESTING.md` | Updated | Actual test inventory and risk-level checks; project-specific |
| `docs/USER_GUIDE.md` | Added | Plain-English operating manual for non-engineer project owner |
| `docs/agents/DEBUGGING.md` | Updated | Root-cause-first failure diagnosis and two-attempt escalation |
| `docs/agents/HANDOFF.md` | Updated | Durable branch/task evidence for context recovery |
| `docs/agents/IMPLEMENTER.md` | Updated | Implementation and handoff contract |
| `docs/agents/ORCHESTRATOR.md` | Added | Independent cross-platform orchestration state contract |
| `docs/agents/REVIEWER.md` | Updated | Separate acceptance review and explicit rejection rules |
| `docs/agents/TASK_INTAKE_CRAFT.md` | Updated | Structured intake contract |
| `docs/decisions/ADR-0001-foundation.md` | Retained | Documented choice to keep foundation vendor-neutral |
| `docs/orchestration/PAPERCLIP.md` | Updated | Paperclip permission/security/policy pilot checklist |
| `docs/orchestration/SYMPHONY.md` | Updated | Symphony alternative with prototype/platform caveats |
| `docs/plans/PLAN_TEMPLATE.md` | Updated | Execution steps and proof for complex tasks |
| `docs/plans/active/README.md` | Retained | Live plan maintenance expectations |
| `docs/plans/completed/README.md` | Retained | Completed plan provenance |
| `docs/specs/SPEC_TEMPLATE.md` | Updated | Task-specific observable acceptance conditions |
| `examples/README.md` | Updated | Stack/configuration example usage caveats |
| `examples/project.node-react.example.json` | Updated | Illustrative npm command configuration (not real tests) |
| `scripts/selftest_verify.py` | Updated | Adversarial synthetic verifier test suite |
| `scripts/verify.py` | Updated | Executable mandatory gate runner and documentation integrity checks |

## Evidence sources

- OpenAI harness engineering: https://openai.com/index/harness-engineering/
- Symphony Elixir README: https://github.com/openai/symphony/blob/main/elixir/README.md
- Paperclip OpenCode adapter: https://docs.paperclip.ing/reference/adapters/opencode/
- Paperclip execution policy: https://github.com/paperclipai/paperclip/blob/master/docs/guides/execution-policy.md
- GitHub required status checks: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets
- GitHub Actions releases: https://github.com/actions/checkout and https://github.com/actions/setup-python

Sources were reviewed as of the audit date. Vendor capabilities and issue statuses may change; no universal reliability ranking is inferred from these documents.
