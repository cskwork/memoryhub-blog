---
title: "Open Code vs Claude Code, Complete Comparison of Terminal AI Coding Agents"
date: 2026-01-17T15:19:33+09:00
slug: "976-Open-Code-vs-Claude-Code-터미널-AI-코딩-에이전트-완전-비교"
original_url: "https://memoryhub.tistory.com/976"
tistory_id: 976
draft: false
---

```
   ___                     ____          _      
  / _ \ _ __   ___ _ __   / ___|___   __| | ___ 
 | | | | '_ \ / _ \ '_ \ | |   / _ \ / _` |/ _ \
 | |_| | |_) |  __/ | | || |__| (_) | (_| |  __/
  \___/| .__/ \___|_| |_| \____\___/ \__,_|\___|
       |_|                    vs                
   ____ _                 _        ____          _      
  / ___| | __ _ _   _  __| | ___  / ___|___   __| | ___ 
 | |   | |/ _` | | | |/ _` |/ _ \| |   / _ \ / _` |/ _ \
 | |___| | (_| | |_| | (_| |  __/| |__| (_) | (_| |  __/
  \____|_|\__,_|\__,_|\__,_|\___| \____\___/ \__,_|\___|

           Terminal AI Coding Agent Comparison
```

When you hear "Claude Code is the best!" you reflexively nod in agreement.

But when asked if you've actually tried Open Code, most people shake their heads.

Both tools support MCP, Skills, and Subagents, but their implementation philosophies are completely different.

**Real expertise isn't about which tool is "better," but understanding what works for which situation.**

**One-line summary:** In short, Claude Code's strength is its integrated experience within the Anthropic ecosystem and polish, while Open Code's strength is freedom in model selection and open-source extensibility.

## Background

The terminal-based AI coding agent market is experiencing explosive growth. As MCP (Model Context Protocol) became the standard in 2024, we've entered the era of "agentic coding" that goes beyond simple code autocompletion to enable file system manipulation,

external API integration, and even browser automation.

> Terminal AI coding agent: A tool where you give natural language commands in the terminal, and AI writes code, executes it, and modifies files. It's more like an "AI colleague" doing actual development work rather than simple autocompletion.

The two tools in question are Open Code, made by the SST (Serverless Stack) team, and Claude Code by Anthropic. Interestingly, Open Code fully supports Claude Code's configuration file format (CLAUDE.md, .mcp.json).

They're developing into complementary rather than competing relationships.

There are four key comparison areas:

- **Settings**: Configuration system and customization
- **MCP**: External tool integration approach
- **Skills**: Reusable knowledge packages
- **Subagents**: Parallel tasks and context separation

## Settings Comparison

The configuration system reveals a tool's philosophy. Claude Code uses a hierarchical settings system designed for enterprise environments,

while Open Code pursues simplicity with a single JSON file approach.

### Claude Code Settings System

Claude Code has a 5-tier setting priority where upper settings override lower ones.

1. **Enterprise Managed Settings**: Central control by organization administrator
2. **Command Line Flags**: Specified at runtime with `--allowedTools` etc.
3. **Local Settings** (`.claude/settings.json`): Per-project settings
4. **Project Settings**: Settings for team sharing
5. **User Settings** (`~/.claude.json`): Personal global settings

Key configuration example:

```
{
  "permissions": {
    "allow": ["Read", "Write", "Bash(npm run test:*)"],
    "deny": ["WebFetch", "Bash(curl:*)"]
  },
  "env": {
    "ANTHROPIC_MODEL": "claude-sonnet-4-5-20250929"
  }
}
```

Project context is defined in the `CLAUDE.md` file. It can be auto-generated with the `/init` command and contains project architecture, coding conventions, build commands, etc.

### Open Code Settings System

Open Code centers around a single `opencode.json` file. It supports both global (`~/.config/opencode/opencode.json`) and per-project settings.

```
{
  "provider": "anthropic",
  "model": "claude-sonnet-4-5-20250929",
  "theme": "dark",
  "agent": {
    "build": { "tools": ["bash", "read", "write", "edit"] },
    "plan": { "tools": ["read", "grep", "glob"] }
  }
}
```

Claude Code compatibility mode is enabled by default, so you can use `CLAUDE.md` and `.mcp.json` as-is. If both `AGENTS.md` and `CLAUDE.md` exist, `AGENTS.md` takes priority.

### Settings Comparison Summary

| Item | Claude Code | Open Code |
| --- | --- | --- |
| Config Files | `~/.claude.json`, `.claude/settings.json` | `opencode.json` |
| Project Context | `CLAUDE.md` | `AGENTS.md` (CLAUDE.md compatible) |
| Setting Tiers | 5-tier (Enterprise → User) | 3-tier (Remote → Global → Project) |
| Model Selection | Anthropic models only | Multi-provider (OpenAI, Gemini, Bedrock, etc.) |
| Theme/UI Customization | Limited | Detailed TUI configuration possible |

## MCP (Model Context Protocol) Comparison

MCP is a standard protocol for AI agents to communicate with external tools. Both tools support MCP, but differ in how they manage it.

### Claude Code's MCP Management

Claude Code manages MCP servers in 3-tier scopes.

- **Local Scope**: For personal experimentation, sensitive credentials
- **Project Scope**: Team sharing, defined in `.mcp.json`
- **User Scope**: Personally used across all projects

```
# Add HTTP server (recommended)
claude mcp add --transport http notion https://mcp.notion.com/mcp

# Specify scope
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic

# Include Bearer token
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

A distinguishing feature is **Tool Search**. When MCP tools exceed 10% of context, it automatically switches to dynamic loading mode.

Supported on Sonnet 4 and above.

### Open Code's MCP Management

Open Code also manages MCP in the `mcp` section of `opencode.json`.

```
{
  "mcp": {
    "gh_grep": {
      "type": "remote",
      "url": "https://grep.dev/api/search",
      "headers": { "Authorization": "Bearer ${GH_GREP_TOKEN}" }
    },
    "local_server": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"],
      "env": ["HOME"]
    }
  }
}
```

It supports environment variable expansion (`${VAR}`) so you don't need to put sensitive values directly in code.

Organizations can also deploy default MCP servers via `.well-known/opencode` endpoint.

### MCP Comparison Summary

| Item | Claude Code | Open Code |
| --- | --- | --- |
| Config File | `.mcp.json`, CLI | `opencode.json` mcp section |
| Scope | 3-tier (Local/Project/User) | 2-tier (Global/Project) |
| Transport | HTTP (recommended), SSE (legacy), STDIO | Remote (HTTP), Local (STDIO) |
| Dynamic Loading | Tool Search auto-enabled | Manual management |
| Permission Control | `mcp__server__*` wildcard | `permission` field |

## Skills Comparison

Skills are reusable knowledge packages. Claude Code has formalized and significantly advanced this concept as "Agent Skills."

### Claude Code's Agent Skills

Agent Skills, officially announced in October 2025, follow the **Progressive Disclosure** principle.

Content isn't loaded all at once, only relevant sections when needed.

```
my-skill/
├── SKILL.md          # Main instruction (required)
├── scripts/          # Executable scripts
│   └── helper.py
└── references/       # Reference documents
    └── schema.md
