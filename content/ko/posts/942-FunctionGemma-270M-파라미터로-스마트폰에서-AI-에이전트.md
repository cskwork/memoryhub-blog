---
title: "? FunctionGemma, 270M 파라미터로 스마트폰에서 AI 에이전트"
date: 2025-12-21T18:33:39+09:00
slug: "942-FunctionGemma-270M-파라미터로-스마트폰에서-AI-에이전트"
original_url: "https://memoryhub.tistory.com/942"
tistory_id: 942
draft: false
categories: ["데브 컨셉"]
tags: ["Tech News"]
---

```
  ╔═══════════════════════════════════════════════════════╗
  ║                                                       ║
  ║      ?  F u n c t i o n G e m m a                    ║
  ║                                                       ║
  ║      "Turn on the light"                              ║
  ║             │                                         ║
  ║             ▼                                         ║
  ║      ┌─────────────┐                                  ║
  ║      │  270M LLM   │  ◄── On-Device (0.5GB)          ║
  ║      └─────────────┘                                  ║
  ║             │                                         ║
  ║             ▼                                         ║
  ║      { "function": "toggle_light",                    ║
  ║        "params": { "state": "on" } }                  ║
  ║                                                       ║
  ║      Natural Language  ──►  API Execution             ║
  ║                                                       ║
  ╚═══════════════════════════════════════════════════════╝
```

"AI 에이전트를 만들려면 GPT-4 API를 호출해야 한다"고 생각하는가? 구글이 2024년 12월 18일 발표한 FunctionGemma는 이 상식을 뒤집는다. 270M(2억 7천만) 파라미터의 초경량 모델이 스마트폰에서 오프라인으로 동작하며, 자연어를 실행 가능한 API 호출로 변환한다. **챗봇 시대가 끝나고 에이전트 시대가 시작됐다면, FunctionGemma는 그 에이전트를 주머니 속에 넣어준 첫 번째 모델이다.**

**한줄요약:** 결론부터 말하면, FunctionGemma는 자연어를 API 호출로 변환하는 데 특화된 초경량 에지 AI 모델로, 파인튜닝 시 85% 정확도를 달성하며 스마트폰에서 완전한 오프라인 에이전트 구현을 가능하게 한다.

---

## 배경

AI가 "말만 하는 챗봇"에서 "실제로 행동하는 에이전트"로 진화하고 있다. 알람을 설정하고, 연락처를 추가하고, 조명을 끄는 일까지 자연어 한 문장으로 처리하려면 모델이 단순히 텍스트를 생성하는 것을 넘어 **구조화된 함수 호출**을 출력해야 한다.

문제는 기존 대형 모델들이 클라우드 의존적이라는 점이다. 네트워크 지연, 개인정보 유출 우려, 배터리 소모까지. 구글이 Gemma 3 270M을 출시한 이후 개발자들이 가장 많이 요청한 기능이 바로 "네이티브 Function Calling"이었던 이유다.

> 한 줄 정의: FunctionGemma는 자연어 명령을 JSON 형태의 함수 호출로 변환하도록 특화 훈련된 Gemma 3 270M 기반 경량 언어 모델이다.

FunctionGemma가 기존 접근법과 다른 점은 **설계 철학** 자체다. 범용 대화 모델이 아니라, 처음부터 특정 작업에 파인튜닝되는 것을 전제로 만들어졌다. 구글은 이를 "맞춤형 에이전트의 출발점"이라고 표현한다.

---

## 핵심 특징

FunctionGemma의 기술적 차별점은 다음과 같다.

**첫째, 통합된 행동과 대화 능력이다.** 이 모델은 컴퓨터와 인간 양쪽과 소통할 줄 안다. 함수 호출을 생성해 도구를 실행한 뒤, 그 결과를 자연어로 요약해 사용자에게 전달하는 컨텍스트 전환이 가능하다.

**둘째, 극단적인 경량화다.** 270M 파라미터는 FP16 기준 약 0.5GB, Q8\_0 양자화 시 약 300MB의 메모리만 차지한다. NVIDIA Jetson Nano, Samsung S25 Ultra 같은 에지 디바이스에서 구동되며, Pixel 8과 iPhone 15 Pro에서 약 50 tokens/s의 추론 속도를 기록한다.

**셋째, 파인튜닝을 통한 정확도 도약이다.** 구글의 "Mobile Actions" 평가에서 기본 모델은 58%의 정확도를 보였지만, 작업 특화 파인튜닝 후 85%까지 상승했다. 27%p의 개선은 프롬프트 엔지니어링만으로는 불가능한 수치다.

| 항목 | 사양 |
| --- | --- |
| 파라미터 | 270M (2억 7천만) |
| 컨텍스트 윈도우 | 32K 토큰 |
| 메모리 (FP16) | 약 0.5GB |
| 메모리 (Q8\_0 양자화) | 약 300MB |
| 지식 컷오프 | 2024년 8월 |
| 학습 토큰 | 6조 개 |

