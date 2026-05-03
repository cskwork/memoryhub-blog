---
title: "? Claude Agent SDK, 코딩용 AI가 범용 에이전트로 진화한 이유"
date: 2025-09-30T20:49:02+09:00
slug: "808-Claude-Agent-SDK-코딩용-AI가-범용-에이전트로-진화한-이유"
original_url: "https://memoryhub.tistory.com/808"
tistory_id: 808
draft: false
categories: ["데브 컨셉"]
tags: ["Tech News"]
---

```
    _______________
   /               \
  /   CLAUDE SDK    \
 /    ___________    \
|    |  ?  ?  |    |
|    |___________|    |
|                     |
|  [컴퓨터 접근권한]   |
|  ↓  ↓  ↓  ↓  ↓     |
|  파일 터미널 API    |
 \___________________/
        Agent
```

AI 코딩 도구를 쓰다가 "이거 다른 업무에도 쓰면 좋겠는데"라고 생각해 본 적 있으신가요? Anthropic이 2025년 9월 29일 공개한 Claude Agent SDK는 바로 그 고민의 답입니다. Claude Code의 기반 기술이었던 SDK를 범용 에이전트 개발 플랫폼으로 확장하면서, 코딩뿐 아니라 리서치·고객 지원·재무 분석까지 자동화할 수 있는 에이전트 구축이 가능해졌습니다. 이 글을 읽으면 **왜 이 SDK가 주목받는지, 어떻게 시작할 수 있는지** 명확히 알 수 있습니다.

---

## 1. 배경: Claude Code에서 Claude Agent SDK로

### 기존 문제점

기존 AI 에이전트는 특정 작업에만 최적화되거나, 복잡한 멀티 스텝 작업에서 문맥을 잃어버리는 한계가 있었습니다. Anthropic은 처음에 내부 개발자 생산성을 위해 Claude Code를 만들었지만, 곧 딥 리서치·영상 제작·노트 정리 등 비코딩 업무에서도 효과적임을 발견했습니다.

### 핵심 설계 원칙

Claude에게 프로그래머가 매일 사용하는 도구(파일 검색, 편집, 코드 실행, 디버깅)를 제공하면 실제 프로그래머처럼 작동한다는 것이 핵심 설계 원칙입니다. 터미널을 통해 컴퓨터 접근 권한을 주자, CSV 파일 읽기·웹 검색·시각화 생성·지표 해석 등 범용 디지털 작업이 가능해졌습니다.

### 주요 용어 정리

| 용어 | 의미 |
| --- | --- |
| **에이전트 루프** | 맥락 수집 → 작업 실행 → 검증 → 반복의 피드백 사이클 |
| **Subagent** | 병렬 처리와 컨텍스트 격리를 위한 독립적인 하위 에이전트 |
| **MCP (Model Context Protocol)** | Slack·GitHub·Drive 등 외부 서비스와 표준화된 통합 |
| **Agentic Search** | RAG 없이 grep·find 등 명령어로 필요한 정보를 동적 검색 |

---

## 2. 핵심: AI가 컴퓨터를 사용하는 방식

> **Claude Agent SDK는 '에이전트에게 컴퓨터를 준다'는 단순하지만 강력한 철학으로, 맥락 수집·실행·검증의 자율 피드백 루프를 완성합니다.**

SDK를 활용하면 재무 에이전트(포트폴리오 분석·투자 평가), 개인 비서(여행 예약·일정 관리), 고객 지원 에이전트(티켓 처리·데이터 수집), 딥 리서치 에이전트(대규모 문서 분석·보고서 생성) 등을 구축할 수 있습니다.

### 에이전트 루프 3단계

**① 맥락 수집 (Gather Context)**

- 파일 시스템을 컨텍스트로 활용 (폴더/파일 구조 = 컨텍스트 엔지니어링)
- Subagent로 병렬 검색 후 핵심 정보만 오케스트레이터에 전달
- Compaction 기능으로 컨텍스트 한계 도달 시 자동 요약

