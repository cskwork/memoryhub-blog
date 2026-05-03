---
title: "Pencil.dev: Design in IDE and Deploy Straight to Code"
date: 2026-02-08T08:43:54+09:00
slug: "1014-Pencil-dev-IDE-안에서-디자인하고-바로-코드로-착지하는-법"
original_url: "https://memoryhub.tistory.com/1014"
tistory_id: 1014
draft: false
---

![](/images/1014-Pencil-dev-IDE-안에서-디자인하고-바로-코드로-착지하는-법/img.png)

What happens when a designer hands off a completed mockup from Figma to a developer? Style mismatches, asset extraction headaches, endless confirmation messages. According to McKinsey's 2024 software development efficiency research,

this "design handoff" process consumes 15-20% of a mid-sized team's entire project timeline.

Pencil.dev flips this problem on its head.

Instead of Figma, **design files live in the code repository, you design directly in the IDE, and AI agents read and write the canvas.**

**TLDR:** Bottom line: Pencil.dev is a next-generation development tool that eliminates design handoff entirely by integrating an MCP-based vector design canvas into the IDE.

## Background

In software development, "design-to-developer handoff" is an old bottleneck. Designers work in Figma, developers work in VS Code. There's always a "translation cost" between them.

> Design handoff is the process of delivering a designer's completed mockup to a developer in an interpretable form (specification documents, asset files, etc.).

The problems from this process aren't just inconvenient. A color value differs, spacing is off by 4px, and "that button wasn't meant to work this way" conversations repeat. The core issue is a **structural problem where design tools and dev tools exist in different worlds**.

Figma's design files live on Figma servers, code lives in Git repos.

With no official corridor connecting these worlds, humans had to manually "translate."

In September 2025, a tool directly targeting this structure emerged. Pencil.dev, created by Tom Krcha.

Krcha worked on Adobe XD development, created video conferencing tool Around (acquired by Miro), and co-founded Alter avatars (acquired by Google).

With 14+ years at the intersection of design and engineering, his answer was "let's put design files in the code repo."

Pencil.dev is currently in early access and **available for free**.

However, AI features require a Claude Code subscription (from $20/month).

Pencil itself is a UI engine, with actual AI generation performed by Anthropic's models.

## Pencil.dev Core Concepts

Understanding Pencil.dev requires knowing three axes.

**First: the .pen file format.** Pencil's design files have .pen extension. Internally it's JSON-based text data. This means a lot. Because it's text, version control via Git is possible. Since it goes into the same repo as code, rolling back code also rolls back design. If you've experienced hunting through "Version History" in Figma asking "what was that version?", you can feel how significant a difference this is.

**Second: MCP (Model Context Protocol) integration.** MCP is a protocol for AI agents to communicate with external tools in a standardized way. Think of it as a "lingua franca" between AI and design canvas. Through MCP, Pencil grants AI not just **read access but write access** to the canvas. Meaning Claude Code or Cursor AI agents can directly position elements on the canvas, modify styles, and create components.

**Third: bidirectional workflow.** It's not just Design → Code. Code → Design also works. Visually recreate components from existing codebases on the canvas, or have design tokens modified on the canvas automatically reflected as CSS variables.

When these three combine, you get a fundamentally different experience from existing workflows. The act of "opening a design tool" itself disappears, and UI is created as an extension of code writing.

## Hands-On: Getting Started with Pencil.dev

### ① Installation

Pencil.dev can be used three ways: standalone desktop app, Cursor extension, and VS Code extension. macOS supports all three, Windows currently supports extensions only. Linux supports both desktop app and extensions, though some UI issues are reported in Wayland environments.

If using Cursor, search for "Pencil" in the extensions menu to install. The Claude Code CLI that serves as the core engine must be installed on your system, and authentication must be completed via the `claude` command.

### ② Verify MCP Connection

