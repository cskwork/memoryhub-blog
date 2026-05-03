---
title: "GSD (Get Shit Done): Solving AI Coding's Context Rot Problem"
date: 2026-02-16T09:44:53+09:00
slug: "1031-GSD-Get-Shit-Done-AI-코딩의-컨텍스트-부패-문제를-해결"
original_url: "https://memoryhub.tistory.com/1031"
tistory_id: 1031
draft: false
---

```
  ┌─────────────────────────────────────────────┐
  │                                             │
  │    ╔═══╗ ╔═══╗ ╔══╦═╗                      │
  │    ║ ╔═╝ ║ ╔═╝ ║  ║ ║                      │
  │    ║ ║╔═╗║ ╚═╗ ║  ║ ║                      │
  │    ║ ╚╝ ║╚═╗ ║ ║  ║ ║                      │
  │    ╚═══╦╝╔═╝ ║ ╚══╩═╝                      │
  │        ╚═╝   ╚═╝                            │
  │                                             │
  │  GET SHIT DONE                              │
  │  Context Engineering for AI Coding          │
  │                                             │
  │  "Complexity lives in the system,           │
  │   workflows stay simple"                    │
  │                                             │
  └─────────────────────────────────────────────┘
```

When working on a project with Claude Code, you encounter something strange. Code that was precise and clean at first becomes increasingly sloppy as conversations lengthen. Instructions get ignored, previous decisions are forgotten,

and it even starts "cutting corners" on its own. This phenomenon is called **Context Rot**, and GSD was born specifically to address this problem head-on.

**One-liner summary:** In short, GSD is a lightweight framework that overcomes Claude Code's context window limitations through subagent orchestration and spec-based development. With over 12,800 GitHub stars, it's emerging as a new standard for AI coding workflows.

---

## Background

The era of AI coding tools is now in full swing. Claude Code, Cursor, GitHub Copilot and others are greatly improving developer productivity, but there's one fundamental limitation.

> Context Rot refers to the phenomenon where response quality gradually deteriorates as tokens accumulate in an LLM's context window.

According to Chroma Research, performance consistently declines across all models as context length increases.

Stanford researchers' "Lost in the Middle" problem shows the same thing: information at the start and end of the context window is found well, but accuracy for information buried in the middle drops by 15-20 percentage points.

In real development environments, this problem is even more serious. When using Claude Code for complex projects, you can feel the quality degradation the moment context usage reaches 70-80% as conversations lengthen.

Claude Code's automatic 'Compaction' (conversation compression) doesn't provide a fundamental solution either.

Because it compresses already-rotted context, in Anthropic's words, it "fixes the rot and makes it worse."

This is exactly where **GSD (Get Shit Done)** enters.

---

## What is GSD?

GSD is a **meta-prompting, context engineering, and spec-based development system** created by solo developer TACHES. It works with Claude Code, OpenCode, and Gemini CLI.

The core philosophy is simple.

> "Complexity goes in the system, user workflow stays simple."

Other spec-based development tools (BMAD, SpecKit, Taskmaster, etc.) exist, but they tend to require enterprise-level processes like sprint ceremonies, story points, and stakeholder syncs. This is overkill for solo developers or small teams.

GSD approaches this differently. Users only see a few slash commands, while internally it automatically handles XML prompt formatting, subagent orchestration, and state management.

---

## The Core Principle: How GSD Solves Context Rot

To explain how GSD solves context rot by analogy: Normal AI coding is like having one person handle a massive project alone, non-stop, without notes. Naturally, they forget earlier content as they progress.

GSD changes this to a **"Project Manager + Specialist Team"** structure. The project manager (orchestrator) manages overall flow only, and the actual work is delegated to a new specialist (subagent) each time with clear instructions.

Specifically, three mechanisms work:

**First, it provides fresh context per task.** Each task plan runs in an independent subagent,

which starts with 200K tokens of clean context. No leftovers from previous work.

The main context window stays at 30-40% level, keeping sessions fast and responsive.

**Second, it eliminates ambiguity with XML-structured prompts.** All task plans are written in Claude-optimized XML format.

Task name, target files, specific action instructions, verification methods, and completion conditions are specified. AI has no room for guessing.

```
<task type="auto">
  <n>Create login endpoint</n>
  <files>src/app/api/auth/login/route.ts</files>
  <action>
    Use jose library for JWT (jsonwebtoken has CommonJS issues).
    Validate credentials against users table.
    Return httpOnly cookie on success.
  </action>
  <verify>curl -X POST localhost:3000/api/auth/login → 200 + Set-Cookie</verify>
  <done>Valid credentials return cookie, invalid returns 401</done>
</task>
```

