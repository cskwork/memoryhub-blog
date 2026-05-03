---
title: "?️ Atlassian CLI 완벽 가이드: Jira 클릭 지옥에서 탈출하는 법"
date: 2025-12-19T10:00:35+09:00
slug: "940-Atlassian-CLI-완벽-가이드-Jira-클릭-지옥에서-탈출하는-법"
original_url: "https://memoryhub.tistory.com/940"
tistory_id: 940
draft: false
categories: ["데브 컨셉"]
tags: ["Tech News"]
---

```
    ___  ________    _____ 
   /   |/_  __/ /   /  ___|
  / /| | / / / /    \__ \ 
 / ___ |/ / / /___  ___/ / 
/_/  |_/_/ /_____/ /____/  

  Atlassian CLI (ACLI)
  터미널에서 Jira를 제어하다
```

Jira에서 100개 이슈의 상태를 변경해야 한다고 상상해 보자. 하나씩 클릭한다면 최소 30분은 걸린다. 그런데 터미널에서 단 한 줄로 끝낼 수 있다면? **Atlassian CLI(ACLI)는 Jira, Confluence 등 Atlassian 제품을 명령줄에서 직접 제어할 수 있게 해주는 공식 도구**다. 2025년 5월 전체 Jira Cloud 플랜에 정식 출시되면서, 이제 누구나 무료로 사용할 수 있다.

**한줄요약:** Atlassian CLI(ACLI)는 Jira, Confluence 작업을 터미널에서 자동화하는 공식 CLI 도구로, 대량 작업과 스크립팅이 가능하다.

## 배경

Jira와 Confluence는 전 세계 개발팀의 표준 도구가 되었다. 하지만 프로젝트 규모가 커지면 문제가 생긴다. 수천 개의 이슈, 수십 개의 프로젝트, 여러 사이트를 관리하려면 GUI만으로는 한계가 있다.

> ACLI(Atlassian Command Line Interface)는 텍스트 기반 명령어로 Atlassian 제품과 상호작용하는 도구다.

기존에는 Appfire(구 Bob Swift)의 서드파티 CLI가 유일한 선택지였다. 그러나 2025년 5월, Atlassian이 공식 ACLI를 출시하면서 상황이 바뀌었다. 공식 ACLI는 모든 Jira Cloud 플랜에 무료로 포함되어 있으며, Java 없이 독립 실행 가능한 바이너리로 제공된다.

| 구분 | 공식 Atlassian ACLI | Appfire ACLI (서드파티) |
| --- | --- | --- |
| 출시 | 2025년 5월 | 2008년 (Bob Swift) |
| 비용 | 무료 (Jira Cloud 포함) | 유료 라이선스 필요 |
| 설치 | 독립 바이너리 (Homebrew/curl) | Java 필요 + 커넥터 앱 |
| 지원 범위 | Jira Cloud 중심 | Jira/Confluence/Bitbucket/Bamboo |
| 명령어 스타일 | `acli jira workitem create` | `acli myjira --action createIssue` |

이 글에서는 **공식 Atlassian ACLI**에 집중한다. 서드파티 솔루션이 필요한 경우 Appfire 문서를 참고하자.

## 왜 CLI인가: GUI vs CLI 비교

CLI를 사용해야 하는 이유를 구체적인 시나리오로 살펴보자.

**시나리오: 50개 이슈를 "In Progress"로 변경**

GUI 방식은 각 이슈를 열고, 상태 드롭다운을 클릭하고, 저장하는 과정을 50번 반복해야 한다. CLI 방식은 JQL로 대상을 지정하고 한 번에 처리한다.

```
acli jira workitem transition --jql "project = TEAM AND status = 'To Do'" --status "In Progress"
```

**ACLI의 핵심 장점**은 세 가지로 요약된다. 첫째, 속도다. UI에서 수십 분 걸리는 대량 작업을 몇 초 만에 처리한다. 둘째, 자동화다. 스크립트로 만들어 CI/CD 파이프라인이나 크론잡에 통합할 수 있다. 셋째, 정밀 제어다. 각 명령을 검증하고 단계별로 실행할 수 있어 실수 위험이 줄어든다.

## 실습

### 1. 설치하기

운영체제별 설치 방법이 다르다. ACLI는 macOS, Windows, Linux를 모두 지원한다.

**macOS (Homebrew 권장)**

```
# Homebrew tap 추가 후 설치
brew tap atlassian/homebrew-acli
brew install acli

# 설치 확인
acli --version
```

**macOS (수동 설치 - Apple Silicon)**

```
# 바이너리 다운로드
curl -LO "https://acli.atlassian.com/darwin/latest/acli_darwin_arm64/acli"

# 실행 권한 부여
chmod +x acli

# PATH에 추가 (선택)
sudo mv acli /usr/local/bin/
```

**Windows (PowerShell)**

Atlassian 공식 사이트에서 Windows용 바이너리를 다운로드한 후 PATH에 추가한다.

**Linux (Debian/Ubuntu)**

```
curl -LO "https://acli.atlassian.com/linux/latest/acli_linux_amd64/acli"
chmod +x acli
sudo mv acli /usr/local/bin/
```

### 2. 인증 설정

ACLI는 API 토큰 또는 OAuth 두 가지 인증 방식을 지원한다.

**방법 A: OAuth (가장 간편)**

```
acli jira auth login --web
```

브라우저가 열리면 Atlassian 계정으로 로그인하고 사이트를 선택한다. 터미널로 돌아오면 인증이 완료된다.

