---
title: "? Gemini 3 Flash Agentic Vision, AI가 이미지를 '조사'하는 방식이 달라졌다"
date: 2026-01-29T16:15:42+09:00
slug: "995-Gemini-3-Flash-Agentic-Vision-AI가-이미지를-조사-하는-방식이-달라졌다"
original_url: "https://memoryhub.tistory.com/995"
tistory_id: 995
draft: false
---

```
    ╔═══════════════════════════════════════════════════════╗
    ║                                                       ║
    ║      ┌─────────┐                                      ║
    ║      │  IMAGE  │──────► THINK ──► ACT ──► OBSERVE    ║
    ║      └─────────┘           │        │         │       ║
    ║           ▲                └────────┴─────────┘       ║
    ║           │                         │                 ║
    ║           └─────────────────────────┘                 ║
    ║                    (Loop)                             ║
    ║                                                       ║
    ║         GEMINI 3 FLASH - AGENTIC VISION              ║
    ║                                                       ║
    ╚═══════════════════════════════════════════════════════╝
```

AI에게 미세한 글씨가 적힌 이미지를 보여준 적이 있는가. 대부분의 AI는 한 번 흘끗 보고 답변한다.

문제는 작은 일련번호나 멀리 있는 표지판처럼 세밀한 정보를 놓치면, AI가 추측에 의존한다는 점이다.

Google이 2026년 1월 27일 발표한 Gemini 3 Flash의 Agentic Vision은 이 문제를 정면으로 해결한다.

**AI가 이미지를 '한 번 보기'에서 '능동적으로 조사하기'로 전환하는 기술**이다.

**한줄요약:** 결론부터 말하면, Agentic Vision은 코드 실행을 통해 이미지를 확대, 조작, 분석하며 시각적 증거에 기반한 답변을 제공하는 새로운 AI 비전 패러다임이다.

## 배경

기존 멀티모달 AI 모델들은 이미지를 정적으로 처리한다. 사진 한 장을 받으면 단 한 번의 추론으로 답변을 생성한다.

사람이 문서를 대충 훑어보고 답하는 것과 비슷하다.

> Agentic Vision: 이미지 이해를 정적 행위에서 능동적 조사 과정으로 전환하는 기술

이 방식의 한계는 명확하다. 마이크로칩의 일련번호, 고해상도 건축 도면의 세부 사항, 멀리 있는 도로 표지판처럼 세밀한 정보가 필요할 때 모델은 추측에 의존할 수밖에 없다. Agentic Vision은 이 문제를 해결하기 위해 **시각적 추론과 코드 실행을 결합**한다.

돋보기로 문서를 꼼꼼히 살피듯, AI가 이미지를 단계적으로 조사한다.

Google에 따르면 Gemini 3 Flash에서 코드 실행을 활성화하면 대부분의 비전 벤치마크에서 **5-10%의 품질 향상**을 달성한다.

## 핵심 원리: Think-Act-Observe 루프

Agentic Vision은 세 단계의 반복 루프로 작동한다.

**Think 단계**에서 모델은 사용자 질문과 이미지를 분석하여 다단계 계획을 수립한다. 단순히 "이 이미지에 뭐가 있지?"가 아니라 "어떤 부분을 확대해야 하는가?", "어떤 처리가 필요한가?"를 판단한다.

**Act 단계**에서 모델은 Python 코드를 생성하고 실행한다. 이미지 자르기, 회전, 주석 추가 같은 조작이나 계산, 바운딩 박스 카운팅 같은 분석 작업을 수행한다. 중요한 점은 이 코드가 결정론적 환경에서 실행된다는 것이다. 확률적 추측이 아닌 검증 가능한 실행 결과를 얻는다.

**Observe 단계**에서 변환된 이미지가 모델의 컨텍스트 윈도우에 추가된다. 모델은 새로운 데이터를 더 나은 맥락에서 검토한 후 최종 응답을 생성한다.

이 루프는 필요에 따라 여러 번 반복될 수 있다. 한 번의 확대로 부족하면 다시 확대하고, 추가 분석이 필요하면 다시 코드를 실행한다.

## 실제 활용 사례

Agentic Vision의 실제 적용 사례는 이 기술의 가치를 명확히 보여준다.

**고해상도 이미지 검사**에서 건축 도면 검증 플랫폼 PlanCheckSolver.com은 이 기능을 도입해 정확도를 5% 향상시켰다. 모델이 지붕 가장자리나 건물 섹션 같은 특정 영역을 반복적으로 잘라내고 분석하여 복잡한 건축 법규 준수 여부를 확인한다.

**이미지 주석 달기**에서 Gemini 앱은 손가락 개수를 세는 작업에 이 기능을 활용한다. 모델이 각 손가락에 바운딩 박스와 숫자 레이블을 직접 그려넣는다. 이 "시각적 메모장"이 픽셀 단위의 정확한 이해를 보장한다.

**시각적 수학과 차트 생성**에서 기존 AI 모델들은 다단계 시각적 산술에서 종종 할루시네이션을 일으킨다.

Agentic Vision은 계산을 결정론적 Python 환경에 위임하여 이 문제를 우회한다. 표에서 원시 데이터를 식별하고,

정규화 코드를 작성하고,

Matplotlib 차트를 생성하는 전 과정이 검증 가능한 실행으로 이루어진다.

## 시작하는 방법

| 사용 환경 | 접근 방법 | 비고 |
| --- | --- | --- |
| Gemini API | Google AI Studio 또는 Vertex AI에서 Code Execution 활성화 | 개발자용 |
| Gemini 앱 | 모델 드롭다운에서 Thinking 선택 | 일반 사용자용 |
| 데모 앱 | Google AI Studio 내 데모 앱 직접 체험 | 기능 테스트용 |

개발자라면 AI Studio Playground에서 Tools 아래 Code Execution을 켜는 것만으로 이 기능을 실험할 수 있다.

## 마치며

- Agentic Vision은 AI 비전을 정적 처리에서 능동적 조사로 전환하는 패러다임 변화다
- Think-Act-Observe 루프와 코드 실행의 결합이 5-10%의 품질 향상을 가져온다
- 고해상도 검사, 이미지 주석, 시각적 계산 등 정밀도가 필요한 작업에서 진가를 발휘한다
- 실전 팁: Google AI Studio에서 Code Execution을 활성화하고 복잡한 이미지 분석 작업을 테스트해보세요.

## 참고자료

- Introducing Agentic Vision in Gemini 3 Flash (<https://blog.google/innovation-and-ai/technology/developers-tools/agentic-vision-gemini-3-flash/>)
- Gemini API Code Execution 문서 (<https://ai.google.dev/gemini-api/docs/code-execution#images>)
- Google AI Studio 데모 앱 (<https://aistudio.google.com/apps/bundled/gemini_visual_thinking>)
