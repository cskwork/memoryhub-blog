---
title: "Save 97% RAG Storage? Memvid vs LEANN, What's Your Choice"
date: 2026-01-17T00:09:28+09:00
slug: "973-RAG-저장공간-97-절약-Memvid-vs-LEANN-당신의-선택은"
original_url: "https://memoryhub.tistory.com/973"
tistory_id: 973
draft: false
---

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║     ┌─────────┐           vs           ┌─────────┐         ║
║     │ MEMVID  │                        │  LEANN  │         ║
║     │ ███████ │                        │ ░░░░░░░ │         ║
║     │ ███████ │   Storage Trade-off    │ ░░░░░░░ │         ║
║     │ ███████ │                        │ ░░░░░░░ │         ║
║     └─────────┘                        └─────────┘         ║
║      [STORED]                          [RECOMPUTE]         ║
║                                                            ║
║       Two Philosophies of RAG Storage Strategy             ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

When building a RAG system, the first problem you hit is embedding storage. Index 100GB of text and the index balloons to 150-700GB. The index is bigger than the original.

Want to run personal AI on your laptop, but the vector DB consumes all your disk?

Two technologies that emerged in 2025 answer this problem in opposite ways.

**Store embeddings or recompute them at query time? This choice determines storage, speed, and operational complexity.**

**One-line summary:** If disk is the bottleneck, LEANN. If operational simplicity matters most, Memvid.

## Background

RAG (Retrieval-Augmented Generation) has become essential for reducing LLM hallucination and leveraging current information. The problem: RAG necessarily involves vector search. Convert text to embedding vectors, store them, find similar vectors.

> Vector index storage overhead is 1.5 to 7 times the original data.

Existing vector DBs (Pinecone, Weaviate, Chroma, etc.) mostly assume "pre-compute and store embeddings." In data center environments, that's rational—storage is cheap, search speed is paramount.

But on personal devices or edge environments, it's different. Index 100GB of personal documents on a 512GB laptop SSD and the index becomes 400GB? Impractical.

Two contrasting approaches emerged in 2025 for this. Memvid says "package in a single file but store embeddings." LEANN says "don't store embeddings at all, compute on-demand."

## Memvid: Everything in a Single File

Memvid's core idea is "portability." Package data, embeddings, search structure, and metadata into one `.mv2` file. Instead of complex RAG pipelines, one file enables search anywhere.

Memvid was inspired by video encoding. It stores text as immutable units called "Smart Frames." Each frame contains content, timestamp, checksum, metadata. Frames are grouped for efficient compression, indexing, parallel reads.

For search, Memvid provides **hybrid search natively**. Supports both BM25-based lexical and HNSW-based semantic search. Local embeddings use ONNX models (BGE, Nomic, etc.), operating completely offline.

Performance improved significantly after v2.0, rewritten in Rust. Official docs claim 10-100x faster than Python. "Sub-5ms local memory access" appears, but note that refers to pure memory access time when cached, not end-to-end latency including embedding computation.

Memvid's limitations are also clear.

**The core design of storing embeddings** means storage issues emerge as corpus grows. With N chunks, d-dimensional FP32 embeddings, you need N × d × 4 bytes just for embeddings. 1M chunks, 768 dimensions = ~3GB. Add HNSW graph metadata.

## LEANN: Don't Store Embeddings

LEANN (Low-Storage Embedding Approximate Nearest Neighbor) takes fundamentally different approach. Don't store embeddings on disk—only **recompute on-the-fly at query time** for visited nodes.

LEANN's core insight: in graph-based indexes like HNSW, a single query actually visits only a fraction of nodes. No need to store all embeddings. Compute only the ones you visit.

Developed by researchers from UC Berkeley, CUHK, AWS, UC Davis, this method uses two key techniques.

First, **two-stage graph traversal and dynamic batching** reduce recomputation latency.

Second, **high-degree node preservation pruning** minimizes graph metadata overhead.

Results are striking. Per the paper, LEANN operates with **less than 5% of original data storage** while achieving 90% top-3 recall. Up to 50x less storage than traditional indexes.

21-200x faster latency than existing recomputation methods like EdgeRAG.

But LEANN has tradeoffs. Recomputing embeddings per query **increases latency**. The paper shows "end-to-end under 2 seconds at 90% top-3 recall." Slow for data centers, but reasonable compared to image/text generation on personal devices taking tens of seconds, researchers argue.

## Storage vs Computation: Trade-offs in Equations

The difference between approaches clarifies with equations. Let N = text chunks, d = embedding dimension, b = bytes per element (4 for FP32).

**Memvid approach (store embeddings) storage:**

```
S_total ≈ S_data + N × d × b + S_graph_metadata
```

**LEANN approach (don't store embeddings) storage:**

```
S_total ≈ S_data + S_pruned_graph (goal: ≤5% of S_data)
```

Query latency differs too.

**Memvid query latency:**

```
T ≈ T_embed_query + T_hnsw_search
```

**LEANN query latency:**

```
T ≈ T_graph_traversal + |C| × T_embed + T_rerank
```

Here |C| is the number of candidate nodes needing recomputed embeddings during traversal. LEANN optimizes this via batching and pruning.

## When to Choose What

| Situation | Recommended | Why |
| --- | --- | --- |
| Storage is hard constraint (laptop, edge) | LEANN | 5% of original storage |
| Single-file deployment, git/scp needed | Memvid | Complete in one .mv2 file |
| Hybrid search (BM25+vector) essential | Memvid | Built-in |
| Large corpus (10M+ chunks) | LEANN | Avoids linear storage growth |
| Fast response speed paramount | Memvid | No recomputation overhead |
| Fully offline operation required | Both viable | Support local embedding models |

In real projects, first understand data scale. 1M chunks, 768 dims, FP32: Memvid needs ~3GB for embeddings alone. LEANN needs ~5% of original.

500 bytes per chunk average: original 500MB, LEANN index ~25MB.

Response speed also matters. Memvid: millisecond responses. LEANN: ~2 seconds at 90% recall. Memvid suits real-time chatbots; LEANN suits batch search or non-real-time workloads.

## Best Practices and Pattern Comparison

| Pattern | Advantage | Caution |
| --- | --- | --- |
| Memvid + local ONNX embeddings | Fully offline, simple config | Storage explodes on large corpus |
| LEANN + small embedding model | Extreme storage savings, edge deployment | Query latency increases |
| Memvid + hybrid search | Simultaneous keyword+semantic | Index size further increases |
| LEANN + hot caching | Cache frequently accessed embeddings, reduce latency | Memory usage increases |

## Conclusion

- Memvid and LEANN are opposite answers to RAG storage. One stores everything but optimizes packaging; the other avoids storage entirely.
- Both are new 2025 projects. Production deployment requires benchmarking and edge case validation.
- Practical tip: Calculate your corpus size and device constraints first, verify expected storage is manageable, then choose your technology.

## References

- Memvid Official GitHub (<https://github.com/memvid/memvid>)
- LEANN: A Low-Storage Vector Index Paper (<https://arxiv.org/abs/2506.08276>)
- LEANN Official GitHub (<https://github.com/yichuan-w/LEANN>)
- Memvid Official Website (<https://memvid.com/>)
- UC Berkeley Sky Computing Lab - LEANN Project (<https://sky.cs.berkeley.edu/project/leann/>)
