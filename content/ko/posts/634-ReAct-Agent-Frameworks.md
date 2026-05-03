---
title: "ReAct Agent Frameworks"
date: 2025-06-01T11:09:06+09:00
slug: "634-ReAct-Agent-Frameworks"
original_url: "https://memoryhub.tistory.com/634"
tistory_id: 634
draft: false
---

## ? Industry-Standard ReAct Agent Frameworks

### 1. **LangChain/LangGraph** (Most Mature & Compatible)

LangChain provides built-in ReAct support through the create\_react\_agent function, making it the most straightforward choice for ReAct implementation.

**Quick Implementation:**

```
from langchain.agents import create_react_agent, AgentExecutor
from langchain_openai import ChatOpenAI
from langchain_community.tools import TavilySearchResults
from langchain import hub

# 간단한 ReAct 에이전트 설정
llm = ChatOpenAI(model="gpt-4")
tools = [TavilySearchResults()]
prompt = hub.pull("hwchase17/react")  # ReAct 프롬프트 템플릿

# ReAct 에이전트 생성
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 실행
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

# 메모리 지원 ReAct 에이전트
memory = MemorySaver()
agent = create_react_agent(
    model="gpt-4",
    tools=[search_tool, calculator_tool],
    checkpointer=memory  # 지속적 메모리
)

# 대화 기록 유지
response = agent.invoke(
    {"messages": [HumanMessage(content="분석해줘")]},
    config={"configurable": {"thread_id": "conv_123"}}
)
```

**Best for:** Complex workflows requiring precise control over state and execution flow

### 3. **CrewAI** (Easiest for Beginners)

CrewAI is built on top of LangChain and offers a higher-level abstraction called a "Crew," which is basically a container for multiple agents.

```
from crewai import Agent, Task, Crew

# 역할 기반 에이전트 정의
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

# 태스크 정의
research_task = Task(
    description='Research the latest AI trends',
    agent=researcher
)

# Crew 생성 및 실행
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

# 대화형 에이전트 생성
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

# 멀티 에이전트 대화
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

# 간단한 에이전트 정의
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

# 실행
client = Swarm()
response = client.run(
    agent=support_agent,
    messages=[{"role": "user", "content": "Analyze this data"}]
)
```

## ? Framework Comparison

Framework ReAct Support Learning Curve Production Ready Best For

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **LangChain** | ✅ Native | Medium | ✅ Yes | General purpose, mature ecosystem |
| **LangGraph** | ✅ Customizable | High | ✅ Yes | Complex workflows, fine control |
| **CrewAI** | ⚠️ Via LangChain | Low | ✅ Yes | Multi-agent, role-based tasks |
| **AutoGen** | ⚠️ Custom impl | High | ✅ Yes | Research, complex reasoning |
| **Swarm** | ⚠️ Basic | Low | ❌ No | Learning, simple prototypes |

## ? Recommendations

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
# Pydantic AI의 타입 안전성을 유지하면서 LangChain으로 마이그레이션
from pydantic import BaseModel
from langchain.output_parsers import PydanticOutputParser

class AgentOutput(BaseModel):
    """Pydantic 모델을 그대로 사용"""
    thought: str
    action: str
    observation: str

# LangChain에서 Pydantic 통합
parser = PydanticOutputParser(pydantic_object=AgentOutput)
```

The consensus in the developer community is that **LangChain/LangGraph offers the most mature and compatible ReAct implementation**, while CrewAI provides the easiest entry point for beginners. AutoGen is powerful but requires more expertise to implement effectively.
