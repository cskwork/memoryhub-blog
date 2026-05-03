---
title: "GPT-5.3 Codex Spark: The Bottleneck in AI Coding Is Not Intelligence, It's Speed"
date: 2026-02-13T06:58:21+09:00
slug: "1022-GPT-5-3-Codex-Spark-AI-코딩의-병목은-지능-이-아니라-속도-였다"
original_url: "https://memoryhub.tistory.com/1022"
tistory_id: 1022
draft: false
cover:
  image: "images/1022-GPT-5-3-Codex-Spark-AI-%EC%BD%94%EB%94%A9%EC%9D%98-%EB%B3%91%EB%AA%A9%EC%9D%80-%EC%A7%80%EB%8A%A5-%EC%9D%B4-%EC%95%84%EB%8B%88%EB%9D%BC-%EC%86%8D%EB%8F%84-%EC%98%80%EB%8B%A4/img.png"
  relative: false
  hidden: false
---

![](/images/1022-GPT-5-3-Codex-Spark-AI-%EC%BD%94%EB%94%A9%EC%9D%98-%EB%B3%91%EB%AA%A9%EC%9D%80-%EC%A7%80%EB%8A%A5-%EC%9D%B4-%EC%95%84%EB%8B%88%EB%9D%BC-%EC%86%8D%EB%8F%84-%EC%98%80%EB%8B%A4/img.png)

If you've used an AI coding tool, you've probably experienced this: requesting code modifications and staring blankly at a blank screen waiting. Those few seconds break your concentration and destroy your workflow. OpenAI's Codex-Spark, released on February 12, 2026, directly addresses this problem.

**By responding at speeds exceeding 1,000 tokens per second, this model is shifting the competitive axis of AI coding tools from "how intelligent" to "how fast."**

**One-liner summary:** To put it bluntly, Codex-Spark runs on Cerebras's wafer-scale chip and provides 15 times faster generation speed compared to the existing Codex—OpenAI's first real-time coding specialized model.

---

## Background

The AI coding tool market is growing rapidly. According to Stack Overflow developer surveys, AI coding assistants have already established themselves in the daily workflows of a significant number of professional developers. However, there's an interesting paradox: as models become more intelligent, developers' frustrations often grow.

The reason is simple. Frontier models like GPT-5.3-Codex can work autonomously for hours or even days.

But even simple edits like "change this variable name," which should take 3 seconds, have to go through the same heavy pipeline.

It's like driving a large trailer to the convenience store to buy a single carton of milk.

> Codex-Spark is OpenAI's first real-time coding specialized model, a lightweight version of GPT-5.3-Codex that operates at speeds exceeding 1,000 tokens per second on Cerebras's WSE-3 chip.

OpenAI changed two things simultaneously to solve this problem.

First, it optimized the model itself for real-time interaction.

Second, it fundamentally replaced the hardware running the model.

That hardware is **Cerebras's Wafer Scale Engine 3 (WSE-3)**.

---

## Cerebras WSE-3: The Secret to Low-Latency Inference

To understand Codex-Spark's speed, you need to understand the WSE-3. Conventional AI chips (NVIDIA GPUs) pack billions of transistors onto a postage stamp-sized piece of silicon. The WSE-3 takes a completely different approach. It turns an entire semiconductor wafer into a single chip.

Why does this matter? In AI inference, the biggest bottleneck isn't computation itself.

It's the time data takes to move between chips, and between chips and memory.

WSE-3 reduces this movement time dramatically by placing all computations and memory on one massive chip.

The numbers make this difference clear.

| Item | Cerebras WSE-3 | NVIDIA B200 |
| --- | --- | --- |
| Transistor Count | 4 trillion | 208 billion |
| AI Cores | 900,000 | ~18,000 |
| On-chip Memory | 44GB (SRAM) | Several GB (SRAM basis) |
| Internal Memory Bandwidth | 21 PB/s | ~3 TB/s |
| Die Area | 46,225 mm² | ~800 mm² |

The key difference is **44GB of on-chip SRAM**. NVIDIA GPUs store model weights in external memory called HBM (High Bandwidth Memory) for fast computation. To retrieve data, it must go outside the chip.

WSE-3 stores a significant portion of the model's working data directly on the chip. For workloads like coding models that involve short burst generation and repeated tool calls, this architecture dramatically reduces first-token time.

OpenAI hasn't disclosed specific latency numbers, but stated it achieved **15 times faster generation speed** compared to existing models.

---

## Codex-Spark Benchmark Performance

Speed alone doesn't mean much if code quality drops. OpenAI evaluated Codex-Spark using two agentic software engineering benchmarks.

**SWE-Bench Pro** measures actual software engineering capabilities across 4 programming languages, not just Python. Codex-Spark recorded higher accuracy than GPT-5.1-Codex-mini, while task completion time was only a fraction of what GPT-5.3-Codex required.

**Terminal-Bench 2.0** evaluates terminal skills necessary for coding agents. Results are as follows:

| Model | Terminal-Bench 2.0 Accuracy |
| --- | --- |
| GPT-5.3-Codex | 77.3% |
| GPT-5.3-Codex-Spark | 58.4% |
| GPT-5.1-Codex-mini | 46.1% |

Codex-Spark has lower accuracy than full-size GPT-5.3-Codex. This is expected.

The key point is that **it significantly outperforms GPT-5.1-Codex-mini while being incomparably faster in task completion time**. In other words, it's a model that is "sufficiently intelligent while extremely fast."

---

