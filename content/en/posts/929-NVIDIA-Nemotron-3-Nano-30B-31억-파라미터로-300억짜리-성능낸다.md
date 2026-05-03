---
title: "? NVIDIA Nemotron 3 Nano 30B, 3.2B Active Parameters Deliver 30B Performance"
date: 2025-12-16T19:55:57+09:00
slug: "929-NVIDIA-Nemotron-3-Nano-30B-31억-파라미터로-300억짜리-성능낸다"
original_url: "https://memoryhub.tistory.com/929"
tistory_id: 929
draft: false
---

```
     ███╗   ██╗███████╗███╗   ███╗ ██████╗ ████████╗██████╗  ██████╗ ███╗   ██╗
     ████╗  ██║██╔════╝████╗ ████║██╔═══██╗╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║
     ██╔██╗ ██║█████╗  ██╔████╔██║██║   ██║   ██║   ██████╔╝██║   ██║██╔██╗ ██║
     ██║╚██╗██║██╔══╝  ██║╚██╔╝██║██║   ██║   ██║   ██╔══██╗██║   ██║██║╚██╗██║
     ██║ ╚████║███████╗██║ ╚═╝ ██║╚██████╔╝   ██║   ██║  ██║╚██████╔╝██║ ╚████║
     ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                     3 . N A N O   3 0 B   |   N V I D I A
                  ┌─────────────────────────────────────────┐
                  │  31.6B Total  →  3.2B Active per Token  │
                  │     128 Experts  →  6 Activated         │
                  │     Context Window: 1M Tokens           │
                  └─────────────────────────────────────────┘
```

"Open-source LLMs ultimately have to give up either performance or speed."  
If you believed this assumption, NVIDIA just shattered it. Released on December 15th, the Nemotron 3 Nano 30B activates only 10% of total parameters yet demonstrates **3.3x faster inference speed** compared to Qwen3-30B. The secret lies in a hybrid architecture combining Mamba and Transformer.

**TL;DR:** To sum up, Nemotron 3 Nano uses an MoE structure that activates just 3.2B of its 31.6B parameters, achieving up to 3.3x faster inference compared to equivalent models while supporting a 1 million token context window—a cutting-edge open-source agentic AI model.

---

## Background

NVIDIA has good reason for building its own LLM. Most existing open-source models rely on Dense Transformer architecture. As parameters increase, performance improves, but inference costs scale proportionally. In environments like agentic AI where multiple models run simultaneously, this becomes a critical bottleneck.

> Nemotron 3 Nano is an open-weight LLM based on a hybrid architecture combining Mamba-2 state-space models, Transformer attention, and MoE (Mixture-of-Experts).

The core design philosophy is clear: don't compute every parameter every time. Among 128 experts, only 6 activate per token, so out of 31.6B total parameters, only 3.2B are actually used. It's like borrowing just 6 books from a massive library instead of reading the entire collection.

This architecture is especially powerful for **agentic AI**. In systems where multiple sub-agents collaborate—search, planning, tool execution, verification—each agent's inference cost directly impacts the system's total cost. Nemotron 3 Nano attempts to solve this problem at the architectural level.

---

## Architecture

Nemotron 3 Nano's 52 layers consist of three types.

| Layer Type | Count | Role |
| --- | --- | --- |
| Mamba-2 | 23 | Handles long-range dependencies, memory-efficient sequence modeling |
| MoE (Mixture-of-Experts) | 23 | 6 out of 128 experts activated, maximizes computational efficiency |
| GQA Attention | 6 | Precise reasoning and structural relationship detection |

Mamba-2 layers process long contexts efficiently, while Transformer attention layers handle complex reasoning. MoE layers activate only relevant experts per token, dramatically reducing computation versus Dense models.

This combination yields measurable results. On a single H200 GPU at 8K input/16K output, it shows **3.3x** higher throughput than Qwen3-30B-A3B and **2.2x** higher than GPT-OSS-20B.

---

## Benchmark Performance

Performance can't be judged on speed alone. Let's see how Nemotron 3 Nano compares with competitors across key benchmarks.

| Benchmark | Nemotron 3 Nano | Qwen3-30B-A3B | GPT-OSS-20B |
| --- | --- | --- | --- |
| AIME25 (math, no tools) | 89.1% | 85.0% | 91.7% |
| AIME25 (with tools) | 99.2% | - | 98.7% |
| LiveCodeBench v6 | 68.3% | 66.0% | 61.0% |
| Arena-Hard-v2 (agent) | 67.7% | 57.8% | 48.5% |
| MMLU-Pro (general knowledge) | 78.3% | 80.9% | - |
| RULER @ 1M (long context) | 86.3% | - | 128K limit |

