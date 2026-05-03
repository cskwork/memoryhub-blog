---
title: "oh-my-opencode Complete Guide: Evolving AI Coding Tools into a Team"
date: 2026-01-22T23:05:04+09:00
slug: "987-oh-my-opencode-완벽-가이드-AI-코딩-도구를-팀으로-진화시키는-방법"
original_url: "https://memoryhub.tistory.com/987"
tistory_id: 987
draft: false
---

```
    ┌─────────────────────────────────────────────────┐
    │                                                 │
    │   ╔═══╗ ╔╗ ╔╗     ╔═╗╔═╗╔╗ ╔╗                  │
    │   ║╔═╗║ ║║ ║║     ║║╚╝║║║╚═╝║                  │
    │   ║║ ║║ ║╚═╝║     ║╔╗╔╗║╚═╗╔╝                  │
    │   ║║ ║║ ║╔═╗║     ║║║║║║  ║║                   │
    │   ║╚═╝║ ║║ ║║     ║║║║║║  ║║                   │
    │   ╚═══╝ ╚╝ ╚╝     ╚╝╚╝╚╝  ╚╝                   │
    │                                                 │
    │   ╔═══╗ ╔═══╗ ╔═══╗ ╔═╗  ╔╗ ╔═══╗ ╔═══╗ ╔═══╗ │
    │   ║╔═╗║ ║╔═╗║ ║╔══╝ ║║╚╗ ║║ ║╔═╗║ ║╔═╗║ ║╔══╝ │
    │   ║║ ║║ ║╚═╝║ ║╚══╗ ║╔╗╚╗║║ ║║ ╚╝ ║║ ║║ ║║╔═╗ │
    │   ║║ ║║ ║╔══╝ ║╔══╝ ║║╚╗║║║ ║║ ╔╗ ║║ ║║ ║║╚╗║ │
    │   ║╚═╝║ ║║    ║╚══╗ ║║ ╚╝║║ ║╚═╝║ ║╚═╝║ ║╚═╝║ │
    │   ╚═══╝ ╚╝    ╚═══╝ ╚╝  ╚═╝ ╚═══╝ ╚═══╝ ╚═══╝ │
    │                                                 │
    │        [ The Magic of Creating AI Agent Teams ] │
    │                                                 │
    │     Sisyphus  +  Oracle  +  Librarian  +  ...  │
    │           ↓         ↓          ↓               │
    │        Productivity Boost 168x with Parallel   │
    │                                                 │
    └─────────────────────────────────────────────────┘
```

Would you believe that Claude Code completes in 1 hour what takes 7 days? There's a project getting reviews about handling 8,000 ESLint warnings in a single day. That's oh-my-opencode. The era of coding with a single AI agent is ending.

**Now is the era of specialized AI teams collaborating in parallel.**

**One-line summary:** oh-my-opencode is a plugin that runs on OpenCode, transforming a single AI agent into a 7-agent specialist team that builds a system that never stops until work is complete.

## Background

The AI coding tools market is changing rapidly. We've passed the code completion era started by GitHub Copilot, enabled conversational code generation with ChatGPT and Claude, and opened an agent era with Claude Code and OpenCode that directly read and modify files in the terminal.

But there was one fundamental problem: even the smartest AI has limits handling everything alone.

> **Agent Harness:** A framework serving as a "control tower" that wraps and orchestrates multiple AI agents. Like a bridle controlling a horse, it controls AIs.

oh-my-opencode is a project developed by Korean developer Kim YeonGyu. He personally validated configurations **consuming $24,000 worth of tokens** and released them packaged as a plugin.

Within 2 weeks of launch it achieved 3,400 stars, and currently (January 2026) records **21,000+ GitHub stars,** garnering hot reactions from the developer community.

### Key Comparison: Vanilla OpenCode vs oh-my-opencode

| Aspect | Vanilla OpenCode | oh-my-opencode |
| --- | --- | --- |
| Agent Composition | build/plan + @general (3) | Sisyphus + 6 specialist agents (7) |
| Model Selection | Single model | Auto-assign optimal per role |
| Execution | Sequential | Parallel background |
| Completion Guarantee | Manual verification needed | Todo Enforcer auto-continues |
| Dev Tools | 8 basic | LSP/AstGrep added |
| MCP Servers | Manual setup | Exa, Context7, Grep.app included |

## Core Concept: Sisyphus and Agent Team

> **Sisyphus:** Like the figure in Greek mythology eternally rolling a boulder, the main orchestrator agent that never stops until work is complete.

oh-my-opencode's philosophy is simple: **Transform solo-working AI into team-collaborating AI.**

In orchestra terms, Sisyphus is the conductor, and the other agents are specialist musicians playing their instruments.

### Specialized Agent Composition

| Agent | Role | Default Model | Invocation |
| --- | --- | --- | --- |
| Sisyphus | Main Orchestrator | Claude Opus 4.5 (32k) | Auto-enabled |
| Oracle | Architecture, Debugging | GPT-5.2 Medium | @oracle |
| Librarian | Official Doc Exploration | GLM-4.7 Free | @librarian |
| Explore | Ultra-fast Codebase Search | Grok Code | @explore |
| Frontend UI/UX | Frontend Dev | Gemini 3 Pro | Auto-called |
| Document-Writer | README, API Docs | Gemini 3 Flash | Auto-called |
| Multimodal-Looker | PDF, Image Analysis | Gemini 3 Flash | Auto-called |

