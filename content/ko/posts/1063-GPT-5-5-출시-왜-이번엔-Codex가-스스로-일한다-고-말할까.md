---
title: "? GPT-5.5 출시, 왜 이번엔 \"Codex가 스스로 일한다\"고 말할까?"
date: 2026-04-24T05:10:43+09:00
slug: "1063-GPT-5-5-출시-왜-이번엔-Codex가-스스로-일한다-고-말할까"
original_url: "https://memoryhub.tistory.com/1063"
tistory_id: 1063
draft: false
cover:
  image: "/images/1063-GPT-5-5-출시-왜-이번엔-Codex가-스스로-일한다-고-말할까/img.png"
  relative: false
  hidden: false
---

![](/images/1063-GPT-5-5-출시-왜-이번엔-Codex가-스스로-일한다-고-말할까/img.png)

GPT-5.4 나온 지 겨우 6주 만에 GPT-5.5가 올라왔습니다. 저도 처음엔 "또 소소한 업데이트 아닌가" 했는데, 벤치마크 수치만 보고 넘길 글이 아니더라고요. Terminal-Bench 2.0에서 82.7%, GDPval에서 84.9%,

그리고 결정적으로 같은 작업을 GPT-5.4보다 **더 적은 토큰으로** 끝내버립니다.

오늘 글을 읽으면 GPT-5.5가 실제로 뭐가 달라졌는지, 어떤 플랜에서 어떻게 써야 하는지,

그리고 네 API 가격이 왜 2배가 됐는지까지 한 번에 정리됩니다.

> GPT-5.5는 "더 똑똑한데 더 빠르고, 심지어 토큰도 덜 쓰는" 모델이며, Codex 안에서 장시간 과제를 사람처럼 끝까지 물고 가는 것이 진짜 차별점입니다.

## 왜 지금 이 모델이 나왔을까요

최근 프론티어 AI 경쟁은 "똑똑함"을 넘어 "얼마나 오래, 얼마나 자율적으로 일하느냐"로 넘어가고 있습니다. GPT-5.4도 충분히 빠르고 강했지만 긴 호흡의 엔지니어링·리서치 작업에서 중간에 막히거나 일찍 멈추는 경우가 남아 있었습니다.

이번 GPT-5.5는 바로 그 지점을 겨냥한 업데이트입니다.

먼저 용어부터 정리해 두면 읽기 편합니다.

| 용어 | 뜻 |
| --- | --- |
| Codex | OpenAI가 만든 코딩·컴퓨터 조작 전용 에이전트 환경 |
| Terminal-Bench 2.0 | 명령줄 환경에서 계획·도구 사용·반복을 평가하는 벤치마크 |
| GDPval | 44개 직군의 실제 지식 노동 과제 수행 품질을 재는 벤치마크 |
| OSWorld-Verified | 실제 컴퓨터 환경을 모델이 조작하는 역량 평가 |
| FrontierMath Tier 4 | 현대 수학 난제 최상급 난이도 문제 모음 |
| Preparedness Framework | OpenAI의 위험 단계 평가 체계(High, Critical 등) |

## 핵심 차이 한 눈에

> GPT-5.5는 "에이전틱 코딩·컴퓨터 사용·지식 노동·초기 과학 연구" 네 축에서 동시에 SOTA를 찍은 모델이다.
>
> 같은 작업을 GPT-5.4보다 **더 적은 토큰**으로 해결한다는 점이 벤치 숫자보다 더 중요한 변화다.

벤치마크 수치를 정리하면 다음과 같습니다(공식 발표 기준).

| 벤치마크 | GPT-5.5 | GPT-5.4 | Claude Opus 4.7 | Gemini 3.1 Pro |
| --- | --- | --- | --- | --- |
| Terminal-Bench 2.0 | **82.7%** | 75.1% | 69.4% | 68.5% |
| Expert-SWE(내부) | **73.1%** | 68.5% | - | - |
| GDPval | **84.9%** | 83.0% | 80.3% | 67.3% |
| OSWorld-Verified | **78.7%** | 75.0% | 78.0% | - |
| FrontierMath Tier 4 | **35.4%** | 27.1% | 22.9% | 16.7% |
| CyberGym | **81.8%** | 79.0% | 73.1% | - |

그리고 GPT-5.5 Pro는 FrontierMath Tier 4에서 **39.6%**, BrowseComp에서 **90.1%**를 찍으며 GPT-5.4 Pro를 한 단계 위에서 밀어냅니다. 특히 Tau2-bench Telecom에서는 프롬프트 튜닝 없이 **98.0%** 정확도를 보여서, 실제 고객 서비스 자동화 수준이 상용 단계에 가까워졌다는 평가를 받습니다.

## 실제로 어떻게 써볼 수 있나요

### ①ChatGPT에서 바로 확인하기

Plus·Pro·Business·Enterprise 플랜 사용자는 모델 선택 드롭다운에서 **GPT-5.5 Thinking**을 고를 수 있습니다. Pro 이상 플랜은 **GPT-5.5 Pro**까지 선택 가능합니다. 요약·리서치·문서 작업처럼 "긴 문맥을 잘라서 보여주는" 작업에서 체감 차이가 가장 큽니다.

