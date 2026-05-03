---
title: "? Vibe-tuning 실전 가이드: Claude Code로 SLM Fine-Tuning"
date: 2025-12-14T20:29:41+09:00
slug: "927-Vibe-tuning-실전-가이드-Claude-Code로-SLM-Fine-Tuning"
original_url: "https://memoryhub.tistory.com/927"
tistory_id: 927
draft: false
---

```
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║      ┌─────────┐     Claude     ┌─────────┐                 ║
║      │  Vibe   │ ──── Code ────▶│  SLM    │                 ║
║      │  Spec   │    (Agent)     │ Tuned!  │                 ║
║      └─────────┘                └─────────┘                 ║
║                                                              ║
║    "자연어로 정의하면, AI가 학습까지 자동화한다"             ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

파인튜닝이라고 하면 데이터셋 구축, 하이퍼파라미터 조정, GPU 세팅까지 몇 주가 걸리는 작업을 떠올립니다. 그런데 만약 "이런 말투로 답해줘"라고 글로 쓰기만 하면, 나머지를 AI가 알아서 처리해준다면 어떨까요? 이 글에서는 **자연어 명세 하나로 데이터 생성부터 학습, 평가, 배포까지 자동화하는 Vibe-tuning 워크플로**를 실습 중심으로 다룹니다. 읽고 나면

Claude Code와 Hugging Face Skills를 연동해 직접 파이프라인을 구축할 수 있습니다.

**한줄요약:** 결론부터 말하면, Vibe-tuning은 원하는 출력 스타일을 자연어로 정의(Vibe Spec)하고, Claude Code가 합성 데이터 생성과 모델 학습을 자동 수행하게 하여 SLM 튜닝 시간을 "몇 주"에서 "몇 시간"으로 단축하는 방법론입니다.

---

## 배경

LLM을 서비스에 적용할 때 가장 흔한 고민이 있습니다. "GPT-4나 Claude를 쓰자니 비용이 부담되고, 오픈소스 소형 모델을 쓰자니 우리 서비스 톤에 안 맞는다." 파인튜닝이 답이라는 건 알지만, 실제로 해보면 벽에 부딪힙니다.

기존 파인튜닝의 진입 장벽은 세 가지로 요약됩니다. 첫째, 양질의 학습 데이터를 수백에서 수천 건 확보해야 합니다. 둘째, 하이퍼파라미터 튜닝과 GPU 환경 세팅에 ML 엔지니어링 경험이 필요합니다. 셋째, 학습 후 평가 기준이 모호해서 "잘 됐는지"를 판단하기 어렵습니다.

Vibe-tuning은 이 문제를 "자동화"로 해결합니다. 핵심 아이디어는 단순합니다. 원하는 결과물을 자연어로 상세히 기술하면, AI 에이전트(Claude Code)가 그에 맞는 합성 데이터를 생성하고, 클라우드 학습 인프라(Hugging Face Jobs)에 작업을 제출하며, 규칙 기반 평가까지 수행합니다.

| 용어 | 정의 |
| --- | --- |
| Vibe Spec | 원하는 말투, 출력 포맷, 금지 규칙 등을 자연어로 작성한 명세 문서 |
| SLM | Small Language Model. 0.5B~3B 파라미터급 소형 언어 모델 |
| SFT | Supervised Fine-Tuning. 레이블된 데이터로 모델을 학습시키는 방식 |
| LoRA | Low-Rank Adaptation. 전체 가중치 대신 일부만 학습해 효율을 높이는 기법 |

---

## 핵심

> 한 줄 정의: Vibe-tuning은 "자연어 프롬프트 → 합성 데이터 생성 → 학습 → 평가"를 하나의 자동화 루프로 묶어, 비개발자도 SLM을 서비스 맞춤형으로 튜닝할 수 있게 하는 접근 방식입니다.

Vibe Coding과 Vibe-tuning은 이름이 비슷하지만 결정적 차이가 있습니다. Vibe Coding이 "프롬프트로 코드 생성"에 그친다면, Vibe-tuning은 **실제 배포 가능한 모델을 만들기 위해 평가 단계까지 포함**합니다. 요리에 비유하면, Vibe Coding은 레시피를 받아 재료를 손질하는 것이고, Vibe-tuning은 손질부터 조리, 플레이팅, 맛 평가까지 전 과정을 자동화하는 것입니다.

전체 파이프라인은 6단계로 구성됩니다.

첫 번째, Vibe Spec 작성입니다. 원하는 말투, 필수/금지 규칙, 출력 포맷을 마크다운 문서로 명세합니다.

두 번째, 데이터 생성입니다. Claude Code가 Spec을 읽고 합성 학습 데이터를 JSONL 형태로 생성합니다.

세 번째, 1차 튜닝입니다. Qwen3-0.6B 같은 소형 모델에 LoRA 방식으로 SFT를 수행합니다.

네 번째, 평가입니다. JSON 파싱 성공률, 필수 키 존재 여부, 금칙어 포함 여부 등을 자동 검증합니다.

다섯 번째, 2차 정렬(선택)입니다. DPO나 GRPO로 선호 스타일을 강화합니다.

여섯 번째, 배포입니다. Hub 업로드 및 GGUF 변환을 수행합니다.

여기서 Claude Code의 역할은 "자동화의 손"입니다. 데이터 생성 프롬프트를 실행하고, Hugging Face Skills를 통해 학습 작업을 제출하며, 결과를 모니터링합니다. 실제 GPU 연산은 Hugging Face 인프라에서 처리되므로 로컬 환경에 고사양 장비가 필요하지 않습니다.

---

## 실습

### ① 환경 설정: Claude Code와 HF Skills 연동

먼저 Claude Code를 설치합니다.

```
# macOS/Linux
curl -fsSL https://claude.ai/install.sh | bash

# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex

# 또는 NPM
npm install -g @anthropic-ai/claude-code
```

다음으로 Hugging Face Skills 플러그인을 추가합니다. Claude Code 터미널에서 아래 명령을 실행합니다.

```
/plugin marketplace add huggingface/skills
/plugin install hf-llm-trainer@huggingface-skills
```

마지막으로 HF 토큰을 설정하고 MCP 서버를 연결합니다.

```
export HF_TOKEN=hf_your_write_access_token_here

claude mcp add --transport http hf-skills \
  https://huggingface.co/mcp?bouquet=skills \
  --header "Authorization: Bearer $HF_TOKEN"
```

Write 권한이 있는 토큰이 필요하며, Hugging Face Jobs 기능은 유료 플랜에서 제공될 수 있습니다.

### ② Vibe Spec 작성

프로젝트 폴더에 `VIBE_SPEC.md` 파일을 생성합니다. 아래는 "포맷 강제형 한국어 기술 어시스턴트" 예시입니다.

```
# VIBE_SPEC.md
목표: 한국어 기술 어시스턴트. 반드시 JSON으로만 응답.

[필수 사항]
- 출력은 순수 JSON 단일 객체일 것 (Markdown 코드 블록이나 사족 금지).
- 포함 키: answer, assumptions, risks, next_steps.
- 불확실성 처리: assumptions에 가정 명시, risks에 잠재 위험 명시.

[금지 사항]
- 과장된 표현 ("100%", "무조건" 등).
- 민감 정보 및 비공개 코드 유출.

[스타일]
- answer는 3~7문장 내외로 간결하게.
- next_steps는 3~6개의 항목으로 구성.
```

Spec이 구체적일수록 생성되는 데이터 품질이 높아집니다. "짧게 써줘"보다 "3~7문장"처럼 정량적 기준을 명시하는 것이 좋습니다.

### ③ 합성 데이터 생성

Claude Code 터미널에서 다음과 같이 명령합니다.

```
"프로젝트 폴더의 VIBE_SPEC.md를 기준으로 다음 작업을 수행해줘:

1. TRL SFTTrainer 호환 messages 포맷으로 학습 샘플 800개(train.jsonl) 생성.
2. 검증 샘플 200개(eval.jsonl) 생성.
3. 주제 분포:
   - 40%: 코드/검증 (UVM, assertion, 디버깅)
   - 30%: 시스템/아키텍처
   - 20%: 문서 요약/변환
   - 10%: 에러 상황에서 "모름/가정" 처리
