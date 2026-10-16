# Runbooks

## GitHub setup (manual)

**Canonical rule (this section is its owner; other documents reference it instead of restating it):** repository protections must require checks that validate the repository's actual purpose, and enforcement must be verified using both a successful and a failing change.

1. Create a repository with `main` as protected default branch.
2. Under Settings → Rules → Rulesets create an active branch ruleset for `main`.
3. Require pull requests and the exact GitHub Actions check name that validates *this* repository's actual purpose (GitHub check names vary with workflows and matrices; prefer strict/up-to-date status):
   - **Foundation repository** (this template's home): require the `maintenance` job — it validates the reusable foundation and passes when the foundation is valid.
   - **Adopting application repository**: require the application `verify` job only after adoption has configured real project checks. Before configuration `verify` is intentionally fail-closed (red), so requiring it earlier deadlocks the repository: no ordinary change can merge through the protected workflow.
   The required check must pass on a valid tree. If integrating an ordinary change requires a protection bypass, the protection is misconfigured — treat that as a defect to correct, never as release mechanics.
4. Require authorized human approval for changes to `.github/workflows/`, `.foundation/`, `scripts/verify.py`, and test policy; use CODEOWNERS/review rules where supported by your GitHub plan and repository visibility. Verify CODEOWNERS file is active (rename `.github/CODEOWNERS.example`). Verify an agent cannot self-approve or bypass the ruleset.
5. Disallow force pushes and deletion of `main`; restrict bypass permissions and automation tokens.
6. Verify enforcement on **both** paths through the normal protected PR workflow, using disposable branches and without any bypass:
   - **Failing path:** open a disposable PR with a deliberately failing test; the required check must fail and merge must be blocked. Do not merge the failing test.
   - **Succeeding path:** open a disposable PR with an ordinary valid change; the required check must pass and the merge must be permitted through the same protected workflow. A protection for which only the failing path was demonstrated is not verified.
   Locally, `python scripts/check_required_checks.py --required <name>[,<name>...]` proves each required check name matches a configured workflow job and passes on the current tree (fail-closed on nonexistent names and jobs that fail); hosted merge enforcement itself must still be observed as described above.
7. **Bypass policy (canonical):** if a protection bypass is ever genuinely unavoidable, it requires explicit authorization, documented rationale, restoration evidence, and evaluation as a potential unresolved system defect. A bypass never counts as proof that the normal workflow functions.

## Release

Check clean working tree, merged verified PRs, tag/version, changelog, compatibility tests, backups and release notes. For app signing/deployments use platform-specific tools and human approval. Verify upgrade/restart; roll back if key journeys regress.

## Incident

Stabilize or roll back, record timing and symptoms, preserve logs, reproduce, find root cause, add regression, update runbook and incident record. Never patch blindly for more than two attempts (`docs/agents/DEBUGGING.md` is the canonical owner of this rule). If a secret may be leaked, revoke/rotate with authorization and audit access.

## Existing app adoption

Follow the single ordered inspect-first procedure in `docs/ADOPTION.md` (read-only inventory before any refactor; existing conventions and instruction files are merged, not overwritten). Start with 3–5 smoke journeys and grow them toward the 5–10 essential flows in `docs/PRODUCT.md`; a foundation migration is never a license to rewrite a functioning app.
