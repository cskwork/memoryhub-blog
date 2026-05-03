---
title: "? NVIDIA Nemotron 3 Nano 30B, 31억 파라미터로 300억짜리 성능낸다"
date: 2025-12-16T19:55:57+09:00
slug: "929-NVIDIA-Nemotron-3-Nano-30B-31억-파라미터로-300억짜리-성능낸다"
original_url: "https://memoryhub.tistory.com/929"
tistory_id: 929
draft: false
---

```
     ███╗   ██╗███████╗███╗   ███╗ ██████╗ ████████╗██████╗  ██████╗ ███╗   ██╗
     ████╗  ██║██╔════╝████╗ ████║██╔═══██╗╚══██╔══╝██╔══██╗██╔═══██╗████╗  ██║
     ██╔██╗ ██║█████╗  ██╔████╔██║██║   ██║   ██║   ██████╔╝██║   ██║██╔██╗ ██║
     ██║╚██╗██║██╔══╝  ██║╚██╔╝██║██║   ██║   ██║   ██╔══██╗██║   ██║██║╚██╗██║
     ██║ ╚████║███████╗██║ ╚═╝ ██║╚██████╔╝   ██║   ██║  ██║╚██████╔╝██║ ╚████║
     ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                     3 . N A N O   3 0 B   |   N V I D I A
                  ┌─────────────────────────────────────────┐
                  │  31.6B Total  →  3.2B Active per Token  │
                  │     128 Experts  →  6 Activated         │
                  │     Context Window: 1M Tokens           │
                  └─────────────────────────────────────────┘
```

"오픈소스 LLM은 결국 성능과 속도 중 하나를 포기해야 한다."  
이런 고정관념이 있다면, NVIDIA가 방금 깨뜨렸다. 12월 15일 공개된 Nemotron 3 Nano 30B는 전체 파라미터의 10%만 활성화하면서도 Qwen3-30B보다 **3.3배 빠른 추론 속도**를 보여준다. 비결은 Mamba와 Transformer를 결합한 하이브리드 아키텍처에 있다.

**한줄요약:** 결론부터 말하면, Nemotron 3 Nano는 31.6B 파라미터 중 3.2B만 활성화하는 MoE 구조로 동급 모델 대비 최대 3.3배 빠른 추론과 100만 토큰 컨텍스트를 지원하는 오픈소스 에이전트 AI 모델이다.

---

## 배경

NVIDIA가 굳이 자체 LLM을 만든 이유가 있다. 기존 오픈소스 모델들은 대부분 Dense Transformer 구조다. 파라미터가 늘어나면 성능은 올라가지만, 추론 비용도 비례해서 증가한다. 에이전트 AI처럼 여러 모델이 동시에 돌아가야 하는 환경에서는 치명적인 병목이 된다.

> Nemotron 3 Nano는 Mamba-2 상태공간 모델과 Transformer 어텐션, 그리고 MoE(Mixture-of-Experts)를 결합한 하이브리드 아키텍처 기반의 오픈웨이트 LLM이다.

핵심 설계 철학은 명확하다. 모든 파라미터를 매번 계산하지 않는다. 128개의 전문가(expert) 중 토큰당 6개만 활성화해서, 31.6B 전체 파라미터 중 실제로는 3.2B만 사용한다. 마치 대형 도서관에서 필요한 책 6권만 꺼내 읽는 것과 같은 원리다.

이 구조가 특히 유효한 영역이 **에이전트 AI**다. 검색, 계획, 도구 실행, 검증 등 여러 하위 에이전트가 협업하는 시스템에서는 각 에이전트의 추론 비용이 곧 전체 시스템 비용이 된다. Nemotron 3 Nano는 이 문제를 아키텍처 레벨에서 해결하려는 시도다.

---

## 아키텍처 구조

Nemotron 3 Nano의 52개 레이어는 세 가지 유형으로 구성된다.

