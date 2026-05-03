---
title: "MiniMax M2.5: Claude Opus-Level Coding AI at 1/10 Price in 108 Days"
date: 2026-02-13T06:16:42+09:00
slug: "1019-MiniMax-M2-5-108일-만에-Claude-Opus급-코딩-AI를-1-10-가격에-내놓다"
original_url: "https://memoryhub.tistory.com/1019"
tistory_id: 1019
draft: false
cover:
  image: "/images/1019-MiniMax-M2-5-108일-만에-Claude-Opus급-코딩-AI를-1-10-가격에-내놓다/img.png"
  relative: false
  hidden: false
---

![](/images/1019-MiniMax-M2-5-108일-만에-Claude-Opus급-코딩-AI를-1-10-가격에-내놓다/img.png)

Using frontier AI models means accepting expensive API costs. Most developers have accepted this as given.

But on February 12, 2026, Shanghai-based AI startup MiniMax flipped this formula on its head with a released model.

SWE-Bench Verified 80.2%, 37% faster task completion, while costing 1/10 to 1/20 of competing models.

**MiniMax M2.5 marks the beginning of a new paradigm: "frontier AI without cost concerns."**

**TLDR:** Bottom line: MiniMax M2.5 achieved three generations of evolution in 108 days, reaching Claude Opus-level coding/agent performance while realizing a revolutionary cost structure of ~$1 per hour.

## Background

The AI coding agent market underwent dramatic changes from late 2025. Claude Opus 4.5 first broke 80% on SWE-Bench Verified, setting new "frontier coding model" standards, with GPT-5 series and Gemini 3 Pro following close behind. The problem was the cost of these top-tier models. Running complex agent workflows 24/7 quickly accumulates token costs.

MiniMax precisely targeted this gap.

> MiniMax is a Shanghai-based AI startup founded by engineers from Chinese AI company SenseTime in 2021, going public on the Hong Kong Stock Exchange in January 2026.

The company name itself comes from game theory's "minimax algorithm," meaning finding optimal solutions even in worst-case scenarios.

Backed by Alibaba, Tencent, and miHoYo (Genshin Impact developer), it operates multimodal products including Hailuo AI (video generation), Talkie (AI character chat), and Speech (voice synthesis). A latecomer in text models, it began aggressive catching up starting with M2 in October 2025.

## M2 Series: 108 Days of Evolution

To understand M2.5, first examine the entire M2 series evolution. Three major updates occurred in just 108 days, each with clear objectives.

**M2 (October 2025)** focused on solving "cost and accessibility" problems. Adopted an MoE (Mixture of Experts) structure with 230B total parameters but only 10B active. Local deployment possible with just 4 H100s, offering aggressive pricing: $0.3/1M input tokens, $1.2/1M output tokens. Achieved 69.4% on SWE-Bench Verified, establishing competitive footing among open-source models.

**M2.1 (December 2025)** focused on "actual performance on complex tasks." Moved beyond Python bias to achieve balanced performance across 10+ languages including Rust, Java, Go, C++. Optimized for stable operation across various coding agent frameworks: Claude Code, Droid, Cline. Pulled SWE-Bench Verified to ~77%, approaching Claude Sonnet 4.5.

**M2.5 (February 12, 2026)** launched with goal of achieving SOTA (state-of-the-art) in coding, agent tool use, search, and general office work.

