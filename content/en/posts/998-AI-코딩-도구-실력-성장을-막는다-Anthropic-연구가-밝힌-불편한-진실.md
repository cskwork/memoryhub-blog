---
title: "Can AI Coding Tools Prevent Skill Growth? The Uncomfortable Truth Revealed by Anthropic Research"
date: 2026-02-02T23:43:07+09:00
slug: "998-AI-코딩-도구-실력-성장을-막는다-Anthropic-연구가-밝힌-불편한-진실"
original_url: "https://memoryhub.tistory.com/998"
tistory_id: 998
draft: false
---

```
    ┌─────────────────────────────────────────┐
    │                                         │
    │    AI + Developer = ?                   │
    │                                         │
    │    ┌─────┐      ┌─────┐                │
    │    │ ?  │  →   │ ?  │  Productivity UP│
    │    └─────┘      └─────┘                │
    │        │                                │
    │        ↓                                │
    │    ┌─────┐                              │
    │    │ ?  │  Skill?                      │
    │    └─────┘                              │
    │                                         │
    │   "HOW you use AI matters"              │
    │                                         │
    └─────────────────────────────────────────┘
```

Using AI coding tools makes work finish faster. But then anxiety creeps in. "If I keep relying on AI like this, won't I get dumber?" Most of us have experienced the illusion of understanding that comes from just looking at answer keys during test prep. In a controlled experiment with 52 real developers, Anthropic found that **the group receiving AI assistance scored 17% lower on comprehension tests compared to the group that coded directly.** However, not all AI users received low scores.

**TL;DR:** The bottom line is that AI doesn't prevent skill growth—how you use AI determines whether learning happens at all.

---

## Background

The productivity benefits of AI coding tools have already been proven in multiple studies. In Anthropic's observational research, AI was confirmed to reduce time on specific tasks by up to 80%. The problem lies elsewhere.

Existing research shows that when people receive AI assistance, their work engagement decreases and they reduce their own cognitive effort.

This is called **Cognitive Offloading**—basically "outsourcing your thinking to AI."

> Cognitive Offloading: The phenomenon of delegating cognitive work that should be done by oneself to external tools or systems

What happens when this phenomenon intensifies? Code becomes increasingly automated, but humans still need to catch errors in AI-generated code, set direction, and maintain oversight in high-risk environments.

Doesn't AI provide a shortcut while making that shortcut bypass skill development altogether?

To answer this question, the Anthropic research team designed a randomized controlled trial.

---

## Research Design

52 junior software developers participated. All had used Python for over a year at least once per week and were somewhat familiar with AI coding tools. There was one critical requirement.

They had never used the Trio library (for asynchronous programming) before.

The experimental structure was as follows:

| Phase | Content |
| --- | --- |
| Warm-up | Basic coding environment adaptation |
| Main Task | Implement two features using Trio |
| Evaluation | Quiz on the code just written |

Half the participants could use an AI assistant (access code in sidebar, generate solution code on request),

while the other half coded entirely by hand.

The important point is that participants were told in advance that "there will be a quiz," but simultaneously were encouraged to "work as fast as possible."

This design mimicked the time pressure of real work environments.

The evaluation measured four competencies:

| Competency Type | Measured Content | Importance in AI Era |
| --- | --- | --- |
| Debugging | Identifying and diagnosing code errors | Essential for detecting AI-generated code errors |
| Code Reading | Understanding what code does | Foundation for AI code validation |
| Code Writing | Choosing correct approaches | System design capability |
| Concept Understanding | Grasping core principles of tools/libraries | Essential for appropriate design pattern decisions |

The research team weighted debugging, code reading, and concept understanding particularly heavily.

They determined these three were most important for overseeing AI-generated code.

---

## Key Results

Let's look at the numbers first.

| Metric | AI Group | Direct Coding Group | Difference |
| --- | --- | --- | --- |
| Average Quiz Score | 50% | 67% | -17%p |
| Task Completion Time | ~2 min faster | Baseline | No statistical significance |

