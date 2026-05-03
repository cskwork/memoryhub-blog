---
title: "? Anthropic SDK vs Agent SDK, 당신의 선택이 프로젝트 성패를 가른다"
date: 2025-12-28T11:56:44+09:00
slug: "949-Anthropic-SDK-vs-Agent-SDK-당신의-선택이-프로젝트-성패를-가른다"
original_url: "https://memoryhub.tistory.com/949"
tistory_id: 949
draft: false
categories: ["데브 라이브러리"]
tags: ["Claude"]
---

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     @anthropic-ai/sdk        @anthropic-ai/claude-agent   ║
    ║    ┌─────────────────┐       ┌─────────────────────────┐  ║
    ║    │  Low-Level API  │       │   High-Level Framework  │  ║
    ║    │ ═══════════════ │       │ ═══════════════════════ │  ║
    ║    │ • Thinking ✓    │       │ • Auto Tool Loop ✓      │  ║
    ║    │ • Full Stream ✓ │       │ • State Mgmt ✓          │  ║
    ║    │ • Manual Loop   │       │ • Retry Logic ✓         │  ║
    ║    └────────┬────────┘       └────────────┬────────────┘  ║
    ║             │                             │               ║
    ║             └──────────┬──────────────────┘               ║
    ║                        ▼                                  ║
    ║              [ Your AI Agent Project ]                    ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
```

Claude로 AI 에이전트를 만들려고 npm을 열었다가 멈칫한 적 있는가. @anthropic-ai/sdk와 @anthropic-ai/claude-agent-sdk, 두 패키지가 눈에 들어온다. "Agent가 붙었으니 더 좋은 거겠지?"라고 생각했다면, 그 판단이 며칠 밤을 새우게 만들 수 있다.

**두 SDK는 상위/하위 관계가 아니라 서로 다른 목적을 위해 설계된 도구다.** 이 글을 읽고 나면 프로젝트 요구사항에 맞는 SDK를 5분 안에 결정할 수 있다.

**한줄요약:** 결론부터 말하면, Extended Thinking 표시나 세밀한 스트리밍 제어가 필요하면 Direct SDK를, 도구 기반 에이전트를 빠르게 구축하려면 Agent SDK를 선택하고, 복잡한 프로젝트에서는 둘을 조합하라.

---

## 배경

Claude를 활용한 AI 에이전트 개발이 폭발적으로 증가하고 있다. Anthropic은 2025년 Claude Code SDK를 Claude Agent SDK로 리브랜딩하며 에이전트 개발 생태계를 본격적으로 확장했다. 문제는 기존 Messages API를 직접 다루는 Direct SDK와 새로운 Agent SDK 사이에서 개발자들이 혼란을 겪고 있다는 점이다.

> **핵심 개념 정리:** Direct SDK는 Claude API와 1:1로 통신하는 저수준 클라이언트이고, Agent SDK는 그 위에 도구 실행 루프, 상태 관리, 재시도 로직을 추가한 고수준 프레임워크다.

두 SDK의 관계를 비유하자면 이렇다. Direct SDK가 수동 변속기 자동차라면 Agent SDK는 자동 변속기 자동차다. 수동 변속기는 모든 기어 변환을 운전자가 제어하므로 세밀한 조작이 가능하지만 익숙해지는 데 시간이 걸린다. 자동 변속기는 변속을 알아서 처리해주므로 운전에 집중할 수 있지만, 특정 상황에서 원하는 대로 제어하기 어렵다.

---

## 아키텍처 차이 이해하기

Direct SDK와 Agent SDK의 가장 근본적인 차이는 코드와 Claude 사이에 무엇이 있느냐다.

**Direct SDK 흐름:**

```
애플리케이션 코드 ←→ Anthropic Messages API ←→ Claude 모델
       ↑
       └── 개발자가 모든 것을 직접 처리: 도구 루프, 상태, 스트리밍
```

**Agent SDK 흐름:**

```
애플리케이션 코드 ←→ Agent SDK ←→ Anthropic Messages API ←→ Claude 모델
                        ↑
                        └── SDK가 처리: 도구 라우팅, 대화 루프, 재시도
