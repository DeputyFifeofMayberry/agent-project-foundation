# Quality score

Weekly-ish self-assessment for rpn-calc; score each 0–2 and total out of 16 (one point-pair per mandatory check category).

| Category | Criterion | Score | Notes |
|---|---|---|---|
| lint | AST rules pass; rules name file+line | 2 | `tools/lint.py` |
| typecheck | 100% annotation coverage in `app/` and `tools/` | 2 | `tools/typecheck.py` |
| unit | Every engine error class covered | 2 | 7 unit tests |
| integration | CLI contract covered in-process | 2 | 4 tests |
| e2e | Real subprocess paths incl. errors | 2 | 4 paths |
| build | Artifact builds and smoke-runs | 2 | zipapp in temp dir |
| security | Scan clean; posture documented | 2 | `docs/SECURITY.md` |
| architecture | Dependency rules enforced, not aspirational | 2 | `tools/architecture.py` |

**Current total: 16/16.**

## Deductions trigger

Any red check, any skipped-or-weakened check (no-op commands are rejected by the verifier), any undocumented new failure mode in `docs/RELIABILITY.md`, or any regression reaching `main` without a regression test drops the affected row to 0 until fixed. Score history lives in `docs/REVIEW_EVIDENCE.md`.
