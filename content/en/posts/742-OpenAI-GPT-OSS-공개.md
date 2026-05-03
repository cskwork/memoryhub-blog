---
title: "OpenAI Releases GPT-OSS"
date: 2025-08-06T05:00:46+09:00
slug: "742-OpenAI-GPT-OSS-공개"
original_url: "https://memoryhub.tistory.com/742"
tistory_id: 742
draft: false
---

Exploring the New Standard in Open-Weight Language Models with Two Models: 120B and 20B  
*Released August 5, 2025* ([OpenAI](https://openai.com/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

---

## 1. What is GPT-OSS?

OpenAI has released two models, **gpt-oss-120b** and **gpt-oss-20b**, under the Apache 2.0 license. Both models deliver outstanding reasoning performance for their size and are optimized to run at low cost on consumer hardware. ([OpenAI](https://openai.com/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

- **gpt-oss-120b**: Runs on a single 80 GB GPU, reasoning performance equivalent to OpenAI's **o4-mini**
- **gpt-oss-20b**: Executes with just 16 GB memory, benchmark results similar to **o3-mini**
- Both models natively support advanced features including tool calling, chain-of-thought (CoT), and few-shot function calling ([OpenAI](https://openai.com/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

## 2. Model Architecture at a Glance

| Model | Total Parameters | Active Parameters/Token | Layers | Experts/Layer | Context Length |  |
| --- | --- | --- | --- | --- | --- | --- |
| gpt-oss-120b | 117 B | 5.1 B | 36 | 4 of 128 active | 128 k |  |
| gpt-oss-20b | 21 B | 3.6 B | 24 | 4 of 32 active | 128 k |  |

Thanks to the MoE (Mixture of Experts) architecture, **only necessary parameters are activated**, significantly reducing memory consumption. Using RoPE positional embeddings handles long contexts of **128k** tokens.

## 3. Training and Post-training

- **Pre-training**: Large-scale text data focused on STEM, coding, and general knowledge
- **Post-training**: Supervised fine-tuning + high-compute RL phase → Aligned to OpenAI Model Spec
- **Three Reasoning Effort levels** (low, medium, high) allow choosing the **speed-performance tradeoff**

## 4. Performance Benchmarks

- **120b**: Matches **o4-mini** on Codeforces, MMLU, TauBench, and excels in healthcare (HealthBench) and competition math (AIME 2024/25)
- **20b**: Achieves **o3-mini** level despite smaller size, exceeding in some tasks

> ※ In specialized domains like medical advice, expert validation is still necessary.

## 5. Safety and Challenges of Open Models

OpenAI directly created **adversarial fine-tuning** scenarios and validated them with its Preparedness Framework, plus underwent external expert review. It also launched a **$500k red team challenge** to publicly explore potential risks.

## 6. Where and How to Use It?

- **Hugging Face**: Available for immediate download (default MXFP4 4-bit quantization)
- **Platform Partners**: Immediate deployment on Azure, Hugging Face, vLLM, Ollama, llama.cpp, LM Studio, AWS, Together AI, and more
- **Windows Developers**: Local inference models based on ONNX Runtime will be supported in VS Code AI Toolkit

## 7. Why Open-Weight Models Matter

- **Improved Access**: Organizations with limited budgets and infrastructure can deploy high-performance LLMs in their own infrastructure
- **Transparency and Accelerated Research**: Model weights, tokenizers, and even harmony prompt renderers are released → Reproducibility achieved
- **Global Innovation**: Anyone, regardless of region or scale, can develop customized AI services

## 8. Closing Remarks and Implications

With the symbolic meaning of "the first open-weight LLM in 6 years since GPT-2," GPT-OSS achieves all three pillars:

**1) Practical performance**, **2) Low execution cost**, **3) Enhanced safety processes**.

As a developer, download the models now and start with **local testing** through **custom fine-tuning**.  
The future where open model ecosystems and proprietary APIs **complement each other** is right around the corner. ([OpenAI](https://openai.com/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))
