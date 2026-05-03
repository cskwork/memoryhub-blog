---
title: "Transformers in LLMs Introduced"
date: 2024-05-26T10:39:03+09:00
slug: "89-Transformers-in-LLMs-Introduced"
original_url: "https://memoryhub.tistory.com/89"
tistory_id: 89
draft: false
categories: ["데브 라이브러리"]
tags: ["Machine Learning"]
cover:
  image: "images/89-Transformers-in-LLMs-Introduced/img.png"
  relative: false
  hidden: false
---

*Transformers in Large Language Models (LLMs) work by processing text through layers that handle both the sequential nature of language and long-range dependencies using self-attention mechanisms.*

---

### **The Big Picture**

Imagine you are trying to understand a complex story with multiple characters and subplots. If you were to read it linearly, you might miss important connections between events. Instead, you periodically review and cross-reference different parts of the story to see how they relate. This is similar to how transformers work in Large Language Models (LLMs). They don't just read text in order but also look back and forth within the text to understand the relationships between words and phrases.

### **Core Concepts**

1. **Self-Attention Mechanism**: This is like our ability to pay attention to different parts of a story simultaneously to understand the whole narrative.
2. **Positional Encoding**: Words in a sentence have a specific order, and this encoding helps the model understand the position of each word.
3. **Multi-Head Attention**: This allows the model to focus on different parts of the sentence at the same time, akin to having multiple highlighters for various themes in a story.
4. **Feedforward Neural Networks**: After understanding relationships between words, these networks process this information further to draw more complex insights.

### **Detailed Walkthrough**

### **1. Self-Attention Mechanism**

![](/images/89-Transformers-in-LLMs-Introduced/img.png)

Think of the self-attention mechanism as a way to measure how important each word is in relation to every other word in a sentence. If you have a sentence, "I kicked the ball," the model evaluates how each word is connected. For instance, it learns that "I" is closely related to "kicked" and "ball."

**Steps of Self-Attention**:

- **Query, Key, Value Vectors**: Each word in the sentence is transformed into three vectors. These vectors help determine the relationships between words.
- **Attention Scores**: The model calculates scores to see how much focus each word should get relative to others.
- **Weighted Sum**: These scores are used to compute a weighted sum of the value vectors, highlighting important words

![](/images/89-Transformers-in-LLMs-Introduced/img_1.png)

### **2. Positional Encoding**

Since transformers don't inherently understand word order, positional encoding adds information about the position of each word in a sentence. This is crucial because "I kicked the ball" is different from "The ball kicked I"

**How It Works**:

- **Sine and Cosine Functions**: These functions are used to create unique encodings for each position. This way, the model can distinguish between the first, second, and nth word in a sentence.

### **3. Multi-Head Attention**

Imagine you have several perspectives to view a story, each highlighting different elements such as characters, setting, or plot twists. Multi-head attention allows the model to look at various aspects of the sentence simultaneously.

**Benefits**:

- **Diverse Insights**: Each "head" focuses on different relationships and patterns in the data.
- **Parallel Processing**: It makes the model more robust and capable of understanding complex interactions.

### **4. Feedforward Neural Networks**

After the model gathers relational information through attention mechanisms, it passes this data through feedforward neural networks. These networks process the information further to derive deeper meanings and make predictions.

### **Understanding Through an Example**

Let's take a simple sentence: "The quick brown fox jumps over the lazy dog."

1. **Self-Attention**: The model calculates how each word relates to every other word. "Fox" might have strong connections with "jumps" and "over."
2. **Positional Encoding**: Adds position information to each word.
3. **Multi-Head Attention**: Different attention heads might focus on different parts of the sentence, like one head focusing on the "quick brown fox" and another on "lazy dog."
4. **Feedforward Neural Networks**: Further process the information to understand the overall meaning and context.

### **Conclusion and Summary**

Transformers in LLMs work by leveraging self-attention mechanisms to understand relationships between words beyond their immediate neighbors. Positional encoding ensures the model recognizes word order, while multi-head attention allows it to analyze different aspects of the text simultaneously. Finally, feedforward neural networks process this information to generate coherent and contextually accurate outputs.

### **Test Your Understanding**

1. What is the purpose of self-attention in transformers?
2. How does positional encoding help transformers understand word order?
3. Why is multi-head attention beneficial in analyzing sentences?
4. What role do feedforward neural networks play after the attention mechanisms?

### **Reference**

- Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30. [Paper link](https://arxiv.org/abs/1706.03762)
- <https://towardsdatascience.com/transformers-141e32e69591>

### Reference
