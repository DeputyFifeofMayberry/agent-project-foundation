# Changelog

Template status is distinct from a real application release history.

Use release-oriented entries, not commit-by-commit duplication. Git records exact file history; ADRs document why important design decisions were made.

## Unreleased

### Changed

- v2.1 finalization — ten permanent engineering standards codified into their owning documents (mapped in `docs/INDEX.md`): valid writable execution workspace before implementation; canonical preservation with changes in authorized isolated workspaces; version-controlled, independently maintained foundation content; implementation distinguished from verified application behavior; evidence tied to the exact tested content or commit; failed/unavailable tests never reported as passing; independently confirmed CI enforcement and branch protection; independent review + QA before foundation releases; recorded installed version and adaptations for every adoption; lessons evaluated for future foundation releases. Foundation released as tagged v2.1 from its dedicated version-controlled repository.
- v2.1 foundation improvement pass — encoded first-adoption lessons across the seven board areas: (a) component inventory with required/stack-conditional/optional classes (`docs/COMPONENTS.md`); (b) stack-adaptive new-project initialization procedure in `SETUP_PROMPT.md`; (c) inspect-first existing-project adoption procedure with per-step exit criteria in `docs/ADOPTION.md`; (d) verification-by-design rules (acceptance criteria first, risk-based selection, read-only checkout rule, app-vs-infrastructure split, no weakening to pass) in `docs/CHECKLISTS.md` and `docs/BASELINE.md`; (e) stack-specific minimum verification sets (`docs/STACKS.md`); (f) persistent-knowledge documentation standards in `docs/INDEX.md`; (g) reusable-lessons process in `docs/HARNESS_MAINTENANCE.md`.
- v2.0 audit: hardened verifier schema and self-tests, refreshed CI action versions, expanded user/onboarding/review guidance, corrected Paperclip security/retry assumptions, documented unresolved controls.

### Added

- Agent Project Foundation scaffold, verification contract, and adoption guides (not yet configured for a target application).
