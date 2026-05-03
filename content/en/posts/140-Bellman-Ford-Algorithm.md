---
title: "Bellman-Ford Algorithm"
date: 2024-05-27T19:42:31+09:00
slug: "140-Bellman-Ford-Algorithm"
original_url: "https://memoryhub.tistory.com/140"
tistory_id: 140
draft: false
---

*The Bellman-Ford Algorithm is used to find the shortest paths from a single source vertex to all other vertices in a weighted graph, even if some of the weights are negative.*

### The Big Picture

Imagine you have a network of roads connecting various cities, with some roads having negative tolls (like discounts or cashbacks). The Bellman-Ford Algorithm helps you determine the shortest paths from your starting city to all other cities, taking into account these positive and negative tolls, and it can also detect if there's a cycle with a net negative toll that could potentially reduce the travel cost indefinitely.

### Core Concepts

1. **Graph**: A collection of nodes (vertices) and edges (paths) connecting pairs of nodes.
2. **Weights**: Values assigned to each edge representing the cost or distance between nodes, which can be positive or negative.
3. **Relaxation**: The process of updating the shortest path estimate to a node when a shorter path is found.
4. **Negative Weight Cycle**: A cycle in the graph where the sum of the edge weights is negative, leading to infinitely reducible path costs.

### Detailed Walkthrough

1. **Initialization**:

   - Set the distance to the source node to 0 and all other nodes to infinity.
   - Create an array to store the shortest path distances from the source to each node.
2. **Edge Relaxation**:

   - For each node, repeat the relaxation process for all edges `|V| - 1` times (where `|V|` is the number of vertices in the graph).
   - For each edge (u, v) with weight w, if the distance to u plus w is less than the distance to v, update the distance to v.
3. **Negative Weight Cycle Detection**:

   - After the relaxation steps, check all edges one more time. If a shorter path is still found, it indicates the presence of a negative weight cycle.

### Understanding Through an Example

Consider a graph with the following edges and weights:

- Nodes: A, B, C, D, E
- Edges with weights:
  - A-B (4), A-C (2)
  - B-C (3), B-D (2), B-E (3)
  - C-B (1), C-D (5)
  - D-E (1)
  - E-D (-3)

We want to find the shortest paths from A to all other nodes.

1. **Initialization**:

   - A: 0 (starting point)
   - B: ∞
   - C: ∞
   - D: ∞
   - E: ∞
2. **First Iteration**:

   - Relax edges:
     - A-B: B = min(∞, 0 + 4) = 4
     - A-C: C = min(∞, 0 + 2) = 2
     - B-C: C = min(2, 4 + 3) = 2 (no change)
     - B-D: D = min(∞, 4 + 2) = 6
     - B-E: E = min(∞, 4 + 3) = 7
     - C-B: B = min(4, 2 + 1) = 3
     - C-D: D = min(6, 2 + 5) = 6 (no change)
     - D-E: E = min(7, 6 + 1) = 7 (no change)
     - E-D: D = min(6, 7 - 3) = 4
3. **Subsequent Iterations**:

   - Repeat the relaxation process for `|V| - 1` times, updating distances if shorter paths are found. After 3 iterations, the distances should stabilize.
4. **Negative Weight Cycle Check**:

   - Check all edges one more time. If any distance can still be reduced, it indicates a negative weight cycle.

### Conclusion and Summary

The Bellman-Ford Algorithm works by:

1. Initializing distances from the source node.
2. Repeatedly relaxing all edges to find the shortest path estimates.
3. Checking for negative weight cycles that could lead to infinite reduction of path costs.

### Test Your Understanding

1. Why do we need to perform the relaxation process |V| - 1 times?
2. How does the algorithm detect negative weight cycles?
3. Can Dijkstra's Algorithm handle graphs with negative weights? Why or why not?

### Reference

For further reading, refer to:

- [Bellman-Ford Algorithm on GeeksforGeeks](https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/)
- [Introduction to Algorithms by Thomas H. Cormen](https://mitpress.mit.edu/books/introduction-algorithms)
