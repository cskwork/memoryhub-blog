---
title: "👁️ Gemini 3 Flash Agentic Vision: How AI Investigates Images Has Changed"
date: 2026-01-29T16:15:42+09:00
slug: "995-Gemini-3-Flash-Agentic-Vision-AI가-이미지를-조사-하는-방식이-달라졌다"
original_url: "https://memoryhub.tistory.com/995"
tistory_id: 995
draft: false
---

```
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║      ┌─────────┐                                      ║
    ║      │  IMAGE  │──────► THINK ──► ACT ──► OBSERVE    ║
    ║      └─────────┘           │        │         │       ║
    ║           ▲                └────────┴─────────┘       ║
    ║           │                         │                 ║
    ║           └─────────────────────────┘                 ║
    ║                    (Loop)                             ║
    ║                                                       ║
    ║         GEMINI 3 FLASH - AGENTIC VISION              ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
```

Ever shown AI an image with fine print? Most AI glances once and answers.

The problem is when missing fine details like serial numbers or distant signs, AI relies on guessing.

Google's Gemini 3 Flash Agentic Vision released January 27, 2026, directly addresses this.

**It's technology converting AI image processing from "seeing once" to "actively investigating."**

**One-sentence summary:** Agentic Vision enables AI to enlarge, manipulate, and analyze images through code execution while providing visually evidence-based answers—a new AI vision paradigm.

## Background

Traditional multimodal AI models process images statically. Given a photo, they generate answers through a single inference pass.

Like humans quickly skimming documents and answering.

> Agentic Vision: Technology converting image understanding from passive processing to active investigation process

Limitations of this approach are clear. When fine details are needed—semiconductor serial numbers, high-resolution architectural drawing details, distant road signs—the model must resort to guessing. Agentic Vision solves this by **combining visual reasoning and code execution**.

Like examining documents with magnifying glass thoroughly, AI investigates images step-by-step.

According to Google, enabling code execution on Gemini 3 Flash achieves **5-10% quality improvement** across most vision benchmarks.

## Core Principle: Think-Act-Observe Loop

Agentic Vision operates through three-stage repeating loop.

In the **Think stage**, the model analyzes user questions and images to establish a multi-step plan. Not simply "what's in this image?" but "which parts need enlargement?" "what processing is needed?"

In the **Act stage**, the model generates and executes Python code. It performs manipulations like image cropping, rotation, annotation, or analytical work like calculation or bounding box counting. Critically, this code executes in deterministic environment. You get verifiable execution results, not probabilistic guesses.

In the **Observe stage**, the transformed image is added to the model's context window. The model reviews new data in better context, then generates final response.

This loop repeats as needed. If one enlargement is insufficient, enlarge again. If additional analysis is needed, execute more code.

## Real-World Use Cases

Agentic Vision's practical applications clearly demonstrate its value.

In **high-resolution image inspection**, architectural drawing verification platform PlanCheckSolver.com adopted this feature, improving accuracy 5%. The model iteratively crops and analyzes specific areas like roof edges or building sections to verify complex architectural code compliance.

In **image annotation**, Gemini app leverages this for finger counting tasks. The model directly draws bounding boxes and number labels on each finger. This "visual notepad" guarantees pixel-level understanding.

In **visual math and chart generation**, traditional AI models often hallucinate in multi-step visual arithmetic.

Agentic Vision delegates calculation to deterministic Python environment, circumventing this problem. The entire process from identifying raw data in tables,

writing normalization code,

to generating Matplotlib charts happens through verifiable execution.

## Getting Started

| Usage Environment | Access Method | Notes |
| --- | --- | --- |
| Gemini API | Enable Code Execution in Google AI Studio or Vertex AI | For developers |
| Gemini App | Select Thinking from model dropdown | For general users |
| Demo App | Try demo app directly in Google AI Studio | For feature testing |

Developers can experiment with this by simply turning on Code Execution under Tools in AI Studio Playground.

## Conclusion

- Agentic Vision is paradigm shift converting AI vision from static processing to active investigation
- Think-Act-Observe loop combined with code execution delivers 5-10% quality improvement
- Excels in tasks requiring precision like high-resolution inspection, image annotation, visual calculation
- Practical tip: Enable Code Execution in Google AI Studio and test complex image analysis tasks.

## References

- Introducing Agentic Vision in Gemini 3 Flash (https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/)
- Gemini API Code Execution Documentation (https://ai.google.dev/gemini-api/docs/code-execution#images)
- Google AI Studio Demo App (https://aistudio.google.com/apps/bundled/gemini_visual_thinking)
