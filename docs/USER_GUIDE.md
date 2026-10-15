# Owner's guide: from idea to trustworthy change

You do **not** need to know every engineering term. The foundation gives agents a common process and gives you a way to check claims.

## First use (one-time per project)

1. Copy the foundation to a **new branch**, without replacing existing application files or agent instructions blindly.
2. Ask the agent to read `AGENTS.md`, then complete `docs/PRODUCT.md` with your actual requirements, `ARCHITECTURE.md` by inspecting real code, and `docs/TESTING.md` with actual tests.
3. Configure `.foundation/project.json`. Commands must refer to scripts/tests that exist. Required checks initially fail, by design.
4. Run `python scripts/selftest_verify.py` to test the *verifier*, then `python scripts/verify.py --ci` to test the *application*. These are different checks.
5. Create/enable GitHub branch rules; test a PR that intentionally fails CI to prove that merging is blocked.
6. Configure a Paperclip pilot only after a coding agent can complete one verifiable task directly.

## For each request

Provide the desired user experience and what must stay unchanged. Have the agent create a feature spec with Given/When/Then outcomes, then an implementation plan for nontrivial work. Require a separate reviewer and evidence of test results before accepting the PR. Test important features on the actual target device. A screenshot is not proof of persistence, network error handling, or security.

## Understand the status words

- **Designed:** specifications agreed; no code claimed ready.
- **Implemented:** code changed; does not imply verified.
- **Verified:** configured commands passed on the specified commit/environment; may still contain undiscovered problems.
- **Accepted:** product owner has reviewed the behavior and accepted known limitations.
- **Released:** approved artifact deployed to target environment and basic post-release checks passed.

These states are separate. Do not let an agent substitute a Paperclip completion status for them.

## If an agent repeatedly breaks things

Stop after two failed speculative repairs. Preserve logs, compare against last known working commit, require a reproducible failing test and root-cause report, and prohibit unrelated refactoring. If tests don't detect an important regression, improve the harness before continuing feature development.

## Who may approve what?

A reviewer can assess routine code quality. You approve important product tradeoffs, high-risk changes, production migrations, deployment credentials, and any change to CI/security rules. If you cannot see objective evidence, the correct status is **unverified**.

## How to choose tools

The foundation and CI are mandatory irrespective of orchestrator. Paperclip is an optional way to manage tasks and human/agent handoffs. Symphony is a separate Codex-centered option. Never run both on the same uncoordinated branch or shared workspace.
