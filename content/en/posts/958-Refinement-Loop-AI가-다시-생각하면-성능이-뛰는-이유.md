---
title: "Refinement Loop: Why AI Performance Surges When It Thinks Again"
date: 2026-01-03T01:31:11+09:00
slug: "958-Refinement-Loop-AI가-다시-생각하면-성능이-뛰는-이유"
original_url: "https://memoryhub.tistory.com/958"
tistory_id: 958
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
---

```
    ╔════════════════════════════════════════════════════╗
    ║                                                    ║
    ║     ┌──────────┐                                  ║
    ║     │  INPUT   │                                  ║
    ║     └────┬─────┘                                  ║
    ║          │                                        ║
    ║          ▼                                        ║
    ║     ┌──────────┐      ┌──────────┐               ║
    ║     │ GENERATE │ ───► │  OUTPUT  │               ║
    ║     └──────────┘      └────┬─────┘               ║
    ║          ▲                 │                      ║
    ║          │                 ▼                      ║
    ║     ┌────┴─────┐      ┌──────────┐               ║
    ║     │  REFINE  │◄─────│ FEEDBACK │               ║
    ║     └──────────┘      └──────────┘               ║
    ║                                                    ║
    ║           R E F I N E M E N T                     ║
    ║                 L O O P                            ║
    ╚════════════════════════════════════════════════════╝
```

When writing emails, few people send the first draft. We draft, reread, fix awkward parts. Programmers do the same—write code, run it, fix errors. Yet we never gave AI this opportunity. We expected perfect answers from single questions. **Refinement Loop is a technique giving AI the chance to "revise."** This simple idea became the core driver of 2025 AI reasoning advances.

In short, Refinement Loop improves performance from 5% to 40% without additional training by having LLMs evaluate and iteratively refine their own outputs.

## Background

The ARC Prize team officially named 2025 the "Year of the Refinement Loop." For good reason. Most major breakthroughs in AI reasoning this year came from this technique.

> Refinement Loop: A technique where AI generates output, the same model evaluates it, and improves based on feedback, repeating the cycle.

Traditional LLM usage was simple: input question, get answer. Called "single-pass" mode. The problem: LLMs often don't produce optimal answers on the first try. Especially for complex reasoning, multi-step problems, and tasks satisfying multiple constraints simultaneously.

A 2023 Carnegie Mellon team's Self-Refine paper offered solutions. The key insight is clear: show LLMs their own output and ask "how's this?" They find problems themselves. Tell them to fix based on feedback, and they produce better results.

## Refinement Loop's Three-Stage Structure

Refinement Loop has three key stages.

**Stage 1: Generate**

Present the problem to the LLM and receive initial answers. This matches existing methods. The key difference: don't accept this answer as final.

**Stage 2: Feedback**

Show the same LLM (or different one) the initial answer and request evaluation. Not "good/bad" but specific, actionable feedback. Specify what's wrong, where to fix, and why.

**Stage 3: Refine**

Modify the answer based on feedback. The refined answer can return to Feedback stage. The process continues until quality criteria are met or max iterations reached.

