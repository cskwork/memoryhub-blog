---
title: "Vibe-Tuning Practical Guide: SLM Fine-Tuning with Claude Code"
date: 2025-12-14T20:29:41+09:00
slug: "927-Vibe-tuning-실전-가이드-Claude-Code로-SLM-Fine-Tuning"
original_url: "https://memoryhub.tistory.com/927"
tistory_id: 927
draft: false
---

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║      ┌─────────┐     Claude     ┌─────────┐                 ║
║      │  Vibe   │ ──── Code ────▶│  SLM    │                 ║
║      │  Spec   │    (Agent)     │ Tuned!  │                 ║
║      └─────────┘                └─────────┘                 ║
║                                                              ║
║    "Define in natural language, AI automates learning"      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

Fine-tuning often brings to mind work taking weeks—dataset building, hyperparameter tuning, GPU setup. But what if you just write "answer in this tone," and AI handles the rest? This article covers **Vibe-tuning workflow that automates from data generation to learning, evaluation, and deployment with just a natural language specification**. After reading, you can build a pipeline by connecting Claude Code with Hugging Face Skills.

**Summary:** In short, Vibe-tuning defines desired output style in natural language (Vibe Spec), lets Claude Code automatically perform synthetic data generation and model learning, shortening SLM tuning from "weeks" to "hours."

---

## Background

The most common concern when applying LLMs to services is this: "GPT-4 or Claude is too costly, but open-source small models don't fit our service tone." Fine-tuning is the answer, but you hit walls when actually trying.

Existing fine-tuning's three barriers are: First, you need hundreds to thousands of quality training data samples. Second, hyperparameter tuning and GPU setup require ML engineering experience. Third, post-learning evaluation criteria are vague, making "did it work" hard to judge.

Vibe-tuning solves this through "automation." The core idea is simple: describe desired output in detail naturally, and an AI agent (Claude Code) generates matching synthetic data, submits work to cloud training infrastructure (Hugging Face Jobs), and even performs rule-based evaluation.

| Term | Definition |
| --- | --- |
| Vibe Spec | Specification document written in natural language detailing desired tone, output format, forbidden rules |
| SLM | Small Language Model. 0.5B-3B parameter-scale small language model |
| SFT | Supervised Fine-Tuning. Training models using labeled data |
| LoRA | Low-Rank Adaptation. Improves efficiency by learning only part instead of all weights |

---

## Core Concepts

> One-line definition: Vibe-tuning bundles "natural language prompt → synthetic data generation → training → evaluation" into a single automation loop, letting non-developers tune SLMs customized for services.

Vibe Coding and Vibe-tuning have similar names but critical differences. Vibe Coding stops at "prompt to code generation," while Vibe-tuning includes evaluation for **creating actually deployable models**. Using cooking as analogy: Vibe Coding means receiving a recipe and prepping ingredients; Vibe-tuning automates everything from prep through cooking, plating, and taste evaluation.

The complete pipeline has 6 stages.

First is Vibe Spec writing—specify desired tone, required/forbidden rules, and output format in markdown.

Second is data generation—Claude Code reads Spec and generates synthetic training data in JSONL format.

Third is first-round tuning—perform SFT on a small model like Qwen3-0.6B using LoRA.

Fourth is evaluation—auto-validate JSON parsing success rates, required key existence, forbidden word inclusion.

Fifth is second-round alignment (optional)—strengthen preferred style with DPO or GRPO.

Sixth is deployment—Hub upload and GGUF conversion.

Claude Code's role is "automation hands." It executes data generation prompts, submits training jobs via Hugging Face Skills, and monitors results. Actual GPU computation happens on Hugging Face infrastructure, so you don't need high-end equipment locally.

---

## Practice

### ① Environment Setup: Connecting Claude Code with HF Skills

First install Claude Code:

```
# macOS/Linux
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex

# Or NPM
npm install -g @anthropic-ai/claude-code
```

Next add the Hugging Face Skills plugin. Run this in Claude Code terminal:

```
/plugin marketplace add huggingface/skills
/plugin install hf-llm-trainer@huggingface-skills
```

Finally configure HF token and connect MCP server:

```
export HF_TOKEN=hf_your_write_access_token_here

claude mcp add --transport http hf-skills \
  https://huggingface.co/mcp?bouquet=skills \
  --header "Authorization: Bearer $HF_TOKEN"
```