**방법 B: API 토큰**

먼저 Atlassian 계정 설정([https://id.atlassian.com/manage/api-tokens)에서](https://id.atlassian.com/manage/api-tokens)%EC%97%90%EC%84%9C) API 토큰을 생성한다.

```
# 토큰 파일에서 읽기
acli jira auth login --site "mysite.atlassian.net" --email "user@example.com" --token < token.txt

# 또는 직접 입력
echo "YOUR_API_TOKEN" | acli jira auth login --site "mysite.atlassian.net" --email "user@example.com" --token
```

### 3. 주요 명령어 실습

**프로젝트 목록 조회**

```
# 최근 조회한 프로젝트 20개
acli jira project list --recent

# 모든 프로젝트 (페이지네이션 적용)
acli jira project list --paginate

# JSON 형식으로 출력
acli jira project list --limit 50 --json
```

**이슈(Work Item) 생성**

```
# 기본 태스크 생성
acli jira workitem create --summary "API 문서 업데이트" --project "TEAM" --type "Task"

# 상세 옵션 포함
acli jira workitem create \
  --summary "버그: 로그인 실패" \
  --project "PROJ" \
  --type "Bug" \
  --assignee "developer@company.com" \
  --label "bug,urgent"
```

**대량 이슈 수정**

```
# 여러 이슈의 담당자 변경
acli jira workitem edit --key "TEAM-1,TEAM-2,TEAM-3" --assignee "newowner@company.com"

# JQL로 대상 선택 후 수정
acli jira workitem edit --jql "project = TEAM AND labels = 'legacy'" --summary "[Archived]"
```

**이슈 상태 전환**

```
# 단일 이슈 상태 변경
acli jira workitem transition --key "TEAM-42" --status "Done"

# JQL 조건에 맞는 모든 이슈 상태 변경
acli jira workitem transition --jql "project = TEAM AND sprint = 'Sprint 15'" --status "In Progress"
```

### 4. 고급 활용: 스크립트 자동화

ACLI의 진정한 힘은 스크립팅에 있다. 아래는 스프린트 종료 시 미완료 이슈를 다음 스프린트로 이동하는 예시다.

```
#!/bin/bash
# move_incomplete_issues.sh

CURRENT_SPRINT="Sprint 15"
NEXT_SPRINT="Sprint 16"
PROJECT="TEAM"

# 미완료 이슈를 다음 스프린트로 이동
acli jira workitem edit \
  --jql "project = $PROJECT AND sprint = '$CURRENT_SPRINT' AND status != Done" \
  --sprint "$NEXT_SPRINT"

echo "미완료 이슈가 $NEXT_SPRINT로 이동되었습니다."
```

## Rovo Dev CLI: AI 코딩 에이전트

2025년 11월, Atlassian은 ACLI의 확장 기능으로 **Rovo Dev CLI**를 출시했다. 이는 터미널에서 AI 에이전트와 대화하며 코드를 작성하고 Jira 이슈를 처리할 수 있게 해준다.

```
# Rovo Dev 인증 (별도 토큰 필요)
acli rovodev auth login --site "mysite.atlassian.net" --email "user@example.com" --token

# 대화형 모드 시작
acli rovodev run
```

Rovo Dev는 코드베이스 분석, 문서 생성, Jira 이슈 완료까지 터미널에서 처리할 수 있다. 현재 베타 단계이며 Rovo Dev 크레딧이 필요하다.

## 모범사례/패턴 비교

| 사용 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| OAuth 인증 (`--web`) | 가장 간편, 토큰 관리 불필요 | 브라우저 필요, CI/CD에서 사용 어려움 |
| API 토큰 인증 | 스크립트/CI/CD 친화적 | 토큰 유출 주의, 정기 갱신 필요 |
| JQL 기반 대량 작업 | 조건부 처리로 유연성 극대화 | JQL 문법 학습 필요 |
| JSON 출력 (`--json`) | 다른 도구와 파이프라인 연결 용이 | jq 같은 JSON 파서 활용 권장 |
| JSON 파일 입력 (`--from-json`) | 복잡한 이슈 구조 재사용 가능 | JSON 스키마 확인 필요 (`--generate-json`) |

## 마치며

- ACLI는 Jira Cloud에서 반복 작업을 자동화하는 공식 CLI 도구로, 모든 플랜에서 무료로 사용 가능하다
- Homebrew나 curl로 설치 후 OAuth 또는 API 토큰으로 인증하면 바로 사용할 수 있다
- JQL 쿼리와 결합하면 수백 개 이슈를 한 번에 처리하는 스크립트를 만들 수 있다

**실전 팁:** 오늘 당장 `brew install acli && acli jira auth login --web`으로 시작해 보자. 프로젝트 목록 조회(`acli jira project list`)부터 시도하면 금방 감이 온다.

## 참고자료

- Atlassian CLI 공식 문서 (<https://developer.atlassian.com/cloud/acli/guides/introduction/>)
- ACLI 설치 가이드 (<https://developer.atlassian.com/cloud/acli/guides/install-acli/>)
- ACLI 명령어 레퍼런스 (<https://developer.atlassian.com/cloud/acli/reference/commands/>)
- Atlassian CLI Homebrew Tap (<https://github.com/atlassian/homebrew-acli>)
- Rovo Dev CLI 소개 (<https://www.atlassian.com/blog/announcements/rovo-dev-command-line-interface>)
- ACLI for Jira 발표 블로그 (<https://www.atlassian.com/blog/jira/atlassian-command-line-interface>)
