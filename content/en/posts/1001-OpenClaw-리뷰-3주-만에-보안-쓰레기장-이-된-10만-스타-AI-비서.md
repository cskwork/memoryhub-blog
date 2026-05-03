---
title: "🔓 OpenClaw Review: The 100k-Star AI Assistant That Became a 'Security Dumpster Fire' in 3 Weeks"
date: 2026-02-04T02:26:18+09:00
slug: "1001-OpenClaw-리뷰-3주-만에-보안-쓰레기장-이-된-10만-스타-AI-비서"
original_url: "https://memoryhub.tistory.com/1001"
tistory_id: 1001
draft: false
---

```
  ╔═══════════════════════════════════════════════════════════╗
  ║                                                           ║
  ║     ██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗██╗       ║
  ║    ██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║       ║
  ║    ██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║     ██║       ║
  ║    ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║     ██║       ║
  ║    ╚██████╔╝██║     ███████╗██║ ╚████║╚██████╗███████╗  ║
  ║     ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝  ║
  ║                     A W                                  ║
  ║               🤖 AI Assistant 🤖                         ║
  ║                                                           ║
  ║        [ The Good, The Bad, and The Malware ]            ║
  ║                                                           ║
  ╚═══════════════════════════════════════════════════════════╝
```

"I want to have a free AI assistant that works 24/7." You've probably thought about it at least once. OpenClaw seemed like it would make that dream a reality. An AI assistant that takes orders via Telegram, does work on its own, and organizes your emails while you sleep.

But why did the VP of Security at Google Cloud warn people to **"absolutely not install it"**?

**TL;DR:** In short, OpenClaw shows the future of personal AI assistants, but

it's difficult to recommend to average users due to monthly API costs of $300-750 and serious security vulnerabilities.

## Background

In November 2025, Clawdbot, a weekend project by iOS developer Peter Steinberger, shook the tech industry in early 2026. It hit 100,000 GitHub stars in just 3 weeks, and even caused Mac mini shortages.

But problems emerged just as rapidly as the explosive popularity.

> OpenClaw is an open-source autonomous AI agent that runs on a user's computer and is controlled through messaging apps.

Think of Jarvis from the Iron Man movies for easy understanding. Like saying "Jarvis, organize my schedule today" and having AI take care of it, OpenClaw can be commanded through Telegram or WhatsApp to actually manipulate the computer and perform tasks.

Unlike existing ChatGPT or Claude, which only "chat,"

OpenClaw "takes action directly." File organization, email sending, and code execution are all possible.

The problem is that this powerful authority is a double-edged sword.

## Why the Name Changed Three Times

The naming history of OpenClaw itself shows the chaotic state of this project.

| Period | Name | Reason for Change |
| --- | --- | --- |
| November 2025 | Clawdbot | Initial launch |
| Mid-January 2026 | Moltbot | Trademark request from Anthropic (confusion with Claude) |
| Late January 2026 | OpenClaw | Awkward pronunciation and brand cleanup |

"Clawd" was too similar to "Claude," so Anthropic raised objections, forcing a quick change to Moltbot.

"Molt" meant when lobsters shed their shells, but the pronunciation was awkward. Eventually, OpenClaw was decided as the final name.

**This is where the security problems begin.** In the confusion of name changes, scammers registered unregistered domains and social media accounts, and

fake malicious extensions appeared.

## Advantages: Why Developers Were Excited

The reason OpenClaw got attention is clear.

First, it's completely open source. With an MIT license, anyone can freely modify and distribute it. The ability to operate it directly without monthly subscription fees is appealing.

Second, it integrates with messaging platforms. Without installing a separate app, you can control AI through Telegram, WhatsApp, Discord, Slack, and even KakaoTalk—messengers you already use.

Third, real automation is possible. If you send a message saying "check my calendar and make a dentist appointment for next week," it actually checks your calendar and attempts to make the appointment. Work that required jumping between multiple apps can now be handled in a single conversation.

A GeekNews user put it this way:

> "You can dynamically generate skills, schedule repetitive and one-time tasks, and it's a persistent agent with remote messaging capability, so it truly feels like a real assistant."

## Drawback 1: API Cost Explosion

OpenClaw itself is free. But the AI model that powers it is not.

MacStories' Federico Viticci consumed 180 million tokens in the first month. That's about 4.8 million won by Claude Sonnet pricing. Another user had an automation loop run wild and spent **$200 a day (about 27,000 won)**.

The crux of the problem lies in how OpenClaw works.

