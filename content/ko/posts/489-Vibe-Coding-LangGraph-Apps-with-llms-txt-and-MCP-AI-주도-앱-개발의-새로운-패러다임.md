---
title: "Vibe Coding LangGraph Apps with llms.txt and MCP - AI 주도 앱 개발의 새로운 패러다임 ?"
date: 2025-03-21T02:46:31+09:00
slug: "489-Vibe-Coding-LangGraph-Apps-with-llms-txt-and-MCP-AI-주도-앱-개발의-새로운-패러다임"
original_url: "https://memoryhub.tistory.com/489"
tistory_id: 489
draft: false
categories: ["데브 라이브러리"]
tags: ["Prompting"]
---

Vibe Coding은 개발자가 코드 구현보다 의도와 설계에 집중하는 새로운 프로그래밍 패러다임입니다. LangGraph, llms.txt, MCP를 결합하면 AI 기반 애플리케이션 개발이 직관적이고 효율적으로 변화합니다. 이 접근 방식은 개발 시간을 단축하고 복잡한 에이전트 시스템 구축을 단순화합니다.

여러분은 요리 레시피를 AI에게 설명하는 것을 상상해보세요. 세세한 측정값과 절차를 일일이 나열하는 대신, 어떤 맛과 질감을 원하는지 설명하면 AI가 알아서 자세한 레시피를 작성해주는 것처럼, Vibe Coding은 개발자가 원하는 기능과 목적을 높은 수준에서 설명하면 AI가 실제 코드 구현을 담당하는 방식입니다.

- 개발자는 "무엇을" 원하는지에 집중하고, AI는 "어떻게" 구현할지를 결정합니다
- 직관적인 자연어 지시로 복잡한 애플리케이션 구조를 설계할 수 있습니다
- 문법적 세부사항보다 전체적인 시스템 흐름을 느끼며 개발합니다

## 왜 필요한가?

Vibe Coding, LangGraph, llms.txt, MCP가 해결하는 문제들은 다음과 같습니다:

1. **개발 복잡성 감소**: 전통적인 프로그래밍은 세부적인 문법 지식과 수많은 코드 라인을 필요로 합니다. Vibe Coding은 AI에게 구현을 맡겨 개발자가 큰 그림에 집중할 수 있게 합니다.
2. **복잡한 LLM 워크플로우 관리**: 여러 에이전트가 상호작용하는 AI 시스템은 상태 관리와 에이전트 조율이 어렵습니다. LangGraph는 이러한 복잡성을 그래프 기반 접근 방식으로 단순화합니다.
3. **표준화 부재**: LLM이 외부 데이터 및 도구와 상호작용하는 방식에 일관된 표준이 없었습니다. MCP는 이를 표준화하여 개발 효율성을 높입니다.
4. **AI 접근성 제한**: 웹사이트와 문서가 AI 시스템이 이해하기 어려운 형식으로 구성되어 있습니다. llms.txt는 웹사이트가 LLM에게 효과적으로 정보를 제공할 수 있는 방법을 제시합니다.

## 기본 원리

Vibe Coding, LangGraph, llms.txt, MCP의 핵심 원리를 알아볼까요?

### Vibe Coding 원리

Vibe Coding은 코드 구현보다 개발 의도를 중심으로 하는 패러다임입니다. 개발자는 자연어로 원하는 기능을 설명하고, AI는 그 의도를 실제 코드로 변환합니다.

```
# 전통적인 코딩 방식
def parse_csv(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    filtered_data = data[data['score'] > 75]
    return filtered_data.groupby('category').mean()

# Vibe Coding 방식
"""
CSV 파일에서 점수가 75점 이상인 항목만 필터링하고
카테고리별 평균을 계산해줘.
"""
# AI가 위 지시에 따라 적절한 코드를 생성합니다
```

### LangGraph 원리

