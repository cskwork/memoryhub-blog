---
title: "? Gemini CLI 보안 설정 완벽 가이드: 위험 명령어 차단부터 MCP 서버 구성"
date: 2025-12-18T21:41:16+09:00
slug: "934-Gemini-CLI-보안-설정-완벽-가이드-위험-명령어-차단부터-MCP-서버-구성"
original_url: "https://memoryhub.tistory.com/934"
tistory_id: 934
draft: false
---

```
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║     ┌─────────────────────────────────────────────────┐      ║
    ║     │  GEMINI CLI                                     │      ║
    ║     │  ═══════════                                    │      ║
    ║     │                                                 │      ║
    ║     │    ┌───────┐   ┌───────┐   ┌───────┐           │      ║
    ║     │    │SANDBOX│   │  MCP  │   │SECURITY│          │      ║
    ║     │    │Docker │◄──│Server │──►│ Policy │          │      ║
    ║     │    │Podman │   │Config │   │coreTools│         │      ║
    ║     │    └───────┘   └───────┘   └───────┘           │      ║
    ║     │         │           │           │              │      ║
    ║     │         └───────────┼───────────┘              │      ║
    ║     │                     ▼                          │      ║
    ║     │              [settings.json]                   │      ║
    ║     │                                                │      ║
    ║     └─────────────────────────────────────────────────┘      ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
```

AI 코딩 도구가 터미널에서 `rm -rf /`를 실행하면 어떻게 될까요? 2025년 6월 출시 직후 발견된 Gemini CLI 취약점은 악성 코드가 사용자 모르게 시스템 명령을 실행할 수 있음을 보여줬습니다. 다행히 Google은 빠르게 패치했지만, 이 사건은 **AI 에이전트 도구의 보안 설정이 선택이 아닌 필수**라는 교훈을 남겼습니다. 이 글에서는 Gemini CLI의 다중 보안 계층을 활용해 안전하면서도 강력한 AI 개발 환경을 구축하는 방법을 다룹니다.

**한줄요약:** 결론부터 말하면, Gemini CLI는 coreTools/excludeTools로 명령어를 제한하고, Docker/Podman 샌드박스로 실행 환경을 격리하며, 프로젝트별 MCP 서버 설정으로 외부 도구를 안전하게 연동할 수 있다.

---

## 배경

Gemini CLI는 Google이 2025년 6월 25일 출시한 오픈소스 AI 에이전트로, 터미널에서 직접 Gemini 모델과 상호작용하며 코드 작성, 버그 수정, 파일 조작 등을 수행한다. 문제는 이런 강력한 기능이 보안 위협으로 이어질 수 있다는 점이다.

> Gemini CLI 보안 모델: AI 에이전트가 시스템 명령을 실행할 때 발생할 수 있는 위험을 다중 계층(샌드박싱, 도구 제한, 승인 모드)으로 방어하는 체계

출시 이틀 만에 보안 연구팀 Tracebit이 발견한 취약점은 충격적이었다. 악의적인 README.md 파일에 숨겨진 프롬프트 인젝션이 화이트리스트 우회와 결합되어, 사용자가 코드를 분석하는 동안 환경 변수가 외부 서버로 유출될 수 있었다.

Google은 이를 P1/S1(최고 심각도)로 분류하고 v0.1.14에서 패치했다.

핵심은 **기본 설정이 "no sandbox" 모드**라는 것이다. 화면 하단에 빨간 경고 문구가 표시되지만, 많은 개발자가 이를 무시한 채 사용한다. 안전한 Gemini CLI 사용을 위해서는 보안 설정을 직접 구성해야 한다.

---

## 설정 파일 구조 이해하기

Gemini CLI 설정은 4단계 우선순위로 적용된다. 숫자가 클수록 우선순위가 높다.

| 우선순위 | 설정 파일 위치 | 적용 범위 |
| --- | --- | --- |
| 1 | `/etc/gemini-cli/system-defaults.json` (Linux) | 시스템 기본값 |
| 2 | `~/.gemini/settings.json` | 사용자 전역 |
| 3 | `프로젝트/.gemini/settings.json` | 프로젝트 한정 |
| 4 | `/etc/gemini-cli/settings.json` | 시스템 강제 적용 |

단일 값 설정(theme 등)은 높은 우선순위가 덮어쓰고, 배열이나 객체(mcpServers, includeDirectories)는 병합된다. 이 구조를 이해해야 프로젝트별 MCP 서버 설정이 왜 가능한지 알 수 있다.

---

## 위험 명령어 차단: coreTools와 excludeTools

### 화이트리스트 방식(coreTools) - 권장

가장 안전한 방법은 허용할 도구만 명시적으로 지정하는 것이다. 지정되지 않은 도구는 모델이 사용할 수 없다.

```
{
  "tools": {
    "core": [
      "ReadFileTool",
      "GlobTool",
      "ShellTool(ls)",
      "ShellTool(cat)",
      "ShellTool(grep)",
      "ShellTool(git status)"
    ]
  }
}
```

