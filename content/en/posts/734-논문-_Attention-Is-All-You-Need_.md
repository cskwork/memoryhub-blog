---
title: "Paper \"Attention Is All You Need\""
date: 2025-07-29T23:06:52+09:00
slug: "734-논문-_Attention-Is-All-You-Need_"
original_url: "https://memoryhub.tistory.com/734"
tistory_id: 734
draft: false
---

This article is an easy-to-understand explanation of the 2017 paper "Attention Is All You Need"[[1]](https://arxiv.org/html/1706.03762v7#:~:text=The%20dominant%20sequence%20transduction%20models,large%20and%20limited%20training%20data) published by the Google Brain team. In this paper, the authors propose a new method to solve the **sequence transduction** problem of processing two sentences of different lengths, such as translation.

Traditionally, **Recurrent Neural Networks (RNNs)** that process words in a sentence sequentially were mainly used, but the paper's authors designed a completely different structure using the **attention** mechanism.

This structure is called **Transformer**.

## 1. Sequence Transduction and Existing Methods

- **Sequence transduction** is a problem that produces output with different order and length from input sequences, such as translating an English sentence to German. For this, neural networks consist of an **encoder** that compresses the input and a **decoder** that produces the output[[2]](https://arxiv.org/html/1706.03762v7#:~:text=Most%20competitive%20neural%20sequence%20transduction,input%20when%20generating%20the%20next).

- Traditionally, **RNN** (especially LSTM) and **Convolutional Neural Networks** were used, but these models had to compute sequentially step-by-step according to input position[[3]](https://arxiv.org/html/1706.03762v7#:~:text=Recurrent%20models%20typically%20factor%20computation,The%20fundamental). Because of this **sequential computation**, long sentences are difficult to parallelize and training time is long.

- Attention is a mechanism that allows "focus" on specific parts of the input. Previous models used attention with RNN, but this paper argues that **attention alone is sufficient**[[4]](https://arxiv.org/html/1706.03762v7#:~:text=In%20this%20work%20we%20propose,hours%20on%20eight%20P100%20GPUs).

## 2. What is Attention?

- **Attention** is a function that takes a query, key, and value and calculates weights for how much to focus on each value[[5]](https://arxiv.org/html/1706.03762v7#:~:text=An%20attention%20function%20can%20be,query%20with%20the%20corresponding%20key). When there are multiple values, the **softmax** function determines which value is more important.

- The paper uses fast and memory-efficient **scaled dot-product attention**, and to prevent the problem of values becoming too large causing softmax gradients to vanish, it scales by dividing by a factor:

![](/images/734-논문-_Attention-Is-All-You-Need_/img.png)

[[6]](https://arxiv.org/html/1706.03762v7#:~:text=We%20call%20our%20particular%20attention,the%20weights%20on%20the%20values).

- **Self-attention** allows words in a sentence to reference each other. Instead of a single word, it compares all positions with each other to find out how related one word is to another[[7]](https://arxiv.org/html/1706.03762v7#:~:text=Self,40%2C%2028%20%2C%20%2047).

### 2.1 Multi-Head Attention

Using only a single attention makes it difficult to represent multiple relationships simultaneously. So the authors use **multi-head attention**. They project Queries, keys, and values multiple times with different linear transformations, then perform multiple attentions in parallel and concatenate the results[[8]](https://arxiv.org/html/1706.03762v7#:~:text=Instead%20of%20performing%20a%20single,values%2C%20as%20depicted%20in%20Figure%C2%A02). Using multi-head attention allows the model to simultaneously focus on different semantic subspaces (such as grammar structure, semantic relationships, etc.)[[9]](https://arxiv.org/html/1706.03762v7#:~:text=Multi,attention%20head%2C%20averaging%20inhibits%20this).

## 3. Transformer Architecture

The Transformer has **multiple layers (stacks)** in both encoder and decoder[[10]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,produce%20outputs%20of%20dimension). The main components of each layer are as follows.

### 3.1 Encoder Layer

- Each encoder layer has **two sublayers**. The first is multi-head **self-attention**, and the second is a small **feed-forward neural network** applied identically at each position[[11]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,To%20facilitate%20these%20residual).

- After each sublayer, there are **residual connections** and **layer normalization** to stabilize learning[[12]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,is%20%2C%20where%20is%20the).

### 3.2 Decoder Layer

- The decoder layer has a similar structure but consists of **three sublayers**, unlike the encoder. The first is self-attention over previously generated outputs, the second is attention over the encoder's output (input sentence information), and the third is a feed-forward neural network[[13]](https://arxiv.org/html/1706.03762v7#:~:text=The%20decoder%20is%20also%20composed,at%20positions%20less%20than).

- In the decoder's self-attention, **masking** is applied so the model cannot see **future words**, ensuring it only references parts already generated[[480715253073321†L234-L369]].

### 3.3 Positional Encoding

The Transformer has no structure like RNN or CNN to process order information. Therefore, **sinusoidal positional encoding** composed of sine and cosine waveforms is added to the input embedding to inject word position information[[14]](https://arxiv.org/html/1706.03762v7#:~:text=Since%20our%20model%20contains%20no,9). This method helps the model generalize position relationships beyond sentence length[[15]](https://arxiv.org/html/1706.03762v7#:~:text=We%20also%20experimented%20with%20using,the%20ones%20encountered%20during%20training).

### 3.4 Why Self-Attention?

- Self-attention computes dependencies between all positions **at once in a single layer**, making parallelization easier compared to RNN and CNN[[16]](https://arxiv.org/html/1706.03762v7#:~:text=4%20Why%20Self). RNN is difficult to parallelize on long sentences because it computes sequentially[[3]](https://arxiv.org/html/1706.03762v7#:~:text=Recurrent%20models%20typically%20factor%20computation,The%20fundamental).

- According to the comparison table in the paper, the number of sequential operations in a self-attention layer is **constant**, while RNN increases proportionally with sequence length[[17]](https://arxiv.org/html/1706.03762v7#:~:text=Table%201%3A%20%20Maximum%20path,Report%20issue%20for%20preceding%20element).

- Self-attention has a short **path length** for information flow even in long sentences, making it easier to learn relationships between distant words[[18]](https://arxiv.org/html/1706.03762v7#:~:text=The%20third%20is%20the%20path,networks%20composed%20of%20the%20different).

## 4. Training and Performance

### 4.1 Training Data

The model was trained on approximately 4.5 million sentences for **English→German** translation and 36 million sentences for **English→French** translation[[19]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20on%20the%20standard,a%20set%20of%20sentence%20pairs). Input and output were subdivided into units using a method called **byte-pair encoding** and represented as approximately 30,000 units[[19]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20on%20the%20standard,a%20set%20of%20sentence%20pairs).

### 4.2 Results Comparison

The paper compares the Transformer to existing models while reporting **BLEU score** (translation quality measurement index) and training cost. The following table is a simplified summary of English→German (newstest2014) results[[20]](https://arxiv.org/html/1706.03762v7#:~:text=Report%20issue%20for%20preceding%20element,8).

| Model | BLEU Score | Features |
| --- | --- | --- |
| ByteNet | 23.75 | CNN-based sequence model |
| GNMT + RL | 26.30 | Google's RNN-based model, uses reward learning |
| ConvS2S | 25.16 | CNN-based seq2seq model |
| **Transformer (base)** | **27.3** | 8 multi-head attention, small parameter count |
| **Transformer (big)** | **28.4** | Uses larger dimensions and head count, best performance |

The Transformer's **big model** was **over 2 BLEU points higher** than the previous best model for English→German translation and achieved the best performance for English→French as a single model[[21]](https://arxiv.org/html/1706.03762v7#:~:text=On%20the%20WMT%202014%20English,any%20of%20the%20competitive%20models). Additionally, the Transformer had very fast **training speed**, with the base model training in **12 hours** on 8 GPUs and the big model in **3.5 days**[[22]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20our%20models%20on,5%20days).

### 4.3 Extension to Other Tasks

The Transformer was also applied to **parsing** tasks that analyze sentence structure and demonstrated performance competitive with existing RNN models[[23]](https://arxiv.org/html/1706.03762v7#:~:text=6). Even with limited data, it showed better performance than other models and adapted well to tasks with different structures without additional training[[24]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20a%204,supervised%20setting).

## 5. Conclusion and Significance

- **Innovative Architecture**: The Transformer completely eliminates RNN and CNN, connecting input and output using only the **attention mechanism**[[25]](https://arxiv.org/html/1706.03762v7#:~:text=7%20Conclusion). This became a major turning point in sequence modeling.

- **Parallelization and Speed**: Thanks to the parallel processing of self-attention, training is fast and information can be transmitted efficiently even in long sentences[[16]](https://arxiv.org/html/1706.03762v7#:~:text=4%20Why%20Self).

- **Performance Improvement**: It demonstrated performance exceeding the previous best model in translation tasks[[21]](https://arxiv.org/html/1706.03762v7#:~:text=On%20the%20WMT%202014%20English,any%20of%20the%20competitive%20models) and showed potential for extension to other language tasks like parsing[[24]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20a%204,supervised%20setting).

- **Future Research Directions**: The paper presented several extension plans such as applying the Transformer to different types of data like **images and speech** and researching sparse attention on long sequences[[26]](https://arxiv.org/html/1706.03762v7#:~:text=We%20are%20excited%20about%20the,inputs%20and%20outputs%20such%20as).

## 6. Analogies for Easy Understanding

When studying the Transformer, think of the following analogies:

- **Attention is a highlighter pen**: Just like highlighting important words in a long sentence, attention gives larger weights to important parts when translating from an input sentence.

- **Multi-head attention is multiple colored pens**: Using only one highlighter makes it difficult to represent various types of importance. Using multiple colored highlighters allows you to emphasize different information simultaneously: grammar, semantics, and position[[27]](https://arxiv.org/html/1706.03762v7#:~:text=Instead%20of%20performing%20a%20single,values%2C%20as%20depicted%20in%20Figure%C2%A02).

- **Residual connection is stacking sticky notes**: When combining two pieces of information, the previous information is passed through as-is and new information is added on top. This ensures learning is stable and information is not lost[[11]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,To%20facilitate%20these%20residual).

That concludes an easy and simple overview of the main ideas in the Transformer paper. Today, the Transformer is the most widely used structure in the natural language processing field and forms the core of various AI services including chatbots and translation apps.

---

[[1]](https://arxiv.org/html/1706.03762v7#:~:text=The%20dominant%20sequence%20transduction%20models,large%20and%20limited%20training%20data) [[2]](https://arxiv.org/html/1706.03762v7#:~:text=Most%20competitive%20neural%20sequence%20transduction,input%20when%20generating%20the%20next) [[3]](https://arxiv.org/html/1706.03762v7#:~:text=Recurrent%20models%20typically%20factor%20computation,The%20fundamental) [[4]](https://arxiv.org/html/1706.03762v7#:~:text=In%20this%20work%20we%20propose,hours%20on%20eight%20P100%20GPUs) [[5]](https://arxiv.org/html/1706.03762v7#:~:text=An%20attention%20function%20can%20be,query%20with%20the%20corresponding%20key) [[6]](https://arxiv.org/html/1706.03762v7#:~:text=We%20call%20our%20particular%20attention,the%20weights%20on%20the%20values) [[7]](https://arxiv.org/html/1706.03762v7#:~:text=Self,40%2C%2028%20%2C%20%2047) [[8]](https://arxiv.org/html/1706.03762v7#:~:text=Instead%20of%20performing%20a%20single,values%2C%20as%20depicted%20in%20Figure%C2%A02) [[9]](https://arxiv.org/html/1706.03762v7#:~:text=Multi,attention%20head%2C%20averaging%20inhibits%20this) [[10]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,produce%20outputs%20of%20dimension) [[11]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,To%20facilitate%20these%20residual) [[12]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,is%20%2C%20where%20is%20the) [[13]](https://arxiv.org/html/1706.03762v7#:~:text=The%20decoder%20is%20also%20composed,at%20positions%20less%20than) [[14]](https://arxiv.org/html/1706.03762v7#:~:text=Since%20our%20model%20contains%20no,9) [[15]](https://arxiv.org/html/1706.03762v7#:~:text=We%20also%20experimented%20with%20using,the%20ones%20encountered%20during%20training) [[16]](https://arxiv.org/html/1706.03762v7#:~:text=4%20Why%20Self) [[17]](https://arxiv.org/html/1706.03762v7#:~:text=Table%201%3A%20%20Maximum%20path,Report%20issue%20for%20preceding%20element) [[18]](https://arxiv.org/html/1706.03762v7#:~:text=The%20third%20is%20the%20path,networks%20composed%20of%20the%20different) [[19]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20on%20the%20standard,a%20set%20of%20sentence%20pairs) [[20]](https://arxiv.org/html/1706.03762v7#:~:text=Report%20issue%20for%20preceding%20element,8) [[21]](https://arxiv.org/html/1706.03762v7#:~:text=On%20the%20WMT%202014%20English,any%20of%20the%20competitive%20models) [[22]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20our%20models%20on,5%20days) [[23]](https://arxiv.org/html/1706.03762v7#:~:text=6) [[24]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20a%204,supervised%20setting) [[25]](https://arxiv.org/html/1706.03762v7#:~:text=7%20Conclusion) [[26]](https://arxiv.org/html/1706.03762v7#:~:text=We%20are%20excited%20about%20the,inputs%20and%20outputs%20such%20as) [[27]](https://arxiv.org/html/1706.03762v7#:~:text=Instead%20of%20performing%20a%20single,values%2C%20as%20depicted%20in%20Figure%C2%A02) Attention Is All You Need

<https://arxiv.org/html/1706.03762v7>

[Attention Is All You Need

Provided proper attribution is provided, Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works. Attention Is All You Need \ANDAshish Vaswani Google Brain avaswani@google.com &Noa

arxiv.org](https://arxiv.org/html/1706.03762v7)

[Attention is all You Need.pptx2.13MB](./file/Attention is all You Need.pptx)
