---
title: "Model Context Protocol (MCP) - Building Your Own AI Tool Server - Complete Mastery ⚙️"
date: 2025-06-01T10:56:24+09:00
slug: "627-Model-Context-Protocol-MCP-나만의-AI-도구-서버-만들기-완전-정복"
original_url: "https://memoryhub.tistory.com/627"
tistory_id: 627
draft: false
categories: ["Dev Library"]
tags: ["MCP"]
---

Imagine if AI chatbots could read files, query databases, and call APIs. This is exactly the magic that **Model Context Protocol (MCP)** enables! Today, we'll explore how to build your own MCP server from A to Z.

## Background ⚙️

What was it like before MCP existed?

**Before 2024**:

- Each AI application required separate custom integrations ⚙️
- M AI apps × N tools = M×N integration tasks
- Duplicate code, inconsistent implementations, maintenance nightmare

**After November 2024** (MCP Launch):

- Anthropic released it as open source standard ⚙️
- Like USB-C, one standard to connect everything
- Reduced to M+N tasks!

Key problems MCP solves:

1. **Data Silo Problem**: AI cannot access isolated data
2. **Integration Complexity**: Each tool has different APIs and authentication methods
3. **Lack of Scalability**: Modifying entire system with each new tool addition

## Core Principles ⚙️

MCP operates on a client-server architecture. Just as a web server responds to browser requests, MCP servers respond to AI application requests.

### Key Components

| Component | Role | Example |
|---|---|---|
| **Host** ⚙️ | Application managing MCP clients | Claude Desktop, VS Code, Cursor |
| **Client** ⚙️ | Protocol handler maintaining 1:1 connection with server | Connection manager inside Host |
| **Server** ⚙️ | Lightweight program exposing specific functions | File system server, DB server, API server |

### 3 Core Capabilities MCP Provides

```
┌─────────────────────────────────────┐
│           MCP Server                │
├─────────────────────────────────────┤
│  ⚙️  Tools (Functions)              │
│  📚 Resources (Data)                │  
│  💬 Prompts (Templates)             │
└─────────────────────────────────────┘
```

1. **Tools** ⚙️: Functions AI can execute
   - Example: get_weather(), send_email(), query_database()
2. **Resources** 📚: Data AI can read
   - Example: File contents, API responses, database records
3. **Prompts** 💬: Pre-defined templates
   - Example: "Review this code", "Summarize the data"

## Building an MCP Server with Python ⚙️

Now let's actually build one! We'll implement a simple MCP server providing calculator functionality.

### 1. Environment Setup

```
# Create project directory
mkdir my-mcp-server
cd my-mcp-server

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install required packages
pip install "mcp[cli]"
```

### 2. Basic Server Implementation

```
# calculator_server.py
from mcp.server.fastmcp import FastMCP
import math

# Create FastMCP server instance
mcp = FastMCP("Calculator Server")

# ⚙️ Tool definition: Add two numbers
@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

# ⚙️ Tool definition: Calculate square root
@mcp.tool()
def sqrt(number: float) -> float:
    """Calculate square root of a number"""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number!")
    return math.sqrt(number)

# 📚 Resource definition: Provide server info
@mcp.resource("calculator://info")
def server_info() -> str:
    """Return server information"""
    return """
    ⚙️ Calculator MCP Server

    Available functions:
    - add(a, b): Sum of two numbers
    - sqrt(number): Calculate square root

    Version: 1.0.0
    """

# 💬 Prompt definition: Calculation help
@mcp.prompt()
def calculate_help(operation: str) -> str:
    """Provide help for calculation tasks"""
    return f"""
    User requested {operation} calculation.

    Explain step by step while calculating:
    1. Verify input
    2. Perform calculation
    3. Explain result
    """

# Run server
if __name__ == "__main__":
    mcp.run()
```

### 3. Connect to Claude Desktop

Modify Claude Desktop configuration file:

```
// ~/Library/Application Support/Claude/claude_desktop_config.json (macOS)
// %APPDATA%\Claude\claude_desktop_config.json (Windows)
{
  "mcpServers": {
    "calculator": {
      "command": "python",
      "args": ["/path/to/calculator_server.py"]
    }
  }
}
```

## Building an MCP Server with TypeScript ⚙️

If you prefer TypeScript, you can build it like this:

```
// calculator-server.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

// Create server instance
const server = new Server({
  name: "calculator-server",
  version: "1.0.0",
}, {
  capabilities: {
    tools: {},
    resources: {}
  }
});

// ⚙️ Register Tool
server.setRequestHandler("tools/call", async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "add":
      return {
        content: [{
          type: "text",
          text: `Result: ${args.a + args.b}`
        }]
      };

    case "multiply":
      return {
        content: [{
          type: "text",
          text: `Result: ${args.a * args.b}`
        }]
      };

    default:
      throw new Error(`Unknown tool: ${name}`);
  }
});

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
```

## Advanced Example: Weather Information Server 🌤️

Let's create a more practical example that integrates with real APIs:

```
# weather_server.py
from mcp.server.fastmcp import FastMCP
import httpx
import asyncio

mcp = FastMCP("Weather Information Server")

# Define async tool
@mcp.tool()
async def get_weather(city: str) -> dict:
    """Get current weather for a city"""

    # Call OpenWeatherMap API (API key required in practice)
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "appid": "YOUR_API_KEY",
                "units": "metric",
                "lang": "en"
            }
        )

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    else:
        raise Exception(f"Cannot retrieve weather information: {city}")

# Define dynamic resource
@mcp.resource("weather://forecast/{city}")
async def weather_forecast(city: str) -> str:
    """Provide weather forecast for a city"""
    weather = await get_weather(city)

    return f"""
    🌤️ {weather['city']} Weather Information

    🌡️ Temperature: {weather['temperature']}°C
    ☁️ Condition: {weather['description']}
    💧 Humidity: {weather['humidity']}%
    💨 Wind Speed: {weather['wind_speed']}m/s
    """

if __name__ == "__main__":
    asyncio.run(mcp.run())
```

## Important Notes and Tips ⚠️

⚠️ **Key Points to Remember!**

1. **Prioritize security**
   - MCP servers can access your system, so only use trusted sources
   - Manage sensitive information with environment variables
   - Always validate input
2. **Handle errors carefully**
3. @mcp.tool() def safe_divide(a: float, b: float) -> float: """Safe division""" if b == 0: raise ValueError("Cannot divide by zero!") return a / b
4. **Use async processing**
   - Use async def for API calls and DB queries
   - Improve performance through concurrency

💡 **Pro Tips**

- **Use FastMCP**: Simpler and more Pythonic interface than official SDK
- **Leverage MCP Inspector**: GUI tool for server testing (mcp dev calculator_server.py)
- **Set up logging**: Enable file logging for debugging

  ```
  import logging
  logging.basicConfig(level=logging.DEBUG, filename='mcp_server.log')
  ```

## Conclusion 🎉

We've explored how to build MCP servers. Though it may seem complex at first, once you understand it, you can provide powerful tools to AI! 

Now create your own MCP server to make AI applications more powerful. Infinite possibilities await including file system access, database queries, and API integration! 🚀

Have questions? MCP is a rapidly evolving technology, so check the official documentation regularly!

## References 📚

- [Model Context Protocol Official Documentation](https://modelcontextprotocol.io/)
- [MCP Python SDK GitHub](https://github.com/modelcontextprotocol/python-sdk)
- [Awesome MCP Servers List](https://github.com/modelcontextprotocol/servers)

---

#MCP #ModelContextProtocol #AIToolDevelopment #Python #TypeScript
