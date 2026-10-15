# Verified repository baseline — complete during adoption

**Status:** UNVERIFIED (foundation has not been installed into or exercised against a target application).

| Field | Actual observed value |
| --- | --- |
| Repository URL and default branch | protection-test project (disposable) |
| Baseline commit SHA | protection-test project (disposable) |
| Runtime versions and OS | protection-test project (disposable) |
| Dependency installation command + result | protection-test project (disposable) |
| CI / local commands and evidence links | protection-test project (disposable) |
| Known failing tests before work | protection-test project (disposable) |
| Critical user journeys with test links | protection-test project (disposable) |
| Current deploy / rollback method | protection-test project (disposable) |
| GitHub ruleset status and evidence | protection-test project (disposable) |
| App-vs-infrastructure classification of each configured check | protection-test project (disposable) |
| Read-only checkout verification run and evidence | protection-test project (disposable) |

Never declare an existing project stable merely because it builds. Distinguish observed failures that predate the foundation from regressions introduced during adoption. Recheck this table when baseline assumptions change.

CI enforcement and branch-protection status are recorded from independent confirmation only — an observed rejected push, a PR actually blocked on the required check, or the platform's effective ruleset — never inferred from workflow files, templates, or docs found in the repository. Record the observed evidence, not merely the configuration's existence.

Classify every configured check as validating the **application** or the **foundation infrastructure** (`docs/CHECKLISTS.md`); gate success is never application verification. Run the verification gate against a read-only checkout and record that evidence here; a check that must write into the source tree is invalid and must be reconfigured or reported BLOCKED.
