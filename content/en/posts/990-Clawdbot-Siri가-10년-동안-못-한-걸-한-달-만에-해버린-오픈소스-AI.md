---
title: "🤖 Clawdbot: The Open-Source AI That Did in a Month What Siri Couldn't in 10 Years"
date: 2026-01-25T22:15:12+09:00
slug: "990-Clawdbot-Siri가-10년-동안-못-한-걸-한-달-만에-해버린-오픈소스-AI"
original_url: "https://memoryhub.tistory.com/990"
tistory_id: 990
draft: false
---

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║      🤖 C L A W D B O T 🤖                                ║
    ║                                                           ║
    ║      ┌─────────────────────────────────────────────┐      ║
    ║      │  Your Computer                              │      ║
    ║      │  ┌─────────┐  ┌─────────┐  ┌─────────┐     │      ║
    ║      │  │ Email   │  │Calendar │  │ Files   │     │      ║
    ║      │  └────┬────┘  └────┬────┘  └────┬────┘     │      ║
    ║      │       │            │            │          │      ║
    ║      │       └────────────┼────────────┘          │      ║
    ║      │                    ▼                       │      ║
    ║      │              ╔═══════════╗                 │      ║
    ║      │              ║  CLAWDBOT ║◄──── WhatsApp   │      ║
    ║      │              ║   Agent   ║◄──── Telegram   │      ║
    ║      │              ╚═══════════╝◄──── Discord    │      ║
    ║      └─────────────────────────────────────────────┘      ║
    ║                                                           ║
    ║      "The AI that actually does things."                  ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
```

What if there's an AI that actually organizes your emails when you say "organize emails." An AI that checks calendars, creates files, and even writes code to add missing features.

That's completely different from when you ask ChatGPT or Claude "send email" and get only instructions on how to do it.

**Clawdbot is "an AI that actually works," not "an AI that talks."** And it's open source, running 24/7 on your computer.

**One-sentence summary:** Clawdbot is an open-source AI agent that resides on your computer and receives instructions via WhatsApp/Telegram to actually perform email, calendar, and file management tasks.

## Background

The AI assistant market faces a paradoxical situation. State-of-the-art models like GPT-4 and Claude Opus have human-level reasoning capabilities, but fall short at "actually doing something" in our daily lives. Siri launched in 2011, Bixby in 2017, yet even in 2026,

they can't handle "organize today's meeting materials and share with team."

> Clawdbot is an open-source personal AI agent that enables LLMs to actually manipulate computers.

A solo developer's open-source project filled this gap. Peter Steinberger (famous for PSPDFKit in the iOS dev community) created Clawdbot, which surpassed 8,000 GitHub stars in less than a month after its late 2025 launch, shaking the developer community. Federico Viticci of MacStories called this project "showing the future of personal AI assistants."

Why did individual projects accomplish in days what corporations couldn't in years? The answer is simple.

The approach was completely different.

## How Clawdbot Differs Fundamentally from Other AI Assistants

### 1. Local Execution: "Resides" on Your Computer

ChatGPT and Claude run on the cloud. You send a question to the server, which generates and returns the answer.

In contrast, Clawdbot **runs directly on your Mac, Windows, or Linux computer**.

Why does this matter? Running locally means it has direct access to your file system, terminal, and browser.

When you say "open the report.docx on desktop and summarize it," it actually opens and reads the file.

When you say "check Google Calendar for this week's schedule," it controls the browser to actually check.

### 2. Messaging App Integration: Talk in Apps You Already Use

Another core of Clawdbot is the **gateway** system. Without installing a separate app,

you can chat with Clawdbot in WhatsApp, Telegram, Discord, Slack, Signal, iMessage that you already use.

Just text "organize today's emails" to Telegram on your commute, and Clawdbot running on your home Mac mini accesses Gmail, categorizes emails, and sends a summary back via Telegram.

It's like messaging a remote-working assistant.

### 3. Self-Improvement: Creates Needed Features Itself

The most shocking part. When Clawdbot needs a feature it doesn't have, **it writes code and adds it itself**.

MacStories' Viticci reported that when he asked Clawdbot to add Google Nano Banana image generation, it found API documentation, figured out how to securely store credentials in macOS keychain, and implemented the feature on its own.

All Clawdbot settings and functions are **stored as markdown files in a local folder**.

Like Obsidian where everything is text files, you can transparently check and modify. AI is not a black box.

## Real-World Use Cases

### Case 1: Automated Morning Briefing

MacStories editor receives an automated briefing from Clawdbot every morning. It compiles today's calendar schedule, Notion task list, Todoist priority tasks into a Telegram message. Plus **voice version** generated by ElevenLabs TTS alongside the text. All this runs with a single cron job.

### Case 2: Zapier Automation Replacement

There's a case where an existing Zapier automation with monthly subscription fee was replaced with Clawdbot. "Check news after sending Friday newsletter, create next issue project in Todoist" task was explained to Clawdbot, which

wrote cron job and script directly in 5 minutes. Automation complete without cloud dependency or subscription fee,

running on your own computer.

### Case 3: Voice Commands and Voice Responses

Send voice messages to Telegram, it converts with Whisper model, processes the task, generates voice response via ElevenLabs and sends back. Handles mixed Korean-English seamlessly. Contrasts with Siri still struggling with multilingual mixing.

## Clawdbot's Core Components

| Component | Role | Characteristics |
| --- | --- | --- |
| **Gateway** | Control hub connecting to messaging apps | Runs 24/7 as launchd/systemd daemon |
| **Agent** | LLM agent performing actual tasks | Model selectable (Claude, GPT, Gemini, etc.) |
| **Skills** | Feature expansion modules | Community-provided or custom-created |
| **Memory** | Stores conversation history and user preferences | Saved locally as markdown files |
| **Channels** | Supported messaging platforms | WhatsApp, Telegram, Discord, Slack, Signal, iMessage, etc. |

## Installation Method

Clawdbot runs on macOS, Windows (WSL2 recommended), Linux. Node.js 22 or higher required.

**Step 1: Installation**

```
# One-line installation (recommended)
curl -fsSL https://clawd.bot/install.sh | bash

