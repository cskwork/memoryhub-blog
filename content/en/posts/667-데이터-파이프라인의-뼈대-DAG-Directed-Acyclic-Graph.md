---
title: "⛓️ The Backbone of Data Pipelines: DAG (Directed Acyclic Graph)"
date: 2025-06-07T23:27:39+09:00
slug: "667-데이터-파이프라인의-뼈대-DAG-Directed-Acyclic-Graph"
original_url: "https://memoryhub.tistory.com/667"
tistory_id: 667
draft: false
categories: ["Dev Framework"]
tags: ["Apache"]
---

```
          +--------+      +--------+
          | Task A |----->| Task B |
          +--------+      +--------+
              |              |
              |              |
              v              v
          +--------+      +--------+
          | Task C |----->| Task D |
          +--------+      +--------+
```

When coding complex data processing or distributed system tasks, have you ever experienced the order of operations getting tangled? When task A's result is needed by B and C, and then B and C's results are needed by D—as dependencies interweave—managing them becomes a headache. The elegant solution to this problem, and today's star, is DAG.

⚡ **TL;DR**  
DAG is a **directed** and **acyclic** graph that clearly expresses task sequences and dependencies.  
It serves as the core conceptual model for systems where dependency management is critical, such as data pipelines and task scheduling.

## Table of Contents

1. Background: Why do we need to understand DAG?
2. Core Concepts: 3 Elements that Make Up a DAG
3. Practice: Implementing Topological Sorting in Python
4. Use Cases: Where is DAG Used?
5. Conclusion & References

---

## 1. Background: Why do we need to understand DAG?

When processing multi-stage tasks, defining the execution order and dependencies of each stage is crucial[4]. For example, in a pipeline that fetches customer data (A), cleanses it (B), analyzes it (C), and generates a report (D), the order `A → B → C → D` must be strictly maintained.

If these dependency relationships are ignored or the task flow gets tangled with a circular structure like `D → A`, the system can enter infinite loops or deadlocks[6][8]. DAG is a data structure designed to prevent such problems and to manage complex task flows clearly and reliably[4][5].

✅ **Key Terminology**

- **Graph:** A collection of vertices (or nodes) and edges connecting them[2][8].
- **Directed:** Edges have direction. That is, there is a path from A to B, but no direct path back from B to A[8].
- **Acyclic:** The graph contains no cycles. A vertex cannot return to itself through multiple edges[1][6][9].

## 2. Core Concepts: 3 Elements that Make Up a DAG

> **One-line Definition**  
> **A DAG (directed acyclic graph) is composed of vertices (tasks) and edges (dependencies), and is a directed graph in which there is no cyclic path that starts from one point and returns to the same vertex.**[2][6][11]

As the name suggests, it means a graph structure that is 'directed' while 'acyclic'[1][10]. Each vertex represents a unit of work to be processed, and each edge represents the sequential relationship or data flow between tasks[4].

```
# Simple DAG representation using a Python dictionary
# Each key is a vertex (task), and the value list is the vertices that the vertex points to (dependencies)
# Task 'A' must complete before tasks 'B' and 'C' can start
# Tasks 'B' and 'C' must both complete before task 'D' can start
dag_representation = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# When visualized, it takes the form A -> B, A -> C, B -> D, C -> D,
# and it's an acyclic structure where no path returns to the starting point.
```

## 3. Practice: Implementing Topological Sorting in Python

One of the most important features of DAG is that **topological sorting** is possible[1][2]. Topological sorting means arranging all vertices of the graph in a single line 'according to dependency order'[1]. In other words, if there's an edge `A → B`, then A must come before B in the sorted result.

### ① Topological Sorting Algorithm (Kahn's Algorithm)

1. For all vertices, calculate the number of edges pointing to it (in-degree).
2. Add all vertices with in-degree 0 to a queue. These vertices have no dependent predecessor tasks and can start first[1].
3. Repeat the following until the queue is empty:
   - Remove one vertex from the queue and add it to the result list.
   - Decrease the in-degree of all vertices that the current vertex points to by 1.
   - If any vertex's in-degree becomes 0, add it to the queue.
4. Once all vertices are visited, the result list is the topological sorting result.

### ② Python Implementation

