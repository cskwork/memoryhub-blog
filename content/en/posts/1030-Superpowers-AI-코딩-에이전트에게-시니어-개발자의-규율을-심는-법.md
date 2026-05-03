---
title: "Superpowers: Teaching AI Coding Agents the Discipline of Senior Developers"
date: 2026-02-16T09:21:25+09:00
slug: "1030-Superpowers-AI-코딩-에이전트에게-시니어-개발자의-규율을-심는-법"
original_url: "https://memoryhub.tistory.com/1030"
tistory_id: 1030
draft: false
---

```
  ╔══════════════════════════════════════════════════╗
  ║                                                  ║
  ║   🦸️  S U P E R P O W E R S                     ║
  ║                                                  ║
  ║   ┌──────────┐  ┌──────────┐  ┌──────────┐      ║
  ║   │ Design   │→ │  Plan    │→ │ Execute  │      ║
  ║   │ (Human)  │  │  (Agent) │  │(Subagent)│      ║
  ║   └──────────┘  └──────────┘  └──────────┘      ║
  ║         ↑                           │            ║
  ║         └───── Code Review ─────────┘            ║
  ║                                                  ║
  ║   "Teaching AI the discipline of a senior dev"   ║
  ║                                                  ║
  ╚══════════════════════════════════════════════════╝
```

What happens when you ask an AI coding agent to build a feature? In most cases, the agent immediately spits out 200 lines of code.

No design, no testing, no consideration for maintainability.

The result looks like it works, but falls apart the moment you try to extend it.

**Superpowers is an agentic skill framework built to solve this problem, forcing AI agents to work like "disciplined senior developers" instead of "code generators."**

**One-liner summary:** In short, Superpowers is an open-source skill library that automatically injects a design-plan-TDD-code-review workflow into AI coding agents like Claude Code, enabling them to work systematically for hours without human intervention.

## Background

AI coding tools are advancing at a remarkable pace. But no matter how good the tools get, without a "methodology" for agents to follow, output quality remains inconsistent. There are four persistent problems with AI agents repeatedly cited by the developer community.

**First**, implementation without testing. Agents build features but skip testing in most cases.

**Second**, improvisational problem-solving. They approach the same type of problem differently each time and don't follow consistent patterns.

**Third**, unplanned coding. They jump straight into code without considering architecture or impact scope.

**Fourth**, random debugging. When errors occur, they rely on trial-and-error instead of analyzing root causes.

> Superpowers is a framework that injects "design first, plan first, test first"—the discipline of senior developers—into AI coding agents via markdown skill files.

Created by Jesse Vincent in October 2025, this project has received over 40,900 stars on GitHub and works with Claude Code, Codex, and OpenCode.

The key is that it's not just a collection of prompts but a complete workflow system deeply integrated into the agent's development lifecycle.

## Superpowers' Core Structure: Five-Stage Workflow

What fundamentally distinguishes Superpowers from existing AI coding tools is "enforcement" rather than "suggestion." Skills automatically activate based on context, and agents can't skip them. The entire workflow consists of five stages.

**Stage 1: Brainstorming (Design)** -- Activated before code is written. The agent refines vague ideas through Socratic questioning, explores alternatives, and presents designs in digestible sizes. Code writing doesn't start until this stage is passed.

**Stage 2: Git Worktree Creation** -- After design approval, an isolated workspace is created in a new branch. A clean test baseline is verified before moving forward. This manages multiple agents working on different features simultaneously without merge conflicts.

**Stage 3: Implementation Plan Writing** -- Work is broken down into small tasks of 2-5 minutes each. Each task specifies exact file paths, complete code, and validation steps. As creator Jesse Vincent puts it, this plan should be specific enough that a "junior engineer with passion but no taste, no judgment, and who hates testing" can follow it.

**Stage 4: Subagent-Based Development (Execution)** -- The most innovative stage. For each task, a new subagent is deployed to focus exclusively on that work without context pollution. After task completion, a code review subagent performs two-stage review: checking spec compliance first, then code quality. If critical issues are found, progress to the next task is blocked.