The AI group received lower scores on the quiz representing nearly a two-grade difference (Cohen's d=0.738, p=0.01).

The largest score gap was in **debugging**.

Participants who coded without AI assistance encountered more errors, and improving their debugging skills through directly solving those errors appears to explain the difference.

Interestingly, regarding work speed, the AI group was about 2 minutes faster on average, but this difference was not statistically significant.

The research team interpreted this as: AI increases productivity on repetitive or familiar tasks,

while its effect is limited when learning new technologies.

---

## AI Usage Pattern Analysis

The research team analyzed screen recordings to classify how participants interacted with AI. There was a surprising finding.

Some participants spent 11 minutes—30% of total task time—writing conversations with AI, sending up to 15 queries.

### Low-Score Patterns (Average below 40%)

| Pattern | Characteristics | Result |
| --- | --- | --- |
| Full Delegation | Entire code writing delegated to AI | Fastest, almost no errors, no learning |
| Progressive Dependence | Started with 1-2 questions, gradually full delegation | Struggled with second task concepts |
| Repetitive Debugging | Relied on AI for debugging/validation | Many questions but problem-solving without understanding |

The common point across all three patterns is clear: AI was used as a "tool that thinks for you."

### High-Score Patterns (Average 65% or above)

| Pattern | Characteristics | Result |
| --- | --- | --- |
| Generate then Understand | Code generation → follow-up questions to grasp principles | Normal speed, high comprehension |
| Hybrid Approach | Request both code and explanations | Takes longer but has learning effect |
| Concept Question Only | Ask about concepts, write code directly | Encounter many errors, solve directly, fastest among high scorers |

The common point in high-score patterns is equally clear: AI was used as a "tool to aid understanding."

In particular, the **Concept Question Only** pattern encountered many errors but solved them directly,

and as a result, was nearly as fast as the full delegation pattern while showing the highest comprehension.

---

## Best Practice Comparison

| Approach | Advantages | Cautions |
| --- | --- | --- |
| Ask concepts → code directly | Highest learning effect, reasonable speed | Requires determination to overcome early errors |
| Generate code + request explanation | Balances speed and learning | Explanation must actually be read and understood for effect |
| Generate then follow-up questions | Looks similar to full delegation but different results | Must ask "why does this work this way" |
| Full AI delegation | Fastest | Almost no learning effect, debugging skills decline |

The core difference is one thing: **"Whether you received code" is not what matters—"whether you pursued understanding" is.**

---

## Implications

The questions this research raises apply to both organizations and individuals.

**From an organizational perspective**, actively adopting AI coding tools can boost short-term productivity. However, if junior developers have fewer opportunities to acquire skills, they may later lack the competence to validate AI-generated code.

Managers should intentionally consider systems or designs that promote learning when deploying AI tools.

**From an individual perspective**, this research demonstrates the value of deliberate skill development. Cognitive effort—even the painful experience of being stuck—can be important to mastery. Major AI services already provide learning modes.

Claude Code's Learning and Explanatory mode and ChatGPT's Study Mode are examples.

One caveat: this research addressed a situation where participants were **learning new technology**. This doesn't contradict results showing AI greatly boosts productivity when working with existing skills (up to 80% time reduction).

The implication is that AI may increase productivity in familiar areas while potentially hindering learning in new ones.

---

## Closing Thoughts

- Using AI coding tools may lower comprehension by 17%, but results differ based on usage approach.
- The difference between "receiving code" and "understanding it" determines your skill growth trajectory.
- Debugging skills improve most effectively when you directly experience and solve errors.

**Practical tip:** Starting today, when you ask AI for code, follow up with "Explain why this works this way."

---

## References

- How AI Impacts Skill Formation, Anthropic Research (<https://www.anthropic.com/news/ai-skill-formation>)
- Full Paper: arXiv:2601.20245
