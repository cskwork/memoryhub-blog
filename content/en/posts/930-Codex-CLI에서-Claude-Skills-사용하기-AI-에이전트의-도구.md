---
title: "? Using Claude Skills in Codex CLI: AI Agent Tools"
date: 2025-12-17T15:38:01+09:00
slug: "930-Codex-CLI에서-Claude-Skills-사용하기-AI-에이전트의-도구"
original_url: "https://memoryhub.tistory.com/930"
tistory_id: 930
draft: false
---

```
  ╔═══════════════════════════════════════════════╗
  ║   SKILL.md                                    ║
  ║   ┌─────────┐    ┌─────────┐    ┌─────────┐  ║
  ║   │ Claude  │ ←→ │ SKILL   │ ←→ │ Codex   │  ║
  ║   │  Code   │    │   .md   │    │  CLI    │  ║
  ║   └─────────┘    └─────────┘    └─────────┘  ║
  ║         ↑              ↑              ↑      ║
  ║    /mnt/skills    YAML + MD    ~/.codex/     ║
  ╚═══════════════════════════════════════════════╝
```

Claude Code's Skills now work in OpenAI Codex. A competitor's feature adopted by OpenAI. This isn't just feature duplication. **It signals the emergence of the industry's first practical standard in the AI coding agent market.**

**TL;DR:** To sum up, Anthropic's SKILL.md format works in OpenAI Codex CLI, and existing Claude Skills can be reused almost as-is.

## Background

In October 2025, Anthropic introduced Skills to Claude Code. Skills are how you teach AI agents "how to perform specific tasks." Think of franchise operation manuals—every procedure from opening to closing is documented so any franchisee delivers consistent service.

> A Skill is a folder containing a SKILL.md file, serving as a reference guide that AI agents consult when performing specific tasks.

Two months later in December, OpenAI quietly adopted the same system. Without official announcement, Skills support was added to Codex CLI PRs and ChatGPT's Code Interpreter.

Why does it matter? In the AI tools market, platform lock-in is common strategy. Yet OpenAI embraced a competitor's format outright. This signals that Skills has potential to become **an industry standard**, not merely a good idea.

## Skill Structure and Operation

Skills are remarkably simple. Just one file consisting of a YAML front matter and Markdown body.

```
---
name: pdf-processing
description: Extract text and tables from PDFs. Use when PDF, form, or document extraction is mentioned.
---
# PDF Processing

- Extract text using pdfplumber.
- For form filling, see FORMS.md.
```

The process of an agent using a Skill happens in two stages.

First, at startup, only the name and description of all Skills are loaded into the system prompt. This metadata helps the agent decide "when should I use this Skill?" **Names are limited to 100 characters and descriptions to 500 characters**, so write concisely.

Second, when an agent decides a specific Skill is needed, only then is the full SKILL.md content loaded into context. This progressive disclosure approach efficiently uses the context window.

## Using Skills in Codex CLI

### 1. Create Skill directory

Codex CLI looks for Skills in `~/.codex/skills/`. It recursively explores subdirectories and only recognizes files named SKILL.md.

```
mkdir -p ~/.codex/skills/my-skill
```

### 2. Write SKILL.md file

```
cat <<'EOF' > ~/.codex/skills/my-skill/SKILL.md
---
name: react-component
description: Use when writing React components. Follow TypeScript, functional components, and custom hooks patterns.
---
# React Component Skill

## Core Rules
- Use functional components only
- Define Props with TypeScript interfaces
- Prioritize useState and useReducer for state management

## File Structure
ComponentName/
  index.tsx
  ComponentName.tsx
  ComponentName.test.tsx
  styles.module.css
EOF
```

### 3. Activate and run Skills

Skills are disabled by default in Codex CLI. Enable them with the `--enable skills` option.

```
codex --enable skills -m gpt-5.2
```

After running, use `/skills` to see available Skills, or call specific Skills directly with `$skill-name` format.

### 4. Reuse existing Claude Skills

Most Skills created for Claude Code are compatible. For example, you can install Simon Willison's Datasette plugin Skill as-is.

```
git clone https://github.com/datasette/skill \
  ~/.codex/skills/datasette-plugin
```

## Claude Code vs Codex CLI: Skill Implementation Comparison

| Item | Claude Code | Codex CLI |
| --- | --- | --- |
| Skill path | /mnt/skills/ or in project | ~/.codex/skills/ |
| Activation | Enabled by default | Requires --enable skills |
| Invocation | Read via view tool | $skill-name or /skills |
| Name limit | No explicit limit | 100 characters |
| Description limit | No explicit limit | 500 characters |
| Prompt injection prevention | Separate handling | Metadata newline removal |

The key point is that **core structure is identical**. The YAML front matter + Markdown body format, progressive disclosure approach, and folder-based structure all match.

## Conclusion

- By adopting Anthropic's Skills format, OpenAI has positioned SKILL.md as the first common standard for AI coding agents.
- Once written, a Skill can be reused across multiple platforms, increasing developer investment value.
- Practical tip: Document existing repetitive tasks as SKILL.md and use them in both Claude Code and Codex CLI.

## References

- OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI (<https://simonwillison.net/2025/Dec/12/openai-skills/>)
- Codex CLI Skills Documentation (<https://github.com/openai/codex/blob/main/docs/skills.md>)
- Anthropic Skills Repository (<https://github.com/anthropics/skills>)
- Porting Skills to OpenAI Codex (<https://blog.fsck.com/2025/10/27/skills-for-openai-codex/>)
