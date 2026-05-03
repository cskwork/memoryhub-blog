---
title: "AI Can Remember Too, Google Titans Transforms the Long-Term Memory Paradigm"
date: 2025-12-06T14:51:17+09:00
slug: "919-AI도-기억-한다-Google-Titans가-바꾸는-장기-기억의-패러다임"
original_url: "https://memoryhub.tistory.com/919"
tistory_id: 919
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
---

```
  ╔══════════════════════════════════════════════════════════════╗
  ║                                                              ║
  ║     ┌─────────────────────────────────────────────────┐      ║
  ║     │  SHORT-TERM        LONG-TERM        PERSISTENT  │      ║
  ║     │  ┌───────┐        ┌───────┐        ┌───────┐   │      ║
  ║     │  │ATTEN- │   +    │NEURAL │   +    │FIXED  │   │      ║
  ║     │  │ TION  │        │MEMORY │        │WEIGHTS│   │      ║
  ║     │  └───┬───┘        └───┬───┘        └───────┘   │      ║
  ║     │      │                │                        │      ║
  ║     │      └───────┬────────┘                        │      ║
  ║     │              ▼                                 │      ║
  ║     │        ╔═══════════╗                           │      ║
  ║     │        ║  TITANS   ║  ← Surprise Metric        │      ║
  ║     │        ║   +       ║  ← 2M+ Tokens             │      ║
  ║     │        ║  MIRAS    ║  ← Real-time Learning     │      ║
  ║     │        ╚═══════════╝                           │      ║
  ║     └─────────────────────────────────────────────────┘      ║
  ║                                                              ║
  ║              AI  LONG-TERM  MEMORY  ARCHITECTURE             ║
  ╚══════════════════════════════════════════════════════════════╝
```

Haven't you ever felt frustrated by the contextual limits of what Transformers can handle? AI that forgets the beginning while summarizing a long document, chatbots that lose the initial context as conversations grow longer. All these problems stem from the fact that **AI had no true long-term memory**. Google Research's Titans and MIRAS, announced at the end of 2024 and officially introduced at NeurIPS in December 2025, directly tackle this issue. **An architecture that combines RNN speed and Transformer accuracy while handling ultra-long contexts exceeding 2 million tokens has arrived.**

**Summary:** In short, Titans is a next-generation architecture that applies neuroscience principles—where AI selectively remembers only "surprising information"—to overcome the contextual limitations of existing Transformers.

## Background

Most current LLMs use the Transformer architecture. Since Google published "Attention is All You Need" in 2017, the Attention mechanism became the core technology of the AI revolution. However, there's a fatal weakness: it has **O(n²) computational complexity** relative to sequence length.

What does this mean? When input tokens double, computation quadruples; when they increase tenfold, computation increases hundredfold. That's why most LLMs have context window limitations and struggle to process long documents or entire books at once. Models like Mamba and recent RNN variants attempted to solve this problem, but by compressing information into fixed-size vectors, **important details get lost**.

| Architecture | Advantages | Limitations |
| --- | --- | --- |
| Transformer | Accurate dependency modeling | O(n²) complexity, context limits |
| RNN/SSM (Mamba) | Linear scaling, fast inference | Fixed-size compression, information loss |
| Titans | Combines both advantages | New architecture, still under validation |

## Core Concepts

> One-line definition: Titans is an AI architecture that separates short-term memory (Attention) from long-term memory (Neural Memory Module), selectively storing only "surprising information" like the human brain.

Think of human memory systems. We quickly forget our daily commute routes, but we vividly remember a sudden accident or an unexpected gift. **"Surprising" information—what defies expectations—gets stored in long-term memory.** Titans applies this principle directly to AI.

**How the Surprise Metric Works**

Titans' core innovation is the "surprise metric." It measures the difference between the state currently remembered by the model and newly incoming input. When that difference (gradient) is large, it judges "this is unexpected and important" and stores it in long-term memory.

For example, while reading a financial report, if a "banana peel" image suddenly appears, the surprise value spikes. In contrast, when words like "revenue" or "sales" appear in the financial report, they're within expectations, so the surprise value stays low. This **selective memory maximizes storage efficiency**.

