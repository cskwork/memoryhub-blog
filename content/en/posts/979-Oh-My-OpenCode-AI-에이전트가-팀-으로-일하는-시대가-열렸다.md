---
title: "Oh My OpenCode: The Era of AI Agents Working as a Team"
date: 2026-01-18T09:11:09+09:00
slug: "979-Oh-My-OpenCode-AI-에이전트가-팀-으로-일하는-시대가-열렸다"
original_url: "https://memoryhub.tistory.com/979"
tistory_id: 979
draft: false
---

```
   ___  _       __  __          ___                    ____          _      
  / _ \| |__   |  \/  |_   _   / _ \ _ __   ___ _ __  / ___|___   __| | ___ 
 | | | | '_ \  | |\/| | | | | | | | | '_ \ / _ \ '_ \| |   / _ \ / _` |/ _ \
 | |_| | | | | | |  | | |_| | | |_| | |_) |  __/ | | | |__| (_) | (_| |  __/
  \___/|_| |_| |_|  |_|\__, |  \___/| .__/ \___|_| |_|\____\___/ \__,_|\___|
                       |___/        |_|                                     
          Your AI Teammates Are Waiting
```

Ever felt frustrated with AI coding tools that work alone? Imagine GPT debugging the backend while Claude tries a different approach, and Gemini works on the frontend.

**Oh My OpenCode is an OpenCode plugin that makes this multi-agent collaboration a reality.**

This project, which has received 17,900+ GitHub stars, is generating explosive interest among developers. Let's explore why.

**One-line summary:** In short, Oh My OpenCode is a powerful OpenCode extension plugin that organizes multiple AI models as specialist agents to enable parallel collaboration.

## Background

The terminal-based AI coding tools market is growing rapidly. Tools like Claude Code, Cursor, and OpenCode compete, but most have an architecture where a single model processes tasks sequentially.

The problem is that a single AI struggles to do everything well on complex projects.

> Oh My OpenCode: A batteries-included plugin for OpenCode where 7+ specialist AI agents collaborate in parallel in the background, providing a compatibility layer that lets you use Claude Code's existing settings as-is.

Think of how teams work in companies. Senior architects handle design, QA specialists do code review, frontend developers implement UI. Oh My OpenCode applies this team structure to AI agents. Each agent is optimized for specific AI models and roles, delivering peak performance in their domain.

This project was created by Korean developer code-yeongyu and currently has 17,900+ GitHub stars and 850+ forks. As an OpenCode plugin, it provides a compatibility layer so Claude Code users can leverage existing settings.

## Core Feature 1: Agent Team System

Oh My OpenCode's most powerful feature is its 7-agent specialist system.

Each agent is configured for specific AI models and roles.

**Sisyphus (Primary Agent)**: The main orchestrator based on Claude Opus 4.5. Uses a 32k token Extended Thinking budget to plan complex tasks and delegate to other agents. Serves as the project's chief coordinator.

**oracle**: Based on GPT-5.2, handles architecture design, code review, and strategy planning.

Called when logical reasoning and deep analysis are needed.

**librarian**: Uses the GLM-4.7 Free model for multi-repository analysis, documentation lookup, and implementation example search. Provides evidence-based answers and specializes in GitHub research.

**explore**: Chosen from Gemini 3 Flash, Claude Haiku 4.5, or Grok depending on configuration.

Optimized for fast codebase exploration and pattern matching.

**frontend-ui-ux-engineer**: Based on Gemini 3 Pro Preview, handles UI/UX design and implementation.

Leverages Gemini's creative code generation capability to create beautiful interfaces.

**document-writer**: A technical documentation specialist using Gemini 3 Flash.

**multimodal-looker**: A visual content specialist based on Gemini 3 Flash, handling PDF, image, and diagram analysis.

Agent invocation is simple with natural language:

```
# Request architecture review
Ask @oracle to review this design and propose an architecture

# Request implementation research
Ask @librarian how this is implemented—why does the behavior keep changing?

# Request quick exploration
Ask @explore for the policy on this feature
```

## Core Feature 2: Background Agents and Parallel Execution

Traditional AI coding tools handle one task at a time. Oh My OpenCode can run multiple agents simultaneously in the background.

Real-world scenario: GPT debugs a bug while Claude finds the root cause with a different approach. Or Gemini writes the frontend while Claude handles the backend. You can execute large-scale parallel searches while continuing implementation elsewhere, then finish using the search results.

Background execution is controlled via the `run_in_background` parameter of the `delegate_task` tool.

When complete, the main agent receives a notification and can wait for results if needed.

## Core Feature 3: IDE-Grade Tools for Agents

The documentation's question is striking: "Why only you use IDE's great tools? What if we give them to agents?"

Oh My OpenCode provides LSP (Language Server Protocol) and AST (Abstract Syntax Tree)-based tools to agents.

| Tool | Function |
| --- | --- |
| lsp_diagnostics | Check errors/warnings before build |
| lsp_prepare_rename | Validate rename operations |
| lsp_rename | Rename symbols across workspace |
| ast_grep_search | AST-aware code pattern search (25 languages) |
| ast_grep_replace | AST-aware code replacement |

Code structure-aware search and replacement, not plain text matching. Variable renaming happens safely across the entire workspace, and potential issues can be identified before building.

## Core Feature 4: Automatic Context Injection

AI coding agent performance greatly depends on context. Oh My OpenCode injects context automatically in three ways:

**AGENTS.md / README.md Injector**: When reading a file, automatically collects and injects all AGENTS.md and

README.md files from that directory up to the project root.

```
project/
├── AGENTS.md              # Project-wide context
├── src/
│   ├── AGENTS.md          # src-specific context
│   └── components/
│       ├── AGENTS.md      # Component-specific context
│       └── Button.tsx     # Reading this file injects all 3 AGENTS.md above
```

**Conditional Rules Injector**: Rules in `.claude/rules/` are conditionally applied based on glob pattern matching. Not all rules are needed all the time.

```
---
globs: ["*.ts", "src/**/*.js"]
description: "TypeScript/JavaScript coding rules"
---
- Use PascalCase for interface names
- Use camelCase for function names
```

**Built-in MCP Servers**: Context7 (official documentation), Exa AI web search, grep.app (public GitHub repo search) are enabled by default.

## Core Feature 5: Claude Code Compatibility Layer

Great news for Claude Code users.

Oh My OpenCode provides a complete Claude Code compatibility layer. **You can use existing configuration files as-is.**

Compatible items include:

| Item | Load Path |
| --- | --- |
| MCP Servers | ~/.claude/.mcp.json, ./.mcp.json |
| Commands | ~/.claude/commands/, ./.claude/commands/ |
| Skills | ~/.claude/skills/, ./.claude/skills/ |
| Agents | ~/.claude/agents/, ./.claude/agents/ |
| Hooks | ~/.claude/settings.json |

Hook system is also supported. Connect custom scripts to PreToolUse, PostToolUse, UserPromptSubmit, and Stop events.

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{ "type": "command", "command": "eslint --fix $FILE" }]
      }
    ]
  }
}
```

A linter automatically runs after file creation or modification.

## Core Feature 6: Skills with Built-in MCP Support

Skills can have their own MCP servers. Define MCP configuration directly in skill frontmatter or mcp.json file.

```
---
description: Browser automation skill
mcp:
  playwright:
    command: npx
    args: ["-y", "@anthropic-ai/mcp-playwright"]
---
```

When a skill loads, its MCP tools become automatically available. With the built-in playwright skill, you can immediately use browser automation, web scraping, testing, and screenshot capabilities.

## Installation Method

① OpenCode must be installed first. Check the OpenCode official site for installation guide.

② Install Oh My OpenCode:

```
bunx oh-my-opencode
# or
npx oh-my-opencode
```

③ Configure Claude, ChatGPT, and Gemini subscriptions as prompted.

④ After installation, type `opencode` in the terminal to start using.

One caveat: As of January 2026, Anthropic has restricted third-party OAuth access as a ToS violation.

While technically usable with a Claude Code subscription, be aware of ToS implications.

## Best Practices/Pattern Comparison

| Approach | Advantages | Cautions |
| --- | --- | --- |
| Single Model (Claude Code) | Consistent experience, official support | Limited model choices, no parallel processing |
| Multi-Model (Oh My OpenCode) | Leverage each model's strengths, parallel collaboration | Configuration complexity, ToS verification needed |
| Local Models (Ollama integration) | Cost reduction, privacy guaranteed | Hardware requirements, performance limits |

## Conclusion

- Oh My OpenCode presents a paradigm shift from "solo assistant" to "team collaborator" AI coding tools.
- 7+ specialist agents, background parallel execution, IDE-grade tool support, and Claude Code compatibility layer are key strengths.
- Practical tip: Start with default configuration and create an AGENTS.md file in your project root to define project-specific context.

## References

- Oh My OpenCode GitHub (<https://github.com/code-yeongyu/oh-my-opencode>)
- OpenCode Official Site (<https://opencode.ai/>)
- OpenCode GitHub (<https://github.com/opencode-ai/opencode>)
