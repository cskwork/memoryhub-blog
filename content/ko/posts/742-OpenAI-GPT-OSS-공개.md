---
title: "OpenAI, GPT-OSS 공개"
date: 2025-08-06T05:00:46+09:00
slug: "742-OpenAI-GPT-OSS-공개"
original_url: "https://memoryhub.tistory.com/742"
tistory_id: 742
draft: false
categories: ["데브 컨셉"]
tags: ["Tech News"]
---

120b·20b 두 모델로 살펴보는 오픈-웨이트 언어모델의 새로운 기준  
*2025 년 8 월 5 일 발표* ([OpenAI](https://openai.com/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

---

## 1. GPT-OSS란?

OpenAI가 **gpt-oss-120b**와 **gpt-oss-20b** 두 가지 모델을 아파치 2.0 라이선스로 공개했습니다. 두 모델은 크기 대비 뛰어난 추론 성능을 제공하며, 개인용 하드웨어에서도 저렴한 비용으로 실행할 수 있도록 최적화되었습니다. ([OpenAI](https://openai.com/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

- **gpt-oss-120b**: 80 GB GPU 한 장으로 동작, OpenAI **o4-mini**급 추론 성능
- **gpt-oss-20b**: 16 GB 메모리만으로 실행, **o3-mini**와 유사한 벤치마크 결과
- 두 모델 모두 툴 호출·체인-오브-생각(CoT)·함수호출 few-shot 등 고급 기능을 기본 지원 ([OpenAI](https://openai.com/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))

## 2. 모델 아키텍처 한눈에 보기

| 모델 | 총 파라미터 | 활성 파라미터/토큰 | 레이어 수 | 전문가(Expert)/레이어 | 컨텍스트 길이 |  |
| --- | --- | --- | --- | --- | --- | --- |
| gpt-oss-120b | 117 B | 5.1 B | 36 | 128 중 4 활성 | 128 k |  |
| gpt-oss-20b | 21 B | 3.6 B | 24 | 32 중 4 활성 | 128 k |  |

MoE(혼합 전문가) 구조 덕분에 **필요한 파라미터만 활성화**하여 메모리를 크게 절감했고, RoPE 포지셔널 임베딩으로 **128 k** 토큰의 긴 문맥을 처리합니다.

## 3. 학습·후처리(포스트트레이닝)

- **사전학습**: STEM·코딩·일반 지식을 중심으로 대용량 텍스트 데이터 학습
- **후처리**: Supervised fine-tuning + 고연산 RL 단계 → OpenAI Model Spec을 충실히 따르도록 조정
- **세 가지 Reasoning Effort**(low·medium·high) 설정으로 **속도–성능 트레이드오프** 선택 가능

## 4. 성능 벤치마크

- **120b**: Codeforces·MMLU·TauBench 등에서 **o4-mini**와 동급, 보건(HealthBench)·경시수학(AIME 2024/25)에서는 앞섬
- **20b**: 소형임에도 **o3-mini** 수준을 달성하고 일부 과제에서 초과 달성

> ※ 의료 조언 등 전문 영역에서는 여전히 전문가 검증이 필요함.

## 5. 안전성과 오픈 모델의 도전

OpenAI는 **악의적 파인튜닝** 시나리오를 직접 만들어 Preparedness Framework로 검증했고, 외부 전문가 리뷰까지 거쳤습니다. 또한 50만 달러 규모의 **레드팀 챌린지**를 개최해 잠재적 위험을 공개적으로 탐색합니다.

## 6. 어디서, 어떻게 써볼까?

- **허깅페이스**: 즉시 다운로드 가능(기본 MXFP4 4-bit 양자화)
- **플랫폼 파트너**: Azure, Hugging Face, vLLM, Ollama, llama.cpp, LM Studio, AWS, Together AI 등에서 즉시 배포
- **윈도우 개발자**: ONNX Runtime 기반 로컬 추론 모델을 VS Code AI Toolkit에서 지원 예정

## 7. 왜 오픈-웨이트 모델이 중요한가?

- **접근성 향상**: 예산·인프라가 제한된 조직도 고성능 LLM을 자체 인프라에 배치 가능
- **투명성과 연구 가속**: 모델 가중치·토크나이저·하모니 프롬프트 렌더러까지 공개 → 재현성 확보
- **글로벌 혁신 촉진**: 지역·규모를 불문하고 누구나 맞춤형 AI 서비스 개발 가능

## 8. 마무리 & 시사점

GPT-OSS는 “GPT-2 이후 6 년 만의 오픈-웨이트 LLM”이라는 상징성과 함께,

**1)실용적 성능**, 2) **낮은 실행 비용**, 3) **강화된 안전 프로세스**라는 세 축을 모두 잡았습니다.

개발자라면 지금 바로 모델을 내려받아 **로컬 테스트**부터 **커스텀 파인튜닝**까지 시도해 보세요.  
오픈 모델 생태계와 프로프라이어터리 API가 **상호 보완**되는 미래가 눈앞에 다가왔습니다. ? ([OpenAI](https://openai.com/index/introducing-gpt-oss/ "Introducing gpt-oss | OpenAI"))
