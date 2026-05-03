---
title: "Tree Breadth-First Search & Tree Depth-Frist Search"
date: 2024-06-06T07:37:00+09:00
slug: "202-Tree-Breadth-First-Search-Tree-Depth-Frist-Search"
original_url: "https://memoryhub.tistory.com/202"
tistory_id: 202
draft: false
---

*In this explanation, we will delve into the concepts of Tree Breadth-First Search (BFS) and Tree Depth-First Search (DFS), starting with a big-picture analogy, followed by core concepts, a detailed walkthrough, examples, a conclusion, and a test to gauge understanding.*

### The Big Picture

Imagine you're exploring a multi-level building. In one approach, you decide to explore all rooms on the current floor before moving to the next floor. This approach is akin to Breadth-First Search (BFS). In another approach, you start from the entrance and go as deep as possible into a room before backtracking. This approach is akin to Depth-First Search (DFS).

### Core Concepts

- **Tree**: A data structure consisting of nodes, where each node has zero or more child nodes. The topmost node is called the root.
- **Breadth-First Search (BFS)**: A traversal method that explores all nodes at the present depth level before moving on to nodes at the next depth level.
- **Depth-First Search (DFS)**: A traversal method that explores as far as possible along each branch before backtracking.

### Detailed Walkthrough

#### Breadth-First Search (BFS)

1. **Initialize a Queue**: Start by enqueuing the root node.
2. **Process Nodes Level by Level**:
   - Dequeue the front node.
   - Process the node (e.g., print its value).
   - Enqueue all its children.
3. **Repeat**: Continue this process until the queue is empty.

**Time Complexity**: O(V + E), where V is the number of vertices (nodes) and E is the number of edges.

#### Depth-First Search (DFS)

1. **Initialize a Stack (or Recursive Call)**: Start by pushing the root node onto the stack.
2. **Process Nodes by Going Deep**:
   - Pop the top node.
   - Process the node (e.g., print its value).
   - Push all its children onto the stack (or make recursive calls).
3. **Repeat**: Continue this process until the stack is empty (or the recursive calls are complete).

**Time Complexity**: O(V + E), where V is the number of vertices (nodes) and E is the number of edges.

### Understanding Through Examples

#### Example Tree

Consider the following tree:

```
      A
     / \
    B   C
   / \   \
  D   E   F
```

#### Breadth-First Search (BFS)

1. Initialize the queue: [A]
2. Dequeue A, enqueue B and C: Queue = [B, C]; Output = [A]
3. Dequeue B, enqueue D and E: Queue = [C, D, E]; Output = [A, B]
4. Dequeue C, enqueue F: Queue = [D, E, F]; Output = [A, B, C]
5. Dequeue D: Queue = [E, F]; Output = [A, B, C, D]
6. Dequeue E: Queue = [F]; Output = [A, B, C, D, E]
7. Dequeue F: Queue = []; Output = [A, B, C, D, E, F]

#### Depth-First Search (DFS)

**Pre-Order Traversal** (Node, Left, Right):

1. Visit A: Output = [A]
2. Visit B: Output = [A, B]
3. Visit D: Output = [A, B, D]
4. Visit E: Output = [A, B, D, E]
5. Visit C: Output = [A, B, D, E, C]
6. Visit F: Output = [A, B, D, E, C, F]

**In-Order Traversal** (Left, Node, Right):

1. Visit D: Output = [D]
2. Visit B: Output = [D, B]
3. Visit E: Output = [D, B, E]
4. Visit A: Output = [D, B, E, A]
5. Visit C: Output = [D, B, E, A, C]
6. Visit F: Output = [D, B, E, A, C, F]

**Post-Order Traversal** (Left, Right, Node):

1. Visit D: Output = [D]
2. Visit E: Output = [D, E]
3. Visit B: Output = [D, E, B]
4. Visit F: Output = [D, E, B, F]
5. Visit C: Output = [D, E, B, F, C]
6. Visit A: Output = [D, E, B, F, C, A]

### Conclusion and Summary

Breadth-First Search (BFS) explores nodes level by level using a queue, making it suitable for finding the shortest path in unweighted graphs. Depth-First Search (DFS) explores as deep as possible along each branch using a stack or recursion, which can be implemented in pre-order, in-order, or post-order traversal methods.

### Test Your Understanding

1. How does BFS ensure that it explores all nodes at the current level before moving to the next level?
2. What is the primary difference in the data structure used for BFS and DFS?
3. Can you implement BFS and DFS in Python for a given tree?

### Reference

For further reading on Tree Traversal Algorithms, you can refer to:

- [Introduction to Algorithms by Cormen, Leiserson, Rivest, and Stein](https://mitpress.mit.edu/books/introduction-algorithms)
- [GeeksforGeeks on Tree Traversal](https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/)
