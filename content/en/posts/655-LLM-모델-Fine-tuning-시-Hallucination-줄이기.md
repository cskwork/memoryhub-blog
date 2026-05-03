---
title: "Reducing Hallucinations When Fine-tuning LLM Models - ✨"
date: 2025-06-05T22:41:31+09:00
slug: "655-LLM-모델-Fine-tuning-시-Hallucination-줄이기"
original_url: "https://memoryhub.tistory.com/655"
tistory_id: 655
draft: false
categories: ["Dev Library"]
tags: ["Fine-Tuning"]
---

Have you ever had a strange experience when training a model? When content that definitely isn't in the training data is generated plausibly by the model? Like a student who doesn't know the test answer making something up and pretending to know! 🎭

This phenomenon is called **Hallucination**. According to recent research, hallucination rates among published LLMs range around 3-16%. This problem can become even more severe when fine-tuning smaller models.

## Background

### Past Approach vs Current Challenges

**Past (Pre-LLM Era)**

- Rule-based systems: Output only predefined patterns
- Simple classification models: Generate only limited answers like Yes/No
- Hallucination? Creative responses were impossible in the first place!

**Present (LLM Era)**

- Generative AI: Enable free text generation
- Fine-tuning democratization: Anyone can easily customize models
- Problem emerges: Models "creatively" generate false information! 🚨

Problems that fine-tuning aims to solve:

1. **Dilemma of injecting new knowledge**: Model hallucinations increase when teaching information it doesn't know
2. **Data quality issues**: Low-quality training data increases hallucination frequency
3. **Reduced generalization**: Over-fitting to specific domains causes hallucinations in other areas

## Core Principles

### Understanding the Mechanism of Hallucination 🧠

```
┌─────────────────────┐
│   Pre-trained Model │
│   (existing knowledge)
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐     ┌──────────────────┐
│  Fine-tuning Data   │────▶│  Known Examples  │ ✅ Learn Quickly
│  (training data)    │     │  (familiar data) │
│                     │     └──────────────────┘
│                     │     
│                     │     ┌──────────────────┐
│                     │────▶│ Unknown Examples │ ⚠️ Learn Slowly
│                     │     │ (unfamiliar data)│ → Hallucination Increases!
└─────────────────────┘     └──────────────────┘
```

### Major Hallucination Reduction Techniques

| Technique | Description | Effect | Difficulty |
| --- | --- | --- | --- |
| **Conservative Supervision** | Learn "I don't know" responses | High | Easy |
| **DPO (Direct Preference Optimization)** | Direct preference-based optimization | High | Medium |
| **RLHF/RLAIF** | Reinforcement learning-based feedback | Very High | Hard |
| **TruthX (Layer Selection)** | Selectively train hallucination-related layers | High | Medium |
| **RAG Integration** | Combine with external knowledge search | Very High | Medium |

### Practical Implementation Strategy 🛠️

**1. Data Preprocessing Stage**

```
# Example of classifying data into Known/Unknown
def classify_data(examples, base_model):
    known_examples = []
    unknown_examples = []

    for example in examples:
        # Calculate model's confidence score
        confidence = base_model.get_confidence(example)

        if confidence > 0.8:
            known_examples.append(example)
        else:
            # Change Unknown data label to "I don't know"
            example['answer'] = "I'm sorry. I'm not certain about that information."
            unknown_examples.append(example)

    return known_examples, unknown_examples
```

**2. Fine-tuning Optimization**

- **Learning rate adjustment**: Use lower learning rates for Unknown data
- **Weight assignment**: Assign higher weights to Known data
- **Early stopping**: Stop before Unknown data is over-trained

**3. Prompt Engineering**

```
System prompt example:
"If you don't know the answer to a question or aren't certain, 
never guess. Instead, respond 'I'm not sure about that.'"
```

## Precautions and Tips 🎯

⚠️ **Be Careful About These!**

1. **Trap of injecting new knowledge**
   - Problem: Forcing model to learn information it doesn't know increases hallucinations
   - Solution: Use search-based methods like RAG or train it to answer "I don't know"
2. **Risk of over-fitting**
   - Problem: Over-learning specific domain data alone
   - Solution: Construct balanced datasets from diverse domains
3. **Limitations of evaluation metrics**
   - Problem: Only looking at accuracy can miss hallucination issues
   - Solution: Use hallucination-specific metrics like FActScore, TruthfulQA

💡 **Practical Pro Tips**

- Conservative Supervision is most effective for smaller models!
- DPO is simpler to implement than RLHF with similar effectiveness
- Make sure to understand the base model's knowledge scope before fine-tuning
- Different strategies needed per domain - be especially careful with healthcare/legal!

## Conclusion

We've explored methods to reduce hallucinations when fine-tuning models. Initially it may seem complex, but the core principle is: "Don't force-teach the model information it doesn't know!"

I hope your AI models stop seeing hallucinations and provide trustworthy answers. If you've read this and tried applying it, I'd love to hear about your results in the comments! 🙌

Which technique will you try first? How about starting lightly with Conservative Supervision?

## Reference Materials 📚

- [Extrinsic Hallucinations in LLMs - Lil'Log](https://lilianweng.github.io/posts/2024-07-07-hallucination/)
- [Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations? - arXiv](https://arxiv.org/abs/2405.05904)
- [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://arxiv.org/abs/2403.05612)
- [Key Strategies to Minimize LLM Hallucinations - Turing](https://www.turing.com/resources/minimize-llm-hallucinations-strategy)
- [3 Recommended Strategies to Reduce LLM Hallucinations - Vellum](https://www.vellum.ai/blog/how-to-reduce-llm-hallucinations)

---

#LLM #FineTuning #Hallucination #AI #MachineLearning #DeepLearning
