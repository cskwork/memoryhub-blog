---
title: "CI LAW - RAG"
date: 2025-08-26T22:09:56+09:00
slug: "762-CI-LAW-RAG"
original_url: "https://memoryhub.tistory.com/762"
tistory_id: 762
draft: false
categories: ["Life"]
tags: ["CI Laws"]
---

## Top 10 Laws of Contextual Retrieval

|  |  |  |  |
| --- | --- | --- | --- |
| **1** | **200K Token Threshold Law** | If knowledge base < 200,000 tokens (~500 pages), skip RAG entirely and use full context in prompt | Eliminates complexity for smaller datasets |
| **2** | **Context Preservation  Principle** | Traditional RAG destroys crucial context when chunking documents, causing retrieval failures | Core problem that contextual retrieval solves |
| **3** | **Contextual  Enhancement Rule** | Prepend chunk-specific explanatory context (50-100 tokens) before embedding each chunk | 35% reduction in retrieval failures |
| **4** | **Hybrid Retrieval Law** | Combine semantic embeddings with BM25 lexical matching for comprehensive search coverage | Balances semantic understanding with exact matches |
| **5** | **49% Performance  Improvement Rule** | Contextual Embeddings + Contextual BM25 together reduce retrieval failures by 49% | Significant measurable improvement |
| **6** | **Reranking Amplification Principle** | Adding reranking step after contextual retrieval achieves 67% failure reduction | Maximum performance boost when combined |
| **7** | **Top-20 Chunk Optimization Law** | Using 20 chunks outperforms 5 or 10 chunks for model context | Sweet spot for information vs. distraction |
| **8** | **$1.02 Cost-Effectiveness Rule** | Prompt caching enables contextual retrieval at $1.02 per million document tokens | Makes the technique economically viable |
| **9** | **Embedding Model  Hierarchy Principle** | Gemini and Voyage embeddings significantly outperform other tested models | Choose the right embedding foundation |
| **10** | **Stacking Benefits Law** | All techniques (contextual embeddings + BM25 + reranking) combine multiplicatively, not additively | Compound improvements when layered together |

## Alternative Approaches

- **Simple Solution**: For small datasets, use prompt caching with full context instead of complex RAG
- **Domain-Specific Optimization**: Customize contextualizer prompts with domain glossaries and terminology

---

**? The Golden Rule: Context is king - never sacrifice meaningful context for computational efficiency, as it directly determines retrieval success.**

**<https://www.anthropic.com/engineering/contextual-retrieval>**

[Contextual Retrieval in AI Systems

Explore how Anthropic enhances AI systems through advanced contextual retrieval methods. Learn about our approach to improving information access and relevance in large language models.

www.anthropic.com](https://www.anthropic.com/engineering/contextual-retrieval)
