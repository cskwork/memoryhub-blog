---
title: "Claude Skills, Teaching AI Your Work Style"
date: 2026-01-20T14:15:00+09:00
slug: "982-Claude-Skills-AI한테-내-업무-스타일-을-기억시키는-방법"
original_url: "https://memoryhub.tistory.com/982"
tistory_id: 982
draft: false
---

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     ? SKILLS                                                ║
║                                                              ║
║     ┌─────────────────────────────────────────────┐          ║
║     │  ? Work Manual                             │          ║
║     │  ├── How to Write Reports                  │          ║
║     │  ├── Presentation Format                   │          ║
║     │  └── Email Templates                       │          ║
║     └─────────────────────────────────────────────┘          ║
║                        ↓                                     ║
║              [ Claude Learns ]                               ║
║                        ↓                                     ║
║              ? Works "My Way"                                ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

You asked "make a report" but got different formats each time. To get the style you want, you have to give long explanations again. Using

AI, haven't you experienced this at least once?

Claude Skills, announced by Anthropic in October 2025, solves exactly this problem.

**Teach AI "how I work" just once, and it automatically follows that method thereafter.**

It's like giving a new employee an operations manual.

**One-line summary:** In short, Claude Skills is a feature that automates repetitive AI tasks "my way."

---

## Background

### Why Was Skills Needed?

As people leveraged AI for work, many encountered the same problem. They had to copy and paste the same prompt every time. AI didn't remember "do it like last time." Different team members requested different things from AI, resulting in inconsistent outputs.

> **What are Skills?** An "operations manual folder" that teaches AI how to perform specific tasks.

Easy analogy:

When you give a new employee a manual saying "use this format for reports, this tone for emails, this template for presentations,"

you get consistent results without explaining each time.

Claude Skills serves exactly that manual role.

---

## How Skills Differ From Regular Prompts

Many people think "isn't it enough to write good prompts?"

The core difference is **reusability** and **automatic application.**

| Aspect | Regular Prompt | Claude Skills |
| --- | --- | --- |
| Usage | Enter manually each time | Set once, auto-applied |
| Scope | Valid only in that conversation | Applied to all related tasks |
| Sharing | Copy-paste text | Shareable across team |
| Complex Work | Requires long prompt | Organized in folder structure |

For example, without Skills, requesting a report prompts Claude to write in a generic way.

But with Skills, Claude checks the preset manual for the same request and writes precisely in the format and style you specified.

---

## How Skills Work

To explain how Skills operate with an everyday analogy:

**First, retrieve only when needed.** Companies don't keep all manuals open while working.

They find the relevant manual only when that task arises. Claude is the same.

It scans the list of available Skills and retrieves only what matches the current task.

**Second, combine multiple Skills.** What if you say "organize data in Excel then create presentation in PowerPoint"?

Claude uses the Excel Skill and PowerPoint Skill sequentially.

It's like referencing operation manuals from different departments to complete a collaborative project.

**Third, it works the same everywhere.** A Skill created on the web works identically in the app and API.

Once created, you can use it anywhere.

---

## What Tasks Can You Use It For?

Anthropic's built-in Skills alone enable quite diverse work.

**Document work is the primary example.** You can write Word documents matching company formats or

generate Excel workbooks with formulas.

You can create PowerPoint slides reflecting brand guidelines, and

automatically fill PDF forms.

**It's also effective for automating repetitive tasks.** You can write weekly reports in the same format consistently or

respond to customer inquiries with consistent tone. Organizing meeting notes in standard templates is also possible.

In fact, Japanese Rakuten introduced Skills and announced they cut **work that took a day in financial management to just 1 hour.**

---

## How to Use Skills: Getting Started in 3 Steps

You can use Skills directly in Claude's web app without development knowledge.

### ① Enable Skills Feature

First, go to Settings in Claude's website or app. Find the Features tab in Settings and activate the Skills option. Note that it's available on Pro, Max, Team, and Enterprise plans; free users aren't supported yet.

### ② Try Built-in Skills

Some Skills work immediately without special setup. Type "make a PowerPoint on Q3 performance" and Claude automatically retrieves the pptx Skill to generate the presentation. "Create an Excel file from this data" works the same way.

### ③ Create Your Own Skill

If there's a task you do frequently, you can create your own Skill. Enable the skill-creator feature and tell Claude "I want to create a new Skill." Claude will ask questions to understand your work method and construct the Skill for you.

For example, if you say "I want to create a Skill for weekly reports," Claude asks what format, what content to include, what tone to use. It creates a completed Skill based on your answers.

---

## Points to Note

Skills are powerful but have some considerations.

**They have code execution permissions.**

Some Skills can actually execute code. Therefore, use Skills only from trusted sources.

Adding Skills from unknown sources indiscriminately creates security risks.

**It's better not to make it too complex from the start.** Start with simple tasks and create Skills,

then gradually add features if they work well.

It's recommended to divide by function rather than putting multiple features in one Skill.

---

## Conclusion

- Claude Skills teach AI "your way" to get consistent results
- No need to copy-paste the same prompt every time; set once and it auto-applies
- Activate in Settings on Pro+ plans and start using immediately

**Practical tip:** Think of the task you repeat most frequently today and ask Claude "create a Skill for this task."

---

## References

- Introducing Agent Skills (<https://claude.com/blog/skills>)
- Claude Skills Official Documentation (<https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview>)
- Claude Skills Usage Guide (<https://support.claude.com/en/articles/12512180-using-skills-in-claude>)
- Example Skills Collection - GitHub (<https://github.com/anthropics/skills>)
