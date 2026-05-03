---
title: "? pi-autoresearch, AI가 밤새 내 코드를 스스로 튜닝한다고요?"
date: 2026-04-17T01:38:25+09:00
slug: "1053-pi-autoresearch-AI가-밤새-내-코드를-스스로-튜닝한다고요"
original_url: "https://memoryhub.tistory.com/1053"
tistory_id: 1053
draft: false
---

```
┌──────────────────────────────┐
│     [ 1. 아이디어 생성 ]     │
│              ↓               │
│     [ 2. 코드 수정·커밋 ]    │
│              ↓               │
│     [ 3. 벤치마크 실행 ]     │
│              ↓               │
│    개선?  Yes  ->  keep      │
│           No   ->  revert    │
│              ↺               │
│        반복 & 누적 기록      │
└──────────────────────────────┘
         pi-autoresearch
```

# 

## 서론 — 수동 벤치마크, 이제 그만

코드를 한 줄 바꿀 때마다 번들 사이즈가 얼마나 줄었는지 일일이 재보신 적 있으신가요? 테스트가 1초라도 더 빨라지길 바라며 "측정 → 수정 → 재측정"을 수십 번 돌려 본 경험, 개발자라면 누구나 있으실 겁니다. pi-autoresearch는 이 반복 루프를 AI 에이전트가 대신 굴려 주는 오픈소스 확장입니다. 이 글을 다 읽으시면 "어떤 지표든" 자동으로 최적화해 주는 실험 루프의 동작 방식과 직접 설치·구동하는 방법까지 한 번에 잡으실 수 있습니다.

## 한줄요약

> pi-autoresearch는 pi AI 코딩 에이전트에 "시도 → 측정 → 채택 or 폐기 → 반복" 자율 실험 루프를 붙여, 어떤 지표든 노이즈에 속지 않고 밤새 알아서 최적화하도록 만들어 주는 MIT 라이선스 오픈소스 확장입니다.

## 왜 지금 이 도구가 주목받나

Karpathy가 공개한 autoresearch 패턴은 원래 LLM 훈련 loop 조율을 위한 ML 전용 기법이었습니다.

pi-autoresearch는 이 아이디어를 "측정 가능한 모든 소프트웨어 지표"로 일반화해 확장성을 크게 넓혔습니다.

실제로 Shopify의 Tobi Lutke CEO가 직접 "pi용 autoresearch 플러그인을 오픈소스로 공개했다"고 알리면서 주목을 끌었고,

현재 4.7k 스타를 넘긴 상태입니다.

| 용어 | 설명 |
| --- | --- |
| pi | 터미널 기반 AI 코딩 에이전트(확장 호스트) |
| autoresearch 루프 | try-measure-keep-discard-repeat 자율 최적화 사이클 |
| MAD | Median Absolute Deviation, 측정 노이즈 기반 신뢰도 지표 |
| 지표(metric) | 최적화 대상(테스트 속도·번들 크기·Lighthouse 점수 등) |

## 핵심 구조

> pi-autoresearch는 지정한 지표가 실제로 개선되는지 자동으로 실험·검증하고,   
> 리뷰 가능한 독립 브랜치로 정리까지 맡기는 pi 확장입니다.
>
> init\_experiment·run\_experiment·log\_experiment 세 도구로 루프를 돌리고,   
> MAD 신뢰도 점수로 노이즈를 걸러낸 뒤,   
> autoresearch-finalize가 검증된 변경을 깔끔한 브랜치로 잘라 줍니다.

확장이 제공하는 파일은 단순합니다. 벤치마크 본체는 Shell 스크립트 한 줄이면 충분합니다.

```
# autoresearch.sh (Bash 5.x 예시 — 테스트 시간을 metric으로 출력)
pnpm test 2>&1 | tail -n 1 \
  | awk '{print "METRIC name=test_time value="$NF}'
```

에이전트는 이 스크립트의 `METRIC name=... value=...` 출력 라인을 파싱해 `autoresearch.jsonl`에 append-only로 기록합니다. 중단돼도 다음 세션에서 같은 jsonl을 읽어 이어서 돌릴 수 있다는 점이 큰 장점입니다.

## 직접 해보기

### ① 설치

