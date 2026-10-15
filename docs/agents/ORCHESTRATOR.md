# Orchestration operating contract

This protocol applies to Paperclip, Symphony, or other coordinators; it does not assume any tool is installed.

1. Assign each issue a spec ID and an isolated worktree/branch. Require a baseline commit before work.
2. One implementer owns a bounded code change; a different reviewer sees the original spec and the diff.
3. Do not treat process exit/agent success as issue acceptance; require CI result tied to the submitted commit and evidence for each criterion.
4. Do not start new merges while there is unresolved background/subagent work for that task.
5. After two unsuccessful revisions, mark BLOCKED, record the root-cause hypotheses, and escalate for human decision. **Implement this in a controller/watchdog or manual policy if the orchestrator lacks an enforced retry cap.**
6. Use limited concurrency by default, short-lived scoped credentials, nonzero run timeouts, and no production secrets in untrusted agent environments.
7. Never auto-merge a task with failed/missing checks, blocked review, unapproved destructive operations, or ambiguous application test evidence.
8. If review and implementation occur in different environments, compare commit SHA and reproduce required checks from clean checkout.
