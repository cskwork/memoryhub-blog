---
title: "ReAct Agent Frameworks"
date: 2025-06-01T11:09:06+09:00
slug: "634-ReAct-Agent-Frameworks"
original_url: "https://memoryhub.tistory.com/634"
tistory_id: 634
draft: false
categories: ["Dev Library"]
tags: ["GPT"]
---

## 🚀 Industry-Standard ReAct Agent Frameworks

### 1. **LangChain/LangGraph** (Most Mature & Compatible)

LangChain provides built-in ReAct support through the create_react_agent function, making it the most straightforward choice for ReAct implementation.

**Quick Implementation:**

```
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_community.tools import TavilySearchResults
from langchain import hub

# Simple ReAct agent setup
llm = ChatOpenAI(model="gpt-4")
tools = [TavilySearchResults()]
prompt = hub.pull("hwchase17/react")  # ReAct prompt template

# Create ReAct agent
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Execute
result = agent_executor.invoke({"input": "What's the weather in Seoul?"})
```

**Advantages:**

- Native ReAct support out of the box
- Extensive documentation and community
- Memory persistence through checkpointing
- Production-ready with LangSmith integration
- Huge ecosystem of tools and integrations

### 2. **LangGraph** (Advanced Graph-Based)

LangGraph allows you to build custom ReAct agents with fine-grained control over the reasoning loop.

```
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

# Memory-supported ReAct agent
memory = MemorySaver()
agent = create_react_agent(
    model="gpt-4",
    tools=[search_tool, calculator_tool],
    checkpointer=memory  # Persistent memory
)

# Maintain conversation history
response = agent.invoke(
    {"messages": [HumanMessage(content="Analyze this")]},
    config={"configurable": {"thread_id": "conv_123"}}
)
```

**Best for:** Complex workflows requiring precise control over state and execution flow

### 3. **CrewAI** (Easiest for Beginners)

CrewAI is built on top of LangChain and offers a higher-level abstraction called a "Crew," which is basically a container for multiple agents.

```
from crewai import Agent, Task, Crew

# Define role-based agents
researcher = Agent(
    role='Research Analyst',
    goal='Find accurate information',
    backstory='Expert at finding and analyzing data',
    tools=[search_tool],
    verbose=True
)

analyst = Agent(
    role='Data Analyst',
    goal='Analyze and synthesize information',
    backstory='Skilled at drawing insights from data'
)

# Define tasks
research_task = Task(
    description='Research the latest AI trends',
    agent=researcher
)

# Create and run Crew
crew = Crew(
    agents=[researcher, analyst],
    tasks=[research_task],
    verbose=True
)

result = crew.kickoff()
```

**Advantages:**

- Faster setup process and more straightforward to get started with
- Built-in role-based collaboration
- Human-in-the-loop support
- Good for multi-agent scenarios

### 4. **AutoGen** (Most Powerful but Complex)

AutoGen offers granular control over agent behavior, system messages, and termination conditions.

```
from autogen import ConversableAgent, AssistantAgent

# Create conversable agents
assistant = AssistantAgent(
    name="assistant",
    llm_config={"model": "gpt-4"},
    system_message="You are a helpful AI assistant"
)

user_proxy = ConversableAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": True}
)

# Multi-agent conversation
user_proxy.initiate_chat(
    assistant,
    message="Solve this step by step..."
)
```

**Best for:** Dynamic problem-solving scenarios where you want the agent to come up with a solution

### 5. **OpenAI Swarm** (Lightweight & Educational)

A lightweight, minimalist framework described by OpenAI to be "educational" rather than "production-ready".

```
from swarm import Swarm, Agent

# Define simple agents
def transfer_to_analyst():
    return analyst_agent

support_agent = Agent(
    name="Support",
    instructions="You are a support agent",
    functions=[transfer_to_analyst]
)

analyst_agent = Agent(
    name="Analyst",
    instructions="You analyze data"
)

# Execute
client = Swarm()
response = client.run(
    agent=support_agent,
    messages=[{"role": "user", "content": "Analyze this data"}]
)
```

## 📊 Framework Comparison

| Framework | ReAct Support | Learning Curve | Production Ready | Best For |
|---|---|---|---|---|
| **LangChain** | ✅ Native | Medium | ✅ Yes | General purpose, mature ecosystem |
| **LangGraph** | ✅ Customizable | High | ✅ Yes | Complex workflows, fine control |
| **CrewAI** | ⚠️ Via LangChain | Low | ✅ Yes | Multi-agent, role-based tasks |
| **AutoGen** | ⚠️ Custom impl | High | ✅ Yes | Research, complex reasoning |
| **Swarm** | ⚠️ Basic | Low | ❌ No | Learning, simple prototypes |

## 💡 Recommendations

### Choose **LangChain** if you want:

- Industry-standard ReAct implementation
- Extensive documentation and community support
- Production-ready features with monitoring
- Wide range of pre-built tools and integrations

### Choose **CrewAI** if you want:

- Easiest setup for multi-agent systems
- Role-based agent collaboration
- Built on top of LangChain and can perform code execution for LLM-generated codes in a simple manner

### Choose **AutoGen** if you want:

- Maximum control and customization
- Built-in secure code execution (containerized environments)
- Complex multi-agent conversations

### Migration Path from Pydantic AI:

```
# Maintain Pydantic AI's type safety while migrating to LangChain
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser

class AgentOutput(BaseModel):
    """Use Pydantic model as-is"""
    thought: str
    action: str
    observation: str

# Integrate Pydantic with LangChain
parser = PydanticOutputParser(pydantic_object=AgentOutput)
```

The consensus in the developer community is that **LangChain/LangGraph offers the most mature and compatible ReAct implementation**, while CrewAI provides the easiest entry point for beginners. AutoGen is powerful but requires more expertise to implement effectively.