```

SKILL.md structure:

```
---
name: pdf-processing
description: Extract text from PDF files, fill forms, merge documents. Use for PDF, form, and document extraction tasks.
allowed-tools: Read, Bash(python:*)
---

# PDF Processing

## Quick Start
Text extraction:
```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For form filling, see <FORMS.md>.

```
Skill discovery process:
1. At startup, only `name` and `description` of all skills are loaded into system prompt
2. When user request matches skill description, activation confirmed
3. After approval, full `SKILL.md` content added to context
4. Only required reference files and scripts are additionally loaded

### Open Code's Skills

Open Code supports Claude Code's Skills format. Place in `~/.config/opencode/skills/` or `.opencode/skills/`.

```yaml
---
name: my-skill
description: Skill description
---

# Detailed instructions
Claude references this content when skill is activated.
```

**Superpowers plugin** provides a richer skill system.

With `find_skills` and `use_skills` tools, dynamically load Anthropic-compatible skills.

### Skills vs Other Concepts

| Feature | Skills | Subagents | CLAUDE.md/AGENTS.md |
| --- | --- | --- | --- |
| Purpose | Provide domain knowledge | Perform parallel tasks | Project context |
| Context | Added to current conversation | Separate context | Always loaded |
| Activation | Automatic (description matching) | Explicit call | Automatic |
| Code Execution | Possible | Possible | Not possible |

## Subagents Comparison

Subagents are independent AI instances with separate context. Useful for preventing context pollution and parallel tasks.

### Claude Code's Subagents

Claude Code provides three built-in subagents.

