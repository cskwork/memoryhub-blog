---
title: "Poetiq AI: How It Achieved World 1st in ARC-AGI-2 Without Model Training"
date: 2026-01-03T01:10:21+09:00
slug: "956-Poetiq-AI-모델-훈련-없이-ARC-AGI-2-세계-1위-달성한-비결"
original_url: "https://memoryhub.tistory.com/956"
tistory_id: 956
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
---

```
    ╔═══════════════════════════════════════════╗
    ║                                           ║
    ║     ┌─────────┐      ┌─────────┐         ║
    ║     │   LLM   │ ───► │ Answer  │         ║
    ║     └─────────┘      └────┬────┘         ║
    ║           ▲               │              ║
    ║           │    Refinement │              ║
    ║           │      Loop     ▼              ║
    ║     ┌─────┴─────┐   ┌─────────┐         ║
    ║     │  Analyze  │◄──│Feedback │         ║
    ║     └───────────┘   └─────────┘         ║
    ║                                           ║
    ║         P O E T I Q   A I                ║
    ║     Recursive Self-Improvement           ║
    ╚═══════════════════════════════════════════╝
```

"Better AI requires bigger models, more data, longer training." That formula we accepted as gospel. Yet in December 2025, a small six-person team from Google DeepMind flipped this formula on its head. Without modifying a single line of code, simply layering a system on top of existing LLMs, they set a new ARC-AGI-2 benchmark world record.

**The paradigm shift: "Prompts are interfaces, not intelligence. Real intelligence comes from iterative refinement loops."**

In short, Poetiq wrapped LLMs in a "meta-system" without retraining them, increasing accuracy 20% over previous records while cutting costs 60%.

## Background

ARC-AGI is a reasoning benchmark created by AI researcher Francois Chollet in 2019. Designed to measure "real reasoning" rather than simple pattern recognition. Early 2025, even state-of-the-art models scored below 5% on ARC-AGI-2. Compare that to 60% human average.

> ARC-AGI: A benchmark measuring the ability to infer and apply new rules. Designed to be unsolvable through memorization or pattern matching.

Existing performance improvement approaches have fundamental limits. Reinforcement learning (RL) post-processing requires millions of data points and works only for domains like coding and math with abundant synthetic data. Model retraining costs astronomical time and resources. This was a "rich person's game" only large AI companies could attempt.

Poetiq asked a completely different question: "If the answers already exist in the LLM, isn't there a way to extract them better?"

## Poetiq's Core Principle: Refinement Loop

Poetiq's founders compare LLMs to vast libraries containing most digitized human knowledge, yet with books scattered without organization. A simple question (prompt) retrieves one relevant book. But solving complex problems requires combining information from multiple books, grasping context, and inferring missing pieces.

Poetiq created a kind of "super librarian" system. This system goes through repeated processes:

| Step | Task | Role |
| --- | --- | --- |
| 1. Question | Present problem to LLM | Generate initial answer |
| 2. Feedback | Validate answer and analyze errors | Identify improvements |
| 3. Analysis | Modify strategy based on feedback | Determine next direction |
| 4. Re-question | Retry with improved approach | Gradually approach correct answer |

**This cycle repeats until the correct answer is found.** The key insight: "Prompts are interfaces, not intelligence." Instead of expecting perfect answers from single questions, it assembles scattered knowledge fragments in LLMs through iterative conversation.

## Results and Significance

December 7, 2025, the ARC Prize team officially verified Poetiq's results. Achieving 54% on the Semi-Private Test Set, far ahead of previous leader Gemini 3 Deep Think's 45%. More striking: cost. At $30.57 per problem versus Gemini 3 Deep Think's $77.16—60% cheaper.

| System | Accuracy | Cost per Problem |
| --- | --- | --- |
| Poetiq (Gemini 3 Pro) | 54% | $30.57 |
| Gemini 3 Deep Think | 45% | $77.16 |
| Claude Opus 4.5 (Thinking) | 37.6% | $2.20 |

Combined with GPT-5.2 X-High, it achieved 75% on Public Eval—the first time exceeding human average 60%. Cost dropped below $8 per problem.

The implications are clear: **Model size isn't the only answer.** The ARC Prize team named 2025 the "Year of the Refinement Loop." Foundational model knowledge is essential, but actual progress happens "in application layers that validate and improve outputs."

## Comparison with Existing Approaches

| Approach | Advantages | Cautions |
| --- | --- | --- |
| Model Retraining | Fundamental improvement | Astronomical cost, takes months |
| RL Post-processing | Domain optimization | Millions of data needed, biased toward coding/math |
| Refinement Loop (Poetiq) | Leverage existing models, low-cost, fast deployment | Requires domain-specific verifiers |

Poetiq's approach doesn't solve everything. Current refinement systems are domain-specialized. However, researchers argue that with verifiers capable of generating feedback signals, it's broadly scalable.

## Direct Experimentation

Poetiq released ARC-AGI solver code as open-source. Full code available in GitHub, runnable with Gemini 3 or GPT models.

Three things are needed: Python environment, API keys for chosen LLMs (Gemini, OpenAI, etc.), and .env file configuration. Adjust problem sets and settings in main.py, then run. Default settings follow the Poetiq 3 config from the blog.

## Conclusion

- Poetiq achieved world 1st in ARC-AGI-2 via a meta-system layered "on top" without modifying LLMs.
- The core principle: Refinement Loop—iterative answer generation, feedback, analysis, and retry.
- This shows AI progress is shifting from "model scaling" to "system design."

Practical tip: Download Poetiq's open-source code and apply the Refinement Loop to your problem domain. Directly verify whether reasoning performance improves without model training.

## References

- Poetiq Official Website (https://poetiq.ai/)
- Poetiq ARC-AGI Solver GitHub (https://github.com/poetiq-ai/poetiq-arc-agi-solver)
- ARC Prize 2025 Results and Analysis (https://arcprize.org/blog/arc-prize-2025-results-analysis)
- TechTalks: Beyond raw intelligence - How Poetiq cracked ARC-AGI-2 (https://bdtechtalks.com/2025/12/09/poetiq-arc-agi-2-solution/)
