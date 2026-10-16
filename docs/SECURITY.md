# Security guarantees

- No network access, no persistence, no secrets read; attack surface is CLI args only.
- Inputs are validated (`greet` rejects empty-after-trim names); no shell is invoked by the application.
- `scripts/security_scan.py` (gate category `security`) fails the build on credential-pattern matches in first-party sources.
- Dependency policy: stdlib only (`ARCHITECTURE.md` change control); new dependencies require an ADR and allowlist update.
