---
title: "? Claude Code는 LSP로 누구와 대화할까? 전체 흐름 한눈에 보기"
date: 2026-01-03T22:00:38+09:00
slug: "960-Claude-Code는-LSP로-누구와-대화할까-전체-흐름-한눈에-보기"
original_url: "https://memoryhub.tistory.com/960"
tistory_id: 960
draft: false
categories: ["데브 라이브러리"]
tags: ["Claude"]
---

```
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║    [사용자]                                                         ║
║       │                                                            ║
║       │ "calculateTotal 함수 수정해줘"                              ║
║       ▼                                                            ║
║  ┌─────────────┐                                                   ║
║  │ Claude Code │  ◄─── Claude AI (Anthropic 서버)                  ║
║  │   (터미널)   │                                                   ║
║  └──────┬──────┘                                                   ║
║         │                                                          ║
║         │ LSP 요청: "calculateTotal 정의 어디야?"                   ║
║         ▼                                                          ║
║  ┌─────────────┐                                                   ║
║  │  Language   │  ◄─── 로컬에서 실행 중                             ║
║  │   Server    │       (pyright, gopls 등)                         ║
║  └──────┬──────┘                                                   ║
║         │                                                          ║
║         │ 코드 분석                                                 ║
║         ▼                                                          ║
║  ┌─────────────┐                                                   ║
║  │  코드베이스  │  ◄─── 내 컴퓨터의 프로젝트 파일들                   ║
║  │   (파일들)   │                                                   ║
║  └─────────────┘                                                   ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
```

Claude Code에 "이 함수 고쳐줘"라고 말하면, 뒤에서 여러 구성요소가 대화를 주고받습니다. 그런데 이게 어디서 어디로 가는 건지 헷갈리죠. **핵심만 말하면, Claude Code는 내 컴퓨터에서 돌아가는 Language Server와 대화합니다.** Anthropic 서버가 아니라 로컬 프로그램이에요.

**한줄요약:** Claude Code가 코드를 "이해"하려면 Language Server라는 로컬 프로그램에게 물어봐야 하고, 이 대화 방식이 LSP다.

---

## 등장인물 소개

먼저 누가 누군지 정리합니다.

| 구성요소 | 어디서 실행? | 하는 일 |
| --- | --- | --- |
| **Claude Code** | 내 컴퓨터 (터미널) | 사용자 명령 받고, AI 응답 전달 |
| **Claude AI** | Anthropic 서버 (클라우드) | 자연어 이해, 코드 생성, 답변 작성 |
| **Language Server** | 내 컴퓨터 (백그라운드) | 코드 구조 분석, 정의/참조 위치 파악 |
| **코드베이스** | 내 컴퓨터 (파일) | 실제 프로젝트 소스 코드 |

여기서 **LSP는 Claude Code와 Language Server 사이의 대화 규칙**입니다.

---

## 실제 대화 흐름

"calculateTotal 함수 찾아서 버그 고쳐줘"라고 입력하면 이런 일이 벌어집니다.

**1단계: 사용자 → Claude Code**

```
사용자: "calculateTotal 함수 찾아서 버그 고쳐줘"
```

**2단계: Claude Code → Claude AI (Anthropic 서버)**

```
Claude Code가 사용자 요청을 Anthropic 서버로 전송
Claude AI: "calculateTotal 함수 위치를 먼저 파악해야겠군"
```

**3단계: Claude Code → Language Server (LSP 요청)**

```
Claude Code: "calculateTotal 정의가 어디야?" (textDocument/definition)
Language Server: "src/billing.py 42번째 줄이야"
```

**4단계: Claude Code → Language Server (추가 LSP 요청)**

```
Claude Code: "이 함수 어디서 호출돼?" (textDocument/references)
Language Server: "3군데 - main.py:15, api.py:88, test.py:23"

Claude Code: "타입 에러 있어?" (textDocument/diagnostics)
Language Server: "billing.py:45에서 str을 int로 더하려고 함"
```

**5단계: Claude AI가 정보 종합해서 수정안 작성**

