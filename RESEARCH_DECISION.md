# Research decision: OpenAI harness engineering + Paperclip pilot

**Reviewed:** October 14, 2026. **Decision:** Use an OpenAI-style repository harness as the permanent quality system and pilot Paperclip with existing OpenCode/Superpowers. Evaluate Symphony only if Paperclip fails the pilot or the coding runtime shifts primarily to Codex. **This is a reasoned recommendation, not an empirically proven platform ranking.**

## Evidence and its limits

1. **OpenAI harness engineering** documents an internally used agent-built system, approximately one million lines of code and 1,500 merged PRs in five months. Its principles include a small `AGENTS.md` map, versioned specs and execution plans, mechanical architectural rules, testable UI/runtime environments, agent-visible telemetry, CI checks and recurring cleanup. These are first-party observations of one custom system—not a turnkey recipe or a causal reliability experiment. [Primary source](https://openai.com/index/harness-engineering/).
2. **Paperclip** supports an OpenCode local adapter, multi-agent issues, and runtime enforcement of reviewer/approver transitions *if* configured on each issue. The [execution policy](https://github.com/paperclipai/paperclip/blob/master/docs/guides/execution-policy.md) explicitly allows no review stages; it also describes correction loops continuing until a reviewer approves. **An automatic correction cap has not been confirmed; enforce one externally.** [OpenCode adapter](https://docs.paperclip.ing/reference/adapters/opencode/) documents an unattended permission-bypass option defaulting to `true`, a serious risk in an untrusted repository. Two [user-reported](https://github.com/paperclipai/paperclip/issues/889) [adapter defects](https://github.com/paperclipai/paperclip/issues/11615) justify a controlled pilot, not a universal reliability conclusion.
3. **Symphony** offers task-triggered isolated workspaces and Codex App Server loops. Its [official Elixir implementation](https://github.com/openai/symphony/blob/main/elixir/README.md) explicitly calls itself prototype software for evaluation. Its release binaries target Linux/macOS rather than native Windows (at review). It is more Codex-centric; no neutral comparative test establishes superior reliability over Paperclip.
4. **GitHub protected branches and required checks** can mechanically prevent a merge on failed CI, but only when external [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets) are enabled with appropriate bypass restrictions. Neither a passing build nor a successful agent review proves product acceptance.
5. **Templates** preserve the procedure but cannot replace real app-specific tests, device/runtime access, or independent human judgments. The foundation intentionally stays incomplete and red until adopted.

## Comparison and decision

| Dimension | Paperclip + OpenCode | Symphony + Codex |
| --- | --- | --- |
| Match for existing stack | Direct integration, needs adapter/permission validation | Requires Codex-focused runtime and possibly Linux/macOS environment |
| Runtime governance | Optional per-issue review and approval | Task/workspace orchestration; review and evidence workflow must be configured |
| Code quality | Determined by coding model, tests, and CI; not guaranteed | Same |
| Known engineering maturity risk | Adapter edge cases and broad unattended tool permissions | Experimental reference runtime |
| Defensible choice today | **Controlled Paperclip pilot** | **Fallback comparative pilot** |

**Confidence:** high that harness + meaningful tests will improve enforcement relative to instructions alone; moderate that Paperclip is the more convenient first pilot for this setup; low that either orchestrator is intrinsically more reliable on generated code, given missing comparable evidence.

## Pilot decision gates

- First verify one direct OpenCode task without orchestrator using the foundation and protected CI.
- Paperclip must demonstrate proper review/approval routing, explicit permission policy, bounded retry via independent watchdog/manual gate, completion of background subagents, timeout recovery, isolated branches, and rejection of a failing code change.
- Record accepted tasks, post-merge regressions, human intervention minutes, cost per accepted task, and stale/stuck task percentage for 10–20 representative tasks.
- Switch only if clear benefit exceeds operational complexity. Keep infrastructure and source code independent of the orchestrator.

## What this does not establish

It does not prove superior pass rates for Paperclip, Codex, Symphony, or any model; no agent ran on the user's real application and no GitHub ruleset has been configured here. Version-specific interfaces may change; verify upstream immediately before installing.
