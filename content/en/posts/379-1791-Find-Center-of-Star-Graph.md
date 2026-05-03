---
title: "1791. Find Center of Star Graph"
date: 2024-11-15T23:10:48+09:00
slug: "379-1791-Find-Center-of-Star-Graph"
original_url: "https://memoryhub.tistory.com/379"
tistory_id: 379
draft: false
---

Hello! Let's solve the problem of finding the center node in a star graph.

1. Clarifying Requirements

```
- Find the center node in a star graph with n nodes
- A star graph consists of one center node and n-1 edges
- The center node is connected to all other nodes
- Input: edge array edges (each element is connection info in [ui, vi] format)
- Output: center node number
```

2. Core Solution Design

```
- The center node appears in every edge, so the most frequently appearing node is the center
- Actually, checking just two edges is sufficient to find the center node
```

3. Implementation Details

```
public class Solution {
    public int findCenter(int[][] edges) {
        // Checking only the first two edges is sufficient
        int[] edge1 = edges[0];
        int[] edge2 = edges[1];

        // The node appearing in both edges is the center node
        if (edge1[0] == edge2[0] || edge1[0] == edge2[1]) {
            return edge1[0];
        }
        return edge1[1];
    }
}
```

4. Key Design Decisions

```
- Optimized approach: check only two edges without examining all edges
- Time Complexity: O(1)
- Space Complexity: O(1)
```

5. Verification Results

```
Test Case 1:
Input: [[1,2],[2,3],[4,2]]
Result: 2 (correct)

Test Case 2:
Input: [[1,2],[5,1],[1,3],[1,4]]
Result: 1 (correct)
```

The key points of this solution are:

- Due to the nature of star graphs, the center node must be included in every edge
- Therefore, checking only the first two edges reveals the center node
- This is an efficient solution without unnecessary iterations or storage

---

## Easy Explanation

Let's first understand what a star graph is.

```
Example:
     3
     |
 4 - 2 - 1
     |
     5

Here, 2 is the center node. All other nodes are connected to 2.
```

Thinking about the problem simply:

1. The center node appears in every line (edge)
2. Other nodes appear only once

So we can solve it with a very simple method:

```
public class Solution {
    public int findCenter(int[][] edges) {
        // Two nodes in the first edge
        int a = edges[0][0];
        int b = edges[0][1];

        // First node in the second edge
        int c = edges[1][0];

        // If a appears in the second edge too, a is the center
        if (a == c) return a;
        // If b appears in the second edge too, b is the center
        if (b == c) return b;

        // Otherwise, the other node in the second edge is the center
        return edges[1][1];
    }
}
```

Let me show you an example:

```
Input: [[1,2],[2,3],[4,2]]
- First edge: 1-2
- Second edge: 2-3
- 2 appears in both edges!
- Therefore, 2 is the center
```

That's it! You can find the center node immediately by looking at just the first two edges.