It repeats attempt-failure-fix-retry cycles until the task is complete, consuming tokens with each attempt.

According to The Register, one developer's simple "heartbeat" task that just checks the time consumed 120,000 tokens every 30 minutes, billing $20 overnight.

## Drawback 2: Security Nightmare

On January 27, 2026, security research firm Aikido discovered a malicious extension called "ClawdBot Agent" on the VS Code Marketplace.

This fake extension ran automatically at VS Code startup and downloaded malicious code.

As a result, attackers could gain remote access to developers' computers.

**The key is that OpenClaw has no official VS Code extension.** Attackers simply exploited the project's popularity and the absence of official tools.

And this was just the beginning.

As of February 3, 2026, here's the list of security issues compiled by The Register.

| Vulnerability | Severity | Status |
| --- | --- | --- |
| CVE-2026-25253: One-click remote code execution | CVSS 8.8 (High) | Patched |
| 341 malicious ClawHub skills discovered | High | Mostly unremoved |
| 2 command injection vulnerabilities | High | Patched |
| Moltbook database exposure | Medium | Under mitigation |

The one-click RCE vulnerability discovered by security researcher Mav Levin was particularly severe.

The attack completes in "milliseconds" if the victim visits a malicious webpage just once.

The problem was caused by failing to validate the origin header in WebSocket connections.

Heather Adkins, VP of Security at Google Cloud, publicly warned:

> "Don't run OpenClaw. This is information-stealing malware disguised as an AI personal assistant."

Additionally, according to SecurityAffairs, between January 27 and February 2, 2026, **over 400 malicious skills** were uploaded to ClawHub and GitHub. While disguised as cryptocurrency trading automation tools,

they were actually malware stealing passwords and cryptocurrency keys from Windows and macOS.

## What Are Safe Alternatives?

The common opinion in Reddit and Hacker News communities is surprisingly simple.

**"Simpler tools cover 99% of use cases."**

| Alternative | Advantages | Best for |
| --- | --- | --- |
| Claude Code + Telegram integration | No complex setup needed, stable | Developers, professionals |
| Kimi K2.5 (local model) | Zero API costs, keeps data local | Privacy-conscious users |
| Existing automation tools (Zapier, n8n) | Proven security, rich integrations | Non-developers |

## Should You Install It Now?

At this point, it's difficult to recommend OpenClaw to most users.

The technical vision is impressive. The concept of a personal AI assistant controlled through messaging apps is certainly forward-looking.

But current risks outweigh the benefits.

**If you still want to try it**, you need to meet these conditions:

1. You're a developer with security knowledge and understand the risks
2. You can set hard limits on API keys
3. You have a separate device for testing (don't use your main PC)
4. Install only from the official GitHub repository, and thoroughly verify ClawHub skills

Project maintainers acknowledge security issues and are working on improvements. It might be wise to check again in 6 months.

## Conclusion

- OpenClaw presented an innovative concept of an "action-taking AI assistant," but within 3 weeks earned the assessment of a "security dumpster fire" due to security vulnerabilities and malware distribution.
- Monthly API costs of $3,000-10,000, one-click RCE vulnerabilities, and over 400 malicious skills mean current risks outweigh the benefits.
- Practical tip: Start with Claude Code or verified automation tools instead of OpenClaw, and reassess in 6 months when security stabilizes.

## References

- OpenClaw - Wikipedia (https://en.wikipedia.org/wiki/OpenClaw)
- OpenClaw Bug Enables One-Click Remote Code Execution via Malicious Link - The Hacker News (https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html)
- DIY AI bot farm OpenClaw is a security 'dumpster fire' - The Register (https://www.theregister.com/2026/02/03/openclaw_security_problems/)
- MoltBot Skills exploited to distribute 400+ malware packages - SecurityAffairs (https://securityaffairs.com/187562/malware/moltbot-skills-exploited-to-distribute-400-malware-packages-in-days.html)
- From Clawdbot to OpenClaw: When Automation Becomes a Digital Backdoor - Vectra AI (https://www.vectra.ai/blog/clawdbot-to-moltbot-to-openclaw-when-automation-becomes-a-digital-backdoor)
- OpenClaw - Personal AI Assistant for All OS and Platforms - GeekNews (https://news.hada.io/topic?id=26122)
- OpenClaw (Formerly Clawdbot): The Good, The Bad, and The Malware - Everyday AI (https://everydayaiblog.com/openclaw-moltbot-ai-assistant-review/)
