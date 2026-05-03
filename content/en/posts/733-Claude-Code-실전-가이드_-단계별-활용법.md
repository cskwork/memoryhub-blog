---
title: "Claude Code Practical Guide: Step-by-Step Usage"
date: 2025-07-29T17:34:49+09:00
slug: "733-Claude-Code-실전-가이드_-단계별-활용법"
original_url: "https://memoryhub.tistory.com/733"
tistory_id: 733
draft: false
categories: ["Dev Library"]
tags: ["Claude"]
  hidden: false
cover:
  image: "/images/733-Claude-Code-실전-가이드_-단계별-활용법/img.jpg"
  relative: false
  hidden: false
---

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img.jpg)

Claude Code is a terminal-based AI coding assistant. It analyzes codebases and supports development work.
This guide covers practical usage from beginners to advanced users.

## ? Prerequisites

**Installation Requirements**

- Node.js 18 or higher
- Installation: `npm install -g @anthropic-ai/claude-code`
- Execution: `claude` command in project directory
- On Windows, install in git bash. Must be installed on C drive to use anywhere.

**Basic Safety Rules**

- Can stop work anytime with ESC key
- Safely analyze with Plan mode (Shift+Tab)
- Always backup before important tasks

---

## ? Beginner: Learning Basic Features

### 1. Getting Started and Exploring the Codebase

**Asking Basic Questions**

```
# Understanding the project
"What does this project do?"
"Show me the main components"
"Write and organize the project structure in the docs/ folder"
```

**Using ESC Keyboard Interrupt**

- Use ESC key when work is going in an undesired direction.
- Immediately stop and redirect. Use actively!!!

### 2. Using CLAUDE.md File

Create a `CLAUDE.md` file in the project root to document guidelines.

If you want Claude to create project context, run the following command: ->   /init

```
 /init
```

**Effect**: Claude automatically follows these guidelines for consistent work / improves accuracy by understanding context/contextual information about the project. In business environments where existing code work is needed, detailed definitions of desired coding format/style etc. are necessary for desired results. (Similar to giving clear instructions to a junior developer who knows nothing)

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img.png)

### 3. Using Plan Mode

- **Switch**: Shift+Tab on MacOS. Alt+M on Windows
- **Purpose**: Safely analyze in read-only mode
- **Usage**: Establish plan with "Research the best approach" then execute

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_1.png)

---

## ? Intermediate: Configuration and Tool Integration

### 1. settings.json Permission Setup

`~/.claude/settings.json` can be subdivided into project-specific `.claude/settings.json`

Security configuration with `~/.claude/settings.json` file:

```
{
  "permissions": {
    "allow": [
      "Task",
      "Bash(npm run lint)",
      "Bash(npm run test:*)",
      "Bash(git log:*)",
      "Bash(curl:*)",
      "Bash(ls:*)",
      "Bash(find:*)",
      "Bash(ollama:*)",
      "Bash(source:*)",
      "Bash(which:*)",
      "Read(~/.zshrc)",
      "Grep",
      "List",
      "Read",
      "WebFetch",
      "WebSearch"
    ],
    "deny": [
      "Bash(rm:*)",
      "Read(application.yml)",
      "Read(**/application.yml)"
    ],
    "defaultMode": "plan"
  },
  "env": {
    "BASH_DEFAULT_TIMEOUT_MS": "60000"
  },
  "includeCoAuthoredBy": false
}
```

**Purpose**: Block dangerous commands, allow only safe commands

### 2. Commands (Slash Commands)

Save frequently used prompts in `.claude/commands/` directory:

