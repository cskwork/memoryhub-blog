---
title: "? Claude Code 구조 분석, 왜 다들 cc를 “현장 엔지니어”라고 부를까?"
date: 2026-04-07T06:43:17+09:00
slug: "1048-Claude-Code-구조-분석-왜-다들-cc를-현장-엔지니어-라고-부를까"
original_url: "https://memoryhub.tistory.com/1048"
tistory_id: 1048
draft: false
cover:
  image: "images/1048-Claude-Code-%EA%B5%AC%EC%A1%B0-%EB%B6%84%EC%84%9D-%EC%99%9C-%EB%8B%A4%EB%93%A4-cc%EB%A5%BC-%ED%98%84%EC%9E%A5-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4-%EB%9D%BC%EA%B3%A0-%EB%B6%80%EB%A5%BC%EA%B9%8C/OIP-a4f2bc3b.png"
  alt: "Enabling Claude Code to work more autonomously \\ Anthropic"
  relative: false
  hidden: false
---

[![Enabling Claude Code to work more autonomously \ Anthropic](/images/1048-Claude-Code-%EA%B5%AC%EC%A1%B0-%EB%B6%84%EC%84%9D-%EC%99%9C-%EB%8B%A4%EB%93%A4-cc%EB%A5%BC-%ED%98%84%EC%9E%A5-%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4-%EB%9D%BC%EA%B3%A0-%EB%B6%80%EB%A5%BC%EA%B9%8C/OIP-a4f2bc3b.png)](https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously?utm_source=chatgpt.com)

## 인트로

- AI 코딩 도구를 쓰다 보면 답변은 그럴듯한데, 실제 파일 수정이나 테스트 실행은 결국 사람이 따로 해야 하는 경우가 많습니다. Claude Code를 바로 그 지점에서 다른 도구와 구분합니다. 단순 답변형이 아니라, 파일 읽기·편집·셸 실행·웹 검색까지 연결하는 실행형 CLI로 설명하거든요.
- 특히 핵심은 “좋은 답변” 자체보다, **질문을 받고 → 도구를 고르고 → 권한을 확인하고 → 실행하고 → 다시 판단하는 루프**에 있습니다. 사용자는 한 번 요청하지만, 내부에서는 여러 번의 API 호출과 도구 실행이 반복됩니다.
- 이 글을 읽고 나면 “왜 이 도구가 실무형으로 보이는지”가 구조적으로 정리됩니다.

## 한줄요약

- Claude Code의 본질은 자연어 요청을 안전한 도구 실행 루프로 바꿔 실제 작업까지 밀어붙이는 에이전트형 CLI 구조입니다.

## 배경

- 이 글의 바탕이 된 위키독스 문서는 분석 대상을 `2026-03-31` 기준 Claude Code 소스 스냅샷으로 두고, 총 약 `1,884개`의 TypeScript + React 파일을 구조 중심으로 해설합니다. 문서는 유출 소스 자체를 공개하지 않고 동작 원리와 계층 구조에 집중한다고 밝힙니다.

| 항목 | 쉬운 설명 |
| --- | --- |
| 정체 | 터미널에서 동작하는 공식 Claude Code CLI |
| 구현 언어 | TypeScript |
| 화면 방식 | React 기반 Ink로 만든 터미널 UI |
| 상태 관리 | Zustand |
| 빌드 | bun |
| 핵심 특징 | 답변만 하는 게 아니라 파일, 명령, 검색, 외부도구까지 실행 |
| 확장 방식 | MCP로 GitHub, Slack, DB 같은 외부 기능 연결 가능 |

