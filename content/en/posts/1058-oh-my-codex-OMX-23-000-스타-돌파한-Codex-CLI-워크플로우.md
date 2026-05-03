---
title: "oh-my-codex (OMX): The 23,000-Star Codex CLI Workflow"
date: 2026-04-17T02:03:52+09:00
slug: "1058-oh-my-codex-OMX-23-000-스타-돌파한-Codex-CLI-워크플로우"
original_url: "https://memoryhub.tistory.com/1058"
tistory_id: 1058
draft: false
---

```
        ┌─────────────────────────────┐
        │   OMX Workflow Layer        │
        │  $deep-interview / $ralplan │
        │     $team   /   $ralph      │
        └──────────────┬──────────────┘
                       │
                       ▼
        ┌─────────────────────────────┐
        │     OpenAI Codex CLI        │
        │   (Execution Engine)        │
        └──────────────┬──────────────┘
                       │
                       ▼
        ┌─────────────────────────────┐
        │  .omx/  — plans · logs ·    │
        │          memory · state     │
        └─────────────────────────────┘
```

If you've tried Codex CLI lately, you've probably hit this pain point: needing to rebuild context from scratch each session, manually creating worktrees for multi-agent work, and having to write new config files just to add a hook.

That's why `oh-my-codex` (OMX), which hit 23,000+ stars on GitHub in April, is getting attention.

By the end of this article, you'll understand what OMX is, why you should install it, and how to spin up your first session in 30 minutes.

## One-Line Summary

OMX is a thin layer that sits on top of OpenAI Codex CLI, adding standard workflows, skills, and persistent state (`.omx/`) without replacing Codex itself.

## Why OMX Now?

Codex CLI is lightweight and powerful, but real-world work reveals a few key gaps:

| Gap | Codex CLI Alone | With OMX |
| --- | --- | --- |
| Multi-agent coordination | Users manually set up worktrees and tmux | `$team N:executor` auto-branches |
| Session persistence | Context vanishes when session ends | `.omx/` stores plans, logs, memory |
| Standard workflow | Each session starts from scratch | `$deep-interview` → `$ralplan` → `$ralph` pipeline |
| Hook integration | Direct editing of `.codex/hooks.json` | OMX-managed wrapper auto-registers |

Let me clarify the terms first:

- **Codex CLI**: OpenAI's official terminal coding agent. Install with `npm install -g @openai/codex`. It's the execution engine running models like GPT-5.4 and GPT-5.3-Codex.
- **OMX (oh-my-codex)**: A TypeScript-based npm package adding workflows, skills, runtime, and HUD on top of Codex CLI. MIT licensed, first released 2026-02-02, v0.12.1 as of 2026-04-16.
- **skill**: Reusable commands OMX registers. The four recommended core skills are `$deep-interview`, `$ralplan`, `$ralph`, and `$team`.

## The Core Idea

> OMX leaves Codex's code generation ability untouched and standardizes "how to get things done."

Think of it this way: if Codex is the **brain**, OMX is the **operations manual + office**. The manual (skills) defines when and what to call, while the office (`.omx/`) stores ongoing plans and records so the next session knows where you left off.

Setup takes two lines:

```
# Node.js 20+ required
npm install -g @openai/codex oh-my-codex
omx setup
```

`omx setup` installs `.codex/config.toml`, OMX-managed hooks, agent scaffolding, and skill bundles all at once.

If you have existing user hooks in `.codex/hooks.json`, they're preserved—only the OMX wrapper is updated. This is idempotent and safe to re-run.

## Hands-On: Spinning Up Your First Session

### ① Installation and Authentication

```
npm install -g @openai/codex oh-my-codex
codex   # First time: log in with ChatGPT account or API key
omx setup
```

After setup, check with `omx doctor`. Output should look something like:

```
✔ codex CLI detected (v...)
✔ .codex/config.toml ready
✔ OMX-managed hooks installed
✔ tmux available
```

### ② Recommended First Run

```
omx --madmax --high
```

`--madmax --high` is OMX's "launch strong" mode.

An interactive leader session spins up immediately, ready for skill commands.

### ③ Try the Standard Four-Step Workflow

Inside a Codex session, enter commands in sequence:

```
$deep-interview "I want to rewrite JWT refresh logic. The boundary conditions are fuzzy"
$ralplan "Based on clarified intent, please approve a safe implementation plan"
$ralph "Take responsibility for the approved plan and drive it to completion"
# Or if parallel work is needed:
$team 3:executor "Execute the approved plan with 3 people in parallel"
```

Each skill's role:

- `$deep-interview`: Clarify requirements and non-goals. Start here if things are fuzzy.
- `$ralplan`: Convert the clarified scope into an architecture and implementation plan for approval.
- `$ralph`: One owner takes full responsibility and loops through verification until done.
- `$team N:role`: tmux + isolated git worktrees run N people in parallel. Worktree isolation means zero merge conflicts.

### ④ Supporting Commands

```
omx team status <team-name>     # Check progress
omx team resume <team-name>     # Resume paused team
omx hud --watch                 # Real-time monitoring HUD
omx explore --prompt "Find where team state is recorded"
omx sparkshell git status       # Shell-based checks
omx wiki query --input '{"query":"session-start lifecycle"}' --json
```

`omx wiki` is a local Markdown-based search-first wiki MCP server, so you can quickly surface project notes without a vector DB.

## Best Practices Comparison

| Pattern | Pros | Notes |
| --- | --- | --- |
| `$deep-interview` first (Clarify-First) | Block wrong directions and agree on non-goals upfront | Can be overkill for simple tasks—use judgment to skip when work is clear |
| `$ralph` solo loop | One owner ensures consistency through validation | Large work becomes a bottleneck—use `$team` to branch out |
| `$team N:executor` parallel | Auto-isolated worktrees = zero merge conflicts, minimal context loss | Depends on tmux (or psmux on Windows); Intel Macs report `syspolicyd` CPU spikes |
| Native Codex hooks | `.codex/hooks.json` is the formal lifecycle surface; standard-compatible | Keep user area separate from OMX area; trust `omx setup` / `omx uninstall` idempotence |

## Closing Thoughts

OMX doesn't replace Codex CLI—it adds a manual and an office to transform every-session-from-scratch work into a standard pipeline. The recommended flow is simple: `omx setup` to install, `omx --madmax --high` to launch, then follow clarify → plan approval → completion loop or parallel team execution. macOS/Linux + tmux is most stable; Windows should prioritize WSL2.

## References

- [oh-my-codex GitHub Repository (README)](https://github.com/Yeachan-Heo/oh-my-codex)
- [oh-my-codex Official Site](https://yeachan-heo.github.io/oh-my-codex-website/)
- [oh-my-codex npm Package](https://www.npmjs.com/package/oh-my-codex)
- [OpenAI Codex CLI Official Docs](https://developers.openai.com/codex/cli)
- [OpenAI Codex CLI Quick Start](https://developers.openai.com/codex/quickstart)
- [OpenAI Codex GitHub](https://github.com/openai/codex)
- [What Is Oh My Codex (OMX)? Complete 2026 Guide — a2a-mcp.org](https://a2a-mcp.org/blog/what-is-oh-my-codex)
