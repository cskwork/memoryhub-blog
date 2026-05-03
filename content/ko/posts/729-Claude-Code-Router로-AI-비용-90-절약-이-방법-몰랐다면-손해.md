---
title: "? Claude Code Router로 AI 비용 90% 절약, 이 방법 몰랐다면 손해!"
date: 2025-07-18T03:12:46+09:00
slug: "729-Claude-Code-Router로-AI-비용-90-절약-이-방법-몰랐다면-손해"
original_url: "https://memoryhub.tistory.com/729"
tistory_id: 729
draft: false
---

```
    ? Claude Code Router ?
         /     |     \
    OpenAI  DeepSeek  Gemini
       |       |       |
    [$$$]   [$$]    [$$$$]
       |       |       |
    Your Choice Based on Task
```

개발하다가 Claude API 요금 폭탄 맞아본 적 있나요? 저도 한 달에 수십만 원 나가는 걸 보고 깜짝 놀랐었는데, Claude

Code Router라는 신박한 도구를 발견했습니다.

같은 작업을 DeepSeek으로 라우팅해서 **비용을 90% 이상 절약**할 수 있다니, 이거 진짜 게임체인저네요. 특히 긴 코드 작업이나 반복 작업이 많다면 필수로 알아둬야 할 툴입니다.

⚡ **TL;DR**: Claude Code 요청을 여러 AI 모델로 자동 분배해서 비용 절약 + 성능 최적화가 가능한 라우터 도구. 설정 한 번으로 상황별 최적 모델 자동 선택!

## 목차

1. 배경 - 왜 AI 모델 라우팅이 필요할까?
2. 핵심 개념 정리 - Claude Code Router란?
3. 실습 - 설치부터 설정까지
4. 모범 사례 - 똑똑한 라우팅 전략
5. 마치며 & 참고자료

---

## 1. 배경 - 왜 AI 모델 라우팅이 필요할까?

AI 개발을 하다 보면 이런 고민에 부딪히죠:

**비용 문제**: Claude Max 같은 프리미엄 모델은 성능은 좋지만 토큰 비용이 비싸서, 간단한 작업에도 과도한 비용이 발생합니다.

**작업별 특성**: 코드 리뷰에는 정확성이, 아이디어 브레인스토밍에는 창의성이, 디버깅에는 논리적 추론이 더 중요하죠.

**컨텍스트 제한**: 긴 코드나 문서를 다룰 때 모델별로 처리 가능한 토큰 길이가 다릅니다.

✅ **주요 용어**

- **라우팅**: 요청을 적절한 모델로 자동 분배하는 과정
- **프로바이더**: OpenAI, DeepSeek, Gemini 등 AI 모델 제공 업체
- **트랜스포머**: 요청/응답을 각 API 형식에 맞게 변환하는 기능

## 2. 핵심 개념 정리

> **Claude Code Router**: Claude Code 요청을 다양한 모델로 라우팅하고 맞춤 설정할 수 있는 강력한 도구

사용자가 직접 라우팅 전략을 정의해 어떤 요청을 어떤 모델에 보낼지 세밀하게 설정할 수 있습니다. 예컨대, 배경 처리에는 경량 모델을, 고도 추론에는 DeepSeek Reasoner를, 긴 컨텍스트 처리에는 Gemini 2.5 Pro와 같은 모델을 사용하도록 분기할 수 있습니다.

**핵심 기능들**:

- 모델 라우팅: 필요에 따라 다른 모델로 요청 라우팅 (백그라운드 작업, 사고, 긴 컨텍스트 등)
- 다중 프로바이더 지원: OpenRouter, DeepSeek, Ollama, Gemini, Volcengine, SiliconFlow 등 다양한 모델 프로바이더 지원
- 동적 모델 전환: /model 명령어를 사용하여 Claude Code 내에서 실시간으로 모델 전환

## 3. 실습 - 설치부터 설정까지

### ① 기본 설치

먼저 Claude Code CLI가 설치되어 있어야 합니다:

```
# Claude Code CLI 설치
npm install -g @anthropic-ai/claude-code

# Claude Code Router 설치  
npm install -g @musistudio/claude-code-router
```