```

Agent SDK는 Claude Code를 구동하는 동일한 인프라를 기반으로 한다. Anthropic 공식 문서에 따르면, Agent SDK는 파일 읽기/쓰기, 명령 실행, 웹 검색, 코드 편집 등을 자율적으로 수행할 수 있는 에이전트 구축을 지원한다.

---

## 기능별 비교 분석

핵심 기능을 기준으로 두 SDK를 비교하면 선택 기준이 명확해진다.

| 기능 | Direct SDK | Agent SDK |
| --- | --- | --- |
| Extended Thinking 스트리밍 | 완전 접근 가능 | 접근 불가 |
| Extended Thinking 최종 결과 | 완전 접근 가능 | 접근 불가 |
| 도구 호출 처리 | 수동 루프 구현 필요 | 자동 처리 |
| 멀티턴 도구 대화 | 수동 상태 관리 | 자동 관리 |
| 스트리밍 텍스트 응답 | 완전 제어 가능 | 추상화됨 |
| 토큰 카운팅 | 직접 접근 | 추상화됨 |
| 에러 처리 및 재시도 | 수동 구현 | 내장 기능 |
| MCP 서버 연동 | 수동 구현 | 내장 지원 |

**가장 중요한 차이점:** Agent SDK는 Claude의 내부 추론 과정인 Extended Thinking 블록에 접근할 수 없다. 이는 버그가 아니라 의도된 설계다. Agent SDK는 에이전트 워크플로우의 단순성을 우선시하며, 모델의 내부 추론 노출보다 실행 효율성에 집중한다.

---

## Direct SDK를 선택해야 하는 상황

### 1. 사용자에게 추론 과정을 보여줘야 할 때

Claude.ai에서 "View thinking" 기능처럼 Claude의 사고 과정을 실시간으로 보여주고 싶다면 Direct SDK가 유일한 선택이다.

```
// Direct SDK - thinking_delta 이벤트를 직접 수신
const stream = client.messages.stream({
  model: "claude-sonnet-4-5-20250929",
  max_tokens: 16000,
  thinking: {
    type: "enabled",
    budget_tokens: 10000
  },
  messages: [{ role: "user", content: "복잡한 문제를 분석해줘..." }]
});

for await (const event of stream) {
  if (event.type === "content_block_delta") {
    if (event.delta.type === "thinking_delta") {
      // 추론 과정을 UI에 실시간 표시
      emitToClient("thinking", event.delta.thinking);
    } else if (event.delta.type === "text_delta") {
      emitToClient("response", event.delta.text);
    }
  }
}
```

Anthropic 공식 문서에 따르면 Extended Thinking을 활성화하면 thinking\_delta 이벤트를 통해 추론 콘텐츠를 실시간으로 수신할 수 있다. Claude Opus 4.5에서는 이전 어시스턴트 턴의 thinking 블록이 기본적으로 모델 컨텍스트에 보존된다.

### 2. 세밀한 스트리밍 제어가 필요할 때

스트리밍 청크를 커스텀 버퍼링하거나 변환해야 하는 경우 Direct SDK의 세분화된 이벤트 접근이 필수다.

### 3. 도구 없는 단순 대화형 앱

질문-답변, 텍스트 생성, 분석 등 도구 사용 없는 단순 상호작용에서는 Agent SDK의 오버헤드가 불필요하다.

### 4. 토큰 비용을 정밀하게 관리해야 할 때

API 호출마다 input\_tokens, output\_tokens, 캐시 관련 토큰을 직접 확인하고 비용을 최적화해야 한다면 Direct SDK가 더 투명한 접근을 제공한다.

---

## Agent SDK를 선택해야 하는 상황

### 1. 표준 에이전트 워크플로우 구축

파일 읽기/쓰기, 웹 검색, 코드 실행 등 도구를 사용해 작업을 완료할 때까지 루프를 돌려야 하는 전형적인 에이전트라면 Agent SDK가 적합하다.

```
// Agent SDK - 전체 루프를 자동 처리
const agent = new Agent({
  model: "claude-sonnet-4-5-20250929",
  tools: [readFileTool, writeFileTool, searchTool],
});

const result = await agent.run({
  messages: [{ role: "user", content: "src/main.ts의 버그를 찾아서 수정해줘" }]
});

