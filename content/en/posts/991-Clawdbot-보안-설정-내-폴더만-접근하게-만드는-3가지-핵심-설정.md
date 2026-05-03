---
title: "🔐 Clawdbot Security Setup: 3 Key Settings to Restrict Access to Your Folders Only"
date: 2026-01-26T20:02:46+09:00
slug: "991-Clawdbot-보안-설정-내-폴더만-접근하게-만드는-3가지-핵심-설정"
original_url: "https://memoryhub.tistory.com/991"
tistory_id: 991
draft: false
---

```
    ┌─────────────────────────────────────┐
    │     🔐  CLAWDBOT SECURITY CONFIG  🔐    │
    │                                         │
    │   ┌───────────────────────────────┐     │
    │   │  SANDBOX    │   TOOL POLICY   │     │
    │   │  ┌───────┐  │   ┌─────────┐   │     │
    │   │  │ 🐳    │  │   │ allow[] │   │     │
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

It's uncomfortable to give AI agents full computer access. What if you say "organize files" and it touches system files? Clawdbot provides powerful security settings, but from official docs alone it's unclear where to start.

**After reading this guide, you'll complete settings that precisely open only desired folders while keeping web browsing and skills functional.**

**One-sentence summary:** Sandbox (execution environment) + Tool Policy (tool permission) + Bind Mount (directory access)

Configure just these 3 to perfectly control AI agent file access.

## Background

Clawdbot is a personal AI agent platform. Through WhatsApp, Telegram, Discord and other channels, you can chat with AI and have it perform file read/write, code execution, web browsing.

The problem is **default settings allow full host access**.

> Clawdbot's security operates in 3-layer structure. Sandbox controls "where" execution happens, Tool Policy controls "what" executes, Bind Mount controls "which folder" gets accessed.

Many users think "running Docker would be safer."

But even with Sandbox on, incorrect Bind Mount configuration exposes sensitive host directories.

Conversely, Tool Policy alone without Sandbox executes permitted tools directly on the host, causing unexpected results.

| Layer | Role | Main Config Key |
| --- | --- | --- |
| Sandbox | Tool execution environment (Docker vs Host) | `agents.defaults.sandbox.*` |
| Tool Policy | Allow/block tool list | `tools.*`, `tools.sandbox.tools.*` |
| Bind Mount | Directories accessible from container | `sandbox.docker.binds` |

Config file location is `~/.clawdbot/clawdbot.json`.

## Detailed Core Settings Analysis

### Sandbox Mode: Isolation of Execution Environment

Sandbox mode determines **where** tools execute.

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

**Mode option comparison:**

| Value | Behavior | Suitable Situation |
| --- | --- | --- |
| `"off"` | All tools run on host | Trusted local environment, maximum performance needed |
| `"non-main"` | Sandbox applies only to group/channel sessions | Personal chat freely, shared chat restricted |
| `"all"` | All sessions run in sandbox | Security is top priority |

**Important:** In `"non-main"` mode, the "main" standard is `session.mainKey`. Group chats and channels are automatically classified as non-main, applying sandbox.

### Workspace Access: Basic Workspace Permissions

```
{
  "sandbox": {
    "workspaceAccess": "none"
  }
}
```

| Value | Behavior | Security Level |
| --- | --- | --- |
| `"none"` | Use isolated sandbox workspace | Most secure |
| `"ro"` | Mount agent workspace to `/agent` read-only | Medium |
| `"rw"` | Mount agent workspace to `/workspace` read-write | Use with caution |

Setting to `"none"` creates isolated workspace under `~/.clawdbot/sandboxes`.

Skill files automatically mirror to this space, no extra setup needed.

### Bind Mount: Open Only Specific Directories

**This is the core setting.** Through Bind Mount, you can expose only specific host directories to the container.

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

Format is `hostpath:containerpath:mode`.

| Mode | Meaning |
| --- | --- |
| `:rw` | Read/write (default) |
| `:ro` | Read-only |

**Directories not specified in binds are inaccessible.**

This is the security core.

### Tool Policy: Tool Allowlist Configuration

Specify exactly which tools can be used within the sandbox.

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

**Available Tool Groups:**

| Group | Included Tools |
| --- | --- |
| `group:runtime` | exec, bash, process |
| `group:fs` | read, write, edit, apply_patch |
| `group:sessions` | sessions_list, sessions_history, sessions_send, sessions_spawn |
| `group:memory` | memory_search, memory_get |
| `group:ui` | browser, canvas |

`deny` always takes priority. Even if in `allow`, if included in `deny`, it's blocked.

### Network Settings: Enable Web Browsing

Default network setting is `"none"` (no network). You must change this to use web browsing.

```
{
  "sandbox": {
    "docker": {
      "network": "bridge"
    }
  }
}
```

## Practice

### 1. Create Config File

From terminal, create config file.

```
mkdir -p ~/.clawdbot
nano ~/.clawdbot/clawdbot.json
```

### 2. Input Security Settings

Copy and paste the configuration below. Modify `youruser` and paths for your environment.

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

### 3. Build Sandbox Image

Build Docker image for Clawdbot sandbox.

```
# Basic sandbox image
scripts/sandbox-setup.sh

# Image with browser (when using web browsing)
scripts/sandbox-browser-setup.sh
```

### 4. Verify Configuration

Verify settings applied correctly.

```
clawdbot sandbox explain
```

Check the output for:

- `mode: all` - All sessions apply sandbox
- `workspaceAccess: none` - Isolated workspace
- `binds` list - Only intended directories shown
- `allow/deny` list - Tool policy confirmed

## Best Practices/Pattern Comparison

| Scenario | mode | workspaceAccess | binds | network |
| --- | --- | --- | --- | --- |
| Development project work | `all` | `none` | Project folder only `:rw` | `bridge` |
| Document review/reference | `all` | `none` | Document folder only `:ro` | `none` |
| Group chat bot | `non-main` | `none` | Minimum only | `bridge` |
| Complete isolation test | `all` | `none` | None | `none` |

**Configuration Absolutely Avoid:**

| Setting | Risk |
| --- | --- |
| Bind `/var/run/docker.sock` | Host complete control takeover possible |
| Bind entire home directory (`~:/home:rw`) | SSH keys, config files sensitive info exposure |
| `elevated.enabled: true` | Bypass sandbox, run directly on host |

## Conclusion

- Clawdbot security comprises 3 layers: Sandbox (environment), Tool Policy (tools), Bind Mount (directories)
- Only directories specified in `binds` are accessible, so open only needed folders minimally
- Use `clawdbot sandbox explain` command anytime to verify currently applied security settings
- Practical tip: When starting a new project, add only that folder to binds, remove after completion. Build this habit.

## References

- Sandbox vs Tool Policy vs Elevated (https://docs.clawd.bot/gateway/sandbox-vs-tool-policy-vs-elevated)
- Sandboxing (https://docs.clawd.bot/gateway/sandboxing)
- Skills Configuration (https://docs.clawd.bot/tools/skills)
