---
title: "Ehcache Introduced"
date: 2024-06-02T14:56:57+09:00
slug: "177-Ehcache-Introduced"
original_url: "https://memoryhub.tistory.com/177"
tistory_id: 177
draft: false
---

*Ehcache is a robust, standards-based caching solution for Java applications, designed to improve performance by reducing the frequency and latency of accessing data.*

### The Big Picture

Imagine you have a library where students frequently request the same books. Instead of fetching these books from a distant warehouse every time, you keep popular books on a nearby shelf for quick access. Ehcache works similarly for Java applications by storing frequently accessed data in a fast, nearby "cache," reducing the need to fetch it repeatedly from a slower "warehouse" (like a database).

### Core Concepts

1. **Caching**: Storing copies of data in a temporary storage area to improve retrieval times.
2. **Cache Store**: The storage location for the cached data, which can be in-memory or on-disk.
3. **Cache Miss**: Occurs when the requested data isn't found in the cache, necessitating a fetch from the primary data store.
4. **Cache Hit**: Happens when the requested data is found in the cache, allowing for faster retrieval.

### Detailed Walkthrough

#### How Ehcache Works

1. **Cache Configuration**: Define how the cache behaves, including its size, eviction policies, and storage tiers (e.g., memory and disk).
2. **Cache Operations**: Interact with the cache through basic operations like put (add data to the cache), get (retrieve data from the cache), and remove (delete data from the cache).
3. **Eviction Policies**: Determine how Ehcache decides which data to remove when the cache is full. Common policies include Least Recently Used (LRU), Least Frequently Used (LFU), and First In, First Out (FIFO).