LangGraph는 LLM 애플리케이션의 워크플로우를 그래프로 정의합니다. 노드는 실행 단계를, 엣지는 제어 흐름을 나타냅니다.

```
from langgraph.graph import StateGraph
from typing import TypedDict, List

# 상태 정의
class AgentState(TypedDict):
    messages: List
    next_steps: List

# 그래프 생성
workflow = StateGraph(AgentState)

# 노드 추가
workflow.add_node("parse_request", parse_request_fn)
workflow.add_node("search_knowledge", search_knowledge_fn)
workflow.add_node("generate_response", generate_response_fn)

# 엣지 추가 (제어 흐름 정의)
workflow.add_edge("parse_request", "search_knowledge")
workflow.add_edge("search_knowledge", "generate_response")

# 그래프 컴파일
agent = workflow.compile()
```

### llms.txt 원리

llms.txt는 웹사이트가 LLM에게 효과적으로 정보를 제공하기 위한 마크다운 파일 형식입니다. 웹사이트의 핵심 정보를 구조화된 방식으로 제공합니다.

```
# 회사명 웹사이트 llms.txt

## 핵심 정보
- 회사명: ABC 테크놀로지
- 설립: 2020년
- 주요 제품: AI 솔루션, 클라우드 서비스

## 중요 페이지
- 제품 소개: https://example.com/products
- 가격 정책: https://example.com/pricing
- 개발자 문서: https://example.com/docs

## API 문서
API 엔드포인트는 다음과 같습니다:
- GET /api/users - 사용자 정보 조회
- POST /api/auth - 인증 토큰 발급
```

### MCP(Model Context Protocol) 원리

MCP는 LLM이 외부 데이터 소스 및 도구와 상호작용하는 방식을 표준화하는 프로토콜입니다. 다양한 도구와 데이터 소스를 일관된 방식으로 연결합니다.

```
from mcp.client import MCPClient
from mcp.tools import WebSearchTool, DatabaseTool

# MCP 클라이언트 설정
client = MCPClient()

# 도구 등록
client.register_tool(WebSearchTool())
client.register_tool(DatabaseTool(connection_string="..."))

# LLM에 MCP 컨텍스트 제공
response = client.run(
    model="claude-3",
    prompt="사용자 데이터베이스에서 최근 가입한 10명의 사용자를 검색하고 분석해줘",
    tools=["web_search", "database"]
)
```

## 실제 예제

대규모 언어 모델을 활용한 고객 지원 시스템을 개발하는 예제를 살펴보겠습니다.

### 기본 사용법

아래는 LangGraph를 사용하여 Vibe Coding 스타일로 고객 지원 에이전트를 구현하는 예시입니다:

```
from langgraph.graph import StateGraph
from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage, AIMessage
from typing import TypedDict, List, Dict

# 상태 정의
class AgentState(TypedDict):
    messages: List
    customer_info: Dict
    support_db: Dict

# LLM 모델 초기화
llm = ChatAnthropic(model="claude-3-sonnet-20240229")

# 이 부분을 자연어 설명으로 Vibe Coding
"""
다음 워크플로우를 가진 고객 지원 에이전트를 만들어줘:
1. 고객 요청을 분석하고 의도를 파악한다
2. 고객 정보 데이터베이스에서 관련 정보를 검색한다
3. 지원 지식 베이스에서 해결책을 찾는다
4. 고객에게 맞춤형 응답을 생성한다
5. 필요한 경우 인간 상담원에게 에스컬레이션한다
"""

# AI가 위 지시에 따라 LangGraph 구조를 생성
workflow = StateGraph(AgentState)
workflow.add_node("parse_intent", parse_intent_fn)
workflow.add_node("retrieve_customer_info", retrieve_customer_info_fn)
workflow.add_node("search_knowledge_base", search_knowledge_base_fn)
workflow.add_node("generate_response", generate_response_fn)
workflow.add_node("human_escalation", human_escalation_fn)

# 조건부 엣지 추가
workflow.add_conditional_edges(
    "parse_intent",
    lambda state: "retrieve_customer_info" if not state.get("escalate") else "human_escalation"
)
workflow.add_edge("retrieve_customer_info", "search_knowledge_base")
workflow.add_edge("search_knowledge_base", "generate_response")

# 그래프 컴파일 및 실행
agent = workflow.compile()
```

