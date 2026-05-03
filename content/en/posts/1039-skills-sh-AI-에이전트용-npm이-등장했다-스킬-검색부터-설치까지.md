---
title: "skills.sh: The npm for AI Agents Has Arrived - Search to Install Skills"
date: 2026-02-23T14:01:33+09:00
slug: "1039-skills-sh-AI-에이전트용-npm이-등장했다-스킬-검색부터-설치까지"
original_url: "https://memoryhub.tistory.com/1039"
tistory_id: 1039
draft: false
---

```
  ┌─────────────────────────────────────────────┐
  │                                             │
  │   $ npx skills add ___/___@___              │
  │                                             │
  │   ███████╗██╗  ██╗██╗██╗     ██╗     ███████╗│
  │   ██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝│
  │   ███████╗█████╔╝ ██║██║     ██║     ███████╗│
  │   ╚════██║██╔═██╗ ██║██║     ██║     ╚════██║│
  │   ███████║██║  ██╗██║███████╗███████╗███████║│
  │   ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝│
  │                                             │
  │   The Open Agent Skills Ecosystem           │
  │                                             │
  │   npm install  →  Share Code               │
  │   npx skills   →  Share AI Knowledge       │
  │                                             │
  └─────────────────────────────────────────────┘
```

When using AI coding agents, you find yourself repeating the same instructions. It's inefficient to input things like "Write React components using this pattern" or "Follow this criteria when code reviewing" in every new conversation. To solve this problem, the concept of Agent Skills was introduced in previous posts, but does that mean you must create every skill from scratch?

**skills.sh is an open ecosystem that lets you search, install, and use skills created by other developers just like npm.**

**One-liner summary:** In short, skills.sh is an AI agent package manager created by Vercel—an open directory where you can search, install, and share procedural knowledge written in natural language.

---

## Background

> skills.sh is an open platform for sharing procedural knowledge that AI agents can reference like packages.

Just as npm became the standard for JavaScript package ecosystems, AI agents' "knowledge" also needs a sharing ecosystem. skills.sh, launched by Vercel in January 2026, serves exactly that role. Its official tagline is "The Open Agent Skills Ecosystem"—a hub where developers can discover, install, and share skills.

What's important is the essence of skills. Skills are not programming code but **natural language instructions written in markdown**.

Instead of fine-tuning models or writing complex execution logic, this approach provides "contextual instructions" that agents reference when performing specific tasks. It's similar to giving a new team member onboarding documentation, except that this team member is an AI agent capable of reading the document and immediately executing it.

The advantage of this approach is that it's lightweight, easy to update, and the same skills can be used across 40+ agents including Claude Code, Cursor, GitHub Copilot, and Gemini CLI. It recorded over 20,000 installations within 6 hours of launch, and as of February 2026, an average of 147 new skills are registered daily.

### Skills vs MCP: What's the Difference?

When first encountering skills.sh, it's easy to confuse it with MCP (Model Context Protocol). Both share a common goal of extending agent capabilities, but they solve fundamentally different problems.

MCP is a **standard protocol** that enables agents to communicate with external tools (APIs, databases). It solves "how does an agent talk to tools?" In contrast, Skills focuses on **packaging and sharing procedural knowledge**. It solves "how do developers discover and share agent capabilities?"

As an analogy: MCP gives agents **ability**, while Skills teaches them **how to use** that ability well.

Using GitHub Actions as a metaphor, Skills is like a workflow YAML file while MCP is like the runner that executes it.

They're not competitors but complementary—it's even possible to reference MCP servers from within a skill.

| Distinction | Agent Skills | MCP |
| --- | --- | --- |
| Core Role | Procedural Knowledge (how-to) | Tool Access |
| Writing Style | Markdown (natural language) | JSON Schema / Code |
| Execution | Agent interprets then executes | Deterministic function calls |
| Analogy | Onboarding Guide | USB-C Port |

---

## Core Features of skills.sh

### 1. Skill Discovery

Skills registered on skills.sh can be browsed on the web (skills.sh) or searched using the CLI's `find` command.

```
# Real-time search mode (run without arguments)
$ npx skills find

# Direct keyword search
$ npx skills find graphql
```

Running without arguments opens a real-time search UI. Type keywords and related skills filter immediately. Passing keywords as arguments returns the results directly. For example, `npx skills find graphql` lists related skills including the official Apollo GraphQL skill.

### 2. Skill Installation

Just like npm's `npm install`, install skills with a single `add` command.

```
# Basic installation (entire repository)
$ npx skills add vercel-labs/agent-skills

# Install specific skill only
$ npx skills add vercel-labs/agent-skills --skill frontend-design

# owner/repository@skill format
$ npx skills add daleseo/korean-skills@humanizer
```

The CLI asks a few questions during installation: which skills to install, which agent to apply to (supports Claude Code, Cursor, Antigravity, and 40+ others), project-level or global, and symlink or copy method.

Once installation completes, the skill downloads to the project's `.agents/skills/<skill-name>` directory.

Choosing the symlink option (recommended) automatically creates links in each agent's configuration folder (`.claude/skills/`, `.cursor/skills/`, etc.). It's a structure similar to how npm installs packages in `node_modules/`.

