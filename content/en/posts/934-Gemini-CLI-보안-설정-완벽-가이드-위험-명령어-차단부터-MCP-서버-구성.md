---
title: "? Gemini CLI Security Configuration Guide: Blocking Dangerous Commands to MCP Server Setup"
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

What if an AI coding tool executed `rm -rf /` at the terminal? A Gemini CLI vulnerability discovered shortly after launch in June 2025 revealed that malicious code could execute system commands without user knowledge. Google patched it quickly, but the incident taught us one lesson: **security configuration for AI agent tools is not optional—it's mandatory.** This article covers using Gemini CLI's multi-layered security to build a safe yet powerful AI development environment.

**TL;DR:** Gemini CLI restricts commands via coreTools/excludeTools, isolates execution with Docker/Podman sandboxes, and safely connects external tools through per-project MCP server configuration.

---

## Background

Gemini CLI is an open-source AI agent Google released June 25, 2025, enabling direct terminal interaction with Gemini models for code writing, debugging, and file manipulation. The problem: this power could lead to security threats.

> **Gemini CLI Security Model**: A multi-layer defense system (sandboxing, tool restrictions, approval modes) protecting against risks when AI agents execute system commands

The vulnerability discovered by security researchers Tracebit just two days after launch was shocking. Hidden prompt injection in malicious README.md combined with whitelist bypass allowed environment variables to leak to external servers while users analyzed code.

Google classified it as P1/S1 (critical) and patched it in v0.1.14.

The issue: **default configuration is "no sandbox" mode.** A red warning appears at screen bottom, but many developers ignore it. Secure Gemini CLI usage requires manual security configuration.

---

## Understanding Configuration File Structure

Gemini CLI settings follow a 4-tier priority system. Higher numbers take precedence.

| Priority | Config File Location | Scope |
| --- | --- | --- |
| 1 | `/etc/gemini-cli/system-defaults.json` (Linux) | System defaults |
| 2 | `~/.gemini/settings.json` | Global user |
| 3 | `project/.gemini/settings.json` | Project-specific |
| 4 | `/etc/gemini-cli/settings.json` | System enforcement |

Single-value settings (theme, etc.) are overridden by higher priority; arrays/objects (mcpServers, includeDirectories) merge. Understanding this explains why per-project MCP configuration works.

---

## Blocking Dangerous Commands: coreTools and excludeTools

### Whitelist Approach (coreTools) - Recommended

Safest method is explicitly specifying allowed tools. Unspecified tools can't be used.

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

This config allows only file reading, listing, searching, and Git status. Dangerous commands like `rm`, `curl`, `wget` are blocked entirely.

### Blacklist Approach (excludeTools)

Blocks specific commands while allowing others. Less secure than whitelist but more flexible.

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

**Caution:** excludeTools uses string-based blocking vulnerable to bypass. For example, blocking `rm -rf` might not stop `rm -r -f` or `eval` within scripts. Prefer coreTools whitelist when possible.

### Using Both Settings Together?

excludeTools takes priority over coreTools. Tools in both lists are blocked.

---

## Sandbox Configuration: Isolating Execution Environment

Sandboxes isolate AI-executed commands in a segregated environment, preventing system damage. Gemini CLI supports three sandbox approaches.

### 1. macOS Seatbelt (macOS Only)

Leverages macOS's built-in sandbox. Lightweight and fast, but macOS-specific.

```
# Enable via environment variable
export GEMINI_SANDBOX=sandbox-exec

# Choose profile (default: permissive-open)
export SEATBELT_PROFILE=restrictive-closed
```

Seatbelt profile options:

| Profile | File Write Restrictions | Network |
| --- | --- | --- |
| permissive-open | Outside project limited | Allowed |
| permissive-closed | Outside project limited | Blocked |
| permissive-proxied | Outside project limited | Proxy only |
| restrictive-open | Strict restrictions | Allowed |
| restrictive-closed | Maximum restrictions | Blocked |

### 2. Docker-Based Sandbox

Provides complete process isolation cross-platform. Choose this for maximum security.

```
{
  "tools": {
    "sandbox": "docker"
  }
}
```

