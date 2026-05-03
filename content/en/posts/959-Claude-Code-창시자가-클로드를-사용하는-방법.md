---
title: "How the Claude Code Founder Uses Claude"
date: 2026-01-03T18:13:48+09:00
slug: "959-Claude-Code-창시자가-클로드를-사용하는-방법"
original_url: "https://memoryhub.tistory.com/959"
tistory_id: 959
draft: false
---

In early January 2026, Claude Code founder Boris Cherny shared his daily setup in a long thread. He calls it "vanilla," but it's actually a systematic set of small repeatable actions that compound into significant impact. This article translates those actions into a practical playbook you can copy, apply, and expand within your own workflow. The goal isn't to imitate exact settings but to borrow principles and apply them to your team, repository, and constraints.

## Target Audience

- Already using Claude Code but want more consistent results
- Managing or influencing team workflow and wanting shared guardrails
- Comfortable configuring simple automation (files, hooks, commands)

## 13 Ways

### 1) Run Multiple Claudes in Parallel — Then Label Them

He runs 5 terminal sessions simultaneously and numbers tabs for easy tracking. He also leverages system notifications (e.g., iTerm2) so sessions can run while you work on other things. The key is throughput: maintain momentum on independent tasks without waiting for one session to finish. Numbering seems trivial but lets you quickly scan progress while switching between tabs.

**Try it:** Start with two sessions, give each a purpose (e.g., "refactor" and "test"), keep them separate until commit.

### 2) Intentionally Mix Local and Web Sessions

He maintains multiple browser sessions (often 5-10) alongside local ones, tossing work between them. Use claude.ai/code's web UI, start sessions from Chrome, even start them from your phone for later. The idea is using the interface best suited to the task: terminal when tools and git matter, web for cleaner views or mobile.

**Try it:** Keep one web session for "review and reason" and one local session for "perform edits."

### 3) Pick a Model, Stick to It for Coding

He uses a single model (Opus 4.5 with thinking) for nearly everything. It may be slower per request, but fewer round-trips often make it faster overall. Meta lesson: consistency beats raw speed.

**Try it:** Commit to one model for a week, measure how much re-prompting you do, then decide whether to change.

### 4) Treat CLAUDE.md as Living Team Memory

He keeps a shared CLAUDE.md in git and updates it every time Claude gets something wrong. Think of it as a "do not repeat" ledger plus local style guide. The file is short, focused, and updated in PRs to stay fresh. His team file is just thousands of tokens and covers commands, code style, UI/content guidelines, state management, logging, error handling, debugging, even PR templates.

Here's a minimal editable pattern:

```
# Bash commands
- pnpm test --filter <name>: run focused tests
- pnpm lint: lint before pushing

# Code style
- prefer early return over nested if
- use named exports

# Workflow
- write tests first for non-trivial changes
- update docs if behavior changes
```

### 5) Start in Plan Mode, Then Switch to Auto-Accept Edits

When the goal is a PR, he starts in Plan mode (Shift+Tab twice) and iterates the plan before code changes. Once the plan feels solid, he switches to auto-accept edits to move fast. Plan is the safety rail; auto-accept is the accelerator.

**Try it:** Treat "plan quality" as actual work. If the plan doesn't feel clear, keep refining it instead of coding.

### 6) Turn Repeating Prompts into Slash Commands