### ②Codex에서 복잡한 과제 맡기기

Plus·Pro·Business·Enterprise·Edu·Go 플랜에서 Codex를 열면 GPT-5.5를 **400K 컨텍스트 윈도우**로 쓸 수 있습니다.

Fast mode를 켜면 **토큰 생성 1.5배 속도**에 요금은 2.5배가 붙는 구조입니다. 실전에서는 아래처럼 한 번에 맡기는 패턴이 잘 먹힙니다.

```
# 예: Codex CLI에서 멀티 파일 리팩토링 맡기기 (터미널 실행 예시)
codex run --model gpt-5.5 \
  "auth 모듈을 JWT 기반으로 재설계하고, 영향받는 테스트까지 한 번에 갱신해줘. 중간 확인 없이 끝까지 진행하고 끝나면 변경 요약을 출력해."
```

위 예시는 OpenAI가 공식 발표에서 강조한 "메시(messy)·멀티파트 과제를 끝까지 들고 가는" 사용 패턴을 그대로 옮긴 것입니다(실제 Codex CLI 플래그 명칭은 플랜·버전에 따라 다를 수 있으니 `codex --help`로 재확인하세요).

### ③API는 "곧" 열립니다

오늘(2026-04-24) 기준 API는 아직 정식 오픈 전이고 "very soon"으로만 안내된 상태입니다.

공개되면 Responses·Chat Completions API에서 다음 가격 구조로 서빙될 예정입니다.

| 항목 | 가격(1M 토큰 기준) |
| --- | --- |
| gpt-5.5 입력 | $5 |
| gpt-5.5 출력 | $30 |
| gpt-5.5-pro 입력 | $30 |
| gpt-5.5-pro 출력 | $180 |
| Batch·Flex | 표준가의 **50%** |
| Priority | 표준가의 **2.5배** |

GPT-5.4보다 단가는 올랐지만, Codex에서는 **같은 결과를 더 적은 토큰**으로 내도록 튜닝돼 있어서 실제 청구액은 예상보다 덜 오를 수 있다는 점이 OpenAI의 공식 입장입니다.

## 어떤 플랜·모드를 골라야 할까요 — 패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| ChatGPT + GPT-5.5 Thinking | 일반 지식 노동·리서치·플러그인 작업에 가장 무난 | Plus 이상 플랜 필요, 초고난도 문제는 Pro 대비 약함 |
| ChatGPT + GPT-5.5 Pro | 법률·금융·데이터 사이언스 등 고정확성 요구 작업에 강함 | Pro·Business·Enterprise 한정, 응답 대기 길어질 수 있음 |
| Codex + GPT-5.5 | 400K 컨텍스트로 리팩토링·디버깅·문서 생성까지 한 번에 | Fast mode는 속도 1.5배지만 비용 2.5배, 사전에 스코프 명확히 |
| Trusted Access for Cyber | 검증된 방어 업무에서 과한 거절 없이 공격·방어 시나리오 돌릴 수 있음 | chatgpt.com/cyber 신청·심사 필요, 민감 요청은 더 엄격한 분류기 적용 |
| API gpt-5.5 / gpt-5.5-pro | 프로덕션 에이전트 서빙, Batch·Flex로 단가 절반 가능 | 2026-04-24 기준 미출시("곧"), 출시 후 안전 요구사항 확인 필요 |

## 마치며

GPT-5.5의 진짜 메시지는 "더 똑똑한 모델"이 아니라 "사람 손을 덜 타고도 끝까지 일하는 모델"이라는 포지셔닝입니다. 벤치 숫자보다 토큰 효율과 지속력(persistence)이 핵심이라는 점을 기억하면 실무 선택이 쉬워집니다.

API는 아직 오픈 전이니, 일단은 ChatGPT와 Codex에서 과제를 던져보며 체감 차이를 확인해 보시길 추천드립니다.

## 참고자료

- [Introducing GPT-5.5 | OpenAI 공식 발표](https://openai.com/index/introducing-gpt-5-5/)
- [OpenAI releases GPT-5.5, bringing company one step closer to an AI 'super app' | TechCrunch, 2026-04-23](https://techcrunch.com/2026/04/23/openai-chatgpt-gpt-5-5-ai-model-superapp/)
- [OpenAI's GPT-5.5 is here, and it's no potato: narrowly beats Anthropic's Claude on Terminal-Bench 2.0 | VentureBeat](https://venturebeat.com/technology/openais-gpt-5-5-is-here-and-its-no-potato-narrowly-beats-anthropics-claude-mythos-preview-on-terminal-bench-2-0)
- [OpenAI launches GPT-5.5 just weeks after GPT-5.4 as AI race accelerates | Fortune, 2026-04-23](https://fortune.com/2026/04/23/openai-releases-gpt-5-5/)
- [OpenAI unveils GPT-5.5, claims a "new class of intelligence" at double the API price | The Decoder](https://the-decoder.com/openai-unveils-gpt-5-5-claims-a-new-class-of-intelligence-at-double-the-api-price/)
- [Trusted Access for Cyber 신청 페이지](https://chatgpt.com/cyber)
