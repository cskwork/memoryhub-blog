---
title: "? Open Code vs Claude Code, 터미널 AI 코딩 에이전트 완전 비교"
date: 2026-01-17T15:19:33+09:00
slug: "976-Open-Code-vs-Claude-Code-터미널-AI-코딩-에이전트-완전-비교"
original_url: "https://memoryhub.tistory.com/976"
tistory_id: 976
draft: false
---

```
   ___                     ____          _      
  / _ \ _ __   ___ _ __   / ___|___   __| | ___ 
 | | | | '_ \ / _ \ '_ \ | |   / _ \ / _` |/ _ \
 | |_| | |_) |  __/ | | || |__| (_) | (_| |  __/
  \___/| .__/ \___|_| |_| \____\___/ \__,_|\___|
       |_|                    vs                
   ____ _                 _        ____          _      
  / ___| | __ _ _   _  __| | ___  / ___|___   __| | ___ 
 | |   | |/ _` | | | |/ _` |/ _ \| |   / _ \ / _` |/ _ \
 | |___| | (_| | |_| | (_| |  __/| |__| (_) | (_| |  __/
  \____|_|\__,_|\__,_|\__,_|\___| \____\___/ \__,_|\___|

           Terminal AI Coding Agent Comparison
```

"Claude Code가 최고야!"라는 말을 들으면 반사적으로 고개를 끄덕이게 된다.

하지만 정작 Open Code를 써본 적 있는지 물으면 대부분 고개를 젓는다.

두 도구 모두 MCP, Skills, Subagent를 지원하지만 구현 철학이 완전히 다르다.

**어떤 도구가 "더 좋다"가 아니라, 어떤 상황에 무엇이 맞는지 알아야 진짜 실력이다.**

**한줄요약:** 결론부터 말하면, Claude Code는 Anthropic 생태계에서의 통합 경험과 완성도가 강점이고, Open Code는 모델 선택의 자유도와 오픈소스 확장성이 강점이다.

## 배경

터미널 기반 AI 코딩 에이전트 시장이 폭발적으로 성장하고 있다. 2024년 MCP(Model Context Protocol)가 표준으로 자리잡으면서, 단순한 코드 자동완성을 넘어 파일 시스템 조작,

외부 API 연동, 심지어 브라우저 자동화까지 가능한 "에이전틱 코딩"의 시대가 열렸다.

> 터미널 AI 코딩 에이전트란: 터미널에서 자연어로 명령을 내리면, AI가 코드를 작성하고 실행하며 파일을 수정하는 도구다. 단순 자동완성이 아닌, 실제 개발 작업을 대행하는 "AI 동료"에 가깝다.

두 도구 모두 SST(Serverless Stack) 팀이 만든 Open Code와 Anthropic의 Claude Code다. 흥미로운 점은 Open Code가 Claude Code의 설정 파일 형식(CLAUDE.md, .mcp.json)을 그대로 호환한다는 것이다.

경쟁이 아닌 상호 보완적 관계로 발전하고 있다.

핵심 비교 영역은 네 가지다.

- **Settings**: 설정 체계와 커스터마이징
- **MCP**: 외부 도구 연동 방식
- **Skills**: 재사용 가능한 지식 패키지
- **Subagents**: 병렬 작업과 컨텍스트 분리

## Settings 비교

설정 체계는 도구의 철학을 보여준다. Claude Code는 계층적 설정 시스템으로 엔터프라이즈 환경을 고려했고,

Open Code는 단일 JSON 파일 중심으로 단순함을 추구했다.

### Claude Code 설정 체계

Claude Code는 5단계 설정 우선순위를 갖는다. 상위 설정이 하위를 덮어쓴다.

1. **Enterprise Managed Settings**: 조직 관리자가 중앙 제어
2. **Command Line Flags**: 실행 시 `--allowedTools` 등으로 지정
3. **Local Settings** (`.claude/settings.json`): 프로젝트별 설정
4. **Project Settings**: 팀 공유용 설정
5. **User Settings** (`~/.claude.json`): 개인 전역 설정

주요 설정 예시:

```
{
  "permissions": {
    "allow": ["Read", "Write", "Bash(npm run test:*)"],
    "deny": ["WebFetch", "Bash(curl:*)"]
  },
  "env": {
    "ANTHROPIC_MODEL": "claude-sonnet-4-5-20250929"
  }
}
```

프로젝트 컨텍스트는 `CLAUDE.md` 파일에 정의한다. `/init` 명령으로 자동 생성할 수 있으며, 프로젝트 아키텍처, 코딩 컨벤션, 빌드 명령어 등을 담는다.

### Open Code 설정 체계

Open Code는 `opencode.json` 단일 파일 중심이다. 전역(`~/.config/opencode/opencode.json`)과 프로젝트별 설정을 지원한다.

```
{
  "provider": "anthropic",
  "model": "claude-sonnet-4-5-20250929",
  "theme": "dark",
  "agent": {
    "build": { "tools": ["bash", "read", "write", "edit"] },
    "plan": { "tools": ["read", "grep", "glob"] }
  }
}
```

Claude Code 호환 모드가 기본 활성화되어, `CLAUDE.md`와 `.mcp.json`을 그대로 사용할 수 있다. `AGENTS.md`와 `CLAUDE.md`가 동시에 있으면 `AGENTS.md`가 우선한다.

### 설정 비교 요약

| 항목 | Claude Code | Open Code |
| --- | --- | --- |
| 설정 파일 | `~/.claude.json`, `.claude/settings.json` | `opencode.json` |
| 프로젝트 컨텍스트 | `CLAUDE.md` | `AGENTS.md` (CLAUDE.md 호환) |
| 설정 계층 | 5단계 (Enterprise → User) | 3단계 (Remote → Global → Project) |
| 모델 선택 | Anthropic 모델 전용 | 멀티 프로바이더 (OpenAI, Gemini, Bedrock 등) |
| 테마/UI 커스텀 | 제한적 | 상세 TUI 설정 가능 |

## MCP(Model Context Protocol) 비교

MCP는 AI 에이전트가 외부 도구와 소통하는 표준 프로토콜이다. 두 도구 모두 MCP를 지원하지만, 관리 방식에 차이가 있다.

### Claude Code의 MCP 관리

Claude Code는 3단계 스코프로 MCP 서버를 관리한다.

- **Local Scope**: 개인 실험용, 민감한 자격 증명
- **Project Scope**: 팀 공유, `.mcp.json`에 정의
- **User Scope**: 개인이 모든 프로젝트에서 사용

```
# HTTP 서버 추가 (권장)
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 스코프 지정
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic

# Bearer 토큰 포함
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

**Tool Search 기능**이 특징적이다. MCP 도구가 컨텍스트의 10%를 초과하면 자동으로 동적 로딩 모드로 전환된다.

Sonnet 4 이상에서 지원한다.

### Open Code의 MCP 관리

Open Code도 `opencode.json`의 `mcp` 섹션에서 관리한다.

```
{
  "mcp": {
    "gh_grep": {
      "type": "remote",
      "url": "https://grep.dev/api/search",
      "headers": { "Authorization": "Bearer ${GH_GREP_TOKEN}" }
    },
    "local_server": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path"],
      "env": ["HOME"]
    }
  }
}
```

환경변수 확장(`${VAR}`)을 지원해서 민감한 값을 코드에 직접 넣지 않아도 된다.

조직에서 `.well-known/opencode` 엔드포인트로 기본 MCP 서버를 배포할 수도 있다.

### MCP 비교 요약

| 항목 | Claude Code | Open Code |
| --- | --- | --- |
| 설정 파일 | `.mcp.json`, CLI | `opencode.json` mcp 섹션 |
| 스코프 | Local/Project/User 3단계 | Global/Project 2단계 |
| 전송 방식 | HTTP(권장), SSE(레거시), STDIO | Remote(HTTP), Local(STDIO) |
| 동적 로딩 | Tool Search 자동 활성화 | 수동 관리 |
| 권한 제어 | `mcp__server__*` 와일드카드 | `permission` 필드 |

## Skills 비교

Skills는 재사용 가능한 지식 패키지다. Claude Code는 이 개념을 "Agent Skills"로 공식화하며 크게 발전시켰다.

### Claude Code의 Agent Skills

2025년 10월 공식 발표된 Agent Skills는 **점진적 공개(Progressive Disclosure)** 원칙을 따른다.

전체 내용을 한 번에 로딩하지 않고, 필요할 때만 관련 부분을 읽는다.

```
my-skill/
├── SKILL.md          # 메인 지침 (필수)
├── scripts/          # 실행 가능한 스크립트
│   └── helper.py
└── references/       # 참조 문서
    └── schema.md
