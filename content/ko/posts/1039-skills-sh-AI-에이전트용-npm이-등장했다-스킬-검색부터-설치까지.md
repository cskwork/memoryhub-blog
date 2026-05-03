---
title: "? skills.sh: AI 에이전트용 npm이 등장했다 - 스킬 검색부터 설치까지"
date: 2026-02-23T14:01:33+09:00
slug: "1039-skills-sh-AI-에이전트용-npm이-등장했다-스킬-검색부터-설치까지"
original_url: "https://memoryhub.tistory.com/1039"
tistory_id: 1039
draft: false
---

```
  ┌─────────────────────────────────────────────┐
  │                                             │
  │   $ npx skills add ___/___@___              │
  │                                             │
  │   ███████╗██╗  ██╗██╗██╗     ██╗     ███████╗│
  │   ██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝│
  │   ███████╗█████╔╝ ██║██║     ██║     ███████╗│
  │   ╚════██║██╔═██╗ ██║██║     ██║     ╚════██║│
  │   ███████║██║  ██╗██║███████╗███████╗███████║│
  │   ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝│
  │                                             │
  │   The Open Agent Skills Ecosystem           │
  │                                             │
  │   npm install  →  코드 공유                  │
  │   npx skills   →  AI 지식 공유              │
  │                                             │
  └─────────────────────────────────────────────┘
```

AI 코딩 에이전트를 쓰다 보면 같은 지시를 반복하는 자신을 발견하게 됩니다. "React 컴포넌트는 이 패턴으로 작성해줘", "코드 리뷰할 때 이 기준을 따라줘"와 같은 말을 매번 새 대화마다 입력하는 건 비효율적이죠. 이 문제를 해결하기 위해 등장한 Agent Skills라는 개념은 이전 글에서 다뤘는데, 그렇다면 매번 스킬을 처음부터 만들어야 할까요?

**skills.sh는 다른 개발자들이 만든 스킬을 npm처럼 검색하고 설치할 수 있게 해주는 오픈 생태계입니다.**

**한줄요약:** 결론부터 말하면, skills.sh는 Vercel이 만든 AI 에이전트용 패키지 매니저로, 자연어로 작성된 절차적 지식을 검색/설치/공유할 수 있는 오픈 디렉토리입니다.

---

## 배경

> skills.sh는 AI 에이전트가 참조할 수 있는 절차적 지식을 패키지처럼 공유하는 오픈 플랫폼입니다.

npm이 자바스크립트 패키지 생태계의 표준이 된 것처럼, AI 에이전트의 "지식"에도 공유 생태계가 필요합니다. 2026년 1월 Vercel에서 출시한 skills.sh가 바로 그 역할을 합니다. 공식 슬로건은 "The Open Agent Skills Ecosystem"으로, 개발자들이 스킬을 검색하고 설치하고 공유할 수 있는 허브입니다.

여기서 중요한 건 스킬의 본질입니다. 스킬은 프로그래밍 코드가 아니라 **마크다운으로 작성된 자연어 명령**입니다.

모델을 파인튜닝하거나 복잡한 실행 로직을 짜는 대신, 에이전트가 특정 작업을 수행할 때 참조할 "컨텍스트 명령(contextual instruction)"을 제공하는 방식이죠. 새 팀원에게 온보딩 문서를 건네주는 것과 비슷한데, 다만 그 팀원이 문서를 읽고 즉시 실행에 옮길 수 있는 AI 에이전트라는 점이 다릅니다.

이 접근 방식의 장점은 가볍고 업데이트가 쉬우며, Claude Code, Cursor, GitHub Copilot, Gemini CLI 등 40개 이상의 에이전트에서 동일한 스킬을 사용할 수 있다는 점입니다. 출시 6시간 만에 2만 건 이상의 설치를 기록했고,

2026년 2월 기준으로 하루 평균 147개의 새로운 스킬이 등록되고 있습니다.

### Skills vs MCP, 뭐가 다를까?

skills.sh를 처음 접하면 MCP(Model Context Protocol)와 헷갈리기 쉽습니다. 둘 다 에이전트의 능력을 확장한다는 공통점이 있지만, 해결하는 문제가 근본적으로 다릅니다.

MCP는 에이전트가 외부 도구(API, 데이터베이스)와 통신하는 **표준 프로토콜**입니다. "에이전트가 도구와 어떻게 대화하는가"를 해결하죠. 반면 Skills는 **절차적 지식의 패키징과 공유**에 초점을 맞춥니다. "개발자가 에이전트의 역량을 어떻게 발견하고 공유하는가"를 해결합니다.

비유하자면, MCP는 에이전트에게 **능력(ability)**을 주고, Skills는 그 능력을 **잘 사용하는 방법(how-to)**을 알려줍니다.

GitHub Actions로 비유하면, Skills는 워크플로우 YAML 파일이고 MCP는 그것을 실행하는 러너(runner)에 해당합니다.

둘은 경쟁 관계가 아니라 상호 보완적이며, 실제로 스킬 안에서 MCP 서버를 참조하는 것도 가능합니다.

