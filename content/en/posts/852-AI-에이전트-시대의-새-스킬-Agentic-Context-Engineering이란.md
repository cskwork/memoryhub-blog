---
title: "A New Skill in the Age of AI Agents: What is Agentic Context Engineering?"
date: 2025-10-14T12:39:24+09:00
slug: "852-AI-에이전트-시대의-새-스킬-Agentic-Context-Engineering이란"
original_url: "https://memoryhub.tistory.com/852"
tistory_id: 852
draft: false
categories: ["Dev Util"]
tags: ["Agents"]
---

```
    _______________
   /               \
  /   CONTEXT       \
 /    ENGINEERING    \
|   _________________ |
|  |  Prompt  Tools | |
|  |  Memory  Data  | |
|  |  ___________   | |
|  | |  AGENT   |  | |
|  | |__________|  | |
|  |_________________| |
 \___________________/
      [  LLM  ]
```

There's a reason prompt engineering alone wasn't enough. Over the past few months, the term "Context Engineering" has emerged among AI developers, with practitioners saying "now we need to design context, not just prompts." Especially in systems like AI agents that perform complex tasks across multiple steps, success depends not just on asking good questions, but on strategically curating what information to provide, when, and how.

Through this guide, you'll learn core concepts of context engineering immediately applicable in practice and the latest research results (ACE framework).

**One-line summary**

Agentic Context Engineering is the technology of cyclically curating optimal information to fit within a limited context window as AI agents perform tasks, and it's a field that goes beyond prompt writing to design the information flow of the entire system.

## Background

### From prompt engineering to context engineering

Early LLM utilization mostly involved one-off tasks. For single-use tasks like classification, summarization, and text generation, writing a good prompt was sufficient. But the situation changed as the age of AI agents opened.

| Aspect | Prompt Engineering | Context Engineering |
| --- | --- | --- |
| Focus | Optimize system prompt writing | Manage entire context window state |
| Application timing | Before single task starts | Throughout multi-turn reasoning |
| Information scope | Mainly instructions | Prompts + tools + memory + external data |
| Update cycle | Static | Cyclic, iterative |

AI agents call tools across multiple steps, interact with environments, and perform long-term tasks. In this process, the context window fills quickly, gets contaminated with irrelevant information (Context Poisoning), or loses important information (Context Collapse).

### What is context?

Context is the set of tokens included when an LLM samples.

Specifically:

- System prompts and instructions
- User inputs and questions
- Short-term memory (conversation history)
- Long-term memory (past task information)
- Retrieved knowledge base information
- Tool descriptions and MCP protocol
- External API response data

Andrej Karpathy expressed it as: "LLM is a new operating system, and context window is like RAM." Context engineering is the delicate work of filling precise information needed for the next step within limited capacity.

### Why is it more important for agents?

AI agents face much harder context management due to these problems:

- Token limit exceeded: Context window fills up during long-running tasks
- Cost and latency: More unnecessary information increases API costs and reduces response speed
- Performance degradation: Noise information reduces reasoning quality
- Tool confusion: Too many tool descriptions confuse which tool to use

## Core Concept

> Agentic Context Engineering is a strategic design methodology for AI agents to select, compress, store, and isolate information suitable for limited context windows at each reasoning step.

Anthropic defines context engineering as "the art and science of filling the context window with information appropriate for the next step." This is a natural evolution of prompt engineering and an essential technique for building complex agentic systems.

### ACE Framework: Agents Evolving Context

In October 2025, a research team from Stanford and UC Berkeley released the ACE (Agentic Context Engineering) framework, treating context not as a static prompt but as an evolving playbook.

Problems with existing approaches:

- Brevity Bias: Important domain knowledge is omitted during summarization
- Context Collapse: Details gradually disappear through repeated rewriting

ACE operates with three roles:

1. Generator: Executes reasoning process and generates results
2. Reflector: Extracts concrete insights from successes and failures
3. Curator: Integrates insights into structured context updates

Core design principles:

- Incremental delta updates: Add only new items without rewriting everything
- Grow-and-Refine: Progressively improve while preserving useful history
- Structured accumulation: Systematically accumulate knowledge for long-context usage

Empirical results:

- AppWorld agent benchmark: +10.6% performance improvement over baseline
- Financial domain reasoning: +8.6% accuracy improvement
- Latency: 82-92% reduction
- Token cost: 75-84% savings

Notably, open-source models with ACE applied (DeepSeek-V3.1) showed equivalent performance to GPT-4.1-based production agents (IBM CUGA), proving that context design alone can bridge model performance gaps.

