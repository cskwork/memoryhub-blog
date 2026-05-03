---
title: "? Gemini CLI v0.7.0, 개발자들이 주목하는 세 가지 킬러 기능"
date: 2025-10-03T08:58:38+09:00
slug: "822-Gemini-CLI-v0-7-0-개발자들이-주목하는-세-가지-킬러-기능"
original_url: "https://memoryhub.tistory.com/822"
tistory_id: 822
draft: false
---

```
    ____                _       _    ____ _     ___   
   / ___| ___ _ __ ___ (_)_ __ (_)  / ___| |   |_ _|  
  | |  _ / _ \ '_ ` _ \| | '_ \| | | |   | |    | |   
  | |_| |  __/ | | | | | | | | | | | |___| |___ | |   
   \____|\___|_| |_| |_|_|_| |_|_|  \____|_____|___|  

         v0.7.0 - 터미널에서 만나는 AI 혁신
```

2025년 10월 1일, Gemini CLI v0.7.0이 정식 출시되면서 개발자 커뮤니티가 들썩이고 있습니다. 저도 출시 소식을 듣자마자 바로 테스트에 돌입했는데요, 솔직히 말해서 이번 업데이트는 단순한 기능 추가가 아니었습니다.  
터미널에서 직접 이미지를 생성하고, TODO 리스트가 자동으로 관리되며, 커스텀 명령어를 스크립트처럼 연결할 수 있다면? 이 글을 읽는 5분 뒤, 여러분의 개발 워크플로우는 완전히 달라질 겁니다.

---

## 1. 배경: Gemini CLI가 주목받는 이유

Gemini CLI는 구글이 공개한 오픈소스 AI 에이전트로, 터미널에서 직접 Gemini 2.5 Pro 모델을 사용할 수 있는 도구입니다. 개인 구글 계정으로 분당 60회 요청, 하루 1,000회까지 무료로 사용할 수 있어 경제적 부담 없이 강력한 AI 기능을 활용할 수 있습니다.  

**✅ 핵심 용어 정리**

|  |  |
| --- | --- |
| MCP (Model Context Protocol) | AI 에이전트가 외부 도구와 통신하기 위한 표준 프로토콜 |
| Extension | 컨텍스트 파일, MCP 서버, 커스텀 명령을 패키징한 확장 기능 |
| Headless Mode | 비대화형 방식으로 CLI를 실행하여 자동화·CI/CD에 활용하는 모드 |

기존에는 코딩 작업에 집중되어 있었지만, v0.7.0부터는 이미지 생성, 작업 관리, 워크플로우 자동화까지 영역을 확장했습니다.

---

## 2. 핵심 기능 살펴보기

> **한 줄 정의**  
> **Gemini CLI v0.7.0은 터미널에서 이미지 생성, TODO 자동 관리, 커스텀 명령 체이닝을 가능하게 만든 통합 개발 환경입니다.**

### 2-1. Nano Banana 익스텐션: 터미널에서 이미지 생성

Nano Banana는 Gemini 2.5 Flash Image 모델의 별칭으로, 이미지 생성 및 편집에 특화되어 있습니다. 한 장의 사진을 업로드하면 여러 이미지를 조합하거나, 특정 부분만 수정하는 등 정교한 작업이 가능합니다.  

**설치 방법**

```
gemini extensions install https://github.com/gemini-cli-extensions/nanobanana
```

설치 후 `/generate`로 이미지를 생성하거나 `/edit`으로 기존 이미지를 편집할 수 있습니다. 문서에 나온 사례처럼 프로필 사진에 배경을 추가하거나 스타일을 변경하는 작업을 명령어 한 줄로 처리할 수 있습니다.

생성된 모든 이미지에는 SynthID 워터마크가 자동 삽입되어 AI 생성 이미지임을 명확히 표시합니다.

### 2-2. TODO 관리 (실험적 기능)

복잡한 작업을 진행할 때 Gemini CLI가 자동으로 TODO 리스트를 생성하고 진행 상황을 체크합니다. 현재는 실험 단계이므로 기본적으로 비활성화되어 있습니다.  

**활성화 방법**

`settings.json` 파일에 다음을 추가하세요.

```
{
  "useWriteTodos": true
}
```

이 기능은 멀티스텝 작업에서 각 단계를 명확히 구분하고, 완료된 항목과 진행 중인 항목을 실시간으로 표시합니다. 향후 업데이트에서는 색상이나 기호로 상태를 구분하거나, 현재 작업 전후 항목만 표시하는 등 개선이 예정되어 있습니다.

### 2-3. Headless 모드에서 커스텀 명령 실행

비대화형(Headless) 모드에서 커스텀 슬래시 명령을 호출할 수 있게 되면서 CI/CD 파이프라인이나 자동화 스크립트에 Gemini CLI를 통합하는 것이 가능해졌습니다.  

**커스텀 명령 체이닝 예제**

```
# ~/.gemini/commands/find-capital.toml
prompt="Please provide the capital city of {{args}}."

