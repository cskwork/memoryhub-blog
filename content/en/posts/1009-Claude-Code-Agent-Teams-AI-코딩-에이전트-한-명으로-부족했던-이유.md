---
title: "Claude Code Agent Teams: Why One AI Coding Agent Wasn't Enough"
date: 2026-02-06T03:01:49+09:00
slug: "1009-Claude-Code-Agent-Teams-AI-코딩-에이전트-한-명으로-부족했던-이유"
original_url: "https://memoryhub.tistory.com/1009"
tistory_id: 1009
draft: false
---

```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║     ┌─────────┐   ┌─────────┐   ┌─────────┐        ║
║     │ Agent 1 │   │ Agent 2 │   │ Agent 3 │        ║
║     │ Frontend│   │ Backend │   │  Test   │        ║
║     └────┬────┘   └────┬────┘   └────┬────┘        ║
║          │             │             │               ║
║          └──────┬──────┘──────┬──────┘               ║
║                 │             │                       ║
║          ┌──────▼─────────────▼──────┐               ║
║          │      TEAM  LEAD           │               ║
║          │   Task List + Mailbox     │               ║
║          └───────────────────────────┘               ║
║                                                      ║
║        Claude Code  Agent Teams                      ║
║     Multi-Agent  Orchestration                       ║
╚══════════════════════════════════════════════════════╝
```

# 

Any developer who has used Claude Code has probably experienced this: you assign a large refactoring task and the context window bottlenecks, or you ask it to review a PR and it catches security issues well but misses performance problems. Expecting one AI agent to do everything is no different than assigning one developer frontend, backend, testing, and documentation simultaneously.

**Claude Code Agent Teams is a multi-agent orchestration system where multiple AI agents each take on distinct roles, communicate with each other, and collaborate in parallel.**

To put it plainly, Agent Teams is an experimental Claude Code feature that solves the context window limitations of a single agent and enables parallel processing of complex tasks. When used in the right situations, it can significantly boost development efficiency.

## Background

In December 2025, a developer running the `strings` command on the Claude Code binary discovered something interesting: a complete multi-agent orchestration layer named TeammateTool hidden behind a feature flag. This discovery sparked significant interest on Hacker News with over 200 comments, and the community even created unofficial access tools.

Then in early 2026, Anthropic officially registered this feature in the documentation as Agent Teams.

There's an industry-wide trend behind the emergence of this feature. According to Gartner, inquiries about multi-agent systems increased 1,445% from Q1 2024 to Q2 2025. By the end of 2026, an estimated 40% of enterprise applications will include task-specialized AI agents.

The transition from single-agent to team orchestration is a paradigm shift similar to the move from monolithic to microservices in software development history.

> Agent Teams is a multi-agent collaboration system where a single leader session creates multiple independent Claude Code instances (teammates), coordinating parallel work through a shared task list and messaging system.

So how does this differ from existing subagents? Understanding this difference is the first step to properly leveraging Agent Teams.

## Subagents vs Agent Teams: Core Differences

Think of it in terms of company organization. A subagent is an **errand runner**.

When the team lead says "go investigate this," it just reports back results.

It can't talk to other errand runners, and only the team lead receives the results.

Agent Teams teammates, on the other hand, are **project team members**.

Each has their own independent workspace, exchanges messages with each other, and autonomously progresses through work while looking at the shared kanban board (task list).

| Comparison | Subagent | Agent Teams |
| --- | --- | --- |
| Context | Own context window, returns results only to caller | Own context window, completely independent |
| Communication | Reports results only to main agent | Direct message exchange between teammates |
| Coordination | Main agent manages all tasks | Self-coordinated through shared task list |
| Best For | Focused work needing only results | Complex work requiring discussion and collaboration |
| Token Cost | Relatively cheaper (results summarized on return) | Relatively expensive (each teammate is a separate instance) |

**Here's the key point:** Do workers need to communicate with each other?

If communication isn't necessary, use subagents. If teammates need to share findings and challenge each other, Agent Teams is the right choice.

## Architecture: How It Works

Agent Teams consists of four core components.

**The Team Lead** is the main Claude Code session. It creates the team, generates teammates, and coordinates overall work.

With Delegate Mode enabled, the lead can focus purely on coordination without writing code directly.

**Teammates** are each independent Claude Code instances. They have their own context window and load base context like the project's CLAUDE.md and MCP servers, but don't inherit the leader's conversation history.

This design is important because each teammate starts with a **fresh context window, maintaining around 40% context per teammate instead of 80-90% that a single agent would fill**.

**The Task List** works like a shared kanban board. Tasks have three states: pending, in progress, and completed. You can also set dependencies between tasks.

When one task completes, dependent follow-up tasks automatically become unblocked.

File locking prevents race conditions where multiple teammates grab the same task simultaneously.

**The Mailbox** is the messaging system between agents. Use `message` for a specific teammate and `broadcast` for all. When a teammate sends a message, it's automatically delivered to the recipient, and the lead gets auto-notified when a teammate finishes and stops.

All this data is stored in the local file system.

```
~/.claude/
├── teams/{team-name}/
│   ├── config.json        # team metadata, member list
│   └── messages/          # message inbox between agents
└── tasks/{team-name}/     # team task list
```

It's notable that this is file-based locally, not cloud-based. Agent coordination happens through the file system alone, with no complex infrastructure needed.

## Hands-On Practice

