# Documentation index

The repository, not a chat transcript, is the durable source of truth. Review each page after architectural or user-visible changes.

| Domain | Source of truth | When to update |
| --- | --- | --- |
| Mission, target users, user journeys | `PRODUCT.md`, `PRODUCT_SENSE.md` | Feature intent changes |
| System components/dependencies | `../ARCHITECTURE.md`, `decisions/` | Architecture or API boundary changes |
| UI/UX/device behavior | `DESIGN.md`, `FRONTEND.md` | UI or navigation changes |
| Tests and gates | `TESTING.md`, `../.foundation/project.json` | New/changed checks |
| Threats/secrets/data | `SECURITY.md` | Security/data change |
| SLOs/recovery | `RELIABILITY.md` | Operational behavior changes |
| Feature contracts | `specs/` | Before implementing features |
| Execution plans | `plans/active/`, `plans/completed/` | During complex work and completion |
| Important why-decisions | `decisions/` | Architecture decisions |
| Backlog of cleanup | `TECH_DEBT.md`, `QUALITY_SCORE.md` | When deferring work |
| Agent contracts | `agents/` | Workflow changes |
| Release/incident steps | `RUNBOOKS.md` | Deployment procedure changes |
| Orchestration | `orchestration/`, `agents/ORCHESTRATOR.md` | Paperclip/Symphony pilot changes |
| Project baseline and owner instructions | `BASELINE.md`, `USER_GUIDE.md` | During onboarding and baseline changes |
| Review evidence | `REVIEW_EVIDENCE.md` | On each substantive PR |
| Harness upkeep | `HARNESS_MAINTENANCE.md` | Monthly, each release, and when the improvement-to-release process changes |
| Component inventory (required/stack-conditional/optional) | `COMPONENTS.md` | During adoption and when adding or changing components |
| Stack-specific minimum verification sets | `STACKS.md` | When choosing a stack or configuring checks |
| Change checklists and verification-by-design rules | `CHECKLISTS.md` | When gate/checklist policy changes |
| Foundation meta (setup, audit, research, examples) | `../SETUP_PROMPT.md`, `../INTERNAL_AUDIT_PROMPT.md`, `../AUDIT_REPORT.md`, `../RESEARCH_DECISION.md`, `../examples/` — classified in the `COMPONENTS.md` optional table | Foundation release or audit activity |

## Permanent engineering standards (foundation governance)

These standards are permanent board-directed rules for every project and for the foundation itself. Each is stated once, in the file that owns it; this index only maps them.

| # | Standard | Owning doc |
| --- | --- | --- |
| 1 | A valid writable execution workspace is established before implementation | `CHECKLISTS.md` (Before work); `ADOPTION.md` (inspect-first step 4) |
| 2 | Canonical sources are preserved; changes happen only in authorized isolated workspaces | `CHECKLISTS.md` (Before work); `HARNESS_MAINTENANCE.md` (Foundation as a maintained product) |
| 3 | Reusable foundation content is version-controlled and independently maintained | `HARNESS_MAINTENANCE.md` (Foundation as a maintained product) |
| 4 | Code implementation is distinguished from verified application behavior | `CHECKLISTS.md` (Verification by design) |
| 5 | Verification evidence identifies the exact content or commit tested | `CHECKLISTS.md` (Verification by design) |
| 6 | Failed or unavailable tests are never represented as passing | `CHECKLISTS.md` (Verification by design) |
| 7 | CI enforcement and branch protection are independently confirmed, never inferred from config files | `CHECKLISTS.md` (Verification by design); `BASELINE.md`; `../README.md` (Start here) |
| 8 | Foundation changes pass independent review and appropriate QA before release | `HARNESS_MAINTENANCE.md` (Lessons process; Foundation as a maintained product) |
| 9 | Every adoption records the installed foundation version and project-specific adaptations | `ADOPTION.md` (head and checklists); `../README.md`; `../SETUP_PROMPT.md` |
| 10 | Lessons learned are evaluated for incorporation into future foundation releases | `HARNESS_MAINTENANCE.md` (Lessons process) |
| 11 | Git-workspace preflight (eight environment checks) before implementation | `CHECKLISTS.md` (Git-workspace preflight) |

## Documentation standards for persistent knowledge

The repository is the durable memory. Create or update documentation when: an architecture decision is made (ADR in `decisions/`), an interface or public contract changes, a dependency is added or upgraded, behavior visible to users or callers changes, or a documented limitation is resolved or newly discovered.

Status claims must match verified repository state: an index row, checklist, or status field may claim "present" or "verified" only when the referenced file or command actually exists in the repository and was executed at a recorded revision — never on a document's self-description. Review claims against source and test results (`docs/CHECKLISTS.md`).

`AGENTS.md` stays a concise router: rules and links only. Project knowledge belongs in the domain files it indexes; do not duplicate it into `AGENTS.md`.

## Document verification status

Until project-specific content replaces required markers, foundation verification intentionally fails. Review stale claims against tests and source code rather than treating documents as ground truth merely because they exist.
