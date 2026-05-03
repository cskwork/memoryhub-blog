---
title: "? Syntriever, GPT-4 출력만으로 검색 모델 18.6% 향상시킨 방법"
date: 2025-12-29T21:43:56+09:00
slug: "952-Syntriever-GPT-4-출력만으로-검색-모델-18-6-향상시킨-방법"
original_url: "https://memoryhub.tistory.com/952"
tistory_id: 952
draft: false
categories: ["데브 컨셉"]
tags: ["Tech News"]
---

```
    ╔═══════════════════════════════════════════════╗
    ║                                               ║
    ║   ┌─────────────┐         ┌─────────────┐    ║
    ║   │   Query     │         │    LLM      │    ║
    ║   │  "What is"  │ ──────> │  (GPT-4)    │    ║
    ║   └─────────────┘         └──────┬──────┘    ║
    ║                                  │           ║
    ║         ┌────────────────────────┴───┐       ║
    ║         ▼                            ▼       ║
    ║   ┌───────────┐              ┌───────────┐   ║
    ║   │ Synthetic │              │  Verify   │   ║
    ║   │ Passages  │   ──────>    │  Quality  │   ║
    ║   └───────────┘              └─────┬─────┘   ║
    ║                                    │         ║
    ║                           ┌────────┴────────┐║
    ║                           ▼                 ▼║
    ║                    ┌──────────┐     ┌────────┐
    ║                    │ Positive │     │Negative│
    ║                    │ Passage  │     │Passage │
    ║                    └────┬─────┘     └────┬───┘
    ║                         │                │   ║
    ║                         └───────┬────────┘   ║
    ║                                 ▼            ║
    ║                        ┌─────────────┐       ║
    ║                        │  Retriever  │       ║
    ║                        │  Training   │       ║
    ║                        └─────────────┘       ║
    ║                                               ║
    ║            S Y N T R I E V E R               ║
    ╚═══════════════════════════════════════════════╝
```

RAG 시스템을 구축할 때 가장 어려운 부분은 무엇일까요. LLM이 아니라 Retriever입니다. 아무리 똑똑한 LLM을 사용해도, 검색 단계에서 엉뚱한 문서를 가져오면 답변 품질은 곤두박질칩니다. 그런데 검색 모델을 LLM 지식으로 훈련하려면 보통 모델 내부 확률값에 접근해야 합니다. GPT-4나 Claude 같은 폐쇄형 API로는 불가능한 일이죠.

**Syntriever는 LLM의 텍스트 출력만으로 검색 모델을 훈련하는 방법을 제시합니다.**

**한줄요약:** 결론부터 말하면, Syntriever는 Black-box LLM이 생성한 합성 데이터로 Retriever를 훈련하여 기존 대비 최대 18.6% 성능 향상을 달성한 2단계 프레임워크다.

## 배경

검색 증강 생성(RAG)은 LLM의 한계를 극복하는 핵심 기술입니다. LLM은 훈련 시점 이후의 정보를 모르고, 환각 현상도 일으킵니다. RAG는 외부 문서를 검색해 LLM에 전달함으로써 이 문제를 해결합니다.

> RAG = Retriever(검색) + Generator(생성). 검색 품질이 최종 답변 품질을 결정한다.

문제는 Retriever 성능입니다. 기존에 LLM 지식을 Retriever로 전이하는 방법들이 있었습니다. InPars는 GPT-3로 쿼리를 생성해 훈련했고, Promptagator는 소수의 예시로 도메인 특화 쿼리를 만들었습니다. 그러나 이 방법들은 공통적인 한계가 있었습니다.

**LLM의 출력 확률(output probability)에 접근해야 한다**는 점입니다. 확률값으로 문서의 관련성을 판단해 훈련 신호로 활용하는 방식인데, GPT-4, Claude, Gemini 같은 상용 API에서는 이 확률값을 제공하지 않습니다. 이런 API를 Black-box LLM이라 부릅니다.

## Syntriever의 핵심 아이디어

Syntriever는 한국 연구진(김민상, 백승준)이 제안한 프레임워크로, NAACL 2025 Findings에 게재되었습니다. 핵심 발상은 단순합니다.

**확률값 대신 LLM이 생성한 텍스트 자체를 훈련 데이터로 쓴다.**

2단계로 구성됩니다.

**1단계 Distillation Stage(증류 단계)**는 LLM에게 쿼리를 주고 관련 문서와 비관련 문서를 생성하게 합니다. 마치 선생님이 학생에게 "이 질문에 대한 좋은 답과 나쁜 답을 만들어봐"라고 시키는 것과 같습니다.

여기서 중요한 장치가 자기 검증(self-verification)입니다. LLM이 생성한 문서 중 사실과 다른 환각 내용이 있으면, 그 문서를 긍정 예시가 아닌 부정 예시(hard-negative)로 재분류합니다. 틀린 답을 만들었다면 그걸 오답 예시로 활용하는 셈입니다.

**2단계 Alignment Stage(정렬 단계)**는 Retriever가 검색한 결과를 LLM에게 다시 평가받습니다. LLM이 "이 문서가 저 문서보다 낫다"고 판단하면, Retriever가 그 선호를 학습합니다. 이때 Partial Plackett-Luce 랭킹이라는 기법을 사용해 LLM의 부분적인 선호도만으로도 효과적으로 학습합니다.

