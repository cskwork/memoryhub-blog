---
title: "? Google Antigravity Skills, AI 에이전트를 '진짜 팀원'으로 만드는 법"
date: 2026-01-15T10:53:31+09:00
slug: "970-Google-Antigravity-Skills-AI-에이전트를-진짜-팀원-으로-만드는-법"
original_url: "https://memoryhub.tistory.com/970"
tistory_id: 970
draft: false
---

```
  ╔════════════════════════════════════════════════════════════════╗
  ║                                                                ║
  ║     ┌──────────────────────────────────────────────────────┐   ║
  ║     │                    SKILL.md                          │   ║
  ║     │  ┌────────────────────────────────────────────────┐  │   ║
  ║     │  │  ---                                           │  │   ║
  ║     │  │  name: deploy-staging                          │  │   ║
  ║     │  │  description: Deploy to staging server...      │  │   ║
  ║     │  │  ---                                           │  │   ║
  ║     │  │                                                │  │   ║
  ║     │  │  # Instructions                                │  │   ║
  ║     │  │  1. Run tests                                  │  │   ║
  ║     │  │  2. Execute deploy script                      │  │   ║
  ║     │  │  3. Verify health check                        │  │   ║
  ║     │  └────────────────────────────────────────────────┘  │   ║
  ║     └──────────────────────────────────────────────────────┘   ║
  ║                            │                                   ║
  ║                            ▼                                   ║
  ║     ┌──────────────────────────────────────────────────────┐   ║
  ║     │              ANTIGRAVITY AGENT                       │   ║
  ║     │     ┌─────────┐  ┌─────────┐  ┌─────────┐            │   ║
  ║     │     │ Discover│→ │ Evaluate│→ │ Execute │            │   ║
  ║     │     │  Skills │  │Relevance│  │  Steps  │            │   ║
  ║     │     └─────────┘  └─────────┘  └─────────┘            │   ║
  ║     └──────────────────────────────────────────────────────┘   ║
  ║                                                                ║
  ║            GOOGLE  ANTIGRAVITY  AGENT  SKILLS                  ║
  ╚════════════════════════════════════════════════════════════════╝
```

"배포할 때는 항상 테스트 먼저 돌리고, staging 환경에서 확인한 다음에..." 같은 말을 AI 코딩 어시스턴트에게 매번 반복하고 있다면, 이제 그만해도 된다. Google Antigravity가 2025년 1월 14일 정식 발표한 Agent Skills는 이 문제를 정면으로 해결한다.

**한 번 정의한 워크플로우를 AI가 자동으로 인식하고, 상황에 맞게 스스로 적용하는 시스템**이다.

더 놀라운 점은 이 Skills가 오픈 표준으로, Claude Code, Gemini CLI, OpenCode 등 여러 플랫폼에서 동일하게 작동한다는 것이다.

**한줄요약:** 결론부터 말하면, Agent Skills는 SKILL.md 파일 하나로 AI 에이전트에게 팀의 작업 규칙과 절차를 학습시키는 표준화된 방법이다.

## 배경

AI 코딩 어시스턴트의 가장 큰 한계는 '기억력'이었다. 아무리 뛰어난 모델이라도 새 대화를 시작하면 이전에 설명한 팀 컨벤션, 배포 절차, 코드 리뷰 기준을 모두 잊어버린다. 결국 개발자는 같은 지시를 반복하거나, 긴 시스템 프롬프트를 매번 복사-붙여넣기 해야 했다.

> Agent Skill은 AI 에이전트가 필요할 때만 로드하는 '주문형 전문 지식 패키지'다.

기존 시스템 프롬프트와의 결정적 차이가 여기에 있다. 시스템 프롬프트는 항상 컨텍스트에 로드되어 토큰을 소비하지만, Skills는 에이전트가 현재 작업과 관련 있다고 판단할 때만 전체 내용을 로드한다. 이 '점진적 공개(Progressive Disclosure)' 설계 덕분에 수십 개의 Skill을 등록해도 성능 저하 없이 운영할 수 있다.

Skills의 기원은 Anthropic이다. Claude Code에서 처음 도입한 이 포맷이 오픈 표준(agentskills.io)으로 공개되면서,

Google Antigravity, OpenCode, Gemini CLI 등이 동일한 규격을 채택했다. 한 번 만든 Skill이 여러 플랫폼에서 재사용되는 상호운용성을 확보한 셈이다.

