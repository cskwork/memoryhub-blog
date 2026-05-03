---
title: "Claude Agent SDK: Effective Agent Building Guide"
date: 2025-10-19T00:36:07+09:00
slug: "861-Claude-Agent-SDK_-효과적인-에이전트-구축-가이드"
original_url: "https://memoryhub.tistory.com/861"
tistory_id: 861
draft: false
---

Claude Agent SDK is a set of tools that helps you build powerful agents based on Claude Code. This article introduces how to get started and best practices.

Last year, I shared how to build effective agents with customers. Since then, Anthropic released Claude Code, our own agent coding solution for improving developer productivity.

Over the past few months, Claude Code has become more than just a coding tool. At Anthropic, we use it for deep research, video production, note-taking, and more beyond coding. Actually, it's driving most of our major agent loops now.

In other words, the agent harness that powers Claude Code (Claude Code SDK) can power other types of agents too. To reflect this expanded vision, we're renaming Claude Code SDK to **Claude Agent SDK**.

This article covers why we developed Claude Agent SDK, how to build your own agents with it, and best practices from our team's real deployment experience.

## Providing Claude with a Computer

The core design principle of Claude Code is **Claude should use the same tools programmers use every day**. It should find appropriate files from codebases, write and edit files, lint code, run it, debug it, edit again, and sometimes repeat these actions until code succeeds.

By providing Claude access to the user's computer (through the terminal), it has everything needed to code like a programmer.

But this also makes Claude from Claude Code effective at non-coding tasks. By providing access to bash command execution, file editing, file creation, and file search tools, Claude can perform all kinds of digital work: reading CSV files, searching the web, building visualizations, interpreting metrics, and more. In other words, you can create a general-purpose agent that uses a computer.

The core design principle of Claude Agent SDK is **providing agents with a computer so they work like people do**.

## Creating New Types of Agents

We believe providing Claude with a computer enables building more effective agents than before. For example, with the SDK, developers can create:

**Financial agents**: Agents that understand portfolios and goals, access external APIs, store data, and run code for calculations to evaluate investments

**Personal assistant agents**: Agents that book travel, manage schedules, set appointments, prepare briefings—connected to internal data sources and track context across applications

**Customer support agents**: Agents that handle ambiguous user requests like customer service tickets, collect and review user data, connect to external APIs, message users, and escalate to humans when needed

**Deep research agents**: Agents that search large document collections, analyze and synthesize information from multiple sources, cross-reference data across files, and generate detailed reports

And more. Fundamentally, the SDK provides building blocks to create agents for any workflow you want to automate.

## Building Agent Loops

In Claude Code, Claude operates in a specific feedback loop: **Gather context → Execute action → Validate work → Iterate**

This provides a useful way to think about other agents and what capabilities they need. To illustrate, let's look at an example of building an email agent with Claude Agent SDK.

### 1. Context Gathering

When developing agents, you shouldn't just provide a prompt—agents must be able to gather and update their own context. Let's see how SDK features help:

**Agent Search and File System**

The file system represents information the model can bring into its context.

When Claude encounters large files like logs or user-uploaded files, it uses bash scripts like grep or tail to decide how to load them into context. Essentially, the folder and file structure of an agent becomes a kind of context engineering.

An email agent could store previous conversations in a 'Conversations' folder. When relevant questions come up, it can search previous conversations to find context.

**Semantic Search**

Semantic search is typically faster than agent search but less accurate, harder to maintain, and less transparent. It works by "chunking" relevant context, embedding these chunks as vectors, then querying those vectors to search concepts. Given these limitations, we recommend starting with agent search and adding semantic search only when you need faster results or more variations.

**Sub-agents**

Claude Agent SDK natively supports sub-agents. Sub-agents are useful for two main reasons.

First, parallelization. You can run multiple sub-agents simultaneously to handle different tasks.

Second, context management. Sub-agents use their own isolated context window and pass only relevant information back to the orchestrator, not everything. Perfect for tasks where you need to filter through massive amounts of mostly-useless information.

When designing an email agent, you could provide a "search sub-agent" capability. Then the email agent can run multiple search sub-agents in parallel, each executing different queries against email history, returning only relevant excerpts rather than full email threads.

**Compaction**

When agents run for extended periods, context management matters. Claude Agent SDK's compact feature automatically summarizes previous messages when approaching context limits, preventing agents from exhausting context. This is based on Claude Code's compact slash command.

### 2. Executing Actions

After gathering context, you must provide agents with flexible ways to execute actions.

**Tools**

Tools are a key component of agent execution. They're prominently displayed in Claude's context window, so they're key actions Claude considers when deciding how to complete tasks. This means you must think carefully about how to design tools to maximize context efficiency.

