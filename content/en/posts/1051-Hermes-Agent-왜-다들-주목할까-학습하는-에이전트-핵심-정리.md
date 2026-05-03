---
title: "Hermes Agent: Why Everyone Pays Attention to This Learning Agent"
date: 2026-04-07T07:41:31+09:00
slug: "1051-Hermes-Agent-왜-다들-주목할까-학습하는-에이전트-핵심-정리"
original_url: "https://memoryhub.tistory.com/1051"
tistory_id: 1051
draft: false
---

```
 ┌──────────────────────────────────────┐
 │          HERMES AGENT                │
 │                                      │
 │  Chat  →  Tool Use  →  Memory        │
 │    │         │           │           │
 │    └────→  Skills  ←─────┘           │
 │                │                     │
 │      CLI / Telegram / Slack / ACP    │
 │                │                     │
 │        Docker / SSH / Modal / VPS    │
 └──────────────────────────────────────┘
```

## Introduction

Looking at open-source agent repositories these days, there are really many descriptions at the level of "calls tools" and "chats." But if you actually want to use it long-term, what matters more is whether memory persists, whether continuity works across channels, and whether it's safe to operate. Hermes Agent puts that exact point front and center, so once you see it, you immediately understand why it's becoming a hot topic. In this article, without reading lengthy READMEs, we'll comprehensively cover why you should try Hermes Agent and how to get started.

## TL;DR

