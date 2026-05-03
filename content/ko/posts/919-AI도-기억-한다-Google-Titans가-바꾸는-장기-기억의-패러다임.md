---
title: "? AI도 '기억'한다, Google Titans가 바꾸는 장기 기억의 패러다임"
date: 2025-12-06T14:51:17+09:00
slug: "919-AI도-기억-한다-Google-Titans가-바꾸는-장기-기억의-패러다임"
original_url: "https://memoryhub.tistory.com/919"
tistory_id: 919
draft: false
---

```
  ╔══════════════════════════════════════════════════════════════╗
  ║                                                              ║
  ║     ┌─────────────────────────────────────────────────┐      ║
  ║     │  SHORT-TERM        LONG-TERM        PERSISTENT  │      ║
  ║     │  ┌───────┐        ┌───────┐        ┌───────┐   │      ║
  ║     │  │ATTEN- │   +    │NEURAL │   +    │FIXED  │   │      ║
  ║     │  │ TION  │        │MEMORY │        │WEIGHTS│   │      ║
  ║     │  └───┬───┘        └───┬───┘        └───────┘   │      ║
  ║     │      │                │                        │      ║
  ║     │      └───────┬────────┘                        │      ║
  ║     │              ▼                                 │      ║
  ║     │        ╔═══════════╗                           │      ║
  ║     │        ║  TITANS   ║  ← Surprise Metric        │      ║
  ║     │        ║   +       ║  ← 2M+ Tokens             │      ║
  ║     │        ║  MIRAS    ║  ← Real-time Learning     │      ║
  ║     │        ╚═══════════╝                           │      ║
  ║     └─────────────────────────────────────────────────┘      ║
  ║                                                              ║
  ║              AI  LONG-TERM  MEMORY  ARCHITECTURE             ║
  ╚══════════════════════════════════════════════════════════════╝
```

# 

Transformer가 처리할 수 있는 문맥의 한계, 한 번쯤 답답했던 적 있지 않은가. 긴 문서를 요약하다가 앞부분을 까먹는 AI, 대화가 길어지면 초반 맥락을 놓치는 챗봇. 이 모든 문제의 근원은 AI에게 **진정한 장기 기억이 없었기 때문**이다. Google

Research가 2024년 말 발표하고 2025년 12월 NeurIPS에서 공식 소개한 Titans와 MIRAS는 바로 이 문제를 정면으로 해결한다. **RNN의 속도와 Transformer의 정확성을 결합하면서, 200만 토큰 이상의 초장문 맥락을 처리할 수 있는 아키텍처**가 등장한 것이다.

**한줄요약:** 결론부터 말하면, Titans는 AI가 '놀라운 정보'만 선택적으로 기억하는 뇌과학 원리를 적용해, 기존 Transformer의 컨텍스트 한계를 극복한 차세대 아키텍처다.

## 배경

현재 대부분의 LLM은 Transformer 아키텍처를 사용한다. 2017년 Google이 발표한 "Attention is All You Need" 논문 이후, Attention 메커니즘은 AI 혁명의 핵심 기술이 되었다. 하지만 치명적인 약점이 있다. 시퀀스 길이에 대해 **O(n²)의 연산 복잡도**를 가진다는 것이다.

무슨 뜻일까. 입력 토큰이 2배가 되면 연산량은 4배, 10배가 되면 100배로 늘어난다. 그래서 대부분의 LLM은 컨텍스트 윈도우에 제한이 있고, 긴 문서나 책 전체를 한 번에 처리하기 어렵다. Mamba 같은 State Space Model이나 최신 RNN 계열 모델들이 이 문제를 해결하려 시도했지만, 고정 크기 벡터에 정보를 압축하다 보니 **중요한 세부 정보가 손실**되는 한계가 있었다.

| 아키텍처 | 장점 | 한계 |
| --- | --- | --- |
| Transformer | 정확한 의존성 모델링 | O(n²) 복잡도, 컨텍스트 제한 |
| RNN/SSM (Mamba) | 선형 스케일링, 빠른 추론 | 고정 크기 압축, 정보 손실 |
| Titans | 둘의 장점 결합 | 신규 아키텍처, 검증 진행 중 |

## 핵심

> 한 줄 정의: Titans는 단기 기억(Attention)과 장기 기억(Neural Memory Module)을 분리하여, 인간의 뇌처럼 '놀라운 정보'만 선택적으로 저장하는 AI 아키텍처다.

인간의 기억 시스템을 떠올려보자. 우리는 일상적인 출퇴근 경로는 금방 잊지만, 갑자기 마주친 사고 현장이나 뜻밖의 선물은 오래 기억한다. 예상을 벗어나는, 즉 **'놀라운' 정보가 장기 기억에 저장**되는 것이다. Titans는 이 원리를 그대로 AI에 적용했다.

**Surprise Metric의 작동 원리**

Titans의 핵심 혁신은 "surprise metric"이다. 모델이 현재 기억하고 있는 상태와 새로 들어온 입력 사이의 차이를 측정한다. 그 차이(gradient)가 크면 "이건 예상 밖이야, 중요해"라고 판단하고 장기 기억에 저장한다.

예를 들어, 금융 보고서를 읽다가 갑자기 "바나나 껍질" 이미지가 등장하면 surprise 값이 급등한다. 반면 금융 보고서에서 "수익", "매출" 같은 단어가 나오면 예상 범위 내이므로 surprise 값이 낮다. 이렇게 **선택적 기억을 통해 메모리 효율을 극대화**한다.

**세 가지 아키텍처 변형**

Titans는 장기 기억을 통합하는 방식에 따라 세 가지 변형을 제공한다.

