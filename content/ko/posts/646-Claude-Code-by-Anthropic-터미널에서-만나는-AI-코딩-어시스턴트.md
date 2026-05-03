---
title: "Claude Code by Anthropic - 터미널에서 만나는 AI 코딩 어시스턴트 ?"
date: 2025-06-04T17:59:43+09:00
slug: "646-Claude-Code-by-Anthropic-터미널에서-만나는-AI-코딩-어시스턴트"
original_url: "https://memoryhub.tistory.com/646"
tistory_id: 646
draft: false
categories: ["데브 언어"]
tags: ["Vibe Coding"]
cover:
  image: "images/646-Claude-Code-by-Anthropic-%ED%84%B0%EB%AF%B8%EB%84%90%EC%97%90%EC%84%9C-%EB%A7%8C%EB%82%98%EB%8A%94-AI-%EC%BD%94%EB%94%A9-%EC%96%B4%EC%8B%9C%EC%8A%A4%ED%84%B4%ED%8A%B8/img.png"
  relative: false
  hidden: false
---

![](/images/646-Claude-Code-by-Anthropic-%ED%84%B0%EB%AF%B8%EB%84%90%EC%97%90%EC%84%9C-%EB%A7%8C%EB%82%98%EB%8A%94-AI-%EC%BD%94%EB%94%A9-%EC%96%B4%EC%8B%9C%EC%8A%A4%ED%84%B4%ED%8A%B8/img.png)

여러분, 코딩하다가 "아, 이 함수가 뭐하는 거였지?" 하면서 파일 이리저리 뒤적이신 적 있으신가요? 아니면 GitHub 이슈 하나 해결하는데 터미널, IDE, 브라우저 창을 번갈아가며 열어둔 채로 작업하신 적은요? 오늘은 이런 고민을 한 방에 해결해주는 Anthropic의 Claude Code에 대해 알아보겠습니다!

## 등장 배경

예전에는 개발자들이 코드를 작성할 때 모든 것을 수동으로 처리해야 했습니다. 파일 검색, 디버깅, 리팩토링, 문서화... 모든 작업이 개발자의 손을 거쳐야 했죠. 그러다가 GitHub Copilot 같은 AI 코딩 어시스턴트가 등장하면서 상황이 조금씩 바뀌기 시작했습니다.

하지만 기존 도구들은 주로 IDE 내부에서만 작동하거나, 단순히 코드 자동완성 수준에 머물렀습니다. 개발자들은 여전히 여러 도구를 오가며 작업해야 했고, 복잡한 작업 흐름을 자동화하기 어려웠죠.

그래서 Anthropic은 완전히 새로운 접근을 시도했습니다. "터미널에서 직접 실행되는 AI 에이전트"라는 컨셉으로 Claude Code를 만든 거죠! 2025년 5월 22일에 정식 출시된 이 도구는 개발자들의 작업 방식을 근본적으로 바꾸고 있습니다.

**Claude Code가 해결하는 문제들**:

1. **컨텍스트 스위칭 문제**: 터미널, IDE, 브라우저를 오가며 작업하는 번거로움을 없애줍니다
2. **대규모 코드베이스 탐색**: 수백만 줄의 코드를 순식간에 이해하고 분석할 수 있습니다
3. **반복적인 작업 자동화**: 테스트 실행, 커밋, PR 생성 등을 자연어 명령으로 처리합니다

## 핵심 원리

Claude Code의 작동 방식을 시각적으로 표현하면 다음과 같습니다:

```
┌─────────────────────────────────────────────────┐
│              개발자의 터미널                      │
│                                                 │
│  $ claude "이 함수를 리팩토링해줘"               │
│       ↓                                         │
│  ┌─────────────┐                               │
│  │ Claude Code │ ←→ [로컬 파일시스템]          │
│  └─────────────┘                               │
│       ↓                                         │
│  ┌─────────────────────────────┐               │
│  │  Claude Opus 4 모델 (API)    │               │
│  └─────────────────────────────┘               │
│       ↓                                         │
│  [코드 분석 → 계획 수립 → 실행]                 │
│       ↓                                         │
│  ✅ 작업 완료!                                  │
└─────────────────────────────────────────────────┘
```

### 주요 기능 비교

기능 기존 도구 (Cursor, Copilot) Claude Code

|  |  |  |
| --- | --- | --- |
| 실행 환경 | IDE 내부 | 터미널 직접 실행 |
| 코드베이스 이해 | 제한적 (열린 파일 위주) | 전체 프로젝트 자동 매핑 |
| 작업 자동화 | 코드 생성 중심 | Git, 테스트, 빌드 등 전체 워크플로우 |
| 확장성 | IDE 플러그인 의존 | MCP 서버로 무한 확장 가능 |
| 백그라운드 실행 | 불가능 | GitHub Actions 연동으로 가능 |

### 실제 사용 예시

```
# 설치
npm install -g @anthropic/claude-code

# 프로젝트 디렉토리로 이동
cd my-project

# Claude Code 시작
claude

# 자연어로 명령하기
> "README.md 파일을 분석하고 프로젝트 구조를 설명해줘"
> "auth 모듈의 모든 타입 에러를 수정해줘"
> "이 이슈를 해결하고 PR을 만들어줘: #1234"
> "테스트를 실행하고 실패한 것들을 수정해줘"
```

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **파일 변경 권한 확인하기**
   - Claude Code는 파일을 직접 수정할 수 있습니다
   - 중요한 작업 전에는 반드시 Git으로 백업하세요
   - --no-auto-accept 플래그로 자동 수정을 막을 수 있습니다
2. **API 사용량 모니터링**
   - Claude Code는 API 토큰을 소비합니다
   - 대규모 작업 시 비용이 발생할 수 있으니 주의하세요
   - 프롬프트 캐싱으로 최대 90% 비용 절감 가능합니다

? **꿀팁**

- /clear 명령어로 컨텍스트를 자주 초기화하세요
- 복잡한 작업은 마크다운 체크리스트로 관리하면 효율적입니다
- .claude/commands 폴더에 자주 쓰는 명령을 저장할 수 있습니다
- MCP 서버를 활용하면 Puppeteer, Sentry 등 외부 도구와 연동 가능합니다

## 마치며

지금까지 Claude Code에 대해 알아보았습니다. 처음에는 "터미널에서 AI랑 대화한다고?" 하고 낯설게 느껴질 수 있지만, 한 번 써보면 그 강력함에 놀라실 거예요! 특히 반복적인 작업이 많거나 대규모 코드베이스를 다루는 개발자분들에게는 정말 혁신적인 도구가 될 것 같습니다.

여러분도 Claude Code로 10배 더 생산적인 개발자가 되어보는 건 어떨까요? ?

## 참고 자료 ?

- [Claude Code 공식 문서](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code GitHub 저장소](https://github.com/anthropics/claude-code)
- [Claude Code 베스트 프랙티스](https://www.anthropic.com/engineering/claude-code-best-practices)

---

#ClaudeCode #AI코딩 #터미널도구 #Anthropic #개발자도구
