---
title: "Gemini CLI v0.7.0: Three Killer Features Developers are Watching"
date: 2025-10-03T08:58:38+09:00
slug: "822-Gemini-CLI-v0-7-0-개발자들이-주목하는-세-가지-킬러-기능"
original_url: "https://memoryhub.tistory.com/822"
tistory_id: 822
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
---

```
    ____                _       _    ____ _     ___   
   / ___| ___ _ __ ___ (_)_ __ (_)  / ___| |   |_ _|  
  | |  _ / _ \ '_ ` _ \| | '_ \| | | |   | |    | |   
  | |_| |  __/ | | | | | | | | | | | |___| |___ | |   
   \____|\___|_| |_| |_|_|_| |_|_|  \____|_____|___|  

         v0.7.0 - AI Innovation Meets Terminal
```

On October 1, 2025, Gemini CLI v0.7.0's official release has the developer community buzzing. I immediately tested it after hearing the news, and honestly, this update was no simple feature addition.

Imagine generating images directly in the terminal, TODO lists automatically managed, custom commands linked like scripts? Five minutes after reading this article, your development workflow will be completely different.

---

## 1. Background: Why Gemini CLI is Getting Attention

Gemini CLI is an open-source AI agent released by Google, allowing you to use the Gemini 2.5 Pro model directly from the terminal. With your personal Google account, you get 60 requests per minute and up to 1,000 per day free—powerful AI capabilities without economic burden.

**Key Terminology**

|  |  |
| --- | --- |
| MCP (Model Context Protocol) | Standard protocol for AI agents to communicate with external tools |
| Extension | Packaged extension functionality combining context files, MCP servers, and custom commands |
| Headless Mode | Running CLI non-interactively for automation and CI/CD |

Previously focused on coding, v0.7.0 expanded to image generation, task management, and workflow automation.

---

## 2. Core Features Explained

> **One-Line Definition**  
> **Gemini CLI v0.7.0 is an integrated development environment enabling image generation, automatic TODO management, and custom command chaining in the terminal.**

### 2-1. Nano Banana Extension: Generate Images in Terminal

Nano Banana is an alias for Gemini 2.5 Flash Image model, specialized in image generation and editing. Upload one photo and combine multiple images or edit specific parts with precision.

**Installation**

```
gemini extensions install https://github.com/gemini-cli-extensions/nanobanana
```

After installation, use `/generate` to create images or `/edit` to modify existing images. Like examples in documentation, you can add backgrounds to profile photos or change styles with a single command.

All generated images automatically include SynthID watermark, clearly marking them as AI-generated.

### 2-2. TODO Management (Experimental Feature)

When handling complex tasks, Gemini CLI automatically generates TODO lists and checks progress. Currently experimental, disabled by default.

**Activation Method**

Add the following to `settings.json`:

```
{
  "useWriteTodos": true
}
```

This feature clarifies each step in multi-step work, displaying completed and ongoing items in real-time. Future updates plan improvements like color or symbol status distinction, or showing only surrounding items.

### 2-3. Run Custom Commands in Headless Mode

Custom slash commands can be called in non-interactive (Headless) mode, enabling integration of Gemini CLI into CI/CD pipelines and automation scripts.

**Custom Command Chaining Example**

```
# ~/.gemini/commands/find-capital.toml
prompt="Please provide the capital city of {{args}}."

# ~/.gemini/commands/things-to-do.toml
prompt="Please provide fun things to do in the city of {{args}}."
```

```
gemini "/things-to-do $(gemini "/find-capital Estonia")"
```

This way you can use one command's output as the next command's input for complex workflows. Applicable to travel planning, data analysis, code review automation, and more.

---

## 3. Real-World Usage Scenarios

### ① Install Extension and Edit Images

[Details on practical implementation...]

---

## Conclusion

Gemini CLI v0.7.0 represents a significant leap in terminal-based AI tooling. The combination of image generation, task management, and command automation creates a more cohesive development experience.

The key value isn't just individual features but how they work together to reduce friction in your workflow.

---

## References

- [Gemini CLI Official Documentation](https://github.com/google-gemini/cli)
- [Nano Banana Extension Guide](https://github.com/gemini-cli-extensions/nanobanana)
- [MCP Integration with Gemini](https://docs.google.com/gemini/mcp)