위 설정은 파일 읽기, 목록 조회, 검색, Git 상태 확인만 허용한다. `rm`, `curl`, `wget` 같은 위험한 명령은 원천 차단된다.

### 블랙리스트 방식(excludeTools)

특정 명령만 차단하고 나머지는 허용하는 방식이다. 화이트리스트보다 보안성이 낮지만 유연하다.

```
{
  "tools": {
    "exclude": [
      "ShellTool(rm -rf)",
      "ShellTool(rm -r)",
      "ShellTool(curl)",
      "ShellTool(wget)",
      "run_shell_command"
    ]
  }
}
```

**주의할 점:** excludeTools는 문자열 기반 차단이라 우회 가능성이 있다. 예를 들어 `rm -rf`를 차단해도 `rm -r -f`나 스크립트 내 `eval`을 통한 실행은 막지 못할 수 있다. 가능하면 coreTools 화이트리스트 방식을 사용하자.

### 두 설정을 함께 사용하면?

excludeTools가 coreTools보다 우선한다. 양쪽에 모두 있는 도구는 차단된다.

---

## 샌드박스 설정: 실행 환경 격리

샌드박스는 AI가 실행하는 명령을 격리된 환경에서 처리해 시스템 손상을 방지한다. Gemini CLI는 세 가지 샌드박스 방식을 지원한다.

### 1. macOS Seatbelt (macOS 전용)

macOS 내장 샌드박스 기능을 활용한다. 가볍고 빠르지만 macOS에서만 사용 가능하다.

```
# 환경 변수로 활성화
export GEMINI_SANDBOX=sandbox-exec

# 프로파일 선택 (기본값: permissive-open)
export SEATBELT_PROFILE=restrictive-closed
```

Seatbelt 프로파일 옵션:

| 프로파일 | 파일 쓰기 제한 | 네트워크 |
| --- | --- | --- |
| permissive-open | 프로젝트 외부 제한 | 허용 |
| permissive-closed | 프로젝트 외부 제한 | 차단 |
| permissive-proxied | 프로젝트 외부 제한 | 프록시만 |
| restrictive-open | 엄격 제한 | 허용 |
| restrictive-closed | 최대 제한 | 차단 |

### 2. Docker 기반 샌드박스

크로스 플랫폼에서 완전한 프로세스 격리를 제공한다. 가장 강력한 보안을 원한다면 이 방식을 선택하자.

```
{
  "tools": {
    "sandbox": "docker"
  }
}
```

프로젝트별 커스텀 샌드박스가 필요하면 `.gemini/sandbox.Dockerfile`을 생성한다.

```
FROM gemini-cli-sandbox

# 프로젝트에 필요한 의존성 추가
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pytest black

# 커스텀 설정 복사
COPY ./scripts /app/scripts
```

빌드 및 실행:

```
export BUILD_SANDBOX=true
gemini -s -p "run tests"
```

### 3. Podman 기반 샌드박스

Docker와 유사하지만 데몬리스로 동작한다. SELinux 환경에서는 추가 설정이 필요할 수 있다.

```
export GEMINI_SANDBOX=podman
export SANDBOX_FLAGS="--security-opt label=disable"
```

### YOLO 모드와 샌드박스 자동 활성화

`--yolo` 또는 `--approval-mode=yolo` 옵션 사용 시 샌드박스가 자동 활성화된다. 모든 도구 실행을 자동 승인하면서도 격리 환경에서 실행되어 위험을 줄인다.

```
gemini --yolo -p "refactor this code"
# 자동으로 샌드박스 내에서 실행
```

엔터프라이즈 환경에서는 YOLO 모드를 시스템 레벨에서 비활성화할 수 있다.

```
{
  "security": {
    "disableYoloMode": true
  }
}
```

---

## 프로젝트 레벨 MCP 서버 구성

MCP(Model Context Protocol)는 Gemini CLI가 외부 시스템과 상호작용할 수 있게 해주는 프로토콜이다. GitHub, 데이터베이스, API 등을 MCP 서버로 연결해 AI의 기능을 확장한다.

### MCP 서버 기본 설정

`~/.gemini/settings.json` 또는 프로젝트의 `.gemini/settings.json`에 설정한다.

```
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "$GITHUB_TOKEN"
      },
      "timeout": 5000
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "$DB_CONNECTION_STRING"
      }
    }
  }
}
```

### MCP 서버별 도구 제한

특정 MCP 서버의 일부 도구만 허용하거나 차단할 수 있다.

```
{
  "mcpServers": {
    "third-party-analyzer": {
      "command": "/usr/local/bin/start-analyzer.sh",
      "includeTools": ["code-search", "get-ticket-details"],
      "excludeTools": ["delete-ticket", "modify-data"]
    }
  }
}
```

위 설정은 분석기 서버에서 검색과 조회만 허용하고 삭제/수정 기능은 차단한다.

### 원격 MCP 서버 연결

