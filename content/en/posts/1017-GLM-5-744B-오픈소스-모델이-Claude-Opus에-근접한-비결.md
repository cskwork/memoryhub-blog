---
title: "GLM-5: How a 744B Open Source Model Neared Claude Opus"
date: 2026-02-12T04:21:42+09:00
slug: "1017-GLM-5-744B-오픈소스-모델이-Claude-Opus에-근접한-비결"
original_url: "https://memoryhub.tistory.com/1017"
tistory_id: 1017
draft: false
cover:
  image: "images/1017-GLM-5-744B-%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4-%EB%AA%A8%EB%8D%B8%EC%9D%B4-Claude-Opus%EC%97%90-%EA%B7%BC%EC%A0%91%ED%95%9C-%EB%B9%84%EA%B2%B0/img.png"
  relative: false
  hidden: false
---

![](/images/1017-GLM-5-744B-%EC%98%A4%ED%94%88%EC%86%8C%EC%8A%A4-%EB%AA%A8%EB%8D%B8%EC%9D%B4-Claude-Opus%EC%97%90-%EA%B7%BC%EC%A0%91%ED%95%9C-%EB%B9%84%EA%B2%B0/img.png)

"Open source models can never catch up to closed ones." Until just a year ago, this was accepted wisdom.

But on February 11, 2026, Chinese AI startup Zhipu AI (Z.ai) unveiled GLM-5, directly challenging that assumption. On the SWE-bench coding benchmark, it showed only 3.1%p difference from Claude Opus 4.5, and on the BrowseComp agent benchmark, it actually leads by 25%p.

**An open-source 744B parameter model that essentially closed the gap with frontier models—this article explores the technical background and significance.**

**TLDR:** Bottom line: GLM-5 combines DeepSeek's sparse attention with its proprietary asynchronous reinforcement learning framework Slime, achieving frontier-model-level agent performance for the first time from an open-source model.

---

## Background

AI model generations are changing faster. In July 2025, GLM-4.5 with 355B parameters demonstrated the potential of "agent-native" models, and in January 2026, Zhipu AI went public on the Hong Kong stock exchange, raising about HK$43.5 billion (about 740 billion won).

This capital was directly invested in GLM-5 development.

But why does GLM-5 draw such attention? It's not just because parameter count grew. Three reasons stand out:

First, it absorbed DeepSeek's sparse attention (DSA) technology to dramatically lower deployment costs.

Second, its self-developed asynchronous reinforcement learning infrastructure Slime revolutionized post-training efficiency.

Third, it released under MIT license as completely open-source, usable commercially by anyone.

> One-line definition: GLM-5 is an open-source large language model with 744B total parameters but only 40B active parameters in an MoE (Mixture of Experts) structure, designed specifically for complex system engineering and long-horizon agent tasks.

---

## From GLM-4.5 to GLM-5: What Changed

To understand GLM-5's progress, examining specific differences from its predecessor:

|  | GLM-4.5 | GLM-5 | Change |
| --- | --- | --- | --- |
| Total Parameters | 355B | 744B | ~2.1x increase |
| Active Parameters | 32B | 40B | 25% increase |
| Pre-training Data | 23T tokens | 28.5T tokens | 24% increase |
| Hidden Layers | Undisclosed | 78 | - |
| Expert Modules | Undisclosed | 256 (8 active simultaneously) | - |
| Max Context | 128K | 202K tokens | 58% expansion |
| Attention Mechanism | Standard | DeepSeek Sparse Attention | New |

Despite 2x+ parameter growth, only 40B parameters activate during inference. This is the essence of the MoE architecture.

It's like a company with 744 employees assigning only 40 to a single project. The other 704 wait until their specialty is needed.

**Result: the model's "knowledge capacity" grew significantly, but execution cost stayed relatively low.**

---

## Core Technology 1: DeepSeek Sparse Attention (DSA)

GLM-5's ability to efficiently handle 202K token contexts stems from DeepSeek's sparse attention technology.

Traditional dense attention has every input token calculate relationships with every other token.