// Agent SDK가 자동으로 수행하는 작업:
// 1. Claude 호출
// 2. tool_use 블록 감지
// 3. 도구 실행
// 4. 결과를 Claude에 반환
// 5. 최종 답변까지 반복
```

### 2. 빠른 프로토타이핑

인프라보다 비즈니스 로직에 집중하고 싶다면 Agent SDK가 보일러플레이트를 대폭 줄여준다. Anthropic 엔지니어링 블로그에 따르면, Agent SDK는 금융 에이전트, 개인 비서 에이전트, 고객 지원 에이전트 등 다양한 유형의 에이전트를 빠르게 구축할 수 있도록 설계되었다.

### 3. 장시간 실행되는 에이전트 세션

여러 턴에 걸쳐 다수의 도구 호출이 이루어지는 확장된 대화에서는 Agent SDK의 대화 상태 관리가 복잡성을 크게 줄여준다.

### 4. 프로덕션 안정성 우선

내장된 에러 처리, 재시도 로직, API 오류 및 속도 제한 대응이 필요하다면 Agent SDK가 이미 베스트 프랙티스를 캡슐화하고 있다.

---

## 실습: 하이브리드 접근 방식 구현

복잡한 애플리케이션에서는 두 SDK를 함께 사용하는 것이 최적의 선택일 수 있다. 사용자에게 추론 과정을 보여주면서 도구 기반 작업도 수행해야 하는 경우를 생각해보자.

### ① 프로젝트 구조 설계

```
src/
├── agents/
│   ├── thinking-agent.ts   // Direct SDK 사용
│   └── tool-agent.ts       // Agent SDK 사용
├── router.ts               // 요청 유형별 라우팅
└── index.ts
```

### ② 라우터 구현

```
// router.ts
async function handleRequest(request: Request) {
  // 추론 과정 표시가 필요한 분석 작업
  if (request.needsThinkingDisplay) {
    return analyzeWithThinking(request.query);
  }

  // 도구 사용이 필요한 에이전트 작업
  if (request.needsTools) {
    return executeAgentTask(request.query);
  }

  // 단순 질문
  return simpleQuery(request.query);
}
```

### ③ 각 에이전트 구현

추론 표시용 에이전트는 Direct SDK로, 도구 실행용 에이전트는 Agent SDK로 구현한다. 이렇게 하면 각 SDK의 강점을 모두 활용할 수 있다.

---

## 의사결정 플로우차트

복잡한 비교표보다 단순한 질문 흐름이 선택을 빠르게 만든다.

```
시작
  │
  ▼
Claude의 추론 과정을 사용자에게 보여줘야 하는가?
  │
  ├── 예 → Direct SDK 선택
  │
  └── 아니오
       │
       ▼
     Claude가 도구를 사용해야 하는가?
       │
       ├── 아니오 → Direct SDK 선택 (단순 대화에 더 적합)
       │
       └── 예
            │
            ▼
          커스텀 도구 오케스트레이션이 필요한가?
          (병렬 실행, 조건 분기 등)
            │
            ├── 예 → Direct SDK 선택
            │
            └── 아니오
                 │
                 ▼
               빠른 개발이 세밀한 제어보다 중요한가?
                 │
                 ├── 예 → Agent SDK 선택
                 │
                 └── 아니오 → Direct SDK 선택
```

---

## 모범사례 비교

| 시나리오 | 권장 SDK | 핵심 이유 |
| --- | --- | --- |
| 사용자에게 추론 과정 표시 | Direct SDK | Agent SDK는 thinking 블록 접근 불가 |
| 도구 없는 단순 챗봇 | Direct SDK | 불필요한 오버헤드 없음 |
| 도구 기반 에이전트, 빠른 개발 | Agent SDK | 자동화된 루프로 개발 속도 향상 |
| 도구 기반 에이전트, 완전 제어 | Direct SDK | 커스텀 오케스트레이션 가능 |
| 프로덕션 에이전트, 안정성 우선 | Agent SDK | 내장 에러 처리 및 재시도 |
| 토큰 비용 최적화 | Direct SDK | 직접적인 사용량 접근 |
| 추론 + 도구 모두 필요 | 하이브리드 | 작업 유형별 라우팅 |

---

## 마치며

- **두 SDK는 대체재가 아니다.** Direct SDK는 저수준 제어와 Extended Thinking 접근을, Agent SDK는 자동화된 에이전트 워크플로우를 제공한다.
- **선택 기준은 단순하다.** 추론 과정 표시나 세밀한 스트리밍 제어가 필요하면 Direct SDK, 도구 루프 자동화가 필요하면 Agent SDK다.
- **복잡한 프로젝트에서는 둘을 조합하라.** 하이브리드 접근 방식으로 각 SDK의 강점을 모두 활용할 수 있다.

**실전 팁:** 지금 바로 프로젝트의 핵심 요구사항을 세 가지로 정리하고, 의사결정 플로우차트를 따라가 보라. 5분 안에 답이 나온다.

---

## 참고자료

- Agent SDK overview - Claude Docs (<https://platform.claude.com/docs/en/agent-sdk/overview>)
- Building agents with the Claude Agent SDK - Anthropic Engineering (<https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk>)
- Building with extended thinking - Claude Docs (<https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking>)
- Claude Agent SDK TypeScript - GitHub (<https://github.com/anthropics/claude-agent-sdk-typescript>)
- Claude Sonnet 4.5 발표 - Anthropic (<https://www.anthropic.com/news/claude-sonnet-4-5>)