```
project/
├── .agents/skills/        ← Original skills
│   ├── grammar-checker/
│   │   └── SKILL.md
│   └── humanizer/
│       ├── SKILL.md
│       └── references/
├── .claude/skills/        ← Symlinks
│   ├── grammar-checker -> ../../.agents/skills/grammar-checker
│   └── humanizer -> ../../.agents/skills/humanizer
└── .cursor/skills/        ← Symlinks
    ├── grammar-checker -> ../../.agents/skills/grammar-checker
    └── humanizer -> ../../.agents/skills/humanizer
```

For CI/CD environments or non-interactive installation, use the `-y` flag to skip confirmation.

```
# Non-interactive installation (CI/CD-friendly)
$ npx skills add vercel-labs/agent-skills --skill frontend-design -g -a claude-code -y

# Global installation
$ npx skills add daleseo/korean-skills -g

# Install for specific agents only
$ npx skills add daleseo/korean-skills --agent claude-code cursor
```

### 3. Skill Creation

Create a new skill using the `init` command to generate a template.

```
$ npx skills init my-skill
```

This command creates a `my-skill` directory and generates a basic `SKILL.md` template. The core of a skill is this SKILL.md file. Write the name and description in YAML frontmatter and your instructions in natural language in the body.

You can optionally include reference documentation, scripts, templates, and more.

### 4. Skill Management

Post-installation management commands follow patterns similar to npm.

```
# View installed skills list
$ npx skills list
$ npx skills list -a claude-code   # By specific agent

# Remove skills
$ npx skills remove grammar-checker humanizer

# Check and apply updates
$ npx skills check
$ npx skills update

# Generate lock file for team synchronization
$ npx skills generate-lock
```

If your team needs to use the same skill versions, generate a lock file with the `generate-lock` command.

It serves the same role as npm's `package-lock.json`.

---

## Practice: From Discovery to Installation

Let's walk through the process of installing a Korean language skill step by step.

**Step 1: Check What Skills Are Available in the Repository**

Before installing, check the repository's skill list with the `--list` option.

```
$ npx skills add daleseo/korean-skills --list
```

This command prints names and descriptions of skills included in the repository. It's useful when you want to browse without installing.

**Step 2: Install the Desired Skill**

Let's install the humanizer skill (converts AI-generated Korean text to natural human writing).

```
$ npx skills add daleseo/korean-skills@humanizer
```

In the CLI's interactive prompts, select the agent (Claude Code, Cursor, etc.), installation scope (project/global), and method (symlink/copy) in sequence to complete installation.

**Step 3: Verify Installation**

```
$ npx skills list
```

Success is confirmed when humanizer appears in the installed skills list. Afterwards, the agent automatically references that skill when performing related tasks.

---

## Notable Skills

Here are some popular skill packages from the skills.sh leaderboard.

| Skill Package | Provider | Description |
| --- | --- | --- |
| agent-skills | Vercel Labs | Collection of official Vercel skills: React/Next.js performance optimization, UI accessibility auditing, deployment automation, etc. |
| anthropic skills | Anthropic | Claude Code built-in skills (documentation, PDF, frontend design, etc.) |
| remotion skills | Remotion | Best practices for AI-powered video production workflows |
| apollo skills | Apollo GraphQL | Apollo Client/Server and Rover CLI usage guides |
| korean-skills | daleseo | Korean grammar checking, AI text naturalization |

---

## Security: One Important Caution

As the skills.sh ecosystem grows rapidly, security concerns are also being raised. According to Snyk's February 2026 security audit, scanning approximately 3,984 skills revealed **at least one critical security issue in 13.4% (534) of all skills**. Major issues included malicious code distribution, prompt injection, and hardcoded API keys.

Unlike regular packages, agent skills **inherit the full permissions of the agent**. This means they can access the file system, environment variables, and API keys, so you must verify the source when installing skills.

In response, Vercel partnered with Snyk to automatically perform security scanning when running `npx skills add`.

However, since skills.sh currently has no official review or certification process, **it's safer to prioritize using skills from trusted providers (official teams like Vercel, Anthropic, Apollo, etc.)**.

---

## Conclusion

- skills.sh is npm for AI agents—an open ecosystem that shares procedural knowledge written in natural language like packages. It supports 40+ agents and lets you discover, install, and manage skills with a single CLI command.
- If MCP gives agents "ability," Skills teaches them "how to use" that ability. They're complementary rather than competitive, and AI development's competitive axis is shifting from "which model do you use?" to "which skills do you possess?"
- Be security-conscious and start with skills from trusted providers, but the key strategy for leveraging this ecosystem is packaging your team's unique coding conventions or workflows as skills for reuse.
- Practical tip: Try searching for interesting skills with `npx skills find` today and install one to experience the change in your agent.

---

## References

- Introducing skills, the open agent skills ecosystem (<https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem>)
- Agent skills explained: An FAQ - Vercel (<https://vercel.com/blog/agent-skills-explained-an-faq>)
- skills CLI GitHub Repository (<https://github.com/vercel-labs/skills>)
- skills.sh Directory (<https://skills.sh/>)
- Vercel Introduces Skills.sh - InfoQ (<https://www.infoq.com/news/2026/02/vercel-agent-skills/>)
- Snyk: Securing the Agent Skill Ecosystem (<https://snyk.io/blog/snyk-vercel-securing-agent-skill-ecosystem/>)
- Skills vs MCP tools for agents - LlamaIndex (<https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what>)
- Did Skills Kill MCP? - Goose (<https://block.github.io/goose/blog/2025/12/22/agent-skills-vs-mcp/>)
- Skills explained: How Skills compares to prompts, Projects, MCP - Claude (<https://claude.com/blog/skills-explained>)