```
┌─────────────────────────────────────────────────────────┐
│                    REFINEMENT LOOP                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   Input ──► [GENERATE] ──► Output_0                    │
│                               │                         │
│                               ▼                         │
│                         [FEEDBACK]                      │
│              "This code lacks exception handling"       │
│                               │                         │
│                               ▼                         │
│                          [REFINE]                       │
│                               │                         │
│                               ▼                         │
│                          Output_1                       │
│                               │                         │
│                    ┌──────────┴──────────┐             │
│                    │  Quality criteria   │             │
│                    │  satisfied?         │             │
│                    └──────────┬──────────┘             │
│                         Yes   │   No                    │
│                          ▼    │    ▼                    │
│                       [DONE]  └──► [FEEDBACK]           │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

## Why It Works

Trying multiple times independently differs fundamentally from Refinement Loop. Sampling—trying independently and picking the best—means each attempt learns nothing from previous ones. Refinement Loop derives specific improvement directions from previous failures.

A key phenomenon observed in Self-Refine research: 71% of initial Python code in math reasoning tasks omitted return statements. Despite explicit instructions. But in the feedback phase, LLMs pinpointed this problem exactly, achieving 19% error reduction in the refinement stage. Accuracy jumped from 22.1% to 59.0%.

**From information theory, refinement itself is intelligence.** Using the ARC Prize team's words, gradually transforming one program into another while approaching goals is the essence of reasoning.

## Actual Performance Improvement Numbers

Results from Self-Refine research measuring seven diverse tasks:

| Task Type | Initial Score | After 3 Iterations | Improvement |
| --- | --- | --- | --- |
| Code Optimization | 22.0 | 28.8 | +31% |
| Sentiment Reversal | 33.9 | 36.8 | +9% |
| Math Reasoning | 22.1% | 59.0% | +167% |
| Constraint Generation | Baseline | +20%+ | Significant |

Poetiq's case is more dramatic. On ARC-AGI-2 benchmark, wrapping Gemini 3 Pro's baseline 31% performance with Refinement Loop boosted it to 54%. Cost dropped from $77 to $31. Achieved without modifying the model at all.

## Poetiq's Implementation: Adding Self-Auditing

Poetiq added an important concept to basic Refinement Loop: Self-Auditing.

Basic Refinement Loop's problem: deciding when to stop. Infinite repetition only increases cost. Poetiq's system judges itself: "Is this good enough?" When satisfied, it terminates without further iteration.

Poetiq's two principles summarize to:

First, **prompts are interfaces, not intelligence.** Instead of expecting perfect answers from single questions, build answers gradually through iterative problem-solving loops.

Second, **self-auditing is key to cost efficiency.** The system monitors its own progress and judges when sufficient information and satisfactory solutions are reached.

## Implementation Pattern

Pseudo code expressing Refinement Loop's basic structure:

```
def refinement_loop(prompt: str, max_iterations: int = 3) -> str:
    # Stage 1: Generate initial output
    output = llm.generate(prompt)

    for i in range(max_iterations):
        # Stage 2: Generate feedback
        feedback = llm.generate(
            f"Evaluate this output and suggest specific improvements:\n{output}"
        )

        # Check termination condition
        if is_satisfactory(feedback):
            break

        # Stage 3: Improve based on feedback
        output = llm.generate(
            f"Improve the output reflecting feedback:\n"
            f"Current output: {output}\n"
            f"Feedback: {feedback}"
        )

    return output
```

The key is feedback quality. Not "good/bad" but specifically what's wrong and how to fix it. This is called "actionable feedback."

## Application Cautions

| Situation | Recommendation | Reason |
| --- | --- | --- |
| Simple Fact Questions | Maintain Single Pass | Iteration is unnecessary overhead |
| Complex Reasoning | Apply Refinement Loop | Significant performance gains |
| Verifiable Tasks | Highly Recommended | Easier feedback quality assurance |
| Subjective Tasks | Use Caution | Difficult termination condition setting |

Refinement Loop isn't suitable for all situations. Self-Refine research shows this technique heavily depends on foundational model capabilities. GPT-4 plus Self-Refine yields far better results than GPT-3.5 plus Self-Refine. The effect is more pronounced for tasks where feedback is verifiable (code execution, math verification, etc.).

## Conclusion

- Refinement Loop gives LLMs the chance to "think again," achieving 5-40% performance gains without additional training.
- Core structure is repeated Generate → Feedback → Refine cycles, with actionable feedback as success key.
- With ARC Prize naming 2025 the "Year of Refinement Loop," it's the core paradigm of current AI reasoning advances.

Practical tip: For LLM applications requiring complex reasoning, replace single calls with Refinement Loops. Reference Poetiq's open-source code or Self-Refine patterns for rapid implementation.

## References

- Self-Refine: Iterative Refinement with Self-Feedback, arXiv (https://arxiv.org/abs/2303.17651)
- Self-Refine Official Page (https://selfrefine.info/)
- ARC Prize 2025 Results and Analysis (https://arcprize.org/blog/arc-prize-2025-results-analysis)
- Poetiq: Traversing the Frontier of Superintelligence (https://poetiq.ai/posts/arcagi_announcement/)
- Poetiq ARC-AGI Solver GitHub (https://github.com/poetiq-ai/poetiq-arc-agi-solver)
