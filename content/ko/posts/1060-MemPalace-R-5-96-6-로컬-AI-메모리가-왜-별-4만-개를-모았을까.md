---
title: "? MemPalace, R@5 96.6% 로컬 AI 메모리가 왜 별 4만 개를 모았을까?"
date: 2026-04-17T02:47:49+09:00
slug: "1060-MemPalace-R-5-96-6-로컬-AI-메모리가-왜-별-4만-개를-모았을까"
original_url: "https://memoryhub.tistory.com/1060"
tistory_id: 1060
draft: false
---

```
   ┌───────────────────────────────────────┐
   │             MemPalace v3.3            │
   │   ┌─────────┐  ┌─────────┐  ┌──────┐  │
   │   │  Wing   │  │  Wing   │  │ Wing │  │
   │   │ project │  │ person  │  │ team │  │
   │   └────┬────┘  └────┬────┘  └──┬───┘  │
   │        │            │           │      │
   │     [Room]       [Room]      [Room]   │
   │        │            │           │      │
   │    [Drawer]     [Drawer]    [Drawer]  │
   │        원문       원문        원문     │
   │                                        │
   │   local-first · verbatim · MCP-ready   │
   │        R@5 96.6%  (no API key)         │
   └───────────────────────────────────────┘
```

# 인트로

Claude나 ChatGPT를 오래 쓰다 보면 꼭 겪는 일이 있어요. "지난주에 내가 뭐라고 말했더라", "그때 그 프로젝트 설정은 어떻게 했더라" 매번 같은 맥락을 다시 붙여넣고 있는 자신을 발견합니다. 저도 처음엔 요약본 몇 개로 해결될 줄 알았는데, 정작 필요한 순간마다 "그 부분은 요약에서 빠졌네요"라는 답을 받기 일쑤였죠.

이 글을 끝까지 읽으면 **로컬에서 공짜로 돌아가고, API 키 없이도 검색 재현율 96.6%를 찍는 오픈소스 AI 메모리 시스템**을 내 노트북에 5분 만에 붙이는 방법을 가져가실 수 있습니다.

## 한줄요약

MemPalace는 대화를 **원문 그대로 로컬에 저장**하고 **Wings·Rooms·Drawers 3계층**으로 검색 범위를 좁혀주는 오픈소스 메모리 시스템이며, MCP 서버 29종을 통해 Claude Code·Cursor·ChatGPT에 바로 꽂힌다.

## 왜 지금 이 프로젝트가 뜨는가

최근 AI 에이전트가 복잡해지면서 "장기 기억"을 외부에 저장하는 접근이 필수가 됐습니다.

기존 해법은 대부분 요약 기반이라 디테일이 증발하거나, 클라우드 API에 대화 전문을 올려야 했습니다.

MemPalace는 이 두 가지를 동시에 피하려고 만들어졌어요.

| 기존 메모리 시스템의 아쉬움 | MemPalace의 선택 |
| --- | --- |
| 요약·추출로 원문 손실 | Verbatim(원문 그대로) 저장 |
| 클라우드 API 의존 | Local-first, 임베딩·검색 전부 내 머신 |
| 평탄한 단일 코퍼스 검색 | Wings → Rooms → Drawers 3계층 스코핑 |
| 벤치마크 제각각이라 비교 난해 | LongMemEval·LoCoMo·ConvoMem·MemBench 공개 재현 |

공식 저장소는 `github.com/MemPalace/mempalace` 하나뿐이며, `mempalace.tech` 같은 유사 도메인은 README에 명시적으로 사칭이라고 경고되어 있으니 설치 전에 반드시 주소를 확인하세요.

## 핵심

> MemPalace는 대화 전문을 서랍(Drawer)에 원문 그대로 넣어두고, 의미 검색으로 꺼내는 로컬 AI 메모리 엔진이다.  
> 요약하지 않고 공간으로 나누기 때문에 "디테일 손실 없음 + 좁은 범위 검색"이 동시에 가능해진다.

구조는 아주 단순합니다. Wings는 사람이나 프로젝트 단위의 최상위 컨테이너, Rooms는 그 안의 주제 폴더, Drawers는 실제 원문이 저장되는 최소 단위입니다.

기본 벡터 백엔드는 ChromaDB이며, 인터페이스(`mempalace/backends/base.py`)만 맞추면 다른 백엔드로 교체할 수 있습니다.

벤치마크는 세 단계로 나눠 봐야 해석이 정확합니다. 언어·버전 기준은 **Python 3.9+ / MemPalace v3.3.0 (2026-04-14 릴리스)** 입니다.

```
# Python 3.9+ / mempalace 3.3.0
from mempalace import Palace

palace = Palace.open("~/projects/myapp")
palace.search("왜 GraphQL로 바꿨더라")
# Drawer 원문 + Wing/Room 경로가 함께 반환된다
```

