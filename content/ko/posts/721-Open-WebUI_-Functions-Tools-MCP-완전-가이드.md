---
title: "Open WebUI: Functions, Tools, MCP 완전 가이드"
date: 2025-07-08T23:40:15+09:00
slug: "721-Open-WebUI_-Functions-Tools-MCP-완전-가이드"
original_url: "https://memoryhub.tistory.com/721"
tistory_id: 721
draft: false
---

Open WebUI는 **자체 호스팅 가능한 AI 플랫폼**으로, Ollama 및 OpenAI 호환 API를 지원하는 확장 가능하고 사용자 친화적인 웹 인터페이스입니다[1][2]. 완전 오프라인 환경에서도 작동할 수 있도록 설계되었으며, 다양한 LLM(Large Language Model)과의 원활한 통합을 제공합니다[3][4]. 이 플랫폼은 ChatGPT와 유사한 사용자 경험을 오픈소스로 제공하면서도, 개인정보 보호와 커스터마이징 가능성을 동시에 보장합니다[5][6].

## Open WebUI의 핵심 개념

### 플랫폼의 주요 특징

Open WebUI는 **웹 기반 상호작용**을 통해 다수의 사용자가 동시에 LLM을 사용할 수 있는 환경을 제공합니다[2]. 이 플랫폼의 핵심 강점은 **확장성과 모듈화**에 있으며, 사용자는 Functions, Tools, MCP(Model Context Protocol) 등 다양한 방법으로 기능을 확장할 수 있습니다[7][8].

### 지원하는 주요 기능

- **다양한 모델 지원**: Ollama, OpenAI, Anthropic, Google Gemini 등[5][9]
- **RAG(Retrieval Augmented Generation) 통합**: 문서 기반 검색 증강 생성[4][6]
- **실시간 웹 검색**: SearXNG, Google PSE, Brave Search, DuckDuckGo 등 다양한 검색 엔진 지원[10][6]
- **음성 및 영상 통화**: 핸즈프리 음성/영상 통화 기능[4][11]
- **이미지 생성 통합**: AUTOMATIC1111 API, ComfyUI, OpenAI DALL-E 지원[4]

## Functions, Tools, MCP 상세 비교

### Functions (함수)

Functions는 **Open WebUI 자체의 기능을 확장하는 플러그인** 시스템입니다[7][12]. 이들은 Open WebUI 서버 내부에서 직접 실행되며, 플랫폼의 핵심 동작을 수정하거나 새로운 기능을 추가할 수 있습니다.

#### Functions의 세 가지 유형

1. **Pipe Functions**: 사용자 정의 "모델"이나 "에이전트"를 생성하여 인터페이스에서 독립적인 모델처럼 나타납니다[7]
2. **Filter Functions**: 입력 및 출력 메시지를 처리하는 미들웨어 역할을 수행합니다[7][12]
3. **Action Functions**: 개별 채팅 메시지에 클릭 가능한 버튼을 추가합니다[7]

#### Functions 활용 사례

- 새로운 AI 모델 제공업체(Anthropic, Vertex AI) 지원 추가
- 메시지 필터링 및 조작
- 사용자 정의 인터페이스 요소 생성
- 사용량 모니터링 및 실시간 번역[12]

### Tools (도구)

Tools는 **LLM이 요청 시점에 실행할 수 있는 Python 스크립트**입니다[13][14]. 이들은 대화 중에 LLM이 필요에 따라 호출할 수 있는 외부 기능을 제공하며, 실시간 데이터 검색과 API 상호작용을 가능하게 합니다.

#### Tools의 특징

- **실시간 실행**: LLM 요청 시에만 실행됩니다[15][14]
- **함수 호출 지원**: LLM이 function calling을 지원해야 효과적으로 사용 가능합니다[13][14]
- **모듈화된 설계**: 각 도구는 독립적으로 설치하고 관리할 수 있습니다[16][15]

#### Tools 활용 사례

- 웹 검색 및 스크래핑
- 날씨 정보 및 주식 가격 조회
- 이미지 생성 및 처리
- 데이터베이스 쿼리 실행[13][14]

### MCP (Model Context Protocol)

MCP는 **AI 모델과 외부 데이터 소스 및 도구를 연결하는 개방형 표준 프로토콜**입니다[17][18]. Anthropic이 2024년 11월에 공개한 이 프로토콜은 AI 생태계의 "USB-C 포트"와 같은 역할을 수행합니다[18][19].

#### MCP의 핵심 아키텍처

MCP는 **클라이언트-서버 구조**를 따르며, JSON-RPC 2.0 메시지 포맷을 사용합니다[17][20]. 주요 구성 요소는 다음과 같습니다:

