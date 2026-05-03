---
title: "? Claude Code Plugin, 팀 전체 AI 개발환경을 5분 만에 통일하는 법"
date: 2025-12-08T22:15:17+09:00
slug: "924-Claude-Code-Plugin-팀-전체-AI-개발환경을-5분-만에-통일하는-법"
original_url: "https://memoryhub.tistory.com/924"
tistory_id: 924
draft: false
categories: ["데브 라이브러리"]
tags: ["Claude"]
---

```
     ┌─────────────────────────────────────┐
     │    ┌───┐  ┌───┐  ┌───┐             │
     │    │ P │  │ L │  │ U │  MARKETPLACE │
     │    │ L │→ │ U │→ │ G │  ═══════════ │
     │    │ U │  │ G │  │ I │   /plugin    │
     │    │ G │  │ I │  │ N │   install    │
     │    └───┘  └───┘  └───┘              │
     │         CLAUDE CODE                 │
     │    ┌──────────────────────┐         │
     │    │  ? → ? → ? → 팀   │         │
     │    └──────────────────────┘         │
     └─────────────────────────────────────┘
```

"팀원마다 Claude Code 설정이 달라서 협업할 때 혼란스럽다."  
"내가 만든 유용한 슬래시 커맨드를 동료에게 공유하고 싶은데 방법이 번거롭다."

이런 경험이 있다면 플러그인 마켓플레이스가 해답입니다.

**Claude Code 플러그인 마켓플레이스는 스마트폰 앱스토어처럼, AI 코딩 도구의 확장 기능을 한 곳에서 검색하고 설치하며 팀 전체에 배포할 수 있게 해주는 시스템입니다.**

**한줄요약:** 결론부터 말하면, 플러그인 마켓플레이스는 Claude Code의 슬래시 커맨드, 에이전트, MCP 서버, 훅을 팀 단위로 표준화하여 배포하는 JSON 기반 카탈로그 시스템입니다.

## 배경

2025년 10월 9일, Anthropic은 Claude Code 플러그인 시스템을 공개 베타로 출시했습니다. 기존에는 개발자가 슬래시 커맨드나 에이전트를 직접 설정해야 했고, 이를 팀원과 공유하려면 설정 파일을 일일이 복사하거나 문서로 안내해야 했습니다. 플러그인 마켓플레이스는 이 문제를 근본적으로 해결합니다.

마켓플레이스가 필요한 이유는 세 가지입니다.

첫째, 팀 표준화입니다. 모든 팀원이 동일한 코드 리뷰 에이전트, 배포 자동화 커맨드를 사용할 수 있습니다.

둘째, 버전 관리입니다. 플러그인 업데이트를 중앙에서 관리하고 자동으로 반영할 수 있습니다.

셋째, 생태계 확장입니다. 커뮤니티가 만든 243개 이상의 플러그인을 바로 활용할 수 있습니다.

핵심 용어를 정리하면 다음과 같습니다.

| 용어 | 설명 |
| --- | --- |
| 플러그인 | 슬래시 커맨드, 에이전트, MCP 서버, 훅을 묶은 패키지 |
| 마켓플레이스 | 플러그인 목록과 설치 정보를 담은 JSON 파일 |
| MCP 서버 | Model Context Protocol 기반 외부 도구 연결 서버 |
| 훅 | Claude Code 동작의 특정 시점에 실행되는 자동화 스크립트 |

## 핵심

> 한 줄 정의: 마켓플레이스는 플러그인의 이름, 출처, 버전 정보를 담은 JSON 파일이며, Git 저장소나 로컬 경로에서 호스팅됩니다.

마켓플레이스를 스마트폰 앱스토어에 비유하면 이해가 쉽습니다. 앱스토어가 수천 개의 앱을 카테고리별로 정리하고 원클릭 설치를 제공하듯, Claude Code 마켓플레이스도 플러그인을 한 곳에 모아 `/plugin install` 명령 하나로 설치할 수 있게 합니다. 차이점이 있다면, 누구나 자신만의 마켓플레이스를 만들어 팀 내부용으로 운영할 수 있다는 것입니다.

마켓플레이스 파일의 기본 구조는 다음과 같습니다.

```
{
  "name": "team-tools",
  "owner": {
    "name": "DevOps Team",
    "email": "devops@company.com"
  },
  "plugins": [
    {
      "name": "code-formatter",
      "source": "./plugins/formatter",
      "description": "저장 시 자동 코드 포맷팅",
      "version": "2.1.0"
    }
  ]
}
```

**핵심 필드 세 가지만 기억하면 됩니다.** `name`은 마켓플레이스 식별자, `owner`는 관리자 정보, `plugins`는 설치 가능한 플러그인 목록입니다. 각 플러그인은 로컬 경로, GitHub 저장소, 또는 임의의 Git URL을 소스로 지정할 수 있습니다.

플러그인 소스 유형별 설정 방식은 다음과 같습니다.

