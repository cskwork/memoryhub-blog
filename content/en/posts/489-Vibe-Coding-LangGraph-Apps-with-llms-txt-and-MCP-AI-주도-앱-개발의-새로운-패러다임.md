---
title: "Vibe Coding, LangGraph Apps with llms.txt and MCP - New Paradigm of AI-Driven App Development"
date: 2025-03-21T02:46:31+09:00
slug: "489-Vibe-Coding-LangGraph-Apps-with-llms-txt-and-MCP-AI-주도-앱-개발의-새로운-패러다임"
original_url: "https://memoryhub.tistory.com/489"
tistory_id: 489
draft: false
---

Vibe Coding is a new programming paradigm where developers focus on intent and design rather than code implementation. Combined with LangGraph, llms.txt, and MCP, AI-based application development becomes intuitive and efficient. This approach shortens development time and simplifies building complex agent systems.

Imagine explaining a cooking recipe to AI. Instead of listing exact measurements and procedures, you describe desired flavors and textures, and AI writes the detailed recipe automatically. Vibe Coding is similar—developers describe wanted functionality at high level, and AI handles actual code implementation.

- Developers focus on "what" they want; AI decides "how" to implement
- Complex application structures can be designed with intuitive natural language
- Feel overall system flow rather than syntactic details

## Why is it Needed?

Problems that Vibe Coding, LangGraph, llms.txt, and MCP solve:

1. **Reduced development complexity**: Traditional programming requires detailed syntax knowledge and numerous code lines. Vibe Coding lets developers focus on big picture by having AI handle implementation.
2. **Managing complex LLM workflows**: AI systems with interacting agents face difficult state management and agent coordination. LangGraph simplifies complexity with graph-based approach.
3. **Lack of standardization**: No consistent standard existed for how LLMs interact with external data and tools. MCP standardizes this, increasing development efficiency.
4. **Limited AI accessibility**: Websites and documents are structured in formats hard for AI to understand. llms.txt shows how websites can effectively provide information to LLMs.

## Basic Principle

Let's explore core principles of Vibe Coding, LangGraph, llms.txt, and MCP.

### Vibe Coding Principle

Vibe Coding is paradigm centered on development intent rather than code implementation. Developers describe desired functionality in natural language, and AI converts that intent into actual code.

```
# Traditional coding approach
def parse_csv(file_path):
    import pandas as pd
    data = pd.read_csv(file_path)
    filtered_data = data[data['score'] > 75]
    return filtered_data.groupby('category').mean()

# Vibe Coding approach
"""
Filter items with score 75 or higher from CSV file
and calculate average by category.
"""
# AI generates appropriate code based on these instructions
```

### LangGraph Principle

LangGraph defines LLM application workflows as graphs. Nodes represent execution steps; edges represent control flow.

```
from langgraph.graph import StateGraph
from typing import TypedDict, List

# Define state
class AgentState(TypedDict):
    messages: List
    next_steps: List

# Create graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("parse_request", parse_request_fn)
workflow.add_node("search_knowledge", search_knowledge_fn)
workflow.add_node("generate_response", generate_response_fn)

# Add edges (define control flow)
workflow.add_edge("parse_request", "search_knowledge")
workflow.add_edge("search_knowledge", "generate_response")

# Compile graph
agent = workflow.compile()
```

### llms.txt Principle

llms.txt is markdown file format for websites to effectively provide information to LLMs. Provides core website information in structured way.

```
# Company Website llms.txt

## Key Information
- Company Name: ABC Technology
- Founded: 2020
- Main Products: AI Solutions, Cloud Services

## Important Pages
- Product Intro: https://example.com/products
- Pricing: https://example.com/pricing
- Developer Docs: https://example.com/docs

## API Documentation
API endpoints are as follows:
- GET /api/users - User information inquiry
- POST /api/auth - Issue authentication token
```

### MCP (Model Context Protocol) Principle

MCP standardizes how LLMs interact with external data sources and tools. Connects diverse tools and data sources in consistent way.

```
from mcp.client import MCPClient
from mcp.tools import WebSearchTool, DatabaseTool

# Set up MCP client
client = MCPClient()

# Register tools
client.register_tool(WebSearchTool())
client.register_tool(DatabaseTool(connection_string="..."))

# Provide MCP context to LLM
response = client.run(
    model="claude-3",
    prompt="Search user database for 10 recently joined users and analyze them",
    tools=["web_search", "database"]
)
```

