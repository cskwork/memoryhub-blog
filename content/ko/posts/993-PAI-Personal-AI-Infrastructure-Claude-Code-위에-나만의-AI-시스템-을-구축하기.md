---
title: "? PAI(Personal AI Infrastructure), Claude Code 위에 '나만의 AI 시스템'을 구축하기"
date: 2026-01-27T07:08:51+09:00
slug: "993-PAI-Personal-AI-Infrastructure-Claude-Code-위에-나만의-AI-시스템-을-구축하기"
original_url: "https://memoryhub.tistory.com/993"
tistory_id: 993
draft: false
---

```
    ╔═══════════════════════════════════════════════╗
    ║   ┌─────────────────────────────────────┐     ║
    ║   │     PAI: Personal AI Infrastructure │     ║
    ║   │   ┌───┐  ┌───┐  ┌───┐  ┌───┐       │     ║
    ║   │   │ T │──│ E │──│ L │──│ O │──│ S │ │     ║
    ║   │   └───┘  └───┘  └───┘  └───┘  └───┘ │     ║
    ║   │         Your Goals, Your AI         │     ║
    ║   └─────────────────────────────────────┘     ║
    ╚═══════════════════════════════════════════════╝
```

Claude Code나 Cursor를 쓰면서 이런 생각 해본 적 있으신가요? "왜 매번 같은 맥락을 다시 설명해야 하지?" "내 프로젝트 구조를 왜 기억 못 하지?" **PAI는 바로 이 문제를 해결하기 위해 탄생한 오픈소스 프로젝트입니다.**

단순한 프롬프트 모음이 아니라, AI가 당신의 목표와 선호도, 작업 히스토리를 '기억'하고 스스로 개선하는 인프라입니다.

**한줄요약:** 결론부터 말하면, PAI는 Claude Code 같은 에이전트 AI 위에 구축하는 개인화 레이어로, 파일 시스템 기반의 Context 관리와 모듈형 Skill/Hook 시스템을 통해 AI를 '당신만의 디지털 어시스턴트'로 만들어줍니다.

## 배경

### Claude Code는 엔진, PAI는 나머지 전부

Claude Code, Cursor, Windsurf 같은 에이전트 AI 도구들이 폭발적으로 성장하고 있습니다. 파일을 읽고, 코드를 작성하고, 명령을 실행하는 강력한 기능을 제공합니다. 하지만 한 가지 치명적인 한계가 있습니다.

> PAI의 핵심 철학: "AI는 본질적으로 Context 관리에 관한 것이다.   
> 메모리와 지식을 시스템 내에서 어떻게 이동시키느냐가 핵심이다."

대부분의 에이전트 시스템은 **도구(Tool) 중심**으로 설계되어 있고, 사용자는 부차적인 요소로 취급됩니다.

또한 **작업(Task) 기반**이라 목표(Goal) 기반이 아닙니다. PAI는 이 패러다임을 뒤집습니다.

| 구분 | 기존 에이전트 AI | PAI |
| --- | --- | --- |
| 중심 | 도구/기능 | 사용자/목표 |
| 접근법 | 작업 단위 실행 | 목표 기반 추론 |
| 메모리 | 세션 종료 시 소멸 | 영구 저장 및 학습 |
| 개인화 | 없음 | 6개 레이어 커스터마이징 |

비유하자면, **Claude Code는 엔진이고 PAI는 그 엔진을 '당신의 차'로 만드는 모든 것**입니다.

### PAI가 제공하는 것

PAI는 Claude Code 위에 다음을 추가합니다.

첫째, **영구 메모리(Persistent Memory)**입니다. DA(Digital Assistant)가 과거 세션, 결정 사항, 학습 내용을 기억합니다.

둘째, **커스텀 스킬(Custom Skills)**입니다. 자주 하는 작업을 위한 특화된 기능을 제공합니다.

셋째, **당신의 컨텍스트**입니다. 목표, 연락처, 선호도 등을 매번 다시 설명할 필요가 없습니다.

넷째, **지능형 라우팅**입니다. "이거 리서치해줘"라고 말하면 적절한 워크플로우가 자동으로 트리거됩니다.

다섯째, **자기 개선**입니다. 시스템이 학습한 내용을 바탕으로 스스로를 수정합니다.

## PAI의 핵심 아키텍처

### USER/SYSTEM 분리 구조

PAI의 가장 중요한 설계 원칙 중 하나는 **USER 디렉토리와 SYSTEM 디렉토리의 분리**입니다. 이렇게 하면 PAI가 업그레이드되어도 사용자의 설정은 그대로 유지됩니다.