비유하자면 1단계는 교과서 만들기, 2단계는 채점과 피드백입니다.

## 기술적 구현

Syntriever의 1단계에서는 Chain-of-Thought 프롬프팅을 활용합니다. LLM에게 단순히 "관련 문서를 만들어라"가 아니라, 왜 이 문서가 관련 있는지 추론 과정을 함께 생성하게 합니다. 이렇게 하면 더 논리적으로 연결된 합성 데이터가 만들어집니다.

훈련 손실함수는 Soft Nearest-Neighbor(SNN) loss를 변형해 사용합니다. 관련 문서들의 임베딩은 가깝게, 비관련 문서는 멀리 배치하도록 학습합니다. 여러 개의 긍정 예시를 동시에 클러스터링할 수 있어 단일 긍정 예시만 쓰는 대조 학습보다 효과적입니다.

2단계의 Partial Plackett-Luce 모델은 완전한 순위가 아닌 부분 순위만으로 학습합니다. LLM이 상위 k개 문서 중 일부에 대해서만 비교 판단을 내려도 충분합니다. 여기에 정규화(regularization)를 추가해 1단계에서 학습한 내용을 잊지 않도록 합니다.

## 성능 검증

BeIR 벤치마크에서 테스트한 결과입니다.

| 데이터셋 | 기존 최고 성능 대비 향상 | 주요 특징 |
| --- | --- | --- |
| MSMARCO | +18.6% (nDCG@10) | 대규모 웹 검색 |
| HotpotQA | 상위 성능 | 다중 홉 추론 필요 |
| SciFact | 상위 성능 | 과학 논문 검증 |
| FiQA | 상위 성능 | 금융 도메인 특화 |

E5 같은 기존 Retriever를 베이스로 사용하고, GPT 계열 LLM으로 합성 데이터를 생성했습니다. 도메인에 관계없이 일관된 성능 향상을 보였습니다.

연구진은 OpenAI의 Batch API를 활용한 대규모 합성 데이터 생성을 권장합니다. 코드는 GitHub에 공개되어 있어 MSMARCO, HotpotQA, FiQA, SciFact, NFCorpus 데이터셋으로 재현 가능합니다.

## 실습

Syntriever를 직접 사용하는 과정입니다.

**1. 환경 준비**

BeIR 데이터셋을 먼저 다운로드합니다. Syntriever 저장소를 클론하고 의존성을 설치합니다.

```
git clone https://github.com/kmswin1/Syntriever
cd Syntriever
pip install -e .
```

**2. 합성 데이터 생성**

datasets 폴더에서 parse\_synthetic.py를 실행합니다. 이 스크립트가 LLM API를 호출해 합성 문서를 생성합니다. 대규모 생성 시 OpenAI Batch API 사용을 권장합니다.

```
cd datasets
python parse_synthetic.py msmarco
```

**3. 1단계 훈련(Distillation)**

생성된 합성 데이터로 Retriever를 훈련합니다. e5는 베이스 모델을 의미합니다.

```
python train_stage1.py e5 msmarco
```

**4. 검색 및 2단계 준비**

훈련된 모델로 검색을 수행하고, 결과에 대한 LLM 비교 데이터를 생성합니다.

```
python retrieval.py e5-sft msmarco
cd stage2
python parse_comparison.py msmarco
```

**5. 2단계 훈련(Alignment)**

LLM 선호도 정렬을 수행합니다.

```
python train_stage2.py e5-sft msmarco
```

**6. 최종 평가**

BeIR 벤치마크로 성능을 측정합니다.

```
python evaluate.py e5-final msmarco
```

## 모범사례/패턴 비교

| 방법 | 장점 | 주의점 |
| --- | --- | --- |
| Syntriever | Black-box LLM 호환, 환각 자동 처리 | LLM API 호출 비용 발생 |
| InPars | 간단한 쿼리 생성 | 확률값 필요, 부정 예시 약함 |
| Promptagator | 소수 예시로 도메인 특화 | 대규모 LLM 필요, 확률값 필요 |
| 직접 라벨링 | 품질 보장 | 비용과 시간 과다 |

Syntriever는 비용 측면에서 LLM API 호출이 필요하지만, 연구진은 API 가격이 지속적으로 하락하고 있어 실용성이 높다고 평가합니다. 실제로 더 작은 LLM으로도 효과적인 합성 데이터 생성이 가능하다는 후속 연구들이 나오고 있습니다.

## 마치며

- Syntriever는 GPT-4 같은 Black-box LLM의 텍스트 출력만으로 Retriever를 훈련하는 최초의 프레임워크다.
- 2단계 구조(증류 + 정렬)와 자기 검증 메커니즘이 핵심이며, BeIR에서 최대 18.6% 성능 향상을 달성했다.
- 실전 팁: RAG 시스템의 검색 품질이 불만족스럽다면, Syntriever 방식으로 도메인 특화 Retriever를 만들어 보세요.

## 참고자료

- Syntriever: How to Train Your Retriever with Synthetic Data from LLMs (<https://arxiv.org/abs/2502.03824>)
- Syntriever GitHub Repository (<https://github.com/kmswin1/Syntriever>)
- ACL Anthology - NAACL 2025 Findings (<https://aclanthology.org/2025.findings-naacl.136/>)
