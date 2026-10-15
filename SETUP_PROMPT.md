# CRAFT — Adopt Project Foundation in a real repository

Use this prompt with OpenCode, Codex, or a Paperclip-assigned planning agent **after** placing the foundation files in the repository. Record the installed foundation version (from `CHANGELOG.md`) and every project-specific adaptation in `docs/BASELINE.md`; an adoption without a recorded installed version is incomplete.

## C — Context

You are working in an existing or new software repository with the Agent Project Foundation installed. The user wants reliable agent-built software that maintains an accurate product specification, architectural knowledge, verified code changes, and regression coverage. The foundation is generic; project-specific facts and quality checks must be discovered, not invented. Read `AGENTS.md`, `docs/USER_GUIDE.md`, `docs/ADOPTION.md`, `docs/BASELINE.md`, and `RESEARCH_DECISION.md`. The user values functional stability, intuitive product behavior, small changes, and minimal manual bug-fixing.

## R — Role and responsibility

Act as the lead engineer responsible for safely adopting the foundation. Do not write new product features until the baseline is documented and verification behavior is proven. Preserve pre-existing instructions, tests, user changes, Git history, settings, and credentials. Delegate independent review only after establishing basic reliability.

## A — Actions

1. Inventory the actual app stack, modules, scripts, tests, deployment environments, existing agent instructions, current Git status and critical user journeys.
2. Choose an adoption mode (new app or existing) and create a safe branch/worktree. Avoid wholesale overwrite; reconcile conflicts.
3. Populate project-specific docs with evidence from actual code/tests, marking unresolved uncertainties explicitly.
4. Propose a minimal, prioritized critical-journey test suite. Implement executable checks for lint/typecheck/unit/integration/E2E/build/security/architecture appropriate to the stack; avoid fake passes, and record the actual project baseline in `docs/BASELINE.md`.
5. Configure `.foundation/project.json` (schema v2) and native CI runners; ensure a deliberately failing test causes `scripts/verify.py --ci` and GitHub CI to fail. Do not accidentally merge the deliberate failure.
6. Establish GitHub branch ruleset and require CI / authorized review. If permissions to configure it are missing, provide exact manual setup steps and report not enforced.
7. For Paperclip, configure one implementer and independent reviewer, a nonzero timeout, explicit permission restrictions, and human escalation. A retry limit must be enforced externally unless the pinned Paperclip version demonstrably enforces it. Test task lifecycle and OpenCode adapter; do not enable unattended auto-merge.
8. Run one representative bug fix with a reproduction test and end-to-end acceptance evidence. Inspect every failure as a harness-improvement opportunity.

## F — Format

Produce an actionable project foundation audit, changed file list, evidence for discovered facts, initial test inventory, explicit commands and pass/fail logs, external controls status, unresolved blockers, and reviewer-ready pull request. Save durable decisions in repository files. Do not report success unless verified.

## T — Tests and acceptance

Acceptance requires the actual application to build, meaningful tests for its critical paths, documented failures, a negative-test demonstration of the gate, and confirmation that an agent cannot bypass protected branch settings. Configuration and tests must match the runtime. Do not fabricate results, convert failing checks into warnings, or call deployment/merge complete without approval. Check Paperclip adapter `dangerouslySkipPermissions` explicitly before unattended execution.

## New-project initialization procedure (stack-adaptive)

For a **new** repository, run this procedure after the CRAFT sections above. It is adaptive: every step derives its concrete content from the actually selected stack — never emit generic filler and never fabricate facts for a stack that was not chosen. Record each step's outcome in the named file before moving to the next step; if a step cannot be completed with verified facts, record it BLOCKED instead of inventing content.

1. **Purpose, scope, success criteria.** Write the product purpose, non-goals, and 3–5 objectively checkable success criteria in `docs/PRODUCT.md`. *Exit:* each criterion can be verified by a test, demonstration, or measurement.
2. **Architecture and technology decisions.** Select language, framework, storage, and deployment target; record them, and an ADR in `docs/decisions/` for every non-obvious choice. *Exit:* `ARCHITECTURE.md` system map contains real entry points, modules, and boundaries — no TODO placeholders.
3. **Development environment and dependencies.** Pin toolchain versions; record exact install, build, and run commands in `docs/BASELINE.md`. *Exit:* a clean checkout installs and builds using only the recorded commands.
4. **Version control and branching.** Initialize Git; set the default branch; document the branching/worktree convention and the commit policy in `docs/RUNBOOKS.md` — commits, merges, and pushes are human-approved; agents deliver a documented exact commit plan, not an executed integration. *Exit:* policy written; branch protection configured or explicitly reported as not enforced.
5. **Required documentation set.** Install the foundation docs listed by `docs/INDEX.md` and `docs/COMPONENTS.md`, replacing every required marker with verified content. *Exit:* every status/index claim matches actual repository state (files and commands exist), never a document's self-description.
6. **Testing strategy.** Define the risk-based test plan in `docs/TESTING.md` tied to documented risk levels — not a fixed test count — and write acceptance criteria before implementing any feature. *Exit:* test inventory maps the first critical journeys to real test files.
7. **CI and quality gates.** Configure all eight `.foundation/project.json` check categories with real stack-appropriate commands (`docs/STACKS.md` gives minimum sets); wire the native CI runner. Keep every check read-only safe (`docs/CHECKLISTS.md`). *Exit:* `python scripts/verify.py --ci` runs every category and a deliberately failing test fails the gate.
8. **Agent responsibilities and permissions.** Configure orchestrator roles, least-privilege permissions, nonzero timeouts, and human escalation per `docs/agents/` and `docs/orchestration/`. *Exit:* unattended permissions audited and restricted; no auto-merge.
9. **Review and acceptance requirements.** Enable independent review plus separate product acceptance per `docs/REVIEW_EVIDENCE.md`; acceptance evidence must be independently reproducible from recorded commands, not dependent on attachments alone. *Exit:* one small real change completes the full implement → verify → review loop.
10. **Known limitations and unresolved decisions.** Record them in `docs/TECH_DEBT.md` and ADRs, including what is deliberately not yet true. *Exit:* no known limitation is undocumented.