```
Claude AI: 
- 함수 위치: src/billing.py 42번째 줄
- 사용처: 3군데
- 발견된 문제: 타입 에러
→ 수정 코드 생성
```

**6단계: 사용자에게 결과 전달**

```
Claude Code: "여기 버그가 있었네요. 이렇게 고쳤습니다."
```

---

## 핵심 포인트

**LSP 통신은 내 컴퓨터 안에서 일어납니다.**

```
┌─────────────────────────────────────────┐
│            내 컴퓨터                     │
│                                         │
│   Claude Code  ◄───LSP───►  pyright    │
│       │                        │        │
│       │                        │        │
│       ▼                        ▼        │
│   터미널 UI              코드 분석       │
│                                         │
└─────────────────────────────────────────┘
         │
         │ (인터넷)
         ▼
┌─────────────────────────────────────────┐
│         Anthropic 서버                   │
│                                         │
│           Claude AI                     │
│      (자연어 이해, 답변 생성)             │
│                                         │
└─────────────────────────────────────────┘
```

**인터넷으로 나가는 것:** 사용자 질문, AI 응답

**내 컴퓨터 안에서 끝나는 것:** 코드 분석 (LSP 통신)

---

## 언어별 Language Server

Claude Code가 대화하는 Language Server는 언어마다 다릅니다.

| 언어 | Language Server | 설치 방법 |
| --- | --- | --- |
| Python | pyright | `npm install -g pyright` |
| TypeScript/JS | vtsls | `npm install -g @vtsls/language-server` |
| Go | gopls | `go install golang.org/x/tools/gopls@latest` |
| Rust | rust-analyzer | `rustup component add rust-analyzer` |

Python 프로젝트를 열면 Claude Code는 pyright와 대화하고, Go 프로젝트면 gopls와 대화합니다.

---

## LSP가 없으면 어떻게 되나?

LSP 연결이 안 되어 있으면 Claude Code는 "눈 감고" 일합니다.

| 상황 | LSP 있을 때 | LSP 없을 때 |
| --- | --- | --- |
| 함수 찾기 | Language Server에게 물어봄 → 즉시 정확한 위치 | grep 텍스트 검색 → 느리고 부정확 |
| 타입 확인 | Language Server가 알려줌 | 코드 읽고 추측 |
| 에러 파악 | 실시간 진단 정보 | 실행해봐야 앎 |

---

## 전체 그림 요약

```
사용자 질문
    │
    ▼
Claude Code (내 컴퓨터)
    │
    ├──► Claude AI (클라우드) : 자연어 이해, 답변 생성
    │
    └──► Language Server (내 컴퓨터, LSP) : 코드 구조 분석
              │
              ▼
         코드베이스 (내 파일들)
```

**세 줄 요약:**

- Claude Code는 두 곳과 대화한다: Claude AI(클라우드)와 Language Server(로컬)
- LSP는 Claude Code와 Language Server 사이의 통신 규격
- Language Server 덕분에 Claude Code가 코드를 "텍스트"가 아닌 "구조"로 이해한다

---

## 마치며

- Claude Code가 코드를 빠르고 정확하게 파악하는 비결은 Language Server와의 LSP 통신이다
- 이 통신은 내 컴퓨터 안에서 일어나며, 코드가 외부로 나가지 않는다
- 언어별로 다른 Language Server가 있고, Claude Code는 프로젝트에 맞는 서버와 자동으로 대화한다

실전 팁: Claude Code에서 `/lsp status` 명령으로 현재 연결된 Language Server 상태를 확인해보세요.

---

## 참고자료