## Not Just a Model Change: Full Infrastructure Optimization

When creating Codex-Spark, OpenAI redesigned not just the model but the entire request-response pipeline.

This optimization is being applied to all Codex models, not just Codex-Spark.

Key improvement metrics are as follows:

| Optimization Item | Improvement |
| --- | --- |
| Client/Server Round-trip Overhead | 80% reduction |
| Per-token Overhead | 30% reduction |
| Time to First Token (TTFT) | 50% reduction |

Technically, the key was replacing the existing HTTP-based communication with **persistent WebSocket connections**.

HTTP requires establishing and closing connections for each request.

WebSocket, once connected, allows continuous bidirectional data exchange, significantly reducing cumulative latency in fast iterative work.

This WebSocket path is applied by default in Codex-Spark and will soon expand to all models.

The core code of the inference stack was also rewritten, and session initialization was restructured so the first token appears on screen faster.

---

## Practice: When and How to Use Codex-Spark

Codex-Spark is currently available as a research preview to ChatGPT Pro users. Available environments include Codex app, CLI, and VS Code extension.

### 1. When Codex-Spark is Suitable

Codex-Spark is fundamentally designed to perform lightweight, minimal edits. It shines in the following situations:

- **Targeted edits** like changing variable names or function signatures
- **Fast prototyping** of UI layouts with immediate result verification
- **Iterative work** refactoring code logic or refining interfaces
- **Interactive exploration** quickly answering contextual questions about codebases

Particularly in situations requiring rapid iteration of "request modification → check results → revise," the time spent waiting for responses essentially disappears. You're free to change directions or stop during work.

### 2. When Existing Codex is Suitable

Conversely, existing GPT-5.3-Codex is more appropriate for:

- **Long-term work** analyzing entire repositories and refactoring
- **Deep debugging** tracking root causes of complex bugs
- **Large-scale implementation** spanning multiple files
- **Work requiring automated testing** (Spark doesn't auto-run tests unless requested)

### 3. Considerations

- 128K context window, text-only (image input not supported)
- Separate usage limits apply during the research preview period
- Access restrictions or queues may occur if demand is high
- API is currently available to only a limited number of design partners

---

## Best Practices/Pattern Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Codex-Spark (Real-time Mode) | 1000+ tokens/second, immediate feedback, freedom to stop/change direction | Lower accuracy than full-size model, text-only, auto-testing not performed |
| GPT-5.3-Codex (Long-term Work Mode) | Highest coding accuracy, autonomous long-duration work, multimodal support | Relatively slower responses, inefficient for real-time iterative work |
| GPT-5.1-Codex-mini | Lightweight model providing basic coding support | Lower accuracy than Spark, no speed advantage |

OpenAI's long-term vision is interesting. The two modes will eventually merge, with the system interacting with developers in real-time while simultaneously delegating long tasks to sub-agents or distributing across multiple models in parallel.

There will be no need to pre-select a work mode.

---

## What the OpenAI-Cerebras Partnership Means

Equally important as the technical content is the industrial context. OpenAI has long depended on NVIDIA GPUs. Codex-Spark is **symbolically significant as OpenAI's first model running on non-NVIDIA chips**.

OpenAI and Cerebras announced a multi-year partnership valued at $10 billion in January 2026, and Cerebras recently raised $1 billion at a $23 billion valuation. IPO is reportedly under consideration.

OpenAI carefully positions this relationship. It emphasizes that "GPUs remain the foundation of our training and inference pipelines and provide the most cost-effective tokens for broad use." Cerebras's role is to **complement workflows requiring extreme low-latency**.

This reflects a larger industry trend. Google develops TPUs, Amazon develops Inferentia and Trainium, and Microsoft develops Maia chips. The era of "solving everything with a single general-purpose GPU" in the AI inference market is ending, and **heterogeneous computing** strategies combining specialized hardware for specific workloads are becoming standard.

---

## Conclusion

- Codex-Spark demonstrates that the next competitive axis for AI coding tools is not "more intelligent AI" but "faster AI." At speeds exceeding 1,000 tokens per second, developers can collaborate with AI in real-time without losing momentum.
- Cerebras's WSE-3 wafer-scale chip fundamentally solves the data movement bottleneck through on-chip memory and integrated design, offering a meaningful alternative to NVIDIA GPU-centric AI inference hardware markets.
- Practical tip: If you're a ChatGPT Pro subscriber, try enabling Codex-Spark in the VS Code extension. You can directly experience the speed difference in small iterative tasks like variable renaming, UI style adjustments, and quick refactoring.

---

## References

- Introducing GPT-5.3-Codex-Spark (https://openai.com/index/introducing-gpt-5-3-codex-spark/)
- Introducing OpenAI GPT-5.3-Codex-Spark Powered by Cerebras (https://www.cerebras.ai/blog/openai-codexspark)
- Cerebras WSE-3 Product Page (https://www.cerebras.ai/chip)
- A new version of OpenAI's Codex is powered by a new dedicated chip - TechCrunch (https://techcrunch.com/2026/02/12/a-new-version-of-openais-codex-is-powered-by-a-new-dedicated-chip/)
- OpenAI deploys Cerebras chips for 15x faster code generation - VentureBeat (https://venturebeat.com/technology/openai-deploys-cerebras-chips-for-15x-faster-code-generation-in-first-major)
- OpenAI's new Codex Spark model is built for speed - The New Stack (https://thenewstack.io/openais-new-codex-spark-is-optimized-for-speed/)