---

## 어떤 상황에서 사용해야 하나

FunctionGemma는 모든 상황에 적합한 범용 모델이 아니다. 다음 조건에 해당할 때 최적의 선택이 된다.

**정의된 API 표면이 있을 때.** 스마트홈 제어, 미디어 재생, 내비게이션처럼 실행 가능한 액션 세트가 명확한 애플리케이션에 적합하다.

**파인튜닝할 준비가 됐을 때.** 제로샷 프롬프팅의 변동성 대신, 특정 데이터로 훈련해 결정적이고 일관된 동작이 필요한 경우다.

**로컬 우선 배포가 목표일 때.** 즉각적인 지연시간, 완전한 데이터 프라이버시, 에지 디바이스의 컴퓨팅 및 배터리 제약 내에서 효율적 동작이 요구되는 경우다.

**복합 시스템을 구축할 때.** 일반적인 명령은 에지에서 FunctionGemma가 처리하고, 복잡한 작업만 Gemma 3 27B 같은 대형 모델로 라우팅하는 "지능형 트래픽 컨트롤러" 역할이 필요할 때다.

---

## 실습: Mobile Actions 파인튜닝

구글이 제공하는 Mobile Actions 데이터셋과 Colab 노트북을 활용해 FunctionGemma를 직접 파인튜닝할 수 있다.

① **환경 준비**  
Hugging Face 계정에서 FunctionGemma 모델 라이선스에 동의하고, 액세스 토큰을 발급받는다. Colab에서 `HF_TOKEN` 환경 변수로 등록한다.

② **모델 및 데이터셋 로드**  
Hugging Face Transformers 라이브러리로 모델을 불러온다. Mobile Actions 데이터셋은 사용자 프롬프트와 예상 함수 호출 쌍으로 구성되어 있다.

```
# Python 3.10+ / transformers 4.40+
from transformers import AutoProcessor, AutoModelForCausalLM

processor = AutoProcessor.from_pretrained(
    "google/functiongemma-270m-it", 
    device_map="auto"
)
model = AutoModelForCausalLM.from_pretrained(
    "google/functiongemma-270m-it", 
    dtype="auto", 
    device_map="auto"
)
```

③ **파인튜닝 실행**  
Hugging Face TRL 라이브러리의 SFTTrainer를 사용해 지도 학습 파인튜닝을 수행한다. 출력 디렉토리에 체크포인트가 저장된다.

④ **모델 배포**  
파인튜닝된 모델을 Hugging Face Hub에 업로드하거나, LiteRT-LM을 통해 모바일 디바이스에 직접 배포한다. Google AI Edge Gallery 앱에서 테스트할 수 있다.

---

## 생태계 및 배포 옵션 비교

| 도구/플랫폼 | 용도 | 특징 |
| --- | --- | --- |
| Hugging Face Transformers | 파인튜닝 | 표준 워크플로우, 풍부한 문서화 |
| Unsloth | 파인튜닝 | LoRA 지원, 메모리 효율 최적화 |
| NVIDIA NeMo | 파인튜닝 | 엔터프라이즈급, DGX Spark 지원 |
| LiteRT-LM | 모바일 배포 | 구글 공식, Edge Gallery 연동 |
| Ollama | 로컬 실행 | 간단한 CLI 인터페이스 |
| Llama.cpp | 범용 추론 | GGUF 양자화 지원, CPU 최적화 |
| Transformers.js | 웹 배포 | 브라우저 내 100% 로컬 실행 |

---

## 마치며

- FunctionGemma는 자연어를 API 호출로 변환하는 초경량(270M) 에지 AI 모델로, 클라우드 없이 스마트폰에서 완전한 오프라인 에이전트를 구현한다.
- 파인튜닝을 통해 58%에서 85%로 정확도가 도약하며, 이는 작업 특화 훈련이 소형 모델에서 필수임을 증명한다.
- 실전 팁: 오늘 당장 Google AI Edge Gallery 앱을 설치해 TinyGarden 게임이나 Mobile Actions 데모를 체험해보세요.

---

## 참고자료

- FunctionGemma 공식 발표 (<https://blog.google/technology/developers/functiongemma/>)
- FunctionGemma 모델 개요 - Google AI (<https://ai.google.dev/gemma/docs/functiongemma>)
- Hugging Face 모델 페이지 (<https://huggingface.co/google/functiongemma-270m-it>)
- Mobile Actions 파인튜닝 가이드 (<https://ai.google.dev/gemma/docs/mobile-actions>)
- Unsloth 파인튜닝 문서 (<https://docs.unsloth.ai/models/functiongemma>)
- Google AI Edge Gallery 앱 (<https://play.google.com/store/apps/details?id=com.google.ai.edge.gallery>)
