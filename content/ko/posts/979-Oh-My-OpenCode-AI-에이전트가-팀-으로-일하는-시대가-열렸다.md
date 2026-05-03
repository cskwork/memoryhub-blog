---
title: "? Oh My OpenCode: AI 에이전트가 '팀'으로 일하는 시대가 열렸다"
date: 2026-01-18T09:11:09+09:00
slug: "979-Oh-My-OpenCode-AI-에이전트가-팀-으로-일하는-시대가-열렸다"
original_url: "https://memoryhub.tistory.com/979"
tistory_id: 979
draft: false
---

```
   ___  _       __  __          ___                    ____          _      
  / _ \| |__   |  \/  |_   _   / _ \ _ __   ___ _ __  / ___|___   __| | ___ 
 | | | | '_ \  | |\/| | | | | | | | | '_ \ / _ \ '_ \| |   / _ \ / _` |/ _ \
 | |_| | | | | | |  | | |_| | | |_| | |_) |  __/ | | | |__| (_) | (_| |  __/
  \___/|_| |_| |_|  |_|\__, |  \___/| .__/ \___|_| |_|\____\___/ \__,_|\___|
                       |___/        |_|                                     
          Your AI Teammates Are Waiting
```

혼자 일하는 AI 코딩 도구에 답답함을 느낀 적 있는가? GPT가 백엔드를 디버깅하는 동안 Claude가 다른 접근법을 시도하고, Gemini가 프론트엔드를 작업하는 상황을 상상해보라.

**Oh My OpenCode는 이런 멀티 에이전트 협업을 현실로 만든 OpenCode 플러그인이다.**

17,900개 이상의 GitHub 스타를 받은 이 프로젝트가 왜 개발자들 사이에서 폭발적인 관심을 받고 있는지 살펴본다.

**한줄요약:** 결론부터 말하면, Oh My OpenCode는 여러 AI 모델을 전문 에이전트로 편성해 병렬 협업하게 만드는 OpenCode의 강력한 확장 플러그인이다.

## 배경

터미널 기반 AI 코딩 도구 시장이 급격히 성장하고 있다. Claude Code, Cursor, OpenCode 등 다양한 도구가 경쟁 중인데, 대부분 하나의 모델이 순차적으로 작업을 처리하는 구조다.

문제는 복잡한 프로젝트에서 하나의 AI가 모든 것을 잘하기 어렵다는 점이다.

> Oh My OpenCode: OpenCode를 위한 배터리 포함 플러그인으로, 7개 이상의 전문 AI 에이전트가 백그라운드에서 병렬로 협업하며 Claude Code의 기존 설정을 그대로 사용할 수 있는 호환 레이어를 제공한다.

회사에서 팀이 일하는 방식을 떠올려보라. 설계는 시니어 아키텍트가, 코드 리뷰는 QA 전문가가, UI 구현은 프론트엔드 개발자가 담당한다. Oh My OpenCode는 이 팀 구조를 AI 에이전트에 적용한 것이다. 각 에이전트는 특정 AI 모델과 역할에 최적화되어 있어, 해당 분야에서 최고의 성능을 발휘한다.

이 프로젝트는 한국인 개발자 code-yeongyu가 만들었으며, 현재 GitHub에서 17,900개의 스타와 850개 이상의 포크를 기록하고 있다. OpenCode의 플러그인으로 작동하면서 Claude Code 사용자들이 기존 설정을 그대로 활용할 수 있는 호환 레이어를 제공하는 것이 특징이다.

## 핵심 기능 1: 에이전트 팀 시스템

Oh My OpenCode의 가장 강력한 기능은 7개의 전문 에이전트 시스템이다.

각 에이전트는 특정 AI 모델과 역할에 맞게 구성되어 있다.

**Sisyphus (기본 에이전트)**: Claude Opus 4.5 기반의 메인 오케스트레이터다. 32k 토큰의 확장된 사고(Extended Thinking) 예산을 사용하며, 복잡한 작업을 계획하고 다른 에이전트에게 위임한다. 프로젝트의 총괄 책임자 역할을 수행한다.

**oracle**: GPT-5.2 기반으로 아키텍처 설계, 코드 리뷰, 전략 수립을 담당한다.

논리적 추론과 심층 분석이 필요할 때 호출된다.

**librarian**: GLM-4.7 Free 모델을 사용해 멀티 레포지토리 분석, 문서 조회, 구현 예시 검색을 수행한다. 근거 기반 답변을 제공하며 GitHub 연구에 특화되어 있다.

**explore**: Gemini 3 Flash, Claude Haiku 4.5, 또는 Grok 중 설정에 따라 선택된다.

빠른 코드베이스 탐색과 패턴 매칭에 최적화되어 있다.

**frontend-ui-ux-engineer**: Gemini 3 Pro Preview 기반으로 UI/UX 디자인과 구현을 담당한다.

Gemini의 창의적 코드 생성 능력을 활용해 아름다운 인터페이스를 만든다.

**document-writer**: Gemini 3 Flash를 사용하는 기술 문서 작성 전문가다.

**multimodal-looker**: Gemini 3 Flash 기반의 시각 콘텐츠 전문가로, PDF, 이미지, 다이어그램 분석을 담당한다.

에이전트 호출은 자연어로 간단하게 할 수 있다.

```
# 아키텍처 리뷰 요청
Ask @oracle to review this design and propose an architecture

# 구현 방식 조사 요청
Ask @librarian how this is implemented—why does the behavior keep changing?

# 빠른 탐색 요청
Ask @explore for the policy on this feature
```

## 핵심 기능 2: 백그라운드 에이전트와 병렬 실행

전통적인 AI 코딩 도구는 한 번에 하나의 작업만 처리한다. Oh My OpenCode는 여러 에이전트를 동시에 백그라운드에서 실행할 수 있다.

실제 활용 시나리오를 보자. GPT가 버그를 디버깅하는 동안 Claude가 다른 접근법으로 근본 원인을 찾는다. 또는 Gemini가 프론트엔드를 작성하는 동안 Claude가 백엔드를 처리한다. 대규모 병렬 검색을 실행하면서 다른 부분의 구현을 계속 진행한 후, 검색 결과를 활용해 마무리하는 워크플로우도 가능하다.

백그라운드 실행은 `delegate_task` 도구의 `run_in_background` 파라미터로 제어한다.

완료되면 메인 에이전트가 알림을 받고, 필요시 결과를 대기할 수도 있다.

## 핵심 기능 3: IDE급 도구를 에이전트에게

문서에서 던지는 질문이 인상적이다. "왜 IDE의 좋은 도구들을 당신만 사용하는가? 에이전트에게도 주면 어떨까?"

Oh My OpenCode는 LSP(Language Server Protocol)와 AST(Abstract Syntax Tree) 기반 도구를 에이전트에게 제공한다.

| 도구 | 기능 |
| --- | --- |
| lsp\_diagnostics | 빌드 전 에러/경고 확인 |
| lsp\_prepare\_rename | 리네임 작업 유효성 검증 |
| lsp\_rename | 워크스페이스 전체에서 심볼 리네임 |
| ast\_grep\_search | AST 인식 코드 패턴 검색 (25개 언어 지원) |
| ast\_grep\_replace | AST 인식 코드 치환 |

일반 텍스트 검색이 아닌 코드의 구조를 이해하는 검색과 치환이 가능하다.

변수명 변경이 전체 워크스페이스에서 안전하게 이루어지고, 빌드 전에 잠재적 문제를 파악할 수 있다.

## 핵심 기능 4: 컨텍스트 자동 주입

AI 코딩 에이전트의 성능은 컨텍스트에 크게 좌우된다. Oh My OpenCode는 세 가지 방식으로 컨텍스트를 자동 주입한다.

**AGENTS.md / README.md 인젝터**: 파일을 읽을 때 해당 디렉토리부터 프로젝트 루트까지의 모든 AGENTS.md와

README.md를 자동으로 수집해 주입한다.

```
project/
├── AGENTS.md              # 프로젝트 전체 컨텍스트
├── src/
│   ├── AGENTS.md          # src 전용 컨텍스트
│   └── components/
│       ├── AGENTS.md      # 컴포넌트 전용 컨텍스트
│       └── Button.tsx     # 이 파일을 읽으면 위 3개 AGENTS.md 모두 주입
```

**조건부 규칙 인젝터**: `.claude/rules/` 디렉토리의 규칙 파일이 glob 패턴 매칭에 따라 조건부로 적용된다. 모든 규칙이 항상 필요한 것은 아니기 때문이다.

```
---
globs: ["*.ts", "src/**/*.js"]
description: "TypeScript/JavaScript 코딩 규칙"
---
- 인터페이스명은 PascalCase 사용
- 함수명은 camelCase 사용
```

**내장 MCP 서버**: Context7(공식 문서 조회), Exa AI 웹 검색, grep.app(공개 GitHub 레포 검색)이 기본 활성화되어 있다.

## 핵심 기능 5: Claude Code 호환 레이어

Claude Code를 사용하던 개발자라면 반가운 소식이다.

Oh My OpenCode는 완전한 Claude Code 호환 레이어를 제공한다. **기존 설정 파일을 그대로 사용할 수 있다.**

호환되는 항목은 다음과 같다.

| 항목 | 로드 경로 |
| --- | --- |
| MCP 서버 | ~/.claude/.mcp.json, ./.mcp.json |
| 커맨드 | ~/.claude/commands/, ./.claude/commands/ |
| 스킬 | ~/.claude/skills/, ./.claude/skills/ |
| 에이전트 | ~/.claude/agents/, ./.claude/agents/ |
| 훅 | ~/.claude/settings.json |

훅 시스템도 지원한다. PreToolUse, PostToolUse, UserPromptSubmit, Stop 이벤트에 커스텀 스크립트를 연결할 수 있다.

```
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [{ "type": "command", "command": "eslint --fix $FILE" }]
      }
    ]
  }
}
```

파일 작성이나 수정 후 자동으로 린터가 실행되는 것이다.

## 핵심 기능 6: 스킬 내장 MCP 지원

스킬이 자체 MCP 서버를 가져올 수 있다. 스킬 프론트매터나 mcp.json 파일에서 직접 MCP 설정을 정의한다.

```
---
description: 브라우저 자동화 스킬
mcp:
  playwright:
    command: npx
    args: ["-y", "@anthropic-ai/mcp-playwright"]
