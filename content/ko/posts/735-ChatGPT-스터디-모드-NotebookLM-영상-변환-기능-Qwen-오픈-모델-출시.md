---
title: "ChatGPT 스터디 모드, NotebookLM 영상 변환 기능, Qwen 오픈 모델 출시"
date: 2025-07-30T05:46:11+09:00
slug: "735-ChatGPT-스터디-모드-NotebookLM-영상-변환-기능-Qwen-오픈-모델-출시"
original_url: "https://memoryhub.tistory.com/735"
tistory_id: 735
draft: false
---

**2025년 7월 29일 (한국 기준 30일) 오늘, AI 교육 분야에서 세 가지 중요한 발전이 있었습니다. ChatGPT는 '스터디 모드'로 교육자 역할을 강화했고, Google의 NotebookLM은 텍스트를 비디오로 변환하는 기능을 추가했으며, Alibaba의 Qwen3-30B-A3B-2507 소형 모델은 추론과 대화 모드를 자유롭게 전환할 수 있는 혁신적 기능을 선보였습니다.**

## ChatGPT 스터디 모드: AI가 개인 튜터가 되다

OpenAI는 2025년 7월 29일 ChatGPT에 '스터디 모드'를 공식 출시했습니다. 이 기능은 단순히 답을 제공하는 대신 학생들이 단계별로 문제를 해결하도록 안내합니다. 스터디 모드는 소크라테스식 교수법을 사용하여 학생들의 사고 과정을 자극하고, 직접적인 답변에 대한 의존도를 줄입니다.

**핵심 특징과 작동 원리**

스터디 모드를 활성화하면 ChatGPT는 학생의 목표와 실력 수준에 맞춰 조정된 가이드 질문을 제공합니다. 만약 학생이 직접적인 답을 요구하면, ChatGPT는 스스로 해결하는 것이 더 나은 학습 방법이라고 알려줍니다. 사용자는 대화 중 언제든지 스터디 모드를 켜거나 끌 수 있어 여전히 답변에 쉽게 접근할 수 있습니다.

**교육계의 반응과 의미**

Common Sense Media의 테스트에서 일반 ChatGPT에게 "To Kill a Mockingbird"에 대한 답변을 9학년 학생처럼 쓰라고 요청했을 때 그대로 따랐지만, 스터디 모드는 "직접 써드리지는 않겠지만 함께 해봅시다!"라고 응답했습니다. 이는 AI가 학생의 학습을 지원하되 대신 해주지는 않겠다는 명확한 철학을 보여줍니다.

## NotebookLM 비디오 오버뷰: 문서가 동영상으로 변신하다

Google은 같은 날 NotebookLM에 '비디오 오버뷰' 기능을 출시했습니다. 이 기능은 복잡한 문서, PDF, 이미지를 소화하기 쉬운 시각적 프레젠테이션으로 변환합니다. 기존 오디오 오버뷰의 시각적 대안으로, AI가 새로운 시각 자료를 생성하면서 업로드된 문서에서 이미지, 다이어그램, 인용구, 숫자를 가져와 내용을 설명합니다.

**기술적 혁신과 활용 가능성**

NotebookLM은 Gemini 2.5 Pro의 멀티모달 기능을 활용하여 사용자가 업로드한 PDF, 이미지, 텍스트, 웹페이지, YouTube 동영상을 직관적인 요약과 설명을 위한 애니메이션 단편으로 변환합니다. 최대 50개의 소스(소스당 최대 500,000단어)를 분석하여 5-15분 길이의 단편을 생성할 수 있으며, 만화 스타일의 시각 효과, 동적 텍스트, AI 나레이션 설명이 포함됩니다.

**실제 성능과 한계**

AIbase의 테스트에 따르면 100페이지 PDF를 업로드했을 때 5분 만에 10분짜리 동영상을 생성할 수 있으며, 핵심 개념, 차트 분석, 인용을 포함하여 90%의 정확도를 보였습니다. 현재는 영어만 지원하지만 다른 언어 지원이 예정되어 있습니다.

## Qwen3-30B-A3B-2507: 사고와 대화를 자유롭게 전환하는 AI

Alibaba Cloud의 Qwen 팀이 개발한 Qwen3-30B-A3B-2507은 총 300억 개의 파라미터를 가진 MoE(Mixture of Experts) 모델로, 실제로는 30억 개의 파라미터만 활성화됩니다. 이 모델의 가장 큰 특징은 복잡한 논리적 추론, 수학, 코딩을 위한 '사고 모드'와 효율적인 일반 목적 대화를 위한 '비사고 모드' 간의 원활한 전환을 지원한다는 것입니다.

