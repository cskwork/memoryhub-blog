---
title: "‘나노바나나’ = Gemini 2.5 Flash Image"
date: 2025-08-27T08:54:56+09:00
slug: "766-나노바나나-Gemini-2-5-Flash-Image"
original_url: "https://memoryhub.tistory.com/766"
tistory_id: 766
draft: false
categories: ["데브 컨셉"]
tags: ["Tech News"]
cover:
  image: "images/766-%EB%82%98%EB%85%B8%EB%B0%94%EB%82%98%EB%82%98-Gemini-2-5-Flash-Image/img.png"
  relative: false
  hidden: false
---

![](/images/766-%EB%82%98%EB%85%B8%EB%B0%94%EB%82%98%EB%82%98-Gemini-2-5-Flash-Image/img.png)

오늘(한국시간 8월 27일) 공개된 **Gemini 2.5 Flash Image(일명 ‘나노바나나’)** 는 이미지 **생성+편집**을 한 번에 처리하고, **캐릭터 일관성·부분 편집·다중 이미지 합성**을 강화한 구글의 최신 모델입니다. 개발자는 **AI Studio/Vertex/ Gemini API**에서 즉시 쓸 수 있고, **이미지 1장 ≈ $0.039** 입니다. 

---

## **핵심 기능**

- **공식 공개 & 모델명**: *Gemini 2.5 Flash Image* (커뮤니티 별칭: **나노바나나**).
- **핵심 기능 4가지**
  1. **캐릭터 일관성**: 같은 인물을 다양한 장면·각도에서 유지
  2. **프롬프트 기반 부분 편집**: 배경 블러/얼룩 제거/자세 변경 등 국소 수정
  3. **다중 이미지 합성**: 여러 이미지를 하나로 자연스럽게 융합
  4. **세계지식 활용**: 손그림/도식 이해, 교육용 설명 등 의미기반 편집

→ 모두 개발자 블로그에 공식 예시와 템플릿이 제공됩니다. 

- **제공 채널 & 상태**: **Gemini API**·**Google AI Studio**(개발자), **Vertex AI**(엔터프라이즈). 현재 **Preview**로 제공되며 안정화가 예고되어 있습니다. 모델 ID 예: gemini-2.5-flash-image-preview.
- **가격**: **출력 100만 토큰당 $30 → 이미지 1장당 약 1,290 토큰 ≈ $0.039**. (대략 $1로 약 25장 수준)
- **워터마킹**: 생성/편집된 모든 이미지에 **SynthID** 보이지 않는 워터마크 삽입.

![](/images/766-%EB%82%98%EB%85%B8%EB%B0%94%EB%82%98%EB%82%98-Gemini-2-5-Flash-Image/blob.jpg)

---

## **바로 써보기 (3단계)**

1. **Google AI Studio 접속** → 모델을 \*\*Gemini 2.5 Flash Image (preview)\*\*로 선택.
2. **프롬프트 작성** → 필요하면 원본 이미지를 업로드(부분 편집·합성).
3. **결과 확인 & 재프롬프트** → 캐릭터 유지·색감·배경만 재지시해 세밀 조정.

> 빠른 테스트는 AI Studio의 \*\*템플릿 앱(사진 편집/캐릭터 일관성/다중 합성)\*\*에서 시작하면 편합니다. 

## **추천 프롬프트 예시**

- “**인물은 그대로** 두고 **배경을 카페 내부**로 바꿔줘. 자연광 느낌으로.”
- “이 두 사진을 합쳐 **제품 A를 사진 B의 책상 위**에 자연스럽게 올려줘. 그림자도 맞춰.”
- “**캐릭터는 동일**하게 유지하고, **봄/여름/가을/겨울** 분위기의 포스터 4종으로 만들어줘.”
- “흑백 가족사진에 **자연스런 컬러**를 입히고 **얼룩을 제거**해줘.”

---

## **가격·접근 요약표**

**항목****내용**

|  |  |
| --- | --- |
| 모델명 | Gemini 2.5 Flash Image *(aka ‘나노바나나’)* |
| 상태 | 프리뷰(Preview) – 곧 안정화 예정 |
| 이용 경로 | Gemini API / Google AI Studio / Vertex AI |
| 과금 | 출력 100만 토큰 $30 |
| 1장 비용 | **약 1,290 토큰 ≈ $0.039/장** (1024x1024 기준) |
| 워터마크 | **SynthID** 보이지 않는 워터마크 자동 삽입 |

---

## **어디에 좋을까**

- **브랜드/마케팅**: 캐릭터·제품 **일관성** 유지한 다변량 시각물 빠른 생산.
- **커머스**: **다중 이미지 합성**으로 배경 변경·제품 배치·톡톡한 소재 합성 컷.
- **교육/설명**: 손그림·도식 이해 → **설명 이미지** 자동 보완/편집.

> 참고: 일부 미디어·크리에이티브 툴은 **통합 지원**을 발표했습니다(예: Adobe Firefly/Express 연계). 워크플로우에 맞춰 선택하세요. 

---

## **실전 팁 (퀄리티/속도 모두 챙기기)**

- **역할 지시 + 스타일 + 제약**을 함께 적기: “아트디렉터처럼… / 잡지 표지 스타일 / 피부 텍스처는 자연스럽게”
- **리롤보다 부분편집**: 전체 재생성보다 **영역 지정·국소 수정** 지시가 효율적.
- **자료 한 번에 제공**: 합성은 원본들을 한 요청에 넣고 **광원/시점/색온도**를 명시.
- **정책·표시 의무 확인**: SynthID 워터마크가 삽입되며, 배포 시 출처·표시 가이드를 팀 정책에 맞춰 정하세요.

## **간단 Q&A**

**Q. 무료인가요?**

A. API/클라우드 과금 기준은 위 표와 같습니다. AI Studio의 체험은 시점·정책에 따라 달라질 수 있으니 콘솔 내 가격 안내를 확인하세요. 

**Q. 모델 코드는?**

A. *AI Studio 예시*로 gemini-2.5-flash-image-preview 가 노출됩니다. 

**Q. 오늘 공개가 맞나요?**

A. 구글 개발자 블로그 게시(현지 8/26) 및 공식 릴리즈 노트(8/26)가 확인됩니다. 한국 기준 8/27에 해당합니다. 

---

> **결론:** *나노바나나는 ‘빠르고 정확한 이미지 생성·편집’을 한 덩어리로 묶은 실전형 모델—오늘부터 바로 써먹자!* ?

![](/images/766-%EB%82%98%EB%85%B8%EB%B0%94%EB%82%98%EB%82%98-Gemini-2-5-Flash-Image/Image.jpeg)

<https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/>

[Introducing Gemini 2.5 Flash Image, our state-of-the-art image model- Google Developers Blog

Today, we’re excited to introduce Gemini 2.5 Flash Image (aka nano-banana), our state-of-the-art image generation and editing model. This update enables you to blend multiple images into a single image, maintain character consistency for rich storytellin

developers.googleblog.com](https://developers.googleblog.com/en/introducing-gemini-2-5-flash-image/)
