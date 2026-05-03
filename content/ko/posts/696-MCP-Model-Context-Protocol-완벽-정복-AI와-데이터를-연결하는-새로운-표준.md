---
title: "? MCP(Model Context Protocol) 완벽 정복: AI와 데이터를 연결하는 새로운 표준!"
date: 2025-06-17T05:27:09+09:00
slug: "696-MCP-Model-Context-Protocol-완벽-정복-AI와-데이터를-연결하는-새로운-표준"
original_url: "https://memoryhub.tistory.com/696"
tistory_id: 696
draft: false
categories: ["데브 라이브러리"]
tags: ["MCP"]
---

```
    ┌─────────────┐         ┌─────────────┐         ┌─────────────┐
    │   Claude    │         │   GitHub    │         │   Slack     │
    │   ? AI     │         │   ? Data   │         │   ? Chat   │
    └──────┬──────┘         └──────┬──────┘         └──────┬──────┘
           │                       │                       │
           └───────────┬───────────┴───────────┬───────────┘
                       │                       │
                    ┌──▼───────────────────────▼──┐
                    │                             │
                    │    ? Model Context         │
                    │        Protocol (MCP)       │
                    │                             │
                    │  ╔═══════════════════════╗ │
                    │  ║  Standardized Bridge  ║ │
                    │  ║  for AI Connections   ║ │
                    │  ╚═══════════════════════╝ │
                    └─────────────────────────────┘
```

오늘 아침 Claude Desktop에서 로컬 파일 시스템을 읽어달라고 했더니 "접근할 수 없다"는 메시지를 받았어요. 그런데 MCP 서버를 설정하니까 마법처럼 모든 게 해결됐죠!

지난 몇 달간 AI 에이전트를 개발하면서 늘 답답했던 게 하나 있었습니다. 바로 **"AI가 실시간 데이터나 외부 도구에 접근하기 너무 어렵다"**는 점이었는데요.

이 문제를 해결할 게임체인저가 등장했습니다. 바로 Anthropic이 2024년 11월에 오픈소스로 공개한 **Model Context Protocol(MCP)**입니다!

⚡ **TL;DR**

- MCP = AI를 위한 USB-C 포트 (표준화된 연결 방식)
- 복잡한 통합 작업 없이 AI가 어떤 데이터/도구든 접근 가능

## 목차

1. 배경 - 왜 MCP가 필요한가?
2. 핵심 개념 정리
3. 실습 - TypeScript로 MCP 서버 만들기
4. 모범 사례·베스트 프랙티스
5. 마치며 & 참고자료

---

## 1. 배경 - 왜 MCP가 필요한가?

기존에 AI 모델이 외부 데이터나 도구에 접근하려면 각각의 데이터 소스마다 커스텀 통합 작업이 필요했습니다. 마치 2000년대 초반에 각 제조사마다 다른 충전기를 사용했던 것처럼요.

MCP는 AI 애플리케이션에 USB-C 포트를 제공하는 것과 같습니다. 표준화된 방식으로 다양한 주변기기와 액세서리를 연결할 수 있게 해주죠.

### ? 주요 용어 정리

| 용어 | 설명 |
| --- | --- |
| **MCP Server** | 데이터나 도구를 제공하는 경량 프로그램 |
| **MCP Client** | AI 모델이 서버와 통신하는 애플리케이션 |
| **Resources** | 서버가 노출하는 데이터 (GET 엔드포인트처럼 동작) |
| **Tools** | 서버가 제공하는 기능 (POST 엔드포인트처럼 동작) |
| **Prompts** | 재사용 가능한 LLM 상호작용 템플릿 |

## 2. 핵심 개념

> **MCP란?**  
> **AI 모델과 외부 데이터/도구를 표준화된 방식으로 연결하는 오픈 프로토콜**

MCP는 클라이언트-서버 아키텍처를 따르며, 하나의 호스트가 여러 서버에 연결할 수 있습니다:

```
// MCP 서버의 기본 구조
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const server = new McpServer({
  name: "나의-첫-MCP-서버",
  version: "1.0.0"
});

// 도구(Tool) 추가 - AI가 실행할 수 있는 기능
server.tool(
  "calculate_sum",
  {
    description: "두 숫자를 더합니다",
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
      text: `결과: ${a + b}`
    }]
  })
);

// 서버 시작
const transport = new StdioServerTransport();
await server.connect(transport);
```

### 핵심 특징

✅ **양방향 통신**: AI가 정보를 받기만 하는 게 아니라 액션도 실행 가능  
✅ **보안 중심 설계**: 호스트가 연결 권한을 완전히 제어  
✅ **표준화된 생태계**: 모든 MCP 호환 모델이 모든 MCP 도구와 작동

