---
title: "JVM Garbage Collection"
date: 2024-06-08T00:16:52+09:00
slug: "223-JVM-Garbage-Collection"
original_url: "https://memoryhub.tistory.com/223"
tistory_id: 223
draft: false
categories: ["데브 언어"]
tags: ["Java"]
---

*The JVM manages memory automatically using a process called garbage collection, which identifies and disposes of objects that are no longer needed, thus freeing up memory.*

### The Big Picture

Imagine you have a magic trash collector in your house that automatically identifies and removes items you no longer use, keeping your house clean without you having to do anything. The JVM's garbage collection system works similarly, automatically managing memory to ensure that your Java program runs efficiently without running out of memory.

### Core Concepts

1. **Heap and Stack Memory**:

   - **Heap**: This is where objects and class instances are stored. It's a large pool of memory used for dynamic allocation.
   - **Stack**: This is used for method execution and local variables. Each thread has its own stack.
2. **Garbage Collection**:

   - The process of automatically identifying and discarding objects that are no longer needed by the program.
   - **Generations**: Memory is divided into different generations (young, old, and permanent generation) to optimize garbage collection.
     - **Young Generation**: Where new objects are allocated. It consists of Eden and Survivor spaces.
     - **Old Generation**: Where long-lived objects are stored.
     - **Permanent Generation (PermGen)**: Used to store metadata required by the JVM. Note that in newer versions of Java, this has been replaced by the Metaspace.

### Detailed Walkthrough

1. **Memory Allocation**:

   - When a new object is created, it is allocated in the Eden space of the Young Generation.
   - If the Eden space is full, a minor garbage collection is triggered.
2. **Minor Garbage Collection**:

   - This process involves collecting garbage from the Young Generation.
   - Objects that are still referenced (alive) are moved to one of the Survivor spaces.
   - Objects that survive multiple minor collections are eventually moved to the Old Generation.
3. **Major Garbage Collection**:

   - This is triggered when the Old Generation becomes full.
   - It involves collecting garbage from both the Young and Old Generations.
   - Major collections are more time-consuming compared to minor collections.
4. **Finalization**:

   - Before an object is garbage collected, its `finalize()` method (if overridden) is called, giving the object a chance to clean up resources.
5. **Mark and Sweep Algorithm**:

   - **Mark Phase**: The garbage collector identifies all reachable objects starting from the root (e.g., active threads, static fields).
   - **Sweep Phase**: It then reclaims the memory occupied by unmarked (unreachable) objects.
6. **Generational Garbage Collection**:

   - By categorizing objects into generations, the JVM optimizes the garbage collection process. Most objects die young, so the Young Generation is collected more frequently.

### Understanding Through an Example

Let's consider a simple scenario:

```
public class Example {
    public static void main(String[] args) {
        String greeting = new String("Hello, World!");
        // 'greeting' is stored in the Young Generation's Eden space.
    }
}
// Once 'greeting' goes out of scope and is no longer referenced, it becomes eligible for garbage collection.
```

1. **Allocation**:

   - `greeting` is created in the Eden space of the Young Generation.
2. **Garbage Collection**:

   - If `greeting` is no longer referenced, during the next minor collection, it might be moved to the Survivor space if it's still needed or collected if it's not.

### Conclusion and Summary

The JVM manages memory automatically using garbage collection, which involves identifying and disposing of objects that are no longer needed. This process includes allocating memory in different generations, performing minor and major collections, and utilizing algorithms like mark and sweep to efficiently reclaim memory.

### Test Your Understanding

1. **What are the different generations in JVM memory management?**
2. **Explain the difference between minor and major garbage collection.**
3. **What happens during the mark and sweep phases of garbage collection?**

### Reference

For further learning, you can refer to the [Java Memory Management and Garbage Collection](https://www.oracle.com/java/technologies/javase/memory-management-whitepaper.html) whitepaper.