## Real Example

Let's examine example of developing large language model-based customer support system.

### Basic Usage

Below is example implementing customer support agent in Vibe Coding style using LangGraph:

```
from langgraph.graph import StateGraph
from langchain.chat_models import ChatAnthropic
from langchain.schema import HumanMessage, AIMessage
from typing import TypedDict, List, Dict

# Define state
class AgentState(TypedDict):
    messages: List
    customer_info: Dict
    support_db: Dict

# Initialize LLM model
llm = ChatAnthropic(model="claude-3-sonnet-20240229")

# Vibe Coding this section with natural language description
"""
Create customer support agent with following workflow:
1. Analyze customer request and identify intent
2. Search customer information database for relevant information
3. Find solutions in support knowledge base
4. Generate customized response to customer
5. Escalate to human representative if needed
"""

# AI generates LangGraph structure based on these instructions
workflow = StateGraph(AgentState)
workflow.add_node("parse_intent", parse_intent_fn)
workflow.add_node("retrieve_customer_info", retrieve_customer_info_fn)
workflow.add_node("search_knowledge_base", search_knowledge_base_fn)
workflow.add_node("generate_response", generate_response_fn)
workflow.add_node("human_escalation", human_escalation_fn)

# Add conditional edges
workflow.add_conditional_edges(
    "parse_intent",
    lambda state: "retrieve_customer_info" if not state.get("escalate") else "human_escalation"
)
workflow.add_edge("retrieve_customer_info", "search_knowledge_base")
workflow.add_edge("search_knowledge_base", "generate_response")

# Compile and run graph
agent = workflow.compile()
```

### Real-World Application

Below compares traditional development approach with Vibe Coding + LangGraph/MCP approach:

| Situation | General Approach | Vibe Coding + LangGraph/MCP | Improvement |
| --- | --- | --- | --- |
| Agent workflow design | Code detailed control flow | Describe workflow in natural language | 70% reduction in development time |
| External API integration | Different integration for each API | Standardized integration with MCP | 50% improvement in maintainability |
| Documentation | Separate documentation needed | llms.txt automatically provides AI accessibility | 60% time savings in documentation |
| Modify agent logic | Code editing and redeployment | Update logic with natural language instruction | 80% reduction in iteration cycle |

## Precautions and Tips

⚠️ **Watch Out For These!**

1. **Avoid over-reliance**

   - Don't implicitly trust AI-generated code; validate it
   - Important business logic requires additional review
2. **Avoid ambiguous instructions**

   - Vibe Coding requires clear intent communication
   - Be specific: "Write code for validating user input" instead of "Write good code"
3. **Automate testing essential**

   - AI-generated code may behave unexpectedly
   - Continuous validation through automated testing is necessary

💡 **Helpful Tips**

- Use LangGraph Studio to visually debug workflows
- llms.txt files are most effective keeping only essential information concise
- Modularize MCP clients for improved reusability
- Breaking complex logic into multiple small steps produces more accurate Vibe Coding results
- Ask AI for explanations of unclear code parts

## Conclusion

So far, we've explored AI-driven app development using Vibe Coding, LangGraph, llms.txt, and MCP. This approach lets developers focus on creative problem-solving and system design rather than implementation details. Though intuitive coding style feels unfamiliar initially, once familiar, development efficiency and enjoyment increase significantly.

As programming paradigm increasingly evolves toward AI collaboration, the future of coding moves closer to clear intent communication rather than accurate syntax writing. Vibe Coding approaches like this are central to this transformation.

If curious or want to learn more, please comment.

## References

- [LangGraph Official Documentation](https://www.langchain.com/langgraph)
- [Model Context Protocol Specification](https://github.com/modelcontextprotocol)
- [llms.txt Guidelines](https://www.analyticsvidhya.com/blog/2025/03/llms-txt/)
- [LangGraph Studio Tutorial](https://langchain-ai.github.io/langgraph/concepts/langgraph_studio/)
- [Vibe Coding Beginner's Guide](https://zbrain.ai/what-is-vibe-coding/)

---

#VibeCoding #LangGraph #MCP #AIAssisted #LLMAgent
