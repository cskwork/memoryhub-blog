---
title: "🤖 Claude Code - An AI Colleague Developer Working in Your Terminal"
date: 2025-06-07T23:48:22+09:00
slug: "672-클로드-코드-Claude-Code-터미널에서-일하는-AI-동료-개발자"
original_url: "https://memoryhub.tistory.com/672"
tistory_id: 672
draft: false
---

You seem to have a lot of interest in AI tools and their practical applications[10].

Haven't you experienced the fatigue of constantly switching between your IDE, terminal, and browser while coding? You might have imagined what it would be like to have a junior developer colleague who understands your entire project and efficiently handles the tedious work. Anthropic's 'Claude Code' that I'll introduce today is exactly that kind of tool[2].

Claude Code is an AI coding agent that resides in your terminal[2][9]. You can delegate complex coding tasks with just natural language commands[4]. From now on, I'll explain everything about Claude Code in an easy and detailed way.

## Background

Past AI coding assistants mostly came in the form of separate chat windows. Developers had to copy and paste parts of their current code and explain the context one by one to get help. This interrupted the development flow and made it difficult to explain the entire project structure.

However, Claude Code integrates directly into the 'terminal,' the heart of the development environment[2][3]. As a result, developers don't have to specify files one by one; through a technology called 'agentic search,' Claude Code can understand the entire project structure and dependencies on its own[5]. This is why it feels like a real 'colleague' that goes beyond simply answering questions in a chatbot, actually modifying files, running tests, and even making commits[2].

## Core Features of Claude Code: Here's What Problems It Solves!

1. **Understand complex codebases at a glance**: When joining a new project or contributing to open source, it often takes days just to understand vast amounts of code[3]. Claude Code draws a complete map of the entire codebase and explains the core logic in just seconds[5]. You can quickly adapt by asking about code architecture[2][3].

2. **Everything from issue resolution to PR in one go**: It reads GitHub and GitLab issues and writes the necessary code to solve problems across multiple files[5]. Then it runs tests, self-corrects if failures occur, and finally commits changes and can even create a Pull Request[2][5]. Developers can simply supervise the entire process over a cup of coffee[5].

3. **Automate refactoring, documentation, and bug fixes**: It automates tedious and repetitive tasks like refactoring for improved code readability, filling in missing comments or documentation, and fixing mysterious bugs[3]. In particular, its ability to analyze error messages, find root causes, and suggest solutions dramatically reduces debugging time[3].

## Core Principles and Usage

Claude Code is a flexible tool that doesn't enforce a fixed workflow[1].

Among them, the most effective and common usage pattern is the **'Explore → Plan → Implement → Commit'** workflow[1].

```
# 1. Explore - First read the code and understand the situation!
# "Analyze the logic related to the logging.py file. Don't write any code yet."
claude "read the file that handles logging, but don't write any code yet."

# 2. Plan - 'Think' about how to solve it.
# You can use 'think' and 'think hard' keywords to induce deeper consideration[1].
claude "think hard and make a plan to improve the logging logic."

# 3. Code - Now write the code according to your plan.
claude "implement the solution according to your plan. verify as you go."

# 4. Commit - When done, commit and create a PR!
claude "commit the result and create a pull request. update the README too."
```

In addition, Claude Code provides various advanced features.

| Feature | Description | Usage Example |
| --- | --- | --- |
| **Screenshot-based Development** | View design mockups (images) and implement UI in code, take screenshots of the results, and iteratively improve through comparison[1]. | `claude "build this webpage according to this design mockup."` |
| **Safe YOLO Mode** | Use the `--dangerously-skip-permissions` flag to skip permission checks and perform tasks like fixing lint errors or generating boilerplate without interruption. (Container environments recommended)[1] | `claude "apply lint rules to all files." --dangerously-skip-permissions` |
| **Headless Mode (`-p`)** | Use the `-p` flag to integrate Claude Code into other scripts or pipelines. Useful for large-scale migrations or data processing automation[1]. | `claude -p "migrate foo.py from React to Vue."` |
| **External Tool Integration** | Uses your bash environment as-is and can integrate with complex tools like Puppeteer through MCP (Multi-Claude Protocol) or REST API[1]. | `claude "take a screenshot of the current page with puppeteer."` |

## Cautions and Tips 💡

⚠️ **Please Pay Attention to These!**

1. **Use YOLO mode carefully**: The `--dangerously-skip-permissions` option skips all permission checks, which is very convenient, but it can cause unintended data loss or system damage[1]. Use it for low-risk tasks like lint fixes, but ideally run it in isolated environments like Docker containers with internet access disabled[1].

💡 **Pro Tips**

- **Use the "Think" keyword**: When assigning complex problems, include words like "think", "think hard", or "think harder" in your prompt[1]. This gives Claude time to evaluate alternatives more carefully and think deeply, resulting in much higher quality planning[1].
- **Repetition is a virtue**: The first output from AI may not be perfect. Especially for visually important tasks like UI coding, repeating the revision 2-3 times with screenshot feedback significantly improves the quality of the results[1].
- **Teach Claude about your tools**: Claude knows well-known tools like `git` and `gh`, but doesn't know custom shell scripts or tools you created yourself[1]. Tell Claude the name and usage examples of your tools, or document frequently used tools in a `CLAUDE.md` file in your project, and Claude can smartly utilize your tools[1].

## Conclusion

We've explored Claude Code, an AI colleague developer working in your terminal. At first it may feel unfamiliar, but it can become a powerful partner that helps throughout the entire development process, from understanding the codebase to creating PRs[5]. I hope this article has helped raise your development productivity to the next level!

How would you like to use Claude Code first? Feel free to share your thoughts in the comments! 👩‍💻

## References 📚

- [Claude Code Official Documentation](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code GitHub Repository](https://github.com/anthropics/claude-code)

**Sources**  
[1] Claude Code: Best practices for agentic coding - Anthropic <https://www.anthropic.com/engineering/claude-code-best-practices>  
[2] Claude Code overview - Anthropic API <https://docs.anthropic.com/en/docs/claude-code/overview>  
[3] Claude Code: A Guide With Practical Examples - DataCamp <https://www.datacamp.com/tutorial/claude-code>  
[4] Using Claude Code with your Pro or Max Plan | Anthropic Help Center <https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan>  
[5] Claude Code: Deep Coding at Terminal Velocity \ Anthropic <https://www.anthropic.com/claude-code>  
[6] How I use Claude AI Projects on a Per-Feature basis to ... - Reddit <https://www.reddit.com/r/ClaudeAI/comments/1eei464/how_i_use_claude_ai_projects_on_a_perfeature/>  
[7] Mastering Claude Code in 30 minutes - YouTube <https://www.youtube.com/watch?v=6eBSHbLKuN0>  
[8] Using Claude Code and Supabase to Create a Hand-Tracking App <https://www.youtube.com/watch?v=TLKxx_-fdio>  
[9] anthropics/claude-code: Claude Code is an agentic coding ... - GitHub <https://github.com/anthropics/claude-code>  
[10] Programming programming.ai\_tools

#ClaudeCode #AIDeveloper #CodingAutomation #DevelopmentProductivity #Anthropic
