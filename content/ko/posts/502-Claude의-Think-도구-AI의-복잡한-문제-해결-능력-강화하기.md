---
title: "Claude의 'Think' 도구 - AI의 복잡한 문제 해결 능력 강화하기 ?"
date: 2025-03-22T21:47:47+09:00
slug: "502-Claude의-Think-도구-AI의-복잡한-문제-해결-능력-강화하기"
original_url: "https://memoryhub.tistory.com/502"
tistory_id: 502
draft: false
---

여러분은 복잡한 문제를 풀 때 어떻게 하시나요? 아마도 종이에 생각을 적거나, 단계별로 메모를 하거나, 문제를 작은 부분으로 나누어 생각하실 겁니다. ? 이런 '생각하는 공간'이 없다면 어떨까요?

Anthropic이 개발한 'Think' 도구는 바로 이런 개념에서 출발했습니다. AI 비서 Claude에게 생각을 정리하고 구조화할 수 있는 전용 공간을 제공함으로써 복잡한 문제 해결 능력을 크게 향상시키는 도구입니다.

- 마치 여러분이 복잡한 수학 문제를 풀 때 풀이 과정을 적어가는 것과 같습니다
- AI가 문제 해결 과정에서 자신의 사고를 정리하고 검증할 수 있는 '메모장' 역할을 합니다

## 왜 필요한가? ?‍♀️

Claude의 'Think' 도구가 해결하는 문제들은 다음과 같습니다:

1. **도구 출력 분석 어려움**: Claude가 이전 도구 호출의 결과를 처리하고 다음 행동을 결정하는 과정에서 발생하는 오류를 줄여줍니다.
2. **정책 준수 문제**: 복잡한 가이드라인과 정책을 따라야 하는 상황에서 각 단계의 준수 여부를 체계적으로 확인할 수 있게 합니다.
3. **순차적 의사결정의 일관성**: 각 결정이 이전 단계를 기반으로 이루어지는 환경에서 오류가 누적되는 문제를 방지합니다.

Extended Thinking과의 차이점은 무엇일까요? Extended Thinking은 Claude가 응답을 생성하기 전에 심층적으로 계획을 수립하는 과정이지만, Think 도구는 응답 생성 중에 새로운 정보를 처리하고 다음 단계를 결정하는 데 도움을 줍니다. 마치 문제를 풀면서 중간에 메모를 하는 것과 비슷합니다. ?

## 기본 원리 ?

Think 도구의 핵심 원리를 알아볼까요?

### 구현 방식

```
{
  "name": "think",
  "description": "Use the tool to think about something. It will not obtain new information or change the database, but just append the thought to the log. Use it when complex reasoning or some cache memory is needed.",
  "input_schema": {
    "type": "object",
    "properties": {
      "thought": {
        "type": "string",
        "description": "A thought to think about."
      }
    },
    "required": ["thought"]
  }
}
```

이 간단한 JSON 형식의 도구 정의만으로도 Claude의 문제 해결 능력이 크게 향상됩니다. 복잡한 구현이 필요 없이, 단지 생각을 기록할 수 있는 공간을 제공하는 것만으로도 효과가 있습니다.

### 최적화된 프롬프트의 중요성

```
## Using the think tool

Before taking any action or responding to the user after receiving tool results, use the think tool as a scratchpad to:
- List the specific rules that apply to the current request
- Check if all required information is collected
- Verify that the planned action complies with all policies
- Iterate over tool results for correctness
```

위와 같은 프롬프트 예시를 통해 Claude에게 Think 도구의 사용 방법을 구체적으로 안내하면 성능이 더욱 향상됩니다. 특히 복잡한 도메인에서는 최적화된 프롬프트가 성능 향상에 큰 영향을 미칩니다.

## 실제 예제 ?

### τ-Bench 성능 결과

Anthropic은 τ-Bench(tau-bench)라는 고객 서비스 시나리오 기반 벤치마크를 통해 Think 도구의 효과를 평가했습니다. 그 결과는 놀라웠습니다:

| 구성 | 항공사 도메인 (k=1) | 소매업 도메인 (k=1) |
| --- | --- | --- |
| 기본 | 0.332 | 0.783 |
| Extended thinking | 0.412 | 0.770 |
| Think 도구 | 0.404 | 0.812 |
| Think + 최적화 프롬프트 | 0.584 | - |

특히 항공사 도메인에서는 최적화된 프롬프트와 함께 사용했을 때 기본 성능 대비 54%의 상대적 성능 향상을 보였습니다! ?

### SWE-Bench 성능 결과

소프트웨어 엔지니어링 벤치마크인 SWE-Bench에서도 Think 도구는 유사한 형태로 적용되어 1.6%의 성능 향상을 보였습니다. 이는 Claude 3.7 Sonnet이 0.623이라는 최첨단 점수를 달성하는 데 기여했습니다.

### 기본 사용법

```
# Think 도구 구현 예시
def think(thought):
    """
    생각을 기록하는 함수
    """
    # 단순히 생각을 로그에 기록만 하고 외부 상태를 변경하지 않음
    log_thought(thought)
    return {"thought_recorded": True}

# 실제 사용 예시
def process_customer_request(request):
    # 기존 방식
    # 바로 응답 생성...

    # Think 도구 활용 방식
    think("고객 요청 분석: 항공권 취소 요청이므로 다음 규칙 확인 필요:")
    think("1. 예약 후 24시간 이내인지 확인")
    think("2. 티켓 클래스와 보험 조건 확인")
    think("3. 이미 지난 여정이 있는지 확인")

    # 이후 검증된 단계에 따라 진행
    # ...
```

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. 모든 상황에 Think 도구가 필요하지는 않습니다

   - 단일 도구 호출이나 병렬 호출만 필요한 경우에는 효과가 크지 않습니다
   - 간단한 지시 사항만 있는 경우에는 기본 동작만으로도 충분합니다
2. 도메인 특화 예시가 중요합니다

   - 단순히 Think 도구를 추가하는 것보다, 관련 도메인의 예시를 함께 제공하는 것이 효과적입니다
   - 특히 복잡한 정책이 있는 도메인에서는 구체적인 사고 예시가 필수적입니다

? **꿀팁**

- 시스템 프롬프트에 Think 도구 사용 안내를 포함하세요
- 도메인별 사고 과정의 예시를 2-3개 이상 제공하면 성능이 크게 향상됩니다
- 복잡한 다단계 도구 사용 시나리오에서 가장 효과적입니다

## 마치며 ?

지금까지 Claude의 'Think' 도구에 대해 알아보았습니다. 이 간단하지만 강력한 도구는 AI 모델이 복잡한 문제를 해결할 때 인간처럼 생각을 정리하고 단계적으로 접근할 수 있도록 도와줍니다. 최소한의 구현 노력으로 최대의 성능 향상을 얻을 수 있는 효율적인 방법입니다.

특히 정책 준수, 다단계 도구 체인, 순차적 의사결정이 필요한 환경에서 Claude의 신뢰성과 일관성을 크게 향상시킬 수 있습니다. 여러분의 AI 어플리케이션에서도 이 기법을 시도해보시는 것을 적극 권장합니다!

혹시 궁금한 점이 있으시거나, 더 알고 싶은 내용이 있으시면 댓글로 남겨주세요.

## 참고 자료 ?

- [The "think" tool: Enabling Claude to stop and think (Anthropic)](https://www.anthropic.com/engineering/claude-think-tool)
- [Anthropic's new 'think tool' lets Claude take notes to solve complex problems (The Decoder)](https://the-decoder.com/anthropics-new-think-tool-lets-claude-take-notes-to-solve-complex-problems/)
- [Claude 3.7 Sonnet (Anthropic)](https://www.anthropic.com/claude/sonnet)

---

#AI #Claude #ThinkTool #문제해결 #AgenticAI
