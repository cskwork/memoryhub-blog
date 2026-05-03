---
title: "Anthropic SDK vs Agent SDK: Your Choice Determines Project Success"
date: 2025-12-28T11:56:44+09:00
slug: "949-Anthropic-SDK-vs-Agent-SDK-당신의-선택이-프로젝트-성패를-가른다"
original_url: "https://memoryhub.tistory.com/949"
tistory_id: 949
draft: false
---

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     @anthropic-ai/sdk        @anthropic-ai/claude-agent   ║
    ║    ┌─────────────────┐       ┌─────────────────────────┐  ║
    ║    │  Low-Level API  │       │   High-Level Framework  │  ║
    ║    │ ═══════════════ │       │ ═══════════════════════ │  ║
    ║    │ • Thinking ✓    │       │ • Auto Tool Loop ✓      │  ║
    ║    │ • Full Stream ✓ │       │ • State Mgmt ✓          │  ║
    ║    │ • Manual Loop   │       │ • Retry Logic ✓         │  ║
    ║    └────────┬────────┘       └────────────┬────────────┘  ║
    ║             │                             │               ║
    ║             └──────────┬──────────────────┘               ║
    ║                        ▼                                  ║
    ║              [ Your AI Agent Project ]                    ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
```

Have you ever opened npm to build an AI agent with Claude, only to freeze at the sight of two packages: @anthropic-ai/sdk and @anthropic-ai/claude-agent-sdk? If you thought "Agent in the name means it's better," that assumption could cost you a few sleepless nights.

**These two SDKs aren't a superior/inferior relationship—they're tools designed for different purposes.** After reading this, you'll be able to choose the right SDK for your project requirements in under 5 minutes.

**One-line summary:** If you need to display thinking or fine-grained streaming control, go with Direct SDK. For rapid AI agent development with tools, use Agent SDK. For complex projects, combine both.

---

## Background

AI agent development with Claude is exploding. In 2025, Anthropic rebranded the Claude Code SDK as the Claude Agent SDK, formally expanding the agent development ecosystem. The problem is that developers are confused between the existing Direct SDK (which communicates directly with the Messages API) and the new Agent SDK.

> **Core concept:** Direct SDK is a low-level client that communicates 1:1 with the Claude API, while Agent SDK is a high-level framework built on top of it, adding tool execution loops, state management, and retry logic.

The relationship between the two SDKs is like this: Direct SDK is a manual transmission car, while Agent SDK is an automatic transmission car. Manual transmission gives drivers control over every gear shift, enabling fine-tuned manipulation but requiring time to master. Automatic transmission handles shifts for you, letting you focus on driving, but specific scenarios may resist your control.

---

## Understanding the Architecture Difference

The most fundamental difference between Direct SDK and Agent SDK is what sits between your code and Claude.

**Direct SDK flow:**

```
Application Code ←→ Anthropic Messages API ←→ Claude Model
       ↑
       └── Developer handles everything: tool loops, state, streaming
```

**Agent SDK flow:**

```
Application Code ←→ Agent SDK ←→ Anthropic Messages API ←→ Claude Model
                        ↑
                        └── SDK handles: tool routing, conversation loops, retries
```

Agent SDK is built on the same infrastructure powering Claude Code. According to Anthropic's official documentation, Agent SDK supports building agents that can autonomously perform file reading/writing, command execution, web search, code editing, and more.

---

## Feature Comparison Analysis

Comparing the SDKs by core functionality makes the selection criteria clear.

| Feature | Direct SDK | Agent SDK |
| --- | --- | --- |
| Extended Thinking Streaming | Full Access | No Access |
| Extended Thinking Final Result | Full Access | No Access |
| Tool Call Processing | Manual Loop Required | Auto Handled |
| Multi-turn Tool Conversation | Manual State Mgmt | Auto Managed |
| Streaming Text Response | Full Control | Abstracted |
| Token Counting | Direct Access | Abstracted |
| Error Handling & Retry | Manual Implementation | Built-in |
| MCP Server Integration | Manual Implementation | Built-in Support |

**Most Critical Difference:** Agent SDK cannot access Extended Thinking blocks—Claude's internal reasoning process. This isn't a bug but intentional design. Agent SDK prioritizes workflow simplicity and focuses on execution efficiency over exposing the model's internal reasoning.

---

## When to Choose Direct SDK

### 1. When You Need to Show the Reasoning Process to Users

If you want to show Claude's thinking in real-time like the "View thinking" feature in Claude.ai, Direct SDK is your only choice.

```
// Direct SDK - directly receive thinking_delta events
const stream = client.messages.stream({
  model: "claude-sonnet-4-5-20250929",
  max_tokens: 16000,
  thinking: {
    type: "enabled",
    budget_tokens: 10000
  },
  messages: [{ role: "user", content: "Analyze this complex problem..." }]
});

