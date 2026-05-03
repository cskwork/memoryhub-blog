---
title: "? Claude Skills vs MCP, Both Extensions But What's Different?"
date: 2025-12-19T05:40:47+09:00
slug: "939-Claude-Skills-vs-MCP-둘-다-확장-기능인데-뭐가-다를까"
original_url: "https://memoryhub.tistory.com/939"
tistory_id: 939
draft: false
---

```
    ╔═══════════════════════════════════════════╗
    ║                                           ║
    ║   ┌─────────┐         ┌─────────┐        ║
    ║   │   MCP   │ ──────► │ External│        ║
    ║   │ Protocol│         │ Systems │        ║
    ║   └─────────┘         └─────────┘        ║
    ║        │                                  ║
    ║        ▼                                  ║
    ║   ┌─────────┐                            ║
    ║   │  Claude │                            ║
    ║   └─────────┘                            ║
    ║        ▲                                  ║
    ║        │                                  ║
    ║   ┌─────────┐         ┌─────────┐        ║
    ║   │  Skills │ ◄────── │SKILL.md │        ║
    ║   │ Loader  │         │  Files  │        ║
    ║   └─────────┘         └─────────┘        ║
    ║                                           ║
    ║      Skills vs MCP: What's Different?     ║
    ╚═══════════════════════════════════════════╝
```

As MCP gains traction, developers everywhere are connecting external tools to Claude. Then in October 2025, Anthropic announced Skills, a new feature. "Isn't this also an extension? How's it different from MCP?" This question is natural. **Bottom line: MCP defines 'what Claude accesses'; Skills define 'how Claude acts.'** They're not competitors—they're complementary roles.

**TL;DR:** MCP is a protocol for connecting external systems. Skills are Markdown-based instruction manuals for performing tasks.

---

## Background

As the AI agent era takes off, interest in extending LLMs has exploded. Writing good prompts alone isn't enough anymore. Querying external databases, calling APIs, and following specific workflows requires systematic approaches.

Anthropic solved this in two directions. MCP (Model Context Protocol), announced November 2024, standardized external system connections. Skills, announced October 2025, offered a way to package repeating task execution. The problem: the boundary between them seems unclear.

> **Think of MCP as AI's nervous system (connecting externally), Skills as AI's playbook (behavioral guidelines).**

---

## What is MCP?

MCP (Model Context Protocol) is an **open protocol** standardizing how AI models communicate with external systems. Think of it as the USB-C port of the AI world. Build an MCP server once, reuse it everywhere—Claude Desktop, IDE extensions, other AI clients.

MCP has three core components. **MCP Host** is an AI application like Claude wanting external data access. **MCP Client** maintains 1:1 connections between Host and each MCP server. **MCP Server** exposes external resources (databases, APIs, file systems) through standard interfaces.

Real examples clarify this. A sales team AI agent queries CRM via MCP. A CI/CD bot fetches GitHub issues through GitHub MCP. Searching Slack or reading Notion pages—all MCP territory.

MCP's strength is **standardization and reusability.** Built once, MCP servers work with all MCP-supporting AI models. Even OpenAI's Agents SDK explicitly supports MCP. SDKs exist for multiple languages (Python, TypeScript, Java, Kotlin), making implementation relatively easy.

**But MCP has token costs.** GitHub's official MCP server reportedly consumes tens of thousands of tokens for initial context alone. More MCP connections mean less available context for actual work.

---

## What are Skills?

Skills are **Markdown-based instruction packages** teaching Claude how to perform specific tasks. Technically: a folder containing SKILL.md (YAML front matter + Markdown guidelines) and optional scripts/resources.

Skills work simply. Claude receives user requests, scans registered Skills metadata, loads only relevant Skills in context, and progressively fetches supporting documents/scripts. This **Progressive Loading** approach is very token-efficient.

Skills shine in clear scenarios: generating PDF reports in specific formats, reviewing code per team conventions, organizing analysis results with templates. Works without external systems, requiring only Markdown files—low barrier to entry.

Simon Willison (renowned developer/blogger) said Skills "could be a bigger change than MCP." Why? MCP requires understanding protocols, servers, clients, transport. Skills need only documentation writing ability.

---

## Core Differences Comparison

| Aspect | MCP | Skills |
| --- | --- | --- |
| **Core Question** | "What can I access?" | "How should I perform?" |
| **Implementation** | Protocol + server build | Markdown file writing |
| **Token Efficiency** | Low (thousands~tens of thousands) | High (loads only when needed) |
| **External Connection** | Core feature | Limited (no OAuth) |
| **Learning Curve** | Steep | Gentle |
| **Standardization** | Open protocol (vendor-neutral) | Anthropic-specific (concepts portable) |
| **Best For** | Real-time external data integration | Repeating task standardization, workflow definition |

As analogy: MCP is **a plumber** connecting pipes for data flow. Skills are **work manuals**—"do this in this situation" guidelines. Pipes without manuals make consistency hard; manuals without pipes can't access external data.

---

## Real Scenario: Customer Support AI Agent

The best example of their relationship is building support agents.

**MCP handles:** Access ticketing systems (Zendesk, Jira) to retrieve inquiries. Fetch customer history from CRM. Call email APIs when needed. This is "external connection" territory.

**Skills handle:** Define customer response tone and language. Specify escalation criteria by issue type. Format response templates. Provide checklists for refund requests. This is "behavioral style" territory.

MCP alone gives data access but inconsistent quality. Skills alone define behavior but can't use real-time customer data. **Combine both, and you get a true AI agent.**

---

## Choosing What to Use When

**Choose MCP when:** Real-time external data is essential. Check GitHub repo status, search CRM customers, analyze Slack messages. Also when reusing integrations across non-Claude AI models.

**Choose Skills when:** Repeating specific-format work without external connections. Daily standup transcription in standard format, team-convention code review, template-based document generation. Skills excel where token efficiency matters.

**Use both when:** Need both external data access and consistent work quality. Customer support agents (earlier example), data journalism agents (external collection + methodology), deployment automation (GitHub/CI connection + release note rules).

---

## Conclusion

- MCP is Claude's nervous system for accessing the external world; Skills are the playbook for performing tasks.
- They're complementary, not competitive. Complex AI agents need both.
- Skills' token efficiency and low barriers open new possibilities in MCP-centric ecosystems.

**Practical tip: Write one repeating task into SKILL.md today. With Markdown skills, you'll have your first Skill in 5 minutes.**

---

## References

- Anthropic Official Blog - Skills Explained (<https://claude.com/blog/skills-explained>)
- Simon Willison - Claude Skills are awesome, maybe a bigger deal than MCP (<https://simonwillison.net/2025/Oct/16/claude-skills/>)
- MCP Directory - Claude Skills vs MCP Complete Guide (<https://www.mcplist.ai/blog/claude-skills-vs-mcp-guide/>)
- IntuitionLabs - Claude Skills vs. MCP: A Technical Comparison (<https://intuitionlabs.ai/articles/claude-skills-vs-mcp>)
