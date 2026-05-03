---
title: "Why Claude Code Auto Memory Goes Beyond CLAUDE.md"
date: 2026-02-27T06:29:36+09:00
slug: "1044-Claude-Code-Auto-Memory-CLAUDE-md만으로는-부족한-이유"
original_url: "https://memoryhub.tistory.com/1044"
tistory_id: 1044
draft: false
---

```
  ╔══════════════════════════════════════════════╗
  ║                                              ║
  ║    ~/.claude/projects/my-app/memory/          ║
  ║    ├── MEMORY.md    ← Written by Claude      ║
  ║    ├── debugging.md                          ║
  ║    ├── api-conventions.md                    ║
  ║    └── ...                                   ║
  ║                                              ║
  ║    "When the session ends, memory persists"  ║
  ║                                              ║
  ╚══════════════════════════════════════════════╝
```

Imagine having to explain your project history from scratch to a colleague every morning at work. Using Claude Code, you've probably experienced something similar. Yesterday you clearly said "our project uses pnpm," but when you open a new session today, Claude tries npm install again. Can't you just write the rules in CLAUDE.md? That's a "manual instruction" you have to write yourself.

**Auto Memory is a system where Claude automatically writes learning notes while working and automatically loads them in the next session.**

**TL;DR:** Claude Code's Auto Memory is a separate system from CLAUDE.md that automatically records project patterns and learning insights as Claude works. Understanding and managing this system significantly improves context retention across sessions.

---

## Background

LLMs are inherently stateless systems. Once a session ends, all information in the context window disappears.

Most Claude Code users have solved this problem with CLAUDE.md files.

By placing a markdown file in the project root, it automatically loads at the start of each session.

However, there's a fundamental limitation here. CLAUDE.md can only contain what you already know. Debugging patterns you discover while working or hidden rules in the codebase must be manually recorded each time. Most developers forget to do this.

> Auto Memory is a persistent directory where Claude automatically records learning content, patterns, and insights discovered during work.

To solve this problem, Anthropic introduced the Auto Memory feature. It's enabled by default and has been fully applied since Claude Code version 2.1.32. If CLAUDE.md is "a manual instruction you write for Claude," then

Auto Memory is "a learning notebook Claude writes for itself."

---

## Core Differences: CLAUDE.md vs Auto Memory (MEMORY.md)

These are often confused. They have completely different roles.

| Aspect | CLAUDE.md | Auto Memory (MEMORY.md) |
| --- | --- | --- |
| Author | Written by developer | Written automatically by Claude |
| Storage Location | Project root or home directory | `~/.claude/projects/<project>/memory/` |
| Content | Coding rules, conventions, instructions | Project patterns, debugging insights, preferences |
| Loading Method | Entire content auto-loaded | Only first 200 lines of MEMORY.md auto-loaded |
| Version Control | Can be committed to Git | Recommended to add to .gitignore |
| Team Sharing | For team-wide sharing | Personal local use only |

To use an analogy, CLAUDE.md is like "team development guidelines" written in a company wiki, while

Auto Memory is like "things I discovered in this project" written in personal notes.

---

## How Auto Memory Works

### Directory Structure

Auto Memory creates an independent directory per project. The path is determined based on the Git repository root.

```
~/.claude/projects/<project>/memory/
├── MEMORY.md           # Core index (auto-loaded each session)
├── debugging.md        # Detailed debugging pattern notes
├── api-conventions.md  # API design decisions
└── ...
```

If there's no Git repository, the current working directory becomes the base. Subdirectories of the same repository share one Auto Memory directory. **Note that Git worktrees have separate memory directories.**

### The 200-Line Limit Rule

MEMORY.md has an important constraint. At the start of each session, **only the first 200 lines are injected into the system prompt.**

If it exceeds 200 lines, Claude shows this warning:

```
WARNING: MEMORY.md is N lines (limit: 200). 
Only the first 200 lines were loaded. 
Move detailed content into separate topic files 
and keep MEMORY.md as a concise index.
```

This design is intentional. MEMORY.md should be kept as a concise index, with detailed content separated into topic files.

