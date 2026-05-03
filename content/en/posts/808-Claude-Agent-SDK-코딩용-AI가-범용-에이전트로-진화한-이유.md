---
title: "Claude Agent SDK: Why AI Evolved from a Coding Tool to a General-Purpose Agent"
date: 2025-09-30T20:49:02+09:00
slug: "808-Claude-Agent-SDK-코딩용-AI가-범용-에이전트로-진화한-이유"
original_url: "https://memoryhub.tistory.com/808"
tistory_id: 808
draft: false
---

```
    _______________
   /               \
  /   CLAUDE SDK    \
 /    ___________    \
|    |  ?  ?  |    |
|    |___________|    |
|                     |
|  [Computer Access]  |
|  ↓  ↓  ↓  ↓  ↓     |
|  Files Terminal API |
 \___________________/
        Agent
```

Have you ever used an AI coding tool and thought, "I wish I could use this for other tasks too"? The Claude Agent SDK released by Anthropic on September 29, 2025, is exactly the answer to that question. By expanding the underlying technology of Claude Code into a general-purpose agent development platform, it's now possible to build agents that can automate not just coding, but also research, customer support, and financial analysis. After reading this article, you'll clearly understand **why this SDK is gaining attention and how to get started**.

---

## 1. Background: From Claude Code to Claude Agent SDK

### Existing Challenges

Traditional AI agents were either optimized for specific tasks or lost context during complex multi-step operations. Anthropic initially created Claude Code for internal developer productivity, but soon discovered it was effective for non-coding work like deep research, video production, and note-taking.

### Core Design Principle

The key design principle is this: if you give Claude the tools that programmers use daily (file search, editing, code execution, debugging), it acts like a real programmer. By providing computer access through the terminal, it became possible to perform general digital tasks like reading CSV files, web searching, creating visualizations, and interpreting metrics.

### Key Terminology

| Term | Definition |
| --- | --- |
| **Agent Loop** | Feedback cycle of context gathering → task execution → verification → iteration |
| **Subagent** | Independent sub-agents for parallel processing and context isolation |
| **MCP (Model Context Protocol)** | Standardized integration with external services like Slack, GitHub, Drive |
| **Agentic Search** | Dynamic information search using commands like grep/find without RAG |

---

## 2. Core: How AI Uses Computers

> **Claude Agent SDK completes an autonomous feedback loop of context gathering, execution, and verification through the simple but powerful philosophy of 'giving the agent a computer'.**

Using the SDK, you can build financial agents (portfolio analysis, investment evaluation), personal assistants (travel booking, schedule management), customer support agents (ticket handling, data collection), and deep research agents (large-scale document analysis, report generation).

### Agent Loop: 3 Steps

**① Gather Context**

- Use the file system as context (folder/file structure = context engineering)
- Parallel search with Subagents, then pass only key information to the orchestrator
- Auto-summarization via Compaction when reaching context limits

**② Take Action**

- Define custom tools (fetchInbox, searchEmails, etc.)
- Flexible tasks via Bash scripts (PDF conversion, text search, etc.)
- Auto-integration with external services like Slack, Asana via MCP (no OAuth management needed)

**③ Verify Work**

- Rule-based feedback (TypeScript linting > JavaScript)
- Visual feedback (screenshots for UI layout and style verification)
- LLM as Judge (separate sub-agent evaluates tone and quality)

---

## 3. Tutorial: Building an Email Agent Example

Claude Agent SDK is provided in Python and supports everything from simple queries to bidirectional conversations. Below is a minimal example based on official documentation.

### ① Installation

```
pip install claude-agent-sdk
```

### ② Basic Query Example

```
import anyio
from claude_agent_sdk import query

async def main():
    async for message in query(prompt="What is 2 + 2?"):
        print(message)

anyio.run(main)
```

**Output example**: Claude returns the calculation result.

### ③ Email Agent Scenario

**Architecture Design**:

- Store previous conversations in `Conversations/` folder → search via grep
- Execute parallel queries with search Subagent
- Verify via Asana MCP if "assignee already assigned"
- Add email address validation rule

```
from claude_agent_sdk import ClaudeAgentOptions

options = ClaudeAgentOptions(
    allowed_tools=["Read", "Bash", "mcp__asana__get_tasks"],
    permission_mode='prompt'  # Request approval when modifying files
)
```

**Note**: Actual implementation requires additional code for MCP server setup and tool definitions. See [official documentation](https://docs.claude.com/en/api/agent-sdk/overview).

---

## 4. Best Practices

| Pattern | Advantage | Caution |
| --- | --- | --- |
| **Agentic Search First** | Dynamic search eliminates re-indexing need | May be slower than semantic search |
| **Subagent Parallelization** | Speed improvement + context savings | Orchestration complexity increases |
| **TypeScript > JavaScript** | Multi-layer feedback via linting | Initial setup cost |
| **MCP-First Integration** | Automatic OAuth handling | Ecosystem dependency |
| **Small Test Sets** | Improvement based on failure cases | Initial preparation time needed |

The key to agent improvement is analyzing failures carefully and asking, "Do we have the right tools?"

---

## 5. Conclusion

**3 Key Takeaways**:

1. Claude Agent SDK, released alongside Claude Sonnet 4.5, is an example of expanding coding infrastructure into a general-purpose agent.
2. The loop design of context gathering, execution, and verification is critical for agent reliability.
3. Without RAG pipelines, you can build powerful agents using just the file system and Bash.

**Practical Tips**: Start with simple tasks (mail classification, document search), gradually add tools, and improve rules and tools based on failure case logs.

---

## References

- **Official Documentation**: [Claude Agent SDK Overview](https://docs.claude.com/en/api/agent-sdk/overview)
- **Engineering Blog**: [Building agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) (2025.09.29)
- **Official Announcement**: [Claude Sonnet 4.5 & Agent SDK Introduction](https://www.anthropic.com/news/claude-sonnet-4-5) (2025.09.29)
- **GitHub Repository**: [anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python)
- **MCP Ecosystem**: [Model Context Protocol Servers](https://github.com/modelcontextprotocol/servers)
