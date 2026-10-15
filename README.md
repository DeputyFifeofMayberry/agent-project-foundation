# Agent Project Foundation v2.1 — audited starter

A reusable, agent-neutral engineering harness for **new or existing** software repositories. Designed to be used with OpenCode, Codex, Superpowers, Paperclip, or Symphony when those tools are separately installed and configured. It is an engineering **foundation**, not a coding agent, and does not claim to eliminate bugs.

## Purpose

Keep product intent, engineering decisions, verification evidence, and change history in the repository so coding agents inherit a consistent working environment. Automated checks, not agent assurances, determine whether required technical verification has passed.

## Start here

1. Copy the contents of this folder (or the tagged release from the foundation's own version-controlled repository) into a **new branch** of the target repository. For existing apps, compare files and merge carefully rather than overwriting existing instructions or CI.
2. Record the installed foundation version (see `CHANGELOG.md`) and every project-specific adaptation in `docs/BASELINE.md` — adoptions without a recorded version are incomplete.
3. Read `AGENTS.md`, `docs/INDEX.md`, `docs/USER_GUIDE.md`, and `docs/ADOPTION.md`.
4. Fill project-specific documents listed by `scripts/verify.py` (including `docs/BASELINE.md`) with *verified* project facts. Replace `TODO_REQUIRED` placeholders. Never invent architecture or tests.
5. Configure `.foundation/project.json` schema v2 with real `argv` arrays and per-check timeouts. All eight categories are mandatory; each must run a meaningful check. Do not use a command that merely prints success.
6. Run `python scripts/selftest_verify.py` (tests the verifier), `python scripts/verify.py --list`, then `python scripts/verify.py --ci` (Windows: `py -3 scripts/verify.py --ci`). Expect failure until initialization is complete.
7. Test that a deliberately failing app test blocks verification and the pull request. Restore the test afterward.
8. Configure the GitHub ruleset described in `docs/RUNBOOKS.md` to require the `verify` job on `main`; this must be done in GitHub, not in repository Markdown. Independently confirm the enforcement (for example, an observed rejected push or blocked PR) rather than inferring it from repository files.
9. Have the agent implement one small real feature or bug fix. Require reproducible evidence, a regression test where appropriate, and independent acceptance before merge.

**Where the adoption instructions live:** new projects follow `SETUP_PROMPT.md` (stack-adaptive initialization procedure); existing projects follow the inspect-first procedure in `docs/ADOPTION.md`; stack-specific minimum verification sets are in `docs/STACKS.md`; the required/stack-conditional/optional component inventory is in `docs/COMPONENTS.md`. Every adoption must record the installed foundation version and its project-specific adaptations (`docs/ADOPTION.md`, standard 9).

## Structure

- `SETUP_PROMPT.md`: CRAFT onboarding task prompt for OpenCode, Codex or Paperclip.
- `INTERNAL_AUDIT_PROMPT.md`, `AUDIT_REPORT.md`: audit approach, results, and remaining limitations.
- `docs/USER_GUIDE.md`, `docs/BASELINE.md`: non-engineer walkthrough and observed baseline.
- `docs/HARNESS_MAINTENANCE.md`, `docs/REVIEW_EVIDENCE.md`: hygiene and review proof.
- `AGENTS.md`: compact, always-read rules and navigation map.
- `ARCHITECTURE.md`: actual components, dependencies, boundaries, and allowed dependency direction.
- `docs/INDEX.md`: complete knowledge-base index and ownership map.
- `docs/COMPONENTS.md`, `docs/STACKS.md`: component inventory (required/stack-conditional/optional) and per-stack minimum verification sets.
- `docs/PRODUCT.md` and `docs/PRODUCT_SENSE.md`: user goals, workflows, behavioral expectations.
- `docs/DESIGN.md` and `docs/FRONTEND.md`: UI, UX, accessibility, device and platform behavior.
- `docs/SECURITY.md`, `docs/RELIABILITY.md`, `docs/TESTING.md`: operational guarantees and verification strategy.
- `docs/specs/`: feature contracts; `docs/plans/`: active and completed execution plans.
- `docs/decisions/`: durable architectural decision records.
- `docs/QUALITY_SCORE.md`, `docs/TECH_DEBT.md`: ongoing improvement queue.
- `docs/agents/`: intake, builder, reviewer, debugging and handoff contracts.
- `docs/orchestration/`: Paperclip and Symphony adapters; neither is assumed installed.
- `.foundation/project.json` and `scripts/verify.py`: configured executable checks.
- `.github/workflows/verify.yml`: independent CI runner. A **green CI status does not imply product acceptance**; manual/human or approved agent product review remains separately necessary.

## Quality policy

Every code change: focused scope, green required checks, no known unintended regression, and review evidence. Riskier changes: extra integration/E2E, security and rollback tests. Test changes and verification config changes require human review. Breakage is not dismissed because a build passes. Two speculative failed fixes trigger root-cause investigation and a fresh plan.

## Template limitations

- No application source code or tests are invented. You must supply stack-specific checks and meaningful tests.
- Branch protection, secret permissions, test runners, device simulators, and Paperclip policies are configured outside this repo. `CODEOWNERS.example` is guidance only. **Paperclip OpenCode unattended runs can grant broad permissions by default; audit and disable this where feasible.**
- The generic verifier runs in Python 3.10+. The repository's own dependencies/toolchains must also be installed. See `examples/` for illustrative commands; these are **not** actual tests unless the app defines them.
- GitHub Actions example defaults to Ubuntu. Windows desktop or iOS builds need their own Windows/macOS CI jobs and signing setup.

## Research and decision

See `RESEARCH_DECISION.md` for the evidence, caveats, and recommended Paperclip pilot, with Symphony as a future swap.
