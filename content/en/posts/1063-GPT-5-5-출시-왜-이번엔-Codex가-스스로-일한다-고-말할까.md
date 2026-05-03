---
title: "GPT-5.5 Launch: Why Does Codex Now Do Work Autonomously?"
date: 2026-04-24T05:10:43+09:00
slug: "1063-GPT-5-5-출시-왜-이번엔-Codex가-스스로-일한다-고-말할까"
original_url: "https://memoryhub.tistory.com/1063"
tistory_id: 1063
draft: false
  hidden: false
cover:
  image: "/images/1063-GPT-5-5-출시-왜-이번엔-Codex가-스스로-일한다-고-말할까/img.png"
  relative: false
  hidden: false
---

![](/images/1063-GPT-5-5-출시-왜-이번엔-Codex가-스스로-일한다-고-말할까/img.png)

GPT-5.5 dropped just 6 weeks after GPT-5.4. I thought "another modest bump," until I saw the benchmarks. Terminal-Bench 2.0: 82.7%, GDPval: 84.9%. And here's the kicker: **it finishes the same task with fewer tokens than GPT-5.4**.

By the end of this article, you'll know what actually changed in GPT-5.5, which plan to use for what, and why your API bill might double.

> GPT-5.5 is "smarter and faster with fewer tokens," and the real differentiator is how long it hangs on in Codex—completing hours of work like a person would.

## Why This Model Now?

The frontier AI race is moving beyond "how smart" to "how long and independent."

GPT-5.4 was fast and capable, but long engineering and research jobs still hit snags or quit early. GPT-5.5 targets exactly that.

Let me define terms first:

| Term | Meaning |
| --- | --- |
| Codex | OpenAI's agent environment for coding and computer manipulation |
| Terminal-Bench 2.0 | Benchmark evaluating planning, tool use, and iteration in CLI |
| GDPval | 44-profession real knowledge-work task quality benchmark |
| OSWorld-Verified | Computer control capability in realistic environments |
| FrontierMath Tier 4 | Hardest modern math problems |
| Preparedness Framework | OpenAI's risk-level assessment (High, Critical, etc.) |

## Core Differences at a Glance

> GPT-5.5 hits SOTA on four axes: agentic coding, computer use, knowledge work, and early scientific research.
> 
> The bigger shift: **same result with fewer tokens than GPT-5.4**—benchmark numbers matter less than this efficiency.

Benchmark summary (official):

| Benchmark | GPT-5.5 | GPT-5.4 | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- |
| Terminal-Bench 2.0 | **82.7%** | 75.1% | 69.4% | 68.5% |
| Expert-SWE (internal) | **73.1%** | 68.5% | - | - |
| GDPval | **84.9%** | 83.0% | 80.3% | 67.3% |
| OSWorld-Verified | **78.7%** | 75.0% | 78.0% | - |
| FrontierMath Tier 4 | **35.4%** | 27.1% | 22.9% | 16.7% |
| CyberGym | **81.8%** | 79.0% | 73.1% | - |

GPT-5.5 Pro hits **39.6%** on FrontierMath Tier 4 and **90.1%** on BrowseComp, a tier above GPT-5.4 Pro. On Tau2-bench Telecom, it achieves **98.0%** accuracy without prompt tuning—production-grade automation is near.

## How to Use It Yourself

### ① Straight from ChatGPT

Plus, Pro, Business, and Enterprise users can pick **GPT-5.5 Thinking** from the model dropdown. Pro+ can also choose **GPT-5.5 Pro**. The feel-difference is biggest for summary, research, and document work—"long context compressed nicely" tasks.

### ② Hand Off Complex Work in Codex

Plus, Pro, Business, Enterprise, Edu, and Go plans access Codex with **GPT-5.5 at 400K context**.

**Fast mode** runs **1.5x faster** but costs **2.5x**. Real-world wins come from patterns like this:

```bash
# Example: Codex CLI multi-file refactor (terminal example)
codex run --model gpt-5.5 \
  "Redesign auth to JWT, update all affected tests at once. No mid-check—drive to completion and summarize changes."
```

That's the pattern OpenAI emphasized: "messy, multi-part work that persists to the end" (confirm flag names in `codex --help` for your plan and version).

### ③ API Launches "Soon"

As of 2026-04-24, API isn't public yet ("very soon" per OpenAI).

When available, expect this pricing on Responses and Chat Completions:

| Item | Price per 1M Tokens |
| --- | --- |
| gpt-5.5 input | $5 |
| gpt-5.5 output | $30 |
| gpt-5.5-pro input | $30 |
| gpt-5.5-pro output | $180 |
| Batch & Flex | 50% of standard |
| Priority | 2.5× standard |

Unit costs exceed GPT-5.4, but Codex is tuned to **finish the same result in fewer tokens**, so actual billing may surprise you lower—per OpenAI.

## Which Plan/Mode—Pattern Comparison

| Pattern | Pros | Notes |
| --- | --- | --- |
| ChatGPT + GPT-5.5 Thinking | General knowledge work, research, plugin tasks most solid | Plus+ required, lower on extreme difficulty vs. Pro |
| ChatGPT + GPT-5.5 Pro | Strong on law, finance, data science, high-precision work | Pro/Business/Enterprise only, longer wait times possible |
| Codex + GPT-5.5 | 400K context refactors, debug, doc generation in one go | Fast mode 1.5× speed but 2.5× cost; clarify scope upfront |
| Trusted Access for Cyber | Verified defense work without over-refusal, red/blue scenarios | Needs chatgpt.com/cyber signup; stricter classifier on sensitive |
| API gpt-5.5 / gpt-5.5-pro | Production agent serving; Batch/Flex cuts unit cost in half | Not live yet ("soon"), check safety once available |

## Closing Thoughts

GPT-5.5's real story is "less hands needed to finish work," not "smarter model." Token efficiency and persistence (staying on task) beat benchmark numbers. API isn't live yet, so test in ChatGPT and Codex, feel the difference, then decide your plan.

## References

- [Introducing GPT-5.5 | OpenAI Official Announcement](https://openai.com/index/introducing-gpt-5-5/)
- [OpenAI releases GPT-5.5, bringing company one step closer to an AI 'super app' | TechCrunch, 2026-04-23](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/)
- [OpenAI's GPT-5.5 is here, and it's no potato: narrowly beats Anthropic's Claude on Terminal-Bench 2.0 | VentureBeat](https://venturebeat.com/technology/openais-gpt-5-5-is-here-and-its-no-potato-narrowly-beats-anthropics-claude-mythos-preview-on-terminal-bench-2-0)
- [OpenAI launches GPT-5.5 just weeks after GPT-5.4 as AI race accelerates | Fortune, 2026-04-23](https://fortune.com/2026/04/23/openai-releases-gpt-5-5/)
- [OpenAI unveils GPT-5.5, claims a "new class of intelligence" at double the API price | The Decoder](https://the-decoder.com/openai-unveils-gpt-5-5-claims-a-new-class-of-intelligence-at-double-the-api-price/)
- [Trusted Access for Cyber Signup](https://chatgpt.com/cyber)