```

SKILL.md 구조:

```
---
name: pdf-processing
description: PDF 파일에서 텍스트 추출, 폼 채우기, 문서 병합. PDF, 폼, 문서 추출 관련 작업 시 사용.
allowed-tools: Read, Bash(python:*)
---

# PDF 처리

## 빠른 시작
텍스트 추출:
```python
import pdfplumber
with pdfplumber.open("doc.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

폼 채우기는 <FORMS.md> 참조.

```
스킬 발견 과정:
1. 시작 시 모든 스킬의 `name`과 `description`만 시스템 프롬프트에 로드
2. 사용자 요청이 스킬 설명과 매칭되면 활성화 확인
3. 승인 후 `SKILL.md` 전체 내용 컨텍스트에 추가
4. 필요한 참조 파일과 스크립트만 추가 로드

### Open Code의 Skills

Open Code는 Claude Code의 Skills 형식을 호환한다. `~/.config/opencode/skills/` 또는 `.opencode/skills/`에 배치한다.

```yaml
---
name: my-skill
description: 스킬 설명
---

# 상세 지침
Claude가 스킬 활성화 시 이 내용을 참조합니다.
```

**Superpowers 플러그인**을 통해 더 풍부한 스킬 시스템을 사용할 수 있다.

`find_skills`, `use_skills` 도구로 Anthropic 호환 스킬을 동적으로 로드한다.

