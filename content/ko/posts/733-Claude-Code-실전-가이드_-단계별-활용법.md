---
title: "Claude Code 실전 가이드: 단계별 활용법"
date: 2025-07-29T17:34:49+09:00
slug: "733-Claude-Code-실전-가이드_-단계별-활용법"
original_url: "https://memoryhub.tistory.com/733"
tistory_id: 733
draft: false
categories: ["데브 라이브러리"]
tags: ["Claude"]
  hidden: false
cover:
  image: "/images/733-Claude-Code-실전-가이드_-단계별-활용법/img.jpg"
  relative: false
  hidden: false
---

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img.jpg)

Claude Code는 터미널 기반 AI 코딩 도우미입니다. 코드베이스를 분석하고 개발 작업을 지원합니다.  
이 가이드는 초보자부터 고급 사용자까지의 실용적인 활용법을 다룹니다.

## ? 사전 준비사항

**설치 요구사항**

- Node.js 18 이상
- 설치: `npm install -g @anthropic-ai/claude-code`
- 실행: 프로젝트 디렉토리에서 `claude` 명령어
- 원도우는 git bash에 설치. C 드라이브에 설치되어야 어디에서든 사용 가능함.

**기본 안전 수칙**

- ESC 키로 언제든 작업 중단 가능
- Plan 모드(Shift+Tab)로 안전하게 분석
- 중요한 작업 전 백업 필수

---

## ? 초보자: 기본 기능 익히기

### 1. 첫 시작과 코드베이스 탐색

**기본 질문하기**

```
# 프로젝트 이해하기
"What does this project do?"
"Show me the main components"
"docs/ 폴더에 프로젝트 구조 파악을 한 내용을 작성하고 정리해줘."
```

**ESC 키보드 키 인터럽트 활용**

- 작업이 원하지 않는 방향으로 진행될 때 ESC 키 사용.
- 즉시 중단 후 다른 방향으로 재지시 가능. 적극 사용하세요!!!

### 2. CLAUDE.md 파일 활용

프로젝트 루트에 `CLAUDE.md` 파일을 생성하여 지침을 문서화하세요.

프로젝트 켄텍스트 생성을 클로드에 맡기고 싶으면 다음과 같은 명령어를 실행하세요. ->   /init

```
 /init
```

**효과**: Claude가 자동으로 이 지침을 따라서 일관된 작업 수행 / 프로젝트에 대한 context/맥락 정보를 파악하여 정확도 향상. 비즈니스 환경에서 기존 코드 작업이 필요한 경우 원하는 코딩 형식/스타일 등 세부적인 정의가 있어야 원하는 결과물 도출 가능. (아무것도 모르는 주니어 개발자에게 명확한 지시를 주는 것과 유사함)

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img.png)

### 3. Plan 모드 사용법

- **전환**: MacOS는 Shift+Tab. 원도우는 alt+m
- **용도**: 읽기 전용으로 안전하게 분석
- **활용**: "Research the best approach"로 계획 수립 후 실행

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_1.png)

---

## ? 중급자: 설정과 도구 통합

### 1. settings.json 권한 설정

`~/.claude/settings.json`프로젝트별 `.claude/settings.json`으로 세분화 가능

`~/.claude/settings.json` 파일로 보안 설정:

```
{
  "permissions": {
    "allow": [
      "Task",
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Bash(git log:*)",
      "Bash(curl:*)",
      "Bash(ls:*)",
      "Bash(find:*)",
      "Bash(ollama:*)",
      "Bash(source:*)",
      "Bash(which:*)",
      "Read(~/.zshrc)",
      "Grep",
      "List",
      "Read",
      "WebFetch",
      "WebSearch"
    ],
    "deny": [
      "Bash(rm:*)",
      "Read(application.yml)",
      "Read(**/application.yml)"
    ],
    "defaultMode": "plan"
  },
  "env": {
    "BASH_DEFAULT_TIMEOUT_MS": "60000"
  },
  "includeCoAuthoredBy": false
}
```

**목적**: 위험한 명령어 차단, 안전한 명령어만 허용

### 2. Commands (슬래시 명령어)

`.claude/commands/` 디렉토리에 자주 사용하는 프롬프트 저장:

