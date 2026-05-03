---
title: "? Clawdbot 보안 설정, 내 폴더만 접근하게 만드는 3가지 핵심 설정"
date: 2026-01-26T20:02:46+09:00
slug: "991-Clawdbot-보안-설정-내-폴더만-접근하게-만드는-3가지-핵심-설정"
original_url: "https://memoryhub.tistory.com/991"
tistory_id: 991
draft: false
---

```
    ┌─────────────────────────────────────────┐
    │     ?  CLAWDBOT SECURITY CONFIG  ?    │
    │                                         │
    │   ┌───────────────────────────────┐     │
    │   │  SANDBOX    │   TOOL POLICY   │     │
    │   │  ┌───────┐  │   ┌─────────┐   │     │
    │   │  │ ?    │  │   │ allow[] │   │     │
    │   │  │Docker │  │   │ deny[]  │   │     │
    │   │  └───────┘  │   └─────────┘   │     │
    │   └─────────────┴─────────────────┘     │
    │              ↓                          │
    │   ┌─────────────────────────────────┐   │
    │   │     BIND MOUNTS (Directory)     │   │
    │   │   /project:rw  /docs:ro         │   │
    │   └─────────────────────────────────┘   │
    └─────────────────────────────────────────┘
```

AI 에이전트에게 컴퓨터 전체 접근 권한을 주는 건 불안합니다. "파일 정리해줘"라고 했다가 시스템 파일을 건드리면 어떡하죠? Clawdbot은 강력한 보안 설정을 제공하지만, 공식 문서만 봐서는 어디서부터 손대야 할지 막막합니다.

**이 글을 읽고 나면 원하는 폴더만 정확히 열어주면서 웹 브라우징과 스킬은 그대로 사용하는 설정을 완성할 수 있습니다.**

**한줄요약:** Sandbox(실행 환경) + Tool Policy(도구 허용) + Bind Mount(디렉토리 접근)

3가지만 설정하면 AI 에이전트의 파일 접근을 완벽하게 통제할 수 있습니다.

## 배경

Clawdbot은 개인용 AI 에이전트 플랫폼입니다. WhatsApp, Telegram, Discord 등 다양한 채널을 통해 AI와 대화하고, 파일 읽기/쓰기, 코드 실행, 웹 브라우징까지 수행할 수 있습니다.

문제는 **기본 설정이 호스트 전체 접근**이라는 점입니다.

> Clawdbot의 보안은 3계층 구조로 작동합니다. Sandbox는 "어디서" 실행할지, Tool Policy는 "무엇을" 실행할지, Bind Mount는 "어느 폴더에" 접근할지를 각각 통제합니다.

많은 사용자가 "Docker로 실행하면 안전하겠지"라고 생각합니다.

하지만 Sandbox를 켜도 Bind Mount 설정이 잘못되면 호스트의 민감한 디렉토리가 그대로 노출됩니다.

반대로 Sandbox 없이 Tool Policy만 설정하면 허용된 도구가 호스트에서 직접 실행되어 예상치 못한 결과를 초래할 수 있습니다.

| 계층 | 역할 | 주요 설정 키 |
| --- | --- | --- |
| Sandbox | 도구 실행 환경 (Docker vs Host) | `agents.defaults.sandbox.*` |
| Tool Policy | 허용/차단할 도구 목록 | `tools.*`, `tools.sandbox.tools.*` |
| Bind Mount | 컨테이너에서 접근 가능한 디렉토리 | `sandbox.docker.binds` |

설정 파일 위치는 `~/.clawdbot/clawdbot.json`입니다.

## 핵심 설정 상세 분석

### Sandbox Mode: 실행 환경 격리

Sandbox mode는 도구가 **어디서** 실행되는지를 결정합니다.

```
{
  "agents": {
    "defaults": {
      "sandbox": {
        "mode": "all"
      }
    }
  }
}
```

**mode 옵션 비교:**

| 값 | 동작 | 적합한 상황 |
| --- | --- | --- |
| `"off"` | 모든 도구가 호스트에서 실행 | 신뢰할 수 있는 로컬 환경, 최대 성능 필요 시 |
| `"non-main"` | 그룹/채널 세션만 샌드박스 적용 | 개인 채팅은 자유롭게, 공유 채팅은 제한 |
| `"all"` | 모든 세션이 샌드박스에서 실행 | 보안이 최우선인 환경 |

**주의할 점:** `"non-main"` 모드에서 "main"의 기준은 `session.mainKey`입니다. 그룹 채팅이나 채널은 자동으로 non-main으로 분류되어 샌드박스가 적용됩니다.

### Workspace Access: 기본 작업 공간 권한

```
{
  "sandbox": {
    "workspaceAccess": "none"
  }
}
```

| 값 | 동작 | 보안 수준 |
| --- | --- | --- |
| `"none"` | 격리된 샌드박스 작업 공간 사용 | 가장 안전 |
| `"ro"` | 에이전트 워크스페이스를 `/agent`에 읽기 전용 마운트 | 중간 |
| `"rw"` | 에이전트 워크스페이스를 `/workspace`에 읽기/쓰기 마운트 | 주의 필요 |

`"none"`으로 설정하면 `~/.clawdbot/sandboxes` 아래에 격리된 작업 공간이 생성됩니다.

스킬 파일은 자동으로 이 공간에 미러링되므로 별도 설정이 필요 없습니다.

### Bind Mount: 특정 디렉토리만 열어주기

**이 설정이 핵심입니다.** Bind Mount를 통해 호스트의 특정 디렉토리만 컨테이너에 노출할 수 있습니다.

```
      "sandbox": {
        "mode": "all",
        "workspaceAccess": "none",
        "scope": "session",
        "docker": {
          "network": "bridge",
          "binds": [
            "/Users/danny/Documents/PARA/Resource/art-assets:rw",
            "/Users/danny/Documents/PARA/Resource/EduFlix:rw"
          ]
        }
      }
```

