---
title: "? Codex CLI에서 Claude Skills 사용하기: AI 에이전트의 도구"
date: 2025-12-17T15:38:01+09:00
slug: "930-Codex-CLI에서-Claude-Skills-사용하기-AI-에이전트의-도구"
original_url: "https://memoryhub.tistory.com/930"
tistory_id: 930
draft: false
---

```
  ╔═══════════════════════════════════════════════╗
  ║   SKILL.md                                    ║
  ║   ┌─────────┐    ┌─────────┐    ┌─────────┐  ║
  ║   │ Claude  │ ←→ │ SKILL   │ ←→ │ Codex   │  ║
  ║   │  Code   │    │   .md   │    │  CLI    │  ║
  ║   └─────────┘    └─────────┘    └─────────┘  ║
  ║         ↑              ↑              ↑      ║
  ║    /mnt/skills    YAML + MD    ~/.codex/     ║
  ╚═══════════════════════════════════════════════╝
```

Claude Code에서만 쓸 수 있던 Skills가 이제 OpenAI Codex에서도 작동한다. 경쟁사가 만든 기능을 OpenAI가 채택한 것이다. 이것은 단순한 기능 복제가 아니다. **AI 코딩 에이전트 시장에서 최초의 실질적 표준이 등장하고 있다는 신호다.**

**한줄요약:** 결론부터 말하면, Anthropic의 SKILL.md 포맷이 OpenAI Codex CLI에서도 동작하며, 기존에 만든 Claude Skills를 거의 그대로 재사용할 수 있다.

## 배경

2025년 10월, Anthropic은 Claude Code에 Skills 시스템을 도입했다. Skills는 AI 에이전트에게 "특정 작업을 어떻게 수행해야 하는지" 가르치는 방법이다. 프랜차이즈 매장의 운영 매뉴얼을 떠올리면 된다. 매장 오픈부터 마감까지 모든 절차가 문서화되어 있어서, 누가 와도 일관된 서비스를 제공할 수 있는 것처럼.

> Skill은 SKILL.md 파일이 들어있는 폴더로, AI 에이전트가 특정 작업을 수행할 때 참조하는 지침서다.

그로부터 두 달 후인 12월, OpenAI가 조용히 같은 시스템을 채택했다. 공식 발표 없이, Codex CLI의 PR과 ChatGPT의 Code Interpreter에 Skills 지원이 추가된 것이다.

왜 중요한가? AI 도구 시장에서 플랫폼 종속(lock-in)은 흔한 전략이다. 그런데 OpenAI가 경쟁사의 포맷을 그대로 수용했다. 이는 Skills가 단순히 좋은 아이디어를 넘어서, **업계 표준으로 자리잡을 가능성**이 높다는 의미다.

## Skill의 구조와 작동 원리

Skill은 놀라울 정도로 단순하다. YAML 프론트매터와 마크다운 본문으로 구성된 파일 하나가 전부다.

```
---
name: pdf-processing
description: PDF에서 텍스트와 테이블을 추출합니다. PDF, 폼, 문서 추출이 언급될 때 사용하세요.
---
# PDF Processing

- pdfplumber를 사용해 텍스트를 추출합니다.
- 폼 작성은 FORMS.md를 참조하세요.
```

에이전트가 Skill을 사용하는 과정은 두 단계로 나뉜다.

첫째, 시작 시 모든 Skill의 name과 description만 시스템 프롬프트에 로드된다. 이 메타데이터는 에이전트가 "언제 이 Skill을 써야 하는지" 판단하는 데 사용된다. **name은 100자, description은 500자 제한**이 있어서 간결하게 작성해야 한다.

둘째, 에이전트가 특정 Skill이 필요하다고 판단하면, 그때서야 전체 SKILL.md 내용을 컨텍스트에 로드한다. 이 점진적 공개(progressive disclosure) 방식은 컨텍스트 윈도우를 효율적으로 사용하게 해준다.

## Codex CLI에서 Skills 사용하기

### 1. Skill 디렉토리 생성

Codex CLI는 `~/.codex/skills/` 경로에서 Skill을 찾는다. 하위 디렉토리를 재귀적으로 탐색하며, SKILL.md라는 이름의 파일만 인식한다.

```
mkdir -p ~/.codex/skills/my-skill
```

### 2. SKILL.md 파일 작성

```
cat <<'EOF' > ~/.codex/skills/my-skill/SKILL.md
---
name: react-component
description: React 컴포넌트 작성 시 사용. TypeScript, 함수형 컴포넌트, 커스텀 훅 패턴을 따릅니다.
---
# React Component Skill

## 기본 규칙
- 함수형 컴포넌트만 사용
- Props는 TypeScript 인터페이스로 정의
- 상태 관리는 useState, useReducer 우선

## 파일 구조
ComponentName/
  index.tsx
  ComponentName.tsx
  ComponentName.test.tsx
  styles.module.css
EOF
```

### 3. Skills 활성화 및 실행

Codex CLI에서 Skills는 기본 비활성화 상태다. `--enable skills` 옵션으로 활성화한다.

```
codex --enable skills -m gpt-5.2
```

실행 후 `/skills` 명령으로 사용 가능한 Skill 목록을 확인하거나, `$skill-name` 형식으로 특정 Skill을 직접 호출할 수 있다.

### 4. 기존 Claude Skills 재사용

Claude Code용으로 만들어진 Skills도 대부분 호환된다. 예를 들어, Simon Willison이 만든 Datasette 플러그인 Skill을 그대로 설치할 수 있다.

```
git clone https://github.com/datasette/skill \
  ~/.codex/skills/datasette-plugin
```

## Claude Code vs Codex CLI: Skill 구현 비교

| 항목 | Claude Code | Codex CLI |
| --- | --- | --- |
| Skill 경로 | /mnt/skills/ 또는 프로젝트 내 | ~/.codex/skills/ |
| 활성화 방식 | 기본 활성화 | --enable skills 필요 |
| 호출 방법 | view 도구로 읽기 | $skill-name 또는 /skills |
| name 제한 | 명시적 제한 없음 | 100자 |
| description 제한 | 명시적 제한 없음 | 500자 |
| 프롬프트 주입 방지 | 별도 처리 | 메타데이터 줄바꿈 제거 |

주목할 점은 **핵심 구조가 동일하다**는 것이다. YAML 프론트매터 + 마크다운 본문이라는 포맷, 점진적 공개 방식, 그리고 폴더 기반 구조 모두 일치한다.

## 마치며

- OpenAI가 Anthropic의 Skills 포맷을 채택함으로써, SKILL.md는 AI 코딩 에이전트의 첫 공통 표준으로 자리잡고 있다.
- 한 번 작성한 Skill을 여러 플랫폼에서 재사용할 수 있어, 개발자의 투자 가치가 높아졌다.
- 실전 팁: 기존 반복 작업을 SKILL.md로 문서화해두면, Claude Code와 Codex CLI 모두에서 활용할 수 있다.

## 참고자료

- OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI (<https://simonwillison.net/2025/Dec/12/openai-skills/>)
- Codex CLI Skills Documentation (<https://github.com/openai/codex/blob/main/docs/skills.md>)
- Anthropic Skills Repository (<https://github.com/anthropics/skills>)
- Porting Skills to OpenAI Codex (<https://blog.fsck.com/2025/10/27/skills-for-openai-codex/>)