# Or install via npm
npm install -g clawdbot
```

**Step 2: Onboarding**

```
clawdbot onboard --install-daemon
```

The onboarding wizard walks through LLM provider selection (Anthropic, OpenAI, Google, etc.), messaging channel connection, basic skill setup.

**Step 3: Connect Messaging App**

For Telegram connection example, get bot token from BotFather and input to Clawdbot settings. Then messages sent to the bot on Telegram are answered by Clawdbot running on your computer.

## Cautions and Limitations

Clawdbot is powerful but still an "early adopter" project. A few things to know:

First, **API costs**. Clawdbot uses your chosen LLM provider's API. MacStories editor disclosed consuming 180 million tokens in a week. Significant costs possible at Claude Opus rates. To reduce costs, use lighter models like GPT-4o-mini or Claude Haiku, or leverage local models (MiniMax, Ollama).

Second, **security considerations**. Clawdbot has broad access to your computer. Email, file, terminal command execution capability means convenience and risk. Use only on trusted networks and

set DM policy to "pairing" mode to restrict access to authorized users.

Third, **technical entry barrier**. Installation is simple for npm and CLI-savvy people, but still challenging for non-developers.

However, beta macOS menu bar app is available, gradually improving accessibility.

## Conclusion

- Clawdbot is not just another chatting AI but a 24/7 resident agent that actually performs tasks on your computer.
- Open source with all settings and memory stored as local markdown files for complete transparency and customization.
- You can issue commands and receive results from existing messaging apps like WhatsApp and Telegram without needing separate apps, using your AI assistant from anywhere.

Practical tip: If you have a Mac mini or spare laptop, set it up as dedicated Clawdbot server.

Separating from your main work computer lets you experiment safely.

## References

- Clawdbot Official Website (https://clawd.bot/)
- Clawdbot GitHub Repository (https://github.com/clawdbot/clawdbot)
- Clawdbot Official Documentation (https://docs.clawd.bot/getting-started)
- MacStories - "Clawdbot Showed Me What the Future of Personal AI Assistants Looks Like" (https://www.macstories.net/stories/clawdbot-showed-me-what-the-future-of-personal-ai-assistants-looks-like/)
- ClawdHub - Community Skill Repository (https://clawdhub.com)
