---
title: "? Save 90% on AI Costs with Claude Code Router - You're Missing Out if You Don't Know This!"
date: 2025-07-18T03:12:46+09:00
slug: "729-Claude-Code-Router로-AI-비용-90-절약-이-방법-몰랐다면-손해"
original_url: "https://memoryhub.tistory.com/729"
tistory_id: 729
draft: false
---

```
    ? Claude Code Router ?
         /     |     \
    OpenAI  DeepSeek  Gemini
       |       |       |
    [$$$]   [$$]    [$$$$]
       |       |       |
    Your Choice Based on Task
```

Have you ever been hit with a Claude API bill surprise? I was shocked when I saw tens of thousands of won coming out each month, but then I discovered a clever tool called Claude Code Router.

The fact that you can route the same task to DeepSeek and **save over 90% on costs** is a total game-changer. Especially if you have a lot of long code work or repetitive tasks, it's essential to know about this tool.

⚡ **TL;DR**: A router tool that automatically distributes Claude Code requests across multiple AI models for cost savings plus performance optimization. Set it once and automatically select the optimal model for each situation!

## Table of Contents

1. Background - Why is AI model routing necessary?
2. Core concepts explained - What is Claude Code Router?
3. Hands-on - From installation to setup
4. Best practices - Smart routing strategies
5. Conclusion & References

---

## 1. Background - Why Is AI Model Routing Necessary?

When you develop with AI, you run into these issues:

**Cost problems**: Premium models like Claude Max have great performance but expensive token costs, so even simple tasks end up costing too much.

**Task characteristics**: Code reviews need accuracy, brainstorming needs creativity, and debugging needs logical reasoning.

**Context limits**: Different models have different token lengths they can handle when dealing with long code or documents.

✅ **Key Terminology**

- **Routing**: The process of automatically distributing requests to appropriate models
- **Provider**: AI model providers like OpenAI, DeepSeek, Gemini, etc.
- **Transformer**: Functionality that converts requests/responses to match each API format

## 2. Core Concepts Explained

> **Claude Code Router**: A powerful tool for routing Claude Code requests across various models and customizing them

Users can define routing strategies directly to precisely configure which requests go to which models. For example, you can branch to use a lightweight model for background processing, DeepSeek Reasoner for advanced reasoning, and Gemini 2.5 Pro for long context handling.

**Key features**:

- Model routing: Route requests to different models as needed (background tasks, thinking, long context, etc.)
- Multi-provider support: Support for various model providers including OpenRouter, DeepSeek, Ollama, Gemini, Volcengine, SiliconFlow, and more
- Dynamic model switching: Use the /model command to switch models in real-time within Claude Code

## 3. Hands-on - From Installation to Setup

### ① Basic Installation

First, you need to have Claude Code CLI installed:

```
# Install Claude Code CLI
npm install -g @anthropic-ai/claude-code

# Install Claude Code Router  
npm install -g @musistudio/claude-code-router
```

### ② Creating Configuration File

Create and configure the `~/.claude-code-router/config.json` file:

```
{
  "APIKEY": "your-secret-key",
  "LOG": true,
  "Providers": [
    {
      "name": "deepseek",
      "api_base_url": "https://api.deepseek.com/chat/completions",
      "api_key": "sk-xxx",
      "models": ["deepseek-chat", "deepseek-reasoner"]
    },
    {
      "name": "openrouter", 
      "api_base_url": "https://openrouter.ai/api/v1/chat/completions",
      "api_key": "sk-xxx",
      "models": ["anthropic/claude-3.5-sonnet", "google/gemini-2.5-pro"]
    }
  ],
  "Router": {
    "default": "deepseek,deepseek-chat",
    "background": "deepseek,deepseek-chat", 
    "think": "deepseek,deepseek-reasoner",
    "longContext": "openrouter,google/gemini-2.5-pro"
  }
}
```

### ③ Running the Router

```
# Start the router
ccr code

# Or set environment variables and then
export ANTHROPIC_BASE_URL="http://127.0.0.1:3456"
export ANTHROPIC_AUTH_TOKEN="test"
claude
```

Now when you use Claude Code normally, requests are automatically distributed to the appropriate models according to the routing rules you configured!

## 4. Best Practices - Smart Routing Strategies

| Task Type | Recommended Model | Reason |
| --- | --- | --- |
| General coding | DeepSeek Chat | Cost-effective with excellent coding performance |
| Complex reasoning | DeepSeek Reasoner | Specialized for reasoning tasks |
| Long context | Gemini 2.5 Pro | Can handle 128K context for long documents |
| Background tasks | Qwen2.5-Coder | Fast and free locally |

**Real-time model switching** is also possible:

```
# Change model while Claude Code is running
/model openrouter,anthropic/claude-3.5-sonnet
/model deepseek,deepseek-reasoner
```

**Cost optimization tips**:

- Simple tasks: DeepSeek Chat (lowest token cost)
- Creative work: Claude 3.5 Sonnet
- Analysis work: Gemini Pro (supports long context)

## 5. Conclusion

With Claude Code Router, I found that **automatically selecting models matching task characteristics** saves costs while improving performance. The most impressive part is being able to perform complex AI tasks with DeepSeek integration at a much lower cost compared to premium models.

If your development team is worried about AI tool costs, definitely give this a try. The flexibility you get from just one JSON configuration is truly innovative.

**Tips for real-world projects**: Standardize and share configurations across your entire team so all developers can benefit from the same cost efficiency.

⸻

## References

- **Official GitHub**: [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router)
- **Claude Code Official Documentation**: [Anthropic Claude Code Overview](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview)

---

## ? Technical Glossary (Easy Enough for Kids to Understand!)

**Router**: Like a mail carrier who receives letters and decides which house to deliver them to. Here it's a program that decides which model to send AI requests to

**API**: How programs talk to each other. Like a translator between friends who speak different languages

**Token**: The unit AI uses to count characters. For Korean, typically 1 character is about 1-2 tokens

**Provider**: Companies that create AI models and rent them out. Examples include OpenAI, DeepSeek, and Google

**Context**: The amount of information an AI can remember at one time. Just like it's hard for people to remember too much at once