4. Eval 데이터에는 Train과 유사한 질문 금지.
5. 생성 후 JSON 파싱 테스트 스크립트도 작성하고 실행해줘."
```

생성되는 데이터는 아래 형식을 따릅니다.

```
{"messages":[
  {"role":"user","content":"아래 요구사항을 만족하는 SystemVerilog assertion 예시를 만들어줘: ..."},
  {"role":"assistant","content":"{\"answer\":\"...\",\"assumptions\":[...],\"risks\":[...],\"next_steps\":[...]}"}
]}
```

**주의할 점이 있습니다.** 학습 시 사용한 Chat Template과 추론 시 Template이 다르면 성능이 급락합니다. TRL의 messages 포맷을 사용하면 Template이 자동 적용되어 이 문제를 예방할 수 있습니다.

### ④ 학습 작업 제출

데이터셋을 Hub에 업로드한 후, Claude Code에 자연어로 명령합니다.

```
"Fine-tune Qwen/Qwen3-0.6B on my-org/korean-tech-json-style for instruction following."
```

Claude Code는 적절한 하드웨어(예: t4-small)를 제안하고, 예상 시간과 비용을 추정한 뒤 승인을 요청합니다. 승인하면 Hugging Face 인프라에서 학습이 실행됩니다. 0.6B 모델은 가볍기 때문에 비용이 저렴합니다.

### ⑤ 평가 자동화

학습이 완료되면 다음 지표를 자동 검증합니다.

| 평가 항목 | 설명 | 목표 |
| --- | --- | --- |
| JSON 파싱 성공률 | 출력이 유효한 JSON인지 | 99% 이상 |
| 필수 키 존재 | answer, assumptions 등 포함 여부 | 100% |
| 금칙어 검출 | "무조건", "100%" 등 포함 시 실패 | 0건 |
| 길이 제한 | answer 3~7문장 준수 | 95% 이상 |

이 지표들이 깨지면 서비스 장애로 이어지므로 반드시 통과해야 합니다. TRL 사용 시 `completion_only=True` 설정으로 Assistant 응답 부분만 Loss를 계산하게 하면 학습 효율이 높아집니다.

---

## 모범사례/패턴 비교

| 접근 방식 | 장점 | 주의점 |
| --- | --- | --- |
| SFT + LoRA | 빠른 반복, 적은 컴퓨팅 비용, 원본 모델 보존 | 일반 언어 능력 저하(과적합) 가능 |
| SFT → DPO 2단계 | 기본 포맷 학습 후 선호 스타일 정교화 | 좋은/나쁜 답변 쌍 데이터 구축 필요 |
| GRPO | 검증 가능한 리워드(컴파일 성공 등) 활용 | 리워드 함수 설계가 복잡할 수 있음 |
| 일반 데이터 혼합(Replay Buffer) | Catastrophic Forgetting 방지 | 혼합 비율 튜닝 필요 |

**트러블슈팅 체크리스트**로 세 가지를 기억하세요.

첫째, 템플릿 불일치입니다. 학습과 추론에서 동일한 Chat Template을 사용해야 합니다.

둘째, Eval 누수입니다. Train 데이터와 유사한 질문이 Eval에 들어가면 평가가 왜곡됩니다.

셋째, 보안입니다. Claude Code가 로컬 파일에 접근하므로 민감 정보 제외 규칙을 명시하고 생성 데이터를 검수해야 합니다.

---

## 마치며

- Vibe-tuning의 핵심은 "자연어 명세(Vibe Spec)"를 작성하고, Claude Code가 데이터 생성부터 학습, 평가를 자동화하게 하는 것입니다.
- 실전 팁: 오늘 당장 `VIBE_SPEC.md` 파일에 원하는 출력 스타일을 3가지 규칙으로 정리해보세요.

---

## 참고자료

- Hugging Face TRL 공식 문서 (<https://huggingface.co/docs/trl>)
- Claude Code 설치 가이드 (<https://docs.anthropic.com/en/docs/claude-code>)
- Distillabs Vibe-tuning 개념 소개 (<https://distillabs.ai>)