# ~/.gemini/commands/things-to-do.toml
prompt="Please provide fun things to do in the city of {{args}}."
```

```
gemini "/things-to-do $(gemini "/find-capital Estonia")"
```

이처럼 한 명령의 결과를 다음 명령의 입력으로 사용하여 복잡한 워크플로우를 구축할 수 있습니다. 여행 계획, 데이터 분석, 코드 리뷰 자동화 등 다양한 시나리오에 활용 가능합니다.

---

## 3. 실전 활용 시나리오

### ① 익스텐션 설치 및 이미지 편집

**단계**

1. Nano Banana 익스텐션 설치
2. `gemini extensions install https://github.com/gemini-cli-extensions/nanobanana`
3. 이미지 생성 또는 편집
4. `/generate A futuristic cityscape at sunset /edit headshot.jpg Add professional studio lighting`
5. 생성된 이미지는 현재 디렉토리에 자동 저장

캐릭터 일관성 유지 기능 덕분에 동일 인물이나 객체를 여러 장면에서 일관되게 표현할 수 있어, 브랜드 에셋이나 연속된 스토리텔링 작업에 유용합니다.

### ② TODO 기능으로 복잡한 프로젝트 관리

**시나리오: API 통합 작업**

1. settings.json에서 TODO 기능 활성화
2. Gemini CLI에 "Stripe 결제 API를 통합해줘"라고 요청
3. 자동으로 생성되는 작업 목록:
   - ✅ Stripe SDK 설치
   - ? API 키 환경변수 설정
   - ⏳ 결제 엔드포인트 구현
   - ⏳ 웹훅 핸들러 작성

각 단계가 완료될 때마다 자동으로 체크되어 진행 상황을 한눈에 파악할 수 있습니다.

### ③ 커스텀 명령 체인으로 워크플로우 자동화

**실제 사용 예: 코드 리뷰 자동화**

```
# PR 정보 추출 → 차이점 분석 → 리뷰 코멘트 생성
gemini "/review-pr $(gemini "/get-pr-diff PR-1234")"
```

Gemini CLI Code Review 익스텐션을 설치한 경우, 터미널을 실행하지 않고도 /code-review 명령을 바로 사용할 수 있습니다.

---

## 4. 모범 사례 및 주의사항

|  |  |  |
| --- | --- | --- |
| 익스텐션 활용 | 기능 확장이 쉽고 커뮤니티 공유 가능 | 신뢰할 수 있는 출처에서만 설치 |
| TODO 실험 기능 | 복잡한 작업의 구조화 및 추적 | 아직 실험 단계로 안정성 검증 필요 |
| Headless 체이닝 | CI/CD 통합 및 반복 작업 자동화 | 명령 간 의존성 관리에 주의 |
| 이미지 생성 | 디자인 프로토타입이나 콘텐츠 제작 시간 단축 | 워터마크가 삽입되므로 상업적 사용 전 확인 |

**추가 팁**  
Gemini CLI는 분당 60회 요청 무료 제공이지만, 대규모 프로젝트나 팀 단위 작업의 경우 Google AI Studio나 Vertex AI 키를 사용하는 것이 안정적입니다. 또한 MCP(Model Context Protocol) 지원을 통해 커스텀 도구를 손쉽게 통합할 수 있습니다.

---

## 5. 마치며

Gemini CLI v0.7.0은 세 가지 핵심 기능으로 요약됩니다.

1. **Nano Banana 익스텐션**으로 터미널에서 이미지 생성 및 편집
2. **TODO 자동 관리**로 멀티스텝 작업의 명확한 추적
3. **Headless 모드의 커스텀 명령 체이닝**으로 워크플로우 자동화

실제 프로젝트에 적용할 때는 먼저 간단한 커스텀 명령부터 시작하고, 익스텐션을 하나씩 추가하며 워크플로우를 점진적으로 개선하는 것을 추천합니다. 무료 사용 한도가 넉넉하므로 부담 없이 다양한 실험이 가능합니다.

---

**참고자료**

- Gemini CLI 공식 릴리스 노트: <https://github.com/google-gemini/gemini-cli/releases>
- Gemini CLI 공식 문서: <https://google-gemini.github.io/gemini-cli/>
- Gemini 2.5 Flash Image 소개 글: <https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/>
- Nano Banana 익스텐션 저장소: <https://github.com/gemini-cli-extensions/nanobanana>
