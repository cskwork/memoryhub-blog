---
title: "? DBeaver에서도 AI Chat? “가능합니다.” 다만 에디션·보안 설정이 핵심!"
date: 2025-09-01T10:21:09+09:00
slug: "771-DBeaver에서도-AI-Chat-가능합니다-다만-에디션-보안-설정이-핵심"
original_url: "https://memoryhub.tistory.com/771"
tistory_id: 771
draft: false
categories: ["생활"]
tags: ["트렌드"]
cover:
  image: "images/771-DBeaver%EC%97%90%EC%84%9C%EB%8F%84-AI-Chat-%EA%B0%80%EB%8A%A5%ED%95%A9%EB%8B%88%EB%8B%A4-%EB%8B%A4%EB%A7%8C-%EC%97%90%EB%94%94%EC%85%98-%EB%B3%B4%EC%95%88-%EC%84%A4%EC%A0%95%EC%9D%B4-%ED%95%B5%EC%8B%AC/img.png"
  relative: false
  hidden: false
---

안녕하세요. DBeaver에 AI를 붙여 **자연어→SQL 생성, 쿼리 설명/리팩터링**까지 할 수 있습니다. OpenAI·Azure OpenAI·Google Gemini·GitHub Copilot·Ollama(로컬 LLM) 등 여러 모델을 연결할 수 있어요. 

![](/images/771-DBeaver%EC%97%90%EC%84%9C%EB%8F%84-AI-Chat-%EA%B0%80%EB%8A%A5%ED%95%A9%EB%8B%88%EB%8B%A4-%EB%8B%A4%EB%A7%8C-%EC%97%90%EB%94%94%EC%85%98-%EB%B3%B4%EC%95%88-%EC%84%A4%EC%A0%95%EC%9D%B4-%ED%95%B5%EC%8B%AC/img.png)

---

## **? 무엇이 되나요? (간단 기능 맵)**

- **자연어 → SQL**: “최근 7일 주문만” 같은 문장을 SQL로 변환
- **쿼리 설명/리팩터링**: 긴 SQL을 단계별로 해석·개선
- **AI Chat 창**: 대화형으로 질의·미리보기·실행 전 확인(25.2부터 쿼리 미리보기/확인 추가)
- **로컬/온프렘도 OK**: **Ollama** 연결 가능, 25.2부터 **Custom OpenAI Base URL**도 지원 → 사내용 게이트웨이/프록시에 유리

---

## **? 에디션별 차이 (중요)**

**에디션****AI Smart Completion(자연어→SQL 팝업)****AI Chat(대화형 창)****샘플데이터 전송 옵션**

|  |  |  |  |
| --- | --- | --- | --- |
| **Community** | **지원** (툴바 아이콘으로 실행) | 미지원 | 미지원 |
| **Lite / Enterprise / Ultimate / Team** | 지원 | **지원** | **지원** |

- **Community**는 “AI Smart Completion” 중심이며, **프로 에디션**(Lite/Enterprise/Ultimate/Team)에서 **AI Chat**과 샘플데이터 전송 기능이 열립니다.
- 2025.07 이후 **Community 설치본에 AI 통합이 동봉**되었지만, 환경에 따라 **AI 확장 설치**가 필요할 수 있습니다(뉴스/릴리스 노트 기준).

![](/images/771-DBeaver%EC%97%90%EC%84%9C%EB%8F%84-AI-Chat-%EA%B0%80%EB%8A%A5%ED%95%A9%EB%8B%88%EB%8B%A4-%EB%8B%A4%EB%A7%8C-%EC%97%90%EB%94%94%EC%85%98-%EB%B3%B4%EC%95%88-%EC%84%A4%EC%A0%95%EC%9D%B4-%ED%95%B5%EC%8B%AC/img_1.png)

---

## **⚙️ 설정 3단계 (가장 빠른 길)**

1. **메뉴**: Window → Preferences → General → AI 이동 → **Enable AI integration** 체크
2. **Provider 선택**: OpenAI / Azure OpenAI / Gemini / Copilot / Ollama 중 선택. OpenAI, Copilot 이외 Provider는 현재 유로 에디션에서만 사용 가능.
3. **키 입력**: 서비스 키(API token) 저장 → SQL 에디터에서 **@ai** 또는 **AI 아이콘**으로 호출
4. (프로판이면 툴바의 **AI Chat** 아이콘으로 대화창 열기)