- Claude Code LSP 공식 문서 (<https://docs.anthropic.com/en/docs/claude-code>)
- Language Server Protocol 공식 사이트 (<https://microsoft.github.io/language-server-protocol/>)
- claude-code-lsps GitHub (<https://github.com/Piebald-AI/claude-code-lsps>)

---

## Spring Boot + Vue Developer LSP Setup for Claude Code

### Your Stack Requires These Language Servers

Technology Language Server Purpose

|  |  |  |
| --- | --- | --- |
| **Java (Spring Boot)** | jdtls | Java code intelligence |
| **Vue 3** | @vue/language-server | .vue file support |
| **TypeScript/JS** | vtsls | .ts/.js files + Vue script blocks |
| **HTML/CSS** | vscode-html-css | Template styling |

---

### Step 1: Prerequisites

```
# Check versions
java --version    # Must be 21+
node --version    # Must be 18+
```

---

### Step 2: Install Language Servers

**Java (jdtls for Spring Boot):**

```
# macOS
brew install jdtls

# Or manual install
curl -LO http://download.eclipse.org/jdtls/snapshots/jdt-language-server-latest.tar.gz
mkdir -p ~/jdtls
tar -xzf jdt-language-server-latest.tar.gz -C ~/jdtls

# Set JAVA_HOME (add to .zshrc or .bashrc)
export JAVA_HOME=$(/usr/libexec/java_home)
```

**Vue + TypeScript (vtsls + vue-language-server):**

```
# Install both together
npm install -g @vtsls/language-server typescript @vue/language-server
```

**HTML/CSS:**

```
npm install -g vscode-langservers-extracted
```

---

### Step 3: Enable LSP in Claude Code

```
# Add to your shell profile (.zshrc or .bashrc)
export ENABLE_LSP_TOOL=1
```

Restart your terminal.

---

### Step 4: Add Claude Code Marketplace & Plugins

```
# Open Claude Code
claude

# Add the LSP marketplace
/marketplace add https://github.com/anthropics/claude-plugins-official

# Install plugins for your stack
/plugin install jdtls@claude-plugins-official
/plugin install vtsls@claude-plugins-official
/plugin install vscode-html-css@claude-plugins-official
```

---

### Step 5: Verify Setup

```
# Check if LSP servers are in PATH
which jdtls
which vtsls
which vue-language-server

# In Claude Code, check plugin status
/plugin list
```

---

### Project Structure Recommendation

```
my-fullstack-project/
├── backend/                 # Spring Boot
│   ├── src/main/java/
│   ├── pom.xml             # or build.gradle
│   └── ...
├── frontend/               # Vue 3
│   ├── src/
│   │   ├── components/     # .vue files
│   │   ├── views/
│   │   └── main.ts
│   ├── package.json
│   └── tsconfig.json
└── ...
```

**Tip:** Run Claude Code from the project root so it can detect both backend and frontend.

---

### What You Get

Feature Java/Spring Vue/TS

|  |  |  |
| --- | --- | --- |
| Go to Definition | Controller -> Service -> Repository | Component -> Composable |
| Find References | Where is this Bean used? | Where is this component imported? |
| Diagnostics | Compile errors, type mismatches | TypeScript errors, Vue template issues |
| Hover Info | Method signatures, Javadoc | Props types, function signatures |

---

### Troubleshooting

**jdtls not starting:**

```
# Check Java version
java --version  # Must be 21+

# Check if jdtls is executable
ls -la $(which jdtls)
```

**Vue files not recognized:**

```
# Ensure @vue/language-server is installed
npm list -g @vue/language-server

# vtsls needs typescript as peer dependency
npm list -g typescript
```

**Memory issues with large Spring Boot projects:**

```
# Increase Java heap for jdtls (add to shell profile)
export JDTLS_JVM_ARGS="-Xmx4g"
```

---

### Quick Test Commands

Once set up, try these in Claude Code:

```
# For Spring Boot
"Find all usages of @Transactional in the project"
"Go to the definition of UserService"
"Show me all REST endpoints"

# For Vue
"Find where HomeView component is imported"
"Show the type definition of this composable"
"What props does this component accept?"
```

---

### Summary

Step Command

|  |  |
| --- | --- |
| 1. Install jdtls | brew install jdtls |
| 2. Install Vue/TS servers | npm install -g @vtsls/language-server typescript @vue/language-server |
| 3. Enable LSP | export ENABLE\_LSP\_TOOL=1 |
| 4. Add plugins | /plugin install jdtls@claude-plugins-official etc. |
| 5. Verify | /plugin list |

This setup gives Claude Code full semantic understanding of both your Spring Boot backend and Vue frontend.
