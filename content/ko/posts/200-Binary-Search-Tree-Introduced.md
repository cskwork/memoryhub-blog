---
title: "Binary Search Tree Introduced"
date: 2024-06-06T07:34:33+09:00
slug: "200-Binary-Search-Tree-Introduced"
original_url: "https://memoryhub.tistory.com/200"
tistory_id: 200
draft: false
categories: ["데브 라이브러리"]
tags: ["DS And Algorithm"]
---

*In this explanation, we will delve into the concept of a Binary Search Tree (BST), starting with a big-picture analogy, followed by core concepts, a detailed walkthrough, an example, a conclusion, and a test to gauge understanding.*

### The Big Picture

Imagine a library where books are arranged in a very specific way to make it easy to find any book quickly. Each shelf represents a decision point: if you're looking for a book and it’s alphabetically before the book on that shelf, you go to the left; if it's after, you go to the right. This efficient way of organizing books is analogous to how a Binary Search Tree (BST) organizes data for quick search, insertion, and deletion.

### Core Concepts

- **Binary Tree**: A tree data structure where each node has at most two children, referred to as the left child and the right child.
- **Binary Search Tree (BST)**: A type of binary tree where the left child of a node contains only nodes with values less than the parent node, and the right child contains only nodes with values greater than the parent node.
- **Node**: An element of the tree that contains a value, and pointers to its left and right children.

### Detailed Walkthrough

#### Structure of a BST

1. **Node Structure**: Each node in a BST contains:

   - A value.
   - A reference to its left child.
   - A reference to its right child.
2. **Properties**:

   - For any node, all values in its left subtree are less than its value.
   - For any node, all values in its right subtree are greater than its value.

#### Operations

1. **Search**:

   - Start at the root.
   - If the value is equal to the node’s value, return the node.
   - If the value is less, move to the left child.
   - If the value is greater, move to the right child.
   - Repeat until the value is found or the subtree is empty.
2. **Insertion**:

   - Start at the root.
   - Compare the value to be inserted with the current node.
   - If less, move to the left child; if greater, move to the right child.
   - When a null spot is found (either left or right child of a leaf node), insert the new node there.
3. **Deletion**:

   - **Leaf Node**: Simply remove the node.
   - **Node with One Child**: Replace the node with its child.
   - **Node with Two Children**: Find the in-order predecessor (maximum value in the left subtree) or in-order successor (minimum value in the right subtree), replace the node’s value with that value, and then delete that value from the subtree.

### Understanding Through an Example

Consider the following sequence of numbers to insert into a BST: [50, 30, 70, 20, 40, 60, 80]

#### Insertion Process:

1. Insert 50:

   ```
   50
   ```
2. Insert 30:

   ```
     50
    /
   30
   ```
3. Insert 70:

   ```
     50
    /  \
   30  70
   ```
4. Insert 20:

   ```
       50
      /  \
     30  70
    /
   20
   ```
5. Insert 40:

   ```
       50
      /  \
     30  70
    / \
   20  40
   ```
6. Insert 60:

   ```
       50
      /  \
     30  70
    / \  /
   20  40 60
   ```
7. Insert 80:

   ```
       50
      /  \
     30  70
    / \  / \
   20  40 60 80
   ```

#### Search Example:

To search for the value 60:

- Start at 50 (root): 60 > 50, go right.
- At 70: 60 < 70, go left.
- At 60: found.

### Conclusion and Summary

A Binary Search Tree (BST) is a data structure that allows for efficient searching, insertion, and deletion operations by maintaining a specific order among its elements. Each node in the BST ensures that values in the left subtree are less and values in the right subtree are greater, facilitating quick lookups.

### Test Your Understanding

1. Why is a BST more efficient than a linked list for search operations?
2. What happens to the performance of a BST if the inserted elements are in sorted order?
3. Can you write a function in Python to insert a value into a BST?

### Reference

For further reading on Binary Search Trees, you can refer to:

- [Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein](https://mitpress.mit.edu/books/introduction-algorithms)
- [GeeksforGeeks on Binary Search Trees](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)