Hermes Agent is closer to an open-source AI agent runtime designed for operations, bundling memory, skills, multi-channel, and execution isolation—not just a simple LLM wrapper for chatting. ([GitHub](https://github.com/nousresearch/hermes-agent))

## Background

When looking at Hermes Agent, the key to remember first is that it's less like "a project with many features" and more like a runtime for actually continuously operating agents. The official repository introduces this project as a self-improving AI agent and, as of April 7, 2026, records approximately 27.9k stars and 3.7k forks in the public repository.

Also based on package metadata, it requires Python 3.11 or higher and uses MIT license. ([GitHub](https://github.com/nousresearch/hermes-agent))

- **Architecture with learning loop front and center**: The official README explains creating skills from experience, improving during use, searching past conversations, and building deep user models beyond sessions. The key here is that it's not a "bot that answers once and ends" but a "structure where context accumulates with use." ([GitHub](https://github.com/nousresearch/hermes-agent))
- **Low model dependency composition**: The Quickstart documentation shows you can choose from various providers: Nous Portal, OpenAI, Anthropic, OpenRouter, Hugging Face, GitHub Copilot, Custom Endpoint. Rather than being locked into one specific model, it centers on the agent runtime itself and swaps providers. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart))
- **High channel extensibility**: Based on README and architecture documentation, it supports both CLI and messaging gateways, and the architecture shows 14 adapters: Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Mattermost, Email, SMS, DingTalk, Feishu, WeCom, Home Assistant, and Webhook. ([GitHub](https://github.com/nousresearch/hermes-agent))
- **Takes security and isolation seriously**: Approval modes, risky command detection, Docker isolation, and environment variable passthrough restrictions are separately documented for operations. It's notable that production environments recommend isolated backends like Docker, Modal, and Daytona. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/security))
- **Fast update pace**: Just looking at recent releases, v0.5.0 on March 28, 2026, v0.6.0 on March 30, and v0.7.0 on April 3 came in quick succession. Recent versions rapidly added features like Hugging Face provider, multi-profile, MCP server mode, Docker containers, and pluggable memory providers. ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.5.0.md))

## Core

> Hermes Agent is an open-source agent runtime that stacks tool execution, long-term memory, a skills system, messaging gateways, and execution environment isolation on top of a conversational LLM interface.

> It's closer to a project for building "operationally viable agents" that work across multiple channels and accumulate user context than building chatbots that answer well.

What makes Hermes Agent interesting is putting memory and skills at the center rather than as separate options.

The README describes past conversation search, memory persistence, and skill creation and improvement as core features, and

in the documentation, Skills System, Memory, Context Files, and Cron Scheduling are placed together as major pillars.

This project is thus closer to "an assistant that progressively structures work habits" than "a chatbot that also does web search." ([GitHub](https://github.com/nousresearch/hermes-agent))

The architecture diagram is also quite clear. The architecture documentation groups multiple entry points like CLI, Gateway, ACP, Batch Runner, API Server, and Python Library around one central `AIAgent`. Also, when assembling prompts, personality, memory, skills, and context files are reflected together, and config, memory, sessions, and gateway PID are separated per profile.

This design enables smooth progression from personal experimentation to team-scale segregated operations. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture))

Security is particularly striking from an operational perspective. The approval system has `manual`, `smart`, and `off` modes and separately detects risky commands. Conversely, the Docker backend strengthens security by making the container itself a boundary, and production gateways recommend isolated backends over hosts.

Also, based on the FAQ documentation, conversations, memory, and skills are stored by default locally under `~/.hermes/` and don't collect telemetry. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/security))

## Hands-On Practice

### Starting with Installation

Language/version is `Bash`, and package requirement is `Python >= 3.11`. The fastest startup path is the official one-line installation script, with guidance based on Linux, macOS, and WSL2. For Windows, WSL2 is the official documentation path over native. ([GitHub](https://github.com/nousresearch/hermes-agent))

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
```

### Connecting Models and Tools

The three important commands immediately after installation are:

```
hermes model
hermes tools
hermes setup
```

You can interactively choose the provider and separately configure the tool activation scope.

### Starting Your First Conversation

The most basic entry point is the CLI. The official Quickstart guides running `hermes` and immediately starting conversation, then extending with commands like `/model`, `/tools`, `/help`, `/save`.

```
hermes
```

The execution result text looks roughly like this:

```
[Text Replacement Snapshot]
- Top welcome banner displayed
- Currently selected provider / model shown
- Available tools / skills displayed
- Input prompt opens and conversation starts immediately
```

### Expanding to Messaging Channels

This is where Hermes Agent gets fun. Instead of staying in CLI, when you open a gateway, you can continue using the same agent on Telegram, Discord, Slack, etc. The basic flow based on README is:

```
hermes gateway setup
hermes gateway start
```

### Must-Have Checks Before Operations

The local backend runs by default under host permissions, so for actual operations or automation, it's safer to switch to an isolated backend like Docker. Both Quickstart and Security documentation recommend separated environments like Docker, SSH, Modal, and Daytona. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart))

```
hermes config set terminal.backend docker
```

## Best Practices and Pattern Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Quick Experience: CLI Standalone | Conversation possible immediately after installation, low barrier to entry. | Local backend uses host environment directly, so it's good to keep experimental scope small. |
| Operation Separation: Docker/Remote Backend | Command execution isolated improves operational stability and security. | Image, resource limits, and environment variable passing policies need integrated design. |
| Multi-Channel: Gateway Connection | Expanding touchpoints via Telegram, Discord, Slack increases practical usability. | It's easier to manage if you define channel-specific permissions, approval flows, and response policies first. |
| Extension: MCP/ACP/Profiles | Can extend to editor integration, external MCP tool connection, and profile-separated operations. | As features multiply, profile-specific settings and tool exposure scope need separation. |

The above comparison is organized based on official Quickstart, architecture, security documentation and recent release notes. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart))

## Conclusion

Hermes Agent has quite a mature structure even to be seen as just "one trending agent repository." The real point of this project is particularly bundling memory, skills, gateway, and isolated execution all together. It's fun even with light experience, but from an operational standpoint, the real value shines through. This can be summarized as a repository where you see deeper value when viewed from an operations perspective.

**Demoing via CLI is fine, but operations are much cleaner when starting with isolated backends and profile separation.**

## References

- GitHub repository main page and README summary information ([GitHub](https://github.com/nousresearch/hermes-agent))
- Hermes Agent Quickstart documentation ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart))
- Hermes Agent Architecture documentation ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture))
- Hermes Agent Security documentation ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/security))
- Hermes Agent FAQ documentation ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/faq/?utm_source=chatgpt.com))
- Hermes Agent v0.5.0 release notes ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.5.0.md))
- Hermes Agent v0.6.0 release notes ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.6.0.md))
- Hermes Agent v0.7.0 release notes ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.7.0.md))