```
$PAI_DIR/  (~/.claude/)
├── USER/                    # 사용자 커스터마이징 (업그레이드 시 보존)
│   ├── ABOUTME.md          # 당신이 누구인지
│   ├── DAIDENTITY.md       # AI 성격과 음성
│   ├── TECHSTACKPREFERENCES.md  # 선호하는 기술 스택
│   ├── CONTACTS.md         # 함께 일하는 사람들
│   └── TELOS/              # Life OS (아래 상세)
│
├── SYSTEM/                  # PAI 인프라 (업그레이드 대상)
│   ├── skills/             # 기능 모듈
│   └── hooks/              # 이벤트 자동화
│
├── MEMORY/                  # 히스토리, 학습, 상태
│   ├── History/
│   ├── Learning/
│   └── Signals/
│
└── settings.json           # 설정
```

이 구조 덕분에 **포터블 아이덴티티**가 가능합니다. ~/.claude/ 폴더만 백업하면 어떤 머신에서든 동일한 AI 경험을 재현할 수 있습니다.

### TELOS: 목표 기반 Context의 핵심

TELOS는 PAI에서 가장 독특한 개념입니다. **당신이 누구인지, 무엇을 추구하는지를 구조화된 마크다운 파일로 정의**합니다. 모든 세션 시작 시 이 Context가 로드되어 AI가 당신의 목표를 이해한 상태에서 작업을 시작합니다.

```
TELOS/
├── MISSION.md      # 핵심 인생 목적
├── GOALS.md        # 구체적 목표
├── CHALLENGES.md   # 현재 장애물
├── STRATEGIES.md   # 장애물 해결 전략
├── BELIEFS.md      # 세상에 대한 믿음
├── FRAMES.md       # 사용하는 멘탈 프레임
├── MODELS.md       # 세상이 어떻게 작동하는지에 대한 이해
├── LEARNED.md      # 힘들게 얻은 교훈
├── WISDOM.md       # 수집한 인사이트
├── WRONG.md        # 마음을 바꾼 것들
├── BOOKS.md        # 사고를 형성한 책들
└── PREDICTIONS.md  # 미래에 대한 예측
```

예를 들어, GOALS.md에 "Q1까지 API 리디자인 완료"라고 적어두면, AI가 관련 없는 레거시 마이그레이션 작업에 시간을 쏟고 있을 때 "지금 이 작업이 Q1 목표와 어떻게 연결되나요?"라고 물어볼 수 있습니다.

### Memory System: 3-Tier 아키텍처

PAI의 Memory System은 **Hot/Warm/Cold 3계층 구조**로 설계되어 있습니다. 모든 상호작용에서 신호(Signal)를 캡처하고, 이를 바탕으로 시스템이 지속적으로 개선됩니다.

| 계층 | 내용 | 접근 빈도 |
| --- | --- | --- |
| Hot | 현재 세션, 활성 컨텍스트 | 실시간 |
| Warm | 최근 히스토리, 자주 쓰는 패턴 | 세션 시작 시 |
| Cold | 아카이브된 과거 데이터 | 필요 시 검색 |

```
MEMORY/
├── History/        # 세션 로그, 결정 기록
├── Learning/       # 성공/실패 패턴 분석
│   ├── Phase1/     # 초기 학습
│   ├── Phase2/     # 패턴 강화
│   └── Phase3/     # 자기 개선 적용
└── Signals/        # 평점, 감성, 검증 결과
```

**지속적 학습의 핵심**은 Signals 디렉토리입니다. 명시적 피드백(좋아요/싫어요)과 암시적 피드백(수정 여부, 재요청 등)을 모두 캡처하여 DA가 점점 더 사용자에게 맞춤화됩니다.

### Skill System: 결정론적 우선 계층

PAI의 Skill System은 **"CODE -> CLI -> PROMPT -> SKILL"** 계층을 따릅니다. 이 원칙은 일관된 결과를 최우선으로 합니다.

> "bash 스크립트로 해결할 수 있다면, AI를 쓰지 마라. SQL 쿼리로 해결할 수 있다면, AI를 쓰지 마라. 실제로 지능이 필요한 부분에만 AI를 써라."

이 원칙 덕분에 비용이 절감되고 신뢰성이 높아집니다.

```
skills/
├── CORE/               # 핵심 라우팅 및 아이덴티티
├── pai-research-skill/ # 멀티소스 리서치
├── pai-browser-skill/  # Playwright 브라우저 자동화
├── pai-telos-skill/    # Life OS 및 목표 캡처
└── ...
```

각 스킬은 **자체 완결형**입니다. 코드, 워크플로우, 설치 지침, 검증 테스트를 모두 포함하고 있어 AI가 직접 읽고 설치할 수 있습니다.

### Hook System: 8가지 이벤트 타입

Hook System은 **라이프사이클 이벤트에 반응**합니다. 세션 시작, 도구 사용, 작업 완료 등 8가지 이벤트 타입을 지원합니다.

| 이벤트 | 설명 | 활용 예 |
| --- | --- | --- |
| session\_start | 세션 시작 | 컨텍스트 자동 로드 |
| tool\_use | 도구 호출 | 보안 검증 |
| task\_complete | 작업 완료 | 음성 알림, 세션 캡처 |
| pre\_command | 명령 실행 전 | AllowList 검증 |

