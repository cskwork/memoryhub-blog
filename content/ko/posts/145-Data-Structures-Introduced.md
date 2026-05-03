---
title: "Data Structures Introduced"
date: 2024-05-27T20:18:08+09:00
slug: "145-Data-Structures-Introduced"
original_url: "https://memoryhub.tistory.com/145"
tistory_id: 145
draft: false
categories: ["데브 라이브러리"]
tags: ["DS And Algorithm"]
---

*Data structures are organized ways to store, manage, and retrieve data efficiently, enabling various operations such as insertion, deletion, and traversal to be performed optimally.*

### The Big Picture

Imagine you have a huge collection of books in a library. To find a specific book quickly, you would organize the books systematically, such as by genre, author, or title. Similarly, in computer science, data structures provide different ways to organize, manage, and store data so that it can be accessed and modified efficiently.

### Core Concepts

1. **Linear Data Structures**: Data elements are arranged in a sequential manner.
2. **Non-linear Data Structures**: Data elements are arranged in a hierarchical or interconnected manner.

### Detailed Walkthrough

#### Linear Data Structures

1. **Arrays**:

   - Fixed-size structure.
   - Stores elements in contiguous memory locations.
   - Allows direct access via index.
   - Example: `[1, 2, 3, 4, 5]`
   - Analogy: Think of an array as a row of lockers, each with a unique number.
2. **Linked Lists**:

   - Dynamic size.
   - Consists of nodes where each node contains data and a reference (or link) to the next node.
   - Types: Singly linked list, doubly linked list, circular linked list.
   - Example: `1 -> 2 -> 3 -> 4 -> 5`
   - Analogy: Like a treasure hunt where each clue (node) leads you to the next clue.
3. **Stacks**:

   - Follows Last In First Out (LIFO) principle.
   - Operations: `push` (add an element), `pop` (remove an element).
   - Example: Stack of plates where you can only take the top plate off.
   - Analogy: Think of a stack as a pile of plates; you can only add or remove the top plate.
4. **Queues**:

   - Follows First In First Out (FIFO) principle.
   - Operations: `enqueue` (add an element), `dequeue` (remove an element).
   - Example: Line of people waiting for a bus.
   - Analogy: Like a line at a checkout counter; the first person in line is the first to be served.

#### Non-linear Data Structures

1. **Trees**:

   - Hierarchical structure.
   - Consists of nodes where each node has a value and children nodes.
   - Types: Binary tree, binary search tree, AVL tree, etc.
   - Example: Family tree.
   - Analogy: Imagine a tree where each branch (node) leads to other branches.
2. **Graphs**:

   - Consists of nodes (vertices) connected by edges.
   - Can represent various relationships and connections.
   - Types: Directed, undirected, weighted, unweighted.
   - Example: Social network.
   - Analogy: Think of a graph as a map of cities (nodes) connected by roads (edges).

### Understanding Through an Example

Let's consider an example of how a stack works in a programming context. Here’s a simple stack implementation in Python:

```
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Outputs: 3
print(stack.pop())  # Outputs: 2
print(stack.peek())  # Outputs: 1
```

### Conclusion and Summary

Data structures are essential for organizing and managing data efficiently. They come in various forms, each suited to specific types of operations and use cases. Linear structures like arrays and linked lists organize data sequentially, while non-linear structures like trees and graphs arrange data hierarchically or in networks.

### Test Your Understanding

1. What is the primary difference between a stack and a queue?
2. How does a binary search tree differ from a general tree?
3. Can you write a function to traverse a linked list and print all its elements?

### Reference

- "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein
- [GeeksforGeeks: Data Structures](https://www.geeksforgeeks.org/data-structures/)