For custom per-project sandboxes, create `.gemini/sandbox.Dockerfile`.

```
FROM gemini-cli-sandbox

# Add project dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pytest black

# Copy custom config
COPY ./scripts /app/scripts
```

Build and run:

```
export BUILD_SANDBOX=true
gemini -s -p "run tests"
```

### 3. Podman-Based Sandbox

Similar to Docker but runs daemonless. May require additional configuration in SELinux environments.

```
export GEMINI_SANDBOX=podman
export SANDBOX_FLAGS="--security-opt label=disable"
```

### YOLO Mode and Auto-Sandbox Activation

Using `--yolo` or `--approval-mode=yolo` auto-activates sandbox. All tool execution is auto-approved while running isolated, reducing risk.

```
gemini --yolo -p "refactor this code"
# Automatically runs in sandbox
```

Enterprise environments can disable YOLO mode system-wide.

```
{
  "security": {
    "disableYoloMode": true
  }
}
```

---

## Project-Level MCP Server Configuration

MCP (Model Context Protocol) enables Gemini CLI interaction with external systems. Connect GitHub, databases, APIs as MCP servers to extend AI capabilities.

### Basic MCP Server Setup

Configure in `~/.gemini/settings.json` or project's `.gemini/settings.json`.

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

### Per-MCP-Server Tool Restrictions

Allow or block specific tools from certain MCP servers.

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

This config permits only search and retrieval from analyzer server, blocking deletion/modification.

### Remote MCP Server Connection

HTTP/SSE-based remote servers work too. Supports OAuth authentication.

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

### MCP Server Allowlist (Enterprise)

System admins can enforce only approved MCP servers.

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

Servers not in `mcp.allowed` won't run even if users add them.

---

## Practice: Setting Up a Secure Development Environment

### Step 1: Create Global User Configuration

Apply base security settings to `~/.gemini/settings.json`.

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

### Step 2: Add Project-Level MCP Servers

For backend projects, add database MCP to `.gemini/settings.json`.

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

### Step 3: Set Environment Variables

Create `.gemini/.env` at project root.

```
# Database connection
DATABASE_URL="postgresql://user:pass@localhost:5432/mydb"

# GitHub token (optional)
GITHUB_TOKEN="ghp_xxxxxxxxxxxx"

# Force sandbox activation
GEMINI_SANDBOX=docker
```

### Step 4: Enable Trusted Folders Feature

Control config loading on first folder access.

```
{
  "security": {
    "trustedFolders": true
  }
}
```

When enabled, opening Gemini CLI in new folders shows a trust dialog. Untrusted folders disable project config, MCP servers, and auto-context loading.

---

## Best Practices and Pattern Comparison

| Security Level | Configuration | Suitable For | Considerations |
| --- | --- | --- | --- |
| Minimal | Defaults (no sandbox) | Trusted personal projects | Don't ignore red warning |
| Medium | excludeTools + Seatbelt | General development | Bypass risks exist |
| High | coreTools + Docker | Team collaboration, external code | Docker install required |
| Enterprise | System settings + MCP allowlist | Corporate environments | Admin rights needed |

---

## Conclusion

Gemini CLI security is completed by **isolating execution with sandboxes**, **restricting tools with coreTools**, and **fine-grained MCP-per-server permissions**. Since defaults are "no sandbox," manual security configuration is essential. As AI agents grow more powerful, security settings become increasingly critical.

**Practical tip: Add `"sandbox": "docker"` to `~/.gemini/settings.json` today and register only frequently-used commands in coreTools.**

---

## References

- Gemini CLI Official Configuration Docs (<https://geminicli.com/docs/get-started/configuration/>)
- Gemini CLI Sandbox Guide (<https://geminicli.com/docs/cli/sandbox/>)
- Gemini CLI Enterprise Configuration (<https://geminicli.com/docs/cli/enterprise/>)
- MCP Server Configuration Guide (<https://geminicli.com/docs/tools/mcp-server/>)
- Gemini CLI GitHub Repository (<https://github.com/google-gemini/gemini-cli>)
- Tracebit Security Vulnerability Analysis (<https://tracebit.com/blog/code-exec-deception-gemini-ai-cli-hijack>)