Topic files (debugging.md, api-conventions.md, etc.) are not auto-loaded at startup.

Claude reads them on-demand using the file tool when that information is needed.

### What Claude Records

The information Claude automatically records in Auto Memory generally includes:

- Repeated commands used in the project (build, test, deploy scripts)
- Architecture patterns and design decisions in the codebase
- Problem-solving methods discovered during debugging
- User's preferred working methods and tools

When "writing memory" or "reading memory" appears during work,

Claude is updating or referencing Auto Memory.

---

## Hands-On Practice

### 1. Check Auto Memory Status

Run the `/memory` command in the Claude Code terminal.

All memory files (CLAUDE.md + Auto Memory) connected to the current project are displayed.

The Auto Memory toggle switch can also be checked on this screen.

If a memory directory already exists under `~/.claude/projects/`, Auto Memory is active.

### 2. Request Memory Directly from Claude

You can explicitly request saving using natural language.

```
"remember that we use pnpm, not npm"
"save to memory that the API tests require a local Redis instance"
"remember that this project always uses vitest"
```

Claude records this content in MEMORY.md and automatically references it in future sessions.

### 3. Edit MEMORY.md Directly

Auto Memory files are regular markdown, so they can be edited anytime. Open the file picker with `/memory` or

access the path directly.

```
# Check Auto Memory for current project
cat ~/.claude/projects/<project-path>/memory/MEMORY.md

# Clean up unnecessary items
code ~/.claude/projects/<project-path>/memory/MEMORY.md
```

### 4. Disable Auto Memory

You can disable it per-project or globally.

**Method 1: /memory Toggle**

Run `/memory` and turn off the auto-memory toggle.

**Method 2: settings.json**

```
// ~/.claude/settings.json
{
  "autoMemoryEnabled": false
}
```

**Method 3: Environment Variable (for CI/managed environments)**

```
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1  # Force disable
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=0  # Force enable
```

Environment variables have higher priority than `/memory` toggle and settings.json. This method is suitable for ensuring consistent behavior in CI pipelines or managed environments.

---

## Best Practices and Pattern Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Separate MEMORY.md as index with topic files | Overcome 200-line limit, systematic management | Topic files don't auto-load |
| Natural language "remember that..." saving | Save instantly without workflow interruption | Phrasing may vary since Claude decides what to save |
| Periodic MEMORY.md review/cleanup | Remove outdated info, save tokens | Requires manual review at least monthly |
| Use Auto Memory + CLAUDE.md together | Separate instructions from learning content | Risk of conflicting rules between the two |
| Disable via environment variable in CI | Maintain reproducible build environment | Recommend keeping enabled in development |

---

## Complete Memory Layer Architecture

Claude Code's memory system consists of 4 layers. In case of conflicts, more specific (lower) files have priority.

```
1. User Global     ~/.claude/CLAUDE.md           (Common across all projects)
2. Project         ./CLAUDE.md                   (Team-shared, Git committed)
3. Module Rules    .claude/rules/*.md            (Path-based conditional application)
4. Auto Memory     ~/.claude/projects/.../memory/ (Claude auto-recorded, personal)
```

Understanding this structure makes "where to put what" clear. Put your personal style that applies to all projects in the global file, team conventions in the project CLAUDE.md, directory-specific rules in module rules, and let Auto Memory handle the rest.

---

## Conclusion

- Claude Code's Auto Memory is a separate system from CLAUDE.md that automatically records patterns and insights Claude discovers while working.
- Only the first 200 lines of MEMORY.md auto-load, so the key is a concise index + topic file separation structure.
- Practical tip: Check your current project's Auto Memory status right now with `/memory`, and clean up any unnecessary items.

---

## References

- Manage Claude's memory - Claude Code Docs (<https://code.claude.com/docs/en/memory>)
- Memory tool - Claude API Docs (<https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool>)
- Claude Code's Experimental Memory System (<https://giuseppegurgone.com/claude-memory>)
- Claude Code Best Practices: Memory Management (<https://cuong.io/blog/2025/06/15-claude-code-best-practices-memory-management>)