---

## **? 보안·프라이버시 체크리스트 (현실적으로 설정하기)**

DBeaver는 정확도를 높이기 위해 \*\*메타데이터(테이블/컬럼명, 데이터타입, FK 등)\*\*를 AI로 보낼 수 있고, 프로판에서는 **일부 샘플데이터 행**도 전송 가능합니다. 각 항목은 **ON/OFF 토글**이 있어서 최소화할 수 있어요. 

- **AI 설정 위치**: Preferences → General → AI
  - *Send database structure / column data types / object descriptions / foreign keys* 등 **전송 항목을 개별 제어**
  - *Sample data*와 **행 수**는 **프로 에디션에서만** 제공 → 기본 **OFF 추천**
- **스코프 좁히기**: AI가 참조할 **스키마/테이블 범위를 제한**(Scope)하면 불필요한 메타데이터 전송과 토큰 소모를 줄입니다.
- **위험 쿼리 방지**: **AI가 생성한 파괴적 쿼리 실행 전 확인 팝업**(위험 쿼리 컨펌)이 추가되었습니다(버전 릴리스 로그).
- **완전 비활성화**: 필요 시 AI 통합 자체를 끌 수 있습니다. Preferences → General → AI → Disable
- **정책 유의**: 일부 유료 플랜은 **서드파티 앱 사용을 제한**할 수 있으니 약관을 확인하세요.

---

## **??‍? 실제로 써보는 예시 프롬프트**

- **생성**: @ai 지난 7일간 신규 결제 고객 수, 일자별 카운트
- **설명**: 긴 SQL 붙여넣고 → “한 줄씩 설명해 줘. 실행 계획도 요약.”
- **리팩터링**: “CTE로 나눠서 가독성↑, 윈도우 함수로 재작성”
- **검증**: “같은 의미를 더 빠르게. 인덱스 후보도 제안.”
- (@ai 호출과 동작 튜토리얼 예시는 실사용 후기 글 기준)

---

## **? 문제 예방/해결 팁**

- **커뮤니티에서 AI가 안 보임**: AI 확장/통합 상태 확인(버전에 따라 **확장 설치 필요**).
- **메타데이터 과다 전송 느낌**: **Scope**를 좁히고 전송 항목(특히 Object descriptions/Types)과 **샘플데이터 OFF**로 조정. 관련 이슈 리포트도 있었습니다.
- **사내망/온프렘 모델**: **Ollama**로 로컬 모델 연결 또는 **Custom Base URL**에 내부 프록시를 설정.

---

## **? 요약 가이드(한 장)**

**추천 기본 세팅**

1. Provider: 회사 정책에 맞는 모델 선택(가능하면 **Ollama/사내용 게이트웨이** 고려)
2. 전송 항목: **Structure 최소 + Sample Data OFF**
3. Scope: **작업 스키마·테이블만 지정**
4. 실행 전: **AI 쿼리 확인 팝업** 켜기(릴리스 추가 기능)

**용도별 팁**

- 학습/초보: **Smart Completion**로 간단 쿼리부터
- 팀/프로덕션: **프로 에디션 + Chat**으로 표준 프롬프트/리팩터링 템플릿화

---

## **? (부록) 빠른 메뉴 경로**

- **AI 통합 켜기/키 입력**: Window → Preferences → General → AI
- **AI Chat 열기(프로)**: 툴바 **AI Chat** 아이콘 → 창에서 질의/미리보기/실행
- **Smart Completion(커뮤니티)**: SQL Editor 좌측 **AI 아이콘 → Translate**
- **AI 완전 끄기**: Preferences → General → AI → Disable

---

*“DBeaver의 AI는 강력하지만,* ***에디션·스코프·전송 항목****만 잘 다루면 안전하고 효율적으로 쓸 수 있습니다!”*

![](/images/771-DBeaver%EC%97%90%EC%84%9C%EB%8F%84-AI-Chat-%EA%B0%80%EB%8A%A5%ED%95%A9%EB%8B%88%EB%8B%A4-%EB%8B%A4%EB%A7%8C-%EC%97%90%EB%94%94%EC%85%98-%EB%B3%B4%EC%95%88-%EC%84%A4%EC%A0%95%EC%9D%B4-%ED%95%B5%EC%8B%AC/img_2.png)

## 참고

<https://dbeaver.com/docs/dbeaver/AI-Smart-Assistance/#data-privacy>
