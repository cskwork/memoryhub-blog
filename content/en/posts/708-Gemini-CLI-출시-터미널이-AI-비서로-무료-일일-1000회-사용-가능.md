---
title: "Gemini CLI Launch: Terminal Becomes Your AI Assistant - Free 1000 Daily Requests!"
date: 2025-06-25T22:48:49+09:00
slug: "708-Gemini-CLI-출시-터미널이-AI-비서로-무료-일일-1000회-사용-가능"
original_url: "https://memoryhub.tistory.com/708"
tistory_id: 708
draft: false
---

```
     ╔══════════════════════════════╗
     ║         GEMINI CLI           ║
     ║    ┌─────────────────┐       ║
     ║    │ $ gemini "help" │       ║
     ║    │ > AI has moved  │       ║
     ║    │   to terminal   │       ║
     ║    └─────────────────┘       ║
     ║         🎯 + 🚀 = 💡         ║
     ╚══════════════════════════════╝
```

Until yesterday, if you wanted AI help in the terminal, you had to bounce back and forth between ChatGPT or Claude websites. Today, Google brought a **game changer**. You can now use Gemini 2.5 Pro directly in your terminal for free - and that's **1000 requests per day**!

⚡ **TL;DR**

- Google released Gemini CLI, an open-source AI tool for the terminal
- Free 1000 daily requests, 60 per minute - industry-leading rates

## Table of Contents

1. Background - Why do we need terminal AI?
2. Core Concepts - What is Gemini CLI?
3. Hands-On - Install and use in 5 minutes
4. Best Practices
5. Closing Thoughts & Resources

---

## 1. Background - Why Terminal AI?

For developers, the terminal is home. CLI's efficiency, universality, and portability make it the most-used tool for getting work done. But in the AI era, the terminal was still stuck in the 'analog' age.

Problems we faced before:

- 🔄 Constant switching between browser and terminal when using ChatGPT
- ⏱️ Time wasted on context switching
- 📋 Tedious code copy-pasting

**Related Terminology**

| Term | Definition |
| --- | --- |
| CLI | Command Line Interface |
| LLM | Large Language Model |
| MCP | Model Context Protocol, standard for AI tool extensions |

## 2. Core Concepts - What is Gemini CLI?

> **One-line Definition**  
> Google's open-source AI agent that brings Gemini directly to your terminal

### Key Features

**1. Exceptional Free Tier**

- 60 requests per minute, 1000 daily requests
- 1 million token context window
- Industry-leading compared to competitors

**2. Powerful Capabilities**

- Code understanding, file manipulation, command execution, dynamic problem solving
- Real-time information access through Google Search integration
- Extensible via MCP support
- Currently Claude Code-compatible with some bugs, so not yet sufficient as a pure code generation tool, but helpful for code analysis and understanding
- Expected to become a strong competitor in coming months

**3. Open Source**

- Apache 2.0 License
- Anyone can contribute on GitHub

## 3. Hands-On - Install and Use in 5 Minutes

<https://github.com/google-gemini/gemini-cli>

### ① Installation

```
# Requires Node.js 18+
# Run in terminal
npm install -g @google/gemini-cli
# or
npx https://github.com/google-gemini/gemini-cli

# In the project you want to use
gemini 
# Run the auth command - sign in with your Google account and you're done!
/auth
```

### ② Basic Usage

```
# Ask about codebase architecture
$ gemini "Explain the main architecture of this project"

# Analyze files
$ gemini "Summarize the README.md file"

# Generate code
$ gemini "Create a simple Todo app in React"
```

### ③ Advanced Features

```
# Search latest information with Google Search
$ gemini "Tell me about the latest Next.js 14 features" --search

# Image analysis (multimodal)
$ gemini "Convert this UI design to a React component" design.png

# Script automation
$ gemini "Convert all .js files in this directory to TypeScript"
```

## 4. Best Practices

| Use Case | Benefit | Caution |
| --- | --- | --- |
| Code review requests | Instant feedback | Be careful with sensitive code |
| Debugging helper | Solve right in terminal | Must provide context |
| Auto documentation | Save time | Review before using |

### 💡 Pro Tips

1. **Set up aliases**
2. `# Add to ~/.zshrc or ~/.bashrc: alias ai="gemini"`
3. **Use project-specific configuration**
4. `# Set instructions per project with GEMINI.md echo "This project uses Vue 3" > GEMINI.md`
5. **Integrate with VS Code**

- Shares same technology as Gemini Code Assist
- Seamless switching between terminal and IDE
- Caution! When usage increases, Gemini 2.5 Pro automatically switches to Gemini 2.5 Flash, causing performance degradation. You'll need to manage your limits.

## 5. Closing Thoughts

What we learned today:

- Google is seriously entering the developer tools market
- Using open source + free strategy to capture developer community
- The terminal is now truly a "smart" tool

In real projects, be cautious with sensitive information while actively using it for automating repetitive tasks.

---

### References

- [Google Official Blog - Introducing Gemini CLI](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
- [Gemini CLI GitHub Repository](https://github.com/google-gemini/gemini-cli)
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs/quickstart)

---

### 📚 Glossary

- **Terminal**: The black window where you talk to your computer using text commands
- **AI Agent**: A smart robot friend that does work for you
- **Open Source**: A program anyone can view and modify
- **Token**: A word chunk that AI understands - 1 million tokens = hundreds of books worth
- **API**: How programs talk to each other
