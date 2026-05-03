---
title: "🔧 Atlassian CLI Complete Guide: Escaping the Jira Click Hell"
date: 2025-12-19T10:00:35+09:00
slug: "940-Atlassian-CLI-완벽-가이드-Jira-클릭-지옥에서-탈출하는-법"
original_url: "https://memoryhub.tistory.com/940"
tistory_id: 940
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
---

```
    ___  ________    _____ 
   /   |/_  __/ /   /  ___|
  / /| | / / / /    \__ \ 
 / ___ |/ / / /___  ___/ / 
/_/  |_/_/ /_____/ /____/  

  Atlassian CLI (ACLI)
  Control Jira from the Terminal
```

Imagine needing to change the status of 100 issues in Jira. If you click through one by one, it takes at least 30 minutes. But what if you could do it with just one line in the terminal? **Atlassian CLI (ACLI) is an official tool that lets you control Jira, Confluence, and other Atlassian products directly from the command line**. With its official launch across all Jira Cloud plans in May 2025, anyone can now use it for free.

**One-liner summary:** Atlassian CLI (ACLI) is an official CLI tool for automating Jira and Confluence tasks in the terminal, enabling bulk operations and scripting.

## Background

Jira and Confluence have become the standard tools for development teams worldwide. However, as projects scale, problems emerge. Managing thousands of issues, dozens of projects, and multiple sites has limits with GUI alone.

> ACLI (Atlassian Command Line Interface) is a text-based tool for interacting with Atlassian products.

Previously, third-party CLIs from Appfire (formerly Bob Swift) were the only option. However, in May 2025, Atlassian launched the official ACLI, changing the landscape. The official ACLI is free for all Jira Cloud plans and is provided as a self-contained binary without requiring Java.

| Aspect | Official Atlassian ACLI | Appfire ACLI (Third-party) |
| --- | --- | --- |
| Launch | May 2025 | 2008 (Bob Swift) |
| Cost | Free (included in Jira Cloud) | Requires paid license |
| Installation | Self-contained binary (Homebrew/curl) | Requires Java + connector app |
| Scope | Jira Cloud focused | Jira/Confluence/Bitbucket/Bamboo |
| Command Style | `acli jira workitem create` | `acli myjira --action createIssue` |

This article focuses on **the official Atlassian ACLI**. If you need third-party solutions, refer to Appfire documentation.

## Why CLI: GUI vs CLI Comparison

Let's examine the reasons for using CLI through specific scenarios.

**Scenario: Change 50 issues to "In Progress"**

The GUI approach requires repeating 50 times: open each issue, click the status dropdown, and save. The CLI approach specifies targets with JQL and handles everything at once.

```
acli jira workitem transition --jql "project = TEAM AND status = 'To Do'" --status "In Progress"
```

**ACLI's core advantages** can be summarized in three points. First, speed. It handles bulk operations in seconds that take tens of minutes in the UI. Second, automation. You can integrate it into CI/CD pipelines or cron jobs as scripts. Third, precise control. You can validate each command and execute step by step, reducing the risk of mistakes.

## Practical Exercise

### 1. Installation

Installation methods vary by operating system. ACLI supports macOS, Windows, and Linux.

**macOS (Homebrew recommended)**

```
# Add Homebrew tap and install
brew tap atlassian/homebrew-acli
brew install acli

# Verify installation
acli --version
```

**macOS (Manual Installation - Apple Silicon)**

```
# Download binary
curl -LO "https://acli.atlassian.com/darwin/latest/acli_darwin_arm64/acli"

# Grant execute permission
chmod +x acli

# Add to PATH (optional)
sudo mv acli /usr/local/bin/
```

**Windows (PowerShell)**

Download the Windows binary from the Atlassian official site and add it to PATH.

**Linux (Debian/Ubuntu)**

```
curl -LO "https://acli.atlassian.com/linux/latest/acli_linux_amd64/acli"
chmod +x acli
sudo mv acli /usr/local/bin/
```

### 2. Authentication Setup

ACLI supports two authentication methods: API tokens or OAuth.

**Method A: OAuth (Most convenient)**

```
acli jira auth login --web
```

When the browser opens, log in with your Atlassian account and select your site. Once you return to the terminal, authentication is complete.

**Method B: API Token**

