---
title: "Claude Code: Best Practices for Agentic Coding"
date: 2025-06-04T18:14:55+09:00
slug: "648-Claude-Code_-에이전트-코딩을-위한-모범-사례"
original_url: "https://memoryhub.tistory.com/648"
tistory_id: 648
draft: false
categories: ["Dev Language"]
tags: ["Vibe Coding"]
---

Claude Code developed by Anthropic is a command-line (CLI) based agentic coding tool[1]. Through this tool, developers can write, edit, and debug code with natural language commands, and automate workflows through integration with development tools like Git[4][8][14]. Claude Code adopts a flexible, low-level design that doesn't force specific workflows, providing users with a powerful and secure coding environment that can be freely customized to their environment[1][10]. However, this flexibility may require some learning for developers using it for the first time[1].

This article introduces tips and best practices for using Claude Code effectively across various codebases, languages, and environments.

### 1. Customize Settings

Claude Code works by automatically importing context from prompts. This process can consume time and tokens, so optimizing your environment is important for improving efficiency.

**Create a CLAUDE.md File**  
`CLAUDE.md` is a special file that Claude automatically includes in the context at the start of a conversation. Documenting the following information in this file is useful:

- Frequently used bash commands
- Core files and utility functions
- Code style guidelines and testing instructions
- Repository rules (e.g., branch naming conventions)
- Development environment configuration information
- Project-specific quirks or warnings
- Other information Claude should remember

The `CLAUDE.md` file can be written concisely and readably without any special format. This file can be placed in multiple locations:

- **Repository Root**: The most common usage, save as `CLAUDE.md` to share with the team, or manage personal settings as `CLAUDE.local.md` after adding to `.gitignore`.
- **Parent and Subdirectories**: In a monorepo structure, multiple `CLAUDE.md` files can be hierarchically loaded.
- **Home Folder (`~/.claude/CLAUDE.md`)**: Applies globally to all Claude sessions.
- Running the `/init` command will automatically create a `CLAUDE.md` file for you.

**Refine CLAUDE.md File**  
The `CLAUDE.md` file becomes part of the prompt, so continuous improvement is necessary. Rather than indiscriminately adding content, it's better to test the model's responses and improve guideline adherence. Using the `#` key to instruct Claude will automatically integrate that content into the `CLAUDE.md` file, allowing you to strengthen your documentation in real-time while coding.

**Manage Allowed Tools List**  
By default, Claude Code requests user permissions for tasks that can modify the system, such as file writing or specific bash commands[5]. This is a conservative approach for safety, and you can skip permission requests for frequently used safe tools (e.g., file editing, git commits) by modifying the allowlist.

- Select "Always Allow" during a session
- Manage allowlist with the `/permissions` command
- Edit `.claude/settings.json` or `~/.claude.json` files directly
- Set session-specific permissions using the `--allowedTools` CLI flag

**Install gh CLI When Using GitHub**  
If GitHub CLI (`gh`) is installed, Claude can perform GitHub-related tasks more smoothly, such as creating issues and opening pull requests[4].

### 2. Provide Claude with More Tools

Claude can access the shell environment and can also leverage more complex tools through MCP (Model Context Protocol) and REST APIs[3][6].

- **bash Tools**: Claude knows common utilities like `gh`, but custom tools require separate explanation. You can tell the tool's name and usage examples, or instruct it to run `--help` commands to learn on its own. Frequently used tools should be documented in `CLAUDE.md`[6].
- **Use with MCP**: Claude Code works as both MCP server and client. By adding servers like Puppeteer or Sentry to your project through `.mcp.json`, all team members working in the repository can immediately use those tools[6].
- **Custom Slash Commands**: For repetitive tasks like debugging or log analysis, you can store prompt templates in the `.claude/commands` folder to create your own slash commands. For example, you can create commands like `/project:fix-github-issue` that automatically fix GitHub issues.

### 3. Common Workflows

Claude Code doesn't force specific workflows, but there are several patterns proven effective by the community[1].

- **Explore, Plan, Code, Commit**: A general-purpose workflow suitable for solving complex problems. Have Claude read relevant files and create a plan, then if the plan seems reasonable, instruct coding and finally request commit and PR creation[6]. Using keywords like "think" prompts Claude to think more deeply.
- **Test-Driven Development (TDD)**: Have Claude write test cases first and confirm tests fail before committing. Then instruct writing code to pass the tests. In this process, Claude iterates through code writing, test execution, and fixes to complete the deliverable.
- **Visual Goal-Based Development**: Use tools like Puppeteer to take UI screenshots or provide design mockup images to present visual goals. Claude iterates through modifying code and taking screenshots until results match the goal.
- **Safe YOLO Mode**: Use the `--dangerously-skip-permissions` flag to skip all permission checks and have Claude perform tasks uninterrupted. Useful for predictable tasks like linting fixes, but due to risks like data loss, using it in isolated environments like internet-blocked Docker containers is recommended.
- **Codebase Q&A**: Useful when adapting to new codebases. Ask questions like "How does logging work?" that you'd ask a colleague, and Claude will explore the codebase and find answers[4][5].
- **Git and GitHub Integration**: Claude can handle most Git tasks including writing commit messages, searching git history, and resolving merge conflicts[4][11]. It can also automate GitHub-related work like creating PRs, incorporating code review feedback, and fixing failed builds[4].
- **Jupyter Notebook Work**: Read and write Jupyter notebooks, interpret image outputs to help with data exploration and visualization work. Requesting to "make it aesthetically pleasing" can enhance the visual quality of results.