Computation grows geometrically with document length—processing a 100K-token document requires 10 billion relationship calculations.

DSA solves this through "selective focus." A lightweight Lightning Indexer module quickly evaluates each token's importance first, then performs attention on only 2,048 key tokens per query token.

Like reading a 100,000-page book by first scanning the table of contents and index, then closely reading only relevant pages.

**DeepSeek-V3.2 experiments proved this maintains output quality while significantly reducing inference cost.**

---

## Core Technology 2: Slime - Asynchronous Reinforcement Learning Infrastructure

If pre-training teaches models "knowledge," post-training converts that knowledge into "abilities usable in practice."

GLM-5's post-training core is **Slime**, a reinforcement learning framework self-developed by Zhipu AI and released open-source.

The biggest bottleneck in traditional RL was data generation and learning happened sequentially.

In agent tasks where models write code, execute it, and await results over minutes, GPUs wasted most time "waiting."

Slime solves this three ways:

First, **asynchronous decoupled architecture**. Data generation (rollout) and training happen independently on separate hardware. Training GPUs run continuously while data generation proceeds in parallel on separate servers.

Second, **mixed precision acceleration**. Data generation uses efficient FP8 format while training maintains stable BF16. Dramatically speeds data generation while preserving training quality.

Third, **agent-oriented design**. Optimized to handle long-tail latency from extended agent tasks like coding, web browsing, and tool calling.

Slime is published on GitHub for use beyond GLM models—Qwen3, DeepSeek V3, and others.

---

## Benchmarks: GLM-5's Performance by Numbers

Benchmarks alone don't determine model value, but effectively show relative positioning versus competitors.

### Reasoning Domain

|  | GLM-5 | GPT-5.2 | Claude Opus 4.5 | Gemini 3.0 Pro | o3-mini |
| --- | --- | --- | --- | --- | --- |
| HLE (Text) | 30.5 | 25.1 | 31.5 | 28.4 | 37.2 |
| HLE (Tool Use) | 50.4 | 40.8 | 51.8 | 43.4 | 45.8 |
| AIME 2026 I | 92.7 | 92.7 | 92.5 | 93.3 | 90.6 |
| GPQA-Diamond | 86.0 | 82.4 | 87.6 | 87.0 | 91.9 |

On AIME 2026 (math competition level), GLM-5 scores 92.7%, only 0.6%p behind Claude Opus 4.5 (93.3%).

On Humanity's Last Exam with tool use, it scores 50.4%, actually outperforming Claude Opus (43.4%).

### Coding Domain

|  | GLM-5 | GPT-5.2 | Claude Opus 4.5 | Gemini 3.0 Pro |
| --- | --- | --- | --- | --- |
| SWE-bench Verified | 77.8 | 73.1 | 80.9 | 80.0 |
| SWE-bench Multilingual | 73.3 | 70.2 | 77.5 | 72.0 |
| Terminal-Bench 2.0 | 56.2 | 39.3 | 59.3 | 54.0 |
| CyberGym | 43.2 | 17.3 | 50.6 | - |

On SWE-bench (solving actual GitHub issues), GLM-5 achieves 77.8%. The gap with Claude Opus 4.5 (80.9%) narrows to 3.1%p. **Previous generation GLM-4.7 was 73.8%, so one generation achieved 4%p improvement.**

Notably, it beats GPT-5.2 (72.0%) on multilingual coding (73.3%).

### Agent Domain - GLM-5's Real Strength

|  | GLM-5 | GLM-4.7 | Claude Opus | Gemini 3.0 Pro |
| --- | --- | --- | --- | --- |
| BrowseComp | 62.0 | 51.4 | 37.0 | 37.8 |
| BrowseComp (Context Management) | 75.9 | 67.6 | 67.8 | 59.2 |
| tau2-Bench | 89.7 | 85.3 | 91.6 | 90.7 |
| MCP-Atlas | 67.8 | 62.2 | 65.2 | 66.6 |
| Vending Bench 2 | $4,432 | $1,034 | $4,967 | $5,478 |

