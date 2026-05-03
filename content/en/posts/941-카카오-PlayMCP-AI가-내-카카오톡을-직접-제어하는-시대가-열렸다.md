---
title: "🎉 Kakao PlayMCP: The Era Where AI Directly Controls Your KakaoTalk"
date: 2025-12-19T21:05:28+09:00
slug: "941-카카오-PlayMCP-AI가-내-카카오톡을-직접-제어하는-시대가-열렸다"
original_url: "https://memoryhub.tistory.com/941"
tistory_id: 941
draft: false
categories: ["Dev Library"]
tags: ["MCP"]
  hidden: false
cover:
  image: "/images/941-카카오-PlayMCP-AI가-내-카카오톡을-직접-제어하는-시대가-열렸다/img.png"
  relative: false
  hidden: false
---

![](/images/941-카카오-PlayMCP-AI가-내-카카오톡을-직접-제어하는-시대가-열렸다/img.png)

"I asked AI to tell me today's schedule, and it told me to open the calendar app myself." Many have experienced this. No matter how smart an AI is, if it cannot access my calendar, my messages, or my music app, it cannot be a true 'assistant'. **Kakao's PlayMCP is Korea's first attempt to break down this wall.**

**To conclude upfront, PlayMCP is an open-source platform that allows AI to directly control Kakao services like KakaoTalk, Melon, and Calendar, and anyone with a Kakao account can use it or participate in development.**

---

## Background

The limitations of AI assistants were clear. Whether ChatGPT or Claude, no matter how well they converse, they couldn't handle requests like "leave a note in my KakaoTalk." This was because AI models and external services were speaking different 'languages'.

In November 2024, Anthropic announced MCP (Model Context Protocol) to solve this problem. Then in July 2025, Kakao became the first in Korea to beta-launch PlayMCP, an open-source platform based on MCP.

> **What is MCP (Model Context Protocol)?** It's a communication standard that standardizes how AI models communicate with external data or tools. Just like a single USB-C port connects various devices, MCP allows AI to access multiple services through one standard.

MCP has become the de facto standard in the AI industry. OpenAI officially adopted it in March 2025, and in December of the same year, Anthropic donated MCP to the Agentic AI Foundation under the Linux Foundation, making it an official open-source project with joint participation from OpenAI, Google, Microsoft, AWS, and others.

---

## PlayMCP's Core Features

PlayMCP's value is divided into two main areas: **Toolbox** for general users, and **MCP Server Registration and Testing Environment** for developers.

### Toolbox: Granting AI Access to Kakao Services

The Toolbox is the core feature of PlayMCP. Users can select desired MCP tools, manage them in one place, and use them with external AI services like ChatGPT or Claude.

The Kakao MCP servers currently available for testing are as follows:

| Service | Example Requests |
| --- | --- |
| KakaoTalk Chat with Me | "Send what you just told me to my chat room" |
| Talk Calendar | "Tell me my schedule for today" |
| Kakao Map | "Show me the route from home to work" |
| Gift Service | "Show me the gifts I received" |
| Melon | "Play the song I listened to today last year" |

**The key is 'one Kakao account authentication.'** You don't need to authenticate for each tool individually. With just one login, you can use all MCP tools in your Toolbox.

### Playground for Developers

Developers can register their MCP servers with PlayMCP and test how they work in actual AI conversations. They can also freely test MCP created by other developers, serving as a playground for experimenting with and expanding the agentic AI ecosystem together.

---

## Practice: Integrating PlayMCP Toolbox with ChatGPT/Claude

### ChatGPT Integration

1. **Access PlayMCP and Log In**  
   Go to playmcp.kakao.com and log in with your Kakao account.
2. **Configure Toolbox**  
   Add desired MCP tools (KakaoTalk, Melon, Calendar, etc.) to your Toolbox.
3. **Set ChatGPT Developer Mode**  
   Select 'Developer Mode' in ChatGPT, then register your custom MCP server URL.
4. **Authenticate Toolbox**  
   Authenticate your Toolbox with your Kakao account to complete integration.

### Claude Integration

1. **Configure Toolbox in PlayMCP**  
   Set up your Toolbox at playmcp.kakao.com in the same way.
2. **Enter Claude Settings**  
   Select 'Settings' in Claude.
3. **Connect Custom Connector**  
   Connect your PlayMCP Toolbox in 'Custom Connector' and authenticate with your Kakao account.

Once integration is complete, AI can directly handle requests like "Tell me today's schedule" or "Save this to my chat room."

---

## MCP Player 10 Contest: An Opportunity for Developers

Kakao officially announced 'MCP Player 10', a development contest for MCP, today (December 19, 2025). It's a contest to develop creative MCP servers using PlayMCP.

| Item | Details |
| --- | --- |
| Application Period | Until January 18, 2026 |
| Eligibility | Any developer |
| Evaluation Criteria | Creativity, Convenience, Technical Stability |
| Results Announcement | February 3, 2026 |

The total prize pool is 21 million won. 10 million won is awarded to 1st place, 3 million won to 2nd place, and 1 million won each to 8 third-place winners in Kakao Pay Points. In addition to the prizes, collaboration opportunities with Kakao services and marketing support are provided.

Participation is simple. Upload the MCP server you developed on PlayMCP, switch it to public, and apply on the contest page.

---

## Conclusion

- PlayMCP is Korea's first open-source platform based on MCP connecting AI and Kakao services
- With the Toolbox feature, general users can integrate and use Kakao services with ChatGPT and Claude
- By participating in the MCP Player 10 contest (~January 18, 2026), you can win prizes and collaboration opportunities with Kakao

**Practical tip:** Go to playmcp.kakao.com right now, add Talk Calendar to your Toolbox, and try asking Claude "Tell me today's schedule."

---

## References

- Kakao Official Press Release - PlayMCP Beta Launch (https://www.kakaocorp.com/page/detail/11674)
- AjuNews - Kakao Adds 'Toolbox' to PlayMCP (https://www.ajunews.com/view/20251124103701262)
- Edaily - Kakao Holds MCP Development Contest 'MCP Player 10' (https://edaily.co.kr/News/Read?mediaCodeNo=257&newsId=03588326642400160)
- Anthropic - Model Context Protocol Introduction (https://www.anthropic.com/news/model-context-protocol)
- PlayMCP Official Website (https://playmcp.kakao.com)