### Step 1: Enable Agent Teams

Agent Teams is an experimental feature and disabled by default. You need to set an environment variable or add it to settings.json.

```
// ~/.claude/settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Or set it directly in your shell environment.

```
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

### Step 2: Create a Team and Give Instructions

After enabling, run Claude Code and give natural language instructions for team composition and tasks.

The important part is **assigning tasks that each role can perform independently**.

```
Create an agent team to review the UX of a CLI development tool.
One person for user experience, one for technical architecture,
and one as a devil's advocate.
```

Claude creates the team, builds the task list, and assigns teammates to each role to start work.

### Step 3: Choose Display Mode

There are two modes for monitoring teammate work.

**In-process mode** is the default. All teammates run in a single terminal. Use `Shift+Up/Down` to select teammates and send messages directly. No additional setup needed, most convenient.

**Split-pane mode** gives each teammate their own terminal window. Requires tmux or iTerm2, letting you watch all teammate outputs simultaneously.

```
// configure in settings.json
{
  "teammateMode": "in-process"   // or "tmux"
}
```

### Step 4: Talk Directly with Teammates

Each teammate is a fully independent Claude Code session. You can give instructions or ask follow-up questions directly without going through the lead.

- In-process mode: Select teammate with `Shift+Up/Down` then type
- Split-pane mode: Click the teammate's window to interact directly

### Step 5: Complete Work and Cleanup

When work finishes, shut down teammates and clean up resources. Order matters here.

```
shut down the research teammate      # stop individual teammate
(after all teammates are stopped)
clean up the team                    # lead cleans shared resources
```

If you try to clean up while teammates are still running, it fails. Always stop teammates first, then have the lead do the cleanup. If a teammate executes cleanup, resources can be left in an inconsistent state, so **always do cleanup through the lead**.

## Real-World Usage Scenarios

### Parallel Code Review

A single reviewer tends to focus on one type of issue at a time. Separating security, performance, and test coverage into independent domains enables thorough review from all angles simultaneously.

```
Create an agent team to review PR #142.
- One person focuses on security vulnerabilities
- One analyzes performance impact
- One validates test coverage
Each reviews independently and reports findings.
```

### Competing Hypothesis-Based Debugging

Solve the problem where one agent picks a hypothesis and stops exploring when the cause is unclear.

With multiple teammates each developing different hypotheses and creating a debate structure where they **try to disprove each other's theories**, the surviving theory has a higher probability of being the actual root cause.

```
Investigate why the app crashes after a user sends one message.
Have 5 teammates each develop different hypotheses,
and have them debate to disprove each other's theories.
Proceed like a scientific discussion and update the document with agreed conclusions.
```

### Cross-Layer Feature Development

When frontend, backend, and testing all need to change for a feature, having each layer managed by a separate teammate enables parallel work without file conflicts.

## Best Practices/Pattern Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Plan Approval Mode | Teammates submit plans to the lead for approval before implementation. Can block risky changes pre-emptively | Since the lead makes judgment calls, specify criteria in the prompt like "only approve plans with test coverage" |
| Delegate Mode | Lead focuses on coordination instead of coding. Prevents lead from intercepting tasks | Enable with `Shift+Tab`. Disable when the lead needs to write code directly |
| 5-6 Tasks per Teammate | Teammates stay busy without idle time. Can reassign blocked work | Too many small tasks exceed coordination overhead. Design around clear deliverables |
| File Ownership Separation | Each teammate owns a different file set. Prevents overwrites in parallel editing | Conflicts occur if two teammates edit the same file. Must set file boundaries beforehand |

## Important Constraints to Know

You must understand that Agent Teams is still an experimental feature. The major known constraints are:

**No Session Resume**: in-process teammates can't be restored with `/resume` or `/rewind`. After resuming a session, the lead might try to message teammates that no longer exist, so create new teammates instead.

**Task State Lag**: Sometimes teammates don't update task status after completion. Dependent follow-up tasks can get blocked, requiring manual verification.

**One Team per Session**: A single lead can only manage one team at a time. To start a new team, you must clean up the existing one first.

**No Nested Teams**: Teammates can't create their own teams or sub-teams. Only the lead manages teams.

**Increased Token Cost**: Each teammate uses a separate context window, so token usage scales with the number of teammates.

Research, review, and new feature development where parallel exploration has high value justify the extra cost, but everyday work is more efficient with a single session.

## Closing Thoughts

- Agent Teams shines in complex work requiring parallel exploration and mutual verification by running multiple Claude Code instances as a team—a multi-agent orchestration feature that truly delivers.
- The core difference from subagents is direct communication between teammates and self-directed coordination via shared task lists. Separating file ownership to prevent conflicts is essential for successful operation.
- Real-world tip: Start with read-only tasks like code reviews or bug investigation where code writing isn't needed. Once you feel the value of parallel exploration, expand into feature development.

## References

- Build with Claude Code - Agent Teams Official Documentation (<https://code.claude.com/docs/en/agent-teams>)
- Claude Code Swarm Orchestration Skill (<https://gist.github.com/kieranklaassen/4f2aba89594a4aea4ad64d753984b2ea>)
- Claude Code's Hidden Multi-Agent System Analysis (<https://paddo.dev/blog/claude-code-hidden-swarm/>)
- What Is the Claude Code Swarm Feature? (<https://www.atcyrus.com/stories/what-is-claude-code-swarm-feature>)
