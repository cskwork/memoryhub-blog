---
title: "Merge Sort Introduced"
date: 2024-05-27T19:46:51+09:00
slug: "143-Merge-Sort-Introduced"
original_url: "https://memoryhub.tistory.com/143"
tistory_id: 143
draft: false
categories: ["데브 라이브러리"]
tags: ["DS And Algorithm"]
---

*Merge sort is an efficient, stable, and comparison-based sorting algorithm that uses a divide-and-conquer approach to sort data by recursively splitting arrays and then merging the sorted sub-arrays.*

### The Big Picture

Imagine you have a deck of cards that you want to sort. Merge sort is like dividing the deck into smaller piles, sorting each pile individually, and then merging the sorted piles back together to form a single, sorted deck.

### Core Concepts

1. **Divide**: Split the array into two halves.
2. **Conquer**: Recursively sort each half.
3. **Merge**: Combine the two sorted halves into a single sorted array.

### Detailed Walkthrough

1. **Divide**:
   - Split the array into two roughly equal halves.
2. **Conquer**:
   - Recursively sort each half.
3. **Merge**:
   - Combine the sorted halves into a single sorted array by comparing the smallest elements of each half and arranging them in order.

Here's a step-by-step breakdown with an example:

#### Step-by-Step Example

Suppose we want to sort the array: `[38, 27, 43, 3, 9, 82, 10]`.

1. **Divide**:
   - Split into `[38, 27, 43]` and `[3, 9, 82, 10]`
2. **Conquer**:
   - Split `[38, 27, 43]` into `[38]` and `[27, 43]`
   - Split `[27, 43]` into `[27]` and `[43]`
   - Recursively sort these to get `[27, 38, 43]`
   - Split `[3, 9, 82, 10]` into `[3, 9]` and `[82, 10]`
   - Split `[3, 9]` into `[3]` and `[9]`
   - Split `[82, 10]` into `[82]` and `[10]`
   - Recursively sort these to get `[3, 9, 10, 82]`
3. **Merge**:
   - Merge `[27, 38, 43]` and `[3, 9, 10, 82]`:
     - Compare `27` and `3`, put `3` first
     - Compare `27` and `9`, put `9` next
     - Compare `27` and `10`, put `10` next
     - Compare `27` and `82`, put `27` next
     - Compare `38` and `82`, put `38` next
     - Compare `43` and `82`, put `43` next
     - Finally put `82`
   - Resulting array: `[3, 9, 10, 27, 38, 43, 82]`

### Understanding Through an Example

Let's merge two sorted arrays `[27, 38, 43]` and `[3, 9, 10, 82]` step by step:

1. Compare the first elements: `27` and `3`. Since `3` is smaller, it's placed in the new array.
2. Compare `27` and `9`. `9` is smaller, so it's placed next.
3. Compare `27` and `10`. `10` is smaller, so it's placed next.
4. Compare `27` and `82`. `27` is smaller, so it's placed next.
5. Continue this process until all elements are merged into the new array.

### Conclusion and Summary

Merge sort organizes data by:

1. Splitting the array into smaller sub-arrays.
2. Sorting each sub-array recursively.
3. Merging the sorted sub-arrays back together.

This process ensures that the data is sorted efficiently, with a time complexity of (O(n \log n)), making it very effective for large datasets.

### Test Your Understanding

1. What are the main steps involved in merge sort?
2. Explain how the merging process works in merge sort.
3. Why is merge sort considered stable and efficient?

### Reference

- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
- [Khan Academy: Merge sort](https://www.khanacademy.org/computing/computer-science/algorithms/merge-sort/a/overview-of-merge-sort)
