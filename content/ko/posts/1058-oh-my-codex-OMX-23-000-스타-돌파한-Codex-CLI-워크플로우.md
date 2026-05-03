---
title: "? oh-my-codex(OMX), 23,000 스타 돌파한 Codex CLI 워크플로우"
date: 2026-04-17T02:03:52+09:00
slug: "1058-oh-my-codex-OMX-23-000-스타-돌파한-Codex-CLI-워크플로우"
original_url: "https://memoryhub.tistory.com/1058"
tistory_id: 1058
draft: false
---

```
        ┌─────────────────────────────┐
        │   OMX Workflow Layer        │
        │  $deep-interview / $ralplan │
        │     $team   /   $ralph      │
        └──────────────┬──────────────┘
                       │
                       ▼
        ┌─────────────────────────────┐
        │     OpenAI Codex CLI        │
        │   (Execution Engine)        │
        └──────────────┬──────────────┘
                       │
                       ▼
        ┌─────────────────────────────┐
        │  .omx/  — plans · logs ·    │
        │          memory · state     │
        └─────────────────────────────┘
```

요즘 Codex CLI 한 번 써보신 분이라면 한 번쯤 이런 경험 있으실 겁니다. 세션마다 처음부터 컨텍스트 다시 깔고,

멀티 에이전트 굴리려니 worktree 수동으로 만들고, 훅(hook) 한번 붙이려면 설정 파일 새로 짜야 하고.

그래서 GitHub에서 23,000 스타 넘은 `oh-my-codex`(이하 OMX)가 4월 들어 화제입니다.

이 글 한 편이면 OMX가 무엇이고, 왜 깔아야 하는지, 어떻게 첫 세션을 띄우는지까지 정리됩니다.

## 한줄요약

OMX는 OpenAI Codex CLI를 갈아끼우지 않고 그 위에 표준 워크플로우·skill·영속 상태(`.omx/`)를 얹는 얇은 레이어다.

## 왜 지금 OMX인가

Codex CLI 자체는 가볍고 강력하지만, 실무에서 반복되는 몇 가지 빈자리가 분명합니다.

| 빈자리 | Codex CLI 단독 | OMX 적용 후 |
| --- | --- | --- |
| 멀티 에이전트 코디네이션 | 사용자가 수동 worktree·tmux 구성 | `$team N:executor`로 자동 분기 |
| 세션 영속성 | 세션 종료 시 컨텍스트 휘발 | `.omx/` 하위 plans·logs·memory 저장 |
| 표준 워크플로우 | 매번 즉흥적 프롬프트 | `$deep-interview`→`$ralplan`→`$ralph` 파이프라인 |
| 훅(hook) 통합 | `.codex/hooks.json` 직접 편집 | OMX-managed wrapper 자동 등록 |

용어 정리부터 짚고 가겠습니다.

- **Codex CLI**: OpenAI 공식 터미널 코딩 에이전트. `npm install -g @openai/codex`로 설치하며 GPT-5.4·GPT-5.3-Codex 등 모델을 탑재한 실행 엔진입니다.
- **OMX(oh-my-codex)**: Codex CLI 위에 워크플로우, skill, runtime, HUD를 더하는 TypeScript 기반 npm 패키지. MIT 라이선스, 2026-02-02 첫 공개, 2026-04-16 기준 v0.12.1.
- **skill**: OMX가 등록한 재사용 가능 명령. `$deep-interview`, `$ralplan`, `$ralph`, `$team` 4종이 기본 권장 흐름입니다.

## 핵심

> OMX는 Codex의 코드 생성 능력은 그대로 두고, "어떻게 일을 시킬지"를 표준화한다.

쉽게 말해 Codex가 **두뇌**라면 OMX는 **업무 매뉴얼 + 사무실**입니다. 매뉴얼(skill)은 언제 무엇을 호출할지를 정해주고,

사무실(`.omx/`)은 진행 중인 계획과 기록을 보관해 다음 세션이 어디서 멈췄는지 알게 합니다.

설치는 두 줄이면 끝납니다.

```
# Node.js 20+ 필요
npm install -g @openai/codex oh-my-codex
omx setup
```

`omx setup`은 `.codex/config.toml`, OMX-managed 훅, AGENTS 스캐폴딩, skill 묶음을 한 번에 깔아둡니다.

기존 사용자 훅이 `.codex/hooks.json`에 있다면 보존하고 OMX wrapper만 갱신하므로,

안전하게 재실행 가능한 멱등 설계입니다.

## 실습으로 첫 세션 띄우기

### ① 설치와 인증

```
npm install -g @openai/codex oh-my-codex
codex   # 최초 1회 ChatGPT 계정 또는 API 키로 로그인
omx setup
```

