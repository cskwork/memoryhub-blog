---
title: "Claude Code - AI Colleague Developer Working in Your Terminal 🚀"
date: 2025-06-07T13:48:05+09:00
slug: "664-클로드-코드-Claude-Code-터미널에서-일하는-AI-동료-개발자"
original_url: "https://memoryhub.tistory.com/664"
tistory_id: 664
draft: false
---

Have you ever gotten tired of frantically switching between IDE, terminal, and browser while coding? Have you imagined having a junior developer colleague who understands your entire project and smoothly handles all the grunt work? Anthropic's 'Claude Code' that I'll introduce today plays exactly that role[2].

Claude Code is an AI coding agent residing in your terminal[2]. You can delegate complex coding tasks with natural language commands alone[4]. From now on, I'll explain everything about Claude Code clearly and in detail.

## Background

Past AI coding assistants were mostly in separate chat window form. Developers had to copy and paste parts of their current code and manually explain context to get help. This interrupted development flow and made it hard to convey entire project structure.

Claude Code, however, integrates directly into the terminal, the core of development environments[2][3]. Thanks to this, developers don't need to specify files one by one; a technology called 'agentic search' allows it to understand entire project structure and dependencies independently[5]. Beyond being a chatbot answering questions, it truly feels like a real 'colleague' actually modifying files, running tests, and even committing[2].

## Claude Code's Core Functionalities: What Problems Does It Solve!

1. **Understand Complex Codebases at a Glance**: When entering new projects or contributing to open source, it typically takes days just to understand vast code[3]. Claude Code draws entire codebase maps and explains core logic in just seconds[5]. You can quickly adapt by asking about code architecture[2][3].
2. **End-to-End Issue Resolution to PR**: It reads GitHub/GitLab issues and writes code across multiple files to solve problems[5]. It then runs tests, self-corrects failures, commits changes, and even generates PRs[2][5]. You just enjoy coffee while supervising the entire process[5].
3. **Automate Refactoring, Documentation, Bug Fixing**: Automate tedious, repetitive work like code refactoring for readability, filling missing comments and documentation, and mysterious bug fixes[3]. Particularly its ability to analyze error messages, identify root causes, and propose solutions dramatically reduces debugging time[3].

## Core Principles and Applications

Claude Code is a flexible tool that doesn't enforce specific workflows[1]. Among these, the most effective and universal workflow is the **'Explore → Plan → Implement → Commit'** pattern[1].

```
# 1. Explore - First read code and understand the situation!
# "Analyze logging.py and related logic. Don't write code yet."
claude "read the file that handles logging, but don't write any code yet."

# 2. Plan - How will you solve it? Let's 'think' about it.
# Using 'think', 'think hard' keywords induces deeper consideration[1].
claude "think hard and make a plan to improve the logging logic."

# 3. Implement - Now write code according to your plan.
claude "implement the solution according to your plan. verify as you go."

# 4. Commit - Create commits and PRs when done!
claude "commit the result and create a pull request. update the README too."
```

Claude Code provides various additional advanced features.

| Feature | Description | Usage Example |
| --- | --- | --- |
| **Screenshot-Based Development** | View design mockups (images) and code UI implementation, take screenshots of results, and iteratively improve by comparison[1]. | `claude "make a webpage like this design mockup."` |
| **Safe YOLO Mode** | Use `--dangerously-skip-permissions` flag to skip permission checks and have Claude execute tasks uninterrupted. (Container environments recommended)[1] | `claude "apply lint rules to all files." --dangerously-skip-permissions` |
| **Headless Mode (`-p`)** | Use `-p` flag to integrate Claude Code into other scripts or pipelines. Useful for large-scale migrations or data processing automation[1]. | `claude -p "migrate foo.py from React to Vue."` |
| **External Tool Integration** | Uses user's bash environment as-is and can integrate with complex tools like Puppeteer through MCP (Multi-Claude Protocol) or REST APIs[1]. | `claude "take a screenshot of the current page with puppeteer."` |

## Precautions and Tips 🎯

⚠️ **Be Careful About These!**

1. **YOLO Mode Requires Caution**: The `--dangerously-skip-permissions` option is very convenient as it skips all permission checks, but can cause unintended data loss or system damage[1]. Use it for low-risk tasks like lint fixing, but ideally run it in isolated environments like internet-blocked Docker containers[1].

💡 **Pro Tips**

- **Leverage "Think" Keywords**: When delegating complex problems, include words like "think", "think hard", "think harder" in your prompt[1]. Claude takes time to more carefully evaluate alternatives and think deeper, resulting in much higher quality plans[1].
- **Iteration is a Virtue**: AI's first output may not be perfect. Especially for visually important tasks like UI coding, iterating 2-3 times with screenshot feedback significantly improves completion quality[1].
- **Teach Your Own Tools**: Claude knows famous tools like `git` and `gh`, but doesn't know custom shell scripts or tools you've created[1]. Telling it the tool name and usage examples, or documenting frequently used tools in your project's `CLAUDE.md` file, helps Claude leverage your tools intelligently[1].

## Conclusion

We've explored Claude Code, the AI colleague working in your terminal. While it may initially feel unfamiliar, it becomes a powerful partner supporting entire development from codebase understanding to PR generation[5]. I hope this article helps elevate your development productivity to the next level!

What tasks do you want to try Claude Code with first? Feel free to share your thoughts in comments! 👩‍💻

## Reference Materials 📚

- [Claude Code Official Documentation](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code GitHub Repository](https://github.com/anthropics/claude-code)

---

#ClaudeCode #AI-Developer #Coding-Automation #Development-Productivity #Anthropic

### Sources

[1] Claude Code: Best Practices for Agentic Coding - Anthropic <https://www.anthropic.com/engineering/claude-code-best-practices>  
[2] Claude Code Overview - Anthropic API <https://docs.anthropic.com/en/docs/claude-code/overview>  
[3] Claude Code: A Guide With Practical Examples - DataCamp <https://www.datacamp.com/tutorial/claude-code>  
[4] Using Claude Code with your Pro or Max Plan | Anthropic Help Center <https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan>  
[5] Claude Code: Deep Coding at Terminal Velocity - Anthropic <https://www.anthropic.com/claude-code>  
[6] How I use Claude AI Projects on a Per-Feature basis to ... - Reddit <https://www.reddit.com/r/ClaudeAI/comments/1eei464/how_i_use_claude_ai_projects_on_a_perfeature/>  
[7] Mastering Claude Code in 30 minutes - YouTube <https://www.youtube.com/watch?v=6eBSHbLKuN0>  
[8] Using Claude Code and Supabase to Create a Hand-Tracking App <https://www.youtube.com/watch?v=TLKxx_-fdio>  
[9] anthropics/claude-code: Claude Code is an Agentic Coding ... - GitHub <https://github.com/anthropics/claude-code>  
[10] Programming programming.ai_tools
