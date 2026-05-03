---
title: "MCP (Model Context Protocol) Complete Mastery: The New Standard Connecting AI and Data!"
date: 2025-06-17T05:27:09+09:00
slug: "696-MCP-Model-Context-Protocol-완벽-정복-AI와-데이터를-연결하는-새로운-표준"
original_url: "https://memoryhub.tistory.com/696"
tistory_id: 696
draft: false
---

```
    ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
    │   Claude    │         │   GitHub    │         │   Slack     │
    │   🤖 AI     │         │   📊 Data   │         │   💬 Chat   │
    └──────┬──────┘         └──────┬──────┘         └──────┬──────┘
           │                       │                       │
           └───────────┬───────────┴───────────┬───────────┘
                       │                       │
                    ┌──▼───────────────────────▼──┐
                    │                             │
                    │    🌉 Model Context        │
                    │        Protocol (MCP)       │
                    │                             │
                    │  ╔═══════════════════════╗ │
                    │  ║  Standardized Bridge  ║ │
                    │  ║  for AI Connections   ║ │
                    │  ╚═══════════════════════╝ │
                    └─────────────────────────────┘
```

This morning, I asked Claude Desktop to read local files, but got "no access" message. Then after setting up an MCP server, everything magically worked!

While developing AI agents these past months, one thing always frustrated me: **"It's so difficult for AI to access real-time data or external tools."** 

A game-changer has arrived to solve this problem: **Model Context Protocol (MCP)**, open-sourced by Anthropic in November 2024!

⚡ **TL;DR**

- MCP = USB-C port for AI (standardized connection method)
- AI can access any data/tool without complex integration work

## Table of Contents

1. Background - Why MCP is Needed?
2. Core Concepts
3. Practice - Build MCP Server with TypeScript
4. Best Practices
5. Conclusion & References

---

## 1. Background - Why MCP is Needed?

Traditionally, for AI models to access external data or tools, custom integration work was required for each data source. Like how different manufacturers used different chargers in the early 2000s.

MCP is like providing USB-C port for AI applications. It enables connecting various peripherals and accessories in a standardized way.

### 🔑 Key Terminology

| Term | Description |
| --- | --- |
| **MCP Server** | Lightweight program providing data or tools |
| **MCP Client** | Application where AI communicates with server |
| **Resources** | Data exposed by server (works like GET endpoint) |
| **Tools** | Features provided by server (works like POST endpoint) |
| **Prompts** | Reusable LLM interaction templates |

## 2. Core Concepts

> **What is MCP?**  
> **An open protocol connecting AI models and external data/tools in a standardized way**

MCP follows client-server architecture, where one host can connect to multiple servers:

```
// Basic structure of MCP server
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new McpServer({
  name: "my-first-mcp-server",
  version: "1.0.0"
});

// Add tool - functionality AI can execute
server.tool(
  "calculate_sum",
  {
    description: "Add two numbers",
    inputSchema: {
      type: "object",
      properties: {
        a: { type: "number" },
        b: { type: "number" }
      }
    }
  },
  async ({ a, b }) => ({
    content: [{
      type: "text",
      text: `Result: ${a + b}`
    }]
  })
);

// Start server
const transport = new StdioServerTransport();
await server.connect(transport);
```

### Core Features

✅ **Bidirectional Communication**: AI not only receives information but can execute actions  
✅ **Security-First Design**: Host completely controls connection permissions  
✅ **Standardized Ecosystem**: All MCP-compatible models work with all MCP tools

## 3. Practice - Build MCP Server with TypeScript

### ① Project Setup

```
# Create project
mkdir my-mcp-server && cd my-mcp-server
npm init -y

# Install dependencies
npm install @modelcontextprotocol/sdk typescript zod
npm install -D @types/node ts-node

# Configure TypeScript
npx tsc --init
```

### ② Implement Basic Server

Create `src/index.ts` file:

```
#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// Create server instance
const server = new Server({
  name: "weather-mcp",
  version: "1.0.0"
}, {
  capabilities: {
    tools: {},     // Enable tool functionality
    resources: {}  // Enable resource functionality
  }
});

// Add weather query tool
server.tool({
  name: "get_weather",
  description: "Query weather for specific city",
  inputSchema: z.object({
    city: z.string().describe("City name to query weather")
  }),
  handler: async ({ city }) => {
    // Normally call weather API, but return mock data here
    const mockWeather = {
      city: city,
      temperature: Math.floor(Math.random() * 30) + 10,
      condition: ["Clear", "Cloudy", "Rainy", "Snowy"][Math.floor(Math.random() * 4)]
    };

    return {
      content: [{
        type: "text",
        text: `Weather in ${city}: ${mockWeather.temperature}°C, ${mockWeather.condition}`
      }]
    };
  }
});

// Start server
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCP server started!");
}

main().catch(console.error);
```

### ③ Connect to Claude Desktop

Modify Claude Desktop's configuration file:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```
{
  "mcpServers": {
    "weather": {
      "command": "node",
      "args": ["/path/to/your/my-mcp-server/dist/index.js"]
    }
  }
}
```

## 4. Best Practices

| Pattern | Advantage | Caution |
| --- | --- | --- |
| **Single Responsibility for Tools** | Each tool performs one clear function | Complex tasks split into multiple tools |
| **Schema Validation** | Validate input with Zod etc. | Prevent runtime errors |
| **Error Handling** | Return clear error messages | Enable users to understand and fix problems |
| **Human-in-the-loop** | Request user approval for important tasks | Improve security and reliability |

### Real-World Use Cases

Companies like Block and Apollo have already integrated MCP, and development tool companies like Zed, Replit, Codeium, and Sourcegraph are adopting MCP.

```
// Common pattern in practice: database connection
server.tool({
  name: "query_database",
  description: "Execute SQL query",
  inputSchema: z.object({
    query: z.string().describe("SQL query to execute")
  }),
  handler: async ({ query }) => {
    // Validation logic allowing read-only queries only
    if (!query.toLowerCase().startsWith("select")) {
      throw new Error("Only read-only queries allowed");
    }

    // DB query execution logic...
  }
});
```

## 5. Conclusion

- **Learned**: MCP acts as standardized bridge connecting AI and external world
- **Core Value**: MCP server built once works with all compatible AI models
- **Future Outlook**: MCP becomes the USB-C of AI ecosystem, enabling more innovation

**Practical Application Tip**: Start with small tools and gradually expand. Security always comes first!

If this article helped, please give ❤️ heart and comment! Share your MCP server development experiences too!

---

### References

- [MCP Official Documentation](https://modelcontextprotocol.io)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)
- [Anthropic MCP Announcement Blog](https://www.anthropic.com/news/model-context-protocol)
- [Awesome MCP Servers Collection](https://github.com/modelcontextprotocol/awesome-mcp)

### Additional Reading

1. [Enterprise AI Integration Strategy Using MCP](https://www.vktr.com/ai-technology/inside-anthropics-model-context-protocol-mcp-the-new-ai-data-standard/)
2. [Using MCP Server in VS Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
3. [Build MCP Server Faster with FastMCP](https://github.com/punkpeye/fastmcp)