### 4. Workflow Optimization

Several optimization suggestions that apply to all workflows[14].

- **Specific Instructions**: Providing specific instructions like "Add a test to foo.py handling edge cases of logged-out users. Don't use mocks" results in higher success rates than vague instructions like "Add tests to foo.py".
- **Use Images**: Pasting screenshots or providing file paths to give Claude visual context is especially useful for UI development and debugging.
- **File and URL References**: Use tab completion to quickly reference files or folders, and provide URLs directly so Claude can fetch necessary information.
- **Early Course Correction**: Review plans before coding, and press Esc to stop tasks or modify previous prompts for early course correction to get better results faster.
- **Context Management**: Periodically reset the context window with the `/clear` command to prevent irrelevant information from impacting performance.
- **Checklist Usage**: For complex tasks, having Claude use markdown files or GitHub issues as checklists improves performance through systematic task handling.
- **Data Transfer**: You can transfer data through various methods like pasting directly in prompts, using pipes (`|`) for input, or having Claude read files.

### 5. Infrastructure Automation Using Headless Mode

Claude Code supports headless mode for non-interactive environments like CI/CD or Git pre-commit hooks[1]. Enable this mode by passing prompts with the `-p` flag, and it can be used for tasks like GitHub issue classification or subjective code review as a linter[14].

### 6. Multiple Claude Workflows

Running multiple Claude instances in parallel can handle more complex tasks efficiently[1].

- **Role Division**: Have one Claude write code while another reviews or writes tests to improve deliverable quality.
- **Multiple Checkouts**: Check out Git repositories in multiple folders and run different tasks simultaneously in each to reduce waiting time.
- **git worktree Usage**: Using `git worktree` allows working on multiple branches of the same repository simultaneously, useful for parallel processing of different independent tasks.
- **Custom Harness**: Combine headless mode with scripts to build highly automated workflows integrating Claude into large-scale code migrations (fan-out) or existing data pipelines (pipelining)[14].

**Sources**  
[1] Claude Code: Best Practices for Agentic Coding - GeekNews <https://news.hada.io/topic?id=20430>  
[2] Claude Code Complete Guide | AI Coding Tool Installation and Usage <https://www.magicaiprompts.com/docs/claude/claude-code/>  
[3] Claude Code: Possibilities and Limitations of New AI Code Assistant <https://digitalbourgeois.tistory.com/951>  
[4] Claude Code - velog <https://velog.io/@yeonililiil/Claude-Code>  
[5] Claude Code Overview - Rudaks - Tistory <https://rudaks.tistory.com/entry/Claude-Code-%EB%B2%88%EC%97%AD-Claude-Code-%EA%B0%9C%EC%9A%94-Claude-Code-overview>  
[6] The Ultimate AI Assistant for Developers, Claude Code Complete Guide <https://digitalbourgeois.tistory.com/1308>  
[7] The End of Code Editors? Emergence of 'Claude Code' - YozM IT <https://yozm.wishket.com/magazine/detail/3162/?data=UD5w1+U5rF0uSl5hLAJAuZMMHaM5MGOAlLF1nFAJQHk%3D>  
[8] Claude Code Overview - Anthropic API <https://docs.anthropic.com/ko/docs/claude-code/overview>  
[9] 2025 Claude Code, AI Coding Innovation Method - Apidog <https://apidog.com/kr/blog/claude-code-coding/>  
[10] [AI Coding Agent Comparison Translation] Claude Code vs. OpenAI Codex <https://rudaks.tistory.com/entry/AI-%EC%BD%94%EB%94%A9-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8-%EB%B9%84%EA%B5%90-%EB%B2%88%EC%97%AD-Claude-Code-vs-OpenAI-Codex-2025%EB%85%84-AI-%EC%BD%94%EB%94%A9-%EB%B0%B0%ED%8B%80>  
[11] AI Coding Tool Evolution, Anthropic 'Claude Code' Practical Usage - Threads <https://www.threads.com/@choi.openai/post/DIvZ5SMvJX8/ai-%EC%BD%94%EB%94%A9-%EB%8F%84%EA%B5%AC%EC%9D%98-%EC%A7%84%ED%99%94-%EC%95%A4%ED%8A%B8%EB%A1%9C%ED%94%BD-claude-code%EC%9D%98-%EC%8B%A4%EC%A0%84-%ED%99%9C%EC%9A%A9%EB%B2%95%EC%95%A4%ED%8A%B8%EB%A1%9C%ED%94%BD%EC%9D%B0-%EC%B5%9C%EA%B7%BC-%EB%B0%9C%ED%91%9C%ED%95%9C-%EC%83%88%EB%A1%9C%EC%9A%B4-%EB%8F%84%EA%B5%AC-claude-code%EA%B0%80-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%93%A4%EC%97%90%EA%B2%8C-%EB%A7%8E%EC%9D%80->  
[12] Claude Code Usage Guide - Hyperithm Tech Blog <https://tech.hyperithm.com/claude_code_guides>  
[13] GeekNews on X: "Claude Code: Best Practices for Agentic Coding" - X <https://x.com/GeekNewsHada/status/1913772292011921808>  
[14] Programming programming.ai_tools