형식은 `호스트경로:컨테이너경로:모드`입니다.

| 모드 | 의미 |
| --- | --- |
| `:rw` | 읽기/쓰기 (기본값) |
| `:ro` | 읽기 전용 |

**binds에 명시되지 않은 디렉토리는 접근 불가능합니다.**

이것이 보안의 핵심입니다.

### Tool Policy: 도구 허용 목록 설정

샌드박스 내에서 사용할 수 있는 도구를 명시적으로 지정합니다.

```
{
  "tools": {
    "sandbox": {
      "tools": {
        "allow": [
          "group:runtime",
          "group:fs",
          "browser",
          "web"
        ],
        "deny": [
          "canvas",
          "nodes",
          "cron",
          "gateway"
        ]
      }
    }
  }
}
```

**사용 가능한 Tool Group:**

| 그룹명 | 포함 도구 |
| --- | --- |
| `group:runtime` | exec, bash, process |
| `group:fs` | read, write, edit, apply\_patch |
| `group:sessions` | sessions\_list, sessions\_history, sessions\_send, sessions\_spawn |
| `group:memory` | memory\_search, memory\_get |
| `group:ui` | browser, canvas |

`deny`가 항상 우선합니다. `allow`에 있어도 `deny`에 포함되면 차단됩니다.

### Network 설정: 웹 브라우징 활성화

기본 네트워크 설정은 `"none"`(네트워크 없음)입니다. 웹 브라우징을 사용하려면 반드시 변경해야 합니다.

```
{
  "sandbox": {
    "docker": {
      "network": "bridge"
    }
  }
}
```

## 실습

### 1. 설정 파일 생성

터미널에서 설정 파일을 생성합니다.

```
mkdir -p ~/.clawdbot
nano ~/.clawdbot/clawdbot.json
```

### 2. 보안 설정 입력

아래 설정을 복사하여 붙여넣습니다. `youruser`와 경로는 실제 환경에 맞게 수정하세요.

```
{
  "agent": {
    "model": "anthropic/claude-sonnet-4-5"
  },
  "agents": {
    "defaults": {
      "workspace": "~/clawd",
      "sandbox": {
        "mode": "all",
        "scope": "session",
        "workspaceAccess": "none",
        "docker": {
          "binds": [
            "/home/youruser/dev/project-a:/workspace/project-a:rw",
            "/home/youruser/dev/project-b:/workspace/project-b:rw",
            "/home/youruser/reference:/workspace/reference:ro"
          ],
          "network": "bridge"
        }
      }
    }
  },
  "tools": {
    "sandbox": {
      "tools": {
        "allow": [
          "group:runtime",
          "group:fs",
          "group:sessions",
          "group:memory",
          "browser",
          "web"
        ],
        "deny": [
          "canvas",
          "nodes",
          "cron",
          "gateway"
        ]
      }
    },
    "elevated": {
      "enabled": false
    }
  },
  "skills": {
    "load": {
      "watch": true,
      "watchDebounceMs": 250
    }
  }
}
```

### 3. 샌드박스 이미지 빌드

Clawdbot 샌드박스용 Docker 이미지를 빌드합니다.

```
# 기본 샌드박스 이미지
scripts/sandbox-setup.sh

# 브라우저 포함 이미지 (웹 브라우징 사용 시)
scripts/sandbox-browser-setup.sh
```

### 4. 설정 확인

설정이 올바르게 적용되었는지 확인합니다.

```
clawdbot sandbox explain
```

출력에서 다음을 확인하세요:

- `mode: all` - 모든 세션 샌드박스 적용
- `workspaceAccess: none` - 격리된 작업 공간
- `binds` 목록 - 의도한 디렉토리만 표시
- `allow/deny` 목록 - 도구 정책 확인

## 모범사례/패턴 비교

| 시나리오 | mode | workspaceAccess | binds | network |
| --- | --- | --- | --- | --- |
| 개발 프로젝트 작업 | `all` | `none` | 프로젝트 폴더만 `:rw` | `bridge` |
| 문서 검토/참고 | `all` | `none` | 문서 폴더만 `:ro` | `none` |
| 그룹 채팅 봇 | `non-main` | `none` | 최소한만 | `bridge` |
| 완전 격리 테스트 | `all` | `none` | 없음 | `none` |

**절대 하지 말아야 할 설정:**

| 설정 | 위험성 |
| --- | --- |
| `/var/run/docker.sock` 바인드 | 호스트 전체 제어권 탈취 가능 |
| 홈 디렉토리 전체 바인드 (`~:/home:rw`) | SSH 키, 설정 파일 등 민감 정보 노출 |
| `elevated.enabled: true` | 샌드박스 우회하여 호스트에서 직접 실행 |

## 마치며

- Clawdbot 보안은 Sandbox(환경), Tool Policy(도구), Bind Mount(디렉토리) 3계층으로 구성됩니다
- `binds`에 명시한 디렉토리만 접근 가능하므로, 필요한 폴더만 최소한으로 열어주세요
- `clawdbot sandbox explain` 명령으로 현재 적용된 보안 설정을 언제든 확인할 수 있습니다
- 실전 팁: 새 프로젝트를 시작할 때마다 해당 폴더만 binds에 추가하고, 완료 후 제거하는 습관을 들이세요

## 참고자료

- Sandbox vs Tool Policy vs Elevated (<https://docs.clawd.bot/gateway/sandbox-vs-tool-policy-vs-elevated>)
- Sandboxing (<https://docs.clawd.bot/gateway/sandboxing>)
- Skills Configuration (<https://docs.clawd.bot/tools/skills>)