**Third, it operates a markdown-based context file system.** PROJECT.md (project vision), REQUIREMENTS.md (scoped requirements), ROADMAP.md (direction), STATE.md (decisions and cross-session memory), etc. are injected to each agent only as much as needed.

File size limits are set based on where Claude's quality degrades.

---

## Actual Workflow: Completing Projects in 5 Steps

### ① Project Initialization

```
npx get-shit-done-cc@latest   # Install
/gsd:new-project               # Start project
```

The system asks questions until it understands goals, constraints, tech stack preferences, edge cases, etc.

Optionally, it also performs domain research using parallel agents. Results include PROJECT.md, REQUIREMENTS.md, ROADMAP.md, and STATE.md.

For existing codebases, running `/gsd:map-codebase` first lets parallel agents analyze existing stack, architecture, and conventions.

### ② Discussion Phase

```
/gsd:discuss-phase 1
```

The roadmap has only one or two lines of description per phase. It's difficult to precisely understand what users want from this alone.

At this stage, the system identifies gray areas in implementation and asks about layouts and interactions for visual features, or response formats and error handling for APIs. Results are saved as CONTEXT.md and reflected in subsequent research and planning.

### ③ Planning Phase

```
/gsd:plan-phase 1
```

A researcher agent investigates implementation methods, and a planner writes 2-3 atomic task plans in XML structure.

Then a checker agent validates the plan across 6 dimensions: requirement coverage, task completeness, and dependency accuracy.

The modify-validate loop repeats until it passes.

### ④ Execution Phase

```
/gsd:execute-phase 1
```

Plans execute in waves. Independent plans run in parallel, those with dependencies run sequentially.

An individual Git commit is created per task, so you can use `git bisect` to find exact failure points or revert individual tasks independently.

### ⑤ Verification Phase

```
/gsd:verify-work 1
```

After automated verification confirms code existence and test passing, you manually test features.

When issues are found, a debug agent diagnoses the cause and automatically generates verified fix plans.

Repeat these 5 steps per phase, tag releases with `/gsd:complete-milestone` when milestones complete, then start the next version with `/gsd:new-milestone`.

---

## Best Practices/Pattern Comparison

Here's how GSD differs from existing spec-based development tools:

| Tool | Approach | Advantages | Cautions |
| --- | --- | --- | --- |
| **GSD** | Subagent orchestration + context separation | Eliminates context rot at source, low learning curve, optimal for solo/small teams | Limited to Claude Code/OpenCode/Gemini CLI |
| **BMAD** | Agile team role simulation (PM, Architect, Scrum Master) | Enterprise-grade structure, automated detailed PRD generation | Complex setup, overkill for small projects |
| **SpecKit** | GitHub-native spec management | Tool-agnostic, GitHub ecosystem integration | No context rot mitigation mechanism |
| **Taskmaster** | Task decomposition and tracking | Intuitive task management | Quality degradation possible in single context execution |

The key difference is clear. BMAD, SpecKit, and Taskmaster execute planning, research, development, and verification all **within one context window**.

GSD delegates each phase to **independent subagents**, structurally blocking context rot.

---

## Configuration and Customization

GSD stores project settings in `.planning/config.json`.

**Model Profiles** control which models each agent uses to balance quality and token cost.

| Profile | Planning | Execution | Verification |
| --- | --- | --- | --- |
| quality | Opus | Opus | Sonnet |
| balanced (default) | Opus | Sonnet | Sonnet |
| budget | Sonnet | Sonnet | Haiku |

Profile switching is one line: `/gsd:set-profile budget`

---

## Conclusion

- GSD is an open-source framework solving context rot through subagent orchestration and spec-based development, enabling multi-hour autonomous work without human intervention following a predetermined plan.
- XML-structured prompts and markdown-based context files ensure each subagent has fresh context and clear specifications without ambiguity.
- Practical tip: Today, run `npx get-shit-done-cc@latest` and `/gsd:new-project` to start your first project using GSD. Track how context quality is maintained even as project complexity grows over hours.

---

## References

- GSD GitHub Repository (https://github.com/TACHES/get-shit-done)
- GSD Documentation (https://gsd-docs.dev)
- Agent Skills - GSD Introduction (https://agent-skills.cc/skills/taches-gsd)
