"""Build: produce a real distributable zipapp artifact (staged, no self-inclusion)."""
import subprocess
import sys
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
dist = root / "dist"
dist.mkdir(exist_ok=True)
artifact = dist / "greeter.pyz"
if artifact.exists():
    artifact.unlink()
staging = dist / "_staging"
if staging.exists():
    import shutil
    shutil.rmtree(staging)
staging.mkdir()
(staging / "greeter.py").write_bytes((root / "greeter.py").read_bytes())
subprocess.run([sys.executable, "-m", "zipapp", str(staging), "-o", str(artifact),
                "-m", "greeter:main", "-p", "/usr/bin/env python3"], check=True, cwd=root)
import shutil
shutil.rmtree(staging)
with zipfile.ZipFile(artifact) as zf:
    assert "greeter.py" in zf.namelist(), zf.namelist()
    assert "__main__.py" in zf.namelist()
assert artifact.stat().st_size < 1_000_000, "artifact implausibly large"
print(f"build: OK ({artifact.name}, {artifact.stat().st_size} bytes)")