| 구분 | Agent Skills | MCP |
| --- | --- | --- |
| 핵심 역할 | 절차적 지식 (how-to) | 도구 접근 (tool access) |
| 작성 방식 | 마크다운 (자연어) | JSON Schema / 코드 |
| 실행 방식 | 에이전트가 해석 후 실행 | 결정적(deterministic) 함수 호출 |
| 비유 | 온보딩 가이드 | USB-C 포트 |

---

## skills.sh 핵심 기능

### 1. 스킬 검색

skills.sh에 등록된 스킬은 웹(skills.sh)에서 브라우징하거나, CLI의 `find` 명령어로 검색할 수 있습니다.

```
# 실시간 검색 모드 (인자 없이 실행)
$ npx skills find

# 키워드 직접 검색
$ npx skills find graphql
```

인자 없이 실행하면 실시간 검색 UI가 뜹니다. 키워드를 입력하면 관련 스킬이 즉시 필터링되어 표시됩니다. 키워드를 인자로 넘기면 해당 결과를 바로 반환하죠. 예를 들어 `npx skills find graphql`을 실행하면 Apollo GraphQL 공식 스킬을 포함한 관련 스킬 목록이 출력됩니다.

### 2. 스킬 설치

npm의 `npm install`처럼, `add` 명령어 한 줄로 스킬을 설치할 수 있습니다.

```
# 기본 설치 (저장소 전체)
$ npx skills add vercel-labs/agent-skills

# 특정 스킬만 설치
$ npx skills add vercel-labs/agent-skills --skill frontend-design

# 소유자/저장소@스킬 형식
$ npx skills add daleseo/korean-skills@humanizer
```

설치 과정에서 CLI가 몇 가지 질문을 던집니다. 어떤 스킬을 설치할지, 어떤 에이전트에 적용할지(Claude Code, Cursor, Antigravity 등 40개 이상 지원), 프로젝트 단위인지 전역인지, 심볼릭 링크 방식인지 복사 방식인지를 선택합니다.

설치가 완료되면 프로젝트의 `.agents/skills/<스킬명>` 디렉토리에 스킬이 다운로드됩니다.

심볼릭 링크 옵션(권장)을 선택하면 각 에이전트의 설정 폴더(`.claude/skills/`, `.cursor/skills/` 등)에 자동으로 링크가 생성됩니다. npm이 `node_modules/`에 패키지를 설치하는 것과 같은 구조입니다.

```
프로젝트/
├── .agents/skills/        ← 스킬 원본
│   ├── grammar-checker/
│   │   └── SKILL.md
│   └── humanizer/
│       ├── SKILL.md
│       └── references/
├── .claude/skills/        ← 심볼릭 링크
│   ├── grammar-checker -> ../../.agents/skills/grammar-checker
│   └── humanizer -> ../../.agents/skills/humanizer
└── .cursor/skills/        ← 심볼릭 링크
    ├── grammar-checker -> ../../.agents/skills/grammar-checker
    └── humanizer -> ../../.agents/skills/humanizer
```

CI/CD 환경이나 비대화형 설치가 필요하다면 `-y` 플래그로 확인 없이 설치할 수도 있습니다.

```
# 비대화형 설치 (CI/CD 친화적)
$ npx skills add vercel-labs/agent-skills --skill frontend-design -g -a claude-code -y

# 전역 설치
$ npx skills add daleseo/korean-skills -g

# 특정 에이전트에만 설치
$ npx skills add daleseo/korean-skills --agent claude-code cursor
```

### 3. 스킬 생성

새로운 스킬을 만들 때는 `init` 명령어로 템플릿을 생성합니다.

```
$ npx skills init my-skill
```

이 명령어는 `my-skill` 디렉토리를 만들고 기본 `SKILL.md` 템플릿을 생성합니다. 스킬의 핵심은 이 SKILL.md 파일입니다. YAML 프론트매터에 이름과 설명을 적고, 본문에 자연어로 된 지시사항을 작성하면 됩니다.

선택적으로 참조 문서, 스크립트, 템플릿 등을 함께 포함시킬 수 있습니다.

### 4. 스킬 관리

설치 이후의 관리 명령어도 npm과 유사한 패턴을 따릅니다.

```
# 설치된 스킬 목록 확인
$ npx skills list
$ npx skills list -a claude-code   # 특정 에이전트 기준

# 스킬 제거
$ npx skills remove grammar-checker humanizer

# 업데이트 확인 및 적용
$ npx skills check
$ npx skills update

# 팀 동기화용 잠금 파일 생성
$ npx skills generate-lock
```

팀에서 동일한 버전의 스킬을 사용해야 한다면 `generate-lock` 명령어로 잠금 파일을 생성할 수 있습니다.

npm의 `package-lock.json`과 같은 역할입니다.

---

## 실습: 스킬 검색부터 설치까지

실제로 한국어 스킬을 설치하는 과정을 단계별로 따라가 보겠습니다.

**1단계: 저장소에 어떤 스킬이 있는지 확인**

설치 전에 `--list` 옵션으로 저장소의 스킬 목록을 먼저 확인합니다.

```
$ npx skills add daleseo/korean-skills --list
```

