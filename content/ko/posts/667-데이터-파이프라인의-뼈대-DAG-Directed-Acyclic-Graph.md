---
title: "⛓️ 데이터 파이프라인의 뼈대, DAG(Directed Acyclic Graph)"
date: 2025-06-07T23:27:39+09:00
slug: "667-데이터-파이프라인의-뼈대-DAG-Directed-Acyclic-Graph"
original_url: "https://memoryhub.tistory.com/667"
tistory_id: 667
draft: false
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

복잡한 데이터 처리나 분산 시스템 작업을 코딩하다 보면, 어느 작업이 먼저 실행되어야 하는지 순서가 꼬여버린 경험, 다들 한 번쯤 있으시죠? 태스크 A의 결과가 B와 C에 필요하고, 또 B와 C의 결과가 D에 필요한 상황처럼 의존성이 얽히기 시작하면 관리하기가 여간 까다로운 게 아닙니다. 이 문제를 우아하게 해결하는 모델이 바로 오늘의 주인공, DAG입니다.

⚡ **TL;DR**  
DAG는 **방향성**이 있고 **순환하지 않는** 그래프로, 작업의 선후 관계와 의존성을 명확하게 표현합니다.  
데이터 파이프라인, 작업 스케줄링 등 의존성 관리가 중요한 시스템의 핵심적인 개념 모델로 사용됩니다.

## 목차

1. 배경: 우리는 왜 DAG를 알아야 할까?
2. 핵심 개념: DAG를 구성하는 3가지 요소
3. 실습: 파이썬으로 위상 정렬 구현하기
4. 활용 사례: DAG는 어디에 쓰일까?
5. 마치며 & 참고자료

---

## 1. 배경: 우리는 왜 DAG를 알아야 할까?

여러 단계로 이루어진 작업을 처리할 때, 각 단계의 실행 순서와 의존성을 정의하는 것은 매우 중요합니다[4]. 예를 들어, 고객 데이터를 가져와서(A), 정제하고(B), 분석한 후(C), 리포트를 생성(D)하는 파이프라인이 있다면 `A → B → C → D` 순서가 반드시 지켜져야 합니다.

만약 이 의존 관계가 무시되거나, 작업 흐름이 꼬여 `D → A` 같은 순환 구조가 생긴다면 시스템은 무한 루프에 빠지거나 교착 상태에 이를 수 있습니다[6][8]. DAG는 이러한 문제를 방지하고 복잡한 작업 흐름을 명확하고 안정적으로 관리하기 위해 고안된 자료구조입니다[4][5].

✅ **핵심 용어 정리**

- **그래프(Graph):** 정점(Vertex, 또는 노드)과 이를 연결하는 간선(Edge)의 집합입니다[2][8].
- **유향(Directed):** 간선에 방향이 존재합니다. 즉, A에서 B로 가는 경로는 있지만 B에서 A로 직접 돌아오는 경로는 없습니다[8].
- **비순환(Acyclic):** 그래프 내에 순환하는 경로(Cycle)가 없습니다. 한 정점에서 출발해 여러 간선을 거쳐 다시 자기 자신에게 돌아올 수 없습니다[1][6][9].

## 2. 핵심 개념: DAG를 구성하는 3가지 요소

> **한 줄 정의**  
> **DAG(유향 비순환 그래프)는 정점(작업)과 간선(의존성)으로 구성되며, 시작점에서 출발해 같은 정점으로 되돌아오는 순환 경로가 없는 방향성 그래프입니다.**[2][6][11]

이름 그대로 '방향이 있으면서(Directed)', '순환은 없는(Acyclic)', '그래프(Graph)' 구조를 의미합니다[1][10]. 각 정점은 처리할 작업 단위를, 간선은 작업 간의 선후 관계 또는 데이터 흐름을 나타냅니다[4].

```
# 파이썬 딕셔너리로 간단한 DAG 표현하기
# 각 Key는 정점(작업), Value 리스트는 해당 정점이 가리키는 정점들(의존성)을 의미합니다.
# 'A' 작업이 끝나야 'B', 'C' 작업을 시작할 수 있습니다.
# 'B', 'C' 작업이 모두 끝나야 'D' 작업을 시작할 수 있습니다.
dag_representation = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

# 시각화하면 A -> B, A -> C, B -> D, C -> D 형태이며,
# 어느 경로로도 시작점으로 돌아올 수 없는 비순환 구조입니다.
```

## 3. 실습: 파이썬으로 위상 정렬 구현하기

DAG의 가장 중요한 특징 중 하나는 **위상 정렬(Topological Sort)**이 가능하다는 것입니다[1][2]. 위상 정렬이란 그래프의 모든 정점을 '의존성 순서에 맞게' 일렬로 나열하는 것을 말합니다[1]. 즉, `A → B`라는 간선이 있다면 정렬된 결과에서 A는 반드시 B보다 앞에 위치해야 합니다.

### ① 위상 정렬 알고리즘 (Kahn's Algorithm)