첫째, **Memory as Context(MAC)**는 개인 비서가 과거 회의 노트를 속삭여주는 방식이다. 장기 기억의 요약본을 현재 처리 중인 문맥에 추가 정보로 제공한다.

둘째, **Memory as Gate(MAG)**는 두 명의 조언자가 동시에 일하는 구조다. 단기 기억과 장기 기억이 각각 처리한 결과를 게이팅 메커니즘으로 결합한다.

셋째, **Memory as Layer(MAL)**는 메모리를 네트워크 레이어 자체로 통합한다. 기존 신경망 구조에 장기 기억 레이어를 직접 삽입하는 방식이다.

**MIRAS: 통합 이론 프레임워크**

Titans가 도구라면, MIRAS는 설계도다. Google 연구진은 Transformer부터 RNN, SSM까지 모든 시퀀스 모델이 사실 **"연관 기억(Associative Memory)"이라는 하나의 문제**를 푸는 서로 다른 방법이라고 주장한다.

MIRAS는 시퀀스 모델을 네 가지 설계 선택으로 분해한다.

- **Memory architecture**: 정보를 저장하는 구조 (벡터, 행렬, 딥 뉴럴넷)
- **Attentional bias**: 모델이 최적화하는 내부 학습 목표
- **Retention gate**: 망각 메커니즘 (정규화의 일종)
- **Memory algorithm**: 메모리 업데이트에 사용하는 최적화 알고리즘

이 프레임워크를 통해 기존 MSE(Mean Squared Error) 기반 접근법의 한계를 넘어, YAAD, MONETA, MEMORA 같은 새로운 attention-free 모델들이 파생되었다.

## 성능 검증

Titans의 성능은 다양한 벤치마크에서 검증되었다. 가장 인상적인 결과는 **BABILong 벤치마크**에서 나왔다. 이 테스트는 수백만 토큰에 걸쳐 분산된 정보를 추론해야 하는 극한의 장문 컨텍스트 과제다.

| 모델 | 파라미터 수 | BABILong 성능 |
| --- | --- | --- |
| GPT-4 | 수천억 (추정) | 기준선 |
| Llama-3 + RAG | 수백억 | GPT-4 미만 |
| Titans (MAC-FT) | 7.6억 | **GPT-4 초과** |

파라미터 수가 훨씬 적음에도 불구하고 Titans가 GPT-4를 능가했다는 점이 주목할 만하다. 연구진은 Titans를 **200만 토큰 이상의 컨텍스트 윈도우**까지 확장하면서도 메모리 비용을 적정 수준으로 유지했다고 밝혔다.

언어 모델링(C4, WikiText)과 상식 추론(HellaSwag, PIQA) 태스크에서도 Titans는 Mamba-2, Gated DeltaNet, Transformer++ 등 최신 모델들을 일관되게 앞섰다. 특히 메모리 모듈의 **깊이(depth)**가 깊을수록 perplexity가 낮아지고, 시퀀스 길이가 증가해도 성능 저하가 덜하다는 ablation 연구 결과도 발표되었다.

## 활용 가능성

Titans 아키텍처가 실제로 적용될 수 있는 영역은 광범위하다.

**문서 이해와 분석** 측면에서, 수백 페이지짜리 법률 문서나 의학 논문을 한 번에 처리하고 특정 조항이나 연구 결과를 정확히 찾아낼 수 있다. 기존에는 RAG(Retrieval-Augmented Generation)로 우회했던 문제를 아키텍처 수준에서 해결한다.

**유전체 분석**에서는 DNA 시퀀스처럼 수백만 개의 염기쌍으로 이루어진 데이터를 모델링할 수 있다. 연구진은 실제로 genomic 태스크에서 Titans를 테스트하여 텍스트 이외 도메인에서도 효과를 검증했다.

**시계열 예측** 영역에서도 장기 패턴을 기억해야 하는 금융 데이터나 기상 데이터 분석에 강점을 보일 수 있다. 과거의 특이 패턴을 "놀라움"으로 기억하고, 유사한 상황에서 활용할 수 있기 때문이다.

| 적용 분야 | 기대 효과 |
| --- | --- |
| 법률/의료 문서 분석 | RAG 없이 전체 문서 처리 |
| 유전체 연구 | 수백만 염기쌍 시퀀스 모델링 |
| 장기 대화 AI | 대화 초반 맥락 완전 유지 |
| 시계열 예측 | 장기 패턴 학습 강화 |

## 마치며

- Titans는 인간 뇌의 "놀라움 기반 기억" 원리를 AI에 적용해, 200만 토큰 이상의 초장문 컨텍스트를 처리할 수 있는 새로운 아키텍처다
- MIRAS 프레임워크는 Transformer, RNN, SSM을 통합된 관점에서 바라보며, 차세대 시퀀스 모델 설계의 이론적 기반을 제공한다
- 이 연구는 "Pre-training 후 고정"되던 기존 AI 패러다임에서 "실시간 학습하며 기억하는" AI로의 전환을 예고한다

실전 팁: Google의 Gemini나 오픈소스 Gemma 모델에 이 기술이 적용될 가능성이 높으니, 장문 컨텍스트가 필요한 프로젝트를 준비 중이라면 Titans 관련 후속 연구와 모델 공개 소식을 주시하자.

## 참고자료

- Titans + MIRAS: Helping AI have long-term memory - Google Research Blog (<https://research.google/blog/titans-miras-helping-ai-have-long-term-memory/>)
- Titans: Learning to Memorize at Test Time - arXiv (<https://arxiv.org/abs/2501.00663>)
- MIRAS: A Unified Framework for Sequence Modeling - arXiv (<https://arxiv.org/pdf/2504.13173>)
- Google's Titans Architecture: Key Concepts Explained - DataCamp (<https://www.datacamp.com/blog/titans-architecture>)
