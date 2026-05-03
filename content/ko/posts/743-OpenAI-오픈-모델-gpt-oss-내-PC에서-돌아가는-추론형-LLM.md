---
title: "OpenAI 오픈 모델(gpt-oss) – “내 PC에서 돌아가는 추론형 LLM”  ??"
date: 2025-08-08T08:17:37+09:00
slug: "743-OpenAI-오픈-모델-gpt-oss-내-PC에서-돌아가는-추론형-LLM"
original_url: "https://memoryhub.tistory.com/743"
tistory_id: 743
draft: false
---

요즘 “회사 데이터는 밖으로 못 나가고, 그래도 GPT급 추론은 하고 싶다”는 요구 진짜 많죠. 그래서 \*\*OpenAI의 오픈 웨이트 추론 모델 `gpt-oss`(120b/20b)\*\*가 화제입니다. 라이선스 자유롭고(아파치 2.0), 에이전트 작업에 맞춰 설계됐고, 심지어 **완전한 생각의 흐름(Chain-of-Thought, CoT)에 접근**도 됩니다. 이 글에서 **왜 나왔고, 뭐가 다르고, 어떻게 돌리면 되는지** 쉽고 빠르게 정리합니다. ([OpenAI](https://openai.com/ko-KR/open-models/ "OpenAI의 오픈 모델 | OpenAI"))

---

## 등장 배경

과거 OpenAI는 GPT-2 이후엔 언어 모델을 오픈 웨이트로 거의 내놓지 않았습니다. 그런데 **온프레미스/로컬 추론** 수요, **비용/지연시간 최적화**, **맞춤형 안전 통제** 니즈가 커졌죠. 그 배경에서 \*\*`gpt-oss-120b`와 `gpt-oss-20b`\*\*가 2025년 8월 5일 공개됐습니다. “추론 작업에서 동급 대비 강력하고, 도구 사용(web search·Python 실행)까지 고려한 에이전트 워크플로”가 핵심 가치 제안입니다. ([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "gpt-oss를 소개합니다 | OpenAI"))

---

## 문제 해결 포인트

1. **배포 유연성** – 데이터센터부터 고급 노트북까지, 환경 맞춰 **로컬 실행**. (20b는 16GB급, 120b는 80GB급/멀티GPU) ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-transformers "How to run gpt-oss with Transformers"))
2. **에이전트 친화** – **함수 호출·웹검색·코드 실행**을 염두에 둔 설계. 추론 난이도(`reasoning_effort`)를 **낮음/중간/높음**으로 조절. ([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "gpt-oss를 소개합니다 | OpenAI"), [OpenAI 플랫폼](https://platform.openai.com/docs/guides/reasoning?utm_source=chatgpt.com "Reasoning models - OpenAI API"))
3. **상업 사용 OK** – **Apache-2.0**으로 실험/맞춤/상업 배포 자유도↑. ([OpenAI](https://openai.com/ko-KR/open-models/ "OpenAI의 오픈 모델 | OpenAI"))

---

## 핵심 원리

### 1) 모델 구조 한눈에 보기

```
# gpt-oss(모두 텍스트 전용) - 에이전트/추론 지향
+------------------+
|  입력 토큰       |
+---------+--------+
          |
          v
   [교차 Attention]  <— GQA, 128k 컨텍스트
          |
          v
   [MoE 블록 (라우터)]
      ├─ 128개 전문가 중 Top-4 활성(120b)
      └─  32개 전문가 중 Top-4 활성(20b)
          |
          v
   [출력 + (필요 시) 도구 호출/구조화 출력]
```

*MoE(혼합 전문가) 구조로 **토큰당 일부 전문가만** 활성화해 **추론 성능↔지연/메모리** 균형을 잡습니다. 두 모델 모두 **최대 128k 컨텍스트**, GQA, RoPE를 사용합니다.* ([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "gpt-oss를 소개합니다 | OpenAI"))

### 2) 스펙 요약

| 항목 | gpt-oss-120b | gpt-oss-20b |
| --- | --- | --- |
| 총 파라미터 | 약 **117B** (정확히 116.8B) | 약 **21B** (정확히 20.9B) |
| 토큰당 활성 파라미터 | **~5.1B** | **~3.6B** |
| 레이어 | **36** | **24** |
| MoE 전문가 수 | **128** (Top-4 활성) | **32** (Top-4 활성) |
| 컨텍스트 길이 | **128k** | **128k** |
| 라이선스 | **Apache-2.0** | **Apache-2.0** |

([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "gpt-oss를 소개합니다 | OpenAI"))

### 3) 성능 포지셔닝(요점만)

- 벤치마크(MMLU, GPQA, AIME 등)에서 **120b는 o4-mini에 근접**, **20b는 소형이지만 o3-mini급**으로 제시됩니다. 자세한 수치는 모델 카드/공식 페이지를 참고하세요. ([OpenAI](https://openai.com/ko-KR/open-models/ "OpenAI의 오픈 모델 | OpenAI"))

### 4) 안전/거버넌스

- 오픈 모델은 **악의적 파인튜닝** 위험 등이 있어 출시 전후로 **준비성 프레임워크(Preparedness Framework)** 기준으로 **적대적 파인튜닝 테스트**를 수행했고, 추적 카테고리(생물·화학, 사이버, AI 자기개선)에서 **‘High’ 기준에 미달**했음을 모델 카드에 명시합니다.
- 기본 정책 준수 외에 \*\*배포자(여러분)\*\*가 **추가 안전장치**를 설계해야 할 수 있습니다.

---

## 바로 써보기: 코드 & 워크플로

### 1) 로컬 서버(Responses 호환)로 호출

```
# 1) Transformers 서버 띄우기
transformers serve

# 2) cURL로 Responses 호환 엔드포인트 호출
curl -X POST http://localhost:8000/v1/responses \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-oss-20b",
    "input": [{"role":"user","content":"오픈 모델 특징을 3줄로 요약해줘"}],
    "max_output_tokens": 300,
    "temperature": 0.7
  }'
```

*왜 Responses 호환이 중요?* 기존 OpenAI 앱/에이전트 코드와 **인터페이스를 맞추기 쉽기 때문**이죠. ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-transformers "How to run gpt-oss with Transformers"))

### 2) 추론 비용·지연 제어: `reasoning.effort`

```
{
  "model": "openai/gpt-oss-20b",
  "reasoning": { "effort": "low" },  // "low" | "medium" | "high"
  "input": [{"role":"user","content":"한 문장 요약"}]
}
```

*간단 작업은 `low`, 난이도 높은 단계적 추론은 `high`로 두면 됩니다.* ([OpenAI 플랫폼](https://platform.openai.com/docs/guides/reasoning?utm_source=chatgpt.com "Reasoning models - OpenAI API"))

### 3) API 응답을 **JSON 스키마**로 강제(구조화 출력)

```
{
  "model": "openai/gpt-oss-20b",
  "response_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "faq",
      "schema": {
        "type": "object",
        "properties": {
          "question": { "type": "string" },
          "answer":   { "type": "string" }
        },
        "required": ["question","answer"],
        "additionalProperties": false
      },
      "strict": true
    }
  },
  "input": [{"role":"user","content":"gpt-oss 핵심 FAQ 하나 만들어줘"}]
}
```

*프론트/백엔드 파이프라인에서 **후처리 없이** 바로 쓰기 좋습니다.* ([OpenAI 플랫폼](https://platform.openai.com/docs/guides/structured-outputs?utm_source=chatgpt.com "Structured model outputs - OpenAI API"))

---

## 주의사항 및 팁 ?

⚠️ **주의할 점**

- **하드웨어 현실 체크**:
  - **20b**는 MXFP4 기준 **~16GB VRAM**에서, **120b**는 **≥60GB VRAM 또는 멀티 GPU**가 권장됩니다. Hopper 이상/MXFP4 지원 확인. ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-transformers "How to run gpt-oss with Transformers"))
  - bfloat16로 돌리면 메모리 사용이 크게 늘어납니다. ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-transformers "How to run gpt-oss with Transformers"))
- **지식 컷오프**: gpt-oss의 **지식 기준일은 2024년 6월**. 최신 이슈는 툴 호출(웹검색)로 보완하세요.
- **의료/안전 가이드라인 준수**: 모델 카드는 **의료 진단/치료 목적 아님**을 명시합니다. 도메인 특화 검증·감사를 붙이세요. ([OpenAI](https://openai.com/ko-KR/index/introducing-gpt-oss/ "gpt-oss를 소개합니다 | OpenAI"))

? **꿀팁**

- **에이전트 워크플로**에서 함수 호출과 구조화 출력을 **동시에** 쓰면 안정성이 확 올라갑니다. ([OpenAI 플랫폼](https://platform.openai.com/docs/guides/function-calling?utm_source=chatgpt.com "Function calling - OpenAI API"))
- **레거시 프롬프트**를 그대로 쓰기보다, `reasoning.effort`를 작업 난이도에 맞춰 지정해 **비용/지연을 세밀 제어**하세요. ([OpenAI 플랫폼](https://platform.openai.com/docs/guides/reasoning?utm_source=chatgpt.com "Reasoning models - OpenAI API"))
- **vLLM/Transformers/Ollama** 등 서빙 스택을 상황에 맞게 고르세요(속도·메모리·운영 편의 트레이드오프). ([OpenAI Cookbook](https://cookbook.openai.com/articles/gpt-oss/run-vllm "How to run gpt-oss with vLLM"))

---

## 마치며

오픈 웨이트라고 해서 “성능은 포기해야지…” 시대는 지난 듯합니다. **gpt-oss는 에이전트-친화 설계, 추론 단계 제어, 구조화 출력**까지 갖춰 **현업 투입 가능한 로컬 추론 옵션**을 열었습니다.  
여러분 팀은 **어떤 워크플로**에 먼저 붙여보고 싶나요? 댓글로 사용 환경(GPU/메모리)과 기대 시나리오를 남겨 주세요!

---

## 참고 자료 ?

- OpenAI — **OpenAI의 오픈 모델(ko-KR)**: <https://openai.com/ko-KR/open-models/>
- OpenAI — **gpt-oss를 소개합니다(ko-KR, 2025-08-05)**: <https://openai.com/ko-KR/index/introducing-gpt-oss/>
- OpenAI — **gpt-oss 모델 카드(PDF)**: <https://cdn.openai.com/pdf/419b6906-9da6-406c-a19d-1bb078ac7637/oai_gpt-oss_model_card.pdf>
- OpenAI API — **Reasoning 가이드(`reasoning.effort`)**: <https://platform.openai.com/docs/guides/reasoning>
- OpenAI API — **Structured Outputs 가이드**: <https://platform.openai.com/docs/guides/structured-outputs>
- OpenAI Cookbook — **Transformers로 gpt-oss 실행하기**: <https://cookbook.openai.com/articles/gpt-oss/run-transformers>
- OpenAI Cookbook — **vLLM로 gpt-oss 서빙하기**: <https://cookbook.openai.com/articles/gpt-oss/run-vllm>

---

**#오픈모델 #gpt-oss #로컬LLM**