| 소스 유형 | 설정 예시 | 사용 시점 |
| --- | --- | --- |
| 로컬 경로 | `"source": "./plugins/my-plugin"` | 같은 저장소 내 플러그인 |
| GitHub | `"source": {"source": "github", "repo": "owner/repo"}` | 공개 GitHub 저장소 |
| Git URL | `"source": {"source": "url", "url": "https://..."}` | GitLab 등 기타 Git 호스팅 |

## 실습

### ① 마켓플레이스 추가하기

Claude Code에서 외부 마켓플레이스를 추가하는 방법은 세 가지입니다. GitHub 저장소를 추가하려면 `/plugin marketplace add owner/repo` 형식을 사용합니다. Git URL을 직접 지정하려면 `/plugin marketplace add https://gitlab.com/company/plugins.git`처럼 전체 주소를 입력합니다. 로컬 개발 환경에서 테스트하려면 `/plugin marketplace add ./my-marketplace`로 디렉토리 경로를 지정합니다.

커뮤니티에서 인기 있는 마켓플레이스 중 하나를 추가해보겠습니다.

```
# Anthropic 공식 예제 마켓플레이스 추가
/plugin marketplace add anthropics/claude-code
```

### ② 플러그인 설치하기

마켓플레이스를 추가한 후에는 개별 플러그인을 설치할 수 있습니다. 특정 플러그인을 직접 설치하려면 `/plugin install plugin-name@marketplace-name` 형식을 사용합니다. 어떤 플러그인이 있는지 모른다면 `/plugin` 명령으로 대화형 브라우저를 열어 탐색할 수 있습니다.

```
# 코드 리뷰 플러그인 설치
/plugin install code-review@anthropics

# 프론트엔드 디자인 플러그인 설치
/plugin install frontend-design@anthropics
```

### ③ 팀 프로젝트에 자동 설치 설정하기

팀 전체가 동일한 플러그인을 사용하도록 강제하려면 프로젝트의 `.claude/settings.json` 파일에 마켓플레이스를 지정합니다. 팀원이 해당 프로젝트 폴더를 신뢰하면 Claude Code가 지정된 마켓플레이스와 플러그인을 자동으로 설치합니다.

```
{
  "extraKnownMarketplaces": {
    "team-tools": {
      "source": {
        "source": "github",
        "repo": "your-org/claude-plugins"
      }
    }
  },
  "enabledPlugins": ["code-formatter", "deployment-tools"]
}
```

이 설정의 핵심은 `enabledPlugins` 필드입니다. 여기에 나열된 플러그인은 팀원이 저장소를 열 때 자동으로 활성화됩니다.

### ④ 자체 마켓플레이스 만들기

회사 전용 플러그인을 배포하려면 자체 마켓플레이스를 구축해야 합니다. Git 저장소 루트에 `.claude-plugin/marketplace.json` 파일을 생성합니다. 필수 필드인 `name`, `owner`, `plugins`를 작성하고, 각 플러그인의 소스 경로를 지정합니다. 저장소를 GitHub나 GitLab에 푸시하면 팀원들이 `/plugin marketplace add` 명령으로 추가할 수 있습니다.

마켓플레이스를 배포하기 전에 검증하는 것이 좋습니다.

```
# JSON 구문 검증
claude plugin validate .

# 로컬 테스트
/plugin marketplace add ./path/to/marketplace
/plugin install test-plugin@marketplace-name
```

## 모범사례/패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| GitHub 호스팅 | 버전 관리, 이슈 트래킹, 협업 기능 내장 | 비공개 저장소는 접근 권한 설정 필요 |
| 로컬 마켓플레이스 | 배포 전 빠른 테스트 가능 | 팀 공유 불가, 개발 용도로만 사용 |
| settings.json 자동 설치 | 팀 표준화 자동 적용 | 폴더 신뢰 설정 필요, 첫 설정 시 안내 필요 |
| strict: false 설정 | plugin.json 없이 마켓플레이스 항목만으로 동작 | 복잡한 플러그인에는 부적합 |

## 마치며

- 플러그인 마켓플레이스는 Claude Code 확장 기능을 중앙에서 관리하고 팀 전체에 배포하는 JSON 기반 카탈로그입니다.
- `/plugin marketplace add` 명령으로 외부 마켓플레이스를 추가하고, `.claude/settings.json`으로 팀 자동 설치를 설정할 수 있습니다.
- 실전 팁: 오늘 당장 `/plugin marketplace add anthropics/claude-code`를 실행해서 공식 예제 플러그인을 설치해보세요.

## 참고자료

- Claude Code Plugin Marketplaces 공식 문서 (<https://code.claude.com/docs/en/plugin-marketplaces>)
- Anthropic 공식 플러그인 발표 (<https://www.anthropic.com/news/claude-code-plugins>)
- Claude Code Plugins Marketplace 커뮤니티 (<https://claudecodemarketplace.com/>)
- Claude Plugins CLI (<https://claude-plugins.dev/>)
