---
title: "? oh-my-opencode 완벽 가이드: AI 코딩 도구를 팀으로 진화시키는 방법"
date: 2026-01-22T23:05:04+09:00
slug: "987-oh-my-opencode-완벽-가이드-AI-코딩-도구를-팀으로-진화시키는-방법"
original_url: "https://memoryhub.tistory.com/987"
tistory_id: 987
draft: false
---

```
    ┌─────────────────────────────────────────────────┐
    │                                                 │
    │   ╔═══╗ ╔╗ ╔╗     ╔═╗╔═╗╔╗ ╔╗                  │
    │   ║╔═╗║ ║║ ║║     ║║╚╝║║║╚═╝║                  │
    │   ║║ ║║ ║╚═╝║     ║╔╗╔╗║╚═╗╔╝                  │
    │   ║║ ║║ ║╔═╗║     ║║║║║║  ║║                   │
    │   ║╚═╝║ ║║ ║║     ║║║║║║  ║║                   │
    │   ╚═══╝ ╚╝ ╚╝     ╚╝╚╝╚╝  ╚╝                   │
    │                                                 │
    │   ╔═══╗ ╔═══╗ ╔═══╗ ╔═╗  ╔╗ ╔═══╗ ╔═══╗ ╔═══╗ │
    │   ║╔═╗║ ║╔═╗║ ║╔══╝ ║║╚╗ ║║ ║╔═╗║ ║╔═╗║ ║╔══╝ │
    │   ║║ ║║ ║╚═╝║ ║╚══╗ ║╔╗╚╗║║ ║║ ╚╝ ║║ ║║ ║║╔═╗ │
    │   ║║ ║║ ║╔══╝ ║╔══╝ ║║╚╗║║║ ║║ ╔╗ ║║ ║║ ║║╚╗║ │
    │   ║╚═╝║ ║║    ║╚══╗ ║║ ╚╝║║ ║╚═╝║ ║╚═╝║ ║╚═╝║ │
    │   ╚═══╝ ╚╝    ╚═══╝ ╚╝  ╚═╝ ╚═══╝ ╚═══╝ ╚═══╝ │
    │                                                 │
    │        [ AI 에이전트 팀을 만드는 마법 ]         │
    │                                                 │
    │     Sisyphus  +  Oracle  +  Librarian  +  ...  │
    │           ↓         ↓          ↓               │
    │        병렬 작업으로 생산성 168배 향상          │
    │                                                 │
    └─────────────────────────────────────────────────┘
```

Claude Code가 7일 걸릴 작업을 1시간에 끝낸다면 믿으시겠습니까? 8,000개의 ESLint 경고를 하루 만에 처리했다는 후기가 쏟아지는 프로젝트가 있습니다. 바로 oh-my-opencode입니다. 단일 AI 에이전트로 코딩하던 시대는 지나가고 있습니다.

**이제는 전문화된 AI 팀이 병렬로 협업하는 시대입니다.**

**한줄요약:** oh-my-opencode는 OpenCode 위에서 동작하는 플러그인으로, 단일 AI 에이전트를 7개의 전문 에이전트 팀으로 변환하여 작업 완료까지 절대 멈추지 않는 시스템을 구축해 줍니다.

## 배경

AI 코딩 도구 시장이 급변하고 있습니다. GitHub Copilot으로 시작된 코드 완성 시대를 지나, ChatGPT와 Claude가 대화형 코드 생성을 가능케 했고, Claude Code와 OpenCode가 터미널에서 직접 파일을 읽고 수정하는 에이전트 시대를 열었습니다.

그런데 여기서 한 가지 근본적인 문제가 있었습니다. 아무리 똑똑한 AI라도 혼자서 모든 일을 처리하려면 한계가 있다는 점입니다.

> **에이전트 하네스(Agent Harness)란?** 여러 AI 에이전트를 감싸서 제어하고 조율하는 "관제탑" 역할의 프레임워크입니다. 마치 말을 제어하는 마구(고삐)처럼 AI들을 통제합니다.

oh-my-opencode는 한국인 개발자 김영규(YeonGyu Kim)가 개발한 프로젝트입니다. 본인이 **$24,000 상당의 토큰을 소비하며** 직접 검증한 설정을 플러그인으로 패키징하여 공개했습니다.

출시 2주 만에 3,400개 스타를 달성했고, 현재(2026년 1월 기준) **21,000개 이상의 GitHub 스타**를 기록하며 개발자 커뮤니티에서 뜨거운 반응을 얻고 있습니다.