터미널에서 한 줄이면 끝납니다.

```
pi install https://github.com/davebcn87/pi-autoresearch
```

수동 설치를 원하시면 저장소의 `extensions/`와 `skills/` 디렉터리를 각각 `~/.pi/agent/extensions/`, `~/.pi/agent/skills/`로 복사한 뒤 pi 세션에서 `/reload`를 실행하시면 됩니다.

### ② 세션 초기화

pi 대화창에서 `/skill:autoresearch-create`를 호출하면 에이전트가 목표·실행 명령·지표·수정 범위 파일을 차례로 물어봅니다. 예를 들어 "Jest 테스트 전체 실행 시간 10% 단축, 단 기존 테스트는 모두 통과"처럼 알려 주면 됩니다.

### ③ 루프 구동 & 결과 확인

이후에는 에이전트가 코드 수정 → git 커밋 → `autoresearch.sh` 실행 → metric 파싱 → jsonl 기록을 자동 반복합니다.

실험이 3회 이상 누적되면 MAD 기반 신뢰도가 붙어 나옵니다. 예시 출력은 다음과 같은 형태입니다.

```
run #7  metric=test_time  value=18.42s  best_delta=-1.80s
         MAD=0.42s  confidence=4.3x   [green]
```

공식은 `confidence = |best_improvement| / MAD`이고, 해석 기준은 아래와 같습니다.

- 2.0× 이상(green): 개선이 실제일 가능성 높음
- 1.0–2.0×(yellow): 노이즈보다는 크지만 경계
- 1.0× 미만(red): 사실상 노이즈, 재실행 권장

### ④ 마무리(finalize)

`/skill:autoresearch-finalize`를 돌리면 jsonl에 "keep"으로 마킹된 실험만 골라,

파일이 겹치지 않는 단위로 묶어 merge-base에서 출발하는 독립 브랜치를 각각 생성해 줍니다.

각 브랜치는 별도 PR로 안전하게 리뷰·병합할 수 있습니다.

### ⑤ 선택 설정

세션 디렉터리에 `autoresearch.config.json`을 두면 실행 범위를 제한할 수 있습니다.

```
{
  "workingDir": "/path/to/project",
  "maxIterations": 50
}
```

`maxIterations`는 LLM 호출 비용 상한을 강제하는 가장 확실한 장치이니 꼭 설정해 두시는 걸 권장합니다.

## 유사 접근 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| pi-autoresearch (자율 루프 + MAD) | 노이즈 기반 신뢰도로 "가짜 개선" 자동 제거, 중단 후 재개 가능, finalize가 독립 브랜치까지 뽑아 줌 | pi 런타임과 LLM API 키 필요, maxIterations 미설정 시 비용 폭주 가능 |
| karpathy/autoresearch 원형 | ML 훈련 loop 최적화에서 검증된 레퍼런스 구현 | 도메인이 ML에 묶여 일반 SW 지표에 그대로 쓰기 어려움 |
| 수동 벤치마크 스크립트 | 외부 의존성 제로, 완전한 수동 제어 | 반복·비교·롤백을 사람이 모두 처리, 노이즈 판단에 주관 개입 |

## 마치며

pi-autoresearch는 "측정 가능한 지표라면 무엇이든" 자동으로 돌릴 수 있는 일반화된 실험 루프 인프라입니다.

MAD 기반 신뢰도 점수 덕분에 측정 노이즈에 속지 않고, finalize 단계에서 리뷰 가능한 독립 브랜치까지 뽑아 준다는 점이

실무 친화적입니다. 반복되는 최적화 작업이 있으시다면, 하루만 돌려 보고 성과를 비교해 보시는 것도 좋은 선택입니다.

## 참고자료

- [pi-autoresearch GitHub 저장소](https://github.com/davebcn87/pi-autoresearch)
- [pi-autoresearch 확장 디렉터리 소스](https://github.com/davebcn87/pi-autoresearch/tree/main/extensions/pi-autoresearch)
- [Ry Walker — pi-autoresearch 리서치 노트](https://rywalker.com/research/pi-autoresearch)
- [Tobi Lutke X(트위터) 오픈소스 공지](https://x.com/tobi/status/2032212536716578932)
