---
title: "OpenAI Open Model (gpt-oss) — \"A Reasoning LLM That Runs on Your PC\""
date: 2025-08-08T08:17:37+09:00
slug: "743-OpenAI-오픈-모델-gpt-oss-내-PC에서-돌아가는-추론형-LLM"
original_url: "https://memoryhub.tistory.com/743"
tistory_id: 743
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
---

These days, there's a huge demand to "keep company data on-premises but still get GPT-grade reasoning." That's why **OpenAI's open-weight reasoning model `gpt-oss` (120b/20b)** is making waves. The license is free (Apache 2.0), it's designed for agentic tasks, and you even get **access to full chain-of-thought (CoT) capabilities**. This article quickly and clearly explains **why it was released, what makes it different, and how to run it**. ([OpenAI](https://openai.com/ko-KR/open-models/ "OpenAI's Open Models | OpenAI"))

---

## Background

Historically, OpenAI released few language models as open-weight after GPT-2. But demand for **on-premises/local inference**, **cost/latency optimization**, and **customized safety controls** has grown. Against this backdrop, **`gpt-oss-120b` and `gpt-oss-20b`** were released August 5, 2025. The core value proposition is "powerful reasoning capabilities and agentic workflows that consider tool use (web search, Python execution)." ([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

---

## Problem-Solving Strengths

1. **Deployment Flexibility** – From data centers to high-end laptops, **run locally** suited to your environment. (20b is ~16GB, 120b is ~80GB/multi-GPU) ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-transformers "How to run gpt-oss with Transformers"))
2. **Agent-Friendly** – Designed with **function calling, web search, and code execution** in mind. Control reasoning difficulty (`reasoning_effort`) with **low/medium/high** levels. ([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"), [OpenAI Platform](https://platform.openai.com/docs/guides/reasoning?utm_source=chatgpt.com "Reasoning models - OpenAI API"))
3. **Commercial Use OK** – **Apache-2.0** licensing provides freedom for experimentation, customization, and commercial deployment. ([OpenAI](https://openai.com/ko-KR/open-models/ "OpenAI's Open Models | OpenAI"))

---

## Core Principles

### 1) Model Architecture at a Glance

```
# gpt-oss (all text-only) - Agent/reasoning-oriented
+------------------+
|  Input tokens    |
+---------+--------+
          |
          v
   [Cross Attention]  <— GQA, 128k context
          |
          v
   [MoE Block (Router)]
      ├─ Top-4 of 128 experts active (120b)
      └─ Top-4 of 32 experts active (20b)
          |
          v
   [Output + (optional) Tool calls/Structured output]
```

*The MoE (Mixture of Experts) structure activates **only some experts per token**, balancing **reasoning performance ↔ latency/memory**. Both models use **up to 128k context**, GQA, and RoPE.* ([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

### 2) Specs Summary

| Item | gpt-oss-120b | gpt-oss-20b |
| --- | --- | --- |
| Total Parameters | ~**117B** (exactly 116.8B) | ~**21B** (exactly 20.9B) |
| Active Parameters/Token | **~5.1B** | **~3.6B** |
| Layers | **36** | **24** |
| MoE Experts | **128** (Top-4 active) | **32** (Top-4 active) |
| Context Length | **128k** | **128k** |
| License | **Apache-2.0** | **Apache-2.0** |

([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

### 3) Performance Positioning (Key Points)

- On benchmarks (MMLU, GPQA, AIME, etc.), **120b approaches o4-mini**, **20b is small but o3-mini-class** according to reports. See model cards and official pages for detailed numbers. ([OpenAI](https://openai.com/ko-KR/open-models/ "OpenAI's Open Models | OpenAI"))

### 4) Safety & Governance

- Open models carry risks of **malicious fine-tuning**, so pre- and post-release testing was conducted to **adversarial fine-tuning** standards per the Preparedness Framework. The model card explicitly states **failure to meet 'High' criteria** in tracked categories (biological/chemical, cyber, AI self-improvement).
- Beyond basic policy compliance, **deployers (you)** may need to design **additional safeguards**.

---

## Try It Out: Code & Workflows

### 1) Invoke via Local Server (Responses-Compatible)

```
# 1) Start Transformers server
transformers serve

# 2) Call Responses-compatible endpoint with cURL
curl -X POST http://localhost:8000/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-oss-20b",
    "input": [{"role":"user","content":"Summarize open model features in 3 lines"}],
    "max_output_tokens": 300,
    "temperature": 0.7
  }'
```

*Why is Responses compatibility important?* It makes it **easy to align interfaces with existing OpenAI apps/agent code**. ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-transformers "How to run gpt-oss with Transformers"))

### 2) Control Inference Cost & Latency: `reasoning.effort`

```
{
  "model": "openai/gpt-oss-20b",
  "reasoning": { "effort": "low" },  // "low" | "medium" | "high"
  "input": [{"role":"user","content":"One-line summary"}]
}
```

*Use `low` for simple tasks, `high` for complex step-by-step reasoning.* ([OpenAI Platform](https://platform.openai.com/docs/guides/reasoning?utm_source=chatgpt.com "Reasoning models - OpenAI API"))

### 3) Force API Response to **JSON Schema** (Structured Output)

```
{
  "model": "openai/gpt-oss-20b",
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "faq",
      "schema": {
        "type": "object",
        "properties": {
          "question": { "type": "string" },
          "answer":   { "type": "string" }
        },
        "required": ["question","answer"],
        "additionalProperties": false
      },
      "strict": true
    }
  },
  "input": [{"role":"user","content":"Create one key FAQ on gpt-oss"}]
}
```

*Great for frontend/backend pipelines to use **directly without post-processing**.* ([OpenAI Platform](https://platform.openai.com/docs/guides/structured-outputs?utm_source=chatgpt.com "Structured model outputs - OpenAI API"))

---

## Cautions & Tips

⚠️ **Things to Watch Out For**

- **Hardware Reality Check**:
  - **20b** is recommended at **~16GB VRAM** (MXFP4), **120b** at **≥60GB VRAM or multi-GPU**. Verify Hopper+ / MXFP4 support. ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-transformers "How to run gpt-oss with Transformers"))
  - Running at bfloat16 significantly increases memory usage. ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-transformers "How to run gpt-oss with Transformers"))
- **Knowledge Cutoff**: gpt-oss's **knowledge cutoff is June 2024**. Supplement current events with tool calls (web search).
- **Medical/Safety Guideline Compliance**: The model card explicitly states **not for medical diagnosis/treatment**. Attach domain-specific validation and auditing. ([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

💡 **Pro Tips**

- Using function calling and structured output **simultaneously** in **agentic workflows** greatly boosts reliability. ([OpenAI Platform](https://platform.openai.com/docs/guides/function-calling?utm_source=chatgpt.com "Function calling - OpenAI API"))
- Rather than using legacy prompts as-is, specify `reasoning.effort` tailored to task difficulty for **fine-grained cost/latency control**. ([OpenAI Platform](https://platform.openai.com/docs/guides/reasoning?utm_source=chatgpt.com "Reasoning models - OpenAI API"))
- Pick serving stacks like **vLLM/Transformers/Ollama** based on your situation (speed, memory, operational convenience tradeoffs). ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-vllm "How to run gpt-oss with vLLM"))

---

## Closing Remarks

The era of "I must sacrifice performance for open-weight" seems behind us. **gpt-oss brings agent-friendly design, reasoning stage control, and structured output**, opening **a production-ready local inference option**.  
Which workflows would your team like to try first? Drop a comment with your GPU/memory setup and expected scenarios!

---

## Resources

- OpenAI — **OpenAI's Open Models**: <https://openai.com/ko-KR/open-models/>
- OpenAI — **Introducing gpt-oss (2025-08-05)**: <https://openai.com/ko-KR/index/introducing-gpt-oss/>
- OpenAI — **gpt-oss Model Card (PDF)**: <https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf>
- OpenAI API — **Reasoning Guide (`reasoning.effort`)**: <https://platform.openai.com/docs/guides/reasoning>
- OpenAI API — **Structured Outputs Guide**: <https://platform.openai.com/docs/guides/structured-outputs>
- OpenAI Cookbook — **Running gpt-oss with Transformers**: <https://cookbook.openai.com/articles/gpt-oss/run-transformers>
- OpenAI Cookbook — **Serving gpt-oss with vLLM**: <https://cookbook.openai.com/articles/gpt-oss/run-vllm>

---

**#openmodels #gpt-oss #localLLM**
