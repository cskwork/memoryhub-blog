---
title: "Why Did Karpathy's CLAUDE.md Get 48,000 Stars?"
date: 2026-04-17T01:53:46+09:00
slug: "1055-Karpathy의-고찰이-담긴-CLAUDE-md-왜-별-4만-8천-개를-찍었을까"
original_url: "https://memoryhub.tistory.com/1055"
tistory_id: 1055
draft: false
cover:
  image: "images/1055-Karpathy%EC%9D%98-%EA%B3%A0%EC%B0%B0%EC%9D%B4-%EB%8B%B4%EA%B8%B4-CLAUDE-md-%EC%99%9C-%EB%B3%84-4%EB%A7%8C-8%EC%B2%9C-%EA%B0%9C%EB%A5%BC-%EC%B0%8D%EC%97%88%EC%9D%84%EA%B9%8C/ChatGPT%20Image%202026%EB%85%84%204%EC%9B%94%2026%EC%9D%BC%20%EC%98%A4%ED%9B%84%2001_54_04.png"
  relative: false
  hidden: false
---

# 

![](/images/1055-Karpathy%EC%9D%98-%EA%B3%A0%EC%B0%B0%EC%9D%B4-%EB%8B%B4%EA%B8%B4-CLAUDE-md-%EC%99%9C-%EB%B3%84-4%EB%A7%8C-8%EC%B2%9C-%EA%B0%9C%EB%A5%BC-%EC%B0%8D%EC%97%88%EC%9D%84%EA%B9%8C/ChatGPT%20Image%202026%EB%85%84%204%EC%9B%94%2026%EC%9D%BC%20%EC%98%A4%ED%9B%84%2001_54_04.png)

You've probably experienced this at some point: asking Claude Code to "just fix one function," only to have five entire files get rewritten.

Andrej Karpathy vented about this exact frustration on Twitter, and when one developer distilled that observation into a single 70-line `CLAUDE.md` file, it accumulated over 48,000 stars in just a few weeks.

By the end of this article, you'll understand what this file is, what principles it contains, and how to attach it to your own project.

## One-Line Summary

A 70-line `CLAUDE.md` based on Karpathy's LLM coding observations can noticeably reduce Claude Code's over-editing, unfounded assumptions, and scope creep.

## Why It's Trending Now

On January 26, 2026, Andrej Karpathy posted on X (formerly Twitter) identifying three chronic problems with LLM coding tools:

- Unfounded assumptions — it invents context without verification
- Over-engineering — it adds abstractions and options that weren't requested
- Scope creep — it "improves" code it shouldn't even touch

The next day, developer Forrest Chang translated this into a one-page behavior guideline called `CLAUDE.md` and released it publicly. By April 2026, the repository had accumulated 48,309 stars—an unusual case where a single-file repository outpaced thousands of contributors to popular open-source projects.

| Term | Meaning |
| --- | --- |
| CLAUDE.md | A project rules file that Claude Code automatically reads at session start |
| Claude Code | Anthropic's officially distributed CLI coding assistant |
| Plugin marketplace | A distribution channel in Claude Code for sharing rule and agent packages |

## The Four Principles at a Glance

> One-line definition: A system prompt that teaches LLMs to "pause, reduce, narrow, and verify" like a developer using four key principles.
> The core is embedding constraints, not adding new features.

- **Think Before Coding** — Expose assumptions and stop to ask if things are unclear ("Don't assume. Don't hide confusion.").
- **Simplicity First** — Forbid features beyond the request, abstractions, or defensive code. If a 200-line solution can be 50 lines, rewrite it.
- **Surgical Changes** — Only change the lines that need changing, and clean up only imports made unused by your changes.
- **Goal-Driven Execution** — Convert vague directives like "add validation" into verifiable goals like "write tests for invalid inputs, then make them pass."

Here's how the Goal-Driven principle looks in transformation when using Claude Code CLI v1.x:

```
# Vague directive → Verifiable goal
"Add input validation" → "Write tests for invalid inputs first, then make them pass"
"Fix the bug"      → "Write a test that reproduces it, then make it pass"
"Refactor X"       → "Verify all existing tests pass before and after refactoring"
```

## Three Steps to Attach to Your Project

#### ① Choose Your Method

You have two options: install as a plugin or download the original file directly. Use the plugin approach for multiple projects; file copying works better for a single project.

#### ② Plugin Method (Recommended)

Enter the following two lines in sequence in Claude Code CLI:

```
# Claude Code CLI v1.x
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

Success looks like: `Installed karpathy-skills plugin. CLAUDE.md rules are now active in this project.`

#### ③ Direct File Merge Method

If your project root already has a `CLAUDE.md`, download the original and append it:

```
curl -fsSL https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md \
  >> ./CLAUDE.md
```

After applying, open a new Claude Code session and confirm the rules are loaded by checking for a `CLAUDE.md loaded` message at the session top.

## Which Method Is Best?

| Method | Pros | Notes |
| --- | --- | --- |
| Plugin install | Apply to multiple projects at once, updates reflect automatically | All teammates need same marketplace access, may conflict with internal policy |
| Direct file merge | Free to customize per project, works offline | Must manually track source updates, need to check for duplication with existing rules |
| Partial principles only | Minimize conflicts with team conventions | Interconnected principles like Surgical Changes lose effectiveness in partial application |

## Closing Thoughts

The lesson proven by 48,000 stars is simple: LLM coding tools don't need more features—they need clearer constraints.

Attach this single file to your project root this evening, and starting tomorrow, you'll notice Claude Code's over-editing fatigue drop significantly.

## References

- forrestchang/andrej-karpathy-skills repository — <https://github.com/forrestchang/andrej-karpathy-skills>
- CLAUDE.md original text — <https://github.com/forrestchang/andrej-karpathy-skills/blob/main/CLAUDE.md>
- antigravity.codes, "Karpathy's CLAUDE.md Skills File: The Complete Guide" — <https://antigravity.codes/blog/karpathy-claude-code-skills-guide>
- explainx.ai, "Karpathy-inspired Claude Code guidelines" — <https://explainx.ai/blog/karpathy-claude-code-guidelines-andrej-karpathy-skills>
- DEV Community, "Karpathy's CLAUDE.md Template: 5,800 Stars and What It Does" — <https://dev.to/max_quimby/karpathys-claudemd-template-5800-stars-and-what-it-does-4a09>