설치가 끝나면 `omx doctor`로 점검 가능합니다. 출력 예시는 대략 다음과 같습니다.

```
✔ codex CLI detected (v...)
✔ .codex/config.toml ready
✔ OMX-managed hooks installed
✔ tmux available
```

### ② 권장 첫 실행

```
omx --madmax --high
```

`--madmax --high`는 OMX가 권장하는 "강하게 시작" 모드입니다.

인터랙티브 leader 세션이 바로 떠서 skill 명령을 받기 시작합니다.

### ③ 표준 워크플로우 4단계 굴려보기

Codex 세션 안에서 다음 순서로 입력합니다.

```
$deep-interview "JWT 갱신 로직을 다시 짜고 싶다. 경계 조건이 모호하다"
$ralplan "검토된 의도를 바탕으로 안전한 구현 계획을 승인해 달라"
$ralph "승인된 계획을 끝까지 책임지고 완료까지 밀어붙여라"
# 또는 병렬 실행이 필요하면
$team 3:executor "승인된 계획을 3명이 병렬로 수행"
```

각 skill의 역할은 다음과 같습니다.

- `$deep-interview`: 요구사항·non-goal 명확화. 모호하면 여기서부터 시작합니다.
- `$ralplan`: 명확화된 스코프를 아키텍처·구현 계획으로 승인합니다.
- `$ralph`: 한 명의 owner가 끈질기게 완료까지 검증 루프를 도는 모드.
- `$team N:role`: tmux + isolated git worktree 기반으로 N명을 병렬 가동. worktree 격리 덕분에 머지 충돌이 발생하지 않습니다.

### ④ 운영 보조 명령

```
omx team status <team-name>     # 진행 상황
omx team resume <team-name>     # 중단된 팀 재개
omx hud --watch                 # 실시간 모니터링 HUD
omx explore --prompt "팀 상태가 어디에 기록되는지 찾아줘"
omx sparkshell git status       # 쉘 기반 검사
omx wiki query --input '{"query":"session-start lifecycle"}' --json
```

`omx wiki`는 로컬 마크다운 기반 검색 우선 위키 MCP 서버라, 벡터 DB 없이도 프로젝트 노트를 빠르게 끌어올 수 있습니다.

## 모범사례 패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| `$deep-interview` 먼저 (Clarify-First) | 잘못된 방향으로 코드 짤 위험 차단, non-goal 미리 합의 | 단순 요청에 과한 절차일 수 있음 — 명확한 작업이면 건너뛰는 판단 필요 |
| `$ralph` 단독 루프 | 한 명의 owner가 검증까지 책임 → 결과물 일관성 높음 | 작업 규모가 크면 단독 실행이 병목 — `$team`으로 분기 권장 |
| `$team N:executor` 병렬 | worktree 자동 격리 → 머지 충돌 0, 컨텍스트 손실 최소화 | tmux(또는 Windows의 psmux) 의존, Intel Mac에서 `syspolicyd` CPU 스파이크 보고됨 |
| 네이티브 Codex 훅 활용 | `.codex/hooks.json`이 lifecycle의 정식 surface, 외부 도구와 표준 호환 | OMX-managed 영역과 사용자 영역이 섞이지 않게 `omx setup`/`omx uninstall` 멱등성 신뢰할 것 |

## 마치며

OMX는 Codex CLI의 자리를 빼앗지 않고 그 위에 매뉴얼과 사무실을 붙여, 매번 새로 시작하던 세션을 표준 파이프라인으로 묶어줍니다. 권장 흐름은 단순합니다 — `omx setup`으로 깔고, `omx --madmax --high`로 띄우고, 명확화→계획 승인→완료 루프 또는 병렬 팀 순서로 굴리면 됩니다. macOS·Linux + tmux 환경이라면 가장 안정적이며, Windows는 WSL2를 우선 고려하시는 편이 좋습니다.

## 참고자료

- [oh-my-codex GitHub 저장소 (README)](https://github.com/Yeachan-Heo/oh-my-codex)
- [oh-my-codex 공식 사이트](https://yeachan-heo.github.io/oh-my-codex-website/)
- [oh-my-codex npm 패키지](https://www.npmjs.com/package/oh-my-codex)
- [OpenAI Codex CLI 공식 문서](https://developers.openai.com/codex/cli)
- [OpenAI Codex CLI 빠른 시작](https://developers.openai.com/codex/quickstart)
- [OpenAI Codex GitHub](https://github.com/openai/codex)
- [What Is Oh My Codex (OMX)? Complete 2026 Guide — a2a-mcp.org](https://a2a-mcp.org/blog/what-is-oh-my-codex)