```
# Create command save folder
mkdir -p ~/.claude/commands

# Add feature
echo "Ultra Think. We would like to add [FEATURE] to this system. This feature should [DESCRIBE]. It must align with our existing system of [EXPLAIN]. 
Create a detailed implementation plan that outlines each file that must be touched, and specific changes that must be made. 
We are looking for a clean, seamless implementation strategy. You must conduct thorough research during this planning phase. Your plan should not contain any analysis or code review. I expect that to be completed by the time you present your plan.  
Prepare a detailed action plan for my review. Together we will finalize and refine the plan for execution." > ~/.claude/commands/add-feature.md

# Review feature
echo "Think. Audit the [FEATURE] system for completeness, security standards, and correct wiring, specifically related to [REQUIREMENT]. 
Identify dead or redundant code, scattered or overly complex logic, and areas where things can be simplified but maintain functionality. Also note gaps in implementation or incomplete refactors, loose ends, and sources of confusion.
Present a focused audit with a step-by-step action plan that outlines the current implementation, discovered errors, opportunities for improvement, and potential for optimization.
Prepare to enhance, debug, or refactor the system as needed according to user feedback in order to ensure a robust and reliable operation that is flexible, extensible, easy to maintain, and crafted with precision." > ~/.claude/commands/review-feature.md
```

**Usage**: Type `/review-feature` to invoke immediately

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_2.png)

### 3. MCP (Model Context Protocol) Integration

```
# Connect external tools
claude mcp add --transport http context7 https://mcp.context7.com/mcp
claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp
```

**Usage Examples**:

- context7 finds official documentation like react, vue3 and follows development principles.

### 4. YOLO Mode (⚠️ Use with Caution)

```
claude --dangerously-skip-permissions
```

**Advantages**: Speed increases by skipping all confirmation steps, useful for large refactoring and boilerplate generation

**Risks**: Possible file deletion, data leakage

**Safe Usage**: Use only in isolated environment

---

## ? Advanced: Complex Workflow Optimization

### 1. Using Subagents

Delegate work to specialized AI agents → Keep main context clean (shorter):

```
# Input this command to create the agent you want
/agents
```

**Effect**: Prevent main context pollution, specialized analysis

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_3.png)

### 2. Ultra-think Mode → Derive Deep Design and Performance Strategy

- Use only for important decisions due to high token consumption

```
"Plan the implementation strategy ultrathink"
```

**Purpose**: Deep analysis of complex problems  
**Caution**: Increased token usage

### 3. Handling Large Codebases

1. Plan mode: "Analyze project and outline steps to add OAuth login."
2. Validate change scope then implement

**Use keyword minimal when requesting minimal changes**:

```
"Refactor client.py in Supabase folder and add minimal user authentication feature with error handling"
```

**Advantages**:

- Add features with minimal changes
- Preserve existing structure
- Minimize side effects

**Other Tools**:

1. Write list of key files in CLAUDE.md
2. Connect Git, Deepwiki, Context7 tools via MCP
3. Establish detailed plan with ultra-think

---

## ✅ Real-World Application Checklist

### Beginner

- Master ESC interrupt usage
- Write CLAUDE.md file
- Safely analyze with Plan mode

### Intermediate

- Configure settings.json permissions
- Register frequently used Commands
- Integrate MCP tools
- Use YOLO mode only in isolated environment

### Advanced

- Delegate work with Subagents
- Complex analysis with ultra-think
- Efficient feature addition with minimal prompt

---

## ? Glossary

- **ESC Interrupt**: A "stop" button you press when in danger, like a car's brake
- **Plan Mode**: A mode for planning before actually building, like sketching before drawing
- **YOLO Mode**: A mode for working quickly with "just do it", but be careful as mistakes can happen
- **Subagents**: Expert friends, special helpers who help with difficult tasks
- **Large Codebase**: Complex code chunks like very large Lego creations
- **Minimal Prompt**: A way to say only what's necessary, like not giving long explanations instead of "please give water"

Follow this guide step-by-step and safely leverage the powerful features of Claude Code!

#### To understand more deeply with official documentation

- <https://docs.anthropic.com/en/docs/claude-code/common-workflows>

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_4.png)

![](/images/733-Claude-Code-실전-가이드_-단계별-활용법/img_5.png)

## Cookies

- Presentation materials created by ChatGPT agent mode

[Claude Code - Practical Guide from Beginner to Advanced.pptx3.19MB](./file/클로드 코드 - 초보부터 고급까지 실전 활용 가이드.pptx)
