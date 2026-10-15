# Architecture contract

**Status:** unverified template. Complete with facts from the actual repository before allowing architectural changes.

## System map

- Entry points: protection-test project (disposable)
- Main services/modules: protection-test project (disposable)
- Storage and schemas: protection-test project (disposable)
- External APIs and trust boundaries: protection-test project (disposable)
- Deployment environments: protection-test project (disposable)
- Runtime observability and logs: protection-test project (disposable)

## Dependency rules

Document actual module dependency directions, allowed shared modules, and prohibited cross-domain imports. Add code-enforced dependency rules for your real language/framework (for example dependency-cruiser, ESLint import rules, custom Python import checks). Do **not** present an illustrative architecture as an existing one.

Proposed default for new apps: UI -> application/service -> domain -> data adapters, with separate typed contracts and validated inputs at trust boundaries. Adapt to the actual stack and publish ADR if choosing a different organization.

## Change control

- Public API, schema, auth boundary, persistent state, background jobs, and deployment changes require an impact inventory and migration/backout plan.
- New libraries need rationale, licensing/security check, and cost/maintenance consideration.
- Tests must cover existing relevant contracts before architecture migration.
- Describe key invariants here and implement machine checks where possible.