**Stage 5: Development Branch Completion** -- When all tasks are done, the full test suite runs, and users choose between merge/PR creation/hold/discard.

The biggest characteristic of Superpowers is that the agent works autonomously for hours while never deviating from the plan.

## TDD Enforcement: The Reality of "Tests Before Code"

The most controversial and effective part of Superpowers is the TDD (Test-Driven Development) skill.

This skill isn't merely suggesting "write tests." If the agent writes code before tests,

it forces that code to be deleted.

It follows the RED-GREEN-REFACTOR cycle. First write a failing test (RED), implement only minimal code to pass it (GREEN), then refactor while keeping tests passing (REFACTOR).

This skill has built-in lists of excuses agents use to avoid TDD and counterarguments to each.

It blocks rationalizations like "it's too simple to need tests," "I'll write tests later," or "let's just follow the spirit."

The fact that these are excuses familiar to human developers shows this skill's design deeply understands real development culture.

## The Skill System: "Markdown Files as Methodology"

The core mechanism of Superpowers is the **Skill** system. Skills are reference guides written as markdown files (SKILL.md), and agents automatically load them based on context. This approach is interesting because non-code documents control agent behavior.

Skills are organized into four main categories:

| Category | Included Skills | Core Role |
| --- | --- | --- |
| Testing | test-driven-development | RED-GREEN-REFACTOR cycle, antipattern reference |
| Debugging | systematic-debugging, verification-before-completion | 4-step root cause analysis, post-fix verification |
| Collaboration | brainstorming, writing-plans, executing-plans, subagent-driven-development, etc. | Design refinement, plan writing, parallel subagent work, code review |
| Meta | writing-skills, using-superpowers | Creating new skills, introducing the skill system |

Notable is the writing-skills skill. This meta-skill teaches "how to create skills," and TDD principles apply here too.

When creating a new skill, subagents create test scenarios and verify failure without that skill,

then write the skill and validate passing. Jesse Vincent calls this "TDD for documentation."

## Installation and Usage

For Claude Code users, installation is very simple. Two command lines in the terminal are enough.

```
# Register Claude Code plugin marketplace
/plugin marketplace add obra/superpowers-marketplace

# Install Superpowers
/plugin install superpowers@superpowers-marketplace
```

After installation, restarting Claude Code automatically injects Superpowers bootstrap on session start.

Without additional configuration, requests like "help me plan this feature" or "let's debug this issue" automatically activate relevant skills.

For Codex or OpenCode, manual installation is required: cloning the GitHub repository and setting up symbolic links.

Detailed instructions are available in official documentation.

Installation verification is possible with the `/help` command. If you see `superpowers:brainstorm`, `superpowers:write-plan`, `superpowers:execute-plan` commands, installation was successful.

## When Superpowers Is and Isn't Suitable

| Suitable For | Not Suitable For |
| --- | --- |
| Complex feature development lasting 2+ hours | Fast prototyping or simple refactoring |
| Production code requiring high test coverage | Experimental or exploratory coding |
| Team projects requiring consistent code quality | Preferring development methodologies other than TDD |
| Complex bugs needing systematic debugging | Wanting maximum agent freedom |

Superpowers is a very opinionated framework. This is both an advantage and disadvantage.

Because it enforces certain methodologies including TDD, developers with their own workflows may feel constrained.

Conversely, developers wanting AI agents to maintain consistent quality find structured workflows translate directly to time savings.

## Conclusion

- Superpowers is an open-source skill framework that enforces the workflow of senior developers—design, plan, TDD, code review—on AI coding agents.
- Subagent-based development maintains quality even in hours of autonomous work by deploying new agents per task and automatically performing two-stage code review.
- Practical tip: Claude Code users should run `/plugin install superpowers@superpowers-marketplace` today and verify that the agent starts with design in your next feature development.

## References

- Superpowers GitHub Repository (https://github.com/obra/superpowers)
- Jesse Vincent, "Superpowers: How I'm using coding agents in October 2025" (https://blog.fsck.com/2025/10/09/superpowers/)
- Agent Skills - Superpowers Introduction (https://agent-skills.cc/skills/obra-superpowers)
