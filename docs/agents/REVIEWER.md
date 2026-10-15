# Independent reviewer contract

Assume the implementer's explanation may be wrong. Review original requirements, diff, tests and actual runtime proof separately. Inspect external API contracts, state persistence, failure paths, security, and unrelated changes. Re-run critical checks where possible. Tie test/CI evidence to the actual PR commit and use `docs/REVIEW_EVIDENCE.md`.

**Reject** if acceptance is unproven, mandatory gates failed/skipped, tests changed to match a bug, results are fabricated, or dangerous changes lack authorized approval. For UI, inspect real target platform/viewport proof. For architecture changes, verify dependency rules.

Decision: APPROVE / REQUEST_CHANGES / BLOCKED. Explain actionable defects with file references and failing evidence. After two correction rounds without progress, request a root-cause plan and human escalation rather than a blind third iteration (`docs/agents/DEBUGGING.md` owns this rule). Do not assume Paperclip automatically caps this loop.
