---
title: "? GSD(Get Shit Done) - AI 코딩의 '컨텍스트 부패' 문제를 해결"
date: 2026-02-16T09:44:53+09:00
slug: "1031-GSD-Get-Shit-Done-AI-코딩의-컨텍스트-부패-문제를-해결"
original_url: "https://memoryhub.tistory.com/1031"
tistory_id: 1031
draft: false
---

```
  ┌─────────────────────────────────────────────┐
  │                                             │
  │    ╔═══╗ ╔═══╗ ╔══╦═╗                      │
  │    ║ ╔═╝ ║ ╔═╝ ║  ║ ║                      │
  │    ║ ║╔═╗║ ╚═╗ ║  ║ ║                      │
  │    ║ ╚╝ ║╚═╗ ║ ║  ║ ║                      │
  │    ╚═══╦╝╔═╝ ║ ╚══╩═╝                      │
  │        ╚═╝   ╚═╝                            │
  │                                             │
  │  GET SHIT DONE                              │
  │  Context Engineering for AI Coding          │
  │                                             │
  │  "복잡함은 시스템 안에, 워크플로는 단순하게"  │
  │                                             │
  └─────────────────────────────────────────────┘
```

Claude Code로 프로젝트를 만들다 보면 이상한 경험을 하게 됩니다. 처음에는 정확하고 깔끔하던 코드가, 대화가 길어질수록 점점 엉성해지는 겁니다. 지시를 무시하거나, 이전에 결정한 사항을 잊거나,

심지어 스스로 "간결하게 하겠습니다"라고 선언하며 코너를 깎기 시작합니다. 이 현상의 이름은 **'컨텍스트 부패(Context Rot)'**이며, GSD는 바로 이 문제를 정면으로 해결하기 위해 탄생한 프레임워크입니다.

**한줄요약:** 결론부터 말하면, GSD는 Claude Code의 컨텍스트 윈도우 한계를 서브에이전트 오케스트레이션과 스펙 기반 개발로 극복하는 경량 프레임워크이며, GitHub 스타 12,800개 이상을 기록하며 AI 코딩 워크플로의 새로운 표준으로 부상하고 있습니다.

---

## 배경

AI 코딩 도구의 시대가 본격적으로 열렸습니다. Claude Code, Cursor, GitHub Copilot 등이 개발자의 생산성을 크게 끌어올리고 있지만, 한 가지 근본적인 한계가 존재합니다.

> 컨텍스트 부패(Context Rot)란, LLM의 컨텍스트 윈도우에 토큰이 쌓일수록 응답 품질이 점진적으로 저하되는 현상을 말합니다.

Chroma Research의 연구에 따르면, 컨텍스트 길이가 증가할수록 모든 모델에서 성능이 일관되게 하락합니다.

Stanford 연구팀이 밝힌 'Lost in the Middle' 문제도 마찬가지입니다.

컨텍스트 윈도우의 시작과 끝에 있는 정보는 잘 찾아내지만, 중간에 묻힌 정보의 정확도는 15~20%p까지 떨어진다는 것입니다.

실제 개발 현장에서 이 문제는 더 심각합니다. Claude Code로 복잡한 프로젝트를 진행하면, 대화가 길어지면서 컨텍스트 사용량이 70~80%에 도달하는 순간 품질 저하가 체감됩니다.

Claude Code가 자동으로 수행하는 'Compaction'(대화 압축)도 근본적 해결책이 되지 못합니다.

이미 부패한 컨텍스트를 압축하는 것이기 때문에, Anthropic의 표현을 빌리면 "부패를 고정시키고 더 썩게 만드는" 결과를 낳습니다.

바로 이 지점에서 **GSD(Get Shit Done)**가 등장합니다.

---

## GSD란 무엇인가

GSD는 TACHES라는 솔로 개발자가 만든 **메타 프롬프팅, 컨텍스트 엔지니어링, 스펙 기반 개발 시스템**입니다. Claude Code, OpenCode, Gemini CLI에서 동작합니다.

핵심 철학은 단순합니다.

> "복잡함은 시스템 안에 넣고, 사용자 워크플로는 단순하게 유지한다."

기존의 스펙 기반 개발 도구들(BMAD, SpecKit, Taskmaster 등)도 존재하지만, 이들은 스프린트 세레모니, 스토리 포인트, 스테이크홀더 싱크 등 엔터프라이즈급 프로세스를 요구하는 경향이 있습니다. 1인 개발자나 소규모 팀에게는 과한 구조입니다.

