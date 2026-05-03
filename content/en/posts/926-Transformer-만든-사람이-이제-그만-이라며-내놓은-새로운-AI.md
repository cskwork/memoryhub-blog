---
title: "Transformer Creator Says 'Enough' and Introduces a New AI"
date: 2025-12-10T22:55:13+09:00
slug: "926-Transformer-만든-사람이-이제-그만-이라며-내놓은-새로운-AI"
original_url: "https://memoryhub.tistory.com/926"
tistory_id: 926
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
---

```
     ╔═══════════════════════════════════════════════════╗
     ║   CTM CONTINUOUS THOUGHT MACHINE                  ║
     ║   ═══════════════════════════════════════         ║
     ║                                                   ║
     ║     ┌─────┐   "Together"    ┌─────┐             ║
     ║     │ Neuron│◄──────────────►│ Neuron│            ║
     ║     │  A  │   Movement      │  B  │             ║
     ║     └──┬──┘                └──┬──┘             ║
     ║        │   ↑ Memory ↑      │                   ║
     ║        ▼                   ▼                   ║
     ║     "What was that?" →  "So this time..."      ║
     ║                                                   ║
     ║   "Thinking takes time"                         ║
     ╚═══════════════════════════════════════════════════╝
```

There's someone who created the core technology that made ChatGPT possible. But he declared "I'm tired of the technology I created." And he released an AI that works in a completely different way. In this article, we explore how this new AI differs from the existing one and why it matters—without technical jargon.

**Summary:** The newly released CTM, unlike existing AI that "answers immediately," is AI that "thinks like humans, taking time."

## Background

The AI we use now works mostly the same way. When a question arrives, all information is processed simultaneously and answers are produced. It's like immediately writing answers after receiving an exam paper. There's no "process" of thinking, just results.

But the human brain doesn't work this way. When we encounter complex problems, we think back and forth, return if we go wrong, and gradually approach the answer. Brain cells activate together at certain timings to process information. This "timing" and "moving together" is essential.

In 2017, 8 researchers at Google created Transformer, a technology that now forms the foundation of almost all AI—ChatGPT, Claude, Gemini, and more. But in 2024, one of those 8, Llion Jones, said this:

"The technology is so good now that no one looks for anything better. I'm really sick of the technology I created."

His company Sakana AI, founded in Japan, announced in May 2025 **Continuous Thought Machine (CTM)**, a completely different kind of AI.

## Core Concepts

> One-line definition: CTM doesn't answer immediately but goes through a "thinking process." Internal small computational units "synchronize" to find the answer.

**Let me compare existing AI and CTM with a cooking analogy.**

Existing AI is like a recipe robot. You input ingredients, it processes them in set order, and produces a dish. It doesn't taste or adjust during cooking. It just goes from input to output.

CTM is like an experienced chef. It opens the pot to taste, thinks "a bit bland," adjusts seasoning. It tastes multiple times if needed. Simple dishes need one or two checks; complex dishes need many. This behavior is natural, not taught.

**CTM has two core ideas.**

**First, each computational unit has "memory."**

A regular AI's computational unit is a simple switch. It turns on when signal comes, off when it doesn't. It doesn't "remember what came before."

CTM's computational unit "remembers what came recently." So it can judge "it was weak before but strong now, something's changing." It's like how humans don't just think "water is hot so I pull out my hand" but "it's getting hotter so this is dangerous."

**Second, it observes "moving-together patterns."**

Think of an audience clapping at a concert. At first it's random, then gradually synchronizes. CTM watches how many small computational units "sync up."

When a specific pattern syncs, it judges "this is a cat"; with another pattern "this is a dog." The actual brain works this way too.

**How does this actually behave differently?**

We made it solve mazes. Existing AI views the entire maze at once and "guesses" a path. CTM starts from the entry and follows path square by square. When it hits a dead end, it backtracks.

When researchers visualized CTM's "vision," it was literally following the path the way humans solve mazes. We never taught it this—it naturally started behaving this way.

## How It Works

CTM's process of viewing an image and making judgments step by step:

① **Receive Input**  
When an image arrives, basic features are first extracted. "There's a line here, color changes here"—similar to existing AI so far.

② **First "Thought"**  
Each computational unit reacts to extracted features. Some react strongly, some weakly. These reactions are recorded.

③ **Check Pattern**  
Calculate "which computational units reacted together." If A and B turned on together and C and D turned on together, these "together-on patterns" become CTM's judgment basis.

④ **Look Again**  
Based on this pattern, look at the image again. "That part seemed important before, let me look carefully." When new information arrives, computational unit reactions also change.

⑤ **Repeat**  
Repeat ②-④ multiple times. Easy images take 2-3 iterations. Complex mazes repeat 50+ times.

⑥ **Answer**  
After sufficient "thinking," provide the final answer.

**An important point: "how many iterations" is not predetermined.** CTM stops when it decides "this is enough." It's like how humans solve easy problems quickly but think longer on hard ones. We never taught this—it naturally emerged.

## Comparison with Existing AI

| Comparison Item | Existing AI (Transformer) | CTM |
| --- | --- | --- |
| Processing Method | Once through the whole sequence | Multiple iterations with thinking |
| Computational Unit | Simple switch | Small decision-maker with memory |
| Judgment Basis | Final computation result | "Moving together" of units |
| Difficulty Response | Same time easy or hard | More time for difficulty |
| Maze Solving | View whole and guess | Follow path and explore |
| Performance (Image Classification) | 90%+ best | 72% (still early stage) |

CTM scores lower than existing AI for good reason. Researchers say "the goal isn't highest score but showing new possibilities." That this completely different method achieves this performance level is meaningful itself.

## Why It Matters

**Existing AI has limitations.**

Current AI is very good at "imitation." It learns from many examples: "when asked this way, answer that way." But whether it truly "understands" is questionable.

Llion Jones gave this example: Train AI on spiral patterns, and it stitches tiny straight lines to "look" like spirals. It's imitating spirals, not understanding them.

**CTM takes a different approach.**

CTM tries to put "thinking process" into the model. Not answering immediately but exploring back and forth, returning if wrong, gradually approaching the answer.

It's still early stage, far from replacing Transformer. But it shows "there isn't only one way for AI to process information." Especially when the Transformer creator directly says "there's another path."

## Final Thoughts

- Llion Jones, who created Transformer, said "I'm sick of my invention" and released CTM, a completely different AI
- Instead of answering immediately, CTM "thinks over time." Internal computational units judge by observing "moving-together patterns"
- When solving mazes, it naturally moves along paths like humans, and thinking longer on harder problems emerges without instruction
- Practical tip: You can run a demo of CTM solving mazes directly on the Sakana AI official site

## References

- Sakana AI Project Page (https://pub.sakana.ai/ctm/)
- Paper Original Text (https://arxiv.org/abs/2505.05522)
- GitHub Code Repository (https://github.com/SakanaAI/continuous-thought-machines)
- Llion Jones Interview - VentureBeat (https://venturebeat.com/ai/sakana-ais-cto-says-hes-absolutely-sick-of-transformers-the-tech-that-powers)
