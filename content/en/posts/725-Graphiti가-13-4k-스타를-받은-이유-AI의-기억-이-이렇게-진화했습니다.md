---
title: "Why Did Graphiti Get 13.4k Stars? Here's How AI Memory Has Evolved"
date: 2025-07-18T02:54:29+09:00
slug: "725-Graphiti가-13-4k-스타를-받은-이유-AI의-기억-이-이렇게-진화했습니다"
original_url: "https://memoryhub.tistory.com/725"
tistory_id: 725
draft: false
---

```
    ? ──→ ? ──→ ⚡
   AI     Graph   Real-time
   Agent  Memory  Updates
    ↑       ↑       ↑
    └───────┼───────┘
           ?
        Graphiti
```

# 

Have you ever had this experience with ChatGPT? After chatting a few times, you realize it forgot something you mentioned earlier and you have to explain it again. I ran into the same problem when building a project management AI bot. Whenever a user said "that feature you mentioned last time," the AI would have no clue and have to ask from scratch.

Recently, I was pleasantly surprised to discover **Graphiti**, an open source released by Zep, solving this problem in a completely different way. Rather than simply storing conversation history, it builds a **knowledge graph** of relationships and facts that change over time. The idea was truly innovative.

⚡ **TL;DR**: Graphiti is an open source framework that enables AI agents to remember and reason about information that changes over time. It goes beyond simple conversation storage to track changes in relationships and facts, making it possible to build smarter AI.

## Table of Contents

1. Background: Why temporal knowledge graphs now?
2. Core concepts explained
3. Hands-on: How Graphiti works
4. Best practices and use cases
5. Conclusion & References

---

## 1. Background: Why Temporal Knowledge Graphs Now?

The existing RAG (Retrieval-Augmented Generation) approach relies on batch processing and static data summarization, making it inefficient for frequently changing data. For example, suppose you have a customer service AI. When a customer's preferences change or their subscription status updates, the traditional approach required reprocessing all data.

Microsoft's GraphRAG extended text chunking to graphs, but it was designed for static documents and couldn't handle the temporal dimension.

**Key problems Graphiti solves:**

✅ **Real-time updates**: New data integrated instantly without batch recalculation  
✅ **Bidirectional time model**: Tracks event time and input time separately  
✅ **Hybrid search**: Combines semantic embeddings, keyword search (BM25), and graph traversal

---

## 2. Core Concepts Explained

> **Temporal Knowledge Graph**  
> A knowledge structure that tracks and records how relationships between entities change over time

Graphiti consists of three levels of subgraphs: Episode Subgraph (raw input data), Entity Subgraph (extracted entities), and a structure representing relationships between them.

**Key components:**

**Episode**: A unit of raw data (messages, JSON, text)

- Acts as a lossless data store
- Stored with timestamps

**Entity**: People, places, concepts, etc.

- Concrete objects like "Kim Min-su," "Seoul," "Project A"

**Edge**: Connections between entities

- "Kim Min-su lives in Seoul"
- Includes temporal metadata (valid_at, invalid_at)

```
# Simple fact example
fact = "Kim Min-su is the marketing team lead"
# Time passes...
updated_fact = "Kim Min-su is the development team lead"
# → Graphiti automatically tracks these changes!
```

---

## 3. Hands-on: How Graphiti Works

**① Installation and setup**

You'll need a Neo4j database and OpenAI API key. The easiest way is to use Neo4j Desktop.

```
# Basic installation
pip install graphiti-core

# Support for various LLMs
pip install graphiti-core[anthropic,groq,google-genai]
```

**② Data input and graph construction**

Graphiti handles both unstructured text and structured data, enabling queries that combine time, full text, semantic search, and graph algorithms.

**③ Search and reasoning**

It supports semantic, keyword, and graph-based search all with fast retrieval speeds under 100ms.

---

## 4. Best Practices and Use Cases

Graphiti enables long-term memory and state-based reasoning across diverse fields: sales, customer service, healthcare, finance, and more.

Use Case | Benefits | Concrete Examples
---|---|---
**Personalized Assistant** | Learn from user interactions | Track preference changes, personalized recommendations
**Customer Service** | Maintain contextual conversations | Remember previous inquiries, resolution processes
**Sales Support** | Track customer relationships | Monitor purchase history, preference changes
**Project Management** | Track state changes | Record progress, staffing changes

**Real results**: Graphiti demonstrated superior performance compared to MemGPT on the Deep Memory Retrieval (DMR) benchmark.

**Notable features:**

? **Smart graph updates**: Automatically compares new entities with existing graphs to reflect latest context  
? **Rich edge semantics**: Human-readable semantic representation improves search performance and interpretability  
⚡ **Performance optimization**: Search results typically return in under 100ms, with latency mainly determined by third-party embedding API calls

---

## 5. Conclusion

Looking at Graphiti, I'm convinced the paradigm of AI memory is changing. AI capable of understanding how relationships change and the flow of time is now possible, going beyond simply storing conversations. The ability to track how data changes over time, hybrid search capabilities, and scalable data processing are the key points.

In particular, achieving 13.4k GitHub stars in just 8 months with over 35 contributors and 25,000 weekly PyPI downloads shows how eagerly developers have been waiting for this technology.

When applying it to actual projects, I recommend starting gradually while considering Neo4j configuration and LLM API costs.

⸻

## References

• [Graphiti official GitHub](https://github.com/getzep/graphiti) - Open source repository with 13.4k stars  
• [Zep official documentation](https://help.getzep.com/graphiti/graphiti/overview) - Detailed guides and API documentation  
• [Research paper: "Zep: A Temporal Knowledge Graph Architecture for Agent Memory"](https://www.themoonlight.io/ko/review/zep-a-temporal-knowledge-graph-architecture-for-agent-memory) - Technical background and benchmark results

---

**Glossary**

? **Knowledge graph**: Like a map with lines connecting friendships, a picture showing connections between pieces of information  
⏰ **Temporal**: The ability to remember things that change over time, like how yesterday differs from today  
? **Entity**: Anything that can be named, like people, places, and things  
? **Episode**: Like a daily entry in a diary, an event or piece of information that happened at one point in time