### 순정 OpenCode vs oh-my-opencode 핵심 비교

| 구분 | 순정 OpenCode | oh-my-opencode |
| --- | --- | --- |
| 에이전트 구성 | build/plan + @general (3개) | Sisyphus + 6개 전문 에이전트 (7개) |
| 모델 선택 | 단일 모델 사용 | 역할별 최적 모델 자동 배정 |
| 작업 방식 | 순차 실행 | 병렬 백그라운드 실행 |
| 작업 완료 보장 | 수동 확인 필요 | Todo Enforcer 자동 지속 |
| 개발 도구 | 기본 8개 | LSP/AstGrep 추가 |
| MCP 서버 | 수동 설정 필요 | Exa, Context7, Grep.app 기본 포함 |

## 핵심 개념: Sisyphus와 에이전트 팀

> **Sisyphus(시시포스):** 그리스 신화에서 영원히 바위를 굴려 올리는 인물처럼, 작업이 완료될 때까지 절대 멈추지 않는 메인 오케스트레이터 에이전트입니다.

oh-my-opencode의 철학은 단순합니다. **혼자 일하는 AI를 팀으로 협업하는 AI로 바꾼다는 것**입니다.

오케스트라에 비유하면 Sisyphus는 지휘자이고, 나머지 에이전트들은 각자의 악기를 연주하는 전문 연주자입니다.

### 전문화된 에이전트 구성

| 에이전트 | 역할 | 기본 모델 | 호출 방법 |
| --- | --- | --- | --- |
| Sisyphus | 메인 오케스트레이터 | Claude Opus 4.5 (32k) | 기본 활성화 |
| Oracle | 아키텍처 설계, 디버깅 | GPT-5.2 Medium | @oracle |
| Librarian | 공식 문서 탐색 | GLM-4.7 Free | @librarian |
| Explore | 초고속 코드베이스 탐색 | Grok Code | @explore |
| Frontend UI/UX | 프론트엔드 개발 | Gemini 3 Pro | 자동 호출 |
| Document-Writer | README, API 문서 작성 | Gemini 3 Flash | 자동 호출 |
| Multimodal-Looker | PDF, 이미지 분석 | Gemini 3 Flash | 자동 호출 |

각 에이전트는 역할에 따라 **파일 권한과 실행 모드**가 다르게 설정됩니다.

예를 들어 Oracle은 Read Only 권한으로 분석만 담당하고,

Frontend UI/UX는 Read+Write 권한으로 직접 코드를 수정합니다.

### Aggressive Delegation 전략

Sisyphus의 핵심 전략은 "공격적 위임"입니다. 가능한 모든 작업을 전문 에이전트에게 위임하여 세 가지 이점을 얻습니다.

**첫째**, 메인 컨텍스트가 불필요한 정보로 오염되지 않습니다.

**둘째**, 여러 작업이 동시에 백그라운드에서 진행됩니다.

**셋째**, 각 작업에 가장 적합한 모델이 자동 선택됩니다.

## 실습: 설치 및 설정

### 사전 요구사항

설치 전에 다음 조건을 확인해야 합니다.

- OpenCode 버전 1.0.150 이상
- Claude Pro/Max, ChatGPT Plus/Pro, Google Gemini 중 하나 이상 구독
- Node.js 환경 (bun 또는 npm 실행 가능)

### 1단계: oh-my-opencode 설치

터미널에서 다음 명령어를 실행합니다.

```
# bun 사용 (권장)
bunx oh-my-opencode install

# npm 사용 (Ubuntu/Debian Snap 환경)
npx oh-my-opencode install
```

설치 과정에서 Claude, OpenAI, Gemini 구독 여부를 물어봅니다. 본인이 사용 중인 서비스에 맞게 선택하면 됩니다.

### 2단계: LLM 제공자 인증

각 LLM 제공자에 대한 인증을 설정합니다.

**중요 업데이트(2026년 1월):** Anthropic이 Claude Code OAuth 토큰을 공식 Claude Code에서만 사용 가능하도록 기술적 제한을 적용했습니다. 제3자 도구에서 OAuth 방식을 사용하면 ToS 위반으로 간주되어 계정 밴 사례가 발생하고 있습니다.

**Anthropic API 키 방식을 사용하는 것을 권장합니다.**

```
# OpenAI 인증
opencode auth login
# 제공자 목록에서 "OPEN AI" 선택 후 OAuth 흐름 완료

# Google Gemini 인증
opencode auth login
# 제공자 목록에서 "Google" 선택 후 OAuth 흐름 완료
# 최대 10개 계정 지원 (자동 로드밸런싱)
```