```
from collections import deque

def topological_sort(graph):
    # 1. Calculate in-degree for each node
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # 2. Add nodes with in-degree 0 to queue
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    # 3. Repeat until queue is empty
    while queue:
        node = queue.popleft()
        result.append(node)

        # Decrease in-degree of connected nodes
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # Add to queue if in-degree becomes 0
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Verify if all nodes are in result (check for cycles)
    if len(result) == len(graph):
        return result
    else:
        return "The graph contains a cycle."

# DAG defined in section 2
dag_representation = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
```

### ③ Checking Execution Results

```
# Run topological sorting
sorted_tasks = topological_sort(dag_representation)
print(f"Topological sorting result: {sorted_tasks}")

# Output result
# Topological sorting result: ['A', 'B', 'C', 'D']
# (Depending on the execution environment, ['A', 'C', 'B', 'D'] is also valid.)
```

Through this result, you can clearly see that you should execute `A` first, then execute `B` and `C` (in any order or in parallel), and finally execute `D`.

## 4. Use Cases: Where is DAG Used?

DAG goes beyond a theoretical model and plays a core role in various computing domains[2][4].

| Use Case | Advantages | Considerations |
| --- | --- | --- |
| **Data Processing Pipelines**[4][5] | Clearly manages dependencies of complex data transformations and ETL tasks, and makes it easy to restart from a failed point (Idempotency)[5]. | Overly complex pipelines can become difficult to visualize and debug. |
| **Task Scheduling**[2] | Defines dependencies between tasks in compiler dependency management and distributed computing environments (e.g., Apache Spark, Airflow), enabling efficient task execution without deadlocks[8]. | Applicability is limited in dynamic environments where dependencies change in real-time. |
| **Causal Inference**[3][7] | Used to visually model causal relationships between variables in statistics and epidemiology[7]. Arrows represent causal effects. | The model is based on researcher assumptions, so actual causal relationships may differ[7]. |
| **Blockchain Technology** | Some cryptocurrencies (e.g., IOTA) attempt to solve scalability and speed issues by using DAG structures instead of blockchains to record transactions[9]. | Consensus mechanisms are complex, and ongoing research on security is necessary. |

## 5. Conclusion

Today we explored DAG, which forms the foundation of data engineering and distributed systems.

- DAG defines task flow and dependencies through two key rules: **directionality and acyclicity**.
- The best way to understand DAG's essence is through **topological sorting** to clarify task execution order.
- Modern data tools like Airflow, Spark, and dbt all use **DAG models** internally to operate pipelines reliably[8].

When designing complex batch jobs in actual projects, first draw the dependencies as a DAG. It will greatly help in establishing code structure and preventing potential issues.

If this article helped you understand DAG, please show your appreciation with **❤️ (hearts)** and **comments**!

---

**References**

- Directed acyclic graph - Wikipedia [2]
- Directed Acyclic Graph (DAG) Overview & Use Cases - Hazelcast [4]
- [Algorithm] Graph - Directed Acyclic Graphs(DAG) - velog [1]

[1] <https://velog.io/@claude_ssim/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Graph-Directed-Acyclic-GraphsDAG>  
[2] <https://en.wikipedia.org/wiki/Directed_acyclic_graph>  
[3] <https://blog.naver.com/coolest_shin/221998284675>  
[4] <https://hazelcast.com/foundations/distributed-computing/directed-acyclic-graph/>  
[5] <https://www.ssp.sh/brain/dag/>  
[6] <https://yonghwankim-dev.tistory.com/222>  
[7] <https://health.ucdavis.edu/media-resources/ctsc/documents/pdfs/directed-acyclic-graphs20220209.pdf>  
[8] <https://orkes.io/content/faqs/directed-acyclic-graph>  
[9] <https://steemit.com/dag/@cryptodreamers/dag-dag-directed-acyclic-graph>  
[10] <https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%96%A5_%EB%B9%84%EC%88%9C%ED%99%98_%EA%B7%B8%EB%9E%98%ED%94%84>  
[11] <https://www.ibm.com/think/topics/directed-acyclic-graph>  
[12] <https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf>  
[13] <https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html>  
[14] <https://www.youtube.com/watch?v=LK_HZjQyQtY>  
[15] <https://www.youtube.com/watch?v=5hg8Ahp3d58>
