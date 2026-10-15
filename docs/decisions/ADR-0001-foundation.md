# ADR-0001: Repository-owned agent development foundation

- Status: Proposed; must be accepted by product owner after adoption
- Date: 2026-10-14
- Context: Long-running AI coding projects need durable specifications, verification, and decisions beyond individual agent session contexts.
- Decision: Maintain compact `AGENTS.md` navigation, repository-local specs, ADRs, executable quality checks, and protected-branch CI. Keep orchestration interchangeable.
- Consequences: Requires initial configuration and maintenance, but reduces dependence on prompt memory. Does not guarantee defect-free output; application tests still need to be built.
- Revisit if: the workflow adds needless overhead without lowering rework across a representative task sample.
