"""Architecture: enforce the dependency rules recorded in ARCHITECTURE.md."""
import ast
from pathlib import Path

root = Path(__file__).resolve().parents[1]
ALLOWED_MODULES = {"greeter"}
ALLOWED_STDLIB = {"__future__", "argparse", "sys", "unittest", "subprocess", "zipfile",
                  "re", "ast", "pathlib", "shutil"}
FOUNDATION_INFRA = {"verify.py", "selftest_verify.py"}
violations = []
for rel in ["greeter.py", *sorted(str(p.relative_to(root)) for p in (root / "tests").glob("*.py")),
            *sorted(str(p.relative_to(root)) for p in (root / "scripts").glob("*.py"))]:
    if Path(rel).name in FOUNDATION_INFRA:
        continue
    tree = ast.parse((root / rel).read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        mods = []
        if isinstance(node, ast.Import):
            mods = [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom) and node.module:
            mods = [node.module]
        for mod in mods:
            top = mod.split(".")[0]
            if top not in ALLOWED_MODULES and top not in ALLOWED_STDLIB:
                violations.append(f"{rel}: imports non-allowlisted module '{mod}'")
if violations:
    print("architecture: FAILED")
    for v in violations:
        print(" ", v)
    raise SystemExit(1)
print("architecture: OK (imports within allowlist; single-module design respected)")
