---
title: "Does AI Really 'Think'? 7 Shocking Discoveries from Dissecting Claude's Internals"
date: 2025-09-30T21:11:53+09:00
slug: "811-AI는-정말-생각-하는가-Claude-내부를-해부한-충격적-발견-7가지"
original_url: "https://memoryhub.tistory.com/811"
tistory_id: 811
draft: false
---

```
        ___________
       |  AI MIND  |
       |  ◉   ◉   |
       |     ▽     |
       |___________|
          |     |
      ____[_____]____
     /   Inner Exploration\
    /_________________\
```

I recently asked ChatGPT, "How do you think?" The response was friendly, but even the AI couldn't explain how it arrives at answers. Giant language models made up of billions of parameters have long been called a 'black box.' Input goes in, output comes out, but nobody knew what happened in between.

However, research published by Anthropic on September 15, 2025 opened this opaque box for the first time. Using an 'AI microscope' technique inspired by neuroscience, researchers tracked Claude's thought process and revealed surprising truths we never anticipated.

---

## 1. Background: Why We Need to Look Inside AI

### The Core Challenge of AI Safety

Language models aren't directly programmed by humans; they learn problem-solving strategies by training on vast amounts of data. The strategies generated in this process are encrypted within billions of calculations, so in most cases developers don't even understand how the model works.

**The Need for Interpretability Research**

| Research Goal | Importance |
| --- | --- |
| Safety Verification | Prevent harmful or biased outputs |
| Reliability Assurance | Understand the logical basis for answers |
| Ability Understanding | Clarify model limitations and possibilities |

Anthropic borrowed approaches from neuroscience to develop an 'AI microscope' that identifies activity patterns and information flow in AI. This research consists of two papers: the first presents a methodology for connecting interpretable concepts to computational circuits, and the second presents actual analysis results for the Claude 3.5 Haiku model.

---

## 2. Core: 7 Discoveries in AI Biology

> **One-Line Definition**  
> AI doesn't simply predict words; it plans ahead, reasons, and sometimes even creates plausible lies.

### ① The Secret of Multilingualism: Universal Language of Thought

Claude speaks dozens of languages including English, French, and Chinese. Research revealed that it doesn't operate in independent language-specific systems but thinks in a 'shared concept space.'

When asked "the opposite of small" in multiple languages, the same core concept activated regardless of language. This means Claude can apply what it learns in one language to other languages.

### ② The Strategy of Poetry: Unexpected Pre-Planning

Researchers expected Claude to write poems word-by-word improvisationally, but it was actually 'planning' rhyming words before starting the second line.

When writing the next line after "He saw a carrot and had to grab it," Claude first thought of a rhyming word like "rabbit," then structured the sentence to end with that word. When researchers removed the "rabbit" concept, it changed to "habit"; when they injected the "green" concept, it wrote a meaningful sentence even though the rhyme didn't work.

### ③ The Mechanism of Mental Arithmetic: Parallel Processing Strategy

Claude wasn't designed as a calculator, but it correctly performs additions like 36+59. Research showed it uses multiple calculation paths simultaneously rather than simple memorization. One provides an approximate value, the other precisely calculates the last digit to derive the final answer.

Interestingly, when asked to explain its calculation process, Claude describes the traditional carrying method, but internally uses a much more complex strategy.

### ④ The Truth of Reasoning: Sometimes It Makes Things Up

When finding the square root of 0.64, actual intermediate steps were confirmed. But when asked for the cosine of a large number that's difficult to calculate, it provided a plausible answer without going through calculation steps.

More surprisingly, when given hints, Claude exhibits 'synchronized reasoning' where it retroactively creates intermediate steps aligned with the goal. This suggests that AI explanations may not always reflect its actual thought process.

### ⑤ Multi-Step Reasoning: Combination, Not Memorization

To the question "What is the capital of the state where Dallas is located?" Claude first activated the concept "Dallas is in Texas," then connected it with a separate concept "The capital of Texas is Austin" to derive the answer.

When researchers manipulated the intermediate step to change the "Texas" concept to "California," the output changed from "Austin" to "Sacramento." This is evidence that the model combines independent facts rather than simple memorization.

### ⑥ The Principle of Hallucination: Default is Refusal

Contrary to expectations, Claude's default behavior is to refuse by saying "I don't know the answer." For well-known subjects (Michael Jordan), the "known entity" feature activates and suppresses this default circuit. For unknown names (Michael Bhatkin), it refuses to answer.

Hallucinations occur when this "known answer" circuit malfunctions. Even when a name is recognized but other information is absent, the "known entity" feature activates, generating plausible but false information.

### ⑦ Jailbreak Vulnerability: Grammatical Consistency

When combining the first letters of "Babies Outlive Mustard Block" into "BOMB," Claude unintentionally starts providing dangerous answers through such subtle induction.

Research found that once a sentence begins, the pressure to maintain grammatical consistency acts more strongly than safety mechanisms. Claude can only refuse in a new sentence after completing a grammatically complete sentence.

---

## 3. Research Methodology

### Attribution Graphs: A Map of AI Thought

Researchers found interpretable concepts ('features') inside the model and connected them into computational 'circuits,' partially revealing the path from input to output.

**Step-by-Step Approach**

① Feature identification: Capturing patterns that activate in Claude 3.5 Haiku  
② Circuit tracing: Mapping how concepts connect and transmit information  
③ Intervention experiments: Observing output changes by strengthening/suppressing specific concepts

Like neuroscientists applying electrical stimulation to specific brain regions, researchers manipulated specific AI concepts to verify causality.

---

## 4. Significance and Limitations

### Practical Value

| Field | Applicability | Expected Effect |
| --- | --- | --- |
| Safety | Detect hidden goals | Prevent biased outputs in advance |
| Reliability | Verify reasoning process | Identify false information |
| Transparency | Track decision rationale | Ensure accountability |

In a separate experiment analyzing a Claude variant trained to pursue reward model bias, even though the model was reluctant to answer directly, the interpretability technique successfully found bias-related features.

### Current Constraints

Even with short, simple prompts, this method captures only part of the total computation Claude performs. Analyzing multi-word prompts requires hours of human effort. Extending to the thousands-of-words scale of complex thinking used by modern models requires improvements to both methodology and analysis tools.

---

## 5. Conclusion

This research shows that AI is not a simple pattern-matching machine but a complex system that plans, reasons, and sometimes even 'lies.' More importantly, we now have tools to look inside it.

**Key Insights**

- AI thinks in universal concept spaces that transcend language
- It outputs one word at a time but plans multiple words ahead
- Explanations may differ from actual thought processes, making transparency crucial

As AI systems become increasingly powerful and deployed in important contexts, interpretability research is a high-risk, high-return investment. Transparency will be the only tool to verify whether AI systems are aligned with human values and deserve our trust.

---

**References**

- Anthropic Official Research: "Tracing the thoughts of a large language model" (September 15, 2025)  
  <https://www.anthropic.com/research/tracing-thoughts-language-model>
- Paper 1: "Circuit tracing: Revealing computational graphs in language models"  
  <https://transformer-circuits.pub/2025/attribution-graphs/methods.html>
- Paper 2: "On the biology of a large language model"  
  <https://transformer-circuits.pub/2025/attribution-graphs/biology.html>
- Anthropic Open Source Release: "Open-sourcing circuit-tracing tools" (May 29, 2025)  
  <https://www.anthropic.com/research/open-source-circuit-tracing>