for await (const event of stream) {
  if (event.type === "content_block_delta") {
    if (event.delta.type === "thinking_delta") {
      // Display reasoning process to UI in real-time
      emitToClient("thinking", event.delta.thinking);
    } else if (event.delta.type === "text_delta") {
      emitToClient("response", event.delta.text);
    }
  }
}
```

According to Anthropic's official documentation, enabling Extended Thinking allows you to receive reasoning content in real-time via thinking_delta events. In Claude Opus 4.5, thinking blocks from previous assistant turns are preserved in the model context by default.

### 2. When Fine-Grained Streaming Control is Required

If you need to apply custom buffering or transformations to streaming chunks, Direct SDK's granular event access is essential.

### 3. Simple Conversational Apps Without Tools

For simple interactions like Q&A, text generation, or analysis without tool usage, Agent SDK's overhead is unnecessary.

### 4. When Token Costs Must Be Managed Precisely

If you need to check input_tokens, output_tokens, and cache-related tokens per API call and optimize costs, Direct SDK provides more transparent access.

---

## When to Choose Agent SDK

### 1. Building Standard Agent Workflows

If you're building a typical agent that needs to loop until it completes work using tools (file read/write, web search, code execution, etc.), Agent SDK is appropriate.

```
// Agent SDK - automatically handles the entire loop
const agent = new Agent({
  model: "claude-sonnet-4-5-20250929",
  tools: [readFileTool, writeFileTool, searchTool],
});

const result = await agent.run({
  messages: [{ role: "user", content: "Find and fix the bug in src/main.ts" }]
});

// Work that Agent SDK automatically performs:
// 1. Call Claude
// 2. Detect tool_use blocks
// 3. Execute tools
// 4. Return results to Claude
// 5. Repeat until final answer
```

### 2. Rapid Prototyping

If you want to focus on business logic rather than infrastructure, Agent SDK significantly reduces boilerplate. According to Anthropic's engineering blog, Agent SDK is designed to quickly build various agent types: financial agents, personal assistant agents, customer support agents, and more.

### 3. Long-Running Agent Sessions

For extended conversations spanning multiple turns with numerous tool calls, Agent SDK's conversation state management dramatically reduces complexity.

### 4. Production Stability Priority

If you need built-in error handling, retry logic, and handling of API errors and rate limits, Agent SDK already encapsulates best practices.

---

## Practice: Implementing a Hybrid Approach

For complex applications, using both SDKs together may be optimal. Consider a scenario where you need to show the reasoning process to users while performing tool-based tasks.

### ① Project Structure Design

```
src/
├── agents/
│   ├── thinking-agent.ts   // Uses Direct SDK
│   └── tool-agent.ts       // Uses Agent SDK
├── router.ts               // Route by request type
└── index.ts
```

### ② Router Implementation

```
// router.ts
async function handleRequest(request: Request) {
  // Analysis tasks requiring thinking display
  if (request.needsThinkingDisplay) {
    return analyzeWithThinking(request.query);
  }

  // Agent tasks requiring tools
  if (request.needsTools) {
    return executeAgentTask(request.query);
  }

  // Simple questions
  return simpleQuery(request.query);
}
```

### ③ Implement Each Agent

Implement the thinking display agent with Direct SDK and the tool execution agent with Agent SDK. This way, you leverage the strengths of both SDKs.

---

## Decision Flowchart

A simple question flow is faster than complex comparison tables.

```
Start
  │
  ▼
Must show Claude's reasoning process to users?
  │
  ├── Yes → Choose Direct SDK
  │
  └── No
       │
       ▼
     Must Claude use tools?
       │
       ├── No → Choose Direct SDK (better for simple conversations)
       │
       └── Yes
            │
            ▼
          Need custom tool orchestration?
          (parallel execution, conditional branching, etc.)
            │
            ├── Yes → Choose Direct SDK
            │
            └── No
                 │
                 ▼
               Is rapid development more important than fine control?
                 │
                 ├── Yes → Choose Agent SDK
                 │
                 └── No → Choose Direct SDK
```

---

## Best Practices Comparison

| Scenario | Recommended SDK | Key Reason |
| --- | --- | --- |
| Display reasoning to users | Direct SDK | Agent SDK cannot access thinking blocks |
| Simple chatbot without tools | Direct SDK | No unnecessary overhead |
| Tool-based agent, rapid development | Agent SDK | Automated loops accelerate development |
| Tool-based agent, full control | Direct SDK | Custom orchestration possible |
| Production agent, stability priority | Agent SDK | Built-in error handling and retries |
| Token cost optimization | Direct SDK | Direct access to usage metrics |
| Need both reasoning + tools | Hybrid | Route by task type |

---

## Conclusion

- **These two SDKs aren't interchangeable.** Direct SDK offers low-level control and Extended Thinking access, while Agent SDK provides automated agent workflows.
- **Selection criteria are simple.** Need thinking display or fine-grained streaming control? Use Direct SDK. Need tool loop automation? Use Agent SDK.
- **For complex projects, combine them.** A hybrid approach leverages the strengths of both SDKs.

**Practical tip:** Right now, summarize your project's three core requirements and follow the decision flowchart. You'll have an answer in 5 minutes.

---

## References

- Agent SDK overview - Claude Docs (https://platform.claude.com/docs/en/agent-sdk/overview)
- Building agents with the Claude Agent SDK - Anthropic Engineering (https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)
- Building with extended thinking - Claude Docs (https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking)
- Claude Agent SDK TypeScript - GitHub (https://github.com/anthropics/claude-agent-sdk-typescript)
- Claude Sonnet 4.5 Announcement - Anthropic (https://www.anthropic.com/news/claude-sonnet-4-5)
