---
title: "🚀 Kimi Linear: The First Linear Attention That Surpasses Full Attention"
date: 2026-01-23T22:57:08+09:00
slug: "988-Kimi-Linear-Full-Attention을-넘어선-최초의-Linear-Attention이-등장했다"
original_url: "https://memoryhub.tistory.com/988"
tistory_id: 988
draft: false
---

```
╔═══════════════════════════════════════════════════════╗
║                                                       ║
║     ██╗  ██╗██╗███╗   ███╗██╗                        ║
║     ██║ ██╔╝██║████╗ ████║██║                        ║
║     █████╔╝ ██║██╔████╔██║██║                        ║
║     ██╔═██╗ ██║██║╚██╔╝██║██║                        ║
║     ██║  ██╗██║██║ ╚═╝ ██║██║                        ║
║     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚═╝                        ║
║                                                       ║
║     ██╗     ██╗███╗   ██╗███████╗ █████╗ ██████╗     ║
║     ██║     ██║████╗  ██║██╔════╝██╔══██╗██╔══██╗    ║
║     ██║     ██║██╔██╗ ██║█████╗  ███████║██████╔╝    ║
║     ██║     ██║██║╚██╗██║██╔══╝  ██╔══██║██╔══██╗    ║
║     ███████╗██║██║ ╚████║███████╗██║  ██║██║  ██║    ║
║     ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝    ║
║                                                       ║
║     [ Selective Forget + Precise Update = O(n) ]     ║
║                                                       ║
╚═══════════════════════════════════════════════════════╝
```

There's been a prevailing belief in the AI industry that "Linear Attention is fast but performs poorly." This dilemma existed because Full Attention memory explodes when processing 1 million tokens, while Linear Attention loses information. But in October 2025, Moonshot AI shattered this orthodoxy. **Kimi Linear surpasses Full Attention performance in fair comparison while reducing memory by 75% and improving decoding speed by 6x.** How did it accomplish what seemed impossible?

**One-sentence summary:** Kimi Linear is a hybrid architecture that finally overcomes the efficiency-performance trade-off by combining "channel-wise selective forgetting" and "delta rule-based precise updates" through Kimi Delta Attention (KDA).

---

## Background: The Achilles Heel of Transformers, the O(n²) Curse

The core of Transformers, Softmax Attention, is powerful but has a fatal weakness: computational complexity grows as n² relative to sequence length n.

> Softmax Attention excels at context understanding because all tokens reference all other tokens, but as sequences grow longer, computation and memory increase exponentially.

Let's look at a concrete example. Processing 1,000 tokens requires about 1 million operations. But processing 1 million tokens requires 1 trillion operations, creating an explosion. With the linear memory cost of KV Cache increasing as well, processing long contexts hits a wall.

**Linear Attention** was proposed to solve this problem. The core idea is to remove Softmax computation and reorder Query and Key operations to achieve O(n) linear complexity. However, Linear Attention also had fundamental limitations.

---

## The Linear Attention Dilemma: Endlessly Accumulating Memory

Let me use a hotel concierge analogy for Linear Attention. A Full Attention concierge perfectly records every guest's conversation—accurate but needing infinite recording tape. A Linear Attention concierge keeps rewriting information on a single notepad. Space is saved, but there's a problem: **old information cannot be deleted.**

Technically, Linear Attention accumulates Key-Value pairs into a matrix-form "state." New information keeps getting added, but there's no mechanism to delete previous information. As sequences grow longer, the state becomes saturated, and recent and past information mix, accumulating "retrieval errors."

Drawing from neuroscientist David Eagleman: "The enemy of memory is not time but other memories."

Linear Attention faces exactly this problem.

---

## Kimi Delta Attention (KDA): The Science of Selective Forgetting

The core of Kimi Linear is **Kimi Delta Attention (KDA)**. KDA improves upon the existing Gated DeltaNet Linear Attention module by combining two key mechanisms.

**First is Delta Rule-based precise update.** Delta Rule is a classical principle of neural network learning: "adjust weights by the difference (Delta) between predicted and target values." Imagine teaching a child archery. If the arrow misses left, you tell them to adjust right. Correction is proportional to how much it missed.

KDA applies this principle to memory updates. When a new Key-Value arrives, it first "deletes" the previous Value associated with that Key from the existing state, then "replaces" it with the new Value. Not just addition but **overwriting** becomes possible.

**Second is channel-wise granular gating.** The existing Gated DeltaNet uses a single forgetting rate (α) for each Attention Head. But KDA provides a separate forgetting rate for each feature channel. Like a concierge distinguishing "I can forget guest names quickly, but I must remember allergy information long-term."

Expressed mathematically:

```
S_t = (I - β_t × k_t × k_t^T) × Diag(α_t) × S_(t-1) + β_t × k_t × v_t^T
```

Here, **Diag(α_t)** is a diagonal matrix representing channel-wise forgetting rates. Using different α values per channel instead of a single scalar provides more precise memory control.

---

## Hybrid Architecture: The Golden Ratio of 3:1

No matter how powerful KDA is, Linear Attention has inherent limitations. It's weaker at precise memory retrieval and copy operations compared to Full Attention. Kimi Linear addresses this with a **hybrid architecture**.

