# Verified repository baseline — complete during adoption

**Status:** UNVERIFIED (foundation has not been installed into or exercised against a target application).

| Field | Actual observed value |
| --- | --- |
| Repository URL and default branch | TODO_REQUIRED |
| Baseline commit SHA | TODO_REQUIRED |
| Runtime versions and OS | TODO_REQUIRED |
| Dependency installation command + result | TODO_REQUIRED |
| CI / local commands and evidence links | TODO_REQUIRED |
| Known failing tests before work | TODO_REQUIRED |
| Critical user journeys with test links | TODO_REQUIRED |
| Current deploy / rollback method | TODO_REQUIRED |
| GitHub ruleset status and evidence | TODO_REQUIRED |
| App-vs-infrastructure classification of each configured check | TODO_REQUIRED |
| Read-only checkout verification run and evidence | TODO_REQUIRED |

Never declare an existing project stable merely because it builds. Distinguish observed failures that predate the foundation from regressions introduced during adoption. Recheck this table when baseline assumptions change.

CI enforcement and branch-protection status are recorded from independent confirmation only — an observed rejected push, a PR actually blocked on the required check, or the platform's effective ruleset — never inferred from workflow files, templates, or docs found in the repository. Record the observed evidence, not merely the configuration's existence.

Classify every configured check as validating the **application** or the **foundation infrastructure** (`docs/CHECKLISTS.md`); gate success is never application verification. Run the verification gate against a read-only checkout and record that evidence here; a check that must write into the source tree is invalid and must be reconfigured or reported BLOCKED.
