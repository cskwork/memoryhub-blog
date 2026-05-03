---
title: "Insertion Sort Introduced"
date: 2024-05-27T19:45:05+09:00
slug: "141-Insertion-Sort-Introduced"
original_url: "https://memoryhub.tistory.com/141"
tistory_id: 141
draft: false
categories: ["데브 라이브러리"]
tags: ["DS And Algorithm"]
---

*Insertion sort is a simple and intuitive sorting algorithm that builds a sorted array (or list) one element at a time by comparing each new element to the already sorted elements and inserting it into its correct position.*

### The Big Picture

Think of sorting a hand of playing cards. You pick up the cards one by one and place each new card into the correct position relative to the cards already in your hand. This process of finding the right spot and inserting the card is what insertion sort does.

### Core Concepts

1. **Incremental Building**: The sorted section of the list grows incrementally, one element at a time.
2. **Insertion**: Each new element is placed in the correct position among the previously sorted elements.
3. **Shifting Elements**: If necessary, elements in the sorted section are shifted to make room for the new element.

### Detailed Walkthrough

1. **Start with the first element**: The first element is trivially sorted by itself.
2. **Move to the next element**: Take the next element from the unsorted portion.
3. **Find its correct position**: Compare this element with the elements in the sorted portion, moving from right to left, until you find an element smaller than or equal to it.
4. **Shift elements if needed**: If the new element is smaller than any of the sorted elements, shift those elements to the right.
5. **Insert the new element**: Place the new element in its correct position.
6. **Repeat**: Continue this process for each element until the entire list is sorted.

### Understanding Through an Example

Let's sort the list `[4, 3, 2, 10, 12, 1, 5, 6]` using insertion sort:

1. **Initial state**:

   - Sorted part: `[4]`
   - Unsorted part: `[3, 2, 10, 12, 1, 5, 6]`
2. **Insert `3`**:

   - Compare `3` with `4`. Since `3` is smaller, shift `4` to the right and insert `3` at the start.
   - Result: `[3, 4] | [2, 10, 12, 1, 5, 6]`
3. **Insert `2`**:

   - Compare `2` with `4` and `3`. Shift both to the right and insert `2` at the start.
   - Result: `[2, 3, 4] | [10, 12, 1, 5, 6]`
4. **Insert `10`**:

   - `10` is larger than `4`, so it stays at the end of the sorted section.
   - Result: `[2, 3, 4, 10] | [12, 1, 5, 6]`
5. **Insert `12`**:

   - `12` is larger than `10`, so it stays at the end.
   - Result: `[2, 3, 4, 10, 12] | [1, 5, 6]`
6. **Insert `1`**:

   - Compare `1` with all sorted elements and shift them right.
   - Result: `[1, 2, 3, 4, 10, 12] | [5, 6]`
7. **Insert `5`**:

   - Compare `5` with `12` and `10`, shift them right.
   - Result: `[1, 2, 3, 4, 5, 10, 12] | [6]`
8. **Insert `6`**:

   - Compare `6` with `12` and `10`, shift them right.
   - Result: `[1, 2, 3, 4, 5, 6, 10, 12] | []`

### Conclusion and Summary

Insertion sort works by incrementally building a sorted list, one element at a time. It inserts each new element into its correct position by comparing it with the elements in the sorted section and shifting those elements if necessary. This method is straightforward and efficient for small or nearly sorted datasets but can be inefficient for large lists due to the need for multiple comparisons and shifts.

### Test Your Understanding

1. Describe the basic process of insertion sort.
2. Why might insertion sort be inefficient for large datasets?
3. What happens when an element is inserted into the sorted part of the list?

### Reference

For more details, check out the [Wikipedia page on insertion sort](https://en.wikipedia.org/wiki/Insertion_sort).
