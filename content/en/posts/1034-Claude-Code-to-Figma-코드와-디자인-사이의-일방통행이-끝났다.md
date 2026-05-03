---
title: "Claude Code to Figma: One-Way Street Between Code and Design Is Over"
date: 2026-02-18T10:45:43+09:00
slug: "1034-Claude-Code-to-Figma-코드와-디자인-사이의-일방통행이-끝났다"
original_url: "https://memoryhub.tistory.com/1034"
tistory_id: 1034
draft: false
cover:
  image: "images/1034-Claude-Code-to-Figma-%EC%BD%94%EB%93%9C%EC%99%80-%EB%94%94%EC%9E%90%EC%9D%B8-%EC%82%AC%EC%9D%B4%EC%9D%98-%EC%9D%BC%EB%B0%A9%ED%86%B5%ED%96%89%EC%9D%B4-%EB%81%9D%EB%82%AC%EB%8B%A4/img.png"
  relative: false
  hidden: false
---

![](/images/1034-Claude-Code-to-Figma-%EC%BD%94%EB%93%9C%EC%99%80-%EB%94%94%EC%9E%90%EC%9D%B8-%EC%82%AC%EC%9D%B4%EC%9D%98-%EC%9D%BC%EB%B0%A9%ED%86%B5%ED%96%89%EC%9D%B4-%EB%81%9D%EB%82%AC%EB%8B%A4/img.png)

Anyone can now build UI with AI. Throw one prompt at Claude Code—"make a dashboard"—and a working interface appears in minutes. But what comes next is the problem. How can you refine it with teammates, compare options, and make decisions together?

Taking screenshots and posting to Slack was the best you could do.

**Figma and Anthropic officially announced "Code to Canvas," solving this problem on February 17, 2026.**

**One-liner summary:** In short, UI built with Claude Code can now be imported directly as an editable design frame into Figma canvas,

and conversely, Figma designs can be implemented as code in Claude Code, opening a bidirectional workflow.

---

## Background

Until now, the flow between design and development was one-directional. Designers create mockups in Figma, developers see them and translate to code. Intent gets lost, and "this doesn't match the design" conversations repeat.

AI coding tools introduced a new variable to this flow.

Tools like Claude Code, Cursor, and Windsurf let developers create working UIs with just prompts.

The problem is results live trapped in the developer's local environment.

For teammates to see results, they must directly run builds, get screenshots, or watch screen recordings.

> Code to Canvas is a feature that transforms working UI created with AI coding tools into editable

> design frames on Figma canvas.

Born from the Figma-Anthropic partnership, "Code to Canvas" converts this one-way flow to bidirectional.

From code to canvas, from canvas to code. Here's why it matters using analogy:

Code work excels at **convergence**. Run builds, click paths, reach one state at a time.

Canvas work excels at **divergence**. Spread the whole experience at a glance, explore branches, collectively set direction.

When two worlds connect, teams narrow when needed and expand when required.

---

## What Code to Canvas Changes

### Editable Design Frames, Not Screenshots

The most critical difference. Capturing UI made with Claude Code transforms not into a flat image but an actual frame editable in Figma. Duplication, rearrangement, modification all work.

Designers, PMs, developers make decisions in identical context over identical output.

### Multi-Screen Capture for Entire Flow at a Glance

Capture multiple screens in one session. Spread entire flows from onboarding to payment to settings preserving order and context on canvas. It's much easier to identify patterns, gaps, and mismatches in complex multi-step flows.

### Explore Alternatives Without Code Changes

On canvas, duplicate frames, rearrange steps, experiment with structural changes.

No need to rewrite code to try ideas. Rejected ideas remain on canvas for later reference.

### Figma to Code Roundtrip

Code to Canvas's real power isn't one-way. Through Figma MCP server, Figma designs can be referenced in Claude Code prompts. Paste frame links and Claude Code understands design context and generates code.

**A workflow emerges where context flows seamlessly—code to design, design to code.**

---

## How It Works: MCP Is Key

Code to Canvas operates on MCP (Model Context Protocol) servers. MCP is an open standard enabling AI tools to interact with external data sources and applications. Think of it simply as a **universal adapter** connecting Claude Code and Figma.

The workflow:

① Create or modify UI with Claude Code. All browser-executed environments target it: local dev servers, staging, production.

② Capture screens. Integration retrieves live browser state, transforming it into Figma-compatible frames.

③ Paste into Figma. Captured screens become editable design frames on canvas.

④ Team collaborates. Comments, duplication, rearrangement, comparison happen directly on canvas.

---

## Practice: Setting Up Figma MCP Server

Figma MCP server works two ways: remote server (Figma-hosted) and local desktop server.

### Method 1: Remote MCP Server (Recommended)

Suited for browser-based Figma users. Works immediately without additional activation.

**1. Add Figma MCP to Claude Code**

```
claude mcp add --transport http figma-remote-mcp https://mcp.figma.com/mcp
```

For all projects, add `--scope user` flag:

```
claude mcp add --scope user --transport http figma-remote-mcp https://mcp.figma.com/mcp
```

**2. Restart Claude Code and Authenticate**

Enter `/mcp` in Claude Code, select `figma-remote-mcp`, proceed with Authenticate. Granting Figma account access completes connection.

**3. Verify Connection**

```
/mcp
```

When `figma-remote-mcp` status shows connected, setup is complete.

### Method 2: Desktop MCP Server

For Figma desktop app users.

**1. Enable MCP Server in Figma Desktop App**

Open latest Figma desktop app, toggle Dev Mode at bottom toolbar (Shift+D shortcut). In Inspect panel's MCP server section, click "Enable desktop MCP server." Server runs at `http://127.0.0.1:3845/mcp`.

**2. Connect Local Server to Claude Code**

```
claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp
```

**3. Start Prompting**

Select frame in Figma, then ask Claude Code "implement the selected design," or copy frame links and paste into Claude Code prompts.

### Claude Code Plugin Method (Alternative)

Install official Figma Claude Code plugin to configure remote/desktop MCP servers and Agent Skills at once.

```
claude plugin install figma@claude-plugins-official
```

---

## Existing Workflow vs Code to Canvas Comparison

| Item | Existing Workflow | Code to Canvas |
| --- | --- | --- |
| Sharing AI Results | Screenshots, screen recordings, local build execution | Direct Figma frame conversion |
| Editability | Designers must recreate from scratch | Immediately editable frames |
| Team Collaboration | Feedback requires dev environment access | Comments, comparison, discussion on Figma canvas |
| Alternative Exploration | Rebuild after code modification | Frame duplication without code changes |
| Bidirectionality | Design→Code unidirectional | Code→Design→Code roundtrip possible |
| Multi-screen | Individual screenshots per screen | Capture entire flow from one session |

---

## What This Partnership Means

"If AI makes code, don't designers become unnecessary?" naturally arises. Figma and Anthropic's answer is opposite: as AI coding tools advance, design collaboration becomes more important. That's this partnership's core premise.

AI making interfaces is no longer the question.

The real question is **whether teams have shared space to collectively evaluate and refine what AI made.**

Code to Canvas creates exactly that space.

However, potential risks exist. According to CNBC, if AI tools keep improving, teams might skip design refinement entirely. Figma may be building an on-ramp to a highway it no longer controls.

But currently, what differentiates products isn't feature presence but

**how the product feels, how it guides users, how clearly it conveys value.**

This space still requires human judgment and team collaboration.

---

## Conclusion

- Code to Canvas transforms UI built with AI coding tools into Figma canvas editable design frames, supporting bidirectional workflows via MCP servers.
- Code excels at convergence, canvas at divergence. Connecting both worlds creates new standards for design-development collaboration in the AI age.
- Practical tip: One line in the terminal—`claude mcp add --transport http figma-remote-mcp https://mcp.figma.com/mcp`—starts you today. Create screens with Claude Code, bring them to Figma, examine them with teammates.

---

## References

- From Claude Code to Figma: Turning Production Code into Editable Figma Designs (https://www.figma.com/blog/introducing-claude-code-to-figma/)
- Guide to the Figma MCP server (https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server)
- Figma MCP Remote Server Developer Docs (https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- Figma MCP Server Guide - GitHub (https://github.com/figma/mcp-server-guide)
- Claude Code MCP Connection Guide (https://code.claude.com/docs/en/mcp)