This is the most important step after installation. If using Cursor, check Settings > Tools & MCP tab that `extension-pencil` is enabled. If using Claude Code directly, typing `/mcp` in the terminal should show `pencil ✔ connected`. This connection lets AI recognize and manipulate the canvas.

### ③ Create First Design File

Create a file with .pen extension in your project directory.

```
mkdir my-app && cd my-app
touch design.pen
```

Opening this file in your IDE displays an infinite canvas. You can draw vector elements directly here or give the AI natural language instructions.

For example, prompting "create a Get Started button with white text on a blue gradient background" immediately reflects on the canvas.

### ④ Import Figma Assets

If you have existing Figma designs, no need to redraw from scratch. Copy elements from Figma (Ctrl+C) and paste into the Pencil canvas (Ctrl+V)—vectors, text, and styles all preserve. Useful when porting brand kits or component libraries.

### ⑤ Generate Code from Design

Select a frame on the canvas and instruct the AI "generate a React component from this design" or "export as a Next.js page component"—code is generated in the same project directory. Generated code is immediately executable.

Looking at actual user feedback, complex 3-column responsive layouts sometimes have 4-8px alignment errors.

When you fine-tune positioning directly on the canvas, changes sync back to code. This **bidirectional synchronization** is Pencil's core value.

## Comparison with Existing Tools

| Item | Figma + Manual Handoff | Pencil.dev |
| --- | --- | --- |
| Design Environment | Separate browser app | IDE-embedded canvas |
| Version Control | Figma's own history | Git (integrated with code) |
| AI Integration | Plugin dependent (Layermate etc) | MCP native (read+write) |
| Code Generation | Manual interpretation or separate tools | Generate directly from canvas |
| Collaboration | Designer-developer separated | Same repo, same tool |
| Manual editing quality | Figma advantage | Figma still ahead on fine-tuning |
| Price | Figma paid + dev tools | Pencil free (Claude Code subscription separate) |

To be honest about one thing: when it comes to "carefully hand-tuning UI with precision," Figma is still ahead according to most users at this point.

Pencil's strength isn't in meticulous manual work, but in the **speed of collaborating with AI agents, rapidly prototyping, and converting to code immediately**.

## What Teams Benefit Most

Scenarios where Pencil.dev delivers the most value are clear.

Projects needing fast UI iteration focused on frontend, like landing pages or SaaS dashboard prototypes.

Teams already using Claude Code or Cursor as primary dev tools will find it naturally integrates into existing workflows.

Conversely, backend-focused projects where complex state management, API integration, and database logic are central have limited direct utility.

Also, being in early access stage currently, when designing long-term dependent structures, consider potential pricing policy changes.

As a startup backed by Andreessen Horowitz (a16z), the current free model is likely a user acquisition strategy.

## Closing Thoughts

- Pencil.dev removes the structural bottleneck of design handoff by putting .pen files in Git repos and connecting to AI agents via MCP.
- Eliminates the act of "opening design tools separately" and creates a workflow where design and code synchronize bidirectionally within the IDE.
- Real-world tip: Install the Pencil extension in Cursor or VS Code, add one `design.pen` file to a project in progress. Just copy-pasting existing Figma mockups lets you feel the workflow difference.

## References

- Pencil Official Documentation (<https://docs.pencil.dev/>)
- <https://www.youtube.com/watch?v=7IRFzZyrKOE>
- Pencil.dev Official Site (<https://www.pencil.dev/>)
- Pencil.dev: Bridging the Design-to-Code Gap in Modern Development - Medium (<https://medium.com/@tentenco/pencil-dev-bridging-the-design-to-code-gap-in-modern-development-fede236fa551>)
- Pencil.dev the Missing Link Between Design and Vibe Coding? - Abduzeedo (<https://abduzeedo.com/pencildev-missing-link-between-design-and-vibe-coding>)
- Pencil.dev Review: Features, Pricing, Alternatives - Banani (<https://www.banani.co/blog/pencil-dev-review>)
- Speedrun by a16z - Pencil.dev (<https://speedrun.a16z.com/companies/pencildev>)
