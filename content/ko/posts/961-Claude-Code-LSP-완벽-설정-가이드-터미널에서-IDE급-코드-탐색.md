---
title: "? Claude Code LSP 완벽 설정 가이드: 터미널에서 IDE급 코드 탐색"
date: 2026-01-08T23:36:30+09:00
slug: "961-Claude-Code-LSP-완벽-설정-가이드-터미널에서-IDE급-코드-탐색"
original_url: "https://memoryhub.tistory.com/961"
tistory_id: 961
draft: false
categories: ["데브 라이브러리"]
tags: ["Claude"]
---

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║      ┌─────────────────────────────────────────────────┐      ║
║      │  Claude Code  ←──────────→  LSP Server          │      ║
║      │      │                         │                │      ║
║      │      ▼                         ▼                │      ║
║      │  [goToDefinition]   [Pyright/gopls/rust-analyzer]│     ║
║      │  [findReferences]   [Type Check, Diagnostics]   │      ║
║      │  [documentSymbol]   [Semantic Navigation]       │      ║
║      └─────────────────────────────────────────────────┘      ║
║                                                               ║
║        45 seconds  ────────→   50 ms   (900x faster)          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

VS Code에서 함수 위에 마우스를 올리면 타입 정보가 뜨고, "정의로 이동"을 누르면 정확한 파일과 라인으로 점프한다. 이 기능의 정체를 아는가? 바로 Language Server Protocol, 줄여서 LSP다. 이제 이 IDE의 핵심 기능이 터미널 기반 AI 코딩 도구인 Claude Code에도 탑재됐다. **코드 탐색 시간이 45초에서 50ms로, 무려 900배 빨라진다.**

**한줄요약:** 결론부터 말하면, Claude Code LSP를 활성화하면 AI가 텍스트 검색 대신 시맨틱 코드 분석으로 함수 정의, 참조, 타입 오류를 즉시 파악한다.

## 배경

2025년 12월, Anthropic은 Claude Code 버전 2.0.74에서 LSP 지원을 공식 추가했다. 이전까지 AI 코딩 도구들은 코드를 이해하는 것처럼 보였지만, 실제로는 텍스트 패턴 매칭에 의존했다. "processRequest 함수가 어디 정의되어 있지?"라고 물으면 AI는 grep처럼 파일을 뒤져야 했다.

> LSP(Language Server Protocol)는 에디터와 언어 서버 간의 표준 통신 규약으로, 코드의 시맨틱 구조를 이해하고 정의 이동, 참조 찾기, 실시간 진단 기능을 제공한다.

문제는 이 방식의 한계다. 텍스트 검색은 같은 이름의 변수가 주석에 있든, 문자열 안에 있든 구분하지 못한다. 대규모 코드베이스에서는 45초씩 걸리기도 한다. LSP는 이 문제를 근본적으로 해결한다. 코드를 텍스트가 아닌 구조로 이해하기 때문이다.

Microsoft가 2016년 만든 LSP의 핵심 혁신은 **언어 지능을 에디터에서 분리**한 것이다. 과거에는 VS Code용 Python 지원, IntelliJ용 Python 지원을 따로 만들어야 했다. LSP 이후로는 Pyright 하나면 어떤 에디터에서든 동일한 Python 지능을 사용할 수 있다. 이제 Claude Code도 그 목록에 들어갔다.

## Claude Code LSP가 제공하는 5가지 기능

Claude Code의 LSP 도구는 다섯 가지 핵심 작업을 지원한다.

| 기능 | 설명 | 실제 동작 |
| --- | --- | --- |
| goToDefinition | 심볼 정의 위치 탐색 | "handleRequest 함수 정의 위치" → src/handlers/request.ts:127:1 |
| findReferences | 심볼 사용 위치 전체 검색 | "CONFIG\_PATH 사용처" → 5개 파일, 12개 위치 즉시 반환 |
| documentSymbol | 파일 내 구조 분석 | 클래스, 함수, 상수 목록을 계층 구조로 표시 |
| hover | 심볼 타입 정보 조회 | 함수 시그니처, 파라미터 타입, 반환 값 표시 |
| getDiagnostics | 실시간 오류 진단 | 타입 오류, 문법 오류를 코드 수정 즉시 감지 |

