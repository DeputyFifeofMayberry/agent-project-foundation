# Reliability and recoverability

- Critical flows/SLOs: TODO_REQUIRED
- Error logging/telemetry: TODO_REQUIRED
- Backup, restore, disaster recovery: TODO_REQUIRED
- Rollback/release process: TODO_REQUIRED
- Offline/retry behavior: TODO_REQUIRED

For important failures, record reproduction, root cause, detection gap, permanent test or alert, and remaining exposure. Include evidence tied to tested commit SHA; do not equate agent process exit with finished delegated work. Repeated regressions are a missing-harness signal, not an invitation to repeatedly patch symptoms. Include restart/recovery tests for persistent state and long-running agent tasks.
