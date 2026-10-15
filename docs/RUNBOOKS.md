# Runbooks

## GitHub setup (manual)

1. Create a repository with `main` as protected default branch.
2. Under Settings → Rules → Rulesets create an active branch ruleset for `main`.
3. Require pull requests and the exact GitHub Actions check name shown for job **`verify`**. Confirm the check exists and succeeds on the target platform; prefer strict/up-to-date status. GitHub check names vary with workflows and matrices.
4. Require authorized human approval for changes to `.github/workflows/`, `.foundation/`, `scripts/verify.py`, and test policy; use CODEOWNERS/review rules where supported by your GitHub plan and repository visibility. Verify CODEOWNERS file is active (rename `.github/CODEOWNERS.example`). Verify an agent cannot self-approve or bypass the ruleset.
5. Disallow force pushes and deletion of `main`; restrict bypass permissions and automation tokens.
6. Confirm by opening a disposable PR with a deliberately failing test, then verify merge is blocked. Do not merge the failing test.

## Release

Check clean working tree, merged verified PRs, tag/version, changelog, compatibility tests, backups and release notes. For app signing/deployments use platform-specific tools and human approval. Verify upgrade/restart; roll back if key journeys regress.

## Incident

Stabilize or roll back, record timing and symptoms, preserve logs, reproduce, find root cause, add regression, update runbook and incident record. Never patch blindly for more than two attempts. If a secret may be leaked, revoke/rotate with authorization and audit access.

## Existing app adoption

Read `docs/USER_GUIDE.md`. Take an inventory before introducing large refactors. Preserve existing build commands, test files, instruction files, CI and secrets. Document the real current architecture, known failing tests, and baseline. Establish first 3–5 smoke tests and gradually expand; do not use a foundation migration as an excuse to rewrite a functioning app.
