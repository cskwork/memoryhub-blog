---
title: "Dijkstra's Algorithm Introduced"
date: 2024-05-27T19:39:37+09:00
slug: "139-Dijkstra-s-Algorithm-Introduced"
original_url: "https://memoryhub.tistory.com/139"
tistory_id: 139
draft: false
categories: ["Dev Library"]
tags: ["DS And Algorithm"]
---

*Dijkstra's Algorithm is a method for finding the shortest path between nodes in a graph, akin to navigating the shortest route between cities on a map.*

### The Big Picture

Imagine you have a map with various cities connected by roads. You want to find the shortest path from your home city to a destination city. Dijkstra's Algorithm helps you determine this shortest path by systematically exploring routes from the starting point, considering the smallest distance to reach each city, and updating paths as shorter routes are found.

### Core Concepts

1. **Graph**: A collection of nodes (vertices) and edges (paths) connecting pairs of nodes.
2. **Weights**: Values assigned to each edge representing the cost or distance between nodes.
3. **Priority Queue**: A data structure used to manage the nodes to be explored based on their current shortest distance from the starting node.
4. **Relaxation**: The process of updating the shortest path estimate to a node when a shorter path is found.

### Detailed Walkthrough

1. **Initialization**:

   - Assign a tentative distance value to every node: set it to zero for the initial node and to infinity for all other nodes.
   - Set the initial node as current and mark all other nodes as unvisited.
2. **Visit Unvisited Nodes**:

   - For the current node, consider all its unvisited neighbors. Calculate their tentative distances through the current node.
   - If this tentative distance is less than the currently assigned value, update the shortest distance.
   - Once considered, mark the current node as visited. A visited node will not be checked again.
3. **Select the Next Node**:

   - From the unvisited nodes, select the node that is marked with the smallest tentative distance and set it as the new current node.
   - Repeat the process until the destination node is marked visited or all nodes have been visited.

### Understanding Through an Example

Let's say we have the following graph:

- Nodes: A, B, C, D, E
- Edges with weights:
  - A-B (4), A-C (2)
  - B-C (5), B-D (10)
  - C-E (3)
  - D-E (4)

We want to find the shortest path from A to E.

1. **Initialization**:

   - A: 0 (starting point)
   - B: ∞
   - C: ∞
   - D: ∞
   - E: ∞
2. **First Iteration** (starting at A):

   - From A, we update B and C:
     - B = min(∞, 0 + 4) = 4
     - C = min(∞, 0 + 2) = 2
   - Current distances: A (0), B (4), C (2), D (∞), E (∞)
   - Mark A as visited.
3. **Second Iteration** (current node C):

   - From C, update E:
     - E = min(∞, 2 + 3) = 5
   - Current distances: A (0), B (4), C (2), D (∞), E (5)
   - Mark C as visited.
4. **Third Iteration** (current node B):

   - From B, update D:
     - D = min(∞, 4 + 10) = 14 (not updated since next current node with smallest tentative distance is E)
   - Current distances: A (0), B (4), C (2), D (14), E (5)
   - Mark B as visited.
5. **Fourth Iteration** (current node E):

   - No updates since E is the destination.
   - Current distances: A (0), B (4), C (2), D (14), E (5)
   - Mark E as visited.

### Conclusion and Summary

Dijkstra's Algorithm effectively finds the shortest path in a weighted graph by:

1. Initializing distances and setting the starting node's distance to zero.
2. Exploring neighboring nodes and updating paths as shorter routes are found.
3. Using a priority queue to always expand the least costly node next.
4. Continuing this process until the shortest path to the destination is found.

### Test Your Understanding

1. Explain the purpose of the priority queue in Dijkstra's Algorithm.
2. What happens if the graph contains a negative weight edge?
3. Can Dijkstra's Algorithm be used on graphs with negative weights? Why or why not?

### Reference

For further reading, refer to:

- [Dijkstra's Algorithm on GeeksforGeeks](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- [Introduction to Algorithms by Thomas H. Cormen](https://mitpress.mit.edu/books/introduction-algorithms)
