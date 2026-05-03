---
title: "🚀 FunctionGemma: AI Agent on Smartphone with 270M Parameters"
date: 2025-12-21T18:33:39+09:00
slug: "942-FunctionGemma-270M-파라미터로-스마트폰에서-AI-에이전트"
original_url: "https://memoryhub.tistory.com/942"
tistory_id: 942
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
---

```
  ╔═══════════════════════════════════════════════════════╗
  ║                                                       ║
  ║      🚀 F u n c t i o n G e m m a                    ║
  ║                                                       ║
  ║      "Turn on the light"                              ║
  ║             │                                         ║
  ║             ▼                                         ║
  ║      ┌─────────────┐                                  ║
  ║      │  270M LLM   │  ◄── On-Device (0.5GB)          ║
  ║      └─────────────┘                                  ║
  ║             │                                         ║
  ║             ▼                                         ║
  ║      { "function": "toggle_light",                    ║
  ║        "params": { "state": "on" } }                  ║
  ║                                                       ║
  ║      Natural Language  ──►  API Execution             ║
  ║                                                       ║
  ╚═══════════════════════════════════════════════════════╝
```

Do you think "Building an AI agent requires calling GPT-4 API"? Google's FunctionGemma, announced on December 18, 2024, flips this common sense upside down. A ultra-lightweight model with 270M (270 million) parameters runs offline on smartphones, converting natural language into executable API calls. **If the chatbot era has ended and the agent era has begun, FunctionGemma is the first model that puts that agent in your pocket.**

**One-liner summary:** FunctionGemma is an ultra-lightweight edge AI model specialized in converting natural language to API calls, achieving 85% accuracy when fine-tuned, and enabling a fully offline agent implementation on smartphones.

---

## Background

AI is evolving from "just talking chatbots" to "agents that actually take action." To handle everything from setting alarms to adding contacts to turning off lights with a single natural language sentence, the model must go beyond simply generating text and output **structured function calls**.

The problem is that existing large models are cloud-dependent. Network latency, privacy concerns, battery drain. After Google released Gemma 3 270M, the most requested feature from developers was precisely "native function calling."

> One-line definition: FunctionGemma is a lightweight language model based on Gemma 3 270M, specially trained to convert natural language commands into JSON-formatted function calls.

What makes FunctionGemma different from existing approaches is its **design philosophy** itself. It's not a general-purpose conversation model, but was designed from the start to be fine-tuned for specific tasks. Google describes this as "the starting point for customized agents."

---

## Core Features

FunctionGemma's technical differentiation is as follows:

**First, integrated action and conversation capability.** This model can communicate with both computers and humans. It can generate function calls to execute tools, summarize the results in natural language, and deliver them to users through context switching.

**Second, extreme lightweight design.** 270M parameters occupy approximately 0.5GB in FP16 or approximately 300MB with Q8_0 quantization. It runs on edge devices like NVIDIA Jetson Nano and Samsung S25 Ultra, recording approximately 50 tokens/s inference speed on Pixel 8 and iPhone 15 Pro.

**Third, accuracy breakthrough through fine-tuning.** In Google's "Mobile Actions" evaluation, the base model showed 58% accuracy, but jumped to 85% after task-specific fine-tuning. A 27 percentage point improvement is impossible with prompt engineering alone.

| Item | Specification |
| --- | --- |
| Parameters | 270M (270 million) |
| Context Window | 32K tokens |
| Memory (FP16) | ~0.5GB |
| Memory (Q8_0 Quantization) | ~300MB |
| Knowledge Cutoff | August 2024 |
| Training Tokens | 6 trillion |

---

## When to Use

FunctionGemma is not a universal model suitable for all situations. It becomes the optimal choice under the following conditions:

**When you have a defined API surface.** It's ideal for applications like smart home control, media playback, and navigation where the set of executable actions is clear.

**When you're ready to fine-tune.** Instead of zero-shot prompting variability, when you need deterministic and consistent behavior trained on specific data.

**When local-first deployment is the goal.** When immediate latency, complete data privacy, and efficient operation within edge device computing and battery constraints are required.

**When building complex systems.** When general commands are handled by FunctionGemma on the edge, and only complex tasks are routed to larger models like Gemma 3 27B, acting as an "intelligent traffic controller."

---

## Practice: Mobile Actions Fine-tuning

You can fine-tune FunctionGemma directly using Google's Mobile Actions dataset and Colab notebook.

① **Environment Setup**  
Agree to the FunctionGemma model license in your Hugging Face account and issue an access token. Register it as an `HF_TOKEN` environment variable in Colab.

② **Load Model and Dataset**  
Load the model with Hugging Face Transformers library. The Mobile Actions dataset consists of pairs of user prompts and expected function calls.

```
# Python 3.10+ / transformers 4.40+
from transformers import AutoProcessor, AutoModelForCausalLM

processor = AutoProcessor.from_pretrained(
    "google/functiongemma-270m-it", 
    device_map="auto"
)
model = AutoModelForCausalLM.from_pretrained(
    "google/functiongemma-270m-it", 
    dtype="auto", 
    device_map="auto"
)
```

③ **Execute Fine-tuning**  
Perform supervised learning fine-tuning using SFTTrainer from Hugging Face TRL library. Checkpoints are saved to the output directory.

④ **Deploy Model**  
Upload the fine-tuned model to Hugging Face Hub or deploy it directly to mobile devices via LiteRT-LM. You can test it in the Google AI Edge Gallery app.

---

## Ecosystem and Deployment Options Comparison

| Tool/Platform | Purpose | Features |
| --- | --- | --- |
| Hugging Face Transformers | Fine-tuning | Standard workflow, rich documentation |
| Unsloth | Fine-tuning | LoRA support, memory efficiency optimization |
| NVIDIA NeMo | Fine-tuning | Enterprise-grade, DGX Spark support |
| LiteRT-LM | Mobile deployment | Google official, Edge Gallery integration |
| Ollama | Local execution | Simple CLI interface |
| Llama.cpp | General inference | GGUF quantization support, CPU optimization |
| Transformers.js | Web deployment | 100% local execution in browser |

---

## Conclusion

- FunctionGemma is an ultra-lightweight (270M) edge AI model that converts natural language to API calls, enabling fully offline agent implementation on smartphones without cloud.
- Fine-tuning achieves an accuracy leap from 58% to 85%, proving that task-specific training is essential for small models.
- Practical tip: Install the Google AI Edge Gallery app today to experience the TinyGarden game or Mobile Actions demo.

---

## References

- FunctionGemma Official Announcement (https://blog.google/technology/developers/functiongemma/)
- FunctionGemma Model Overview - Google AI (https://ai.google.dev/gemma/docs/functiongemma)
- Hugging Face Model Page (https://huggingface.co/google/functiongemma-270m-it)
- Mobile Actions Fine-tuning Guide (https://ai.google.dev/gemma/docs/mobile-actions)
- Unsloth Fine-tuning Documentation (https://docs.unsloth.ai/models/functiongemma)
- Google AI Edge Gallery App (https://play.google.com/store/apps/details?id=com.google.ai.edge.gallery)
