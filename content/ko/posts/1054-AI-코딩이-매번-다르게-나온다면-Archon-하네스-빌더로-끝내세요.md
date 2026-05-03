---
title: "? AI 코딩이 매번 다르게 나온다면, Archon 하네스 빌더로 끝내세요"
date: 2026-04-17T01:46:45+09:00
slug: "1054-AI-코딩이-매번-다르게-나온다면-Archon-하네스-빌더로-끝내세요"
original_url: "https://memoryhub.tistory.com/1054"
tistory_id: 1054
draft: false
---

```
   ┌────────┐   ┌────────────┐   ┌────────┐   ┌──────┐
   │  plan  │──▶│ implement  │──▶│  test  │──▶│  PR  │
   └────────┘   └────────────┘   └────────┘   └──────┘
           YAML workflow · deterministic node · AI node
                    .archon/workflows/*.yaml
```

# 

## 들어가며

같은 지시를 두 번 내렸는데 결과가 달라서 당황한 적, 한 번쯤은 있으실 거예요.

저도 Claude Code에 "리팩터링 후 테스트까지 돌려줘"라고 매번 똑같이 말해도,

어떤 날은 PR까지 올리고 어떤 날은 중간에 멈추곤 했습니다.

이런 '들쭉날쭉한 AI 코딩'을 재현 가능한 절차로 묶어주는 오픈소스가 바로 Archon이에요.

이 글을 끝까지 읽으시면 30초 설치부터 기본 워크플로우 실행까지,

오늘 당장 프로젝트에 붙이는 방법을 파악하실 수 있습니다.

## 한줄요약

Archon은 AI 코딩 절차를 YAML 워크플로우로 고정해 같은 결과를 반복 재현하도록 만들어주는, n8n 같은 최초의 오픈소스 하네스 빌더입니다.

## 왜 지금 Archon인가

'바이브 코딩(vibe coding)'이라는 말처럼 AI 어시스턴트는 요청을 받을 때마다 조금씩 다른 경로를 탑니다.

이 비결정성은 프로토타입에서는 괜찮지만, 팀 공통 프로세스나 반복 작업에서는 품질 저하의 원인이 돼요.

Archon 제작자는 "Dockerfile이 인프라에, GitHub Actions가 CI/CD에 해준 일을 AI 코딩 워크플로우에 한다"라고 포지셔닝합니다.

참고로 이름이 같은 구 버전이 하나 있는데요, 기존 'Archon OS'는 Python 기반 MCP 서버로 지식·태스크 관리 백본을 담당했고,

2026년 4월 현재 저장소는 TypeScript + Bun 기반 워크플로우 엔진으로 완전히 재작성되었습니다.

이 글은 재작성 이후 최신 버전을 기준으로 설명드려요.

| 용어 | 정의 |
| --- | --- |
| 하네스(Harness) | AI 모델 호출을 감싸 절차·검증·출력 형식을 강제하는 외부 골격 |
| 결정적 노드 | `bash:` 등 고정된 명령을 그대로 실행하는 단계 |
| AI 노드 | `prompt:`로 모델에게 지능을 채우게 하는 단계 |
| 워크플로우 | 노드들의 의존 관계(DAG)를 YAML로 기록한 실행 계획서 |

## 핵심 개념

> AI 코딩의 절차를 YAML로 못 박고, 지능은 그 틀 안에서만 채워 넣는다.  
> 결과적으로 실행 순서는 결정적이지만, 각 단계의 판단은 여전히 AI가 담당합니다.

아래는 공식 README에 실린 가장 작은 샘플이에요. `depends_on`으로 의존성을 걸고, `loop + until`로 반복 종료를 명시하며, `bash:`로 검증까지 꽂는 구조를 보실 수 있습니다.

```
# .archon/workflows/sample.yaml  ·  Archon (Bun/TypeScript, 2026-04)
nodes:
  - id: plan
    prompt: "Explore the codebase and create an implementation plan"
  - id: implement
    depends_on: [plan]
    loop:
      prompt: "Read the plan. Implement the next task. Run validation."
      until: ALL_TASKS_COMPLETE
  - id: run-tests
    depends_on: [implement]
    bash: "bun run validate"
  - id: create-pr
    depends_on: [run-tests]
    prompt: "Push changes and create a pull request"
```

핵심은 세 가지예요.

첫째, 각 실행이 별도 git worktree에서 돌기 때문에 여러 작업을 병렬로 돌려도 서로 간섭하지 않습니다.

둘째, 같은 워크플로우는 매번 같은 순서로 실행되므로 팀원 간 편차가 사라집니다.

