---
title: "Claude Skills: How to Get Started (They Might Matter More Than MCP)"
date: 2025-10-18T01:29:50+09:00
slug: "858-MCP보다-더-중요할-수도-있는-Claude-Skills-어떻게-시작할까"
original_url: "https://memoryhub.tistory.com/858"
tistory_id: 858
draft: false
categories: ["Dev Library"]
tags: ["Claude"]
cover:
  image: "/images/858-MCP보다-더-중요할-수도-있는-Claude-Skills-어떻게-시작할까/img.png"
  relative: false
  hidden: false
---

![](/images/858-MCP보다-더-중요할-수도-있는-Claude-Skills-어떻게-시작할까/img.png)

When I heard Claude Skills launched, I immediately found the official documentation. After reading it, my first thought? "This looks interesting... but how am I actually supposed to use it?"

Have you had that experience? Every time a new AI tool launches, you see "revolutionary," "game-changer" everywhere, but find nothing about "what can I actually do tomorrow?"

So I spent the last 2 days trying it myself and exploring what people are saying. I found things worth sharing.

## What exactly are Claude Skills?

Let me skip the complicated explanations and describe it as simply as possible:

**One folder + a few Markdown files = Skills**

That's really it. Unlike MCP (Model Context Protocol) which loads tens of thousands of tokens upfront, Skills only use tens of tokens at startup. Additional content loads only when needed.

The structure looks like:

- Markdown files: Instructions and descriptions
- YAML files: Configuration
- Optionally: Scripts or additional tools

Works in Claude app, Claude Code, and via API.

## Why does it matter?

Simon Willison (famous developer) said: "This might be even bigger than MCP."

At first it seemed like hype, but after using it, I understood why.

**Real example:**

- For me: Made repetitive code review work into a Skill, so I don't have to use the same prompt every time

The key is **simplicity**. MCP is powerful but setup is complex. Skills? Just a few Markdown files and you're done.

## How to start right now

### Step 1: Pick one repetitive task (5 minutes)

Weekly reports, code reviews, meeting notes, newsletter ideas... anything works.

### Step 2: Create a simple Skill (10 minutes)

Create one folder and write a `skill.md` file:

```
# Weekly Report Assistant

You're an expert at organizing weekly work into concise reports.

## How you work
1. Listen to last week's work
2. Extract 3 key achievements
3. Organize next week's plan
4. Format into clean report
```

That's it.

### Step 3: Connect to Claude and try it (5 minutes)

Specify the Skill folder in Claude app or Claude Code and it's ready to use.

## What to know

**Pros:**

- Really easy setup
- Uses only as much context as needed
- Works everywhere with same format
- Version control possible (just files)

**Cautions:**

- Still early stage (2 days into launch)
- Security: Check what permissions Skills request
- When using someone else's Skill, read the code first

Security especially matters. Skills can have file access or command execution permissions, so it's good to verify trusted sources.

## Why timing matters

Honestly, there's almost no practical guidance yet. Just official docs and conceptual explanations, not much "I tried this and it worked" real-world experience.

**Which means if you start now:**

- You can join the early community
- Build useful Skills before everyone else
- Even if you stumble, everyone's at the same stage

I'm still experimenting too. Failing, rebuilding, that's normal.

## Things worth trying this week

1. **Find one repetitive task**: The one you do most often that's most boring
2. **Build your first Skill**: 10 minutes, doesn't need to be perfect
3. **Use it and iterate**: Try it once or twice and you'll see what to fix
4. **Find others' experiences**: Search #ClaudeSkills on Twitter, Reddit

Don't try to build a perfect Skill. Just build one and actually use it. Mine was terrible the first time. By the third iteration, it got useful.

---

**Action points:**

• Today: Pick one repetitive task (write it down)  
• This week: Create a simple Skill (10-15 minutes is enough)  
• Next week: Use it and improve (doesn't need to be perfect)  
• Share questions or experiences in comments

Starting is half the battle. Don't overthink it. Start small.