### ② 설정 파일 생성

`~/.claude-code-router/config.json` 파일을 생성하고 설정합니다:

```
{
  "APIKEY": "your-secret-key",
  "LOG": true,
  "Providers": [
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "sk-xxx",
      "models": ["deepseek-chat", "deepseek-reasoner"]
    },
    {
      "name": "openrouter", 
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-xxx",
      "models": ["anthropic/claude-3.5-sonnet", "google/gemini-2.5-pro"]
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "deepseek,deepseek-chat", 
    "think": "deepseek,deepseek-reasoner",
    "longContext": "openrouter,google/gemini-2.5-pro"
  }
}
```

### ③ 라우터 실행

```
# 라우터 시작
ccr code

# 또는 환경변수로 설정 후
export ANTHROPIC_BASE_URL="http://127.0.0.1:3456"
export ANTHROPIC_AUTH_TOKEN="test"
claude
```

이제 Claude Code를 평소처럼 사용하면 설정한 라우팅 규칙에 따라 자동으로 적절한 모델로 요청이 분배됩니다!

## 4. 모범 사례 - 똑똑한 라우팅 전략

| 작업 유형 | 추천 모델 | 이유 |
| --- | --- | --- |
| 일반 코딩 | DeepSeek Chat | 비용 효율적이면서도 코딩 성능 우수 |
| 복잡한 추론 | DeepSeek Reasoner | 추론 작업에 특화된 모델 |
| 긴 컨텍스트 | Gemini 2.5 Pro | 128K 컨텍스트로 긴 문서 처리 가능 |
| 백그라운드 작업 | Qwen2.5-Coder | 로컬에서 빠르고 무료 |

**실시간 모델 전환**도 가능합니다:

```
# Claude Code 실행 중에 모델 변경
/model openrouter,anthropic/claude-3.5-sonnet
/model deepseek,deepseek-reasoner
```

**비용 최적화 팁**:

- 단순 작업: DeepSeek Chat (토큰당 비용 최저)
- 창의적 작업: Claude 3.5 Sonnet
- 분석 작업: Gemini Pro (긴 컨텍스트 지원)

## 5. 마치며

Claude Code Router로 **작업 특성에 맞는 모델을 자동 선택**하니까 비용은 절약되고 성능은 더 좋아지더라고요. 특히 DeepSeek 통합으로 복잡한 AI 작업을 프리미엄 모델 대비 훨씬 저렴한 비용으로 수행할 수 있다는 점이 가장 인상적입니다.

개발팀에서 AI 도구 비용 때문에 고민이라면 꼭 한번 시도해보세요. JSON 설정 하나로 이런 유연성을 얻을 수 있다니 정말 혁신적입니다.

**실제 프로젝트 적용 팁**: 팀 전체 설정을 표준화해서 공유하면 모든 개발자가 동일한 비용 효율성을 누릴 수 있어요.

⸻

## 참고자료

- **공식 GitHub**: [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router)
- **Claude Code 공식 문서**: [Anthropic Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)
- **한국어 커뮤니티**: [파이토치 한국 사용자 모임 - Claude Code Router 소개](https://discuss.pytorch.kr/t/claude-code-router-llm-claude-code/7202)

---

## ? 기술 용어 해설 (어린이도 이해할 수 있게!)

**라우터**: 편지를 받아서 어느 집으로 배달할지 정하는 우체부 같은 역할. 여기서는 AI 요청을 어떤 모델에게 보낼지 정해주는 프로그램

**API**: 프로그램들이 서로 대화하는 방법. 마치 서로 다른 언어를 쓰는 친구들 사이의 번역기 같은 것

**토큰**: AI가 글자를 세는 단위. 한국어는 보통 글자 1개가 토큰 1~2개 정도

**프로바이더**: AI 모델을 만들어서 빌려주는 회사들. OpenAI, DeepSeek, Google 등이 있어요

**컨텍스트**: AI가 한 번에 기억할 수 있는 정보의 양. 사람도 한 번에 너무 많은 걸 기억하기 어렵죠?