First, generate an API token in your Atlassian account settings (https://id.atlassian.com/manage/api-tokens).

```
# Read token from file
acli jira auth login --site "mysite.atlassian.net" --email "user@example.com" --token < token.txt

# Or enter directly
echo "YOUR_API_TOKEN" | acli jira auth login --site "mysite.atlassian.net" --email "user@example.com" --token
```

### 3. Main Command Practice

**List Projects**

```
# 20 recently accessed projects
acli jira project list --recent

# All projects (with pagination)
acli jira project list --paginate

# Output as JSON
acli jira project list --limit 50 --json
```

**Create Issue (Work Item)**

```
# Create basic task
acli jira workitem create --summary "Update API documentation" --project "TEAM" --type "Task"

# Include detailed options
acli jira workitem create \
  --summary "Bug: Login failure" \
  --project "PROJ" \
  --type "Bug" \
  --assignee "developer@company.com" \
  --label "bug,urgent"
```

**Bulk Issue Modification**

```
# Change assignee for multiple issues
acli jira workitem edit --key "TEAM-1,TEAM-2,TEAM-3" --assignee "newowner@company.com"

# Select targets by JQL and modify
acli jira workitem edit --jql "project = TEAM AND labels = 'legacy'" --summary "[Archived]"
```

**Issue Status Transition**

```
# Change single issue status
acli jira workitem transition --key "TEAM-42" --status "Done"

# Change status for all issues matching JQL condition
acli jira workitem transition --jql "project = TEAM AND sprint = 'Sprint 15'" --status "In Progress"
```

### 4. Advanced Usage: Script Automation

ACLI's true power lies in scripting. Below is an example of moving incomplete issues to the next sprint at the end of a sprint.

```
#!/bin/bash
# move_incomplete_issues.sh

CURRENT_SPRINT="Sprint 15"
NEXT_SPRINT="Sprint 16"
PROJECT="TEAM"

# Move incomplete issues to next sprint
acli jira workitem edit \
  --jql "project = $PROJECT AND sprint = '$CURRENT_SPRINT' AND status != Done" \
  --sprint "$NEXT_SPRINT"

echo "Incomplete issues have been moved to $NEXT_SPRINT."
```

## Rovo Dev CLI: AI Coding Agent

In November 2025, Atlassian launched **Rovo Dev CLI** as an extension of ACLI. This allows you to write code and manage Jira issues by conversing with an AI agent in the terminal.

```
# Rovo Dev authentication (requires separate token)
acli rovodev auth login --site "mysite.atlassian.net" --email "user@example.com" --token

# Start interactive mode
acli rovodev run
```

Rovo Dev enables codebase analysis, documentation generation, and Jira issue completion all from the terminal. It's currently in beta and requires Rovo Dev credits.

## Best Practices/Pattern Comparison

| Usage Pattern | Advantages | Cautions |
| --- | --- | --- |
| OAuth authentication (`--web`) | Most convenient, no token management | Requires browser, difficult to use in CI/CD |
| API token authentication | Script/CI/CD friendly | Be careful with token exposure, requires periodic renewal |
| JQL-based bulk operations | Maximum flexibility with conditional processing | Requires learning JQL syntax |
| JSON output (`--json`) | Easy to pipe to other tools | Recommend using JSON parser like jq |
| JSON file input (`--from-json`) | Reusable complex issue structure | Verify JSON schema (`--generate-json`) |

## Conclusion

- ACLI is an official CLI tool for automating repetitive tasks in Jira Cloud, free for all plans
- After installation via Homebrew or curl and authentication with OAuth or API token, you're ready to use it
- Combined with JQL queries, you can create scripts that process hundreds of issues at once

**Practical tip:** Start right away with `brew install acli && acli jira auth login --web`. Try listing projects first (`acli jira project list`) to get the hang of it.

## References

- Atlassian CLI Official Documentation (https://developer.atlassian.com/cloud/acli/guides/introduction/)
- ACLI Installation Guide (https://developer.atlassian.com/cloud/acli/guides/install-acli/)
- ACLI Command Reference (https://developer.atlassian.com/cloud/acli/reference/commands/)
- Atlassian CLI Homebrew Tap (https://github.com/atlassian/homebrew-acli)
- Rovo Dev CLI Introduction (https://www.atlassian.com/blog/announcements/rovo-dev-command-line-interface)
- ACLI for Jira Announcement Blog (https://www.atlassian.com/blog/jira/atlassian-command-line-interface)