Each agent has **different file permissions and execution modes** based on role.

For example, Oracle has Read-Only permission for analysis only,

while Frontend UI/UX has Read+Write to directly modify code.

### Aggressive Delegation Strategy

Sisyphus's core strategy is "aggressive delegation." By delegating all possible tasks to specialist agents, you gain three benefits.

**First**, main context doesn't get polluted with unnecessary information.

**Second**, multiple tasks proceed simultaneously in the background.

**Third**, the most suitable model is auto-selected for each task.

## Practical Exercise: Installation and Configuration

### Prerequisites

Before installation, verify these conditions:

- OpenCode version 1.0.150+
- One of: Claude Pro/Max, ChatGPT Plus/Pro, Google Gemini subscription
- Node.js environment (bun or npm executable)

### Step 1: Install oh-my-opencode

Run this command in terminal:

```bash
# Using bun (recommended)
bunx oh-my-opencode install

# Using npm (Ubuntu/Debian Snap environment)
npx oh-my-opencode install
```

During installation, you're asked about Claude, OpenAI, Gemini subscriptions. Select based on what you use.

### Step 2: LLM Provider Authentication

Set up authentication for each LLM provider.

**Important Update (January 2026):** Anthropic has applied technical restrictions so Claude Code OAuth tokens are usable only from official Claude Code. Using OAuth in third-party tools is considered ToS violation with account bans occurring.

**It's recommended to use Anthropic API key method.**

```bash
# OpenAI authentication
opencode auth login
# Select "OPEN AI" from provider list and complete OAuth flow

# Google Gemini authentication
opencode auth login
# Select "Google" from provider list and complete OAuth flow
# Supports up to 10 accounts (auto load-balancing)
```

When authenticating Gemini via Antigravity method, register multiple Google accounts to bypass rate limit issues.

### Step 3: Verify Installation

```bash
# Check OpenCode version (1.0.150+ required)
opencode --version

# Check authentication status
opencode auth list

# Check available models
opencode models google | grep gemini-3
```

### Step 4: Understanding Configuration Files

oh-my-opencode configuration files are stored here:

```
# Global config directory
~/.config/opencode/
├── opencode.json           # Plugin and provider settings
├── oh-my-opencode.json     # Agent-to-model mapping
└── antigravity-accounts.json

# Per-project config (overrides global)
project-root/.opencode/
└── oh-my-opencode.json
```

To specify models per agent, edit `oh-my-opencode.json`:

```json
{
  "$schema": "https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/master/assets/oh-my-opencode.schema.json",
  "google_auth": true,
  "agents": {
    "Sisyphus": {
      "model": "anthropic/claude-opus-4-5"
    },
    "oracle": {
      "model": "openai/gpt-5.2"
    },
    "librarian": {
      "model": "google/gemini-3-flash"
    }
  }
}
```

## Usage: The ultrawork Keyword

The simplest way to activate all oh-my-opencode features is including `ultrawork` or `ulw` in your prompt:

```
Analyze this project and create a refactoring plan ultrawork

Implement login functionality ulw

Fix all 8000 ESLint warnings ultrawork
```

The single `ultrawork` keyword auto-activates:

- Parallel agent execution
- Background task activation
- Todo Continuation Enforcer
- Specialist agent auto-delegation
- Continued execution until complete

To directly call specific agents, use @ mention:

```
@oracle How can we improve this system's architecture?

@librarian Find the new API documentation for React Query v5

@explore Where's the authentication-related code in this project?
```

## Best Practices/Pattern Comparison

| Usage Method | Suitable Situation | Advantages | Cautions |
| --- | --- | --- | --- |
| ultrawork | Complex multi-step tasks | Sisyphus auto-selects optimal agent | High token consumption possible |
| @oracle | Design/debugging questions | Deep analysis with GPT-5.2 possible | Response time may be long |
| @librarian | Document/code search | Fast research results | Docs may not be latest |
| @explore | Codebase exploration | Fastest response | Unsuitable for deep analysis |
| Vanilla OpenCode | Simple tasks, fast prototyping | Cost-effective | Limited for complex work |

## Conclusion

- oh-my-opencode is an OpenCode plugin transforming a single AI agent into a **7-agent specialist team.**
- Sisyphus orchestrator distributes work, and Todo Enforcer guarantees **execution that doesn't stop until complete.**
- The single `ultrawork` keyword activates parallel work, auto-delegation, and context management.

**Practical tip:** Install immediately with `bunx oh-my-opencode install` command and try typing "analyze this code ultrawork" in your project.

## References

- oh-my-opencode Official GitHub (<https://github.com/code-yeongyu/oh-my-opencode>)
- OpenCode Official Site (<https://opencode.ai/>)
- Oh My OpenCode Official Documentation (<https://ohmyopencode.com/>)
- Goddaehee's Blog - OpenCode Review Series (<https://goddaehee.tistory.com/485>)