## Hands-on Practice

We'll explore how to implement context engineering in practice step by step.

### 1. Establish context strategy: Write, Select, Compress, Isolate

Apply the four patterns proposed by Lance Martin:

**Write (create)**: Store information outside context window

- Store task history in database
- Manage learned patterns in separate files
- Index agent memory in vector DB

**Select (choose)**: Bring only necessary information into context

- Search only relevant documents with RAG
- Tool description filtering: Select tools based on semantic similarity
- For code agents, embed only meaningful chunks via AST parsing

**Compress (condense)**: Keep only essentials

- Conversation summarization: Keep recent 3 turns fully, summarize others
- Token optimization: Remove duplicates, use abbreviations
- Apply prompt compression techniques

**Isolate (separate)**: Prevent confusion through context separation

- Multi-agent: Independent context per agent
- Domain separation: Dedicated context for finance/legal tasks
- Hierarchy: Separate main and sub-agent contexts

### 2. Optimize tool management

Agents become confused when shown too many tools.

Implementation method:

```
User query: "Analyze recent sales data"

Step 1: Embed tool descriptions
   - Vectorize all 50 tools

Step 2: Calculate semantic similarity with query
   - Select top 5 tools only
   - "sales_data_fetch", "analytics_tool", "chart_generator" ...

Step 3: Include only selected tools in context
   - 3x improvement in tool selection accuracy (recent research)
```

### 3. Design memory system

Clearly separate short-term and long-term memory:

Short-term memory:

- Maintain last 3-5 turns of conversation fully
- Intermediate results of current task
- Temporary variables and state

Long-term memory:

- User preferences
- Successfully applied strategy patterns
- Domain-specific knowledge
- ACE-style playbooks

Storage location:

- Short-term: Within context window
- Long-term: Vector DB, graph DB, key-value store

### 4. Build iterative improvement loop

Real-world process inspired by ACE framework:

```
Iteration cycle:

[Execute]
→ Agent performs task
→ Collect execution results and feedback

[Reflect]
→ What worked well?
→ What information was missing?
→ What patterns repeat?

[Curate]
→ Convert insights into structured items
→ Add delta update to playbook
→ Apply merge rules if conflicting with existing items

[Apply]
→ Perform next task with updated context
```

### 5. Monitor context quality

Track context status in real-time:

Monitoring metrics:

- Context window utilization (70-90% recommended)
- Relevant information vs noise ratio
- Tool call success rate
- Task completion time
- API token consumption

Cognizant announced in August 2025 that it will deploy 1,000 context engineers through its ContextFabric platform. They will convert enterprise operating models, workflows, and policies into context that agents can understand. This shows context engineering is becoming a professional specialty, not just a technique.

## Best practices and pattern comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Static Prompt | Simple to implement, predictable | Unsuitable for complex agent tasks, no adaptability |
| Dynamic Summary | Can control context size | Risk of Brevity Bias losing important info, Context Collapse |
| RAG-based Selection | Provide only relevant information | Depends on search quality, embedding model performance critical |
| Delta Update (ACE) | Accumulate information, preserve details, scalable | High implementation complexity, depends on feedback quality |
| Multi-Agent Isolation | Specialized per role, prevent context confusion | Need inter-agent coordination, increased overhead |
| Hierarchical Memory | Clearly distinguish short/long-term info | Memory system design and maintenance costs |

## Conclusion

AI agent performance isn't determined by the model alone. What information you provide, when, and how matters. If prompt engineering was "what will we ask," context engineering is "what will we show." As the ACE framework proved, even open-source models can compete with premium models through appropriate context design.

Practical tip:

When starting your next AI agent project, ask first: "Is our agent really seeing only the necessary information at each step?" Redesigning your context strategy using the Write-Select-Compress-Isolate pattern can simultaneously achieve performance improvements and cost savings.

## References

- Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models (<https://arxiv.org/abs/2510.04618>)
- Effective context engineering for AI agents - Anthropic (<https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents>)
- Context Engineering for Agents - Lance Martin (<https://rlancemartin.github.io/2025/06/23/context_engineering/>)
- Cognizant to Deploy 1,000 Context Engineers (<https://news.cognizant.com/2025-08-29-Cognizant-to-Deploy-1,000-Context-Engineers>)
- How to Perform Effective Agentic Context Engineering - Towards Data Science (<https://towardsdatascience.com/how-to-perform-effective-agentic-context-engineering/>)
- Context Engineering - LlamaIndex (<https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider>)
