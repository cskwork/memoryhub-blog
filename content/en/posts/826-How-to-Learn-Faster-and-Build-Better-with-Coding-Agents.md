---
title: "How to Learn Faster and Build Better with Coding Agents"
date: 2025-10-03T22:09:49+09:00
slug: "826-How-to-Learn-Faster-and-Build-Better-with-Coding-Agents"
original_url: "https://memoryhub.tistory.com/826"
tistory_id: 826
draft: false
---

A practical, beginner‑friendly workflow to go from idea → working app without getting lost in auto‑generated complexity.

**Reading time:** 7–9 minutes

**Based on:** "This Agent Stack Makes 10x Coder (Plan→Verify)" — <https://www.youtube.com/watch?v=B4uD9z6i_IU>

---

## TL;DR

- **Don't offload everything to one agent.** Use a **planning agent** to co‑design the feature, and a separate **implementation agent** to build it. Then loop back to the planner to **verify** (00:00–02:41).
- **Divide & conquer.** Plan in **atomic features/phases**; implement and test one at a time to avoid regressions and keep learning (01:45–02:41).
- Tools like **Tracer** (a VS Code extension) streamline this **Plan → Implement → Verify** loop with built‑in web search, file‑level plans, and automated checks (03:08–07:52).

---

## Why the usual "one‑click build" fails

When you give a vague idea to a single coding agent, it often produces **hundreds of files** and a **heavy architecture**—and then fails (00:00–00:22). Specs‑driven development improves success rates (00:22–00:51), but if you let the agent do everything, **you don't actually learn much** (00:51–01:22).

---

## The VE Planning Method (Plan → Implement → Verify)

Treat the LLM as a **collaborator**, not a replacement (01:22). Here's the loop:

1. **Brainstorm & clarify with a planning agent** (separate from the coder).
   Ask it to **ask you clarifying questions**; this accelerates your own learning (01:22–01:45).
2. **Divide the app into atomic features** (APIs, screens, flows).
   Plan each feature separately while keeping the big picture in view (01:45–02:13).
3. **Pick one feature** and **implement it with a separate coding agent** (e.g., Claude/Copilot) (02:13–02:41).
4. **Verify** the result using the **original planning agent**.
   Iterate until it passes; this prevents regressions and keeps prior work stable (02:13–02:41).
5. **Repeat** for the next feature.
   You'll build momentum without breaking what already works (02:41).

---

## A Walkthrough Example

Goal: A simple web app with an **HTML front end** and a **Python backend** that calls Google's **Gemini 2.5 Flash Image** model (nicknamed **"nano banana"**) via **REST**, no SDK. The app should generate **four images** from a prompt, let the user **select one**, then **iterate** on that selection with a new prompt (04:22–05:41, 06:06–06:38).

### 1) Plan with the AI (Tracer's chat)

- The planner performs a **web search** to locate the correct REST endpoints and confirms details like **API key** and **backend language** (05:15–06:06).
- You confirm **Python** for backend and attempt to use a **candidateCount** style parameter for four images (06:06–06:38).
- The planner produces a **multi‑phase plan** plus a **file‑level implementation plan**: what files to create and what goes in each (06:38–07:32).

### 2) Implement with an independent coding agent

- Execute the agreed plan in your coding agent (e.g., Claude/Copilot). Tracer keeps **state and context** about which project/file it's working on (07:32–09:27).

### 3) Verify and iterate

- Tracer offers a **verification step** to check the agent's output (07:32–07:52).
- **Incremental testing**: test backend functionality after each phase; provide your **Gemini API key** when needed (07:52–08:46).
- If an issue appears (e.g., wrong REST parameters), the planner specifies the **exact fix** and you re‑run tests (08:46–09:27).

### 4) Handle real‑world quirks

- The attempt to use a single‑call **candidate count** didn't work, so the solution switched to **four separate API calls** (09:50–10:13).

### 5) See it working end‑to‑end

- Prompt: "A cat on a skateboard on a beach at sunset." The app returns **four images** (10:13–10:45).
- Select one, then iterate: "Put a hat on the cat while it's drinking orange juice on a sofa watching TV." You get **four more**; composition stays **similar** to the selected image—minor details may shift (11:08–11:33).

**Takeaway:** You can add new features by adding a **new phase**, describing it, and letting the Plan → Implement → Verify cycle repeat (11:33–11:57).

---

## What Tracer Adds (on top of any agent)

- **VS Code extension** you install in your IDE (03:08–03:29).
- **Two starting modes** (03:51–04:22):
  - Chat to clarify intent and break work into tasks/phases.
  - Generate a **file‑level plan**, refine with AI, then send to an agent for execution.
- **Auto‑research** during planning (web search for docs, endpoints) (05:15–05:41).
- **Verification** of the implementation with context of the original plan (07:32–07:52).
- **Progress tracking** and **no‑regression checks** across phases (09:27–09:50).

> The same technique works in any coding agent. Tracer just makes it smooth and low‑friction (03:08–03:29).

---

## Common Mistakes (and Fixes)

Mistake Why it hurts Fix

|  |  |  |
| --- | --- | --- |
| One giant "build me an app" prompt | Bloated architecture; fragile code; you learn little | Start with a **planning agent**; demand clarifying questions; scope to one feature |
| Letting the agent plan **and** build | No separation of concerns; tough to verify | Use **two agents**: planner vs. implementer; then **verify** against the plan |
| Planning the whole system up front | Over‑commit, then stall | **Atomic phases**; deliver one working slice at a time |
| Skipping verification | Regressions creep in | After each phase, run the **planner's checks** and **incremental tests** |
| Assuming one REST call can do everything | Real APIs have quirks (e.g., candidate count) | Be ready to **adjust tactics** (multiple calls, alternative params) |

---

## Fast Start Checklist

- Choose your **planning agent** and your **implementation agent**.
- Write a **one‑paragraph goal** for the current feature.
- Ask the planner to **interview you**: requirements, constraints, edge cases.
- Approve a **file‑level plan** (filenames + responsibilities).
- Implement with the coding agent; keep diffs small.
- **Verify** with the planner; fix issues; re‑test.
- Repeat for the next feature.

---

## Memorable Lines (with timestamps)

- "**Ask the model to ask you clarifying questions.** That is extremely helpful—especially for your own learning." (01:22–01:45)
- "**Divide the application into atomic parts** and plan those separately while keeping the big picture." (01:45–02:13)
- "**Incremental testing** keeps track of progress and prevents regressions." (07:52–09:27)

---

## FAQ

**Q. Can I do this without Tracer?**
Yes. Use any agent for planning (with web search if possible), a separate agent for implementation, and keep a manual verify checklist after each phase. Tracer bundles these steps into a smooth IDE workflow.

**Q. Why two agents?**
Separation of concerns. The **planner** thinks in requirements and tests; the **implementer** focuses on code. The hand‑off makes verification objective.

**Q. How big is a "phase"?**
Small enough to **demo in minutes**: one endpoint, one UI panel, one background job.

**Q. What if the API feature I want doesn't exist (e.g., candidate count)?**
Adapt. Split work into **multiple calls** or adjust parameters, then document the workaround.

---

## Closing Thought

If you remember one thing: **Plan with one agent, build with another, and verify with the planner—one small feature at a time.** That's how you level up your skills while shipping real software.