- **MCP 호스트**: AI 모델을 운용하는 주체 애플리케이션
- **MCP 클라이언트**: 호스트 내부에서 MCP 서버와 1:1 연결을 담당
- **MCP 서버**: 외부 데이터나 기능을 제공하는 경량 프로그램[19][20]

#### MCP의 표준화된 기능

1. **Resources**: 외부 데이터를 읽는 기능 (예: 시장 상태 확인)[21]
2. **Tools**: 작업을 실행하는 기능 (예: 데이터베이스 업데이트)[21]
3. **Prompts**: AI 모델이 사용할 템플릿 프롬프트[21]

## 설치 및 설정 가이드

### 기본 설치 방법

Open WebUI는 여러 가지 설치 방법을 제공합니다[3][22][23]:

#### Docker를 통한 설치

```
# 기본 설치
docker run -d -p 3000:8080 --name open-webui --restart always ghcr.io/open-webui/open-webui:main

# GPU 지원 설치
docker run -d -p 3000:8080 --gpus all --name open-webui --restart always ghcr.io/open-webui/open-webui:cuda
```

#### pip를 통한 설치

```
pip install open-webui
open-webui serve
```

### Functions 설정 방법

Functions는 관리자 권한이 필요하며, 다음 단계를 통해 설정할 수 있습니다[7][8]:

1. **관리자 패널 접근**: `워크스페이스` → `Functions` 선택
2. **새 함수 추가**: 커뮤니티에서 가져오거나 직접 개발
3. **함수 활성화**: 전역적으로 또는 특정 모델에만 할당

### Tools 설정 방법

Tools는 더 간단한 설정 과정을 가집니다[15][14]:

1. **도구 설치**: `워크스페이스` → `Tools`에서 커뮤니티 도구 가져오기
2. **모델 할당**: `워크스페이스` → `Models`에서 원하는 모델에 도구 할당
3. **채팅 중 활용**: 채팅 창에서 '+' 아이콘을 통해 도구 활성화

### MCP 설정 방법

MCP는 가장 복잡한 설정 과정을 요구합니다[24][25][26]:

1. **MCP 서버 구현**: Python 또는 TypeScript로 MCP 서버 개발
2. **MCPO 설치**: MCP-to-OpenAPI 프록시 서버 설치

   ```
   uvx mcpo --port 8000 --api-key "top-secret" -- your_mcp_server_command
   ```
3. **Open WebUI 연결**: 설정에서 도구 서버로 MCPO 엔드포인트 추가

## 실제 사용 사례와 활용 방안

### 개인 사용자 활용

개인 사용자들은 주로 **로컬 LLM 채팅, 문서 요약, 코드 생성, 개인 지식 관리** 등의 목적으로 Open WebUI를 활용합니다[5][11]. 특히 오프라인 환경에서의 AI 모델 사용이 가능하다는 점이 개인정보 보호 측면에서 큰 장점을 제공합니다[4][6].

### 기업 환경에서의 활용

기업 사용자들은 **내부 데이터 활용, 업무 자동화, 고객 서비스, 보안 강화** 등을 위해 Open WebUI를 도입합니다[27]. 특히 Block, Apollo 등의 기업들이 MCP를 활용하여 내부 시스템과 AI 에이전트를 통합하고 있습니다[18].

### 개발자 및 연구자 활용

개발자들은 **API 통합, 커스텀 도구 개발, 모델 실험, 프로토타입 제작**을 위해 Open WebUI를 활용하며[23], 연구자들은 **연구 데이터 분석, 논문 작성 지원, 실험 자동화, 지식 베이스 구축** 등의 용도로 사용합니다[27].

## 성능 최적화 및 보안 고려사항

### 성능 최적화 전략

Open WebUI의 성능을 최적화하기 위해서는 **GPU 지원 활성화, 적절한 모델 선택, 메모리 관리** 등이 중요합니다[9][23]. 특히 대용량 모델 사용 시에는 최소 16GB RAM과 충분한 저장 공간이 필요합니다[9].

### 보안 및 개인정보 보호

Open WebUI는 **완전 오프라인 작동, 로컬 데이터 처리, 사용자 권한 관리** 등을 통해 강력한 보안을 제공합니다[1][4]. MCP 또한 **사용자 동의와 제어를 최우선**으로 하는 보안 중심 설계를 채택하고 있습니다[17].

## 결론 및 향후 전망

Open WebUI는 AI 기술의 민주화를 위한 강력한 플랫폼으로, Functions, Tools, MCP라는 세 가지 확장 메커니즘을 통해 다양한 요구사항을 충족할 수 있습니다. **Functions는 플랫폼 자체의 기능 확장에**, **Tools는 실시간 LLM 기능 향상에**, **MCP는 복잡한 외부 시스템 통합에** 각각 최적화되어 있습니다.