## Skill의 구조 이해하기

Skill은 본질적으로 **폴더 기반 패키지**다. 필수 파일인 SKILL.md와 선택적 리소스(스크립트, 템플릿, 참조 문서)로 구성된다.

```
my-skill/
├── SKILL.md           # 필수: 정의 파일
├── scripts/           # 선택: 실행 스크립트
│   ├── deploy.sh
│   └── validate.py
├── templates/         # 선택: 코드 템플릿
└── references/        # 선택: 참조 문서
```

SKILL.md 파일은 두 부분으로 나뉜다. YAML 프론트매터(메타데이터)와 마크다운 본문(상세 지시사항)이다.

```
---
name: deploy-staging
description: Deploys the current branch to staging environment. 
  Use when user asks to "deploy", "push to staging", or "test on staging server".
---

# Deploy to Staging

## Prerequisites
1. Ensure `git status` is clean
2. Run `npm run test` to verify no regressions

## Deployment Steps
1. Run `./scripts/deploy.sh staging`
2. Wait for health check to return 200 OK
3. Notify user with staging URL
```

여기서 **description 필드가 가장 중요하다**. 에이전트는 대화 시작 시 모든 Skill의 name과 description만 읽는다. 현재 작업이 특정 Skill과 관련 있다고 판단하면 그때서야 전체 SKILL.md를 로드한다. 따라서 description은 AI가 이해하기 쉽게, 트리거 키워드를 명확히 포함해야 한다.

| description 품질 | 예시 |
| --- | --- |
| 좋음 | "Generates REST API endpoint handlers in FastAPI following internal security and logging conventions. Use when creating new API endpoints." |
| 나쁨 | "API 만들기 도움" |

## Skill 저장 위치

Antigravity는 두 가지 스코프의 Skill을 지원한다.

| 위치 | 스코프 | 용도 |
| --- | --- | --- |
| `<project>/.agent/skills/` | Workspace | 프로젝트별 워크플로우, 팀 공유용 (Git 커밋 가능) |
| `~/.gemini/antigravity/skills/` | Global | 개인 유틸리티, 모든 프로젝트에서 사용 |

실전 팁으로, 새 Skill은 먼저 프로젝트 레벨(.agent/skills/)에서 테스트한다. 여러 프로젝트에서 유용하다고 검증되면 글로벌 폴더로 이동하거나 심볼릭 링크를 건다. 이렇게 하면 실험 과정에서 다른 프로젝트를 오염시키지 않는다.

## 실습: 첫 번째 Skill 만들기

가장 흔한 문제 중 하나인 '일관성 없는 커밋 메시지'를 해결하는 Skill을 만들어보자.

### 1단계: 폴더 구조 생성

```
mkdir -p .agent/skills/git-commit-formatter
touch .agent/skills/git-commit-formatter/SKILL.md
```

### 2단계: SKILL.md 작성

```
---
name: git-commit-formatter
description: Formats git commit messages according to Conventional Commits 
  specification. Use when user asks to commit changes or write a commit message.
---

# Git Commit Formatter

When writing a git commit message, follow the Conventional Commits specification.

## Format
```

```
## Allowed Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only
- **style**: Formatting, no code change
- **refactor**: Code restructuring
- **test**: Adding tests
- **chore**: Maintenance tasks

## Rules
1. Type is mandatory and lowercase
2. Scope is optional, in parentheses
3. Description starts lowercase, no period at end
4. Description must be under 72 characters
5. Body explains "what" and "why", not "how"

## Examples
- `feat(auth): add OAuth2 login support`
- `fix: resolve null pointer in user service`
- `docs(readme): update installation instructions`

## Decision Tree
- If adding new functionality → use `feat`
- If fixing a bug → use `fix`
- If changing documentation only → use `docs`
- If changing code style without logic change → use `style`
```

### 3단계: 테스트

Antigravity에서 새 대화를 시작하고 "커밋 메시지 작성해줘"라고 요청한다. 에이전트가 자동으로 Conventional Commits 형식을 따르는지 확인한다. 명시적으로 "git-commit-formatter Skill 사용해서 커밋해줘"라고 강제 호출할 수도 있다.

## 실습: 스크립트 포함 Skill

단순 지시를 넘어, 실제 스크립트를 실행하는 Skill을 만들어보자. 스테이징 배포 자동화가 좋은 예시다.

### 폴더 구조

