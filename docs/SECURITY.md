# Security

rpn-calc is an offline, single-process calculator. Its attack surface is intentionally minimal.

## Posture

- **No network, no filesystem writes, no dynamic execution.** The `security` check (`tools/security.py`) fails the gate if `app/` contains secret-shaped literals, `eval`/`exec`/`compile`/`__import__`, `pickle`, `ctypes`, `subprocess`, or `os.system`.
- **No secrets in code.** The tool takes only expression tokens from argv; there is no configuration, no credentials, no environment reads in `app/`.
- **No unsafe input handling.** Expression tokens are parsed to `float` or matched against four operators; everything else raises `RpnError` and exits `2`. There is no shell interpolation anywhere.

## Rules for contributors

1. New dependencies are disallowed by default; the codebase is stdlib-only (`docs/STACKS.md` minimums for Python).
2. Any change introducing I/O, subprocess use, or dynamic execution in `app/` must update this document and the `security` check with a concrete justification, never a blanket allow.
3. Untrusted input is still untrusted: expression text from other systems must pass through the same argv path; do not add string-concatenated evaluation.

## Verification

`python3 tools/security.py` runs as the `security` category on every `verify.py --ci` invocation.