**Three Architecture Variants**

Titans offers three variants depending on how long-term memory is integrated.

First, **Memory as Context (MAC)** works like a personal assistant whispering past meeting notes. A summary of long-term memory is provided as additional context to what's currently being processed.

Second, **Memory as Gate (MAG)** is like two advisors working simultaneously. Short-term and long-term memory outputs are combined through a gating mechanism.

Third, **Memory as Layer (MAL)** integrates memory directly as a network layer, inserting a long-term memory layer into existing neural network structures.

**MIRAS: Unified Theoretical Framework**

If Titans is a tool, MIRAS is the blueprint. Google researchers argue that all sequence models—from Transformers to RNNs to SSMs—are actually different ways of solving a single problem: **"associative memory."**

MIRAS decomposes sequence models into four design choices:

- **Memory architecture**: The structure for storing information (vector, matrix, deep neural network)
- **Attentional bias**: Internal learning objectives the model optimizes for
- **Retention gate**: Forgetting mechanism (a form of regularization)
- **Memory algorithm**: Optimization algorithm used for memory updates

Through this framework, beyond the limitations of traditional MSE-based approaches, new attention-free models like YAAD, MONETA, and MEMORA have emerged.

## Performance Validation

Titans' performance has been validated across various benchmarks. The most impressive results came from the **BABILong benchmark**, a test requiring reasoning across information distributed over millions of tokens—an extreme long-context task.

| Model | Parameters | BABILong Performance |
| --- | --- | --- |
| GPT-4 | Hundreds of billions (estimated) | Baseline |
| Llama-3 + RAG | Tens of billions | Below GPT-4 |
| Titans (MAC-FT) | 760 million | **Exceeds GPT-4** |

It's noteworthy that Titans surpassed GPT-4 despite having far fewer parameters. Researchers revealed that Titans can be extended to **context windows exceeding 2 million tokens** while maintaining reasonable memory costs.

On language modeling (C4, WikiText) and common-sense reasoning (HellaSwag, PIQA) tasks, Titans consistently outperformed recent models like Mamba-2, Gated DeltaNet, and Transformer++. Ablation studies also showed that the deeper the memory module, the lower the perplexity, with less performance degradation even as sequence length increases.

## Potential Applications

Titans architecture can be applied across a wide range of domains.

For **document understanding and analysis**, it can process hundred-page legal documents or medical papers at once and precisely locate specific clauses or research findings. This solves at the architecture level what previously required RAG (Retrieval-Augmented Generation) workarounds.

In **genomic analysis**, it can model data like DNA sequences consisting of millions of base pairs. Researchers actually tested Titans on genomic tasks, validating its effectiveness beyond text domains.

The **time series forecasting** domain can benefit from long-term pattern memory. Financial or weather data analysis can leverage anomalous patterns from the past and apply them to similar situations.

| Application Domain | Expected Effect |
| --- | --- |
| Legal/Medical Document Analysis | Process entire documents without RAG |
| Genomic Research | Model millions of base-pair sequences |
| Long-Context Conversational AI | Fully maintain conversation context from beginning |
| Time Series Forecasting | Enhanced long-term pattern learning |

## Final Thoughts

- Titans applies the human brain's "surprise-based memory" principle to AI, enabling processing of ultra-long contexts exceeding 2 million tokens
- The MIRAS framework provides a unified view of Transformers, RNNs, and SSMs, offering the theoretical foundation for next-generation sequence model design
- This research heralds a shift from the old "fixed after pre-training" AI paradigm to "learning and remembering in real-time" AI

Practical tip: This technology will likely be incorporated into Google's Gemini or open-source Gemma models, so if you're preparing projects requiring long-context processing, keep an eye on follow-up Titans research and model release announcements.

## References

- Titans + MIRAS: Helping AI have long-term memory - Google Research Blog (https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/)
- Titans: Learning to Memorize at Test Time - arXiv (https://arxiv.org/abs/2501.00663)
- MIRAS: A Unified Framework for Sequence Modeling - arXiv (https://arxiv.org/pdf/2504.13173)
- Google's Titans Architecture: Key Concepts Explained - DataCamp (https://www.datacamp.com/blog/titans-architecture)