## 3. 실습 - TypeScript로 MCP 서버 만들기

### ① 프로젝트 설정

```
# 프로젝트 생성
mkdir my-mcp-server && cd my-mcp-server
npm init -y

# 의존성 설치
npm install @modelcontextprotocol/sdk typescript zod
npm install -D @types/node ts-node

# TypeScript 설정
npx tsc --init
```

### ② 기본 서버 구현

`src/index.ts` 파일을 만들어 봅시다:

```
#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

// 서버 인스턴스 생성
const server = new Server({
  name: "weather-mcp",
  version: "1.0.0"
}, {
  capabilities: {
    tools: {},     // 도구 기능 활성화
    resources: {}  // 리소스 기능 활성화
  }
});

// 날씨 조회 도구 추가
server.tool({
  name: "get_weather",
  description: "특정 도시의 날씨를 조회합니다",
  inputSchema: z.object({
    city: z.string().describe("날씨를 조회할 도시명")
  }),
  handler: async ({ city }) => {
    // 실제로는 날씨 API를 호출하겠지만, 여기서는 모의 데이터 반환
    const mockWeather = {
      city: city,
      temperature: Math.floor(Math.random() * 30) + 10,
      condition: ["맑음", "흐림", "비", "눈"][Math.floor(Math.random() * 4)]
    };

    return {
      content: [{
        type: "text",
        text: `${city}의 날씨: ${mockWeather.temperature}°C, ${mockWeather.condition}`
      }]
    };
  }
});

// 서버 시작
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("MCP 서버가 시작되었습니다!");
}

main().catch(console.error);
```

### ③ Claude Desktop에 연결

Claude Desktop의 설정 파일을 수정합니다:

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

## 4. 모범 사례·베스트 프랙티스

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **도구 단일 책임** | 각 도구는 하나의 명확한 기능만 수행 | 복잡한 작업은 여러 도구로 분리 |
| **스키마 검증** | Zod 등을 사용해 입력값 검증 | 런타임 에러 방지 |
| **에러 핸들링** | 명확한 에러 메시지 반환 | 사용자가 문제를 이해하고 해결 가능 |
| **Human-in-the-loop** | 중요한 작업은 사용자 승인 요구 | 보안과 신뢰성 향상 |

### 실제 활용 사례

Block, Apollo 같은 기업들이 이미 MCP를 시스템에 통합했고, Zed, Replit, Codeium, Sourcegraph 같은 개발 도구 회사들도 MCP를 도입하고 있습니다.

```
// 실무에서 자주 사용되는 패턴: 데이터베이스 연결
server.tool({
  name: "query_database",
  description: "SQL 쿼리 실행",
  inputSchema: z.object({
    query: z.string().describe("실행할 SQL 쿼리")
  }),
  handler: async ({ query }) => {
    // 읽기 전용 쿼리만 허용하는 검증 로직
    if (!query.toLowerCase().startsWith("select")) {
      throw new Error("읽기 전용 쿼리만 실행 가능합니다");
    }

    // DB 쿼리 실행 로직...
  }
});
```

## 5. 마치며

- **배운 점**: MCP는 AI와 외부 세계를 연결하는 표준화된 다리 역할을 합니다
- **핵심 가치**: 한 번 만든 MCP 서버는 모든 호환 AI 모델에서 사용 가능
- **미래 전망**: MCP가 AI 생태계의 USB-C가 되어 더 많은 혁신을 가능하게 할 것

**실제 프로젝트 적용 팁**: 작은 도구부터 시작해서 점진적으로 확장하세요. 보안은 항상 최우선!

이 글이 도움이 되셨다면 ❤️ 하트와 댓글로 응원해주세요! 여러분의 MCP 서버 개발 경험도 공유해주시면 감사하겠습니다.

---

### 참고자료

- [MCP 공식 문서](https://modelcontextprotocol.io)
- [MCP GitHub 저장소](https://github.com/modelcontextprotocol)
- [Anthropic MCP 발표 블로그](https://www.anthropic.com/news/model-context-protocol)
- [Awesome MCP 서버 모음](https://github.com/modelcontextprotocol/awesome-mcp)

### 추가 읽을거리

1. [MCP를 활용한 엔터프라이즈 AI 통합 전략](https://www.vktr.com/ai-technology/inside-anthropics-model-context-protocol-mcp-the-new-ai-data-standard/)
2. [VS Code에서 MCP 서버 사용하기](https://code.visualstudio.com/docs/copilot/chat/mcp-servers)
3. [FastMCP로 더 빠르게 MCP 서버 구축하기](https://github.com/punkpeye/fastmcp)
