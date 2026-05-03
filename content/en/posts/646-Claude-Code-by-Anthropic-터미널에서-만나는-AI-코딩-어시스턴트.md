---
title: "Claude Code by Anthropic - AI Coding Assistant in the Terminal 💻"
date: 2025-06-04T17:59:43+09:00
slug: "646-Claude-Code-by-Anthropic-터미널에서-만나는-AI-코딩-어시스턴트"
original_url: "https://memoryhub.tistory.com/646"
tistory_id: 646
draft: false
categories: ["Dev Language"]
tags: ["Vibe Coding"]
cover:
  image: "/images/646-Claude-Code-by-Anthropic-터미널에서-만나는-AI-코딩-어시스턴트/img.png"
  relative: false
  hidden: false
---

![](/images/646-Claude-Code-by-Anthropic-터미널에서-만나는-AI-코딩-어시스턴트/img.png)

Have you ever been coding and thought "Wait, what does this function do again?" while digging through files? Or have you had a GitHub issue open with your terminal, IDE, and browser window simultaneously? Today, let's explore Claude Code by Anthropic, a tool that solves all these concerns at once!

## Background

In the past, developers had to manually handle everything when writing code. File searching, debugging, refactoring, documentation... all tasks went through the developer's hands. Then AI coding assistants like GitHub Copilot started to change this gradually.

However, existing tools mainly worked only within IDEs or remained at simple code autocomplete levels. Developers still had to switch between multiple tools, and it was difficult to automate complex workflows.

That's why Anthropic tried a completely new approach. They created Claude Code with the concept of "an AI agent running directly in the terminal!" This tool, officially launched on May 22, 2025, is fundamentally changing how developers work.

**Problems Claude Code solves:**

1. **Context switching problem**: Eliminates the hassle of switching between terminal, IDE, and browser
2. **Large codebase exploration**: Can understand and analyze millions of lines of code instantly
3. **Repetitive task automation**: Handles test execution, commits, PR creation, and more through natural language commands

## Core Principles

The way Claude Code works can be visualized as follows:

```
┌─────────────────────────────────────────────────┐
│            Developer's Terminal                 │
│                                                 │
│  $ claude "Refactor this function for me"      │
│       ↓                                         │
│  ┌─────────────┐                               │
│  │ Claude Code │ ←→ [Local File System]        │
│  └─────────────┘                               │
│       ↓                                         │
│  ┌─────────────────────────────┐               │
│  │  Claude Opus 4 Model (API)  │               │
│  └─────────────────────────────┘               │
│       ↓                                         │
│  [Analyze Code → Plan → Execute]               │
│       ↓                                         │
│  ✅ Task Complete!                             │
└─────────────────────────────────────────────────┘
```

### Key Feature Comparison

| Feature | Traditional Tools (Cursor, Copilot) | Claude Code |
|---|---|---|
| Execution Environment | Within IDE | Direct terminal execution |
| Codebase Understanding | Limited (open files only) | Automatic full project mapping |
| Task Automation | Code generation focused | Full workflow (Git, tests, build, etc.) |
| Extensibility | IDE plugin dependent | Infinite extensibility through MCP servers |
| Background Execution | Not possible | Possible with GitHub Actions integration |

### Practical Usage Examples

```
# Installation
npm install -g @anthropic/claude-code

# Navigate to project directory
cd my-project

# Start Claude Code
claude

# Command with natural language
> "Analyze the README.md file and explain the project structure"
> "Fix all type errors in the auth module"
> "Solve this issue and create a PR: #1234"
> "Run tests and fix the failing ones"
```

## Important Notes and Tips 📝

⚠️ **Key Points to Remember!**

1. **Check file modification permissions**
   - Claude Code can directly modify files
   - Always backup with Git before critical work
   - Use the --no-auto-accept flag to prevent automatic modifications
2. **Monitor API usage**
   - Claude Code consumes API tokens
   - Be cautious of costs for large-scale work
   - Can save up to 90% costs with prompt caching

💡 **Pro Tips**

- Use the /clear command to frequently reset context
- Manage complex tasks efficiently with markdown checklists
- Save frequently used commands in .claude/commands folder
- Connect external tools like Puppeteer and Sentry using MCP servers

## Conclusion

We've explored Claude Code in detail. At first, you might think "Talk to AI in the terminal?" and feel unfamiliar, but once you try it, you'll be amazed at its power! Especially for developers with many repetitive tasks or those dealing with large codebases, this seems like a truly revolutionary tool.

Why not become 10x more productive with Claude Code? 🚀

## References 📚

- [Claude Code Official Documentation](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code GitHub Repository](https://github.com/anthropics/claude-code)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

---

#ClaudeCode #AICoding #TerminalTool #Anthropic #DeveloperTools
