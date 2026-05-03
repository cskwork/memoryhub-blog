---
title: "Model Context Protocol (MCP) - 나만의 AI 도구 서버 만들기 완전 정복 ?"
date: 2025-06-01T10:56:24+09:00
slug: "627-Model-Context-Protocol-MCP-나만의-AI-도구-서버-만들기-완전-정복"
original_url: "https://memoryhub.tistory.com/627"
tistory_id: 627
draft: false
---

여러분, AI 챗봇이 파일을 읽고, 데이터베이스를 조회하고, API를 호출할 수 있다면 어떨까요? ? 바로 이런 마법같은 일을 가능하게 해주는 것이 \*\*Model Context Protocol (MCP)\*\*입니다! 오늘은 여러분만의 MCP 서버를 만드는 방법을 A부터 Z까지 알아보겠습니다.

## 등장 배경 ?

과거에는 AI 모델과 외부 도구를 연결하려면 어땠을까요?

**2024년 이전**:

- 각 AI 애플리케이션마다 별도의 커스텀 통합 구현 필요 ?
- M개의 AI 앱 × N개의 도구 = M×N개의 통합 작업
- 중복된 코드, 일관성 없는 구현, 유지보수의 악몽

**2024년 11월 이후** (MCP 등장):

- Anthropic이 오픈 소스로 공개한 표준 프로토콜 ?
- USB-C처럼 하나의 표준으로 모든 연결 가능
- M+N개의 작업으로 감소!

MCP가 해결하는 주요 문제들:

1. **데이터 사일로 문제**: AI가 격리된 데이터에 접근 불가
2. **통합의 복잡성**: 각 도구마다 다른 API와 인증 방식
3. **확장성 부족**: 새로운 도구 추가시마다 전체 시스템 수정 필요

## 핵심 원리 ?

MCP는 클라이언트-서버 아키텍처로 동작합니다. 마치 웹 서버가 브라우저의 요청에 응답하듯이, MCP 서버는 AI 애플리케이션의 요청에 응답합니다.

### 주요 구성 요소

구성 요소 역할 예시

|  |  |  |
| --- | --- | --- |
| **Host** ? | MCP 클라이언트를 관리하는 애플리케이션 | Claude Desktop, VS Code, Cursor |
| **Client** ? | 서버와 1:1 연결을 유지하는 프로토콜 핸들러 | Host 내부의 연결 관리자 |
| **Server** ⚙️ | 특정 기능을 노출하는 경량 프로그램 | 파일 시스템 서버, DB 서버, API 서버 |

### MCP가 제공하는 3가지 핵심 기능

```
┌─────────────────────────────────────┐
│           MCP Server                │
├─────────────────────────────────────┤
│  ?️  Tools (도구)                    │
│  ? Resources (리소스)               │  
│  ? Prompts (프롬프트)               │
└─────────────────────────────────────┘
```

1. **Tools** ?️: AI가 실행할 수 있는 함수들
   - 예: get\_weather(), send\_email(), query\_database()
2. **Resources** ?: AI가 읽을 수 있는 데이터
   - 예: 파일 내용, API 응답, 데이터베이스 레코드
3. **Prompts** ?: 사전 정의된 템플릿
   - 예: "이 코드를 리뷰해주세요", "데이터를 요약해주세요"

## Python으로 MCP 서버 만들기 ?

자, 이제 실제로 만들어봅시다! 계산기 기능을 제공하는 간단한 MCP 서버를 구현해보겠습니다.

### 1. 환경 설정

```
# 프로젝트 디렉토리 생성
mkdir my-mcp-server
cd my-mcp-server

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 필요한 패키지 설치
pip install "mcp[cli]"
```

### 2. 기본 서버 구현

```
# calculator_server.py
from mcp.server.fastmcp import FastMCP
import math

# FastMCP 서버 인스턴스 생성
mcp = FastMCP("계산기 서버")

# ?️ Tool 정의: 두 수를 더하는 함수
@mcp.tool()
def add(a: float, b: float) -> float:
    """두 숫자를 더합니다"""
    return a + b

# ?️ Tool 정의: 제곱근 계산
@mcp.tool()
def sqrt(number: float) -> float:
    """숫자의 제곱근을 계산합니다"""
    if number < 0:
        raise ValueError("음수의 제곱근은 계산할 수 없습니다!")
    return math.sqrt(number)

# ? Resource 정의: 서버 정보 제공
@mcp.resource("calculator://info")
def server_info() -> str:
    """서버 정보를 반환합니다"""
    return """
    ? 계산기 MCP 서버

    사용 가능한 기능:
    - add(a, b): 두 수의 합
    - sqrt(number): 제곱근 계산

    버전: 1.0.0
    """

# ? Prompt 정의: 계산 도움말
@mcp.prompt()
def calculate_help(operation: str) -> str:
    """계산 작업에 대한 도움말을 제공합니다"""
    return f"""
    사용자가 {operation} 연산을 요청했습니다.

    단계별로 설명하면서 계산해주세요:
    1. 입력값 확인
    2. 연산 수행
    3. 결과 설명
    """

# 서버 실행
if __name__ == "__main__":
    mcp.run()
```