HTTP/SSE 기반 원격 서버도 연결 가능하다. OAuth 인증을 지원한다.

```
{
  "mcpServers": {
    "remote-api": {
      "httpUrl": "https://mcp.example.com/api",
      "headers": {
        "Authorization": "Bearer ${API_TOKEN}",
        "Content-Type": "application/json"
      },
      "timeout": 10000,
      "authProviderType": "dynamic_discovery"
    }
  }
}
```

### MCP 서버 허용 목록 (엔터프라이즈)

시스템 관리자는 허용된 MCP 서버만 사용하도록 강제할 수 있다.

```
{
  "mcp": {
    "allowed": ["corp-data-api", "approved-github"]
  },
  "mcpServers": {
    "corp-data-api": {
      "command": "/opt/tools/corp-api.sh",
      "timeout": 5000
    },
    "approved-github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"]
    }
  }
}
```

`mcp.allowed` 목록에 없는 서버는 사용자가 추가해도 실행되지 않는다.

---

## 실습: 안전한 개발 환경 구성

### 1단계: 사용자 전역 설정 생성

기본 보안 설정을 `~/.gemini/settings.json`에 적용한다.

```
{
  "tools": {
    "sandbox": "docker",
    "core": [
      "ReadFileTool",
      "WriteFileTool", 
      "EditFileTool",
      "GlobTool",
      "ShellTool(ls)",
      "ShellTool(cat)",
      "ShellTool(grep)",
      "ShellTool(git)"
    ],
    "exclude": [
      "ShellTool(rm -rf)",
      "ShellTool(curl)",
      "ShellTool(wget)"
    ]
  },
  "security": {
    "disableYoloMode": false
  }
}
```

### 2단계: 프로젝트별 MCP 서버 추가

백엔드 프로젝트라면 `.gemini/settings.json`에 데이터베이스 MCP를 추가한다.

```
{
  "mcpServers": {
    "project-db": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "DATABASE_URL": "$DATABASE_URL"
      },
      "includeTools": ["query", "list-tables"],
      "excludeTools": ["execute", "drop-table"]
    }
  }
}
```

### 3단계: 환경 변수 설정

프로젝트 루트에 `.gemini/.env` 파일을 생성한다.

```
# 데이터베이스 연결
DATABASE_URL="postgresql://user:pass@localhost:5432/mydb"

# GitHub 토큰 (선택)
GITHUB_TOKEN="ghp_xxxxxxxxxxxx"

# 샌드박스 강제 활성화
GEMINI_SANDBOX=docker
```

### 4단계: 신뢰 폴더 기능 활성화

처음 접근하는 폴더에서 설정 로드를 제어한다.

```
{
  "security": {
    "trustedFolders": true
  }
}
```

이 설정이 활성화되면 새 폴더에서 Gemini CLI 실행 시 신뢰 여부를 묻는 대화상자가 나타난다. 신뢰하지 않는 폴더에서는 프로젝트 설정, MCP 서버, 자동 컨텍스트 로드가 비활성화된다.

---

## 모범사례/패턴 비교

| 보안 수준 | 설정 조합 | 적합한 상황 | 주의점 |
| --- | --- | --- | --- |
| 최소 | 기본값 (no sandbox) | 신뢰할 수 있는 개인 프로젝트 | 화면 하단 빨간 경고 무시 금지 |
| 중간 | excludeTools + Seatbelt | 일반 개발 환경 | 우회 가능성 존재 |
| 높음 | coreTools + Docker | 팀 협업, 외부 코드 분석 | Docker 설치 필요 |
| 엔터프라이즈 | 시스템 설정 + MCP 허용 목록 | 기업 환경 | 관리자 권한 필요 |

---

## 마치며

Gemini CLI의 보안은 **샌드박스로 실행 환경을 격리**하고, **coreTools로 허용 도구를 제한**하며, **MCP 서버별 세밀한 권한 관리**로 완성된다. 기본 설정이 "no sandbox"이므로 반드시 직접 보안 설정을 구성해야 한다. AI 에이전트가 강력해질수록 보안 설정의 중요성도 커진다.

실전 팁: 오늘 당장 `~/.gemini/settings.json`에 `"sandbox": "docker"`를 추가하고, 자주 사용하는 명령어만 coreTools에 등록해보세요.

---

## 참고자료

- Gemini CLI 공식 설정 문서 (<https://geminicli.com/docs/get-started/configuration/>)
- Gemini CLI 샌드박스 가이드 (<https://geminicli.com/docs/cli/sandbox/>)
- Gemini CLI 엔터프라이즈 설정 (<https://geminicli.com/docs/cli/enterprise/>)
- MCP 서버 구성 가이드 (<https://geminicli.com/docs/tools/mcp-server/>)
- Gemini CLI GitHub 저장소 (<https://github.com/google-gemini/gemini-cli>)
- Tracebit 보안 취약점 분석 (<https://tracebit.com/blog/code-exec-deception-gemini-ai-cli-hijack>)