```
.agent/skills/deploy-staging/
├── SKILL.md
└── scripts/
    └── deploy.sh
```

### SKILL.md

```
---
name: deploy-staging
description: Deploys current branch to staging environment. Use when 
  user asks to "deploy to staging", "push to staging", or "test on staging".
---

# Deploy to Staging

## Prerequisites
1. Verify `git status` is clean (no uncommitted changes)
2. Run `npm run test` and ensure all tests pass

## Deployment Process
Execute the deployment script:
```bash
./scripts/deploy.sh staging

Post-Deployment Verification
Wait for health check endpoint to return HTTP 200
Verify staging URL is accessible
Report staging URL to user
Rollback
If deployment fails:
```

```
./scripts/deploy.sh rollback
```

```
### scripts/deploy.sh

```bash
#!/bin/bash
ENV=$1

if [ "$ENV" = "staging" ]; then
    echo "Deploying to staging..."
    # 실제 배포 로직
    kubectl apply -f k8s/staging/
    echo "Deployment complete. URL: https://staging.example.com"
elif [ "$ENV" = "rollback" ]; then
    echo "Rolling back..."
    kubectl rollout undo deployment/app -n staging
fi
```

스크립트는 원자적(atomic)으로 작성한다. 하나의 스크립트가 하나의 작업만 수행하도록 설계해야 에이전트가 명확하게 호출할 수 있다.

## 모범사례/패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| 단일 책임 원칙 | 에이전트가 정확히 언제 사용할지 판단하기 쉬움 | "모든 것을 하는" 거대 Skill 피하기 |
| description에 트리거 키워드 포함 | 자동 활성화 정확도 향상 | AI 관점에서 작성 (3인칭, 명확한 동사) |
| 프로젝트 Skill 우선 | Git으로 팀 전체 공유 가능 | 검증 후 글로벌로 승격 |
| 스크립트 분리 | 결정론적 실행, 토큰 효율적 | 스크립트 인자/플래그 명확히 문서화 |
| Decision Tree 포함 | 조건부 로직 명확화 | "If...then...else" 구조 명시 |

## Rules, Workflows와의 차이

Antigravity에는 Skills 외에도 Rules와 Workflows가 있다. 혼동하기 쉬우니 차이를 명확히 하자.

| 구분 | 로드 시점 | 용도 | 저장 위치 |
| --- | --- | --- | --- |
| Rules | 항상 (시스템 프롬프트처럼) | 코드 스타일, 필수 컨벤션 강제 | `.agent/rules/`, `~/.gemini/GEMINI.md` |
| Workflows | 사용자가 `/명령어`로 호출 | 저장된 프롬프트 시퀀스 | `.agent/workflows/` |
| Skills | 에이전트가 관련성 판단 시 | 재사용 가능한 전문 지식 | `.agent/skills/`, `~/.gemini/antigravity/skills/` |

Rules는 "항상 TypeScript 사용", "docstring 필수"처럼 예외 없이 적용되어야 하는 규칙에 적합하다.

Workflows는 "새 기능 개발" 같은 멀티스텝 작업을 `/new-feature`로 한 번에 실행할 때 유용하다. Skills는 에이전트가 스스로 판단해서 적용하는 '주문형 전문성'이다.

## 마치며

- Agent Skills는 반복적인 AI 지시 문제를 해결하는 오픈 표준으로, SKILL.md 파일 하나로 에이전트의 행동을 프로그래밍할 수 있다.
- Workspace Skills(.agent/skills/)는 Git으로 팀 전체에 공유되고, Global Skills는 개인 워크플로우를 모든 프로젝트에 적용한다.
- 실전 팁: 오늘 당장 가장 자주 반복하는 지시 하나를 SKILL.md로 만들어보고, 에이전트가 자동으로 인식하는지 테스트해보자.

## 참고자료

- Google Antigravity Skills Documentation (<https://antigravity.google/docs/skills>)
- Agent Skills Open Standard (<https://agentskills.io/home>)
- Anthropic Skills Repository (<https://github.com/anthropics/skills>)
- How to Build Custom Skills in Google Antigravity - Google Cloud Community (<https://medium.com/google-cloud/tutorial-getting-started-with-antigravity-skills-864041811e0d>)
- Easily Extend Your AI with Google Antigravity Agent Skills (<https://www.xugj520.cn/en/archives/google-antigravity-agent-skills-guide-2.html>)
