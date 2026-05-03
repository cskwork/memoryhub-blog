---
title: "If AI Coding Results Differ Each Time, Use Archon Harness Builder"
date: 2026-04-17T01:46:45+09:00
slug: "1054-AI-코딩이-매번-다르게-나온다면-Archon-하네스-빌더로-끝내세요"
original_url: "https://memoryhub.tistory.com/1054"
tistory_id: 1054
draft: false
---

```
   ┌────────┐   ┌────────────┐   ┌────────┐   ┌──────┐
   │  plan  │──▶│ implement  │──▶│  test  │──▶│  PR  │
   └────────┘   └────────────┘   └────────┘   └──────┘
           YAML workflow · deterministic node · AI node
                    .archon/workflows/*.yaml
```

## Introduction

You've probably experienced the frustration of giving the same instruction twice and getting different results.

Even when I tell Claude Code the exact same thing repeatedly—"refactor and run tests"—

sometimes it creates a PR and sometimes it stops midway.

Archon is an open-source project that wraps this "inconsistent AI coding" into reproducible procedures.

After reading this article to the end, you'll understand how to attach it to your project today, from 30-second installation to running your first workflow.

## TL;DR

Archon is the first open-source harness builder like n8n that fixes AI coding procedures into YAML workflows to reliably reproduce the same results every time.

## Why Archon Now

As the term "vibe coding" suggests, AI assistants take slightly different paths each time they receive a request.

This non-determinism is fine for prototypes but becomes a source of quality degradation in team common processes and repetitive work.

Archon's creator positions it as: "What Dockerfile does for infrastructure and GitHub Actions does for CI/CD, Archon does for AI coding workflows."

Note that there's an older project with the same name—the original 'Archon OS' was a Python-based MCP server handling knowledge and task management backbone, but as of April 2026, the repository is completely rewritten as a TypeScript + Bun workflow engine.

This article explains the latest version after the rewrite.

| Term | Definition |
| --- | --- |
| Harness | External skeleton that wraps AI model calls to enforce procedures, validation, and output format |
| Deterministic Node | Stages like `bash:` that execute fixed commands as-is |
| AI Node | Stages using `prompt:` where the model applies intelligence |
| Workflow | Execution plan recording node dependency relationships (DAG) in YAML |

## Core Concept

> Fix AI coding procedures in YAML and fill in intelligence only within that framework.  
> As a result, execution order is deterministic, but AI still handles each stage's judgment.

Below is the smallest sample from official README. You can see the structure where `depends_on` sets dependencies, `loop + until` specifies repeat termination, and `bash:` plugs in validation.

```
# .archon/workflows/sample.yaml  ·  Archon (Bun/TypeScript, 2026-04)
nodes:
  - id: plan
    prompt: "Explore the codebase and create an implementation plan"
  - id: implement
    depends_on: [plan]
    loop:
      prompt: "Read the plan. Implement the next task. Run validation."
      until: ALL_TASKS_COMPLETE
  - id: run-tests
    depends_on: [implement]
    bash: "bun run validate"
  - id: create-pr
    depends_on: [run-tests]
    prompt: "Push changes and create a pull request"
```

There are three key points.

First, each execution runs in a separate git worktree, so running multiple tasks in parallel doesn't interfere.

Second, the same workflow executes in the same order every time, eliminating variance between team members.

Third, committing YAML files to `.archon/workflows/` makes them callable identically from CLI, Web UI, Slack, Telegram, or GitHub.

## Hands-On Practice: From Zero to First Workflow

### ① Preparation

Bun runtime (official bun.sh), GitHub CLI, and Claude Code must be installed.

All three can be installed via official distribution scripts on Mac, Linux, and Windows.

### ② 30-Second Installation

One line below and you have the CLI:

```
# macOS / Linux
curl -fsSL https://archon.diy/install | bash

# Windows (PowerShell)
irm https://archon.diy/install.ps1 | iex
```

### ③ Full Setup (about 5 minutes)

If you want to contribute source or explore internal flows:

```
git clone https://github.com/coleam00/Archon
cd Archon
bun install
claude
```

Then in a Claude Code session, say "Set up Archon" and it handles MCP server registration and default template placement.

### ④ Running Your First Workflow

Navigate to your project root, open Claude Code, and say:

```
Use archon to add dark mode to the settings page
```

The router automatically selects the best match from 17 default workflows based on intent.

To choose manually, check the list with `archon workflow list` then specify by name.

Representative workflows include `archon-assist` (general Q&A/debugging), `archon-fix-github-issue` (investigation to PR), `archon-idea-to-pr` (feature implementation pipeline), `archon-comprehensive-pr-review` (multi-agent review), `archon-refactor-safely` (safe refactoring with validation).

Results are viewable real-time in the Web dashboard.

Running `archon serve` in a new terminal lets you monitor progress, logs, and artifacts in your browser (convenient to run once after installation).

## Approach Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Free Prompting (each time) | Fast start, good for idea exploration | Non-deterministic results, hard to reproduce for teams |
| Archon Workflow | Repeat same order and same validation, safe with parallel worktrees | Initial workflow design cost, Bun/Claude Code dependency |
| Traditional Shell/CI Scripts | Completely deterministic, reuses existing infrastructure | Difficult inserting AI decision steps, limited flexibility |

The three approaches aren't mutually exclusive. Naturally, use free prompting to understand exploration phases, wrap stable repetitive work with Archon workflows, and leave completely deterministic areas like deployment and checks to existing CI.

## Conclusion

The next challenge for AI coding increasingly centers on "more predictable procedures" over "smarter models." Archon places deterministic execution and AI judgment side-by-side in the familiar YAML format, presenting that answer as open-source first.

As of April 2026, it exceeds 18k GitHub stars and is growing rapidly, so

for projects with repetitive work, I recommend creating and attaching one or two workflows.

## References

- Archon GitHub Repository — <https://github.com/coleam00/Archon>
- Archon README (dev branch) — <https://github.com/coleam00/Archon/blob/dev/README.md>
- Archon Official Documentation·Installation Homepage — <https://archon.diy>
- Complete Rewrite Announcement Issue #957 — <https://github.com/coleam00/Archon/issues/957>
- HelloGitHub Introduction Page — <https://hellogithub.com/en/repository/coleam00/Archon>
- AIToolly Article (2026-04-14) — <https://aitoolly.com/ai-news/article/2026-04-14-archon-the-first-open-source-ai-coding-test-framework-generator-for-deterministic-and-repeatable-dev>
