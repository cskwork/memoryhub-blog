---
title: "? Claude Sonnet 5 Fennec과 Opus 4.6, 403 응답이 증명한 출시 임박"
date: 2026-02-05T21:49:57+09:00
slug: "1006-Claude-Sonnet-5-Fennec과-Opus-4-6-403-응답이-증명한-출시-임박"
original_url: "https://memoryhub.tistory.com/1006"
tistory_id: 1006
draft: false
---

```
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║     VERTEX AI MODEL GARDEN - ENDPOINT SCAN RESULTS             ║
    ║     ══════════════════════════════════════════════════         ║
    ║                                                                ║
    ║     ┌────────────────────────────────────────────────┐         ║
    ║     │  MODEL ID                    │  HTTP RESPONSE  │         ║
    ║     ├────────────────────────────────────────────────┤         ║
    ║     │  claude-sonnet-99 (fake)     │  404 NOT FOUND  │         ║
    ║     │  claude-opus-99 (fake)       │  404 NOT FOUND  │         ║
    ║     ├────────────────────────────────────────────────┤         ║
    ║     │  claude-sonnet-5             │  403 FORBIDDEN  │  ←      ║
    ║     │  claude-opus-4-6             │  403 FORBIDDEN  │  ←      ║
    ║     └────────────────────────────────────────────────┘         ║
    ║                                                                ║
    ║     403 = EXISTS but ACCESS DENIED (permission-gated)          ║
    ║     404 = DOES NOT EXIST                                       ║
    ║                                                                ║
    ║          ┌─────────┐        ┌─────────┐                        ║
    ║         /  FENNEC   \      /  OPUS    \                        ║
    ║        │   (o   o)   │    │   4.6     │                        ║
    ║         \   \_/    /      │    ???    │                        ║
    ║          \_______/        └─────────┘                          ║
    ║                                                                ║
    ║              SONNET 5          OPUS 4.6                        ║
    ║            "가성비 괴물"      "새로운 정점?"                    ║
    ╚════════════════════════════════════════════════════════════════╝
```

"모델이 존재하지 않으면 404, 존재하지만 접근 권한이 없으면 403." 이 단순한 HTTP 응답 규칙이 AI 업계에서 가장 큰 유출 사건의 기술적 증거가 되었습니다.

개발자 Ben Taleb Jr.가 Google Vertex AI 엔드포인트를 스캔한 결과, `claude-sonnet-5`와 `claude-opus-4-6` 모두 403 Forbidden을 반환했습니다. 가짜 모델 ID는 404를 반환했고요.

**이것은 두 모델이 Google 인프라에 이미 배포되어 있으며, 공개 스위치만 기다리고 있다는 기술적 증거입니다.**

**한줄요약:** 결론부터 말하면, Claude Sonnet 5와 Opus 4.6 모두 Vertex AI에서 존재가 확인되었고,

Anthropic의 "듀얼 트랙" 전략이 현실화되고 있다.

## 배경

Anthropic의 모델 라인업은 명확한 계층 구조를 가지고 있었습니다. Haiku는 속도, Sonnet은 균형, Opus는 최고 성능. 그런데 이번 유출은 이 구조에 균열을 일으킵니다.

> 한 줄 정의: 403 Forbidden은 RESTful API에서 "리소스가 존재하지만 접근 권한이 없다"는 의미다. 404 Not Found와 달리, 서버가 해당 리소스를 인식하고 있음을 나타낸다.

2026년 2월 초, 개발자 Ben Taleb Jr.(@macintoch)가 X에 올린 포스트가 AI 커뮤니티를 뒤흔들었습니다.

그는 Google Cloud Vertex AI의 Model Garden 엔드포인트를 대상으로 스캔 스크립트를 실행했고, 결과는 명확했습니다.

존재하지 않는 가짜 모델 ID(claude-sonnet-99)는 404를,

유출된 모델 ID(claude-sonnet-5, claude-opus-4-6)는 403을 반환했습니다.

이 발견은 독립적으로 검증되었습니다.

DeepakNess를 포함한 여러 개발자들이 자체 Vertex AI 프로젝트를 생성하고 동일한 테스트를 수행했습니다.

결과는 일관되게 동일했습니다. 실제 존재하는 모델(Opus 4.5 등)은 200 OK, 유출된 모델들은 403, 가짜 모델은 404.

## 유출의 핵심: 두 모델이 동시에 발견되었다

주목해야 할 점은 **Sonnet 5와 Opus 4.6이 함께 발견되었다**는 사실입니다. 이는 Anthropic이 두 가지 다른 목적의 모델을 동시에 준비하고 있음을 시사합니다.

**Claude Sonnet 5 "Fennec" - 유출된 정보**

모델 ID는 `claude-sonnet-5@20260203`으로, Anthropic의 기존 명명 규칙(`claude-opus-4-5@20251101`)과 일치합니다. 내부 코드네임 "Fennec"은 큰 귀를 가진 사막여우를 의미하며, 이는 100만 토큰이라는 확장된 컨텍스트 윈도우를 상징하는 것으로 해석됩니다. 유출된 벤치마크에 따르면 SWE-Bench Verified 점수는 82.1%에서 83.3% 사이로 추정되며,