---
```

스킬을 로드하면 해당 MCP 도구가 자동으로 사용 가능해진다. 기본 제공되는 playwright 스킬로 브라우저 자동화,

웹 스크래핑, 테스트, 스크린샷 기능을 바로 사용할 수 있다.

## 설치 방법

① OpenCode가 먼저 설치되어 있어야 한다. OpenCode 공식 사이트에서 설치 가이드를 확인한다.

② Oh My OpenCode 설치:

```
bunx oh-my-opencode
# 또는
npx oh-my-opencode
```

③ 프롬프트에 따라 Claude, ChatGPT, Gemini 구독을 설정한다.

④ 설치 완료 후 터미널에서 `opencode`를 입력하면 사용 가능하다.

주의할 점이 있다. 2026년 1월 기준, Anthropic이 서드파티 OAuth 접근을 ToS 위반으로 제한했다.

Claude Code 구독으로 기술적으로는 사용 가능하지만, ToS 관련 사항을 인지하고 사용해야 한다.

## 모범사례/패턴 비교

| 접근법 | 장점 | 주의점 |
| --- | --- | --- |
| 단일 모델 (Claude Code) | 일관된 경험, 공식 지원 | 모델 선택 제한, 병렬 처리 불가 |
| 멀티 모델 (Oh My OpenCode) | 모델별 강점 활용, 병렬 협업 | 설정 복잡도, ToS 확인 필요 |
| 로컬 모델 (Ollama 연동) | 비용 절감, 프라이버시 보장 | 하드웨어 요구사항, 성능 제한 |

## 마치며

- Oh My OpenCode는 AI 코딩 도구를 "혼자 일하는 조수"에서 "팀으로 협업하는 동료"로 전환하는 패러다임 변화를 제시한다.
- 7개 이상의 전문 에이전트, 백그라운드 병렬 실행, IDE급 도구 지원, Claude Code 호환 레이어가 핵심 강점이다.
- 실전 팁: 먼저 기본 설정으로 시작하고, 프로젝트 루트에 AGENTS.md 파일을 만들어 프로젝트별 컨텍스트를 정의해보라.

## 참고자료

- Oh My OpenCode GitHub (<https://github.com/code-yeongyu/oh-my-opencode>)
- OpenCode 공식 사이트 (<https://opencode.ai/>)
- OpenCode GitHub (<https://github.com/opencode-ai/opencode>)