1. 모든 정점에 대해 자신을 가리키는 간선(진입 차수, In-degree)의 개수를 계산합니다.
2. 진입 차수가 0인 모든 정점을 큐(Queue)에 넣습니다. 이 정점들은 의존하는 선행 작업이 없는, 가장 먼저 시작할 수 있는 작업들입니다[1].
3. 큐가 빌 때까지 다음을 반복합니다.
   - 큐에서 정점 하나를 꺼내 결과 리스트에 추가합니다.
   - 해당 정점이 가리키던 모든 정점의 진입 차수를 1씩 감소시킵니다.
   - 만약 진입 차수가 0이 된 정점이 있다면, 큐에 추가합니다.
4. 모든 정점을 방문했다면, 결과 리스트가 바로 위상 정렬의 결과가 됩니다.

### ② 파이썬 코드 구현

```
from collections import deque

def topological_sort(graph):
    # 1. 각 노드의 진입 차수(in-degree) 계산
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # 2. 진입 차수가 0인 노드를 큐에 추가
    queue = deque([node for node in graph if in_degree[node] == 0])
    result = []

    # 3. 큐가 빌 때까지 반복
    while queue:
        node = queue.popleft()
        result.append(node)

        # 현재 노드와 연결된 노드들의 진입 차수 감소
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            # 진입 차수가 0이 되면 큐에 추가
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 모든 노드가 결과에 포함되었는지 확인 (사이클 존재 여부)
    if len(result) == len(graph):
        return result
    else:
        return "그래프에 사이클이 존재합니다."

# 2번 섹션에서 정의한 DAG
dag_representation = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}
```

### ③ 실행 결과 확인

```
# 위상 정렬 실행
sorted_tasks = topological_sort(dag_representation)
print(f"위상 정렬 결과: {sorted_tasks}")

# 출력 결과
# 위상 정렬 결과: ['A', 'B', 'C', 'D']
# (실행 환경에 따라 ['A', 'C', 'B', 'D']가 나올 수도 있으며, 둘 다 유효한 결과입니다.)
```

이 결과를 통해 `A`를 먼저 실행하고, 그 다음 `B`와 `C`를 (순서에 상관없이 또는 병렬로) 실행한 뒤, 마지막으로 `D`를 실행해야 한다는 작업 순서를 명확히 알 수 있습니다.

## 4. 활용 사례: DAG는 어디에 쓰일까?

DAG는 이론적인 모델을 넘어 다양한 컴퓨팅 분야에서 핵심적인 역할을 합니다[2][4].

| 활용 분야 | 장점 | 주의점 |
| --- | --- | --- |
| **데이터 처리 파이프라인**[4][5] | 복잡한 데이터 변환, ETL 작업의 의존성을 명확하게 관리하고, 실패한 지점부터 재시작(Idempotency)하기 용이합니다[5]. | 파이프라인이 지나치게 복잡해지면 시각화 및 디버깅이 어려워질 수 있습니다. |
| **작업 스케줄링**[2] | 컴파일러의 의존성 관리나 분산 컴퓨팅 환경(예: Apache Spark, Airflow)에서 태스크 간의 선후 관계를 정의하여 교착 상태 없이 효율적으로 작업을 수행합니다[8]. | 실시간으로 의존성이 변하는 동적인 환경에는 적용이 제한적일 수 있습니다. |
| **인과관계 추론**[3][7] | 통계학이나 역학에서 변수들 간의 인과관계를 시각적으로 모델링하는 데 사용됩니다[7]. 화살표는 인과적 영향을 나타냅니다. | 모델은 연구자의 가정에 기반하므로, 실제 인과관계와 다를 수 있습니다[7]. |
| **블록체인 기술** | 일부 암호화폐(예: IOTA)는 블록체인 대신 DAG 구조를 사용하여 거래를 기록함으로써 확장성과 속도 문제를 해결하려 시도합니다[9]. | 합의 메커니즘이 복잡하고, 보안성에 대한 지속적인 연구가 필요합니다. |

## 5. 마치며

오늘은 데이터 엔지니어링과 분산 시스템의 근간을 이루는 DAG에 대해 알아보았습니다.

- DAG는 **방향성, 비순환**이라는 두 가지 핵심 규칙으로 작업의 흐름과 의존성을 정의합니다.
- DAG의 본질을 이해하는 가장 좋은 방법은 **위상 정렬**을 통해 작업의 실행 순서를 명확히 하는 것입니다.
- Airflow, Spark, dbt와 같은 최신 데이터 도구들은 모두 내부적으로 **DAG 모델**을 사용하여 파이프라인을 안정적으로 운영합니다[8].

실제 프로젝트에서 복잡한 배치 작업을 설계할 때, 먼저 종속성을 DAG 형태로 그려보세요. 코드 구조를 잡고 잠재적인 문제를 예방하는 데 큰 도움이 될 것입니다.

이 글이 DAG를 이해하는 데 도움이 되셨다면 **❤️(하트)**와 **댓글** 부탁드립니다!

---

**참고자료**

- Directed acyclic graph - Wikipedia [2]
- Directed Acyclic Graph (DAG) Overview & Use Cases - Hazelcast [4]
- [알고리즘] Graph - Directed Acyclic Graphs(DAG) - velog [1]

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