이 기능들이 중요한 이유는 AI의 코드 이해 방식이 근본적으로 달라지기 때문이다. "이 함수를 리팩토링해줘"라고 요청하면, LSP가 없을 때는 AI가 파일을 하나씩 열어 텍스트로 분석한다. LSP가 있으면 호출 관계, 의존성, 타입 정보를 즉시 파악하고 정확한 수정 범위를 제안한다.

## 실습

### 1. LSP 도구 활성화

Claude Code의 LSP 기능은 기본적으로 비활성화되어 있다. 환경변수로 명시적 활성화가 필요하다.

```
# 일회성 활성화
ENABLE_LSP_TOOL=1 claude

# 영구 활성화 (~/.zshrc 또는 ~/.bashrc에 추가)
export ENABLE_LSP_TOOL=1
```

환경변수를 셸 설정 파일에 추가하면 Claude Code 실행 시마다 자동으로 LSP가 활성화된다.

### 2. 플러그인 마켓플레이스 등록

Claude Code는 플러그인 시스템으로 LSP 서버를 관리한다. 커뮤니티 마켓플레이스를 등록하면 다양한 언어 플러그인을 설치할 수 있다.

**최우선 설치!!!!**

```
# Claude Code 내에서 실행
/plugin marketplace add boostvolt/claude-code-lsps
```

이 명령은 한 번만 실행하면 된다. 마켓플레이스 정보는 세션 간에 유지된다.

### 3. 언어별 플러그인 설치

주로 사용하는 언어의 플러그인을 설치한다.

```
# Python 개발자
/plugin install pyright@claude-code-lsps

# TypeScript/JavaScript 개발자
/plugin install vtsls@claude-code-lsps

# Go 개발자
/plugin install gopls@claude-code-lsps

# Rust 개발자
/plugin install rust-analyzer@claude-code-lsps
```

플러그인 설치 시 LSP 서버 바이너리 자동 설치를 시도한다. 자동 설치 실패 시 `/plugin` 메뉴의 Errors 탭에서 수동 설치 안내를 확인할 수 있다.

### 4. 언어 서버 바이너리 수동 설치 (자동 설치 실패 시)

자동 설치가 실패하는 경우, 언어 서버를 직접 설치해야 한다.

```
# Python (Pyright)
pip install pyright
# 또는
npm install -g pyright

# TypeScript (vtsls)
npm install -g @vtsls/language-server typescript

# Go (gopls)
go install golang.org/x/tools/gopls@latest
# ~/go/bin이 PATH에 있어야 함

# Rust (rust-analyzer)
rustup component add rust-analyzer
# 또는
brew install rust-analyzer
```

설치 후 해당 바이너리가 PATH에 있는지 확인한다. `which pyright`, `which gopls` 명령으로 경로가 출력되면 정상이다.

### 5. 동작 확인

설치가 완료되면 실제 프로젝트에서 테스트한다.

```
# Claude Code에서 Python 프로젝트를 열고 질문
> main 함수의 정의 위치를 찾아줘

# LSP 정상 동작 시 응답 예시:
"main 함수는 src/app/main.py 파일의 42번 라인에 정의되어 있습니다."

# LSP 미동작 시 응답 예시:
"main이라는 이름이 포함된 파일들을 검색하고 있습니다..."
```

응답에 정확한 파일명과 라인 번호가 포함되면 LSP가 정상 작동하는 것이다. 파일 검색 언급이 나오면 플러그인 상태를 재확인해야 한다.

## 지원 언어 및 LSP 서버 비교