```
// 예: 세션 시작 시 TELOS 컨텍스트 로드
hooks.on('session_start', async () => {
  await loadContext('USER/TELOS/');
  await loadContext('USER/ABOUTME.md');
});

// 예: 위험한 명령 차단
hooks.on('pre_command', async (cmd) => {
  if (!isAllowed(cmd)) {
    throw new SecurityError('Command not in AllowList');
  }
});
```

Hook 덕분에 `--dangerously-skip-permissions` 없이도 원활한 워크플로우가 가능합니다. PAI의 보안 훅이 실행 전에 명령을 검증하여 위험한 작업은 차단하면서 정상 워크플로우는 부드럽게 진행됩니다.

## 실습: PAI 설치 및 기본 설정

### 1단계: Full Release 설치 (권장)

가장 빠르게 동작하는 PAI 시스템을 얻는 방법입니다.

```
# 리포지토리 클론
git clone https://github.com/danielmiessler/PAI.git
cd PAI/Releases/v2.4

# 기존 Claude Code 설정 백업 (있다면)
[ -d ~/.claude ] && mv ~/.claude ~/.claude-backup-$(date +%Y%m%d)

# PAI 설치 복사
cp -r .claude ~/

# 설정 위자드 실행
cd ~/.claude && bun run PAIInstallWizard.ts
```

위자드가 묻는 것들은 다음과 같습니다. 당신의 이름, DA 이름(예: Kai), 타임존, 환경 변수 설정(bash/zsh 자동 감지), 음성 선호도(선택사항)입니다.

설치 후 **Claude Code를 재시작**하면 Hook이 활성화됩니다.

### 2단계: TELOS 설정

~/.claude/USER/TELOS/ 디렉토리의 파일들을 편집합니다. 최소한 다음 세 파일은 작성하는 것을 권장합니다.

```
<!-- MISSION.md 예시 -->
# 핵심 미션
- 개발자 경험(DX)을 혁신하는 도구 만들기
- 기술 지식을 접근 가능하게 공유하기

<!-- GOALS.md 예시 -->
# 2026 Q1 목표
- [ ] 오픈소스 프로젝트 v2.0 릴리즈
- [ ] 기술 블로그 월 4회 포스팅
- [ ] 영어 기술 문서 작성 능력 향상

<!-- CHALLENGES.md 예시 -->
# 현재 장애물
- 시간 관리: 야간 코딩으로 인한 수면 부족
- 기술적: 대규모 리팩토링 필요하나 테스트 커버리지 부족
```

### 3단계: 개별 Pack 추가 설치

필요한 기능만 선택적으로 설치할 수 있습니다. Claude Code에서 다음과 같이 요청합니다.

```
이 Pack을 설치해줘. PAI_DIR="~/.claude"로 설정하고 
hooks 설정, 코드 저장, 동작 검증까지 해줘.
```

유용한 Skill Pack 추천 목록입니다. 리서치용으로는 pai-research-skill(멀티소스 리서치), 개발용으로는 pai-browser-skill(Playwright 자동화), 생산성용으로는 pai-telos-skill(목표 추적)을 권장합니다.

## 6개 레이어 커스터마이징

PAI는 6개 레이어에서 커스터마이징이 가능합니다. 기본값으로 시작해서 필요할 때 점진적으로 수정하면 됩니다.

| 레이어 | 파일 위치 | 용도 |
| --- | --- | --- |
| Identity | USER/DAIDENTITY.md | AI 이름, 성격, 음성 |
| Preferences | USER/TECHSTACKPREFERENCES.md | 기술 스택, 도구 |
| Workflows | skills/\*/workflow.md | 스킬 실행 방식 |
| Skills | skills/ | 기능 정의 |
| Hooks | hooks/ | 이벤트 처리 방식 |
| Memory | MEMORY/ | 캡처 대상 |

## 마치며

- PAI는 Claude Code 같은 에이전트 AI를 '나만의 디지털 어시스턴트'로 변환하는 오픈소스 인프라입니다.
- 핵심은 파일 시스템 기반 Context 관리(TELOS), 3계층 Memory System, 결정론적 Skill 계층입니다.
- 모듈형 설계로 필요한 기능만 선택 설치하고, USER/SYSTEM 분리로 업그레이드해도 설정이 보존됩니다.

**실전 팁:** 오늘 당장 ~/.claude/USER/TELOS/GOALS.md 파일 하나만 작성해보세요. 그것만으로도 AI가 당신의 맥락을 이해하기 시작합니다.

## 참고자료

- PAI GitHub 리포지토리 (<https://github.com/danielmiessler/Personal_AI_Infrastructure>)
- Building a Personal AI Infrastructure - Daniel Miessler 블로그 (<https://danielmiessler.com/blog/personal-ai-infrastructure>)
- A Personal AI Maturity Model - Daniel Miessler 블로그 (<https://danielmiessler.com/blog/personal-ai-maturity-model>)
