---
title: "? Theory of Mind Prompting, Making AI Understand 'Me'"
date: 2025-12-17T20:25:05+09:00
slug: "932-Theory-of-Mind-프롬프팅-AI가-나-를-이해하게-만드는-법"
original_url: "https://memoryhub.tistory.com/932"
tistory_id: 932
draft: false
---

```
    ╔══════════════════════════════════════╗
    ║     ?  THEORY OF MIND  ?             ║
    ║  ┌─────────┐      ┌─────────┐       ║
    ║  │  USER   │ ───▶ │   LLM   │       ║
    ║  │ Context │      │ Perspect│       ║
    ║  └─────────┘      └─────────┘       ║
    ║   "What I know"  →  "Personalized"   ║
    ╚══════════════════════════════════════╝
```

"No matter how well I write prompts, the AI doesn't understand my intent." Clear instructions yield wrong answers, explaining context gets the details wrong. The problem is that AI knows *what* to do, but fails to grasp *what you know*, *why you want it*.

**Bottom line: When you tell an AI "who I am, what I know, and what I want," response quality improves by 29% or more.**

## Background

Theory of Mind (ToM) originated in psychology. It refers to the human cognitive ability to infer mental states of others—their beliefs, desires, intentions. A six-year-old understands "Sam thinks candy is in the drawer, but mom actually moved it."

> **Theory of Mind**: The ability to infer and understand mental states (beliefs, intentions, knowledge) of oneself and others

ToM's meaning in LLM prompting is slightly different.

**Here, the key is making the LLM properly understand the user's context, knowledge level, and intent.**

At ACL 2024, Carnegie Mellon researchers presented SimToM, applying this principle to prompting. Results were striking: **+29.5% accuracy improvement** over conventional Chain-of-Thought. GPT-4 achieved 100% accuracy on some tests with proper ToM prompting.

The core principle is simple. When you have an LLM **"clarify what this person knows and doesn't know first,"** answers become precise.

## Core Technique: SimToM 2-Step Prompting

SimToM's structure mimics how humans understand others. "If I were in their shoes..." — that's perspective shift.

**Step 1 - Perspective Shift**: Filter only information known to a specific subject.

**Step 2 - Answer**: Respond using only filtered information.

LLMs struggle processing all information simultaneously. But when you break it into "extract only what this person knows," accuracy shoots up.

## Practice: 3 Key Examples

### Example 1: Basic SimToM Structure

The classic False Belief Test best demonstrates ToM principles.

**Scenario**

```
Noor is a barista. A customer requested oat milk.
Noor filled the pitcher with oat milk.
A coworker secretly switched it to almond milk.
Noor saw the coworker switch it.

Question: What does Noor believe is in the pitcher?
```

**Standard Prompting**

```
Read the scenario and answer the question.
```

→ Many LLMs incorrectly answer "oat milk," missing "Noor saw it."

**SimToM Prompting**

```
[Step 1] 
From Noor's perspective, list only events Noor directly experienced or witnessed.

[Step 2] 
Based solely on Noor's knowledge from Step 1,
what does Noor believe is in the pitcher?
```

**Result**: Step 1 explicitly clarifies "Noor witnessed the coworker switching milk," and the answer is precisely "almond milk."

Why the difference? LLMs tend to process all information from an "omniscient viewpoint." Step 1 forces extraction of only one perspective's information, so Step 2 yields answers faithful to that perspective.

---

### Example 2: Communicating User Context (Making LLM Understand 'Me')

Most practically applicable pattern. Telling the LLM "who I am."

**Scenario**: Requesting code review, wanting feedback tailored to my skill level.

**Standard Prompting**

```
Review this Python code.
[code]
```

→ LLM doesn't know your level, so feedback mixes overly basic and overly advanced suggestions.

**ToM Applied Prompting**

```
[What I know]
- 3 years using Python, backend development experience
- Familiar with async processing (asyncio)
- Using type hints

[What I'm not familiar with]
- Memory optimization, profiling
- C extension modules

[This code's context]
- Planned for production deployment
- Must handle 1,000 requests per second

[Request]
Review the code considering the above context.
Briefly cover what I already know,
focus in detail on memory/performance issues I might miss.
```

**Result**: LLM skips basic async syntax explanations and concentrates feedback on memory leaks or GC issues—"things I don't know."

The key is **explicitly distinguishing "what's known / unknown."** Just following this structure transforms answer quality.

---

### Example 3: Multi-Perspective Simulation

Useful for predicting stakeholder reactions or practicing negotiations.

**Scenario**: Want to predict diverse stakeholder reactions to a new feature proposal.

**Standard Prompting**

```
Give feedback on this proposal.
[Proposal: Add cryptocurrency payment option to system]
```

→ Generic, vague feedback.

**ToM Applied Prompting**

```
Read the proposal and analyze from each stakeholder perspective.

[Proposal]
Add cryptocurrency payment option to payment system

---
[CFO Perspective Simulation]
What this person knows:
- Company financial status, ROI criteria
- Cryptocurrency price volatility

What this person doesn't know:
- Technical implementation difficulty
- Young customer demographic crypto usage rate

→ What questions and concerns arise from this perspective?

---
[Engineering Lead Perspective Simulation]
What this person knows:
- Current payment system architecture
- Team resource situation

What this person doesn't know:
- Current cryptocurrency regulations
- Marketing impact forecast

→ What technical concerns would they raise?
```

**Result**: Since each role's "knowns" and "unknowns" differ, realistic, specific simulation emerges. CFO raises ROI questions, engineering lead raises implementation complexity concerns.

This pattern applies directly to negotiation practice, presentation prep, and stakeholder analysis.

## Best Practices and Pattern Comparison

| Prompting Technique | Advantages | Considerations |
| --- | --- | --- |
| Zero-Shot | Simple | Low accuracy on ToM tasks |
| Chain-of-Thought | Effective for complex reasoning | Limited improvement on ToM |
| SimToM (2-step) | 29%+ ToM accuracy gain | Longer prompts |
| Context Clarification (know/don't know) | Easy real-world application | Requires pre-planning |

The simplest ToM trigger is adding **"and why?"** to questions. "What does Sam believe is in the bag?" versus "What does Sam believe is in the bag? **Why does he believe that?**" yields more accurate answers. Explaining "why" requires the LLM to infer the person's knowledge state.

## Conclusion

- The core of ToM prompting is making the LLM understand **"what this person (or I) know and don't know"**
- SimToM's 2-step structure (perspective filtering → answer) delivers 29%+ accuracy gains on ToM tasks
- In practice, just adding **[Know] / [Don't Know] / [Goal]** structure to prompts shows results

**Practical tip: Add "I know ~ and am unfamiliar with ~" to your next prompt. The LLM will match your level.**

## References

- Think Twice: Perspective-Taking Improves Large Language Models' Theory-of-Mind Capabilities, ACL 2024 (<https://arxiv.org/abs/2311.10227>)
- Boosting Theory-of-Mind Performance in Large Language Models via Prompting (<https://arxiv.org/abs/2304.11490>)
- A Survey of Theory of Mind in Large Language Models, 2025 (<https://arxiv.org/html/2502.06470>)
- In Theory of Mind Tests, AI Beats Humans - IEEE Spectrum (<https://spectrum.ieee.org/theory-of-mind-ai>)