### 실전 활용

다음은 전통적인 개발 방식과 Vibe Coding + LangGraph/MCP 방식의 비교입니다:

| 상황 | 일반적인 방법 | Vibe Coding + LangGraph/MCP | 개선효과 |
| --- | --- | --- | --- |
| 에이전트 워크플로우 설계 | 상세한 제어 흐름 코딩 | 자연어로 워크플로우 설명 | 개발 시간 70% 단축 |
| 외부 API 통합 | 각 API마다 다른 통합 방식 | MCP로 표준화된 통합 | 유지보수성 50% 향상 |
| 문서화 | 별도의 문서 작성 필요 | llms.txt로 자동 AI 접근성 제공 | 문서화 시간 60% 절약 |
| 에이전트 로직 수정 | 코드 수정 및 재배포 | 자연어 지시로 로직 업데이트 | 반복 주기 80% 단축 |

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **과도한 의존성 주의**

   - AI 생성 코드를 무조건 신뢰하지 말고 검증하세요
   - 중요한 비즈니스 로직은 추가 검토가 필요합니다
2. **모호한 지시 피하기**

   - Vibe Coding은 명확한 의도 전달이 중요합니다
   - "좋은 코드를 작성해줘"보다 "사용자 입력 유효성을 검사하는 코드를 작성해줘"처럼 구체적으로 지시하세요
3. **테스트 자동화 필수**

   - AI 생성 코드는 예상치 못한 동작을 할 수 있습니다
   - 자동화된 테스트로 지속적인 검증이 필요합니다

? **꿀팁**

- LangGraph Studio를 활용해 워크플로우를 시각적으로 디버깅하세요
- llms.txt 파일은 핵심 정보만 간결하게 포함하는 것이 효과적입니다
- MCP 클라이언트를 모듈화하여 재사용성을 높이세요
- 복잡한 로직은 여러 작은 단계로 나누어 Vibe Coding하면 더 정확한 결과를 얻을 수 있습니다
- 생성된 코드에서 이해하기 어려운 부분이 있다면 AI에게 설명을 요청하세요

## 마치며

지금까지 Vibe Coding, LangGraph, llms.txt, MCP를 활용한 AI 주도 앱 개발 방법에 대해 알아보았습니다. 이 접근 방식은 개발자가 세부적인 구현보다 창의적인 문제 해결과 시스템 설계에 집중할 수 있게 해줍니다. 처음에는 직관적인 코딩 방식이 낯설게 느껴질 수 있지만, 익숙해지면 개발 효율성과 즐거움이 크게 향상됩니다.

개발의 패러다임이 점점 더 AI와의 협업 방향으로 진화하면서, 코딩의 미래는 정확한 구문 작성보다 명확한 의도 전달에 더 가까워지고 있습니다. Vibe Coding과 같은 접근 방식이 이러한 변화의 중심에 있습니다.

혹시 궁금한 점이 있으시거나, 더 알고 싶은 내용이 있으시면 댓글로 남겨주세요.

## 참고 자료 ?

- [LangGraph 공식 문서](https://www.langchain.com/langgraph)
- [Model Context Protocol 사양](https://github.com/modelcontextprotocol)
- [llms.txt 가이드라인](https://www.analyticsvidhya.com/blog/2025/03/llms-txt/)
- [LangGraph Studio 튜토리얼](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)
- [Vibe Coding 입문 가이드](https://zbrain.ai/what-is-vibe-coding/)

---

#VibeCoding #LangGraph #MCP #AIAssisted #LLMAgent
