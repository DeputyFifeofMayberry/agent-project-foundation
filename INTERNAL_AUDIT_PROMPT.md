# Internal audit instruction — CRAFT

This is the review contract used to audit and revise the foundation. It is a reusable *instruction*, not proof of application reliability.

## C — Context

Audit every file in the Agent Project Foundation repository as a reusable starter for developers using OpenCode, Superpowers, Paperclip, Codex, or Symphony. Target: trustworthy change delivery, regression resistance, and accessible instructions for someone who delegates coding to AI. Preserve compatibility with Windows 11 and Python 3.10+; avoid inventing a real application's stack or tests.

## R — Role

Act as an independent staff engineer, security reviewer, QA lead, release engineer, and documentation editor. Treat the previous version as untrusted. Verify vendor features in primary docs. Distinguish claims, prototypes, user reports, and local test results.

## A — Action

1. Inventory every file and map it to a purpose, dependency, and owner.
2. Examine each statement and cross-reference for correctness and freshness; resolve contradictions and remove ungrounded claims.
3. Trace an entire feature lifecycle: onboarding → spec → plan → isolated implementation → test → independent review → CI → protected merge → docs/changelog → recovery.
4. Threat-model prompt injection, excess permissions, concurrency, missing tests, false CI green, config bypass, state persistence, secret exposure, and destructive actions.
5. Exercise the executable verification with positive and adversarial fixtures, including missing gates, removed gate categories, skipped checks, failed commands, missing docs, and timeouts.
6. Fix issues directly while preserving the fail-closed onboarding state; never configure fake application tests to make the template pass.
7. Produce a file-by-file audit report and final archive with reproducible test results, open risks, and adoption instructions.

## F — Format

Return `AUDIT_REPORT.md` (complete inventory and findings), `RESEARCH_DECISION.md` (source-backed decision and uncertainty), and corrected project files as a reviewed working state of the foundation repository. Deliver through the `docs/HARNESS_MAINTENANCE.md` release path — independent review plus QA, then a verified commit eligible for an annotated release tag — not as a ZIP or ad-hoc archive. Provide concise instructions for a first run. All claimed checks must show exactly what was executed and its outcome.

## T — Test / acceptance criteria

- Every file inventoried and verified as valid/useful or revised/removal documented.
- No unsupported claims of runtime-enforced behavior or vendor superiority.
- Python parses, JSON schemas validate, YAML structure is plausible, Markdown links resolve locally, and the corrected working tree contains exactly the intended files (no stray archive or temporary artifacts).
- Test harness rejects meaningful negative cases and passes the synthetic positive fixture.
- Untailored starter intentionally fails project CI (not ready for production).
- Orchestrator not claimed installed or tested; external branch rules not claimed enabled.
