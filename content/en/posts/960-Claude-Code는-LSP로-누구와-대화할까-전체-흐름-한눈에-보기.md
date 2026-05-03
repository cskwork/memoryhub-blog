---
title: "Who Does Claude Code Talk to via LSP? A Complete Overview"
date: 2026-01-03T22:00:38+09:00
slug: "960-Claude-Code는-LSP로-누구와-대화할까-전체-흐름-한눈에-보기"
original_url: "https://memoryhub.tistory.com/960"
tistory_id: 960
draft: false
categories: ["Dev Library"]
tags: ["Claude"]
---

```
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║    [User]                                                          ║
║       │                                                            ║
║       │ "Fix the calculateTotal function"                         ║
║       ▼                                                            ║
║  ┌─────────────┐                                                   ║
║  │ Claude Code │  ◄─── Claude AI (Anthropic server)               ║
║  │ (terminal)  │                                                   ║
║  └──────┬──────┘                                                   ║
║         │                                                          ║
║         │ LSP request: "Where is calculateTotal defined?"         ║
║         ▼                                                          ║
║  ┌─────────────┐                                                   ║
║  │  Language   │  ◄─── Running locally                             ║
║  │   Server    │       (pyright, gopls, etc.)                      ║
║  └──────┬──────┘                                                   ║
║         │                                                          ║
║         │ Code analysis                                            ║
║         ▼                                                          ║
║  ┌─────────────┐                                                   ║
║  │ Codebase    │  ◄─── Project files on my computer               ║
║  │   (files)   │                                                   ║
║  └─────────────┘                                                   ║
║                                                                    ║
╚════════════════════════════════════════════════════════════════════╝
```

When you tell Claude Code "fix this function," multiple components are talking behind the scenes. But where exactly does this conversation go? **The core idea is that Claude Code talks to a Language Server running on my computer.** It's not the Anthropic server—it's a local program.

**One-sentence summary:** For Claude Code to "understand" code, it needs to ask a local program called Language Server, and the way they talk is called LSP.

---

## Meet the Players

First, let's clarify who does what.

| Component | Where does it run? | What does it do? |
| --- | --- | --- |
| **Claude Code** | My computer (terminal) | Receives user commands, delivers AI responses |
| **Claude AI** | Anthropic server (cloud) | Understands natural language, generates code, writes answers |
| **Language Server** | My computer (background) | Analyzes code structure, identifies definition/reference locations |
| **Codebase** | My computer (files) | Actual project source code |

Here, **LSP is the communication protocol between Claude Code and Language Server**.

---

## The Actual Conversation Flow

When you type "Find the calculateTotal function and fix the bug," here's what happens.

**Step 1: User → Claude Code**

```
User: "Find the calculateTotal function and fix the bug"
```

**Step 2: Claude Code → Claude AI (Anthropic server)**

```
Claude Code sends user request to Anthropic server
Claude AI: "I need to find the calculateTotal function location first"
```

**Step 3: Claude Code → Language Server (LSP request)**

```
Claude Code: "Where is calculateTotal defined?" (textDocument/definition)
Language Server: "It's at line 42 in src/billing.py"
```

**Step 4: Claude Code → Language Server (additional LSP requests)**

```
Claude Code: "Where is this function called?" (textDocument/references)
Language Server: "Three places - main.py:15, api.py:88, test.py:23"

Claude Code: "Any type errors?" (textDocument/diagnostics)
Language Server: "billing.py:45 is trying to add str to int"
```

**Step 5: Claude AI synthesizes information and writes a fix**

```
Claude AI:
- Function location: src/billing.py line 42
- Call sites: 3 places
- Problem found: Type error
→ Generate fixed code
```

**Step 6: Results delivered to user**

```
Claude Code: "Found a bug here. I've fixed it like this."
```

---

## Key Points

**LSP communication happens entirely on my computer.**

```
┌─────────────────────────────────────────┐
│            My Computer                  │
│                                         │
│   Claude Code  ◄───LSP───►  pyright    │
│       │                        │        │
│       │                        │        │
│       ▼                        ▼        │
│   Terminal UI            Code Analysis  │
│                                         │
└─────────────────────────────────────────┘
         │
         │ (Internet)
         ▼
┌─────────────────────────────────────────┐
│         Anthropic Server                │
│                                         │
│           Claude AI                     │
│  (Natural language, answer generation)  │
│                                         │
└─────────────────────────────────────────┘
```

**What goes over the internet:** User questions, AI responses

**What stays on my computer:** Code analysis (LSP communication)

---

## Language Server by Language

The Language Server that Claude Code talks to differs by programming language.

| Language | Language Server | Installation |
| --- | --- | --- |
| Python | pyright | `npm install -g pyright` |
| TypeScript/JS | vtsls | `npm install -g @vtsls/language-server` |
| Go | gopls | `go install golang.org/x/tools/gopls@latest` |
| Rust | rust-analyzer | `rustup component add rust-analyzer` |

Open a Python project, and Claude Code talks to pyright. Open a Go project, it talks to gopls.

---

## What if there's no LSP?

Without an LSP connection, Claude Code works "blind."

| Situation | With LSP | Without LSP |
| --- | --- | --- |
| Find function | Asks Language Server → instant, accurate location | grep text search → slow, inaccurate |
| Check types | Language Server tells | Read code and guess |
| Detect errors | Real-time diagnostics | Must run to find out |

---

## Big Picture Summary

```
User question
    │
    ▼
Claude Code (my computer)
    │
    ├──► Claude AI (cloud) : understands natural language, generates answers
    │
    └──► Language Server (my computer, LSP) : analyzes code structure
              │
              ▼
         Codebase (my files)
```

**Three-line summary:**

- Claude Code talks to two places: Claude AI (cloud) and Language Server (local)
- LSP is the communication protocol between Claude Code and Language Server
- Language Server lets Claude Code understand code as "structure," not just "text"

---

## Conclusion

- Claude Code's secret to fast, accurate code understanding is LSP communication with Language Server
- This communication happens entirely on my computer—code doesn't leak outside
- Each language has its own Language Server, and Claude Code automatically talks to the right one for your project

Practical tip: Use `/lsp status` command in Claude Code to check the current Language Server connection status.

---

## References

- Claude Code LSP Official Documentation (<https://docs.anthropic.com/en/docs/claude-code>)
- Language Server Protocol Official Site (<https://microsoft.github.io/language-server-protocol/>)
- claude-code-lsps GitHub (<https://github.com/Piebald-AI/claude-code-lsps>)

---

## Spring Boot + Vue Developer LSP Setup for Claude Code

### Your Stack Requires These Language Servers

| Technology | Language Server | Purpose |
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

| Feature | Java/Spring | Vue/TS |
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

| Step | Command |
| --- | --- |
| 1. Install jdtls | brew install jdtls |
| 2. Install Vue/TS servers | npm install -g @vtsls/language-server typescript @vue/language-server |
| 3. Enable LSP | export ENABLE_LSP_TOOL=1 |
| 4. Add plugins | /plugin install jdtls@claude-plugins-official etc. |
| 5. Verify | /plugin list |

This setup gives Claude Code full semantic understanding of both your Spring Boot backend and Vue frontend.