```
# 커맨드 저장 폴더 생성 
mkdir -p ~/.claude/commands

# 기능 추가
echo "Ultra Think. We would like to add [FEATURE] to this system. This feature should [DESCRIBE]. It must align with our existing system of [EXPLAIN]. 
Create a detailed implementation plan that outlines each file that must be touched, and specific changes that must be made. 
We are looking for a clean, seamless implementation strategy. You must conduct thorough research during this planning phase. Your plan should not contain any analysis or code review. I expect that to be completed by the time you present your plan.  
Prepare a detailed action plan for my review. Together we will finalize and refine the plan for execution." > ~/.claude/commands/add-feature.md

# 기능 리뷰
echo "Think. Audit the [FEATURE] system for completeness, security standards, and correct wiring, specifically related to [REQUIREMENT]. 
Identify dead or redundant code, scattered or overly complex logic, and areas where things can be simplified but maintain functionality. Also note gaps in implementation or incomplete refactors, loose ends, and sources of confusion.
Present a focused audit with a step-by-step action plan that outlines the current implementation, discovered errors, opportunities for improvement, and potential for optimization.
Prepare to enhance, debug, or refactor the system as needed according to user feedback in order to ensure a robust and reliable operation that is flexible, extensible, easy to maintain, and crafted with precision." > ~/.claude/commands/review-feature.md
```

**사용법**: `/review-feature` 입력으로 즉시 호출

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_2.png)

### 3. MCP (Model Context Protocol) 연동

```
# 외부 도구 연결
claude mcp add --transport http context7 https://mcp.context7.com/mcp
claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp
```

**활용 예시**:

- context7은 react, vue3 등 공식문서를 찾아서 개발 원칙을 따름.

### 4. YOLO 모드 (⚠️ 주의 필요)

```
claude --dangerously-skip-permissions
```

**장점**: 모든 확인 절차를 생략해 대량 리팩터·보일러플레이트 생성 시 속도 ↑

**위험**: 파일 삭제, 데이터 유출 가능성

**안전한 사용법**: 격리 환경에서 사용

---

## ? 고급자: 복잡한 워크플로우 최적화

### 1. Subagents 활용

전문 AI 에이전트로 작업 위임 → 메인 컨텍스트 청결 유지(길이 줄어듬):

```
# 해당 명령어를 입력하면 내가 원하는 Agent 생성 가능
/agents
```

**효과**: 메인 컨텍스트 오염 방지, 전문 분석

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_3.png)

### 2. Ultra-think 모드 → 깊이 있는 설계·성능 전략 도출

- 토큰 소비가 많으므로 중요한 결정에만 활용

```
"Plan the implementation strategy ultrathink"
```

**용도**: 복잡한 문제의 심층 분석  
**주의**: 토큰 사용량 증가

### 3. 대형 코드베이스 다루기

1. Plan 모드: “Analyze project and outline steps to add OAuth login.”
2. 변경 범위 검증 후 구현

**최소한의 수정 요청할 때 키워드 minimal 사용**:

```
"Refactor client.py in Supabase folder and add minimal user authentication feature with error handling"
```

**장점**:

- 최소한의 변경으로 기능 추가
- 기존 구조 보존
- 부작용 최소화

**기타 도구**:

1. CLAUDE.md에 핵심 파일 목록 작성
2. MCP로 Git, Deepwiki, Context7 도구 연동
3. Ultra-think로 상세 계획 수립

---

## ✅ 실전 적용 체크리스트

### 초보자

- ESC 인터럽트 사용법 숙지
- CLAUDE.md 파일 작성
- Plan 모드로 안전하게 분석

### 중급자

- settings.json 권한 설정
- 자주 사용하는 Commands 등록
- MCP 도구 연동
- YOLO 모드는 격리 환경에서만

### 고급자

- Subagents로 작업 위임
- Ultra-think로 복잡한 분석
- Minimal prompt로 효율적 기능 추가

---

## ? 용어

- **ESC Interrupt**: 위험할 때 누르는 "정지" 버튼, 자동차의 브레이크 같아요
- **Plan 모드**: 실제로 만들기 전에 계획만 세우는 모드, 그림 그리기 전 밑그림 그리는 것처럼
- **YOLO 모드**: "그냥 해!"라고 빠르게 일하는 모드, 하지만 실수할 수 있어서 조심해야 해요
- **Subagents**: 전문가 친구들, 어려운 일을 도와주는 특별한 도우미들
- **Large Codebase**: 아주 큰 레고 작품처럼 복잡한 코드 덩어리
- **Minimal Prompt**: 꼭 필요한 말만 하는 방법, "물 주세요" 대신 긴 설명 안 하는 것처럼

이 가이드를 단계별로 따라하며 Claude Code의 강력한 기능을 안전하게 활용해보세요!

#### 공식 문서로 더 깊이 이해하고 싶으면

- <https://docs.anthropic.com/ko/docs/claude-code/common-workflows>

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_4.png)

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_5.png)

## 쿠키

- chatgpt agent 모드가 만든 발표자료

[클로드 코드 - 초보부터 고급까지 실전 활용 가이드.pptx3.19MB](./file/클로드 코드 - 초보부터 고급까지 실전 활용 가이드.pptx)