| 레이어 유형 | 개수 | 역할 |
| --- | --- | --- |
| Mamba-2 | 23 | 장거리 의존성 처리, 메모리 효율적 시퀀스 모델링 |
| MoE (Mixture-of-Experts) | 23 | 128개 전문가 중 6개 활성화, 연산 효율 극대화 |
| GQA Attention | 6 | 정밀한 추론과 구조적 관계 파악 |

Mamba-2 레이어가 긴 컨텍스트를 저비용으로 처리하고, Transformer 어텐션 레이어가 복잡한 추론을 담당한다. MoE 레이어는 토큰마다 관련 전문가만 활성화해서 Dense 모델 대비 연산량을 크게 줄인다.

이 조합의 결과는 수치로 나타난다. H200 GPU 단일 카드에서 8K 입력/16K 출력 기준, Qwen3-30B-A3B 대비 **3.3배**, GPT-OSS-20B 대비 **2.2배** 높은 처리량을 보인다.

---

## 벤치마크 성능

성능은 속도만으로 평가할 수 없다. Nemotron 3 Nano가 경쟁 모델과 어떻게 다른지 주요 벤치마크로 비교해보자.

| 벤치마크 | Nemotron 3 Nano | Qwen3-30B-A3B | GPT-OSS-20B |
| --- | --- | --- | --- |
| AIME25 (수학, 도구 없음) | 89.1% | 85.0% | 91.7% |
| AIME25 (도구 사용) | 99.2% | - | 98.7% |
| LiveCodeBench v6 | 68.3% | 66.0% | 61.0% |
| Arena-Hard-v2 (에이전트) | 67.7% | 57.8% | 48.5% |
| MMLU-Pro (일반 지식) | 78.3% | 80.9% | - |
| RULER @ 1M (장문맥) | 86.3% | - | 128K 한계 |

수학과 코딩에서는 도구를 결합했을 때 성능이 급상승한다. 특히 에이전트 워크플로우 신뢰도를 측정하는 Arena-Hard-v2에서 Qwen3 대비 **10% 포인트** 앞선다. 반면 MMLU-Pro 같은 광범위한 지식 테스트에서는 Qwen3가 근소하게 앞서는데, 이는 Dense 아키텍처가 백과사전적 지식 보존에 유리하기 때문으로 분석된다.

**100만 토큰 컨텍스트**는 단순한 마케팅 수치가 아니다. RULER 벤치마크에서 1M 컨텍스트 길이에서도 86.3%의 정확도를 유지한다. 대규모 코드베이스 분석이나 장기 에이전트 세션에서 chunking 없이 전체 맥락을 유지할 수 있다는 의미다.

---

## 훈련 데이터와 투명성

NVIDIA가 이번 릴리스에서 강조한 부분 중 하나는 **투명성**이다. 모델 가중치뿐 아니라 훈련 레시피와 재배포 가능한 데이터셋까지 공개했다.

- **Nemotron-CC-v2.1**: Common Crawl에서 추출한 2.5조 영어 토큰, 합성 리프레이징과 다국어 번역 포함
- **Nemotron-CC-Code-v1**: 4,280억 코드 토큰, Lynx 파이프라인으로 코드 구조 보존
- **Nemotron-Pretraining-Code-v2**: GitHub 코드 레퍼런스의 다단계 필터링 및 중복 제거 결과물

총 **25조 토큰**으로 훈련했으며, 사전훈련 이후 SFT(Supervised Fine-Tuning)와 RLHF(Reinforcement Learning from Human Feedback)를 거쳤다. 특히 다중 환경 강화학습에서 수학, 코딩, 도구 사용, 멀티턴 대화 등 실제 에이전트 태스크에 맞춘 GRPO(Group Relative Policy Optimization)를 적용했다.

---

## 실습: 로컬에서 Nemotron 3 Nano 실행하기

### 1. vLLM으로 서버 실행

가장 간단한 방법은 vLLM을 사용하는 것이다. FP8 양자화 버전을 사용하면 메모리 사용량을 줄일 수 있다.

```
vllm serve --model nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-FP8 \
  --max-num-seqs 8 \
  --tensor-parallel-size 1 \
  --max-model-len 262144 \
  --port 8000 \
  --trust-remote-code \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --reasoning-parser-plugin nano_v3_reasoning_parser.py \
  --reasoning-parser nano_v3
```

