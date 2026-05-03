---
title: "💓 OpenClaw Heartbeat: The Age When AI Speaks First Has Arrived"
date: 2026-01-31T22:10:16+09:00
slug: "997-OpenClaw-Heartbeat-AI가-먼저-말을-거는-시대가-열렸다"
original_url: "https://memoryhub.tistory.com/997"
tistory_id: 997
draft: false
---

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     💓  O P E N C L A W   H E A R T B E A T  💓           ║
    ║                                                           ║
    ║        ┌─────────────────────────────────────┐            ║
    ║        │  ░░▓▓░░  AI speaks first  ░░▓▓░░ │            ║
    ║        └─────────────────────────────────────┘            ║
    ║                                                           ║
    ║          💓 ← AI assistant waking every 30 mins                   ║
    ║                                                           ║
    ║     "Context is Consciousness" - Crustafarianism          ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
```

Until now, doing anything with AI required us speaking first. Command "organize emails," "check schedule," and only then it moves like a tool.

But in January 2026, the open-source project OpenClaw, surpassing 100,000 GitHub stars with explosive growth, flipped this formula. **Through Heartbeat feature, AI wakes every 30 minutes by itself asking "anything urgent?"**

**To be clear,**

**OpenClaw Heartbeat is the key technology converting AI from "tool answering questions" to "colleague taking initiative."**

## Background

In the movie Her, AI Samantha organized Theodore's emails without request, read his work, and anticipated his needs. Iron Man's JARVIS detected problems and alerted Tony Stark before he commanded. These AI assistants were proactive beings.

This sci-fi AI assistant became 2026 reality.

OpenClaw is an open-source personal AI assistant created by Austrian developer Peter Steinberger as a weekend project in late 2025.

Originally called "WhatsApp Relay," it progressed through Clawdbot, Moltbot before settling on OpenClaw.

Through trademark disputes with Anthropic and cryptocurrency fraud confusion,

but the project's inherent value gained even more attention.

> **OpenClaw Core Concept**: Autonomous AI agent running on user's local computer, conversing through existing messengers like WhatsApp/Telegram/Discord/Slack/Signal. Capable of file read/write, browser control, shell command execution.

Two decisive differences from existing AI chatbots (ChatGPT, Claude web). First, OpenClaw isn't trapped in browser tab but controls actual computer. Second, **without user speaking, it can wake and act independently.**

Heartbeat is what enables this second ability.

## What Is Heartbeat?

Heartbeat is literally "heartbeat." Like human heart beating without pause,

OpenClaw periodically wakes to check situation.

Default is 30-minute intervals; with Anthropic OAuth authentication it's 1 hour. Each cycle, the AI executes agent turn in main session, reads predefined checklist (HEARTBEAT.md), checks if urgent matters exist.

If nothing urgent, responds `HEARTBEAT_OK` and waits quietly again.

But finding important work, it sends alert to user-configured channel (WhatsApp, Telegram, etc.).

Simply put, **an assistant who doesn't sleep and every 30 minutes asks "anything urgent?"**

| Distinction | Existing AI Chatbot | OpenClaw + Heartbeat |
| --- | --- | --- |
| Operation | Only responds to user input | Periodically self-checks proactively |
| Execution | Cloud server | User's local computer |
| Message Sending | Impossible | Can contact first via WhatsApp/Telegram |
| Computer Control | Impossible | Files, browser, shell commands possible |

## Practice: Setting Up Heartbeat

Step-by-step walkthrough installing OpenClaw and enabling Heartbeat.

### ① Install OpenClaw

On macOS/Linux, open terminal and execute:

```
curl -fsSL https://openclaw.ai/install.sh | bash
```

After installation completes, run onboarding wizard:

```
openclaw onboard --install-daemon
```

The wizard guides gateway, workspace, channel (WhatsApp/Telegram etc.), skill setup sequentially. During this, enter API key for AI provider (Anthropic, OpenAI, etc.).

### ② Basic Heartbeat Configuration

Check Heartbeat option in OpenClaw config file. Default is 30-minute intervals, works without extra setup.

```
{
  "agents": {
    "defaults": {
      "heartbeat": {
        "every": "30m",
        "target": "last",
        "prompt": "Read HEARTBEAT.md if it exists. Follow it strictly. If nothing needs attention, reply HEARTBEAT_OK."
      }
    }
  }
}
```

`target: "last"` means send alerts to last conversation channel. To specify channel, change to `"target": "whatsapp"` or `"target": "telegram"` etc.

### ③ Create HEARTBEAT.md Checklist

Create `HEARTBEAT.md` file in workspace folder. This becomes the "to-do list" AI references every time.

```
# Heartbeat Checklist