## 실습

### ① 설치

```
# Python 3.9+, ~300MB (기본 임베딩 모델)
pip install mempalace
mempalace init ~/projects/myapp
```

설치 직후 `~/projects/myapp/.mempalace/` 아래에 Wings 기본 구조와 SQLite 기반 지식 그래프 DB가 생성됩니다. 화면에는 초기화된 Wing 이름과 ChromaDB 컬렉션 경로가 출력됩니다(그림 대체 설명).

### ② 대화·프로젝트 채굴(Mine)

```
# 프로젝트 파일을 서랍에 넣기
mempalace mine ~/projects/myapp

# 대화 내보내기(JSON·Markdown 등)를 서랍에 넣기
mempalace mine ~/chats/ --mode convos
```

`mine`은 원문을 그대로 쪼개 Drawer에 저장하고, 자동으로 Room·Wing으로 분류합니다. 요약·의역은 일절 하지 않습니다.

### ③ 검색과 세션 깨우기

```
mempalace search "왜 GraphQL로 바꿨더라"
mempalace wake-up   # 새 세션 시작 시 관련 맥락을 꺼내온다
```

검색 결과는 Drawer 원문 + Wing·Room 경로 + 유사도 점수가 함께 나옵니다.

화면 우측에 최근 접근한 Room이 나란히 표시되어 맥락 전환이 빠릅니다(그림 대체 설명).

### ④ Claude Code에 MCP로 연결

```
mempalace mcp   # 로컬 MCP 서버 기동 (stdio)
```

Claude Code의 MCP 설정에 위 명령을 등록하고 재시작하면, 29종의 MCP 도구(팰리스 읽기·쓰기, 지식 그래프, 크로스 윙 탐색, 서랍 관리, 에이전트 다이어리)가 자동 노출됩니다. 외부 네트워크 호출 없이 로컬 파이프로만 통신합니다.

## 고를 때 참고할 패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| Verbatim 저장 (MemPalace 기본) | 원문 손실 없음, 사후 재질의에 강함 | 디스크 사용량 증가, 민감 정보는 선별 저장 필요 |
| 요약 기반 메모리 | 용량 절약, 빠른 문맥 주입 | 세부 정보 소실, 재요약 시 누락 누적 |
| 클라우드 메모리 SaaS | 초기 셋업 간단, 기기 간 동기화 쉬움 | API 키 비용, 대화 전문이 외부로 전송됨 |
| 단일 코퍼스 벡터 DB | 구조 단순, 구현 쉬움 | 검색 범위 제한 어려움, 프로젝트·인물 구분 난해 |
| Wings·Rooms·Drawers 스코핑 | 검색 범위를 자연스럽게 좁힘, 윙 단위 삭제 용이 | 초기 분류 규칙 학습 필요, 채굴 흐름 이해 필수 |

벤치마크는 공식 README 기준으로 **LongMemEval R@5 Raw 96.6% / Hybrid v4 held-out 98.4% / Rerank ≥99%**, LoCoMo Hybrid v5 R@10 88.9%, ConvoMem 평균 재현율 92.9%, MemBench R@5 80.3%입니다. 저자들은 "100%"라는 수치는 테스트 암기에 가깝다고 스스로 경계하므로, 실제 운영 기대치는 Raw 96.6% 또는 held-out 98.4%로 잡는 편이 정직합니다.

## 마치며

MemPalace는 "요약하지 않고, 밖으로 내보내지 않고, 공간으로 나눈다"는 세 가지 원칙으로 AI 장기 기억을 설계한 오픈소스 프로젝트입니다. Python 3.9+에 `pip install`만 하면 붙고, MCP 한 줄로 Claude Code에 바로 연결되니 오늘 바로 내 작업 흐름에 끼워 실험해 볼 만합니다. 공식 저장소와 `mempalaceofficial.com` 외의 도메인은 사칭이라는 점만 반드시 기억해 두세요.

## 참고자료

- MemPalace 공식 GitHub 저장소 (v3.3.0, 2026-04-14) — <https://github.com/MemPalace/mempalace>
- MemPalace 공식 도큐먼트 사이트 — <https://mempalaceofficial.com>
- PyPI 패키지 페이지 — <https://pypi.org/project/mempalace/>
- 벤치마크 방법론(BENCHMARKS.md) — <https://github.com/MemPalace/mempalace/blob/main/benchmarks/BENCHMARKS.md>
- 릴리스 노트(CHANGELOG) — <https://github.com/MemPalace/mempalace/blob/main/CHANGELOG.md>
- 사칭 도메인 경고 및 이력(docs/HISTORY.md) — <https://github.com/MemPalace/mempalace/blob/main/docs/HISTORY.md>
