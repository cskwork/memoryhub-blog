---
title: "? Claude Advanced Tool Use 에이전트 개발의 패러다임이 바뀐다"
date: 2025-11-25T20:31:02+09:00
slug: "914-Claude-Advanced-Tool-Use-에이전트-개발의-패러다임이-바뀐다"
original_url: "https://memoryhub.tistory.com/914"
tistory_id: 914
draft: false
categories: ["데브 라이브러리"]
tags: ["Claude"]
---

```
    ┌─────────────────────────────────────────────────────────┐
    │  CLAUDE ADVANCED TOOL USE                               │
    │  ════════════════════════                               │
    │                                                         │
    │   ┌──────┐    ┌──────┐    ┌──────┐                     │
    │   │ Tool │───▶│Search│───▶│ Load │  (On-Demand)        │
    │   │  1   │    │  ?  │    │ Tool │                     │
    │   └──────┘    └──────┘    └──────┘                     │
    │                                                         │
    │   ┌─────────────────────────────────────────┐          │
    │   │  CODE EXECUTION SANDBOX                 │          │
    │   │  ┌────┐ ┌────┐ ┌────┐ ┌────┐          │          │
    │   │  │API1│ │API2│ │API3│ │API4│ ─▶ Result│          │
    │   │  └────┘ └────┘ └────┘ └────┘          │          │
    │   └─────────────────────────────────────────┘          │
    │                                                         │
    │   85% Token Saved  │  37% Cost Reduced                 │
    └─────────────────────────────────────────────────────────┘
```

50개 도구를 연결했더니 대화 시작 전에 이미 7만 토큰이 사라졌다. 익숙한 상황인가요? MCP 서버를 여러 개 연결하면서 컨텍스트 윈도우가 터지기 직전까지 가본 경험, 개발자라면 한 번쯤 있을 겁니다. Anthropic이 이 문제를 정면으로 해결했습니다.

**도구를 '미리 외우는' 방식에서 '필요할 때 찾는' 방식으로 전환한 세 가지 신기능이 등장했습니다.**

**한줄요약:** Tool Search Tool, Programmatic Tool Calling, Tool Use Examples 세 가지 베타 기능으로 Claude가 수천 개 도구를 토큰 낭비 없이 정확하게 사용할 수 있게 되었다.

## 배경

AI 에이전트의 미래는 수백, 수천 개의 도구를 동시에 다루는 것입니다. IDE 어시스턴트가 git, 파일 관리, 패키지 매니저, 테스트 프레임워크, 배포 파이프라인을 통합하는 상황을 생각해보세요. 운영 코디네이터가 Slack, GitHub, Google Drive, Jira, 사내 데이터베이스, 수십 개의 MCP 서버를 동시에 연결하는 경우도 있습니다.

기존 방식의 문제는 명확했습니다. 5개 서버만 연결해도 도구 정의만으로 약 55,000 토큰이 소비됩니다. GitHub 35개 도구에 26K, Slack 11개 도구에 21K, 여기에 Jira까지 추가하면 100K 토큰을 훌쩍 넘깁니다. Anthropic 내부에서는 최적화 전 도구 정의에만 134K 토큰이 소비된 사례도 있었습니다.

토큰 비용만이 문제가 아닙니다. 가장 흔한 실패 원인은 잘못된 도구 선택과 부정확한 파라미터입니다. `notification-send-user`와 `notification-send-channel`처럼 이름이 비슷한 도구가 많아지면 혼란이 가중됩니다.

| 문제 유형 | 기존 방식의 한계 |
| --- | --- |
| 컨텍스트 오염 | 중간 결과물이 모두 컨텍스트에 쌓임 |
| 토큰 낭비 | 사용하지 않는 도구 정의도 미리 로드 |
| 정확도 저하 | 유사한 이름의 도구 간 혼동 |
| 지연 시간 | 도구 호출마다 추론 패스 필요 |

## 핵심

> Claude가 도구를 동적으로 발견하고, 코드로 실행하며, 예시로 학습하는 세 가지 신규 베타 기능이다.

### Tool Search Tool: 도서관 사서처럼 도구 찾기

모든 책을 책상에 쌓아두고 필요한 걸 찾는 것과 사서에게 물어보는 것, 어느 쪽이 효율적일까요? Tool Search Tool은 후자의 접근법입니다. 모든 도구 정의를 미리 로드하는 대신, Claude가 필요한 도구를 **온디맨드로 검색**합니다.

작동 방식은 간단합니다. 도구 정의에 `defer_loading: true`를 설정하면 해당 도구는 초기 컨텍스트에 로드되지 않습니다. Claude가 특정 기능이 필요할 때 Tool Search Tool로 검색하면, 매칭되는 도구만 컨텍스트에 추가됩니다.

내부 테스트 결과가 인상적입니다. **Opus 4의 정확도가 49%에서 74%로, Opus 4.5는 79.5%에서 88.1%로 향상**되었습니다. 토큰 사용량은 77K에서 8.7K로 약 85% 감소했습니다.