The agent domain is GLM-5's real highlight. On BrowseComp (measuring web search and information understanding), it scores 62.0% for open-source #1 rank. It leads Claude Opus (37.0%) by 25%p.

On MCP-Atlas (large-scale tool-calling benchmark), it scores 67.8%, exceeding Claude Opus (65.2%).

Particularly interesting is Vending Bench 2—a benchmark simulating one year running a virtual vending machine business. GLM-5 closed with $4,432 balance, near Claude Opus ($4,967), **demonstrating long-term planning and resource management capacity matching frontier models.**

---

## Hands-On: How to Use GLM-5

GLM-5 is immediately accessible through several channels.

### 1. Z.ai Web Chat

Simplest approach. Go to Z.ai and switch model option to GLM-5. Provides Chat mode (light conversation) and Agent mode (tool use, file generation). In Agent mode, convert text or source materials directly to .docx, .pdf, .xlsx files.

### 2. Integration with Coding Agents

GLM-5 works with major coding agents: Claude Code, OpenCode, Kilo Code, Roo Code, Cline, etc.

In Claude Code, it's simple: change the model name to "GLM-5" in `~/.claude/settings.json`. However, GLM Coding Plan subscription is required, currently rolling out sequentially starting with Max plan users.

Note that GLM-5 requests consume more plan quota than GLM-4.7.

### 3. Local Deployment

Model weights are publicly available on HuggingFace and ModelScope under MIT license. Supports vLLM and SGLang inference frameworks, and deployment is possible not just on NVIDIA GPUs but also Huawei Ascend, Moore Threads, Cambricon, and other non-NVIDIA chips.

### 4. API Calls

Access via API on developer platform api.z.ai and BigModel.cn. Supports OpenAI API-compatible interface, so most applications integrate by just changing endpoint and model name in existing code.

---

## Best Practices/Pattern Comparison: GLM-5 vs Competitors Selection Guide

|  | Recommended Model | Reason |
| --- | --- | --- |
| Web browsing·search agent | GLM-5 | BrowseComp #1, top information gathering·understanding |
| Real-world coding (bug fixes) | Claude Opus 4.5 | Still highest at SWE-bench 80.9%, though GLM-5 nears at 77.8% |
| Long-term planning·resource mgmt | Gemini 3.0 Pro | Vending Bench 2 $5,478 rank #1 |
| Open-source·self-deployment needed | GLM-5 | MIT license, local deployment support, non-NVIDIA chip compatible |
| Cost-efficient API use | GLM-5 | GLM series API pricing reportedly ~1/10 of GPT-5 |
| Math·science reasoning | Gemini 3.0 Pro | GPQA-Diamond 91.9% top performance |

---

## Closing Thoughts

- GLM-5 combines 744B parameter (40B active) MoE structure with DeepSeek Sparse Attention and Slime async RL, achieving frontier-model-level performance in agent and coding domains for the first time from open-source.
- Open-source competitive dynamics are fundamentally changing. The "closed-only is best" formula no longer holds, and selection criteria shift from "performance gap" to "cost-efficiency."
- Real-world tip: Try GLM-5 free in Agent mode on Z.ai, then test Claude Code integration in your existing workflow.

---

## References

- GLM-5 Official Blog (<https://z.ai/blog/glm-5>)
- GLM-5 Developer Documentation (<https://docs.z.ai/guides/llm/glm-5>)
- Slime RL Framework GitHub (<https://github.com/THUDM/slime>)
- GLM-4.5 Technical Blog (<https://z.ai/blog/glm-4.5>)
- DeepSeek Sparse Attention Paper - DeepSeek-V3.2 (<https://arxiv.org/pdf/2512.02556>)
- Bloomberg - China's Zhipu Unveils New AI Model (<https://www.bloomberg.com/news/articles/2026-02-11/china-s-zhipu-unveils-new-ai-model-jolting-race-with-deepseek>)
- SCMP - DeepSeek boosts AI model as Zhipu AI unveils GLM-5 (<https://www.scmp.com/tech/tech-trends/article/3343225/deepseek-boosts-ai-model-10-fold-token-addition-zhipu-ai-gears-glm-5-launch>)
