---
title: "Codex Now Directly Controls Your PC: Codex App Update"
date: 2026-04-17T02:58:27+09:00
slug: "1061-Codex가-이제-내-PC를-직접-조작한다고-Codex-앱-업데이트"
original_url: "https://memoryhub.tistory.com/1061"
tistory_id: 1061
draft: false
---

![](/images/1061-Codex가-이제-내-PC를-직접-조작한다고-Codex-앱-업데이트/img.png)

How many times a day do you bounce between JIRA, Slack, code, and Notion? I watched this morning disappear switching between browser, terminal, and docs. But this Codex update came with a promise: "An agent that clicks windows, types, and works alongside you."

Read this to the end and you'll grasp what changed, where to pilot it first, and where the biggest wins are.

## One-Line Summary

OpenAI Codex added background computer use, in-app browser, gpt-image-1.5 image generation, 90+ plugins, and persistent memory—expanding from code writing to a partner for the entire software development lifecycle.

## Why This Update Is "Major"

OpenAI reports Codex's weekly active users exceed 3 million.

Over the past year, how developers use Codex evolved: from pure code generation to system understanding, context collection, review, debugging, and sustained long-work. This release formalizes that expansion at the tool level.

| What's New | Core Content |
| --- | --- |
| Background computer use | Codex gets its own cursor, sees/clicks/types in apps; you're free to work elsewhere while multiple agents run in parallel |
| In-app browser | Comment directly on web pages to give agents pixel-precise instructions; applies first to frontend and game dev |
| Image generation (gpt-image-2) | Generate product concepts, frontend mockups, game visuals in the same workflow as code and screenshots |
| 90+ new plugins | Atlassian Rovo (JIRA), CircleCI, CodeRabbit, GitLab Issues, Microsoft Suite, Neon by Databricks, Remotion, Render, Superpowers, etc. |
| SDLC support expanded | GitHub review comment handling, multi-terminal tabs, SSH remote devbox (alpha), sidebar file preview, summary panel |
| Long-term automation | Reuse existing threads; wake up at future times to continue work days/weeks later |
| Memory preview | Remember preferences, corrections, collected context to boost speed and quality next session |
| Proactive suggestions | Context from project, plugins, memory suggests "where to pick up next" with priority list |

## The Core

> This Codex update's essence: "Agents stepped out of the code editor window to directly work on computer and web, integrated team tools."
> Computer use, browser, image, plugins, memory, and scheduling converge in one workspace—Codex is no longer the "write" stage of SDLC; it's the full-cycle orchestrator.

## Hands-On—30 Minutes Before Clocking Out

### ① Frontend Iteration via Computer Use

Update macOS Codex desktop app to the latest and log in with ChatGPT account. Background computer use appears.

Example: Pull up a Figma mockup and say "Implement this screen as a Next.js page and verify it works in a real browser." The agent uses its own cursor to bounce between editor and browser. Your other apps stay untouched.

### ② Precise UI Fixes via In-App Browser

Open your dev server in Codex's in-app browser and comment directly on buttons and forms: "Pad this area to 16px, fix layout break on mobile at 320px."

Coordinates and element context travel with the directive—no more screenshot paste marathons. The difference is biggest for game UIs and complex dashboards where visual density matters.

### ③ Prepare "Tomorrow's You" with Automation and Memory

Long-term automation: "Wake up Friday at 5 PM, apply PR comments, land to merge queue."

Memory preview learns your repeated corrections (e.g., "We don't use barrel files, each import stands alone") so agents remember style conventions.

Sidebar shows agent plan, reference sources, and outputs in a timeline view.

For quick CLI checks (Node.js 20+, `openai/codex` basis):

```bash
npm install -g @openai/codex
codex login
codex plugins list        # See 90+ installable plugins
codex --help              # Check automation and memory flags
```

## Competitive Pattern Comparison

| Pattern | Pros | Notes |
| --- | --- | --- |
| OpenAI Codex (this update) | Computer use, in-app browser, image generation, 90+ plugins, long memory in single app; covers full SDLC | Desktop app focus; lower IDE friendliness. Computer use and personalization roll out gradually EU/UK first |
| GitHub Copilot | Mature IDE autocomplete and chat, strong enterprise adoption, audit logs | Multi-app orchestration, long-duration tasks, auto-manipulation of external tools lag Codex |
| Claude Code (Anthropic) | Terminal, SDK, flexible MCP ecosystem; strong long-context and sub-agent design freedom | Native computer use UX, desktop app-based visual workflows come later than Codex |

## Closing Thoughts

The insight isn't "the model got smarter"—it's "the agent's seat moved."

When computer use, browser, plugins, and memory all converge in one workspace, Codex shifted from a code-editor tool to a partner touching JIRA, Slack, Notion, and CI.

Tomorrow, grab one repetitive task and hand it to Codex automation. You'll feel why this shift matters.

## References

- [OpenAI, Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/)
- [OpenAI, Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [OpenAI Developers, Codex Changelog](https://developers.openai.com/codex/changelog)
- [OpenAI Developers, Agent Skills](https://developers.openai.com/codex/skills)
- [OpenAI Developers, Subagents](https://developers.openai.com/codex/subagents)
- [GitHub, openai/codex](https://github.com/openai/codex)
