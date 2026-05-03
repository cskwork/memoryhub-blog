---
title: "🔬 Gemma Scope 2: Opening the AI Black Box - An 'AI Microscope' Made with 110 Petabytes"
date: 2025-12-22T00:07:19+09:00
slug: "943-Gemma-Scope-2-AI-블랙박스를-열다-110-페타바이트로-만든-AI-현미경"
original_url: "https://memoryhub.tistory.com/943"
tistory_id: 943
draft: false
---

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║      ┌─────────────────────────────────────────────┐      ║
    ║      │  🔬 G E M M A   S C O P E   2              │      ║
    ║      │      ━━━━━━━━━━━━━━━━━━━━━━━━━              │      ║
    ║      │                                             │      ║
    ║      │   [ LLM ]  ───▶  [ SAE ]  ───▶  [Features] │      ║
    ║      │    Black         Sparse        Interpretable      ║
    ║      │     Box        Autoencoder      Concepts   │      ║
    ║      │                                             │      ║
    ║      │   "A microscope peering into AI's brain"   │      ║
    ║      └─────────────────────────────────────────────┘      ║
    ║                                                           ║
    ║           Google DeepMind | December 2025                 ║
    ╚═══════════════════════════════════════════════════════════╝
```

Have you ever wondered why ChatGPT gave a certain response? Even if you ask "provide evidence," AI only offers plausible explanations, and no one knows what actual calculations happen inside. This is the AI "black box problem." On December 19, 2025, Google DeepMind released a tool that directly challenges this issue. **Gemma Scope 2 is the largest-scale open-source interpretation tool ever capable of tracking the "thought circuits" inside AI models.**

**One-liner summary:** Gemma Scope 2 uses Sparse Autoencoder technology to decompose the internal activations of LLMs, enabling direct tracking of safety issues like hallucinations, jailbreaks, and false reasoning.

---

## Background

As AI models grow more powerful, a paradoxical situation is unfolding. Models become increasingly intelligent, yet it becomes increasingly difficult to understand why they behave that way. When large models like GPT-4 or Claude confidently state false information like "Seoul's population is 50 million," developers cannot pinpoint exactly where that error originated.

> Interpretability is a research field that analyzes how AI models work internally so humans can understand why they make specific decisions.

This problem matters for clear reasons. As AI becomes used in medical diagnosis, financial transactions, and legal advice, systems that cannot answer "why?" are hard to trust. The EU's AI Act requires "explainable AI" for this same reason.

Existing interpretation methods had limitations. Analyzing individual neurons often revealed that one neuron simultaneously handles "academic citations," "English conversations," "HTTP requests," and "Korean text." This is called the **polysemanticity problem**. One neuron does not equal one concept.

---

## Sparse Autoencoder: The Key to Opening the Black Box

Gemma Scope 2's core technology is Sparse Autoencoder, or SAE for short. To understand this concept, you first need to know what autoencoders are.

A regular autoencoder is a neural network that compresses input and then reconstructs it. It compresses a 100-dimensional vector to 50 dimensions, then expands it back to 100 dimensions. Where SAE differs is by adding a **sparsity constraint**.

> Sparse Autoencoder is a technique that decomposes a model's internal activations into a "sparse" form, allowing only a small number of interpretable features to be activated.

By way of analogy: A regular brain scan lights up the entire brain simultaneously like bright lights, making it hard to tell which area does what. SAE shows "right now, only these three spots are active" in high-resolution scanning. By removing unnecessary noise, each region's role becomes much clearer.

In fact, when Anthropic applied SAE to Claude 3, they could identify "code type signatures," "personality traits," "cultural biases," and even "abstract features related to deceptive behavior." OpenAI also succeeded in extracting 16 million interpretable features from GPT-4.

---

## Gemma Scope 2's Core Upgrades

Gemma Scope 2 has evolved significantly across four dimensions compared to its predecessor.

First, **full model coverage**. It supports all sizes of the entire Gemma 3 family, from 270M to 27B parameter models. Now emergent behaviors that only appear in larger models can be studied. As a reference, there was a previous case where a C2S Scale model of 27B size discovered a new cancer treatment pathway, and Gemma Scope 2 can be utilized to understand such behaviors.

Second, **complex internal operation analysis tools** have been added. All layers have trained SAE and transcoder. Through skip-transcoder and cross-layer transcoder, multi-step computations spanning multiple layers can be tracked.

Third, **latest training techniques** have been applied. The Matryoshka training technique is used for SAE to detect more useful concepts and resolve flaws discovered in the previous Gemma Scope.

Fourth, **chatbot behavior analysis tools**. Specialized tools for analyzing conversational models are included, enabling analysis of jailbreaks, refusal mechanisms, and chain-of-thought fidelity.

---

## Overwhelming Difference in Scale

The scale of Gemma Scope 2's creation is inadequately described as simply "large."

| Item | Number |
| --- | --- |
| Stored Data Volume | Approximately 110 petabytes |
| Total Training Parameters | Over 1 trillion |
| Supported Model Sizes | 270M ~ 27B |
| Coverage | All Gemma 3 models, all layers |

According to Google DeepMind, this is the **largest-scale interpretability tool ever released by an AI research lab**. Tools are provided not just for one or two layers, but for all layers and sub-layers of the entire model.

---

## Real-world Application Scenarios

Let's look at actual safety issues that Gemma Scope 2 can address.

**Hallucination tracking**: Identify internal features activated when a model generates false information. Through this, you can create a warning system stating "this response is likely a hallucination."

**Jailbreak detection**: When a prompt attempting to bypass safety restrictions is received, you can track how the model internally processes it. You can analyze why the refusal mechanism worked or didn't work.

**Sycophancy analysis**: The phenomenon of a model only agreeing with users can also be captured as internal features. Distinguishing genuine reasoning from simple agreement becomes possible.

**Reasoning fidelity verification**: You can verify whether the reasoning process the model expresses externally matches its actual internal state. This is key to detecting the problem where AI "makes explanations seem plausible while actually making decisions differently."

---

## Trying It Yourself

Gemma Scope 2 has been released completely open-source. Researchers or developers can access it right now.

1. **Neuronpedia interactive demo**: You can directly visualize feature activation in a web browser. Experience it immediately without downloading files.
2. **Hugging Face repository**: All model weights are publicly available. You can choose from gemma-scope-2-270m-pt to gemma-scope-2-27b-it.
3. **Google Colab tutorial**: Notebooks are provided where you can follow along with JumpReLU SAE training in JAX and PyTorch.
4. **Technical paper**: A detailed paper containing architecture and training methodology has been released.

However, there's a caveat. It's currently in rolling release status and is scheduled to be finalized by December 31, 2025. Some data may be replaced or updated, so check the latest status on Hugging Face.

---

## Best Practices/Pattern Comparison

| Interpretation Technique | Advantages | Cautions |
| --- | --- | --- |
| Individual neuron analysis | Intuitive, simple implementation | Polysemanticity makes interpretation difficult |
| Attention visualization | Can understand input-output relationships | Doesn't explain why attention works that way |
| Sparse Autoencoder | Interpretable feature decomposition, multi-layer analysis possible | Requires massive computing for training |
| Cross-layer Transcoder | Can trace multi-step inference | High complexity, cutting-edge technique |

---

## Conclusion

- Gemma Scope 2 is an interpretation tool that lets you "peek through a microscope" into AI internals, covering all Gemma 3 models and all layers.
- With SAE technology, safety issues like hallucinations, jailbreaks, and sycophancy can be tracked directly at their internal causes.
- At 110 petabytes scale, it's the largest interpretation tool ever released by an AI research lab.
- Practical tip: Check directly in the Neuronpedia demo which features activate for specific prompts.

---

## References

- Gemma Scope 2 Official Blog (https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/)
- Hugging Face Repository (https://huggingface.co/google/gemma-scope-2)
- Neuronpedia Interactive Demo (https://www.neuronpedia.org/gemma-scope-2)
- Google Colab Tutorial (https://colab.sandbox.google.com/drive/1NhWjg7n0nhfW--CjtsOdw5A5J_-Bzn4r)
- Technical Report PDF (https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/Gemma_Scope_2_Technical_Paper.pdf)