- 용어는 이 정도만 알고 읽으면 편합니다. Tool은 AI가 쓰는 실행 수단이고, Command는 사용자가 `/commit`처럼 직접 부르는 명령입니다. 또 MCP는 외부 서비스를 Claude Code에 붙이는 연결 표준입니다.
- Claude Code의 내장 도구는 45개 이상, 명령어는 80개 이상입니다. ([위키독스](https://wikidocs.net/338204 "

      별첨 91. 클로드 코드 소스 코드 분석서 - 클로드 코드 가이드

          "))

## 핵심

> Claude Code는 “대화형 AI”가 아니라, 도구 실행 루프를 중심으로 설계된 작업 엔진입니다.

- 전체 구조는 크게 `STARTUP → QUERY LOOP → TOOL EXECUTION → DISPLAY` 네 단계입니다. 이 네 칸만 먼저 잡아도 1,800개가 넘는 파일 설명이 어디에 속하는지 훨씬 쉽게 읽힙니다. ([위키독스](https://wikidocs.net/338204 "

      별첨 91. 클로드 코드 소스 코드 분석서 - 클로드 코드 가이드

          "))
- STARTUP 시작 단계에서는 인증, 모델 선택, 설정 로딩, Git 상태와 `CLAUDE.md` 같은 컨텍스트 수집이 먼저 이뤄집니다. 여기에 병렬 I/O 사전 실행과 조건부 모듈 로딩 같은 시작 최적화도 들어갑니다.
- QUERY LOOP 질의 루프에서는 스트리밍 응답, `tool_use` 감지, 긴 대화 압축, 에러 보류와 복구가 핵심입니다. 문서는 Snip Compact, Microcompact, Auto-Compact 같은 전략으로 토큰 한계를 관리한다고 설명합니다.
- TOOL EXECUTION 도구 실행부는 속도와 안전성의 균형이 포인트입니다. 안전한 도구는 최대 10개까지 병렬 실행하고, 편집이나 Bash처럼 위험도가 높은 작업은 순차적으로 단독 실행합니다.
- 이 강한 실행력을 통제하는 장치가 권한 시스템입니다. 입력 검증, 도구별 권한 확인, 사용자 정의 훅, `alwaysAllow`·`alwaysDeny` 규칙, 그리고 모드별 승인 정책이 순서대로 작동합니다.

```
[사용자 입력]
      ↓
[STARTUP]
인증 / 모델선택 / 설정 / Git상태 / CLAUDE.md
      ↓
[QUERY LOOP]
스트리밍 응답 / tool_use 감지 / 컨텍스트 압축
      ↓
[TOOL EXECUTION]
Read / Edit / Bash / Web / MCP
      ↓
[DISPLAY]
결과 표시 / diff / 진행상황
      ↑
      └──── tool_use가 남아 있으면 다시 루프
```

## 실습

## Tool과 Command를 분리해서 이해하기

1. - Tool은 AI가 자동으로 쓰는 기능이고, Command는 사용자가 직접 호출하는 기능입니다.
   - 예를 들어 파일 읽기나 편집은 Tool이고, `/commit`, `/review`, `/settings`는 Command 쪽입니다.
   - 이 차이를 잡으면 Claude Code 내부 구조가 훨씬 덜 헷갈립니다.   
     `Tool = FileRead / FileEdit / Bash / WebSearch`  
     `Command = /commit / review / settings / help`
2. 권한 파이프라인만 따로 외워두기
   - 실무 관점에서 제일 중요한 파트는 “무엇을 할 수 있나”보다 “무엇을 함부로 못 하게 막나”입니다.
   - 요청은 `validateInput()` → `checkPermissions()` → `PreToolUse hooks` → 규칙 매칭 → 권한 모드 판정 순으로 흘러갑니다.

```
[Tool 요청 도착]
      ↓
1) validateInput()
      ↓
2) checkPermissions()
      ↓
3) PreToolUse hooks
      ↓
4) 규칙 매칭
   - alwaysAllow → 승인
   - alwaysDeny  → 거부
   - alwaysAsk   → 사용자 확인
      ↓
5) 모드 판정
   - Default
   - Auto
   - Plan
   - Bypass
```

4. 확장 포인트를 마지막에 묶어보기
   - Claude Code를 단순 CLI로만 보면 반쪽 이해입니다.
   - MCP로 외부 도구를 붙이고, 스킬과 플러그인으로 복합 작업을 묶고, 코디네이터 모드에서는 리더 에이전트가 워커들을 병렬 운영한다고 설명합니다.
   - 즉, 도구를 넘어서 플랫폼처럼 확장되는 구조라는 점이 중요합니다. ([위키독스](https://wikidocs.net/338204 "

         별첨 91. 클로드 코드 소스 코드 분석서 - 클로드 코드 가이드

             "))
   - `Leader Agent` → `Worker 1 조사` / `Worker 2 수정` / `Worker 3 테스트` → `Leader 종합`

## 모범사례/패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| 질의 루프 중심 설계 | 한 번의 요청을 여러 번의 실행으로 자동 분해해 실제 작업까지 연결하기 좋음 | 루프가 길어질수록 컨텍스트 압축과 복구 전략이 중요해짐 |
| 안전/비안전 도구 분리 실행 | 읽기 계열은 빠르게 병렬화하고, 수정 계열은 충돌 없이 제어 가능 | 도구 분류가 잘못되면 속도나 안정성 중 하나를 잃기 쉬움 |
| 권한 파이프라인 우선 설계 | 실행력이 강한 도구를 현실적으로 통제할 수 있음 | 규칙과 모드가 많아질수록 운영 복잡도가 올라감 |
| MCP·스킬·플러그인 확장 | GitHub, Slack, DB 등으로 활용 범위가 크게 넓어짐 | 권한, 인증, 실패 처리까지 함께 설계해야 안정적임 |
| 리더-워커 코디네이터 패턴 | 큰 작업을 병렬 분업해 처리 속도를 높일 수 있음 | 리더가 결과를 검증하지 않으면 품질 편차가 커질 수 있음 |

- 위 비교표는 도구 동시성 모델, 권한 시스템, MCP 확장, 코디네이터 모드를 실무 패턴 관점으로 재배열한 것입니다.

## 마치며

- 핵심은 Claude Code를 “답변 잘하는 AI”가 아니라 “실제로 일하는 실행 시스템”으로 보게 만든다는 점입니다. ([위키독스](https://wikidocs.net/338204 "

      별첨 91. 클로드 코드 소스 코드 분석서 - 클로드 코드 가이드

          "))
- 특히 성능, 안전성, 확장성이 따로 노는 게 아니라 같은 루프 안에서 동시에 설계된다는 점이 인상적입니다. ([위키독스](https://wikidocs.net/338204 "

      별첨 91. 클로드 코드 소스 코드 분석서 - 클로드 코드 가이드

          "))
- 그래서 실무에서는 기능 이름보다, 요청이 어떤 도구와 권한과 상태를 거쳐 실행되는지 보는 시각이 더 중요합니다.
- 미팅에서 써먹을 한마디: **“Claude Code의 경쟁력은 모델 그 자체보다, 모델을 안전하게 일하게 만드는 실행 아키텍처에 있다.”**

## 참고자료

- 위키독스, 「별첨 91. 클로드 코드 소스 코드 분석서」 ([위키독스](https://wikidocs.net/338204 "

      별첨 91. 클로드 코드 소스 코드 분석서 - 클로드 코드 가이드

          "))
- Anthropic, Claude Code 공식 소개 및 인터페이스 예시 화면