셋째, YAML 파일을 `.archon/workflows/`에 커밋하면 CLI·Web UI·Slack·Telegram·GitHub 어디서든 동일하게 호출돼요.

## 실습: 0에서 첫 워크플로우까지

### ① 사전 준비

Bun 런타임(공식 홈페이지 bun.sh), GitHub CLI, Claude Code가 설치돼 있어야 합니다.

세 가지 모두 맥·리눅스·윈도우에서 공식 배포 스크립트로 설치할 수 있어요.

### ② 30초 설치

아래 한 줄이면 CLI가 바로 잡힙니다.

```
# macOS / Linux
curl -fsSL https://archon.diy/install | bash

# Windows (PowerShell)
irm https://archon.diy/install.ps1 | iex
```

### ③ 풀 셋업 (약 5분)

소스까지 받아 기여하거나 내부 흐름을 보고 싶으시다면 아래처럼 진행하시면 됩니다.

```
git clone https://github.com/coleam00/Archon
cd Archon
bun install
claude
```

이어서 Claude Code 세션 안에 "Set up Archon"이라고 말하면, MCP 서버 등록과 기본 템플릿 배치까지 알아서 처리합니다.

### ④ 첫 워크플로우 실행

자신의 프로젝트 루트로 이동해 Claude Code를 연 뒤, 이렇게 말씀하시면 됩니다.

```
Use archon to add dark mode to the settings page
```

라우터가 17개의 기본 워크플로우 중 의도에 가장 맞는 것을 자동 선택해 실행합니다.

직접 고르고 싶다면 `archon workflow list`로 목록을 확인한 뒤 이름으로 지정할 수도 있어요.

대표 워크플로우로는 `archon-assist`(일반 Q&A·디버깅), `archon-fix-github-issue`(이슈 조사부터 PR까지), `archon-idea-to-pr`(기능 구현 파이프라인), `archon-comprehensive-pr-review`(멀티 에이전트 리뷰), `archon-refactor-safely`(검증이 포함된 안전한 리팩터링) 등이 있습니다.

실행 결과는 Web 대시보드에서도 실시간으로 확인 가능합니다.

새 터미널에서 `archon serve`를 실행하면 브라우저에서 진행 상황과 로그, 아티팩트를 모니터링할 수 있어요(설치 직후 한 번만 실행해두시면 편합니다).

## 접근 방식 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| 자유 프롬프팅(매번 지시) | 빠른 시작, 아이디어 실험에 유리 | 결과 비결정성, 팀 단위 재현 어려움 |
| Archon 워크플로우 | 같은 순서·같은 검증 반복, 병렬 워크트리로 안전 | 워크플로우 초기 설계 비용, Bun·Claude Code 의존 |
| 전통 셸/CI 스크립트 | 완전 결정적, 기존 인프라 재활용 | AI 판단 단계를 끼워 넣기 어려움, 유연성 부족 |

세 방식은 상호 배타적이지 않습니다. 탐색 단계에서는 자유 프롬프팅으로 감을 잡고, 안정화된 반복 작업은 Archon 워크플로우로 묶고,

배포·체크 같은 완전 결정적 영역은 기존 CI에 맡기는 분업이 자연스러워요.

## 마치며

AI 코딩의 다음 숙제는 '더 똑똑한 모델'보다 '더 예측 가능한 절차'라는 관점이 점점 힘을 얻고 있습니다. Archon은 YAML이라는 익숙한 포맷에 결정적 실행과 AI 판단을 나란히 얹어, 그 해답을 오픈소스로 먼저 제시합니다.

2026년 4월 기준 GitHub 스타 1.8만 개를 넘기며 빠르게 크고 있으니,

반복 작업이 많은 프로젝트라면 한 번쯤 워크플로우 한두 개를 만들어 붙여보시길 권해드립니다.

## 참고자료

- Archon GitHub 저장소 — <https://github.com/coleam00/Archon>
- Archon README (dev 브랜치) — <https://github.com/coleam00/Archon/blob/dev/README.md>
- Archon 공식 문서·설치 홈페이지 — <https://archon.diy>
- 완전 재작성 공지 이슈 #957 — <https://github.com/coleam00/Archon/issues/957>
- HelloGitHub 소개 페이지 — <https://hellogithub.com/en/repository/coleam00/Archon>
- AIToolly 기사(2026-04-14) — <https://aitoolly.com/ai-news/article/2026-04-14-archon-the-first-open-source-ai-coding-test-framework-generator-for-deterministic-and-repeatable-dev>