이 명령어는 저장소에 포함된 스킬의 이름과 설명을 출력합니다. 설치 없이 둘러보기만 하고 싶을 때 유용합니다.

**2단계: 원하는 스킬 설치**

humanizer 스킬(AI가 생성한 한국어 텍스트를 자연스러운 인간의 글쓰기로 변환)을 설치해보겠습니다.

```
$ npx skills add daleseo/korean-skills@humanizer
```

CLI의 대화형 프롬프트에서 에이전트 선택(Claude Code, Cursor 등), 설치 범위(프로젝트/전역),

설치 방식(심볼릭 링크/복사)을 차례로 선택하면 설치가 완료됩니다.

**3단계: 설치 확인**

```
$ npx skills list
```

설치된 스킬 목록에 humanizer가 표시되면 성공입니다. 이후 에이전트가 관련 작업을 수행할 때 자동으로 해당 스킬을 참조합니다.

---

## 주목할 만한 스킬들

skills.sh 리더보드에서 인기 있는 스킬 패키지 몇 가지를 소개합니다.

| 스킬 패키지 | 제공자 | 설명 |
| --- | --- | --- |
| agent-skills | Vercel Labs | React/Next.js 성능 최적화, UI 접근성 감사, 배포 자동화 등 Vercel 공식 스킬 모음 |
| anthropic skills | Anthropic | Claude Code의 기본 내장 스킬 (문서 생성, PDF, 프론트엔드 디자인 등) |
| remotion skills | Remotion | AI를 활용한 비디오 제작 워크플로우 모범 사례 |
| apollo skills | Apollo GraphQL | Apollo Client/Server, Rover CLI 활용 가이드 |
| korean-skills | daleseo | 한국어 문법 검사, AI 텍스트 자연어화 |

---

## 보안, 한 가지 주의할 점

skills.sh 생태계가 빠르게 성장하면서 보안 우려도 제기되고 있습니다. Snyk의 2026년 2월 보안 감사에 따르면, 약 3,984개 스킬을 스캔한 결과 **전체의 13.4%(534개)에서 최소 하나의 심각한 보안 문제**가 발견되었습니다. 악성 코드 배포, 프롬프트 인젝션,

하드코딩된 API 키 등이 주요 문제였죠.

일반적인 패키지와 달리 에이전트 스킬은 **에이전트의 전체 권한을 상속**받습니다. 파일 시스템, 환경 변수, API 키에 접근할 수 있다는 뜻이므로, 스킬 설치 시 출처를 반드시 확인해야 합니다.

Vercel은 이에 대응하여 Snyk와 파트너십을 맺고, `npx skills add` 실행 시 자동으로 보안 스캔을 수행하도록 했습니다.

하지만 현재 skills.sh에는 공식적인 리뷰나 인증 프로세스가 없으므로, **신뢰할 수 있는 공급자(Vercel, Anthropic, Apollo 등 공식 팀)의 스킬을 우선 사용하는 것이 안전**합니다.

---

## 마치며

- skills.sh는 AI 에이전트용 npm으로, 자연어로 된 절차적 지식을 패키지처럼 공유하는 오픈 생태계입니다. 40개 이상의 에이전트를 지원하며, CLI 한 줄로 스킬을 검색/설치/관리할 수 있습니다.
- MCP가 에이전트에게 "능력"을 준다면, Skills는 그 능력을 "잘 쓰는 방법"을 가르칩니다. 둘은 경쟁이 아닌 보완 관계이며, AI 개발의 경쟁축이 "어떤 모델을 쓰느냐"에서 "어떤 스킬을 보유했느냐"로 이동하고 있습니다.
- 보안에 주의하면서 신뢰할 수 있는 공급자의 스킬부터 시작하되, 팀만의 코딩 컨벤션이나 워크플로우를 스킬로 패키징해 재사용하는 것이 이 생태계를 활용하는 핵심 전략입니다.
- 실전 팁: 오늘 당장 `npx skills find`로 관심 있는 스킬을 검색하고, 하나를 설치해서 에이전트의 변화를 체감해보세요.

---

## 참고자료

- Introducing skills, the open agent skills ecosystem (<https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem>)
- Agent skills explained: An FAQ - Vercel (<https://vercel.com/blog/agent-skills-explained-an-faq>)
- skills CLI GitHub 저장소 (<https://github.com/vercel-labs/skills>)
- skills.sh 디렉토리 (<https://skills.sh/>)
- Vercel Introduces Skills.sh - InfoQ (<https://www.infoq.com/news/2026/02/vercel-agent-skills/>)
- Snyk: Securing the Agent Skill Ecosystem (<https://snyk.io/blog/snyk-vercel-securing-agent-skill-ecosystem/>)
- Skills vs MCP tools for agents - LlamaIndex (<https://www.llamaindex.ai/blog/skills-vs-mcp-tools-for-agents-when-to-use-what>)
- Did Skills Kill MCP? - Goose (<https://block.github.io/goose/blog/2025/12/22/agent-skills-vs-mcp/>)
- Skills explained: How Skills compares to prompts, Projects, MCP - Claude (<https://claude.com/blog/skills-explained>)