| 언어 | 플러그인 명령 | LSP 서버 | 수동 설치 |
| --- | --- | --- | --- |
| Python | `pyright@claude-code-lsps` | Pyright | `pip install pyright` |
| TypeScript/JS | `vtsls@claude-code-lsps` | vtsls | `npm install -g @vtsls/language-server` |
| Go | `gopls@claude-code-lsps` | gopls | `go install golang.org/x/tools/gopls@latest` |
| Rust | `rust-analyzer@claude-code-lsps` | rust-analyzer | `rustup component add rust-analyzer` |
| Java | `jdtls@claude-code-lsps` | Eclipse JDT | `brew install jdtls` (Java 21+ 필요) |
| C/C++ | `clangd@claude-code-lsps` | clangd | `brew install llvm` |
| C# | `omnisharp@claude-code-lsps` | OmniSharp | `brew install omnisharp-mono` |
| PHP | `intelephense@claude-code-lsps` | Intelephense | `npm install -g intelephense` |
| Kotlin | `kotlin-language-server@claude-code-lsps` | kotlin-lsp | `brew install kotlin-lsp` |
| Ruby | `solargraph@claude-code-lsps` | Solargraph | `gem install solargraph` |
| Dart | `dart-analyzer@claude-code-lsps` | Dart Analyzer | Dart SDK 포함 |

## Claude Code settings.json으로 ENABLE\_LSP\_TOOL 설정하는 방법

~/.claude/settings.json 파일에 env 섹션을 추가하면 됩니다:

```
{
  "env": {
    "ENABLE_LSP_TOOL": "1"
  }
}
```

### 설정 파일 위치별 적용 범위

위치 적용 범위 용도

|  |  |  |
| --- | --- | --- |
| ~/.claude/settings.json | 모든 프로젝트 (전역) | 개인 기본 설정 |
| .claude/settings.json | 해당 프로젝트만 | 팀 공유 (버전 관리) |
| .claude/settings.local.json | 해당 프로젝트만 | 개인 오버라이드 (gitignore) |

### 전체 설정 예시

플러그인 활성화와 함께 LSP를 설정하려면:

```
{
  "env": {
    "ENABLE_LSP_TOOL": "1"
  },
  "enabledPlugins": {
    "pyright@claude-code-lsps": true,
    "vtsls@claude-code-lsps": true
  }
}
```

### 프로젝트별 팀 설정

팀원 전체가 LSP를 사용하게 하려면 프로젝트 루트의 .claude/settings.json에 추가:

```
{
  "env": {
    "ENABLE_LSP_TOOL": "1"
  },
  "extraKnownMarketplaces": [
    "boostvolt/claude-code-lsps"
  ]
}
```

이렇게 하면 팀원이 저장소를 trust할 때 자동으로 LSP가 활성화되고 플러그인 설치 안내를 받습니다.

## 자주 발생하는 문제와 해결법

| 문제 | 원인 | 해결 방법 |
| --- | --- | --- |
| "No LSP server available for file type" | 플러그인 미설치 또는 미인식 | `/plugin` 탭에서 설치 확인, Claude Code 재시작 |
| "Executable not found in $PATH" | 언어 서버 바이너리 경로 문제 | `which [서버명]` 확인 후 PATH에 추가 |
| 플러그인 설치 후 동작 안 함 | 세션 초기화 문제 | Claude Code 종료 후 재실행 |
| Windows에서 LSP 미작동 | 플랫폼 호환성 이슈 | GitHub Issue #15914 참고, WSL 사용 권장 |

## 마치며

- Claude Code LSP는 AI 코딩 도구가 코드를 텍스트가 아닌 구조로 이해하게 만드는 전환점이다
- 5분 이내 설정으로 11개 이상 언어에서 IDE급 코드 탐색을 터미널에서 사용할 수 있다
- 실전 팁: 오늘 당장 `export ENABLE_LSP_TOOL=1`을 셸 설정에 추가하고, 자주 쓰는 언어의 플러그인 하나만 설치해보자

## 참고자료

- Claude Code 공식 플러그인 문서 (<https://code.claude.com/docs/en/discover-plugins>)
- boostvolt/claude-code-lsps GitHub (<https://github.com/boostvolt/claude-code-lsps>)
- Claude Code LSP 관련 이슈 #14803 (<https://github.com/anthropics/claude-code/issues/14803>)
- LSP 이슈 수정 진행 상황 #13952 (<https://github.com/anthropics/claude-code/issues/13952>)