You need a token with write access. Hugging Face Jobs may be available only on paid plans.

### ② Write Vibe Spec

Create `VIBE_SPEC.md` in your project folder. Here's an example for "Korean technical assistant enforcing format":

```
# VIBE_SPEC.md
Goal: Korean technical assistant. Respond exclusively in JSON.

[Required]
- Output must be pure JSON single object (no Markdown code blocks or extras)
- Include keys: answer, assumptions, risks, next_steps
- Uncertainty handling: specify assumptions in assumptions, potential risks in risks

[Forbidden]
- Exaggerated expressions ("100%", "definitely" etc.)
- Sensitive information and private code leaks

[Style]
- answer: concise, 3-7 sentences max
- next_steps: 3-6 items
```

The more specific the Spec, the higher the generated data quality. It's better to specify "3-7 sentences" quantitatively than vague "write briefly."

### ③ Generate Synthetic Data

From Claude Code terminal:

```
"Based on VIBE_SPEC.md in the project folder, do this:

1. Generate 800 training samples (train.jsonl) in TRL SFTTrainer compatible messages format.
2. Generate 200 validation samples (eval.jsonl).
3. Topic distribution:
   - 40%: Code/verification (UVM, assertion, debugging)
   - 30%: System/architecture
   - 20%: Document summary/conversion
   - 10%: Error situation 'don't know/assumption' handling
4. No similar questions between train and eval data.
5. After generation, also write and run JSON parsing test script."
```

Generated data follows this format:

```
{"messages":[
  {"role":"user","content":"Create a SystemVerilog assertion example satisfying these requirements: ..."},
  {"role":"assistant","content":"{\"answer\":\"...\",\"assumptions\":[...],\"risks\":[...],\"next_steps\":[...]}"}
]}
```

**Important point:** If Chat Template during training differs from inference, performance drops sharply. Using TRL's messages format automatically applies templates, preventing this issue.

### ④ Submit Training Job

After uploading dataset to Hub, command Claude Code naturally:

```
"Fine-tune Qwen/Qwen3-0.6B on my-org/korean-tech-json-style for instruction following."
```

Claude Code suggests appropriate hardware (e.g., t4-small), estimates time and cost, then requests approval. Once approved, training runs on Hugging Face infrastructure. The 0.6B model is lightweight, so costs are reasonable.

### ⑤ Automated Evaluation

Once training completes, validate these metrics automatically:

| Evaluation Item | Description | Target |
| --- | --- | --- |
| JSON Parse Success Rate | Valid JSON output | 99%+ |
| Required Keys Present | answer, assumptions included | 100% |
| Forbidden Word Detection | Catch "definitely", "100%" etc. | 0 cases |
| Length Limit | answer 3-7 sentences compliance | 95%+ |

These metrics breaking causes service outages, so they must pass. Using TRL with `completion_only=True` improves training efficiency by computing Loss only on Assistant response portions.

---

## Best Practices/Pattern Comparison

| Approach | Advantages | Considerations |
| --- | --- | --- |
| SFT + LoRA | Fast iteration, low compute cost, preserve base model | Possible general language ability degradation (overfitting) |
| SFT → DPO 2-Stage | Learn basic format then refine preferred style | Requires good/bad answer pair data |
| GRPO | Leverage verifiable rewards (compile success) | Reward function design can be complex |
| General Data Mixing (Replay Buffer) | Prevent catastrophic forgetting | Mixing ratio needs tuning |

**Remember this troubleshooting checklist:**

First, template mismatch. Must use identical Chat Template in training and inference.

Second, eval leakage. Similar questions from train data in eval data cause evaluation distortion.

Third, security. Since Claude Code accesses local files, specify sensitive information exclusion rules and review generated data.

---

## Final Thoughts

- Vibe-tuning's core is writing "natural language specification (Vibe Spec)" and having Claude Code automate data generation through evaluation
- Practical tip: Today, open VIBE_SPEC.md and organize desired output style into 3 rules.

---

## References

- Hugging Face TRL Official Documentation (https://huggingface.co/docs/trl)
- Claude Code Installation Guide (https://docs.anthropic.com/en/docs/claude-code)
- Distillabs Vibe-Tuning Concept Introduction (https://distillabs.ai)
