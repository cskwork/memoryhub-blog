---
title: "AgentKit at a Glance: Building, Deploying, and Operating Agents"
date: 2025-10-07T16:55:41+09:00
slug: "838-AgentKit-한눈에-보기-에이전트를-만들고-배포하고-잘-굴리는-방법"
original_url: "https://memoryhub.tistory.com/838"
tistory_id: 838
draft: false
---

AgentKit is an **all-in-one agent toolkit** offering visual workflow design (Agent Builder), centralized data/tool connection management (Connector Registry), embedded chat UI (ChatKit), evaluation (Evals), and reinforcement fine-tuning (RFT) in one place. It dramatically cuts complex orchestration, prompt tuning, and UI development time, letting you reach production **faster and more reliably**.

---

## Why AgentKit?

Previously, agent development required manual assembly:

- Complex orchestration (no versioning)
- Custom connectors and manual evaluation pipelines
- Prompt tuning, then weeks of frontend work

**AgentKit** packages these into standardized building blocks, delivering the entire flow **design → embed → evaluate/optimize** in one stream. Klarna processed 2/3 of support tickets with agents, Clay achieved **10x growth** with sales agents.

---

## Core Components and Impact

| Component | Key Functions | Expected Impact |
| --- | --- | --- |
| **Agent Builder** | Drag-and-drop nodes for multi-agent logic, preview execution, inline evaluation, **complete versioning** | Faster iteration, easier collaboration (product/legal/eng on same canvas) |
| **Connector Registry** | Unify data sources/tools from ChatGPT and APIs in **one admin panel**. Includes Dropbox/Google Drive/SharePoint/Teams and third-party MCP | Enhanced data governance, connector reuse and central management |
| **Guardrails** | **Open-source safety layer**: PII masking, jailbreak detection, Python/JS library support | Stability and compliance, reduced operational risk |
| **ChatKit** | Embed complex chat UI with streaming/threads/thinking display in **short time**, theme/brand customization | Frontend dev time slash (case: Canva, 2 weeks → 1 hour to integrate) |
| **Evals (Updated)** | **Datasets, Trace grading, auto-prompt optimization, third-party model evaluation** | Precise performance measurement and improvement loop (case: accuracy +30%, dev time -50%) |
| **RFT (Reinforcement Fine-Tuning)** | o4-mini GA, GPT-5 private beta. **Custom tool calls** and **custom graders** support | Optimize reasoning/tool use for specific workflows |

---

## Agent Builder: Turn Complex Logic into "Visible Design"

- **Node-based** (Agent, file search, Guardrails, MCP, user approval, etc.) connects flows
- **Preview execution, inline evaluation, versioning** enable fast iteration

**Cases**

- Ramp: Buyer agent: "months → hours", **70% faster iteration cycle**
- LY Corporation: Multi-agent workflow built and executed in **under 2 hours**

---

## ChatKit: Agent-Type Chat UI Instantly in Your Product

- Provides **agent UX essentials**: streaming responses, thread management, "show thinking"
- Embed anywhere (app/web), **easy branding customization**
- **Case**: Canva integrated developer community support agent in **1 hour**, saving **2 weeks**
- Adoption by HubSpot, Albertsons, Evernote, Taboola

---

## Evaluation (Evals) Upgrade: Turn Performance into Numbers

- **Datasets**: Build quick eval sheets → expand to auto grading and human labels
- **Trace grading**: Evaluate **end-to-end workflows** and auto-score to pinpoint bottlenecks
- **Auto-prompt optimization**: Generate improved prompts from human feedback and grader results
- **Third-party model support**: Evaluate non-OpenAI models by same criteria
- **Case**: Carlyle—multi-agent due diligence framework **dev 50% faster**, **accuracy +30%**

---

## RFT (Reinforcement Fine-Tuning): "Tool-Using" Reasoning Aligned to Your Work

- **o4-mini** GA, **GPT-5 private beta** underway
- **Custom tool calls**: Learn "when and which tools to use," raising **reasoning-action quality**
- **Custom graders**: Align model behavior to **usage-specific criteria**

---

## Real Application Ideas

- **Customer support**: Classify → guardrail → knowledge search → summarize/answer—full automation
- **Sales/research**: Multi-agent division (collect/summarize/verify/followup) for speed and accuracy
- **Internal knowledge assistant**: Document repos, messengers, no-code tools—with access/PII guards
- **Onboarding/training**: Interactive guides, document Q&A, progress tracking, auto-feedback

---

## Getting Started

1. **Agent Builder** – Choose template or start with blank canvas
2. **Connector Registry** – Configure data source/tool connections (including MCP)
3. **Guardrails** – Enable rules (PII, jailbreak, etc.)
4. **ChatKit** – Embed chat widget in product and customize theme
5. **Evals** – Create dataset and use **Trace grading** to find bottlenecks → **auto-prompt optimization**
6. **RFT** if needed – Fine-tune tool use/scoring criteria for your work

---

## Closing

**Core Insight:**

Agent success depends on **design, data connection, evaluation, UI**—the full loop. AgentKit provides this loop as the default. Start with one small template now and immediately spin a **measurable improvement loop**.