- **Explore**: Code exploration only, auto-called in Plan mode
- **Task**: General-purpose task delegation
- **Custom**: User-defined subagents

```
# .claude/agents/reviewer.md
---
name: reviewer
description: Code review only
model: sonnet
color: orange
---

You are a professional code reviewer.
Focus on security, performance, and maintainability.
```

Subagent characteristics:

- Same tool access permissions as parent
- Context isolation (no direct information sharing between subagents)
- Each subagent's usage counted separately
- Run in background with `Ctrl+B`

### Open Code's Subagents

Open Code distinguishes between **Primary Agent** and **Subagent**.

Primary Agents (switch with Tab):

- **Build**: All tools enabled, for development tasks
- **Plan**: Read-only, for analysis and planning

Subagents (called with @ mention):

- **General**: Complex searches, multi-step tasks
- **Explore**: Codebase exploration

```
{
  "agent": {
    "custom-reviewer": {
      "description": "Code review only",
      "model": "openai/gpt-5.1",
      "temperature": 0.3,
      "tools": ["read", "grep", "glob"]
    }
  }
}
```

Can also be defined as markdown file:

```
<!-- ~/.config/opencode/agent/reviewer.md -->
---
description: Code review only
model: anthropic/claude-sonnet-4-5
temperature: 0.3
---

Perform code review focusing on security, performance, and maintainability.
```

### Subagents Comparison Summary

| Item | Claude Code | Open Code |
| --- | --- | --- |
| Built-in Agents | Explore, Task | Build, Plan, General, Explore |
| Custom Definition | `.claude/agents/*.md` | `agent/` folder or JSON |
| Invocation | Automatic or explicit | Tab (Primary), @ (Subagent) |
| Model Selection | Limited | Different model per agent possible |
| Background | Ctrl+B supported | Not supported |

## Practical Guide: Project Configuration Example

### Step 1: Project Initialization

**Claude Code**:

```
cd my-project
claude
/init  # Auto-generates CLAUDE.md
```

**Open Code**:

```
cd my-project
opencode
/init  # Auto-generates AGENTS.md
```

### Step 2: Add MCP Server

**Claude Code**:

```
claude mcp add --transport http github https://api.github.com/mcp
```

**Open Code** (edit `opencode.json`):

```
{
  "mcp": {
    "github": {
      "type": "remote",
      "url": "https://api.github.com/mcp"
    }
  }
}
```

### Step 3: Create Custom Command

Both tools define slash commands via markdown files.

**Claude Code** (`.claude/commands/review.md`):

```
---
description: Perform PR code review
---

Perform code review for $ARGUMENTS.
1. Check for security vulnerabilities
2. Inspect performance issues
3. Review test coverage
```

**Open Code** (`.opencode/command/review.md`):

```
---
description: Perform PR code review
---

Perform code review for $ARGUMENTS.
1. Check for security vulnerabilities
2. Inspect performance issues
3. Review test coverage
```

Usage: `/review PR #123`

## Best Practices/Pattern Comparison

| Use Case | Claude Code | Open Code |
| --- | --- | --- |
| Anthropic models only | Optimal (native integration) | Compatible |
| Multi-model (GPT + Claude + Gemini) | Not possible | Optimal (free provider choice) |
| Enterprise deployment | Optimal (Managed Settings) | Limited |
| Open source contribution | Not possible (closed source) | Optimal (MIT license) |
| Leverage existing Claude Code config | Native | Compatible mode supported |
| TUI customization | Limited | Detailed configuration possible |
| Skills ecosystem | Rich (official skills) | Compatible + plugin extensibility |

## Conclusion

- Claude Code provides an integrated experience optimized for the Anthropic ecosystem. Enterprise management features, official Skills library, and advanced features like Tool Search are its strengths.
- Open Code's strengths are freedom in model selection and open-source extensibility. You can use GPT-5 or Gemini while keeping Claude Code settings as-is.
- Practical tip: If you're currently using Claude Code, keep your configuration files and install Open Code too. Since `CLAUDE.md` and `.mcp.json` are compatible, you can use both tools in parallel without switching costs.

## References

- Claude Code Official Documentation (<https://docs.anthropic.com/en/docs/claude-code>)
- Open Code Official Documentation (<https://opencode.ai/docs>)
- Agent Skills Introduction - Anthropic Engineering (<https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>)
- Open Code GitHub (<https://github.com/opencode-ai/opencode>)
- MCP Protocol Specification (<https://modelcontextprotocol.io>)
