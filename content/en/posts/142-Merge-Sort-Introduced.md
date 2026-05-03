---
title: "Merge Sort Introduced"
date: 2024-05-27T19:46:02+09:00
slug: "142-Merge-Sort-Introduced"
original_url: "https://memoryhub.tistory.com/142"
tistory_id: 142
draft: false
---

*Quick sort is an efficient sorting algorithm that uses a divide-and-conquer approach to organize data by partitioning arrays and recursively sorting the partitions.*

### The Big Picture

Imagine you have a messy room full of books, and you want to organize them on a shelf. Quick sort is like picking a random book (called the "pivot"), then arranging all other books into two piles: those that should come before the pivot and those that should come after. You repeat this process for each pile until the whole room is sorted.

### Core Concepts

1. **Pivot Selection**: Choosing an element from the array as the pivot.
2. **Partitioning**: Rearranging the array so that elements less than the pivot come before it, and elements greater come after it.
3. **Recursion**: Applying the same process to the sub-arrays (or piles) created by partitioning.

### Detailed Walkthrough

1. **Choose a Pivot**: Select an element from the array. This can be the first element, last element, or a random element.
2. **Partition the Array**:
   - Move elements smaller than the pivot to the left of the pivot.
   - Move elements larger than the pivot to the right.
   - The pivot element is now in its correct position.
3. **Recursively Sort Sub-arrays**: Apply the same process to the left and right sub-arrays around the pivot.

Here's a step-by-step breakdown with an example:

#### Step-by-Step Example

Suppose we want to sort the array: `[8, 3, 1, 7, 0, 10, 2]`.

1. **Choose a Pivot**: Let's pick `7`.
2. **Partitioning**:
   - Elements less than `7`: `[3, 1, 0, 2]`
   - Elements greater than `7`: `[8, 10]`
   - Resulting array: `[3, 1, 0, 2, 7, 8, 10]`
3. **Recursively Apply Quick Sort**:
   - Left sub-array `[3, 1, 0, 2]`:
     - Choose pivot: `2`
     - Partition: `[1, 0]`, `[3]`
     - Resulting array: `[1, 0, 2, 3]`
     - Apply quick sort on `[1, 0]`:
       - Pivot: `0`
       - Partition: `[]`, `[1]`
       - Resulting array: `[0, 1]`
   - Right sub-array `[8, 10]`:
     - Pivot: `10`
     - Partition: `[8]`, `[]`
     - Resulting array: `[8, 10]`

After sorting all partitions, we combine them to get the final sorted array: `[0, 1, 2, 3, 7, 8, 10]`.

### Conclusion and Summary

Quick sort organizes data efficiently by:

1. Selecting a pivot.
2. Partitioning the array into two sub-arrays based on the pivot.
3. Recursively sorting the sub-arrays.

By continually dividing the problem and conquering smaller sub-problems, quick sort can sort an array with an average time complexity of (O(n \log n)).

### Test Your Understanding

1. What is the purpose of the pivot in quick sort?
2. Describe the partitioning process in your own words.
3. How does the recursive nature of quick sort help in sorting an array?

### Reference

- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
- [Khan Academy: Quick sort](https://www.khanacademy.org/computing/computer-science/algorithms/quick-sort/a/overview-of-quicksort)