Specifically, it places one Multi-Head Latent Attention (MLA) layer for every 3 KDA layers. MLA is an efficient Full Attention variant introduced in DeepSeek-V2, compressing KV Cache to improve memory efficiency.

| Architecture | Train PPL | Val PPL | Characteristics |
| --- | --- | --- | --- |
| Full Attention (0:1) | 9.45 | 5.77 | Baseline |
| KDA:MLA = 1:1 | 9.29 | 5.66 | Even mix |
| **KDA:MLA = 3:1** | **9.23** | **5.65** | Optimal ratio |
| KDA:MLA = 7:1 | 9.23 | 5.70 | Efficiency first |
| KDA:MLA = 15:1 | 9.34 | 5.82 | Quality degradation starts |

The 3:1 ratio is the optimal balance point between performance and efficiency. With this configuration, **KV Cache is reduced by 75%** while

achieving lower Perplexity compared to Full Attention.

Interestingly, Kimi Linear doesn't use positional encoding (Positional Encoding) in the MLA layers.

All positional information processing is delegated to KDA layers, contributing to both architectural simplification and improved computational efficiency.

---

## Benchmark Results: Numbers Proving Performance

Kimi Linear is a 48B parameter model (3B active) trained on 1.4 trillion tokens. Results from comparison with Full Attention MLA and Gated DeltaNet Hybrid (GDN-H) using the same training recipe are striking.

**In general task performance**, Kimi Linear achieved top scores across all domains including MMLU-Pro, BBH, and GPQA-Diamond. Notably, on the difficult reasoning benchmark GPQA-Diamond, it showed 2.1% improvement over MLA.

**In mathematics and coding tasks**, it maintained an advantage on difficult benchmarks like AIME 2025, HMMT 2025, and LiveCodeBench. RL learning convergence was faster than MLA too. On MATH500, Kimi Linear achieved 90% final accuracy while MLA reached only 84%.

**On 128K long-context tasks**, it significantly outperformed MLA and GDN-H with RULER benchmark scores of 84.3 points and RepoQA of 68.5 points. This indicates superior selective information retrieval ability in long contexts.

**In inference efficiency**, at 1 million token context, decoding throughput improved 6x over Full Attention. Token Per Output Time (TPOT) also decreased significantly, raising practical applicability for real-time services.

---

## Practice: Using Kimi Linear Model

Moonshot AI released model checkpoints and KDA kernels as open source. You can use them right away via Hugging Face and vLLM.

**1. Environment Setup**

Recommended environment is Python 3.10 or higher, PyTorch 2.4 or higher, CUDA 12.4. The transformers library must support trust_remote_code.

**2. Model Loading and Inference**

```
# Python 3.10+, latest transformers version required
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "moonshotai/Kimi-Linear-48B-A3B-Instruct"
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto",
    trust_remote_code=True
)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "What is the core innovation of Kimi Linear?"}
]

input_ids = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

output = model.generate(inputs=input_ids, max_new_tokens=500)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

**3. Deployment as API Server via vLLM**

In production environments, you can build an OpenAI-compatible API endpoint using vLLM. The latest vLLM officially supports Kimi Linear.

---

## Architecture Comparison: Full Attention vs Linear Attention vs Kimi Linear

| Item | Full Attention | Existing Linear Attention | Kimi Linear (KDA) |
| --- | --- | --- | --- |
| Time complexity | O(n²) | O(n) | O(n) |
| KV Cache growth | Linear increase | Fixed | Fixed (75% reduction) |
| Forgetting mechanism | None (full preservation) | None (accumulation only) | Channel-wise selective forgetting |
| Precise update | Complete recalculation | Not possible | Delta Rule-based |
| Long-context performance | Excellent | Degraded | Surpasses Full Attention |
| Inference speed | Baseline | 3x or more | 6x or more |

The key differentiator of Kimi Linear is that **efficiency improvement didn't lead to performance degradation**. It broke the old formula that Linear Attention is "fast but inaccurate."

---

## Conclusion

- Kimi Linear solves the chronic problem of Linear Attention, "information saturation," through Kimi Delta Attention (KDA). Channel-wise granular gating and Delta Rule updates are the core.
- With a 3:1 KDA-MLA hybrid structure, it achieved 75% KV Cache reduction and 6x decoding speed improvement while surpassing Full Attention performance. This is the first case where Linear Attention beats Full Attention in fair comparison.
- Practical tip: Open-source checkpoints are available, so test Kimi Linear on projects requiring long-context processing. Production deployment is possible with vLLM support.

---

## References

- Kimi Linear: An Expressive, Efficient Attention Architecture - arXiv (https://arxiv.org/abs/2510.26692)
- MoonshotAI/Kimi-Linear - GitHub (https://github.com/MoonshotAI/Kimi-Linear)
- moonshotai/Kimi-Linear-48B-A3B-Instruct - Hugging Face (https://huggingface.co/moonshotai/Kimi-Linear-48B-A3B-Instruct)
- Gated Delta Networks: Improving Mamba2 with Delta Rule - ICLR 2025 (https://arxiv.org/abs/2412.06464)
- Flash Linear Attention Library (https://github.com/fla-org/flash-linear-attention)
