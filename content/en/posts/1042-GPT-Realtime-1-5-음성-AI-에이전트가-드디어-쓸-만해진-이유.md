---
title: "GPT-Realtime-1.5: Why Voice AI Agents Are Finally Production-Ready"
date: 2026-02-25T21:39:45+09:00
slug: "1042-GPT-Realtime-1-5-음성-AI-에이전트가-드디어-쓸-만해진-이유"
original_url: "https://memoryhub.tistory.com/1042"
tistory_id: 1042
draft: false
---

```
  ╔══════════════════════════════════════════╗
  ║                                          ║
  ║   GPT-Realtime-1.5                       ║
  ║                                          ║
  ║   ┌──────────┐    ┌──────────────────┐   ║
  ║   │  Audio   │───>│  Speech-to-Speech │   ║
  ║   │  Input   │    │     Model         │   ║
  ║   └──────────┘    └────────┬─────────┘   ║
  ║                            │              ║
  ║         ┌──────────────────┼──────┐       ║
  ║         v                  v      v       ║
  ║   ┌──────────┐  ┌───────┐ ┌────────┐     ║
  ║   │  Audio   │  │ Text  │ │ Tools  │     ║
  ║   │  Output  │  │Output │ │ Calls  │     ║
  ║   └──────────┘  └───────┘ └────────┘     ║
  ║                                          ║
  ║   +5% Reasoning | +10% Transcription     ║
  ║   +7% Instruction Following              ║
  ║                                          ║
  ╚══════════════════════════════════════════╝
```

"I built an AI voice assistant, but it couldn't even follow half the instructions." This is a frustration many developers have experienced when deploying voice agents to production. When you connect separate speech recognition, text generation, and speech synthesis components, latency increases and nuance disappears. OpenAI's gpt-realtime-1.5, released on February 23, 2026, takes the answer to this problem up another notch.

**After reading this, you'll clearly understand what gpt-realtime-1.5 does differently from previous models and what it means for voice agent development.**

**One-liner summary:** In short, gpt-realtime-1.5 improves reasoning ability, alphanumeric recognition, and instruction following by 5-10% respectively, making voice AI agents truly usable in production environments.

---

## Background

Voice AI has undergone dramatic changes over the past two years. The previous approach was a pipeline structure connecting three separate stages: STT (speech-to-text conversion), LLM (text generation), and TTS (text-to-speech conversion). The problem stems from latency and information loss in this structure.

Non-linguistic signals like human laughter, intonation changes, and code-switching are lost during text conversion.

> An end-to-end speech model takes audio input, responds immediately with audio output, without intermediate text conversion.

OpenAI started this approach by releasing the Realtime API in beta in October 2024, officially launched (GA) gpt-realtime in August 2025. Then on February 23, 2026, released the further-advanced gpt-realtime-1.5.

But why "1.5"? If gpt-realtime was the first production-level model, 1.5 is a version that intensively improved real-world weaknesses that emerged—particularly instruction following, multilingual handling, and tool invocation stability.

Rather than fundamentally changing architecture, it strategically strengthened the points that generated the most complaints in actual deployments.

## GPT-Realtime Model Evolution

Let's understand where this model came from and where it's heading.

**gpt-4o-realtime-preview (October 2024)** was the first beta model of the Realtime API. It processed audio input/output based on WebSocket, but the audio output token price of $200 per million tokens made it burdensome to apply to actual services. Instruction following and tool invocation accuracy fell short of production standards.

**gpt-realtime (August 2025)** came with official release, dramatically lowered prices, and improved performance. It scored 82.8% on the Big Bench Audio inference benchmark, a 17.2 percentage point increase from the previous model (65.6%).

The MultiChallenge instruction following score rose from 20.6% to 30.5%, and the ComplexFuncBench tool invocation accuracy rose from 49.7% to 66.5%.

Features like SIP telephone connectivity, image input, and MCP server support were also added.

**gpt-realtime-1.5 (February 23, 2026)** improved three key metrics once more from there.

| Benchmark | Improvement vs gpt-realtime (2025.8) | Significance |
| --- | --- | --- |
| Big Bench Audio (Reasoning) | +5% | Enhanced speech-based reasoning for complex questions |
| Alphanumeric Recognition Accuracy | +10.23% | Accurate recognition of phone numbers, VIN, etc. |
| Instruction Following | +7% | Improved adherence to developer-set system prompts |

Looking at numbers alone, you might think "just 5-10%?" But there's a reason these figures matter. A 10% alphanumeric recognition error in a voice agent means getting 1 out of 10 phone numbers a customer recites wrong.

A 7% improvement in instruction following means "you must read the disclaimer" instructions are no longer ignored as often.

Actual responses from using companies back this up. Genspark reported that call connection success rates increased by nearly double to about 66%, and call errors were cut in half. Sendbird reported significantly improved interruption handling when users cut off speech.

## Core Features and Specifications

gpt-realtime-1.5's technical specifications are as follows:

**Input Modalities:** Text, audio, image. Image input is a feature supported from gpt-realtime (2025.8), allowing customers to send product photos and ask "what is this?" while receiving voice responses.

**Output Modalities:** Text, audio. Text-only mode is possible, but simultaneous text and audio output isn't supported.

**Context Window:** 32,000 tokens. Maximum output tokens are 4,096. While smaller than the 270,000 token context of GPT-5 series, this covers typical customer service sessions in real-time voice conversations adequately.

**Knowledge Cutoff:** September 30, 2024. This is identical to gpt-realtime and about a year earlier than GPT-5's cutoff.

