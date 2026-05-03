---
title: "CI LAW - Claude Code (Agentic Coding)"
date: 2025-08-26T22:01:35+09:00
slug: "760-CI-LAW-Claude-Code-Agentic-Coding"
original_url: "https://memoryhub.tistory.com/760"
tistory_id: 760
draft: false
categories: ["Life"]
tags: ["CI Laws"]
---

|  |  |  |  |
| --- | --- | --- | --- |
| **1** | **The Context Law** | Create and maintain CLAUDE.md files to provide Claude with essential project context, commands, and guidelines automatically | **Critical** - Foundation for all other  practices |
| **2** | **The Specificity Law** | Be explicit and detailed in instructions rather than vague - "add tests for foo.py" vs "write test case for foo.py covering logged-out user edge case" | **High** - Dramatically improves first-attempt success rates |
| **3** | **The Plan-Before-Code Law** | Always have Claude explore and plan before implementing - use "think" keywords to trigger extended reasoning | **High** - Prevents jumping to suboptimal solutions |
| **4** | **The Iteration Law** | Design workflows around clear targets (tests, visual mocks, screenshots) that Claude can iterate against until success | **High** - Enables continuous  improvement cycles |
| **5** | **The Course Correction Law** | Actively guide Claude using escape to interrupt, prompt editing, and early feedback rather than passive supervision | **Medium-High** - Prevents wasted  effort on wrong directions |
| **6** | **The Context Window  Law** | Use /clear frequently between tasks to prevent context pollution and maintain focus on current objectives | **Medium-High** - Maintains performance in long sessions |
| **7** | **The Multimodal Law** | Leverage images, screenshots, file paths, and URLs as inputs - Claude excels with visual and diverse data types | **Medium** - Expands problem- solving capabilities significantly |
| **8** | **The Permission  Management Law** | Curate allowed tools thoughtfully - balance safety with workflow efficiency through strategic permission grants | **Medium** - Enables smooth  automation while maintaining security |
| **9** | **The Multi-Agent Law** | Use multiple Claude instances in parallel for complex workflows - separate verification, testing, and implementation | **Medium** - Unlocks advanced  collaborative patterns |
| **10** | **The Automation Law** | Leverage headless mode (claude -p) for CI/CD, issue triage, and infrastructure tasks with structured JSON output | **Low-Medium** - Scales human-AI  collaboration beyond interactive  sessions |

### **Key Workflow Patterns Hierarchy:**

- **Basic**: Explore → Plan → Code → Commit
- **Advanced**: Write Tests → Code → Iterate → Commit
- **Expert**: Visual Mock → Code → Screenshot → Iterate

### **Essential Tools Integration:**

- **CLAUDE.md** for persistent context
- **Custom slash commands** for repeated workflows
- **MCP servers** for extended capabilities
- **Git/GitHub integration** for version control automation

---

**Bottom Line:** Master context management and specificity first—these two laws alone will transform your Claude Code effectiveness more than any other optimization.

<https://www.anthropic.com/engineering/claude-code-best-practices>

[Claude Code Best Practices

A blog post covering tips and tricks that have proven effective for using Claude Code across various codebases, languages, and environments.

www.anthropic.com](https://www.anthropic.com/engineering/claude-code-best-practices)