### Skills vs 다른 개념

| 기능 | Skills | Subagents | CLAUDE.md/AGENTS.md |
| --- | --- | --- | --- |
| 목적 | 도메인 지식 제공 | 병렬 작업 수행 | 프로젝트 컨텍스트 |
| 컨텍스트 | 현재 대화에 추가 | 별도 컨텍스트 | 항상 로드 |
| 활성화 | 자동(설명 매칭) | 명시적 호출 | 자동 |
| 코드 실행 | 가능 | 가능 | 불가 |

## Subagents 비교

Subagents는 별도 컨텍스트를 가진 독립 AI 인스턴스다. 컨텍스트 오염 방지와 병렬 작업에 유용하다.

### Claude Code의 Subagents

Claude Code는 세 가지 내장 서브에이전트를 제공한다.

- **Explore**: 코드베이스 탐색 전용, Plan 모드에서 자동 호출
- **Task**: 범용 작업 위임
- **Custom**: 사용자 정의 서브에이전트

```
# .claude/agents/reviewer.md
---
name: reviewer
description: 코드 리뷰 전용
model: sonnet
color: orange
---

당신은 전문 코드 리뷰어입니다.
보안, 성능, 유지보수성에 집중하세요.
```

서브에이전트 특징:

- 부모와 동일한 도구 접근 권한
- 컨텍스트 격리 (서브에이전트 간 직접 정보 공유 불가)
- 각 서브에이전트 사용량은 별도 집계
- `Ctrl+B`로 백그라운드 실행 가능

### Open Code의 Subagents

Open Code는 **Primary Agent**와 **Subagent**를 구분한다.

Primary Agents (Tab으로 전환):

- **Build**: 모든 도구 활성화, 개발 작업용
- **Plan**: 읽기 전용, 분석과 계획 수립용

Subagents (@ 멘션으로 호출):

- **General**: 복잡한 검색, 멀티스텝 작업
- **Explore**: 코드베이스 탐색

```
{
  "agent": {
    "custom-reviewer": {
      "description": "코드 리뷰 전용",
      "model": "openai/gpt-5.1",
      "temperature": 0.3,
      "tools": ["read", "grep", "glob"]
    }
  }
}
```

