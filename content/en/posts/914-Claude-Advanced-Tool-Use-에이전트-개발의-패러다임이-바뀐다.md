---
title: "Claude Advanced Tool Use: Agent Development Paradigm Shifts"
date: 2025-11-25T20:31:02+09:00
slug: "914-Claude-Advanced-Tool-Use-에이전트-개발의-패러다임이-바뀐다"
original_url: "https://memoryhub.tistory.com/914"
tistory_id: 914
draft: false
---

```
    ┌─────────────────────────────────────────────────────────┐
    │  CLAUDE ADVANCED TOOL USE                               │
    │  ════════════════════════                               │
    │                                                         │
    │   ┌──────┐    ┌──────┐    ┌──────┐                     │
    │   │ Tool │───▶│Search│───▶│ Load │  (On-Demand)        │
    │   │  1   │    │  ?  │    │ Tool │                     │
    │   └──────┘    └──────┘    └──────┘                     │
    │                                                         │
    │   ┌─────────────────────────────────────────┐          │
    │   │  CODE EXECUTION SANDBOX                 │          │
    │   │  ┌────┐ ┌────┐ ┌────┐ ┌────┐          │          │
    │   │  │API1│ │API2│ │API3│ │API4│ ─▶ Result│          │
    │   │  └────┘ └────┘ └────┘ └────┘          │          │
    │   └─────────────────────────────────────────┘          │
    │                                                         │
    │   85% Token Saved  │  37% Cost Reduced                 │
    └─────────────────────────────────────────────────────────┘
```

Connected 50 tools and already burned 70,000 tokens before starting the conversation. Sound familiar? Ever pushed your context window to the brink by connecting multiple MCP servers? Anthropic solved this problem head-on.

**Three new beta features shift tools from 'pre-memorizing' to 'finding when needed.'**

**One-line summary:** With three beta features—Tool Search Tool, Programmatic Tool Calling, Tool Use Examples—Claude can now use thousands of tools accurately without token waste.

## Background

The future of AI agents is handling hundreds, even thousands of tools simultaneously. Think of an IDE assistant integrating git, file management, package manager, testing framework, deployment pipeline. Or an operations coordinator connecting Slack, GitHub, Google Drive, Jira, internal database, dozens of MCP servers all at once.

The problem with the old approach was clear. Just connecting 5 servers consumes around 55,000 tokens for tool definitions alone. GitHub's 35 tools consume 26K, Slack's 11 tools 21K, add Jira and you're over 100K tokens. Anthropic internally saw cases where tool definitions alone consumed 134K tokens.

Token cost isn't the only problem. The most common failure cause is wrong tool choice and inaccurate parameters. With many similar-named tools like `notification-send-user` and `notification-send-channel`, confusion multiplies.

| Problem Type | Old Approach Limitation |
| --- | --- |
| Context Pollution | All intermediate results stack in context |
| Token Waste | Unused tool definitions pre-loaded too |
| Accuracy Degradation | Confusion between similar tool names |
| Latency | Reasoning pass needed for each tool call |

## Core Concept

> Claude dynamically discovers tools, executes them via code, and learns from examples—three new beta features.

### Tool Search Tool: Finding Tools Like a Librarian

Which is more efficient—stacking all books on a desk and searching yourself, or asking a librarian? Tool Search Tool takes the latter approach. Instead of pre-loading all tool definitions, Claude **searches for needed tools on-demand**.

How it works is simple. Set `defer_loading: true` on tool definition and that tool won't load into initial context. When Claude needs specific functionality, Tool Search Tool searches and only matching tools get added to context.

Internal test results are impressive. **Opus 4 accuracy improved from 49% to 74%, Opus 4.5 from 79.5% to 88.1%**. Token usage dropped about 85% from 77K to 8.7K.

```
# Tool definition example
{
  "tools": [
    {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
    {
      "name": "github.createPullRequest",
      "description": "Create a pull request",
      "input_schema": {...},
      "defer_loading": true  # Set as on-demand search target
    }
  ]
}
```

### Programmatic Tool Calling: Chef Handling Ingredients Directly

Imagine a restaurant where the chef gets each ingredient one by one from a waiter. Inefficient. Programmatic Tool Calling lets Claude **directly orchestrate multiple tools through code**.

For example, handling "Who exceeded travel budget in Q3?" Query-wise, the old way would fetch 20 team members, then pull each person's cost history, then verify budget limits—with 2,000+ expense items stacking in context.

With Programmatic Tool Calling, Claude writes a Python script handling the entire workflow. Intermediate results are processed in the code environment, **only final results return to Claude's context**. 200KB of raw data compresses to 1KB result.

Performance improvements are clear. Token usage dropped average 43,588 to 27,297 (37% decrease), knowledge search accuracy improved 25.6% to 28.5%, GIA benchmark 46.5% to 51.2%.

### Tool Use Examples: A Picture's Worth a Thousand Words

JSON Schema defines what's structurally valid but doesn't express usage patterns. Is `due_date` "2024-11-06" or "Nov 6, 2024"? Is `reporter.id` a UUID or "USR-12345" format? You can't tell from schema alone.

Tool Use Examples **includes concrete usage examples directly in tool definitions**. Claude learns date formats, ID conventions, optional parameter combination patterns from these examples.

```
"input_examples": [
  {
    "title": "Login page returns 500 error",
    "priority": "critical",
    "labels": ["bug", "authentication", "production"],
    "due_date": "2024-11-06"  # Learn date format
  },
  {
    "title": "Add dark mode support",
    "labels": ["feature-request", "ui"]  # Feature requests simpler
  }
]
```

Internal tests showed complex parameter handling accuracy improved **from 72% to 90%**.

## Hands-On Practice

① **Add Beta Header**

All three features are in beta, so include beta header in API calls.

```
client.beta.messages.create(
    betas=["advanced-tool-use-2025-11-20"],
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    tools=[...]
)
```

② **Set Up Tool Search Tool**

If tool definitions exceed 10K tokens or use 10+ tools, consider Tool Search Tool. Keep 3-5 frequently-used tools as `defer_loading: false`, rest as `defer_loading: true`.

③ **Apply Programmatic Tool Calling**

Set `allowed_callers` on tools where parallel execution is possible or intermediate results aren't needed for final response. Especially effective for large data aggregation, multi-step workflows.

④ **Write Tool Use Examples**

Add 1-5 realistic examples for tools with complex nested structures or domain-specific conventions. Use actual data instead of placeholders like "string" or "value".

## Best Practices / Pattern Comparison

| Feature | Best For | Not For |
| --- | --- | --- |
| Tool Search Tool | Tool definitions 10K+ tokens, 10+ tools, MCP multi-server | Small tool library, all tools used every session |
| Programmatic Tool Calling | Large data aggregation, 3+ sequential tool calls, parallel processing | Simple single tool call, need to see intermediate results |
| Tool Use Examples | Complex nested structures, domain-specific conventions, distinguish similar tools | Simple single parameter, standard formats like URL/email |

## Closing Remarks

- Claude's tool usage evolved from "pre-load everything" to "search when needed."
- Tool Search Tool saves 85% tokens, Programmatic Tool Calling saves additional 37%.
- Practical tip: Measure your current agent's tool definition tokens. If over 10K, consider Tool Search Tool adoption.

## References

- Introducing advanced tool use on the Claude Developer Platform (<https://www.anthropic.com/news/advanced-tool-use>)
- Claude API Documentation (<https://docs.anthropic.com>)