### 2. llama.cpp로 소비자 GPU에서 실행

RTX 시리즈 GPU에서 실행하려면 llama.cpp를 사용할 수 있다. 4비트 양자화 GGUF 버전이 필요하다.

```
# llama.cpp 빌드 (CUDA 지원)
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release -j

# 모델 다운로드 및 실행
./build/bin/llama-cli \
  -m NVIDIA-Nemotron-3-Nano-30B-A3B-Q4_K_M.gguf \
  -c 32768 \
  --special \
  -p "What is 2+2?"
```

### 3. 추론 모드 설정

Nemotron 3 Nano는 추론(reasoning) 모드를 on/off 할 수 있다. 복잡한 수학이나 코딩 문제에는 추론 모드를 켜고, 단순 대화에는 끄는 것이 효율적이다.

- **추론 ON**: `<think>` 토큰으로 내부 사고 과정 출력 후 최종 답변
- **추론 OFF**: 바로 답변 출력, 더 빠르지만 복잡한 문제에서 정확도 감소

---

## 모범사례/패턴 비교

| 활용 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| 멀티 에이전트 시스템 | 낮은 토큰당 비용으로 다수 에이전트 병렬 운영 가능 | 각 에이전트의 역할 분리가 명확해야 효율 극대화 |
| RAG 시스템 | 1M 컨텍스트로 chunking 없이 대용량 문서 처리 | 매우 긴 컨텍스트 사용 시 메모리 요구량 증가 |
| 코딩 어시스턴트 | LiveCodeBench 68.3%로 코드 생성 품질 우수 | MMLU-Pro 기준 일반 지식은 Qwen3 대비 소폭 열세 |
| 로컬 배포 | llama.cpp/LM Studio로 소비자 GPU 지원 | 전체 성능 발휘를 위해서는 H100급 GPU 권장 |

---

## Nemotron 3 패밀리 로드맵

Nano는 시작일 뿐이다. NVIDIA는 2026년 상반기까지 두 개의 상위 모델을 예고했다.

| 모델 | 총 파라미터 | 활성 파라미터 | 타겟 유스케이스 |
| --- | --- | --- | --- |
| Nano | 31.6B | 3.6B | 고효율 단일 에이전트 |
| Super | ~100B | ~10B | 협업 에이전트, IT 자동화 |
| Ultra | ~500B | ~50B | SOTA 추론, 복잡한 AI 애플리케이션 |

Super와 Ultra에는 LatentMoE(동일 비용으로 4배 더 많은 전문가 활용), Multi-Token Prediction(장문 생성 효율화), NVFP4 훈련 등 추가 기술이 적용될 예정이다.

---

## 마치며

- Nemotron 3 Nano는 하이브리드 Mamba-Transformer MoE 아키텍처로 31.6B 파라미터 중 3.2B만 활성화하여 동급 모델 대비 최대 3.3배 빠른 추론을 달성한다.
- 100만 토큰 컨텍스트와 에이전트 최적화 훈련으로 멀티 에이전트 시스템 구축에 적합하며, 가중치와 훈련 레시피, 데이터셋까지 공개해 재현 가능성을 높였다.
- 실전 팁: Hugging Face에서 FP8 버전을 다운로드해 vLLM으로 테스트 서버를 띄워보자. 에이전트 구축 프로젝트가 있다면, 기존 모델과 처리량 비교부터 시작하는 것이 좋다.

---

## 참고자료

- NVIDIA Nemotron 3 공식 페이지 (<https://research.nvidia.com/labs/nemotron/Nemotron-3/>)
- Hugging Face 모델 카드 (<https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16>)
- NVIDIA Developer Blog: Inside Nemotron 3 (<https://developer.nvidia.com/blog/inside-nvidia-nemotron-3-techniques-tools-and-data-that-make-it-efficient-and-accurate/>)
- Nemotron 3 Nano Technical Report (<https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf>)
- Unsloth Nemotron 3 실행 가이드 (<https://docs.unsloth.ai/models/nemotron-3>)
