---
title: "MCP (Model Context Protocol) - The Secret Key to Connect Smart AI with the World"
date: 2025-04-02T18:22:09+09:00
slug: "542-MCP-Model-Context-Protocol-똑똑한-AI-세상과-통하게-하는-비밀-열쇠"
original_url: "https://memoryhub.tistory.com/542"
tistory_id: 542
draft: false
categories: ["Dev Library"]
tags: ["Claude"]
cover:
  image: "/images/542-MCP-Model-Context-Protocol-똑똑한-AI-세상과-통하게-하는-비밀-열쇠/img.png"
  relative: false
  hidden: false
---

These days, AI is incredibly smart, right? But sometimes it feels like AI is trapped in its own world. For example, when you ask an AI chatbot "What's my schedule today?", it can't answer if it can't directly access your calendar app. It's like a brilliant scientist who doesn't speak any foreign language at all.

To solve this AI "communication problem," a company called Anthropic has come up with a brilliant solution called **MCP (Model Context Protocol)**. You can think of MCP as a **"universal communication helper"** or a **"standard USB port in the AI world"** that helps AI communicate freely with various external tools and data! This makes it easier to understand.

## Why Was It Needed? (Historical Background)

In the past, developers really struggled to connect AI with external services (Slack, databases, Google Calendar, etc.). They had to create separate connection programs for each service, and if something went wrong, they'd have to fix it again. It was like trying to build with LEGO blocks where each piece has a different shape. This took a lot of time, was hard to manage, and adding new services was even more difficult.

To solve this **"connection inconvenience"** and create **"standardized communication rules"** so AI could do more, MCP was born.

[Problems MCP Solves]:

1. **Complex connection tasks**: Instead of creating separate connection programs for each service, you just need to follow one MCP standard, making development much easier.
2. **Breaking down information barriers**: AI can easily access various databases and apps to find the information it needs.
3. **Expanding AI capabilities**: Beyond just retrieving information, AI can now use external tools directly to send emails, save files, and do other tasks.

## Core Principles: How Does It Work? ⚙️

How does MCP connect AI with the outside world? You can understand it through three core principles.

### 1. Dividing Roles: Client and Server

MCP works by dividing roles like a librarian and a library user.

- **Client (AI App)**: Acts like a library user requesting needed information or functions (books or services). This includes the AI chatbots and AI-based apps we use.
- **Server (Data/Tool Gateway)**: Acts like a librarian, receiving user requests, finding needed books (data), or providing specific services (tool execution). External services like databases, Slack, and Google Drive are wrapped according to MCP rules to serve as servers.
- **Communication Language**: They communicate using **JSON-RPC 2.0**, an easy and standardized protocol. It's like exchanging requests using a predetermined format.

[Client-Server Interaction]

![](/images/542-MCP-Model-Context-Protocol-똑똑한-AI-세상과-통하게-하는-비밀-열쇠/img.png)

### 2. Service Menu: Tools, Resources, Prompts

An MCP server provides functionalities that AI (client) can use like a "menu."

- **Tools**: Specific functions AI can request to do. (Example: `send message`, `search files`, `add schedule`)
- **Resources**: Data pieces AI can request. (Example: `specific customer information`, `recent email list`)
- **Prompts**: Guidelines or templates that help AI perform specific tasks better.

AI can look at this menu and request the functions or information it needs from the server.

### 3. Automatic Notifications: Dynamic Discovery

You don't need to manually tell AI about every new tool or service! MCP clients can **automatically detect** what MCP servers (services) are nearby and what new features (tools, resources) they provide. It's like a librarian announcing "New books arrived!" Thanks to this, AI can always use the latest features.

## So What Can It Do? (Case Studies)

Thanks to MCP, AI can be a much more useful and intelligent assistant!

- **Quick-witted Secretary**: "Share last month's team performance report on Slack." → AI finds the report from the internal database (MCP server) and sends a message on Slack (MCP server).
- **Development Assistant**: "Commit and push what I just worked on to Git." → AI communicates with Git (MCP server) to execute commands.
- **Real-time Analyst**: Analyzes stock market data in real-time (MCP server) and immediately sends an alert when an anomalous pattern is detected.
- **Personalized AI**: Safely accesses files or emails on your computer (local MCP server) without sending them externally to handle requests like "Find the contract draft I received yesterday."

**The Difference With and Without MCP!**

| **Feature** | **Before MCP (Difficult times)** | **After MCP (Convenient world)** |
| --- | --- | --- |
| **Connection Method** | Different for each service, complex | Unified with one standard (MCP) |
| **Development** | Hard work and difficult maintenance | Easy and simple! |
| **Scalability** | Adding a new service? Develop again... | Just add a new MCP server! |
| **Feature Discovery** | Developer must manually inform | AI detects automatically! |
| **AI Role** | Mainly information retrieval | Information retrieval + actual actions! |

## Important Considerations & Pro Tips

⚠️ **Be Careful About:**

1. **Still Growing**: MCP is a relatively new technology, so not all services or AI platforms may support it immediately. You need to check if your environment supports it.
2. **Security is Critical**: An MCP server is like a gateway to important data and functions. You must properly manage passwords (authentication) and access rights so unauthorized users can't enter!

💡 **Pro Tips!**

- **Use Official Tools**: Using the SDK (development toolkit) provided by Anthropic makes it easier to build MCP features. (Supports Python, TypeScript, Java, etc.)
- **Try Following Examples**: Following examples on the MCP official site (modelcontextprotocol.io) or GitHub helps you get a feel for it.
- **MCP is a 'Connection Expert'**: MCP itself isn't an AI brain (agent framework), but rather acts like a "neural network" helping the brain use its limbs (external tools) well. It becomes even more powerful when used with other AI technologies!

## Conclusion

MCP is one of the key technologies that allows AI to go beyond being simply a smart conversation partner and help us more deeply in our actual work and life. I look forward to a future where AI communicates freely with the outside world and shows more possibilities, with MCP opening that door wide!

If you have any other questions about MCP, feel free to ask!

## References

- **MCP Official GitHub**: [https://github.com/modelcontextprotocol](https://github.com/modelcontextprotocol)
- **MCP Official Documentation**: [https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
- **(Blog) What is the Trending 'MCP'? - Yozm**: [https://yozm.wishket.com/magazine/detail/3041/](https://yozm.wishket.com/magazine/detail/3041/)
- **(Blog) What is MCP (Model Context Protocol)? - DEV.DY**: [https://dytis.tistory.com/112](https://dytis.tistory.com/112)

#MCP #ModelContextProtocol #Anthropic #AI #LLM #API_Integration #OpenProtocol #AI_Agent