마크다운 파일로도 정의 가능:

```
<!-- ~/.config/opencode/agent/reviewer.md -->
---
description: 코드 리뷰 전용
model: anthropic/claude-sonnet-4-5
temperature: 0.3
---

보안, 성능, 유지보수성에 집중한 코드 리뷰를 수행합니다.
```

### Subagents 비교 요약

| 항목 | Claude Code | Open Code |
| --- | --- | --- |
| 내장 에이전트 | Explore, Task | Build, Plan, General, Explore |
| 커스텀 정의 | `.claude/agents/*.md` | `agent/` 폴더 또는 JSON |
| 호출 방식 | 자동 또는 명시적 | Tab(Primary), @(Subagent) |
| 모델 선택 | 제한적 | 에이전트별 다른 모델 지정 가능 |
| 백그라운드 | Ctrl+B 지원 | 미지원 |

## 실습: 프로젝트 설정 예시

### 1단계: 프로젝트 초기화

**Claude Code**:

```
cd my-project
claude
/init  # CLAUDE.md 자동 생성
```

**Open Code**:

```
cd my-project
opencode
/init  # AGENTS.md 자동 생성
```

### 2단계: MCP 서버 추가

**Claude Code**:

```
claude mcp add --transport http github https://api.github.com/mcp
```

**Open Code** (`opencode.json` 편집):

```
{
  "mcp": {
    "github": {
      "type": "remote",
      "url": "https://api.github.com/mcp"
    }
  }
}
```

### 3단계: 커스텀 명령어 생성

두 도구 모두 마크다운 파일로 슬래시 명령어를 정의한다.

**Claude Code** (`.claude/commands/review.md`):

```
---
description: PR 코드 리뷰 수행
---

$ARGUMENTS에 대한 코드 리뷰를 수행해주세요.
1. 보안 취약점 확인
2. 성능 이슈 점검
3. 테스트 커버리지 검토
```

**Open Code** (`.opencode/command/review.md`):

```
---
description: PR 코드 리뷰 수행
---

$ARGUMENTS에 대한 코드 리뷰를 수행해주세요.
1. 보안 취약점 확인
2. 성능 이슈 점검
3. 테스트 커버리지 검토
```

사용: `/review PR #123`

## 모범사례/패턴 비교

| 사용 사례 | Claude Code | Open Code |
| --- | --- | --- |
| Anthropic 모델만 사용 | 최적 (네이티브 통합) | 호환 가능 |
| 멀티 모델 (GPT + Claude + Gemini) | 불가 | 최적 (프로바이더 자유 선택) |
| 엔터프라이즈 배포 | 최적 (Managed Settings) | 제한적 |
| 오픈소스 기여 | 불가 (폐쇄형) | 최적 (MIT 라이선스) |
| 기존 Claude Code 설정 활용 | 기본 | 호환 모드 지원 |
| TUI 커스터마이징 | 제한적 | 상세 설정 가능 |
| Skills 생태계 | 풍부 (공식 Skills) | 호환 + 플러그인 확장 |

## 마치며

- Claude Code는 Anthropic 생태계에 최적화된 통합 경험을 제공한다. 엔터프라이즈 관리 기능, 공식 Skills 라이브러리, Tool Search 같은 고급 기능이 강점이다.
- Open Code는 모델 선택의 자유와 오픈소스 확장성이 강점이다. Claude Code 설정을 그대로 사용하면서 GPT-5나 Gemini를 쓸 수 있다.
- 실전 팁: 현재 Claude Code를 쓰고 있다면 설정 파일을 그대로 유지하면서 Open Code도 설치해보세요. `CLAUDE.md`와 `.mcp.json`이 호환되므로 전환 비용 없이 두 도구를 병행할 수 있다.

## 참고자료

- Claude Code 공식 문서 (<https://docs.anthropic.com/en/docs/claude-code>)
- Open Code 공식 문서 (<https://opencode.ai/docs>)
- Agent Skills 소개 - Anthropic Engineering (<https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills>)
- Open Code GitHub (<https://github.com/opencode-ai/opencode>)
- MCP 프로토콜 명세 (<https://modelcontextprotocol.io>)