So tools should be the main actions your agent performs. Learn how to create custom tools in Claude Agent SDK.

For an email agent, you could define tools like "fetchInbox" or "searchEmails" as the agent's most frequently used main actions.

**Bash and Scripts**

Bash is useful as a general-purpose tool enabling agents to perform flexible tasks using the computer.

For an email agent, users might have important information stored in attachments. Claude can write code to download a PDF, convert it to text, search it, and find useful information.

**Code Generation**

Claude Agent SDK excels at code generation, and for good reason. Code is precise, composable, and infinitely reusable—ideal output for agents needing to reliably perform complex tasks.

When building agents, ask: What tasks benefit from being expressed as code? Often the answer opens up substantial functionality.

For example, file generation capabilities recently launched in Claude.AI rely entirely on code generation. Claude writes Python scripts to generate Excel spreadsheets, PowerPoint presentations, Word documents with consistent formatting and complex features otherwise hard to achieve.

For an email agent, you might want users to create rules for incoming emails. You could write code to run on those events.

**MCP**

Model Context Protocol (MCP) provides standardized integration with external services, automatically handling authentication and API calls. This means you can connect agents to tools like Slack, GitHub, Google Drive, Asana without writing integration code or managing OAuth flows yourself.

For an email agent, you might want to search Slack messages to understand team context, or check Asana tasks to see if someone is already assigned to handle customer requests. MCP servers make these integrations work immediately—Claude just calls tools like search_slack_messages or get_asana_tasks and MCP handles the rest.

As the MCP ecosystem grows, pre-built integrations are available, letting you quickly add new functionality to agents while staying focused on agent behavior.

### 3. Validating Work

Claude Code SDK completes the agent loop by evaluating work. Agents that can check their own output and improve are fundamentally more stable. They catch mistakes before they accumulate, correct course when things go wrong, and improve with iteration.

The key is providing Claude with specific ways to evaluate tasks. We've found three approaches effective:

**Define Rules**

The best feedback is clear, defined rules about output, then explains which rules failed and why.

Code linting is a great form of rule-based feedback. The more detailed feedback, the better. For example, generating TypeScript and linting it is usually better than pure JavaScript. It provides multiple additional feedback layers.

When generating emails, you could make Claude verify email addresses are valid (error if not) or check if the user previously emailed them (warn if so).

**Visual Feedback**

When using agents for visually-oriented tasks like UI generation or testing, visual feedback (screenshots or renderings) can help. For example, when sending HTML-formatted emails, take a screenshot and provide it to the model for visual validation and iterative improvement. The model then confirms visual output matches what was requested.

For example:

- **Layout** - Are elements positioned correctly? Is spacing appropriate?
- **Styling** - Do colors, fonts, formatting appear as intended?
- **Content hierarchy** - Is information presented in the right order with appropriate emphasis?
- **Responsiveness** - Broken or narrow-looking? (Single screenshot limits viewport info, but helps)

Using MCP servers like Playwright, you can automate these visual feedback loops. Screenshot rendered HTML, capture various viewport sizes, even test interactive elements—all within agent workflows.

**Using LLMs as Evaluators**

You can also have another language model "grade" agent output against ambiguous rules. This generally isn't robust and has major latency tradeoffs, but for applications where performance improvement justifies costs, it can help.

An email agent could use a separate sub-agent to evaluate draft tone, ensuring it matches the user's previous messages.

## Testing and Improving Agents

After looping through the agent cycle a few times, test agents and confirm they're ready for tasks. The best way to improve agents is carefully reviewing output—especially failures—and thinking from the agent's perspective. Does it have the right tools for the job?

When evaluating if agents are ready for tasks, ask:

- If the agent misunderstands tasks, critical information might be missing. Can you restructure the search API so needed information is easier to find?
- If the agent repeatedly fails at tasks, can you add formal rules to tool calls to identify and fix failures?
- If the agent can't fix errors, can you provide more useful or creative tools to approach problems differently?
- If performance fluctuates with new features, build representative test sets based on customer usage patterns for programmatic evaluation (or evals).

## Getting Started

Claude Agent SDK makes building autonomous agents easier by providing compute access—writing files, running commands, iterating on work.

With the agent loop (gather context, execute action, validate work) in mind, you can build reliable agents that are easy to deploy and iterate.

You can start with Claude Agent SDK today. If you're already building based on the SDK, we recommend migrating to the latest version following this guide.

---

**Key Summary**: Claude Agent SDK provides agents with computers for file writing, command execution, and iteration. Through context gathering → action execution → work validation loops, it enables building autonomous agents across diverse domains like finance, research, and customer support.

<https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk>