Gemini 인증 시 Antigravity를 통한 방식을 선택하면 여러 Google 계정을 등록하여 rate limit 문제를 우회할 수 있습니다.

### 3단계: 설치 확인

```
# OpenCode 버전 확인 (1.0.150 이상 필요)
opencode --version

# 인증 상태 확인
opencode auth list

# 사용 가능한 모델 확인
opencode models google | grep gemini-3
```

### 4단계: 설정 파일 이해하기

oh-my-opencode의 설정 파일은 다음 위치에 저장됩니다.

```
# 글로벌 설정 디렉토리
~/.config/opencode/
├── opencode.json           # 플러그인 및 provider 설정
├── oh-my-opencode.json     # 에이전트별 모델 매핑
└── antigravity-accounts.json

# 프로젝트별 설정 (글로벌 설정보다 우선 적용)
프로젝트루트/.opencode/
└── oh-my-opencode.json
```

에이전트별 모델을 직접 지정하고 싶다면 `oh-my-opencode.json`을 수정합니다.

```
{
  "$schema": "https://raw.githubusercontent.com/code-yeongyu/oh-my-opencode/master/assets/oh-my-opencode.schema.json",
  "google_auth": true,
  "agents": {
    "Sisyphus": {
      "model": "anthropic/claude-opus-4-5"
    },
    "oracle": {
      "model": "openai/gpt-5.2"
    },
    "librarian": {
      "model": "google/gemini-3-flash"
    }
  }
}
```

## 사용법: ultrawork 키워드

oh-my-opencode의 모든 기능을 활성화하는 가장 간단한 방법은 프롬프트에 `ultrawork` 또는 `ulw`를 포함하는 것입니다.

```
이 프로젝트를 분석하고 리팩토링 계획을 세워줘 ultrawork

로그인 기능을 구현해줘 ulw

8000개의 ESLint 경고를 모두 수정해줘 ultrawork
```

ultrawork 키워드 하나로 다음 기능이 자동 활성화됩니다.

- 병렬 에이전트 실행
- 백그라운드 작업 활성화
- Todo Continuation Enforcer 작동
- 전문 에이전트 자동 위임
- 완료까지 지속 실행

특정 에이전트를 직접 호출하고 싶다면 @ 멘션을 사용합니다.

```
@oracle 이 시스템의 아키텍처를 어떻게 개선하면 좋을까?

@librarian React Query v5의 새로운 API 문서 찾아줘

@explore 이 프로젝트에서 인증 관련 코드가 어디에 있는지 찾아줘
```

## 모범사례/패턴 비교

| 사용 방식 | 적합한 상황 | 장점 | 주의점 |
| --- | --- | --- | --- |
| ultrawork | 복잡한 멀티스텝 작업 | Sisyphus가 자동으로 최적 에이전트 선택 | 토큰 소비가 많을 수 있음 |
| @oracle | 설계/디버깅 질문 | GPT-5.2로 깊은 분석 가능 | 응답 시간이 길 수 있음 |
| @librarian | 문서/코드 검색 | 빠른 리서치 결과 | 최신 문서가 아닐 수 있음 |
| @explore | 코드베이스 탐색 | 가장 빠른 응답 | 깊은 분석에는 부적합 |
| 순정 OpenCode | 단순 작업, 빠른 프로토타이핑 | 비용 효율적 | 복잡한 작업에 한계 |

## 마치며

- oh-my-opencode는 단일 AI 에이전트를 **7개의 전문 에이전트 팀**으로 변환하는 OpenCode 플러그인입니다.
- Sisyphus 오케스트레이터가 작업을 분배하고, Todo Enforcer가 **완료까지 멈추지 않는 실행**을 보장합니다.
- `ultrawork` 키워드 하나로 병렬 작업, 자동 위임, 컨텍스트 관리가 모두 활성화됩니다.

**실전 팁:** 오늘 당장 `bunx oh-my-opencode install` 명령어로 설치하고, 프로젝트에서 "이 코드를 분석해줘 ultrawork"를 입력해 보세요.

## 참고자료

- oh-my-opencode 공식 GitHub (<https://github.com/code-yeongyu/oh-my-opencode>)
- OpenCode 공식 사이트 (<https://opencode.ai/>)
- Oh My OpenCode 공식 문서 (<https://ohmyopencode.com/>)
- 갓대희's 작은공간 - OpenCode 리뷰 시리즈 (<https://goddaehee.tistory.com/485>)
