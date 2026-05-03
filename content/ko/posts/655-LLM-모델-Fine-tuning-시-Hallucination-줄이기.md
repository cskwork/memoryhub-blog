---
title: "LLM 모델 Fine-tuning 시 Hallucination 줄이기 - ?"
date: 2025-06-05T22:41:31+09:00
slug: "655-LLM-모델-Fine-tuning-시-Hallucination-줄이기"
original_url: "https://memoryhub.tistory.com/655"
tistory_id: 655
draft: false
categories: ["데브 라이브러리"]
tags: ["Fine-Tuning"]
---

AI 모델을 학습시키다 보면 이상한 경험을 하신 적 있으신가요? 분명 학습 데이터에 없는 내용인데 모델이 그럴듯하게 지어내서 답하는 경우 말이죠. 마치 시험 문제를 모르는 학생이 아는 척하며 답을 지어내는 것처럼요! ?

이런 현상을 우리는 **Hallucination(환각)**이라고 부릅니다. 최근 연구에 따르면 공개된 LLM들의 hallucination 발생률은 약 3~16%에 달한다고 합니다. 특히 작은 모델을 fine-tuning할 때 이 문제가 더 심각해질 수 있어요.

## 등장 배경

### 과거의 접근 방식 vs 현재의 도전 과제

**과거 (Pre-LLM 시대)**

- 규칙 기반 시스템: 정해진 패턴만 출력
- 단순 분류 모델: Yes/No 같은 제한된 답변만 생성
- Hallucination? 애초에 창의적인 답변 자체가 불가능했죠!

**현재 (LLM 시대)**

- 생성형 AI: 자유로운 텍스트 생성 가능
- Fine-tuning 대중화: 누구나 쉽게 모델 커스터마이징
- 문제 발생: 모델이 "창의적으로" 거짓 정보를 생성! ?

Fine-tuning이 해결하려는 문제들:

1. **새로운 지식 주입의 딜레마**: 모델이 모르는 정보를 가르치면 환각이 증가
2. **데이터 품질 문제**: 학습 데이터의 질이 낮으면 환각 빈도 상승
3. **일반화 능력 저하**: 특정 도메인에 과적합되면서 다른 영역에서 환각 발생

## 핵심 원리

### Hallucination이 발생하는 메커니즘 이해하기 ?

```
┌─────────────────────┐
│   Pre-trained Model │
│   (기존 지식)       │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐     ┌──────────────────┐
│  Fine-tuning Data   │────▶│  Known Examples  │ ✅ 빠르게 학습
│  (학습 데이터)      │     │  (익숙한 데이터)  │
│                     │     └──────────────────┘
│                     │     
│                     │     ┌──────────────────┐
│                     │────▶│ Unknown Examples │ ⚠️ 느리게 학습
│                     │     │ (낯선 데이터)    │ → Hallucination 증가!
└─────────────────────┘     └──────────────────┘
```

### 주요 Hallucination 감소 기법들

| 기법 | 설명 | 효과 | 난이도 |
| --- | --- | --- | --- |
| **Conservative Supervision** | "모르겠습니다" 답변 학습 | 높음 | 쉬움 |
| **DPO (Direct Preference Optimization)** | 선호도 기반 직접 최적화 | 높음 | 중간 |
| **RLHF/RLAIF** | 강화학습 기반 피드백 활용 | 매우 높음 | 어려움 |
| **TruthX (Layer Selection)** | 환각 관련 레이어만 선택적 학습 | 높음 | 중간 |
| **RAG Integration** | 외부 지식 검색 결합 | 매우 높음 | 중간 |

### 실전 구현 전략 ?️

**1. 데이터 전처리 단계**

```
# 데이터를 Known/Unknown으로 분류하는 예시
def classify_data(examples, base_model):
    known_examples = []
    unknown_examples = []

    for example in examples:
        # 모델의 confidence score 계산
        confidence = base_model.get_confidence(example)

        if confidence > 0.8:
            known_examples.append(example)
        else:
            # Unknown 데이터는 "I don't know" 레이블로 변경
            example['answer'] = "죄송합니다. 그 정보는 확실하지 않습니다."
            unknown_examples.append(example)

    return known_examples, unknown_examples
```

**2. Fine-tuning 최적화**

- **학습률 조정**: Unknown 데이터는 더 낮은 학습률 사용
- **가중치 할당**: Known 데이터에 더 높은 가중치 부여
- **조기 종료**: Unknown 데이터가 과하게 학습되기 전 중단

**3. 프롬프트 엔지니어링**

```
시스템 프롬프트 예시:
"질문에 대한 답을 모르거나 확실하지 않은 경우, 
절대 추측하지 말고 '확실하지 않습니다'라고 답하세요."
```

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **새로운 지식 주입의 함정**
   - 문제: 모델이 모르는 정보를 억지로 학습시키면 환각 증가
   - 해결: RAG 같은 검색 기반 방법 활용하거나, "모르겠다"고 답하도록 학습
2. **과적합의 위험**
   - 문제: 특정 도메인 데이터만 과도하게 학습
   - 해결: 다양한 도메인의 균형잡힌 데이터셋 구성
3. **평가 지표의 한계**
   - 문제: 정확도만 보면 환각 문제를 놓칠 수 있음
   - 해결: FActScore, TruthfulQA 같은 환각 전용 평가 지표 활용

? **실전 꿀팁**

- 작은 모델일수록 Conservative Supervision이 효과적!
- DPO는 RLHF보다 구현이 간단하면서도 효과는 비슷
- Fine-tuning 전에 꼭 베이스 모델의 지식 범위를 파악하세요
- 도메인별로 다른 전략이 필요 - 의료/법률은 특히 신중하게!

## 마치며

지금까지 모델의 fine-tuning 시 hallucination을 줄이는 방법에 대해 알아보았습니다. 처음에는 복잡해 보일 수 있지만, 핵심은 "모델이 모르는 것을 억지로 가르치지 말자"는 것입니다!

여러분의 AI 모델이 더 이상 환상을 보지 않고, 신뢰할 수 있는 답변을 제공하길 바랍니다. 혹시 이 글을 읽고 실제로 적용해보셨다면, 어떤 효과가 있었는지 공유해주시면 좋겠네요! ?

어떤 기법부터 시작하시겠어요? Conservative Supervision으로 가볍게 시작해보는 건 어떨까요?

## 참고 자료 ?

- [Extrinsic Hallucinations in LLMs - Lil'Log](https://lilianweng.github.io/posts/2024-07-07-hallucination/)
- [Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations? - arXiv](https://arxiv.org/abs/2405.05904)
- [Unfamiliar Finetuning Examples Control How Language Models Hallucinate](https://arxiv.org/abs/2403.05612)
- [Key Strategies to Minimize LLM Hallucinations - Turing](https://www.turing.com/resources/minimize-llm-hallucinations-strategy)
- [3 Recommended Strategies to Reduce LLM Hallucinations - Vellum](https://www.vellum.ai/blog/how-to-reduce-llm-hallucinations)

---

#LLM #FineTuning #Hallucination #AI #MachineLearning #딥러닝