Every prompt you repeat becomes a slash command. This reduces your friction and lets Claude invoke the same workflow on its own. He keeps those command files in git so the team shares them, using inline bash to pre-calculate context (so the model doesn't need to ask).

Simple example:

```
---
description: Prepare clean commits and push PR
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git commit:*), Bash(git push:*)
---

# Context
- Status: !`git status -sb`
- Diff: !`git diff --stat`

# Task
Write commit message, commit, and push current branch.
```

### 7) Promote Repeating Roles to Subagents

He uses subagents for repeating tasks like code simplification or end-to-end validation. This keeps the main thread focused and gives each subagent clear permissions.

Minimal subagent template:

```
---
name: verify-app
description: Run the app, validate key flows, report issues.
tools: Bash, Read
model: inherit
---

Validate app changes using standard project commands.
Report failures with exact error output and reproduction steps.
```

### 8) Use Hooks to Make the Last 10% Deterministic

He uses PostToolUse hooks to format code so formatting doesn't become a late surprise. Hooks turn "do this in most cases" into "do this every time," which is how you avoid CI noise.

Example hook config (simplified):

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          { "type": "command", "command": "npm run format" }
        ]
      }
    ]
  }
}
```

### 9) Pre-Allow Safe Tools, Don't Default to YOLO

He avoids blanket permission skipping by default. Instead, he pre-allows a small set of tools he trusts for the repository through /permissions and shared settings (often in .claude/settings.json). It's safer than blanket skipping and faster than endless prompts.

**Try it:** Create a "safe allowlist" and review monthly. Exclude risky commands by default.

### 10) Connect Claude to Real Systems via MCP

He uses MCP to connect Claude to tools like Slack, BigQuery, Sentry, sharing config in .mcp.json. Transforms Claude from code editor to workflow hub.

**Try it:** Start with one system removing daily friction (logs, analytics, tickets), then expand.

### 11) Add Background Validation Stages for Long-Running Tasks

For time-consuming tasks, he sets Claude to validate the work once complete. He uses background agents, Stop hooks, or plugins like ralph-wiggum. He also runs in relaxed permissions mode in the sandbox so the session isn't blocked on prompts. Makes "run and wait" safer, especially when away from desk.

**Try it:** Add a Stop hook that runs smoke tests and posts a short summary to transcript.

### 12) Give Claude Validation Loops (This Is the Multiplier)

His most important tip: give Claude ways to validate its own work. Tests, CLI commands, browser actions—quality improves dramatically when output is verifiable. He even uses the Claude Chrome extension to test UI changes in real browsers.

**Simple validation ladder:**

1. Single command (e.g., pnpm test --filter ...)
2. Small test suite
3. UI check in browser (manual or automated)
4. "Review pass" by another subagent

### 13) Intentionally Share Team Skills and Conventions

He uses shared skills and settings where appropriate while allowing personal tweaks. The key is drawing lines: what matters to the team (shared) vs personal preference (local). Claude Code supports multiple skill directories for exactly this separation.

**Try it:** Keep project skills in git, personal skills in home directory, name them clearly so Claude picks the right ones.

## Starter Kit You Can Copy Today

Want a quick start? These four artifacts deliver 80% of the value:

1. Short CLAUDE.md with commands, style, workflow rules
2. One slash command for your most common loop
3. One subagent for validation or review
4. One hook removing a consistent CI noise source

## Common Pitfalls to Avoid

- **Over-automate too early:** Start with one command or hook, not ten.
- **Skip validation:** If you can't verify it, you're gambling.
- **Messy parallelization:** Label sessions and keep work independent.
- **Bloated memory files:** Keep CLAUDE.md short and review often.

## References

- Boris Cherny, "Claude Code setup thread" (Nitter mirror) — https://nitter.net/bcherny/status/2007179832300581177 — Primary source for 13-step workflow and follow-up answers.
- Claude Code Docs: Terminal notifications — https://code.claude.com/docs/en/terminal-config#iterm-2-system-notifications — Details on system notifications mentioned in setup.
- Claude Code Docs: Slash commands — https://code.claude.com/docs/en/slash-commands — How custom commands work and where to store them.
- Claude Code Docs: Subagents — https://code.claude.com/docs/en/sub-agents — Subagent configuration and best practices.
- Claude Code Docs: Hooks guide — https://code.claude.com/docs/en/hooks-guide — Event-based hooks for formatting, checks, notifications.
- Claude Code Docs: Skills — https://code.claude.com/docs/en/skills — Sharing and configuring team skills.
- Claude Code Docs: Chrome extension — https://code.claude.com/docs/en/chrome — For browser-based validation loops.
- Anthropic Engineering: "Claude Code: Best practices for agentic coding" — https://www.anthropic.com/engineering/claude-code-best-practices — Broader context and workflow patterns.
- Anthropic plugins (ralph-wiggum) — https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-wiggum — Example plugin used for long-running validation
