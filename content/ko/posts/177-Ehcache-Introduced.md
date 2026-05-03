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

#### Cache Tiers

1. **In-Memory Cache**: Fastest access, stored in the RAM. Best for frequently accessed data.
2. **Disk Cache**: Slower than in-memory but allows for larger data storage. Used as a secondary layer to the in-memory cache.
3. **Off-Heap Cache**: Stored outside the Java heap, reducing the risk of Java garbage collection pauses.

### Understanding Through an Example

Let's consider a simple example of a Java application using Ehcache.

#### Step-by-Step Example

1. **Adding Ehcache Dependency**:

   ```
   <!-- In your pom.xml for a Maven project -->
   <dependency>
       <groupId>org.ehcache</groupId>
       <artifactId>ehcache</artifactId>
       <version>3.10.0</version>
   </dependency>
   ```
2. **Configuring Ehcache**:

   ```
   <!-- ehcache.xml -->
   <config xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'
           xmlns='http://www.ehcache.org/v3'
           xsi:schemaLocation="http://www.ehcache.org/v3 http://www.ehcache.org/schema/ehcache-core-3.0.xsd">
       <cache alias="myCache">
           <resources>
               <heap unit="entries">100</heap>
               <offheap unit="MB">10</offheap>
               <disk unit="GB">1</disk>
           </resources>
       </cache>
   </config>
   ```
3. **Using Ehcache in Java**:

   ```
   import org.ehcache.Cache;
   import org.ehcache.CacheManager;
   import org.ehcache.config.builders.CacheConfigurationBuilder;
   import org.ehcache.config.builders.CacheManagerBuilder;
   import org.ehcache.config.builders.ResourcePoolsBuilder;

   public class EhcacheExample {
       public static void main(String[] args) {
           CacheManager cacheManager = CacheManagerBuilder.newCacheManagerBuilder()
                   .withCache("preConfigured",
                           CacheConfigurationBuilder.newCacheConfigurationBuilder(Long.class, String.class,
                                   ResourcePoolsBuilder.heap(100)))
                   .build();
           cacheManager.init();

           Cache<Long, String> cache = cacheManager.getCache("preConfigured", Long.class, String.class);

           // Putting data into the cache
           cache.put(1L, "Hello, Ehcache!");

           // Getting data from the cache
           String value = cache.get(1L);
           System.out.println(value);  // Output: Hello, Ehcache!

           cacheManager.close();
       }
   }
   ```

### Conclusion and Summary

Ehcache is a highly efficient caching library for Java applications, designed to enhance performance by minimizing the need to repeatedly access slow data sources. It achieves this by maintaining a fast-access cache in-memory and potentially on-disk, managed through configurable policies and tiers.

### Test Your Understanding

1. What is a cache miss, and how does it affect performance?
2. Describe the difference between in-memory and disk cache.
3. How does Ehcache determine which data to evict when the cache is full?

### Reference

For further reading on Ehcache and its configurations, you can refer to the [Ehcache Official Documentation](https://www.ehcache.org/documentation/3.0/).