| Metric | M2 | M2.1 | M2.5 |
| --- | --- | --- | --- |
| SWE-Bench Verified | 69.4% | ~77% | 80.2% |
| Multi-SWE-Bench | - | improved | 51.3% (#1) |
| BrowseComp | 44.0% | improved | 76.3% |
| Task Completion Speed | baseline | baseline | 37% faster vs M2.1 |

In 108 days, SWE-Bench Verified climbed ~11%p.

MiniMax claims this evolution speed is fastest versus Claude, GPT, Gemini series.

## M2.5's Core Capabilities

### Coding: "Think Like an Architect, Build Like One"

M2.5 isn't just a bug-fix tool because it covers the complete development lifecycle. MiniMax explains step-by-step:

Zero-to-one system design and environment setup, one-to-ten system development, ten-to-ninety iterative feature development, ninety-to-hundred code review and system testing. M2.5 shows reliable results throughout.

Notably, **"native spec behavior"** naturally emerged during reinforcement learning.

The model self-learned to decompose and plan functionality, structure, UI design from an architect's perspective before writing code.

Target platforms exceed web frontend demo level.

Handles multiplatform full-stack projects: Web, Android, iOS, Windows, Mac, plus server APIs, business logic, databases. Trained on 10+ programming languages (Go, C, C++, TypeScript, Rust, Kotlin, Python, Java, JS, PHP, Lua, Dart, Ruby) and hundreds of thousands of real-world environments.

Versatility across coding agent tools verified. Droid scores 79.7% (exceeding Opus 4.6's 78.9%), OpenCode 76.1% (exceeding Opus 4.6's 75.9%)—stable performance not dependent on specific frameworks.

### Search and Tool Use

For agents to autonomously handle complex tasks, web search and tool-calling ability are essential. M2.5 achieves 76.3% on BrowseComp, reaching top-tier in this domain.

MiniMax's proprietary RISE (Realistic Interactive Search Evaluation) benchmark is interesting.

Unlike typical search benchmarks, it's based on actual search tasks experts perform. Search queries are only part; it evaluates deep exploration within specialist webpages. M2.5 showed strong results on this benchmark.

Efficiency improvements: M2.5 reduced search round consumption by ~20% versus M2.1 while achieving better results.

Beyond just matching right answers, improved ability to reach results through more efficient paths.

### Office Work

A M2.5 differentiator is strengthening office scenarios through collaboration with active professionals in finance, law, social sciences.

Targeted deliverable-quality results in advanced office tasks: Word, PowerPoint, Excel financial modeling.

On proprietary framework GDPval-MM, achieved average 59.0% win rate comparing with mainstream models.

Shows the model expanding beyond pure coding into practical business document creation.

## Shocking Price Structure

M2.5's most shocking aspect is pricing. MiniMax offers two versions:

| Version | Processing Speed | Input Price (per 1M tokens) | Output Price (per 1M tokens) | Hourly Cost |
| --- | --- | --- | --- | --- |
| M2.5-Lightning | ~100 TPS | $0.3 | $2.4 | ~$1 |
| M2.5 (Standard) | ~50 TPS | $0.15 | $1.2 | ~$0.3 |

For context, M2.5-Lightning's 100 TPS is roughly 2x faster than current mainstream frontier models.

Output token pricing is 1/10 to 1/20 of Claude Opus, Gemini 3 Pro, GPT-5.

MiniMax explains more intuitively: "With $10,000, you can continuously run 4 M2.5 agents for an entire year."

This is attractive for enterprises needing sustained complex agent workflows.

## Speed's Secret: Forge and Large-Scale Reinforcement Learning

Behind M2.5's performance lies large-scale reinforcement learning. MiniMax conducted RL training on hundreds of thousands of real complex environments,

including company's own real work environments.

Core technology infrastructure is **Forge**, a proprietary Agent RL framework. Unlike existing RL frameworks, Forge introduces middle layers for complete decoupling of lower-level training/inference engines and agents. This enables optimizing any agent framework. Through asynchronous scheduling and tree-structured learning sample merging, achieved ~40x training acceleration.

Algorithmically uses CISPO to ensure large-scale MoE training stability. Introduced Process Reward mechanisms to solve credit assignment problems from agent scenarios' unique long contexts.

This monitors entire task progress, not just final results. Notably, directly estimated actual real-world task time and used as reward. Optimizes not just "correctness" but "speed and efficiency."

Result: M2.5 completes SWE-Bench Verified tasks averaging 22.8 minutes, 37% faster than M2.1's 31.3 minutes and nearly identical to Claude Opus 4.6's 22.9 minutes.

## Best Practices/Pattern Comparison

For practical M2.5 use, precisely understand positioning versus competing models:

| Model | SWE-Bench Verified | Price (per 1M output tokens) | Main Advantage | Caution |
| --- | --- | --- | --- | --- |
| MiniMax M2.5 | 80.2% | $1.2~$2.4 | Performance-to-price ratio, open-source, fast speed | High self-benchmark weight, independent validation needed |
| Claude Opus 4.5 | 80.9% | ~$15 | Top performance, validated stability | High cost |
| GPT-5 High | 88% (LiveBench) | Various | Reasoning strength | Variance across benchmarks |
| Gemini 3 Pro | 76.2% | ~$3.5 | Multimodal, 1M context | Relatively lower coding specialization |
| GLM-4.7 | 73.8% | ~$0.05/task | Strong open-source, very cheap | Limited agent versatility |

One caution: many M2.5 benchmark results are MiniMax internal tests.

Public benchmarks like SWE-Bench Verified allow external validation, but RISE, GDPval-MM, VIBE-Pro are proprietary.

Best practice: await independent community validation of new model claims before final judgment.

## Access Paths for Developers

Three main routes for using M2.5:

1. **API Access**: Immediate use via official MiniMax platform (platform.minimax.io). Provides Anthropic-compatible endpoint, so existing SDK integration is relatively straightforward.
2. **Coding Agent Frameworks**: Can specify M2.5 as backend model in major tools: Claude Code, Droid, OpenCode. MiniMax also operates separate "Coding Plan" pricing.
3. **Local Deployment**: M2 series available open-source (Modified-MIT license) with weights downloadable from HuggingFace. Supports inference frameworks: SGLang, vLLM, Transformers. M2.5 open-source timing TBD, but M2 and M2.1 already public.

Recommended parameters: temperature=1.0, top_p=0.95, top_k=40.

M2 series uses interleaved thinking, so maintaining assistant's thinking content in message history is important.

## Closing Thoughts

- MiniMax M2.5 underwent three generations of evolution in 108 days, achieving top-tier SWE-Bench Verified 80.2% coding performance, with Forge-based large-scale RL as core driver.
- However, high self-benchmark weight means awaiting community independent validation while testing directly in your workflow is most reliable.

Real-world tip: Try MiniMax API free trial, connect M2.5 as backend to your existing coding agent framework, then directly compare quality and cost on identical tasks.

## References

- MiniMax M2.5 Official Announcement (<https://www.minimax.io/news/minimax-m25>)
- MiniMax M2.1 HuggingFace (<https://huggingface.co/MiniMaxAI/MiniMax-M2.1>)
- MiniMax M2 GitHub (<https://github.com/MiniMax-AI/MiniMax-M2>)
- MiniMax Wikipedia (<https://en.wikipedia.org/wiki/MiniMax_(company)>)
- SWE-Bench Leaderboard (<https://swe-bench.com>)
- Artificial Analysis - MiniMax M2 Benchmarks (<https://artificialanalysis.ai/articles/minimax-m2-benchmarks-and-analysis>)
