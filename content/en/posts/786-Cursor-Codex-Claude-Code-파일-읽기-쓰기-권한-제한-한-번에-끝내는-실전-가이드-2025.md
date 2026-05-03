---
title: "Cursor, Codex, Claude Code: Practical Complete Guide to File Read/Write Permission Restrictions (2025)"
date: 2025-09-23T09:01:41+09:00
slug: "786-Cursor-Codex-Claude-Code-파일-읽기-쓰기-권한-제한-한-번에-끝내는-실전-가이드-2025"
original_url: "https://memoryhub.tistory.com/786"
tistory_id: 786
draft: false
---

As development AI agents touch on "editor+terminal+browser," clearly controlling **which files can be read or modified** has become critical for both security and productivity.

This article provides a **one-stop practical guide** on how to actually implement "read/write restrictions on specific files/folders" in **Cursor, Codex, and Claude Code**, including setup examples and cautions.

---

## Quick Comparison Summary

| Tool | Read Blocking Method | Write Control Point | Caution |
| --- | --- | --- | --- |
| **Cursor** | **.cursorignore blocks AI file access entirely** (indexing, tabs, chat, @symbols) | Modifications generally easy but **approval required for risky operations** | **Terminal/MCP external tool calls aren't blocked by .cursorignore** → Protect sensitive files **outside workspace/OS permissions**. ([Cursor Docs](https://docs.cursor.com/ja/context/ignore-files)) |
| **Codex** | **Global control via sandbox mode**: Read-only / Auto / Full Access | **Approval mode** controls execution/modification scope | Default: **Allow read/write within workspace, approval for external** — Fine-grained ignore files **not yet provided (feature request exists)**. ([OpenAI Developer](https://developers.openai.com/codex/security/?utm_source=chatgpt.com)) |
| **Claude Code** | **.claude/settings.json permission rules**: deny/allow/ask + glob patterns | /permissions, **allowlist**, **hooks**, canUseTool for fine control | Pattern example: Read(./.env) **deny**, Write(./production/**) **ask** — SDK uses same rules. ([Claude Docs](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-permissions)) |

---

# 1) Cursor: **.cursorignore** to Block "Reading" Itself and Approval for Risky Operations

### Core Configuration

- Place **.cursorignore** in project root, and Cursor **completely hides files/folders from indexing, tabs, chat, @symbol contexts**. Uses gitignore syntax. Example:
- # Sensitive info .env secrets/** *.pem # Large/unnecessary dist/ *.log
- **Hierarchical ignore** feature applies .cursorignore from parent directories. (Settings → Features → Editor → Hierarchical Cursor Ignore) ([Cursor Docs](https://docs.cursor.com/ja/context/ignore-files))

### Write and Command Execution

- **Reading** is generally possible without approval (except files blocked by .cursorignore).  
  **Command execution and sensitive operations require approval by default**, though some have allowlists—**not recommended as a security control**. ([Cursor Docs](https://docs.cursor.com/en/account/agent-security))

### Practical Production Notes

- .cursorignore is **strong for editor, indexer, conversation context**, but **doesn't block "external tool calls" like terminal/MCP at the OS level**. After approval, a shell can run `cat secrets.env`.  
  → **Move sensitive files outside workspace** or add **OS permissions (ACL/permission bits)**. ([Cursor Docs](https://docs.cursor.com/ja/context/ignore-files))

---

# 2) Codex: **Sandbox & Approval Mode** for Step-by-Step Read/Write Limiting

### Core Concept

- Codex (2025) CLI/IDE extensions have **sandbox** and **approval mode**.
  - Default (**Auto/Basic Mode**): **Within workspace** reads, modifications, commands proceed smoothly; **external/network risky operations request approval**.
  - **Read-only**: **Read-only** (no modifications/commands).
  - **Full Access**: Warning level. Minimal approval prompts (experimental use recommended). ([OpenAI Developer](https://developers.openai.com/codex/security/?utm_source=chatgpt.com))

### Practical Recipe

- **Read-only mode (completely safe)**
- codex --sandbox read-only --ask-for-approval never # Workspace read-only, never ask approval
- **Basic (convenient) mode**: Workspace modifications/commands proceed naturally, risky ops need approval.  
  Switch modes as needed via /approvals command. ([OpenAI Developer](https://developers.openai.com/codex/security/?utm_source=chatgpt.com))

### Current Limitations & Tips

- No official **.codexignore** style **file-level denylist** (feature request in progress). Move sensitive files **outside project** or protect with **OS permissions**. ([GitHub](https://github.com/openai/codex/issues/1397?utm_source=chatgpt.com))

---

# 3) Claude Code: **.claude/settings.json Permission Rules** + **Hooks/canUseTool** for Fine Control

### Easiest Way: .claude/settings.json

Declare "allow/deny/ask" rules with **glob patterns**:

```
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./secrets/**)",
      "WebFetch"
    ],
    "ask": [
      "Write(./production/**)",
      "Bash(git push:*)"
    ],
    "allow": [
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ]
  }
}
```

- Rules evaluated in order: deny → allow → ask → (others) canUseTool.
- File rules use **globs** (./secrets/**), Bash rules use **prefix matching** (Bash(npm:*)). ([Claude Docs](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-permissions))

### Finer Control

- **/permissions command** or **allowlist** manage per-session tool approval.
- **canUseTool callback**: Code-level runtime "allow/deny" decisions.
- **Hooks (PreToolUse/PostToolUse)**: Intercept before/after for logging, validation, blocking. ([Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices))

> Note: Some versions had config-ignore bugs (may be fixed in updates)—verify latest behavior. ([GitHub](https://github.com/anthropics/claude-code/issues/3501?utm_source=chatgpt.com))

---

## Ready-to-Use **Permission Recipes**

### Cursor

```
# .cursorignore (root)
.env
secrets/**
**/*.pem
dist/
*.log
```

- Hierarchical Cursor Ignore applies parent rules.
- For indexing-only exclusion, use .cursorindexingignore. ([Cursor Docs](https://docs.cursor.com/ja/context/ignore-files))

### Codex

```
# Read-only session startup
codex --sandbox read-only --ask-for-approval never

# Basic mode (workspace natural ops, risky ops need approval)
codex            # Switch modes via /approvals in session
```

- Protect sensitive files **outside workspace** or with **OS permissions (read-only/owner-only)**. ([OpenAI Developer](https://developers.openai.com/codex/security/?utm_source=chatgpt.com))

### Claude Code

```
// .claude/settings.json
{
  "permissions": {
    "deny":  ["Read(./.env)", "Read(./secrets/**)"],
    "ask":   ["Write(./production/**)", "Bash(git push:*)"],
    "allow": ["Bash(npm run test:*)"]
  }
}
```

- Add **hooks** for extra monitoring/blocking logic if needed. ([Claude Docs](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-permissions))

---

## Mini Checklist to Complete Safety

- **Secrets outside repository** (or deployment system's secret manager)
- Agent works **under branch/git management only**
- Cursor **blocks reads via .cursorignore**
- Codex **switches Read-only/Auto appropriately**
- Claude Code declares **deny/ask/allow via .claude/settings.json**
- **Default approvals preserved** + gradually relax only as needed

---

## Reference Documentation

- Cursor: **Ignore files**, **Agent Security**, **Codebase Indexing**. ([Cursor Docs](https://docs.cursor.com/ja/context/ignore-files))
- Codex: **Security & Sandbox/Approval modes** (official guide), **Mode summary**, **ignore file feature request issue**. ([OpenAI Developer](https://developers.openai.com/codex/security/?utm_source=chatgpt.com))
- Claude Code: **Permissions (config/rules/hooks/SDK)**, **Best Practices (allowlist, /permissions)**. ([Claude Docs](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-permissions))

---

### One-Line Conclusion

**Read via .cursorignore / Write via approval·rules (Approvals/Rules)** — master this combo and **prevent most accidents**.
