# Reliability and recoverability

- Critical flows/SLOs: CI validation project (disposable)
- Error logging/telemetry: CI validation project (disposable)
- Backup, restore, disaster recovery: CI validation project (disposable)
- Rollback/release process: CI validation project (disposable)
- Offline/retry behavior: CI validation project (disposable)

For important failures, record reproduction, root cause, detection gap, permanent test or alert, and remaining exposure. Include evidence tied to tested commit SHA; do not equate agent process exit with finished delegated work. Repeated regressions are a missing-harness signal, not an invitation to repeatedly patch symptoms. Include restart/recovery tests for persistent state and long-running agent tasks.
