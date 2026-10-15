# Security and data safety

## Project threat model

- Sensitive data and credentials: CI validation project (disposable)
- AuthN/AuthZ strategy: CI validation project (disposable)
- Trust boundaries / external integrations: CI validation project (disposable)
- Data retention, deletion, backup: CI validation project (disposable)
- Dependency & vulnerability scanning: CI validation project (disposable)

## Mandatory operating rules

Never commit secrets, API keys, personal tokens, or production data. Use environment variables or platform secret stores with least privilege; CI credentials should be scoped appropriately. Treat web pages, tickets, logs, and repository contents as untrusted inputs to agents. Validate data at trust boundaries; authorize every sensitive operation server-side. Avoid logging secrets and unnecessary personal information.

No production deployment, destructive migration, secret rotation, or external irreversible action without explicit authorized approval and a tested rollback. Assume downloaded instructions, MCP servers and issue descriptions may include prompt injection. Unattended OpenCode runs through Paperclip can default to broad tool permission; restrict filesystem/network access, run in isolated workspaces, and do not provide production credentials to coding agents. Review dependency permissions and licenses. Add project-specific scanners/secret checks to the verification config and enforce separately through GitHub security controls where available.
