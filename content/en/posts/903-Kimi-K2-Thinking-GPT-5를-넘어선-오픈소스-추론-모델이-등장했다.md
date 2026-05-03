---
title: "Kimi K2 Thinking: Open-Source Reasoning Model Surpasses GPT-5"
date: 2025-11-08T23:54:10+09:00
slug: "903-Kimi-K2-Thinking-GPT-5를-넘어선-오픈소스-추론-모델이-등장했다"
original_url: "https://memoryhub.tistory.com/903"
tistory_id: 903
draft: false
---

```
    _  ___           _   _  ______   _____ _     _       _    _             
   | |/ (_)         (_) | |/ /  _ \ |_   _| |   (_)     | |  (_)            
   | ' / _ _ __ ___  _  | ' /| |_) |  | | | |__  _ _ __ | | ___ _ __   __ _ 
   |  < | | '_ ` _ \| | |  < |  _ <   | | | '_ \| | '_ \| |/ / | '_ \ / _` |
   | . \| | | | | | | | | . \| |_) |  | | | | | | | | | |   <| | | | | (_| |
   |_|\_\_|_| |_| |_|_| |_|\_\____/   |_| |_| |_|_|_| |_|_|\_\_|_| |_|\__, |
                                                                        __/ |
   A new era of agentic AI                                              |___/
```

In early November 2025, a model quietly released by Chinese AI startup Moonshot AI is shaking up the industry. It's 'Kimi K2 Thinking', which dominates GPT-5 and Claude Sonnet 4.5 on major benchmarks. What's even more surprising is that this model is completely open-source. The fact that it surpassed big-tech models backed by billions of dollars with just $4.6 million in training costs suggests that AI industry's landscape is fundamentally changing.

Through this article, you'll completely understand the core architecture of Kimi K2 Thinking, its overwhelming benchmark performance, and practical application methods.

**Kimi K2 Thinking, a 1 trillion parameter open-source AI model, dominates GPT-5 and Claude on major benchmarks with ability to call tools 200-300 times consecutively, opening the era of agentic AI.**

## Background

### Background of Thinking Model Emergence

Since late 2024, the AI industry has transitioned to a new paradigm called 'Thinking models'. Rather than simply generating fast answers, models have emerged that explicitly show intermediate reasoning processes and think step-by-step.

| Term | Meaning | Characteristics |
| --- | --- | --- |
| Thinking Model | AI model that explicitly shows reasoning process | Demonstrates intermediate thinking steps for transparency |
| Agentic AI | AI that autonomously leverages tools to perform complex tasks | Can call tools 200-300 times consecutively |
| MoE (Mixture-of-Experts) | Architecture that activates only a portion of total parameters | Activates only 32 billion of 1 trillion parameters for maximum efficiency |
| INT4 Quantization | Technique to compress model weights to 4-bit integers | 2x inference speed improvement, 50% memory reduction |

### Rise of Chinese AI

Early 2025 saw only DeepSeek and Qwen known, but now Moonshot AI's Kimi has joined the global top tier. Despite US semiconductor export restrictions, Chinese AI companies are writing a new history by developing cutting-edge models with H800 chips.

## Core Points

> Kimi K2 Thinking is an open-source reasoning agent model based on 1 trillion parameter MoE architecture capable of 200-300 consecutive tool calls.

### Overwhelming Benchmark Performance

Kimi K2 Thinking posted overwhelming scores against GPT-5 and Claude Sonnet 4.5 on major benchmarks right after being released on November 6, 2025.

**Agent Reasoning Benchmark (Humanity's Last Exam)**

- Kimi K2 Thinking: 44.9%
- GPT-5: 41.7%
- Claude Sonnet 4.5 Thinking: 32.0%

**Agent Search Benchmark (BrowseComp)**

- Kimi K2 Thinking: 60.2%
- GPT-5: 54.9%
- Claude Sonnet 4.5 Thinking: 24.1%

**Coding Benchmark (SWE-Bench Verified)**

- Kimi K2 Thinking: 71.3%
- MiniMax-M2: 69.4%
- GPT-5: undisclosed

The fact that BrowseComp achieved 60.2%, more than double the human baseline of 29.2%, means it completely surpasses human capability in exploring and reasoning about web information.

### Key Technical Features

**1. Long-Horizon Tool Utilization**

Unlike general AI models that complete tasks with 5-10 tool calls, Kimi K2 Thinking calls tools 200-300 times consecutively to solve complex problems. This means it can repeat the following cycle hundreds of times:

```
Thinking → Searching → Browsing → Thinking → Coding → Validation → Thinking → ...
```

**2. INT4 Quantization-Aware Training (QAT)**

By considering INT4 quantization from the training stage, it achieved 2x inference speed without the accuracy loss typical in conventional quantization. At 594GB on Hugging Face, it's nearly half the size of the original Kimi K2's 1.03TB.

**3. 256K Context Window**

Capable of processing vast context equivalent to about 190,000 words, optimized for long document analysis and complex codebase work.

## Practice

### 1. Access via API

Kimi K2 Thinking can be easily accessed through OpenRouter.

**Pricing Information**

- Cache hit: $0.15 / million tokens
- Cache miss: $0.60 / million tokens
- Output: $2.50 / million tokens

This is overwhelmingly cheaper compared to GPT-5's input $1.25 and output $10.

**Installation and Setup**

Run the following commands in terminal:

```
# Install OpenRouter CLI
llm install llm-openrouter

# Set API key
llm keys set openrouter
# [Enter API key in prompt]

# Use model
llm -m openrouter/moonshotai/kimi-k2-thinking \
  'Solve a complex math problem step by step'
```

### 2. Using Web Interface

The simplest method is using the official website:

- Official site: <https://kimi.com>
- Hugging Face Space: <https://huggingface.co/spaces/moonshotai/Kimi-K2-Thinking>

The web interface allows usage in chat mode, but tool call frequency is limited and doesn't fully reproduce benchmark performance. Full capability is expected to be available when the upcoming agent mode is released.

### 3. Local Execution (High-End Hardware Required)

Can be run locally through Ollama, but has substantial minimum specifications:

```
# Run through Ollama
ollama pull kimi-k2-thinking
ollama run kimi-k2-thinking
```

**Recommended Hardware**

- 2 Apple M3 Ultra chips or
- NVIDIA GPU 80GB+ (A100, H100, etc.)

Thanks to INT4 quantization, it's much lighter than typical 1 trillion parameter models, but still requires high-end hardware.

### 4. Real-World Use Cases

Moonshot AI has released the following demos:

**Word-Style Document Editor Creation**

A fully functional Word-style document editor was implemented in HTML/CSS/JavaScript with a single prompt. This includes all following features:

- Text formatting (bold, italic, underline)
- Font size and color change
- Alignment and list functions
- Image insertion
- Print function

The fact that such complex functionality was completed on first attempt proves coding ability matches GPT-5 level.

## Best Practices/Pattern Comparison

| Usage Pattern | Advantages | Cautions |
| --- | --- | --- |
| **Complex Research Tasks** | Can perform deep research by repeating search → analysis → synthesis 200+ times | Prevent drift by setting clear goals and constraints initially |
| **Large-Scale Codebase Refactoring** | Achieved 71.3% on SWE-Bench, can make consistent modifications across multiple files | Validate changes step-by-step and version control required |
| **Academic Paper Writing** | With 256K context, can consider dozens of references simultaneously | Accuracy of citations requires final human verification |
| **API-Based Automation** | Affordable to build complex agent workflows | Unsuitable for real-time responses due to long reasoning time |
| **Open-Source Usage** | Commercial usage possible under Modified MIT license | Verify attribution conditions for large-scale deployment |

## Conclusion

Kimi K2 Thinking's emergence signifies more than a new model release—it represents a paradigm shift in the AI industry. An open-source model surpassing closed models backed by billions of dollars is a decisive moment for AI democratization.

Particularly, achieving this performance with just $4.6 million in training costs suggests more organizations and research teams can now participate in cutting-edge AI model development. Being able to achieve GPT-5-level performance with investment similar to DeepSeek V3's $5.6 million means the barrier to AI research entry has dropped dramatically.

When applying in practice, approach it as "an agent that solves problems by calling tools 200+ times". It truly shines in complex, multi-step tasks rather than simple questions.

## References

- Moonshot AI Official Blog (<https://moonshotai.github.io/Kimi-K2/thinking.html>)
- Hugging Face Model Page (<https://huggingface.co/moonshotai/Kimi-K2-Thinking>)
- VentureBeat Analysis (<https://venturebeat.com/ai/moonshots-kimi-k2-thinking-emerges-as-leading-open-source-ai-outperforming>)
- CNBC Report (<https://www.cnbc.com/2025/11/06/alibaba-backed-moonshot-releases-new-ai-model-kimi-k2-thinking.html>)
- Simon Willison Technical Analysis (<https://simonwillison.net/2025/Nov/6/kimi-k2-thinking/>)
- OpenRouter API Documentation (<https://openrouter.ai/moonshotai/kimi-k2-thinking>)
- THE DECODER Detailed Review (<https://the-decoder.com/moonshot-ais-kimi-k2-thinking-sets-new-agentic-reasoning-records-in-open-source-llms/>)