Math and coding performance spike when combined with tools. Notably, on Arena-Hard-v2—which measures agent workflow reliability—it leads Qwen3 by **10 percentage points**. However, on broad knowledge tests like MMLU-Pro, Qwen3 has a slight edge, likely because Dense architectures better preserve encyclopedic knowledge.

The **1 million token context** isn't just marketing. RULER benchmark shows 86.3% accuracy even at 1M context length. This means analyzing large codebases or long agent sessions can maintain full context without chunking.

---

## Training Data and Transparency

One aspect NVIDIA emphasized with this release is **transparency**. Beyond model weights, they published training recipes and redistributable datasets.

- **Nemotron-CC-v2.1**: 2.5 trillion English tokens extracted from Common Crawl, including synthetic rephrasing and multilingual translation
- **Nemotron-CC-Code-v1**: 428 billion code tokens, preserving code structure via the Lynx pipeline
- **Nemotron-Pretraining-Code-v2**: Multi-stage filtered and deduplicated GitHub code references

Trained on **25 trillion tokens**, followed by SFT (Supervised Fine-Tuning) and RLHF (Reinforcement Learning from Human Feedback). Notably, they applied GRPO (Group Relative Policy Optimization) in multi-environment reinforcement learning tailored to actual agentic tasks: math, coding, tool use, and multi-turn conversation.

---

## Practice: Running Nemotron 3 Nano Locally

### 1. Running the server with vLLM

The simplest approach uses vLLM. Using the FP8 quantized version reduces memory consumption.

```
vllm serve --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 \
  --max-num-seqs 8 \
  --tensor-parallel-size 1 \
  --max-model-len 262144 \
  --port 8000 \
  --trust-remote-code \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser-plugin nano_v3_reasoning_parser.py \
  --reasoning-parser nano_v3
```

### 2. Running on consumer GPUs with llama.cpp

To run on RTX series GPUs, you can use llama.cpp. You'll need the 4-bit quantized GGUF version.

```
# Build llama.cpp (with CUDA support)
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release -j

# Download and run the model
./build/bin/llama-cli \
  -m NVIDIA-Nemotron-3-Nano-30B-A3B-Q4_K_M.gguf \
  -c 32768 \
  --special \
  -p "What is 2+2?"
```

### 3. Configure inference mode

Nemotron 3 Nano lets you toggle reasoning mode on/off. For complex math or coding problems, enable reasoning; for simple conversations, disable it for efficiency.

- **Reasoning ON**: Output internal thought process with `<think>` tokens, then final answer
- **Reasoning OFF**: Output answer immediately, faster but less accurate on complex problems

---

## Best Practices and Pattern Comparison

| Use Case | Advantages | Considerations |
| --- | --- | --- |
| Multi-agent systems | Run multiple agents in parallel with low token-per-token cost | Clear agent role separation needed for efficiency |
| RAG systems | Handle large documents with 1M context without chunking | Very long contexts increase memory requirements |
| Coding assistant | Excellent code generation at 68.3% LiveCodeBench | Slight weakness in general knowledge vs Qwen3 per MMLU-Pro |
| Local deployment | Consumer GPU support via llama.cpp/LM Studio | H100-level GPUs recommended for full performance |

---

## Nemotron 3 Family Roadmap

Nano is just the beginning. NVIDIA has announced two larger models through mid-2026.

| Model | Total Parameters | Active Parameters | Target Use Case |
| --- | --- | --- | --- |
| Nano | 31.6B | 3.6B | Efficient single-agent |
| Super | ~100B | ~10B | Collaborative agents, IT automation |
| Ultra | ~500B | ~50B | SOTA reasoning, complex AI applications |

Super and Ultra will include additional technologies like LatentMoE (4x more experts at same cost), Multi-Token Prediction (long-form generation efficiency), and NVFP4 training.

---

## Conclusion

- Nemotron 3 Nano uses a hybrid Mamba-Transformer MoE architecture that activates just 3.2B of 31.6B parameters, achieving up to 3.3x faster inference compared to equivalent models.
- With 1 million token context and agentic-optimized training, it's ideal for building multi-agent systems, and with publicly released weights, training recipes, and datasets, it enhances reproducibility.
- Practical tip: Download the FP8 version from Hugging Face and test a server with vLLM. If you're building agentic projects, start by comparing throughput against existing models.

---

## References

- NVIDIA Nemotron 3 Official Page (<https://research.nvidia.com/labs/nemotron/Nemotron-3/>)
- Hugging Face Model Card (<https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16>)
- NVIDIA Developer Blog: Inside Nemotron 3 (<https://developer.nvidia.com/blog/inside-nvidia-nemotron-3-techniques-tools-and-data-that-make-it-efficient-and-accurate/>)
- Nemotron 3 Nano Technical Report (<https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf>)
- Unsloth Nemotron 3 Execution Guide (<https://docs.unsloth.ai/models/nemotron-3>)