특히 MCP의 등장은 AI 생태계의 표준화에 중요한 이정표를 제시하며, 향후 다양한 AI 플랫폼 간의 상호 운용성을 크게 향상시킬 것으로 전망됩니다[18][27]. Open WebUI와 같은 오픈소스 플랫폼의 지속적인 발전은 AI 기술의 접근성을 높이고, 개인과 기업 모두에게 맞춤형 AI 솔루션을 구축할 수 있는 기회를 제공할 것입니다.

## 출처

[1] open-webui/open-webui <https://github.com/open-webui/open-webui>  
[2] Open WebUI: Home <https://docs.openwebui.com>  
[3] Open WebUI 설치와 운영 : AI 모델 활용을 위한 오픈소스 웹 인터페이스 <https://blog.oriang.net/69>  
[4] Open-WebUI: 실시간 웹 검색과 개인 메모리 기능을 갖춘 LLM 실행기 <https://fornewchallenge.tistory.com/entry/Open-WebUI-%F0%9F%94%8D%EC%8B%A4%EC%8B%9C%EA%B0%84-%EC%9B%B9-%EA%B2%80%EC%83%89%EA%B3%BC-%EA%B0%9C%EC%9D%B8-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EA%B8%B0%EB%8A%A5%EC%9D%84-%EA%B0%96%EC%B6%98-LLM-%EC%8B%A4%ED%96%89%EA%B8%B0>  
[5] Getting Started | Open WebUI <https://docs.openwebui.com/getting-started/>  
[6] Open WebUI 프레임워크 소개 - 속도 < 방향 - 티스토리 <https://maxo.tistory.com/134>  
[7] Open WebUI , 오프라인 및 Local LLM 등을 위한 오픈소스 AI 플랫폼 <https://discuss.pytorch.kr/t/open-webui-local-llm-ai/5964>  
[8] openwebui · GitHub Topics <https://github.com/topics/openwebui>  
[9] Open WebUI: 사용자 친화적인 AI 인터페이스 솔루션 - 기본 설치 방법 <https://digitalbourgeois.tistory.com/685>  
[10] 019 Open WebUI Channels - 바이브 코딩(Vibe Coding) - 위키독스 <https://wikidocs.net/279054>  
[11] OPEN WebUI 이란 무엇인가? - MSAP.ai <https://www.msap.ai/blog/open-webui-llm-platform/>  
[12] GitHub - Open WebUI <https://open-webui.com/github/>  
[13] Ollama와 Open WebUI 사용법 - Apidog <https://apidog.com/kr/blog/open-webui-ollama-kr/>  
[14] If you haven't checked out the Open WebUI Github in a couple of ... <https://www.reddit.com/r/LocalLLaMA/comments/1df1zjr/if_you_havent_checked_out_the_open_webui_github/>  
[15] 2. Open-WebUI : 모델 추가하고 사용해 보기 <https://toyourlight.tistory.com/124>  
[16] ollama-webui · GitHub Topics <https://github.com/topics/ollama-webui>  
[17] OpenWebUI 사용해보기 <https://velog.io/@martin-han/OpenWebUI-%EC%82%AC%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B0>  
[18] [Open WebUI] 소개 및 설치하기 (Ollama, llama3 LLM) - YouTube <https://www.youtube.com/watch?v=lTOhY-RuKrI>  
[19] Msty와 Open WebUI: 직관적인 UI와 로컬 RAG까지 지원하는 언어 ... <https://fornewchallenge.tistory.com/entry/Msty%EC%99%80-Open-WebUI-%EC%A7%81%EA%B4%80%EC%A0%81%EC%9D%B8-UI%EC%99%80-%EB%A1%9C%EC%BB%AC-RAG%EA%B9%8C%EC%A7%80-%EC%A7%80%EC%9B%90%ED%95%98%EB%8A%94-%EC%96%B8%EC%96%B4-%EB%AA%A8%EB%8D%B8-%ED%99%9C%EC%9A%A9-%EB%8F%84%EA%B5%AC>  
[20] Functions | Open WebUI <https://docs.openwebui.com/features/plugin/functions/>  
[21] Functions | Open WebUI <https://docs.openwebui.com/pipelines/functions/>  
[22] GitHub - GewoonJaap/open-webui-tools: Tools for open webui <https://github.com/GewoonJaap/open-webui-tools>  
[23] Open-WebUI Functions, Tools, Pipelines, and Instructions - GitHub <https://github.com/BrandXX/open-webui>  
[24] Python Code Execution - Open WebUI <https://docs.openwebui.com/features/code-execution/python/>  
[25] Getting Started with Open WebUI: A Self-Hosted AI Interface <https://dev.to/vpjigin/getting-started-with-open-webui-a-self-hosted-ai-interface-53da>  
[26] Functions - Open WebUI <https://open-webui.com/functions/>  
[27] Tools | Open WebUI <https://docs.openwebui.com/features/plugin/tools/>  
[28] Tools & Functions | Open WebUI <https://docs.openwebui.com/features/plugin/>  
[29] Open WebUI-Tool Use with 3 Demos for Beginners and Advance Users <https://www.youtube.com/watch?v=-Ev773G3CoQ>  
[30] owndev/Open-WebUI-Functions - GitHub <https://github.com/owndev/Open-WebUI-Functions>  
[31] GitHub - suurt8ll/open\_webui\_functions: My collection of helper functions for Open WebUI. <https://github.com/suurt8ll/open_webui_functions>  
[32] Exploring Open WebUI: Features, Models, & Tools [Updated] <https://www.youtube.com/watch?v=CDiVq3mPZc8>  
[33] Tools - Open WebUI <https://open-webui.com/tools/>  
[34] Openwebui Complete Tutorial | Tests - Function Tool Model Prompt <https://www.youtube.com/watch?v=8g_r_G_niEs>  
[35] GitHub - taylorwilsdon/open-webui-tools: Tools for Open-WebUI <https://github.com/taylorwilsdon/open-webui-tools>  
[36] Open WebUI, Tools, Functions, Filters, Pipelines, and Valves, with a ... <https://www.youtube.com/watch?v=Jxt-coDVbR4>  
[37] a Repository of Open-WebUI tools to use with your favourite LLMs <https://github.com/Haervwe/open-webui-tools>  
[38] 1\_정의와목적 - Model Context Protocol (MCP) Anthropic 개발 방법 <https://wikidocs.net/268792>  
[39] Open WebUI - MCP fetch 체험기 - JOHNNY DEV <https://johnny-mh.github.io/blog/open-webui-mcp-fetch/>  
[40] Anthropic, Model Context Protocol 오픈소스로 공개 - GeekNews <https://news.hada.io/topic?id=17951>  
[41] Introducing the Model Context Protocol - Anthropic <https://www.anthropic.com/news/model-context-protocol>  
[42] MCP Support | Open WebUI <https://docs.openwebui.com/openapi-servers/mcp/>  
[43] MCP(Model Context Protocol) - 더이노베이터스 <https://theinnovators.zone/archives/4204>  
[44] MCP(Model Context Protocol)이 뭐길래? - DEV.DY - 티스토리 <https://dytis.tistory.com/112>  
[45] MCP Integration into Open-WebUI : r/OpenWebUI - Reddit <https://www.reddit.com/r/OpenWebUI/comments/1jaidh4/mcp_integration_into_openwebui/>  
[46] Claude MCP Community <https://www.claudemcp.com>  
[47] Model Context Protocol: Introduction <https://modelcontextprotocol.io>  
[48] Open WebUI용 MCP 도구 | MCP Servers - LobeHub <https://lobehub.com/ko/mcp/joshua-hub-mcp_things2>  
[49] Model Context Protocol (MCP) - Anthropic API <https://docs.anthropic.com/en/docs/mcp>  
[50] Model Context Protocol - Wikipedia <https://en.wikipedia.org/wiki/Model_Context_Protocol>  
[51] How to connect MCPs to OpenWebUI and Ollama (model ... - YouTube <https://www.youtube.com/watch?v=g4eEnTep-BA>  
[52] Claude MCP(Model Context Protocol) 완벽 가이드 <https://www.intellieffect.com/blog/claude-mcp-model-context-protocol-%EC%99%84%EB%B2%BD-%EA%B0%80%EC%9D%B4%EB%93%9C>  
[53] MCP(Model Context Protocol) 개념 및 이해를 위한 학습 자료 <https://discuss.pytorch.kr/t/deep-research-model-context-protocol-mcp/6594>  
[54] open-webui/mcpo: A simple, secure MCP-to-OpenAPI proxy server <https://github.com/open-webui/mcpo>  
[55] MCP(Model Context Protocol)이 뭐길래? 실습편 - DEV.DY - 티스토리 <https://dytis.tistory.com/113>  
[56] Model Context Protocol - GitHub <https://github.com/modelcontextprotocol>  
[57] Rag Integration: Connect RAG to Open-WebUI via MCP - MCP Market <https://mcpmarket.com/server/rag-integration>