**Connection Methods:** Supports all three: WebRTC, WebSocket, and SIP. SIP support is a key feature enabling direct integration with enterprise telephone systems, meaning you can connect AI voice agents directly to existing call center infrastructure.

**Voice Options:** In addition to the existing 8 voices (Alloy, Ash, Ballad, Coral, Echo, Sage, Shimmer, Verse), it supports 2 new voices: Cedar and Marin. Cedar and Marin are exclusive to the Realtime API. Custom voice IDs can also be used.

**Asynchronous Tool Invocation:** Long-running function calls don't interrupt conversation flow. For example, even if checking a reservation system takes 3 seconds, the model naturally continues conversation saying "just a moment, let me check." This feature has been built-in from gpt-realtime without requiring code modifications.

**Semantic VAD (Voice Activity Detection):** Instead of simple silence detection, it semantically determines the end of user speech. It distinguishes between pauses for thinking and completed utterances, reducing unnecessary interruptions.

## Pricing

Pricing remains identical to existing gpt-realtime. Same price, better performance.

| Token Type | Input (per 1M tokens) | Cached Input | Output (per 1M tokens) |
| --- | --- | --- | --- |
| Text | $4.00 | $0.40 | $16.00 |
| Audio | $32.00 | $0.40 | $64.00 |
| Image | $5.00 | $0.50 | - |

For reference, compared to the beta in October 2024 when audio output was $200 per million tokens, the current $64 is 68% cheaper. By actively utilizing prompt caching, you can significantly reduce costs for recurring system prompts.

There's a practical tip for cost optimization. The Realtime API supports fine-grained token limit settings for conversation context and multi-turn batching truncation. Cleaning up unnecessarily accumulated context in long sessions can significantly reduce costs.

## Practice: Realtime API Connection Basics

To use gpt-realtime-1.5, you must connect through the Realtime API.

Let's examine the simplest WebSocket connection flow step-by-step:

1. **Create Session**
   - Establish WebSocket connection to Realtime API endpoint (`/v1/realtime`)
   - Specify model as `gpt-realtime-1.5` in session configuration
   - Configure response modalities (audio or text), voice, VAD settings, etc.

2. **Configure System Prompt**
   - Pass system message via `session.update` event
   - gpt-realtime-1.5 responds better to detailed instructions. Even changing "inaudible" to "unintelligible" improves noise handling
   - Natural language (`escalate to agent after 3+ failures`) is more effective than conditionals (`IF x > 3 THEN ESCALATE`)

3. **Stream Audio**
   - Client transmits audio chunks in real-time
   - Server detects speech end with Semantic VAD or Server VAD
   - Model returns audio response via streaming

4. **Handle Tool Calls**
   - When model determines function call is needed, it triggers `mcp_tool_use` or function call event
   - Operates asynchronously, conversation continues while awaiting tool results
   - When results return, model reflects them in response

```
// Session configuration example (JavaScript)
const session = {
  model: "gpt-realtime-1.5",
  modalities: ["audio"],
  voice: "cedar",
  turn_detection: {
    type: "semantic_vad",
    eagerness: "medium"
  },
  tools: [
    {
      type: "function",
      name: "lookup_order",
      description: "Look up order status by order number",
      parameters: {
        type: "object",
        properties: {
          order_id: { type: "string" }
        },
        required: ["order_id"]
      }
    }
  ]
};
```

WebRTC connections suit browser-based applications, while SIP connections suit existing telephone infrastructure integration.

Choose the connection method that fits your use case.

## Best Practices/Pattern Comparison

Comparing approaches to consider when building voice agents:

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| gpt-realtime-1.5 alone | Lowest latency, preserves non-linguistic signals, natural multilingual switching | 32K context limit, knowledge cutoff September 2024 |
| STT + LLM + TTS pipeline | Freedom to choose model per stage, text intermediate processing possible | Increased latency, emotion/nuance loss, high integration complexity |
| Using gpt-realtime-mini | Cost reduction, low latency | Reasoning ability and instruction following accuracy lower than full-size model |
| Hybrid (simple→mini, complex→1.5) | Balance cost optimization and quality | Requires routing logic, complex session management during model switching |

gpt-realtime-1.5 is most suitable for customer service, telephone-based services, and voice agents requiring multilingual support.

Conversely, for simple announcement broadcasts or cost-sensitive bulk calling services, the mini model may be more practical.

## Conclusion

- gpt-realtime-1.5 improves reasoning (+5%), alphanumeric recognition (+10.23%), and instruction following (+7%), elevating voice agent production stability to the next level
- Pricing remains identical to gpt-realtime, so existing users can immediately experience performance improvements by just changing the model name
- With support for SIP, WebRTC, and MCP server integration, it applies broadly from enterprise telephone systems to web-based services
- Practical tip: If using gpt-realtime already, try changing the model parameter in session configuration to `gpt-realtime-1.5` and enabling Semantic VAD.

---

## References

- gpt-realtime-1.5 Official Documentation (<https://developers.openai.com/api/docs/models/gpt-realtime-1.5>)
- Realtime API Guide (<https://developers.openai.com/api/docs/guides/realtime/>)
- OpenAI Community Announcement: gpt-realtime-1.5 Launch (<https://community.openai.com/t/gpt-realtime-1-5-is-live-in-realtime-api/1374919>)
- gpt-realtime Introduction Blog (<https://openai.com/index/introducing-gpt-realtime/>)
- Microsoft Foundry Model Updates (<https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/new-azure-open-ai-models-bring-fast-expressive-and-real%E2%80%91time-ai-experiences-in-m/4496184>)
- OpenAI API Changelog (<https://platform.openai.com/docs/changelog>)