**성능과 효율성**

작은 MoE 모델인 Qwen3-30B-A3B는 10배 많은 활성 파라미터를 가진 QwQ-32B를 능가하며, Qwen3-4B 같은 작은 모델도 Qwen2.5-72B-Instruct의 성능에 맞먹습니다. 사고 모델은 온도 0.6, top\_p 0.95를 사용하고, 지시 모델은 온도 0.7, top\_p 0.8을 사용하는 등 서로 다른 설정을 최적화했습니다.

**오픈소스 접근성**

두 개의 MoE 모델과 6개의 밀집 모델이 Apache 2.0 라이센스 하에 오픈소스로 제공되어 연구자, 개발자, 조직이 최첨단 모델을 활용한 혁신적 솔루션을 구축할 수 있습니다.

## 장기적 영향과 교육의 미래

이 세 가지 기술은 AI 교육의 새로운 패러다임을 제시합니다. **개인화된 학습 경험**이 핵심 키워드로 떠오르고 있으며, AI가 단순한 답변 제공자에서 진정한 학습 파트너로 진화하고 있습니다.

**교육 형평성 측면에서** 이러한 기술들은 양날의 검입니다. 고가의 개인 튜터를 대체할 수 있는 접근성을 제공하지만, 동시에 정확하지 않은 정보를 제공할 위험도 있습니다. 학생들이 여전히 일반 모드로 쉽게 전환할 수 있다는 점은 '스마트한 부정행위'의 새로운 형태를 만들 수 있습니다.

## 교육자와 학습자를 위한 실용적 대안

이러한 기술 트렌드에 대응하기 위한 세 가지 전략을 제안합니다:

• **점진적 도입**: 기존 교육 방식을 완전히 대체하기보다는 보완적 도구로 활용하며, 학생들의 비판적 사고 능력 개발에 초점을 맞춘 커리큘럼 설계

• **윤리적 사용 교육**: AI 도구의 적절한 사용법과 한계에 대한 체계적 교육을 통해 학습자가 스스로 판단할 수 있는 능력 배양

• **평가 방식 혁신**: 단순 암기나 정답 도출보다는 사고 과정과 창의적 문제 해결 능력을 평가하는 새로운 시스템 구축

## 기술 용어 해설 (어린이도 이해할 수 있게)

**소크라테스식 교수법**: 선생님이 바로 답을 가르쳐주는 대신 질문을 통해 학생이 스스로 답을 찾아가도록 도와주는 방법입니다. 마치 수수께끼를 풀 때 힌트를 조금씩 주는 것과 같아요.

**MoE (Mixture of Experts)**: 여러 명의 전문가가 각자 잘하는 분야만 담당하는 것처럼, AI 모델의 일부분만 활성화시켜 효율적으로 작동하게 하는 기술입니다.

**멀티모달**: 텍스트뿐만 아니라 그림, 음성, 동영상 등 여러 종류의 정보를 동시에 이해하고 처리할 수 있는 능력을 말합니다.

**파라미터**: AI가 학습한 정보를 저장하는 단위로, 숫자가 클수록 더 많은 지식을 가지고 있다고 볼 수 있습니다. 사람의 뇌세포 연결과 비슷한 개념입니다.

#### 참고

- <https://openai.com/ko-KR/index/chatgpt-study-mode/>

- <https://blog.google/technology/google-labs/notebooklm-video-overviews-studio-upgrades/>

[What’s new in NotebookLM: Video Overviews and an upgraded Studio

NotebookLM launches Video Overviews and upgrades to the Studio panel.

blog.google](https://blog.google/technology/google-labs/notebooklm-video-overviews-studio-upgrades/)

- <https://docs.unsloth.ai/basics/qwen3-2507>

[Qwen3-2507 | Unsloth Documentation

Run Qwen3-30B-A3B-Instruct-2507 and both 235B-A22B Thinking and Instruct versions locally on your device!

docs.unsloth.ai](https://docs.unsloth.ai/basics/qwen3-2507)

- <https://www.techi.com/openai-adds-study-mode-to-chatgpt/>

[OpenAI Adds Study Mode to ChatGPT for Smarter Student Use

OpenAI’s ChatGPT now features Study Mode, guiding students to think critically by prompting logic and reducing over-reliance on direct AI answers.

www.techi.com](https://www.techi.com/openai-adds-study-mode-to-chatgpt/)