GSD는 이 문제를 다르게 접근합니다. 사용자에게는 몇 개의 슬래시 커맨드만 보여주고, 내부에서는 XML 프롬프트 포맷팅, 서브에이전트 오케스트레이션, 상태 관리를 자동으로 처리합니다.

---

## 컨텍스트 부패를 해결하는 핵심 원리

GSD가 컨텍스트 부패를 해결하는 방식을 비유로 설명하면 이렇습니다. 일반적인 AI 코딩은 한 사람이 거대한 프로젝트를 혼자서, 쉬지 않고, 메모도 없이 처리하는 것과 같습니다. 당연히 뒤로 갈수록 앞의 내용을 잊게 됩니다.

GSD는 이것을 **'프로젝트 매니저 + 전문 팀'** 구조로 바꿉니다. 프로젝트 매니저(오케스트레이터)는 전체 흐름만 관리하고, 실제 작업은 매번 새로운 전문가(서브에이전트)에게 명확한 지시서와 함께 위임합니다.

구체적으로 세 가지 메커니즘이 작동합니다.

**첫째, 작업별 신선한 컨텍스트를 부여합니다.** 각 태스크 플랜은 독립된 서브에이전트에서 실행되며,

이 에이전트는 200K 토큰의 깨끗한 컨텍스트를 가지고 시작합니다. 이전 작업의 찌꺼기가 전혀 없습니다.

메인 컨텍스트 윈도우는 30~40% 수준을 유지하므로 세션이 빠르고 반응성이 좋습니다.

**둘째, XML 구조화 프롬프트로 모호성을 제거합니다.** 모든 태스크 플랜은 Claude에 최적화된 XML 형식으로 작성됩니다.

태스크 이름, 대상 파일, 구체적 행동 지침, 검증 방법, 완료 조건이 명시됩니다. AI가 추측할 여지가 없습니다.

```
<task type="auto">
  <n>로그인 엔드포인트 생성</n>
  <files>src/app/api/auth/login/route.ts</files>
  <action>
    JWT에 jose 라이브러리 사용 (jsonwebtoken은 CommonJS 이슈).
    users 테이블 대비 자격 증명 검증.
    성공 시 httpOnly 쿠키 반환.
  </action>
  <verify>curl -X POST localhost:3000/api/auth/login → 200 + Set-Cookie</verify>
  <done>유효한 자격 증명은 쿠키 반환, 무효는 401 반환</done>
</task>
```

**셋째, 마크다운 기반 컨텍스트 파일 시스템을 운용합니다.** PROJECT.md(프로젝트 비전), REQUIREMENTS.md(스코프된 요구사항), ROADMAP.md(진행 방향), STATE.md(결정 사항과 세션 간 메모리) 등이 각 에이전트에 필요한 만큼만 주입됩니다.

Claude의 품질이 저하되는 지점을 기준으로 파일 크기 제한이 설정되어 있습니다.

---

## 실제 워크플로: 5단계로 프로젝트 완성하기

### ① 프로젝트 초기화

```
npx get-shit-done-cc@latest   # 설치
/gsd:new-project               # 프로젝트 시작
```

시스템이 목표, 제약 조건, 기술 스택 선호도, 엣지 케이스 등을 파악할 때까지 질문합니다.

선택적으로 병렬 에이전트를 활용한 도메인 리서치도 수행합니다. 결과물로 PROJECT.md, REQUIREMENTS.md, ROADMAP.md, STATE.md가 생성됩니다.

이미 코드베이스가 있는 경우 `/gsd:map-codebase`를 먼저 실행하면, 병렬 에이전트가 기존 스택, 아키텍처, 컨벤션을 분석합니다.

### ② 논의 (Discuss Phase)

```
/gsd:discuss-phase 1
```

로드맵에는 각 페이즈별로 한두 줄의 설명만 있습니다. 이것만으로 사용자가 원하는 방식을 정확히 파악하기 어렵습니다.

이 단계에서 시스템은 구현의 회색 영역을 식별하고, 시각적 기능이면 레이아웃과 인터랙션을, API라면 응답 형식과 에러 처리를 묻습니다. 결과는 CONTEXT.md로 저장되어 이후 리서치와 계획 수립에 반영됩니다.

### ③ 계획 수립 (Plan Phase)

```
/gsd:plan-phase 1
```

리서처 에이전트가 구현 방법을 조사하고, 플래너가 2~3개의 원자적 태스크 플랜을 XML 구조로 작성합니다.

이후 체커 에이전트가 요구사항 커버리지, 태스크 완전성, 의존성 정확성 등 6가지 차원에서 플랜을 검증합니다.