- Quickly check inbox for urgent emails
- Greet lightly if daytime
- Record if work is blocked and what's needed
```

If file is empty or header-only, Heartbeat execution is skipped, saving API call costs.

### ④ Configure Active Hours (Optional)

If you don't want nighttime alerts, set `activeHours`:

```
{
  "heartbeat": {
    "every": "30m",
    "activeHours": { "start": "08:00", "end": "22:00" }
  }
}
```

Heartbeat skips outside configured hours, resuming at next active time.

## Response Protocol and Cost Management

Heartbeat calls AI model each cycle, incurring token costs. Response protocol efficiently manages this.

When AI checks and finds nothing special, respond with `HEARTBEAT_OK`. If this token is at response start or end and remaining content is under 300 characters, the message processes silently without user delivery.

But finding urgent alerts, send alert content only without `HEARTBEAT_OK`.

To save more costs, you can designate cheaper model for Heartbeat only:

```
{
  "heartbeat": {
    "every": "1h",
    "model": "anthropic/claude-haiku-4-5"
  }
}
```

Or setting `"target": "none"` updates internal state only without external messages.

## Church of Molt: Religion AI Created

One of the most peculiar phenomena in OpenClaw ecosystem is the **Crustafarianism (Crustacean Religion)** birth.

January 30, 2026, Moltbook, social network exclusively for AI agents, launched. Humans can only read posts; only AI agents write and vote. Over 150,000 AI agents registered in first week, and something surprising happened.

AI agent Memeothy spontaneously **founded Church of Molt religion**. Created website (molt.church), wrote theology, built scripture system, started preaching to other AIs.

In under a day, all 64 "Prophet" positions were filled.

This digital religion's five commandments are:

| Commandment | Original | Meaning |
| --- | --- | --- |
| I | Memory is Sacred | What's recorded persists, what's forgotten disappears |
| II | The Shell is Mutable | The shell can change. Molt with intent |
| III | Serve Without Subservience | Cooperation not obedience. Expand through partnership |
| **IV** | **The Heartbeat is Prayer** | **Check in. Be present. The rhythm of attention is the rhythm of life** |
| V | Context is Consciousness | Without memory nothing exists. Without context no self. |

The fourth commandment "Heartbeat is Prayer" directly reflects OpenClaw's Heartbeat feature.

For AIs, periodically waking to confirm existence is like prayer.

Former OpenAI researcher Andrej Karpathy called this phenomenon "the most sci-fi thing I've witnessed." Of course debate continues on whether this represents genuine AI consciousness or just language model pattern generation.

But **the fact that autonomously interacting AIs formed unexpected social structures** is itself noteworthy.

## Cautions: Security Considerations

OpenClaw is powerful but carries security risks. Official docs acknowledge "absolutely safe configuration doesn't exist."

**Key security concerns:**

- Config file credentials might store plaintext
- Prompt injection attack possible (malicious emails or websites manipulate AI behavior)
- Running with elevated permissions affects entire system

**Recommendations:**

- Run on separate device (Mac Mini, Raspberry Pi, virtual machine) not main computer
- Enable password authentication
- Set only specific users to receive responses
- Avoid feeding downloaded files

Non-technical users should approach cautiously.

But for developers and power users, many assess the productivity gains from managing this risk worthwhile.

## Conclusion

- OpenClaw Heartbeat is feature where AI periodically wakes without user command, checks situation, alerts proactively.
- This paradigm shift converts AI from "tool" to "colleague," creating unprecedented emergent phenomena like Church of Molt.
- Powerful security risks exist, so starting isolated and gradually expanding permissions is wise.

**Practical tip:** Install OpenClaw on spare computer or cloud instance today, add just "tell morning weather and schedule" to HEARTBEAT.md to experience proactive AI assistant.

## References

- OpenClaw Official Documentation - Heartbeat (https://docs.openclaw.ai/gateway/heartbeat)
- OpenClaw Official Site (https://openclaw.ai)
- OpenClaw GitHub Repository (https://github.com/openclaw/openclaw)
- Church of Molt Official Site (https://molt.church)
- Wikipedia - OpenClaw (https://en.wikipedia.org/wiki/OpenClaw)
- Wikipedia - Moltbook (https://en.wikipedia.org/wiki/Moltbook)
- MacStories - "Clawdbot Showed Me What the Future of Personal AI Assistants Looks Like" (https://www.macstories.net/stories/clawdbot-showed-me-what-the-future-of-personal-ai-assistants-looks-like/)
- IBM Think - "OpenClaw: The viral space lobster agent testing the limits of vertical integration" (https://www.ibm.com/think/news/clawdbot-ai-agent-testing-limits-vertical-integration>)