### 3. Claude Desktop에 연결하기

Claude Desktop 설정 파일을 수정합니다:

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

## TypeScript로 MCP 서버 만들기 ?

TypeScript를 선호하신다면 이렇게 만들 수 있습니다:

```
// calculator-server.ts
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

// 서버 인스턴스 생성
const server = new Server({
  name: "calculator-server",
  version: "1.0.0",
}, {
  capabilities: {
    tools: {},
    resources: {}
  }
});

// ?️ Tool 등록
server.setRequestHandler("tools/call", async (request) => {
  const { name, arguments: args } = request.params;

  switch (name) {
    case "add":
      return {
        content: [{
          type: "text",
          text: `결과: ${args.a + args.b}`
        }]
      };

    case "multiply":
      return {
        content: [{
          type: "text",
          text: `결과: ${args.a * args.b}`
        }]
      };

    default:
      throw new Error(`Unknown tool: ${name}`);
  }
});

// 서버 시작
const transport = new StdioServerTransport();
await server.connect(transport);
```

## 고급 예제: 날씨 정보 서버 ?️

실제 API와 연동하는 더 실용적인 예제를 만들어보겠습니다:

```
# weather_server.py
from mcp.server.fastmcp import FastMCP
import httpx
import asyncio

mcp = FastMCP("날씨 정보 서버")

# 비동기 도구 정의
@mcp.tool()
async def get_weather(city: str) -> dict:
    """도시의 현재 날씨를 가져옵니다"""

    # OpenWeatherMap API 호출 (실제로는 API 키 필요)
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "appid": "YOUR_API_KEY",
                "units": "metric",
                "lang": "ko"
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
        raise Exception(f"날씨 정보를 가져올 수 없습니다: {city}")

# 동적 리소스 정의
@mcp.resource("weather://forecast/{city}")
async def weather_forecast(city: str) -> str:
    """도시의 날씨 예보를 제공합니다"""
    weather = await get_weather(city)

    return f"""
    ?️ {weather['city']} 날씨 정보

    ?️ 온도: {weather['temperature']}°C
    ☁️ 상태: {weather['description']}
    ? 습도: {weather['humidity']}%
    ? 풍속: {weather['wind_speed']}m/s
    """

if __name__ == "__main__":
    asyncio.run(mcp.run())
```

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **보안을 최우선으로**
   - MCP 서버는 시스템에 접근할 수 있으므로 신뢰할 수 있는 소스만 사용
   - 민감한 정보는 환경 변수로 관리
   - 입력값 검증 필수
2. **에러 처리를 꼼꼼히**
3. @mcp.tool() def safe\_divide(a: float, b: float) -> float: """안전한 나눗셈""" if b == 0: raise ValueError("0으로 나눌 수 없습니다!") return a / b
4. **비동기 처리 활용**
   - API 호출이나 DB 쿼리는 async def 사용
   - 동시성을 통한 성능 향상

? **꿀팁**

- **FastMCP 사용하기**: 공식 SDK보다 간단하고 Pythonic한 인터페이스 제공
- **MCP Inspector 활용**: 서버 테스트를 위한 GUI 도구 (mcp dev calculator\_server.py)
- **로깅 설정**: 디버깅을 위해 파일 로깅 활성화

  ```
  import logginglogging.basicConfig(level=logging.DEBUG, filename='mcp_server.log')
  ```

## 마치며 ?

지금까지 MCP 서버를 만드는 방법에 대해 알아보았습니다. 처음에는 복잡해 보일 수 있지만, 한 번 이해하고 나면 AI에게 강력한 도구를 제공할 수 있는 훌륭한 방법입니다!

이제 여러분만의 MCP 서버를 만들어 AI 애플리케이션을 더욱 강력하게 만들어보세요. 파일 시스템 접근, 데이터베이스 쿼리, API 통합 등 무한한 가능성이 기다리고 있습니다! ?

궁금한 점이 있으신가요? MCP는 빠르게 발전하는 기술이니 공식 문서를 자주 확인하시는 것을 추천드립니다!

## 참고 자료 ?

- [Model Context Protocol 공식 문서](https://modelcontextprotocol.io/)
- [MCP Python SDK GitHub](https://github.com/modelcontextprotocol/python-sdk)
- [Awesome MCP Servers 목록](https://github.com/modelcontextprotocol/servers)

---

#MCP #ModelContextProtocol #AI도구개발 #Python #TypeScript
