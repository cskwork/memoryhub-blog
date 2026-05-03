---
title: "Claude Code Architecture Analysis: Why Everyone Calls it the 'Field Engineer'"
date: 2026-04-07T06:43:17+09:00
slug: "1048-Claude-Code-구조-분석-왜-다들-cc를-현장-엔지니어-라고-부를까"
original_url: "https://memoryhub.tistory.com/1048"
tistory_id: 1048
draft: false
  hidden: false
cover:
  image: "/images/1048-Claude-Code-구조-분석-왜-다들-cc를-현장-엔지니어-라고-부를까/OIP-a4f2bc3b.png"
  alt: "Enabling Claude Code to work more autonomously \\ Anthropic"
  relative: false
  hidden: false
---

[![Enabling Claude Code to work more autonomously \ Anthropic](/images/1048-Claude-Code-구조-분석-왜-다들-cc를-현장-엔지니어-라고-부를까/OIP-a4f2bc3b.png)](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously?utm_source=chatgpt.com)

## Introduction

- When using AI coding tools, the answers often look convincing, but you typically still have to manually modify files and run tests yourself. Claude Code stands apart from other tools at that exact point. It's not just a question-answer tool, but an executable CLI that connects file reading, editing, shell execution, and web search.
- The core, in particular, isn't in "good answers" themselves, but in **the loop of receiving a question → choosing tools → checking permissions → executing → reassessing.** A user makes one request, but internally multiple API calls and tool executions repeat.
- After reading this article, you'll understand structurally "why this tool appears to be production-oriented."

## TL;DR

- Claude Code's essence is an agentic CLI architecture that transforms natural language requests into safe tool execution loops and pushes work all the way to completion.

## Background

- This article is based on a WikiDocs document that analyzes a Claude Code source snapshot as of `2026-03-31`, explaining approximately `1,884` TypeScript + React files with focus on structure. The document states it doesn't disclose the source code itself but focuses on operating principles and layer architecture.

| Item | Simple Explanation |
| --- | --- |
| Identity | Official Claude Code CLI that runs in terminal |
| Implementation Language | TypeScript |
| Display Format | Terminal UI created with Ink based on React |
| State Management | Zustand |
| Build | bun |
| Core Feature | Doesn't just answer—executes files, commands, searches, and external tools |
| Extension Method | MCP enables connection to external functions like GitHub, Slack, DB |

- Knowing these terms helps reading. Tool is the execution means AI uses, Command is instructions users call directly like `/commit`. MCP is the connection standard for attaching external services to Claude Code.
- Claude Code has 45+ built-in tools and 80+ commands. ([WikiDocs](https://wikidocs.net/338204))

## Core

> Claude Code is not "conversational AI" but a work engine designed around tool execution loops.

- The overall structure consists of four stages: `STARTUP → QUERY LOOP → TOOL EXECUTION → DISPLAY`. Understanding just these four boxes makes it much easier to read where 1,800+ files belong. ([WikiDocs](https://wikidocs.net/338204))
- In the STARTUP initialization stage, authentication, model selection, settings loading, Git status and context collection like `CLAUDE.md` happen first. This also includes startup optimizations like parallel I/O pre-execution and conditional module loading.
- In QUERY LOOP, streaming responses, `tool_use` detection, long conversation compression, and error recovery are key. The document explains managing token limits with strategies like Snip Compact, Microcompact, and Auto-Compact.
- In TOOL EXECUTION, balancing speed and safety is crucial. Safe tools execute up to 10 in parallel, while high-risk tasks like editing or Bash run sequentially and solo.
- The mechanism controlling this strong execution capacity is the permission system. Input validation, per-tool permission checking, custom hooks, `alwaysAllow`·`alwaysDeny` rules, and mode-based approval policies work in sequence.

```
[User Input]
      ↓
[STARTUP]
Authentication / Model selection / Settings / Git status / CLAUDE.md
      ↓
[QUERY LOOP]
Streaming response / tool_use detection / Context compression
      ↓
[TOOL EXECUTION]
Read / Edit / Bash / Web / MCP
      ↓
[DISPLAY]
Display results / diff / progress
      ↑
      └──── If tool_use remains, loop again
```

## Hands-On Practice

## Understanding Tool and Command Separately

1. - Tool is functionality AI uses automatically; Command is functionality users call directly.
   - For example, file reading and editing are Tools, while `/commit`, `/review`, `/settings` are Commands.
   - Grasping this distinction makes Claude Code's internal structure much less confusing.   
     `Tool = FileRead / FileEdit / Bash / WebSearch`  
     `Command = /commit / review / settings / help`
2. Memorize the permission pipeline separately
   - From a practical standpoint, the most important part is "what's prevented" over "what's possible."
   - Requests flow through `validateInput()` → `checkPermissions()` → `PreToolUse hooks` → rule matching → permission mode determination.

```
[Tool Request Arrives]
      ↓
1) validateInput()
      ↓
2) checkPermissions()
      ↓
3) PreToolUse hooks
      ↓
4) Rule Matching
   - alwaysAllow → Approve
   - alwaysDeny  → Deny
   - alwaysAsk   → User confirmation
      ↓
5) Mode Determination
   - Default
   - Auto
   - Plan
   - Bypass
```

4. Tie together extension points at the end
   - Understanding Claude Code as just a CLI is half-understanding.
   - The documentation describes attaching external tools via MCP, bundling complex operations with Skills and Plugins, and in Coordinator mode, the reader agent operates workers in parallel.
   - The key is that it extends like a platform beyond just tools. ([WikiDocs](https://wikidocs.net/338204))
   - `Leader Agent` → `Worker 1 Research` / `Worker 2 Modify` / `Worker 3 Test` → `Leader Synthesis`

## Best Practices and Pattern Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Query loop-centered design | Automatically breaks down one request into multiple executions, good for connecting to actual work | As loops grow longer, context compression and recovery strategies become critical |
| Safe/unsafe tool separation execution | Read operations parallelize quickly, modification operations controllable without conflicts | Wrong tool classification easily loses either speed or stability |
| Permission pipeline-first design | Realistically controls strong execution tools | Complexity rises as rules and modes multiply |
| MCP·Skill·Plugin extension | Utilization scope greatly expands to GitHub, Slack, DB, etc. | Needs integrated design of permissions, authentication, failure handling for stability |
| Reader-Worker Coordinator pattern | Large tasks split into parallel work, increasing processing speed | Quality variance increases if reader doesn't validate results |

- The comparison table above reorganizes tool concurrency models, permission systems, MCP extension, and coordinator mode from a practical patterns perspective.

## Conclusion

- The essence is making you see Claude Code not as "an AI that answers well" but as "an execution system that actually works." ([WikiDocs](https://wikidocs.net/338204))
- It's particularly striking that performance, safety, and extensibility don't operate separately but are designed simultaneously within the same loop. ([WikiDocs](https://wikidocs.net/338204))
- In practice, it's more important to understand how a request flows through tools, permissions, and states rather than feature names.
- A takeaway for meetings: **"Claude Code's competitiveness lies not in the model itself, but in the execution architecture that makes the model work safely."**

## References

- WikiDocs, "Appendix 91. Claude Code Source Code Analysis" ([WikiDocs](https://wikidocs.net/338204))
- Anthropic, Claude Code Official Introduction and Interface Example Screens
