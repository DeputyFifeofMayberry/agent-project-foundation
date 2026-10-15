# Quality scorecard

Review after each release; consult `docs/HARNESS_MAINTENANCE.md`. Use observed evidence, not agent confidence.

| Area | Grade | Evidence | Biggest gap | Action |
| --- | --- | --- | --- | --- |
| Core flows | Unrated | None yet | TODO_REQUIRED | Add automated critical journeys |
| Architecture | Unrated | None yet | TODO_REQUIRED | Map actual boundaries |
| Security | Unrated | None yet | TODO_REQUIRED | Complete threat model |
| UX/accessibility | Unrated | None yet | TODO_REQUIRED | Test real devices |
| Reliability | Unrated | None yet | TODO_REQUIRED | Define rollback/restore |

Suggested measures: first-pass task acceptance, post-merge regression rate, reopened defects, average time to resolution, human rework minutes, cost per accepted change, flaky-check rate. Review trends over multiple tasks; do not treat a sample of one as proof.
