---
title: "MemPalace: Why Did Local AI Memory Hit 40,000 Stars with R@5 96.6%?"
date: 2026-04-17T02:47:49+09:00
slug: "1060-MemPalace-R-5-96-6-로컬-AI-메모리가-왜-별-4만-개를-모았을까"
original_url: "https://memoryhub.tistory.com/1060"
tistory_id: 1060
draft: false
---

```
   ┌───────────────────────────────────────┐
   │             MemPalace v3.3            │
   │   ┌─────────┐  ┌─────────┐  ┌──────┐  │
   │   │  Wing   │  │  Wing   │  │ Wing │  │
   │   │ project │  │ person  │  │ team │  │
   │   └────┬────┘  └────┬────┘  └──┬───┘  │
   │        │            │           │      │
   │     [Room]       [Room]      [Room]   │
   │        │            │           │      │
   │    [Drawer]     [Drawer]    [Drawer]  │
   │      source     source      source    │
   │                                        │
   │   local-first · verbatim · MCP-ready   │
   │        R@5 96.6%  (no API key)         │
   └───────────────────────────────────────┘
```

## Intro

If you've been using Claude or ChatGPT for a while, you hit this wall: "What did I say last week again?" or "How did I set up that project?" You find yourself pasting the same context over and over. I thought a few summaries would solve it, but every time I needed something specific, the answer was "that detail didn't make it into the summary."

By the end of this article, you'll take home a way to attach an open-source AI memory system to your laptop in 5 minutes—one that runs locally and free, has 96.6% search recall without an API key.

## One-Line Summary

MemPalace is an open-source memory system that stores conversations **verbatim in local storage**, narrows search scope across **Wings, Rooms, and Drawers (three tiers)**, and plugs into Claude Code, Cursor, and ChatGPT through **29 MCP server tools**.

## Why This Project Is Hot Right Now

As AI agents grew more complex, "long-term memory" became essential to stash outside the session.

Most existing solutions rely on summaries (losing detail) or require uploading full conversations to cloud APIs.

MemPalace was built to sidestep both:

| Existing Memory System Gap | MemPalace's Choice |
| --- | --- |
| Summaries/extraction lose source | Store verbatim (word-for-word) |
| Cloud API dependency | Local-first; embedding and search all on your machine |
| Flat single-corpus search | Wings → Rooms → Drawers three-tier scoping |
| Inconsistent benchmarking | Public reproducible LongMemEval, LoCoMo, ConvoMem, MemBench |

The official repository is `github.com/MemPalace/mempalace` only. Domain imitations like `mempalace.tech` are explicitly flagged as impersonation in the README—always verify the URL before installing.

## Core Idea

> MemPalace stores full conversation text in drawers (smallest unit) and retrieves it via semantic search. No summarization, no cloud upload—just "divide by space, search narrow."

Structure is simple: Wings are top-level containers (person or project), Rooms are topic folders, and Drawers are the unit where raw text lives.

The base vector backend is ChromaDB; swap it by matching the backend interface (`mempalace/backends/base.py`).

Benchmarks need interpretation across three tiers. Language and version: **Python 3.9+ / MemPalace v3.3.0 (released 2026-04-14)**:

```python
# Python 3.9+ / mempalace 3.3.0
from mempalace import Palace

palace = Palace.open("~/projects/myapp")
palace.search("Why did we switch to GraphQL again?")
# Returns drawer source + Wing/Room path
```

## Hands-On

### ① Installation

```bash
# Python 3.9+, ~300MB (base embedding model)
pip install mempalace
mempalace init ~/projects/myapp
```

Right after setup, `~/projects/myapp/.mempalace/` contains Wing scaffolding and a SQLite-backed knowledge graph. The CLI prints initialized Wing names and ChromaDB collection paths.

### ② Mine Conversations and Projects

```bash
# Put project files into drawers
mempalace mine ~/projects/myapp

# Export conversations (JSON, Markdown, etc.) into drawers
mempalace mine ~/chats/ --mode convos
```

`mine` splits raw text into drawers as-is and auto-classifies into Rooms and Wings. No summarizing, no paraphrasing.

### ③ Search and Wake Up Sessions

```bash
mempalace search "Why did we switch to GraphQL?"
mempalace wake-up   # On new session start, surfaces related context
```

Results include drawer source + Wing/Room path + similarity score.

The recent-access Room list appears on the right for quick context-switching.

### ④ Connect to Claude Code via MCP

```bash
mempalace mcp   # Start local MCP server (stdio)
```

Register this command in Claude Code's MCP config and restart. You'll see 29 MCP tools exposed (palace read/write, knowledge graph, cross-wing search, drawer management, agent diary)—all local, no external calls.

## Reference Patterns

| Pattern | Pros | Notes |
| --- | --- | --- |
| Verbatim storage (MemPalace default) | No detail loss, great for later re-queries | Disk usage grows; filter sensitive data upfront |
| Summaries | Saves space, quick context injection | Loses detail, re-summary accumulates omissions |
| Cloud memory SaaS | Easy setup, sync across devices | API keys cost money; full chats sent outside |
| Single flat vector DB | Simple structure, easy to build | Hard to constrain search scope, bad at person/project boundaries |
| Wings/Rooms/Drawers scoping | Naturally narrows search, easy per-wing deletion | Takes initial learning, mining flow understanding needed |

Benchmarks per official README: **LongMemEval R@5 Raw 96.6% / Hybrid v4 held-out 98.4% / Rerank ≥99%**, LoCoMo Hybrid v5 R@10 88.9%, ConvoMem average 92.9%, MemBench R@5 80.3%. Authors note that "100%" is close to test memorization, so real operations expect Raw 96.6% or held-out 98.4%.

## Closing Thoughts

MemPalace is built on three principles: "no summaries, no cloud exports, divide by space." Install with `pip install` on Python 3.9+, plug in one MCP line, and test it in your workflow today. Just remember: the official site is `mempalaceofficial.com` and the repo is `github.com/MemPalace/mempalace`—anything else is impersonation.

## References

- MemPalace Official GitHub Repository (v3.3.0, 2026-04-14) — <https://github.com/MemPalace/mempalace>
- MemPalace Official Docs Site — <https://mempalaceofficial.com>
- PyPI Package Page — <https://pypi.org/project/mempalace/>
- Benchmark Methodology (BENCHMARKS.md) — <https://github.com/MemPalace/mempalace/blob/main/benchmarks/BENCHMARKS.md>
- Release Notes (CHANGELOG) — <https://github.com/MemPalace/mempalace/blob/main/CHANGELOG.md>
- Domain Impersonation Warning & History (docs/HISTORY.md) — <https://github.com/MemPalace/mempalace/blob/main/docs/HISTORY.md>
