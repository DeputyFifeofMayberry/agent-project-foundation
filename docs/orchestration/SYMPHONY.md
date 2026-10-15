# Symphony — Codex-centered alternative

Symphony is a task orchestration specification with an Elixir/OTP reference implementation. Its reference runner polls issues, allocates workspaces, and starts Codex App Server. The reference implementation is explicitly described by OpenAI as **prototype software intended for evaluation**. Do not treat it as a validated drop-in replacement for Paperclip.

## Evaluation procedure

1. Keep this foundation and its CI rules independent. Confirm the real repository and target machine/toolchain are compatible; official binary release targets documented are macOS/Linux, not native Windows.
2. Review current [Symphony repo](https://github.com/openai/symphony) and [Elixir README](https://github.com/openai/symphony/blob/main/elixir/README.md). Pin an approved release/commit and verify available tracker support.
3. In an isolated environment, copy and customize the upstream `WORKFLOW.md` to the current schema. Do not assume this foundation includes a deployable workflow.
4. Wire feature contracts, acceptance evidence, `python scripts/verify.py --ci`, reviewer gate, and human approval for high-risk changes. Require protected PR merge independently of a Symphony completion signal.
5. Test task lifecycle, workspace isolation, secret scope, operator block/approval, restarts, review handoff, child processes, and persistent evidence links.
6. Compare 10–20 representative tasks using similar models and the same project tests. If migrating, use one orchestrator per branch/task; never let Symphony and Paperclip independently mutate the same worktree.

## Recommendation

Pilot only if Paperclip fails its reliability/permissions gates or if a Codex-specific orchestration workflow becomes preferable. No independent Paperclip-vs-Symphony reliability benchmark is known from the cited sources.