이는 현재 Opus 4.5의 80.9%를 상회합니다. 가격은 Sonnet 4.5와 동일한 $3/$15(input/output per 1M tokens)로 알려졌습니다.

**Claude Opus 4.6 - 존재만 확인**

Opus 4.6에 대해서는 상세 스펙이 유출되지 않았습니다. 확인된 것은 `claude-opus-4-6` 엔드포인트가 403 응답을 반환한다는 사실뿐입니다. 이는 모델이 존재하며 배포되어 있지만, 아직 공개되지 않았음을 의미합니다.

Pankaj Kumar는 X에서 2월 3일에 4차례 서비스 장애가 발생했으며, 이것이 실패한 배포와 롤백의 증거일 수 있다고 분석했습니다.

## 기술적 증거 분석

| 테스트 대상 | HTTP 응답 | 의미 |
| --- | --- | --- |
| claude-sonnet-99 (가짜) | 404 Not Found | 리소스 존재하지 않음 |
| claude-opus-99 (가짜) | 404 Not Found | 리소스 존재하지 않음 |
| claude-opus-4-5 (현재) | 200 OK | 정상 접근 가능 |
| **claude-sonnet-5** | **403 Forbidden** | **존재하나 접근 불가** |
| **claude-opus-4-6** | **403 Forbidden** | **존재하나 접근 불가** |

여러 독립적인 검증자들이 동일한 결과를 얻었다는 점이 중요합니다.

이는 단순한 스크린샷이나 루머가 아닌, 재현 가능한 기술적 증거입니다.

## 두 모델의 포지셔닝 추론

유출된 정보를 바탕으로 Anthropic의 전략을 추론하면 다음과 같습니다.

**Sonnet 5: 가성비 혁명**

Opus 4.5 수준의 성능을 Opus 가격의 20%에 제공합니다.

100만 토큰 컨텍스트는 전체 코드베이스를 한 번에 처리할 수 있게 합니다. "Dev Team Mode"를 통해 자율적 서브 에이전트 생성이 가능합니다. 주요 타겟은 대량 API 호출, 에이전트 워크플로우, 비용 민감 프로젝트입니다.

**Opus 4.6: 새로운 정점?**

구체적 스펙은 미확인 상태입니다. 그러나 Anthropic의 패턴상, Opus 라인은 항상 "최고 성능"을 목표로 합니다.

Sonnet 5가 Opus 4.5를 넘어선다면, Opus 4.6은 그보다 더 높은 수준을 목표로 할 것입니다.

예상 타겟은 극한의 추론 능력이 필요한 연구, 미션 크리티컬 엔터프라이즈 작업입니다.

## 모범사례/대응 전략 비교

| 상황 | 권장 전략 | 근거 |
| --- | --- | --- |
| 현재 Opus 4.5 사용 중 | 유지, Sonnet 5 출시 시 A/B 테스트 | Sonnet 5가 더 저렴하고 성능 동등 이상 가능성 |
| 고비용 추론 작업 | Opus 4.6 출시 대기 | 최고 성능이 필요한 경우 새 플래그십 필요 |
| 대량 에이전트 운영 | Sonnet 5 즉시 전환 준비 | 비용 80% 절감 가능성 |
| 미확인 정보에 의존 불가 | 현재 모델로 계속 진행 | 공식 발표 전까지 모든 정보는 미검증 |

## 마치며

- Google Vertex AI 스캔 결과, Claude Sonnet 5와 Opus 4.6 모두 403 Forbidden으로 존재가 확인되었다.
- Sonnet 5 "Fennec"은 Opus 4.5 성능을 20% 가격에 제공할 가능성이 있으며, Opus 4.6은 새로운 최상위 모델로 추정된다.
- Anthropic은 공식 발표를 하지 않았으므로, 모든 스펙과 출시일은 미검증 상태다.
- 실전 팁: Anthropic 공식 블로그(anthropic.com/news)를 모니터링하고, 출시 즉시 `model` 파라미터만 변경하여 테스트할 수 있도록 코드를 준비해두세요.

## 참고자료

- Claude Sonnet 5 & Opus 4.6 Leak: The 403 Forbidden Proof - Marco Patzelt (<https://www.marc0.dev/en/blog/claude-sonnet-5-fennec-leak-what-the-vertex-ai-logs-actually-show-1770048662320>)
- Claude Opus 4.6 launching soon - DeepakNess (<https://deepakness.com/raw/opus-4-6-soon/>)
- Anthropic Fennec Leak Signals Imminent Launch - Dataconomy (<https://dataconomy.com/2026/02/04/anthropic-fennec-leak-signals-imminent-claude-sonnet-5-launch/>)
- Pankaj Kumar X Post on Double Drop (<https://x.com/pankajkumar_dev/status/2019055211164381649>)
- Anthropic 공식 뉴스 페이지 (<https://www.anthropic.com/news>)