**② 작업 실행 (Take Action)**

- 커스텀 도구 정의 (fetchInbox, searchEmails 등)
- Bash 스크립트로 PDF 변환·텍스트 검색 등 유연한 작업
- MCP를 통해 Slack·Asana 등 외부 서비스 자동 연동 (OAuth 관리 불필요)

**③ 검증 (Verify Work)**

- 규칙 기반 피드백 (TypeScript 린팅 > JavaScript)
- 시각적 피드백 (스크린샷으로 UI 레이아웃·스타일 검증)
- LLM as Judge (별도 서브에이전트로 톤/품질 평가)

---

## 3. 실습: 이메일 에이전트 구축 예시

Claude Agent SDK는 Python으로 제공되며, 간단한 쿼리부터 양방향 대화까지 지원합니다. 아래는 공식 문서 기반 최소 예제입니다.

### ① 설치

```
pip install claude-agent-sdk
```

### ② 기본 쿼리 예제

```
import anyio
from claude_agent_sdk import query

async def main():
    async for message in query(prompt="2 + 2는?"):
        print(message)

anyio.run(main)
```

**출력 예시**: Claude가 계산 결과를 반환합니다.

### ③ 이메일 에이전트 시나리오

**구조 설계**:

- `Conversations/` 폴더에 이전 대화 저장 → grep으로 검색
- 검색 Subagent로 병렬 쿼리 실행
- Asana MCP로 "이미 담당자 배정됐는지" 확인
- 이메일 주소 유효성 검증 규칙 추가

```
from claude_agent_sdk import ClaudeAgentOptions

options = ClaudeAgentOptions(
    allowed_tools=["Read", "Bash", "mcp__asana__get_tasks"],
    permission_mode='prompt'  # 파일 수정 시 승인 요청
)
```

**주의**: 실제 구현은 MCP 서버 설정·도구 정의 등 추가 코드가 필요하므로, [공식 문서](https://docs.claude.com/en/api/agent-sdk/overview)를 참고하세요.

---

## 4. 모범 사례

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **Agentic Search 우선** | 동적 검색으로 재인덱싱 불필요 | 의미론적 검색보다 느릴 수 있음 |
| **Subagent 병렬화** | 속도 향상 + 컨텍스트 절약 | 오케스트레이션 복잡도 증가 |
| **TypeScript > JavaScript** | 린팅으로 다층 피드백 | 초기 설정 비용 |
| **MCP 우선 통합** | OAuth 자동 처리 | 생태계 의존성 |
| **작은 테스트 세트** | 실패 케이스 기반 개선 | 초기 준비 시간 필요 |

에이전트 개선의 핵심은 실패 사례를 면밀히 분석하고 "올바른 도구를 갖췄는지" 자문하는 것입니다.

---

## 5. 마치며

**배운 점 3줄**:

1. Claude Sonnet 4.5와 함께 공개된 Claude Agent SDK는 코딩용 인프라를 범용 에이전트로 확장한 사례입니다.
2. 맥락 수집·실행·검증의 루프 설계가 에이전트 신뢰성의 핵심입니다.
3. RAG 파이프라인 없이도 파일 시스템 + Bash로 강력한 에이전트 구축이 가능합니다.

**실전 적용 팁**: 간단한 작업(메일 분류·문서 검색)부터 시작해 점진적으로 도구를 추가하며, 실패 케이스 로그를 기반으로 규칙과 도구를 개선하세요.

---

## 참고자료

- **공식 문서**: [Claude Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)
- **엔지니어링 블로그**: [Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) (2025.09.29)
- **공식 발표**: [Claude Sonnet 4.5 & Agent SDK 소개](https://www.anthropic.com/news/claude-sonnet-4-5) (2025.09.29)
- **GitHub 저장소**: [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python)
- **MCP 생태계**: [Model Context Protocol Servers](https://github.com/modelcontextprotocol/servers)