```
# 도구 정의 예시
{
  "tools": [
    {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
    {
      "name": "github.createPullRequest",
      "description": "Create a pull request",
      "input_schema": {...},
      "defer_loading": true  # 온디맨드 검색 대상으로 설정
    }
  ]
}
```

### Programmatic Tool Calling: 요리사가 직접 재료 손질하기

레스토랑에서 셰프가 매번 웨이터를 통해 재료를 하나씩 받아오는 상황을 상상해보세요. 비효율적입니다. Programmatic Tool Calling은 Claude가 **코드로 여러 도구를 직접 오케스트레이션**할 수 있게 합니다.

예를 들어 "Q3에 출장 예산을 초과한 팀원은 누구인가?"라는 질문을 처리한다고 가정합니다. 기존 방식이라면 20명의 팀원 정보를 가져오고, 각각의 비용 내역을 조회하고, 예산 한도를 확인하는 과정에서 2,000개 이상의 비용 항목이 컨텍스트에 쌓입니다.

Programmatic Tool Calling을 사용하면 Claude가 Python 스크립트를 작성해 전체 워크플로우를 처리합니다. 중간 결과는 코드 실행 환경에서 처리되고, **최종 결과만 Claude의 컨텍스트로 반환**됩니다. 200KB의 원시 데이터가 1KB의 결과로 압축되는 셈입니다.

성능 개선 수치도 명확합니다. 토큰 사용량이 평균 43,588에서 27,297로 37% 감소했고, 지식 검색 정확도는 25.6%에서 28.5%로, GIA 벤치마크는 46.5%에서 51.2%로 향상되었습니다.

### Tool Use Examples: 백문이 불여일견

JSON Schema는 구조적으로 유효한 것을 정의할 뿐, 사용 패턴을 표현하지 못합니다. `due_date` 필드가 "2024-11-06"인지 "Nov 6, 2024"인지, `reporter.id`가 UUID인지 "USR-12345" 형식인지 스키마만으로는 알 수 없습니다.

Tool Use Examples는 **구체적인 사용 예시를 도구 정의에 직접 포함**시킵니다. Claude는 이 예시들로부터 날짜 형식, ID 컨벤션, 선택적 파라미터의 조합 패턴을 학습합니다.

```
"input_examples": [
  {
    "title": "Login page returns 500 error",
    "priority": "critical",
    "labels": ["bug", "authentication", "production"],
    "due_date": "2024-11-06"  # 날짜 형식 학습
  },
  {
    "title": "Add dark mode support",
    "labels": ["feature-request", "ui"]  # 기능 요청은 간단하게
  }
]
```

내부 테스트에서 복잡한 파라미터 처리 정확도가 **72%에서 90%로 향상**되었습니다.

## 실습

① **베타 헤더 추가**

세 기능 모두 베타 상태이므로 API 호출 시 베타 헤더를 포함해야 합니다.

```
client.beta.messages.create(
    betas=["advanced-tool-use-2025-11-20"],
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    tools=[...]
)
```

② **Tool Search Tool 설정**

도구 정의가 10K 토큰을 넘거나 10개 이상의 도구를 사용한다면 Tool Search Tool 도입을 고려하세요. 자주 사용하는 3~5개 도구는 `defer_loading: false`로 유지하고, 나머지는 `defer_loading: true`로 설정합니다.

③ **Programmatic Tool Calling 적용**

병렬 실행이 가능하거나 중간 결과가 최종 응답에 불필요한 도구에 `allowed_callers`를 설정합니다. 대용량 데이터 집계, 다단계 워크플로우에 특히 효과적입니다.

④ **Tool Use Examples 작성**

복잡한 중첩 구조, 도메인별 컨벤션이 있는 도구에 1~5개의 현실적인 예시를 추가합니다. "string"이나 "value" 같은 플레이스홀더 대신 실제 데이터를 사용하세요.

## 모범사례/패턴 비교

| 기능 | 적합한 상황 | 부적합한 상황 |
| --- | --- | --- |
| Tool Search Tool | 도구 정의 10K+ 토큰, 10개 이상 도구, MCP 멀티 서버 | 소규모 도구 라이브러리, 모든 도구가 매 세션 사용 |
| Programmatic Tool Calling | 대용량 데이터 집계, 3개 이상 연속 도구 호출, 병렬 처리 | 단순 단일 도구 호출, 중간 결과를 봐야 하는 작업 |
| Tool Use Examples | 복잡한 중첩 구조, 도메인별 컨벤션, 유사 도구 구분 필요 | 단순 단일 파라미터, URL/이메일 등 표준 형식 |

## 마치며

- Claude의 도구 사용 방식이 "모든 것을 미리 로드"에서 "필요할 때 검색"으로 진화했습니다.
- Tool Search Tool로 토큰 85% 절감, Programmatic Tool Calling으로 37% 추가 절감이 가능합니다.
- 실전 팁: 현재 에이전트의 도구 정의 토큰 수를 측정하고, 10K를 넘는다면 Tool Search Tool 도입을 검토해보세요.

## 참고자료

- Introducing advanced tool use on the Claude Developer Platform (<https://www.anthropic.com/news/advanced-tool-use>)
- Claude API Documentation (<https://docs.anthropic.com>)