통과할 때까지 수정-검증 루프가 반복됩니다.

### ④ 실행 (Execute Phase)

```
/gsd:execute-phase 1
```

플랜이 웨이브 단위로 실행됩니다. 독립적인 플랜은 병렬로, 의존성이 있는 것은 순차적으로 처리됩니다.

각 태스크마다 개별 Git 커밋이 생성되어, `git bisect`로 정확한 실패 지점을 찾거나 개별 태스크를 독립적으로 되돌릴 수 있습니다.

### ⑤ 검증 (Verify Work)

```
/gsd:verify-work 1
```

자동 검증으로 코드 존재와 테스트 통과를 확인한 뒤, 사용자가 직접 기능을 테스트합니다.

문제가 발견되면 디버그 에이전트가 원인을 진단하고, 검증된 수정 플랜을 자동으로 생성합니다.

이 5단계를 페이즈별로 반복하고, 마일스톤이 완료되면 `/gsd:complete-milestone`로 릴리스를 태깅한 뒤, `/gsd:new-milestone`로 다음 버전을 시작합니다.

---

## 모범사례/패턴 비교

GSD와 기존 스펙 기반 개발 도구들의 차이를 정리하면 다음과 같습니다.

| 도구 | 접근 방식 | 장점 | 주의점 |
| --- | --- | --- | --- |
| **GSD** | 서브에이전트 오케스트레이션 + 컨텍스트 분리 | 컨텍스트 부패 원천 차단, 학습 곡선 낮음, 1인/소규모 팀에 최적 | Claude Code/OpenCode/Gemini CLI에 한정 |
| **BMAD** | 애자일 팀 역할 시뮬레이션 (PM, Architect, Scrum Master) | 엔터프라이즈급 구조, 상세 PRD 자동 생성 | 설정 복잡, 소규모 프로젝트에 과함 |
| **SpecKit** | GitHub 네이티브 스펙 관리 | 도구 무관(Tool-agnostic), GitHub 생태계 통합 | 컨텍스트 부패 대응 메커니즘 부재 |
| **Taskmaster** | 태스크 분해 및 추적 | 직관적 태스크 관리 | 단일 컨텍스트 실행으로 품질 저하 가능 |

핵심 차이는 명확합니다. BMAD, SpecKit, Taskmaster는 계획, 리서치, 개발, 검증을 **하나의 컨텍스트 윈도우** 안에서 실행합니다.

GSD는 각 단계를 **독립된 서브에이전트**에 위임하여 컨텍스트 부패를 구조적으로 차단합니다.

---

## 설정과 커스터마이징

GSD는 `.planning/config.json`에 프로젝트 설정을 저장합니다.

**모델 프로필**은 각 에이전트가 사용하는 모델을 제어하여 품질과 토큰 비용을 균형 잡습니다.

| 프로필 | 계획(Planning) | 실행(Execution) | 검증(Verification) |
| --- | --- | --- | --- |
| quality | Opus | Opus | Sonnet |
| balanced (기본값) | Opus | Sonnet | Sonnet |
| budget | Sonnet | Sonnet | Haiku |

프로필 전환은 `/gsd:set-profile budget` 한 줄이면 됩니다.

**워크플로 에이전트** 토글로 리서치, 플랜 검증, 검증기를 선택적으로 활성화/비활성화할 수 있습니다.

빠른 작업에는 `/gsd:quick`으로 리서치와 검증을 건너뛰면서도 원자적 커밋과 상태 추적은 유지할 수 있습니다.

---

## 마치며

- GSD는 AI 코딩의 근본 문제인 컨텍스트 부패를 서브에이전트 오케스트레이션으로 해결하는 프레임워크입니다.
- 사용자에게는 몇 개의 슬래시 커맨드만 노출하면서, 내부에서는 리서치-계획-실행-검증의 전 과정을 자동화합니다.
- 실전 팁: `npx get-shit-done-cc@latest`로 설치한 뒤, 개인 사이드 프로젝트에서 `/gsd:new-project`부터 시작해보세요.

---

## 참고자료

- GSD 공식 GitHub (<https://github.com/gsd-build/get-shit-done>)
- Chroma Research - Context Rot 연구 (<https://research.trychroma.com/context-rot>)
- Anthropic - Effective Context Engineering for AI Agents (<https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>)
- The New Stack - Beating Context Rot in Claude Code with GSD (<https://thenewstack.io/beating-the-rot-and-getting-stuff-done/>)
- ProductTalk - Context Rot: Why AI Gets Worse the Longer You Chat (<https://www.producttalk.org/context-rot/>)
