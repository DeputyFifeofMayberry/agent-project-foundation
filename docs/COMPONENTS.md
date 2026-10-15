# Foundation component inventory

Adoption classifies every component per the gap matrix in `docs/ADOPTION.md`: **Adopted**, **Adapted**, **Present-sufficient**, **NA-justified**, or **Missing**. Required components may be adapted or matched by an existing equivalent, but never silently dropped.

## Required for every project

| Component | Why |
| --- | --- |
| `AGENTS.md` | Compact always-read router into the knowledge base; rules and links only. |
| `README.md` | Human onboarding and start-here order. |
| `ARCHITECTURE.md` | Real system map and dependency rules before any architectural change. |
| `CHANGELOG.md` | Release-visible change summary, kept separate from Git history. |
| `docs/INDEX.md` | Knowledge map: where every fact lives and when each file is updated. |
| `docs/PRODUCT.md` + `docs/PRODUCT_SENSE.md` | User goals and behavioral expectations agents must not silently reinterpret. |
| `docs/USER_GUIDE.md` | Owner (non-engineer) operating instructions. |
| `docs/BASELINE.md` | Observed repository facts; separates legacy failures from new regressions. |
| `docs/TESTING.md` | Risk-based test strategy and the executable check inventory. |
| `docs/CHECKLISTS.md` | Before-work/definition-of-done gates, including verification-by-design rules. |
| `docs/REVIEW_EVIDENCE.md` | Independent review and acceptance evidence contract. |
| `docs/SECURITY.md` | Threats, secrets handling, and data-protection rules. |
| `docs/RELIABILITY.md` | SLOs, recovery, and operational guarantees. |
| `docs/RUNBOOKS.md` | Release/incident procedures and external-controls setup (branch rulesets, CI admin). |
| `docs/ADOPTION.md` | New-project and inspect-first existing-project adoption procedures. |
| `docs/COMPONENTS.md` | This inventory; the adoption gap matrix works from it. |
| `docs/STACKS.md` | Minimum verification sets per stack; prevents infrastructure-only "verification". |
| `docs/specs/` (`SPEC_TEMPLATE.md`) | Acceptance criteria are written before implementation. |
| `docs/decisions/` | Durable why-decisions (ADRs) for non-obvious choices. |
| `docs/TECH_DEBT.md` + `docs/QUALITY_SCORE.md` | Deferred-work queue; keeps known limitations documented, not hidden. |
| `docs/agents/` | Implementer, reviewer, debugging, handoff, intake, orchestrator contracts. |
| `.foundation/project.json` (schema v2) | The executable verification contract; all eight categories mandatory. |
| `scripts/verify.py` + `scripts/selftest_verify.py` | The gate, plus proof that the gate itself works. |
| `.github/workflows/verify.yml` | CI enforcement independent of any agent or local run. |

## Stack-conditional

| Component | When required | Why |
| --- | --- | --- |
| `docs/DESIGN.md` + `docs/FRONTEND.md` | Any UI (web, desktop, mobile) | UI/UX contracts and device behavior; NA-justified for headless services. |
| Stack-specific CI runners/jobs | Non-Linux targets (macOS/iOS, Windows) | App verification must run on the target OS (`docs/STACKS.md`). |
| `.github/CODEOWNERS.example` | Orgs using GitHub review ownership | Guidance only; must be adapted to real ownership. |
| `docs/orchestration/` | When Paperclip/Symphony is used | Orchestrator adapter contracts; neither is assumed installed. |

## Optional

| Component | Why it exists | When to skip |
| --- | --- | --- |
| `docs/plans/` | Active/completed execution-plan records for complex work | Trivial projects with single-session tasks (NA-justified) |
| `SETUP_PROMPT.md` | CRAFT onboarding prompt for the adopting agent | Already-adopted repositories (onboarding done) |
| `INTERNAL_AUDIT_PROMPT.md`, `AUDIT_REPORT.md` | Template self-audit approach and findings | Target apps: foundation-meta, not project knowledge |
| `RESEARCH_DECISION.md` | Evidence and caveats behind the foundation design | Target apps: foundation-meta |
| `examples/` | Illustrative check configurations | Always illustrative — never configured as real checks |
