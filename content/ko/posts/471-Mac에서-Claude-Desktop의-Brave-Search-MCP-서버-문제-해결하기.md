---
title: "Mac에서 Claude Desktop의 Brave Search MCP 서버 문제 해결하기 ?"
date: 2025-03-13T20:54:18+09:00
slug: "471-Mac에서-Claude-Desktop의-Brave-Search-MCP-서버-문제-해결하기"
original_url: "https://memoryhub.tistory.com/471"
tistory_id: 471
draft: false
---

맥 환경에서 Claude Desktop 애플리케이션의 Brave Search MCP 서버가 작동하지 않는 문제를 해결하는 방법에 대해 알려드리겠습니다.

## MCP 서버와 Brave Search가 뭔가요? ?

MCP(Model Context Protocol) 서버는 Claude AI가 외부 도구와 통신할 수 있게 해주는 인터페이스입니다.

- 마치 Claude가 인터넷을 탐색할 수 있는 눈을 갖게 해주는 것과 같아요!
- Brave Search MCP는 Claude가 웹에서 최신 정보를 검색할 수 있게 해줍니다.
- 이 기능이 없으면 Claude는 자신의 학습 데이터로만 답변해야 합니다.

## 문제의 원인은 무엇인가요? ?

Mac에서 Brave Search MCP 서버가 작동하지 않는 주요 원인들:

1. **Node.js 환경 문제**

   - Claude Desktop이 Node.js와 npx를 찾지 못하는 경우
   - 경로(PATH) 설정이 잘못된 경우
2. **설정 파일 오류**

   - 설정 파일이 잘못된 위치에 있거나
   - JSON 형식이 올바르지 않거나
   - 필요한 환경 변수가 누락된 경우
3. **API 키 문제**

   - Brave Search API 키가 없거나 잘못 설정된 경우

## 문제 해결 방법 ?

### 1. Node.js 설치 확인하기

```
# 터미널에서 Node.js 및 npm 설치 확인
node -v
npm -v

# 설치되지 않은 경우 nvm으로 설치
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
source ~/.zshrc  # 또는 source ~/.bash_profile
nvm install --lts  # LTS 버전 설치
```

### 2. 정확한 경로 찾기

```
# npx의 전체 경로 찾기
which npx
# 예: /Users/사용자이름/.nvm/versions/node/v18.12.1/bin/npx

# Node.js 경로 찾기
which node
# 예: /Users/사용자이름/.nvm/versions/node/v18.12.1/bin/node
```

### 3. Brave Search API 키 얻기

1. [Brave Search API](https://brave.com/search/api/) 웹사이트 방문
2. 개발자 계정 생성 또는 로그인
3. API 키 생성 및 복사

### 4. 설정 파일 수정하기

1. 파일 위치 찾기:

   ```
   /Users/사용자이름/Library/Application Support/Claude/claude_desktop_config.json
   ```

   - `사용자이름`은 여러분의 실제 Mac 사용자 이름으로 바꿔주세요.
2. 파일이 없다면 생성하기:

   ```
   mkdir -p ~/Library/Application\ Support/Claude/
   touch ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```
3. 설정 파일에 다음 내용 추가하기:

   ```
   {
     "mcpServers": [
       {
         "name": "brave-search",
         "command": "여기에_npx_전체경로",
         "args": ["-y", "@modelcontextprotocol/server-brave-search"],
         "env": {
           "BRAVE_API_KEY": "여기에_API_키_입력",
           "PATH": "여기에_node_경로:/usr/local/bin:/usr/bin:/bin",
           "NODE_PATH": "여기에_node_모듈_경로"
         }
       }
     ]
   }
   ```
4. 실제 경로로 수정하기:

   ```
   {
     "mcpServers": [
       {
         "name": "brave-search",
         "command": "/Users/사용자이름/.nvm/versions/node/v버전번호/bin/npx",
         "args": ["-y", "@modelcontextprotocol/server-brave-search"],
         "env": {
           "BRAVE_API_KEY": "여기에_API_키_입력",
           "PATH": "/Users/사용자이름/.nvm/versions/node/v버전번호/bin:/usr/local/bin:/usr/bin:/bin",
           "NODE_PATH": "/Users/사용자이름/.nvm/versions/node/v버전번호/lib/node_modules"
         }
       }
     ]
   }
   ```

### 5. MCP 서버 패키지 설치하기

```
# 전역으로 패키지 설치
npm install -g @modelcontextprotocol/server-brave-search
```

### 6. Claude Desktop 재시작하기

1. Claude Desktop 완전히 종료
2. 애플리케이션 다시 시작

## 문제 해결 사례 ?️

다음은 Reddit 사용자가 공유한 성공적인 해결 방법입니다:

```
{
  "mcpServers": [
    {
      "name": "brave-search",
      "command": "/Users/사용자이름/.nvm/versions/node/v23.3.0/bin/npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "여기에_API_키_입력",
        "PATH": "/Users/사용자이름/.nvm/versions/node/v23.3.0/bin:/usr/local/bin:/usr/bin:/bin",
        "NODE_PATH": "/Users/사용자이름/.nvm/versions/node/v23.3.0/lib/node_modules"
      }
    }
  ]
}
```

## 흔한 오류와 해결 방법 ⚠️

### 1. `spawn npx ENOENT` 오류

- **원인**: Claude Desktop이 npx를 찾지 못함
- **해결**: 설정 파일에 npx의 전체 경로 지정

### 2. API 키 관련 오류

- **원인**: API 키가 잘못됨
- **해결**: 새로운 API 키 발급 및 정확하게 입력

### 3. MCP 서버 시작 실패

- **원인**: 패키지 설치 문제
- **해결**: `npm install -g @modelcontextprotocol/server-brave-search` 다시 실행

### 4. 설정 파일 인식 못함

- **원인**: 파일 위치나 형식 오류
- **해결**: 정확한 경로와 JSON 형식 확인

## 주의할 점 ⚠️

1. **Node.js 설치 방법**: Node 버전 관리자(nvm)를 사용하여 설치하는 것을 권장합니다. 설치 프로그램보다 경로 관리가 더 용이합니다.
2. **경로의 정확성**: 설정 파일에서 사용하는 모든 경로(PATH)는 실제 환경과 정확히 일치해야 합니다. 특히 사용자 이름과 Node.js 버전에 주의하세요.
3. **JSON 형식**: 설정 파일은 올바른 JSON 형식이어야 합니다. 쉼표, 따옴표 등의 오류가 없는지 확인하세요.
4. **API 키 보안**: Brave Search API 키는 개인 정보입니다. 공개 장소에 공유하지 마세요.
5. **파일 권한**: 설정 파일과 Node.js 관련 디렉토리에 적절한 읽기/쓰기 권한이 있어야 합니다.

---

이 가이드가 Mac에서 Claude Desktop의 Brave Search MCP 서버 문제를 해결하는 데 도움이 되었기를 바랍니다! 궁금한 점이 있으시면 언제든지 질문해주세요. ?

## 참고 자료

1. [Reddit - Resolved MCP Brave Search Issue](https://www.reddit.com/r/ClaudeAI/comments/1h758o0/resolved_mcp_brave_search_issue/)
2. [GitHub - Model Context Protocol Servers Issues](https://github.com/modelcontextprotocol/servers/issues/63)
3. [Stack Overflow - Could not start MCP server for Brave Search](https://stackoverflow.com/questions/79262030/could-not-start-mcp-server-for-brave-search-in-computer-use-and-claude-desktop)
4. [Medium - MCP Integration: How Brave Search and Claude Desktop Enhance AI Assistant](https://medium.com/@richardhightower/mcp-integration-how-brave-search-and-claude-desktop-enhance-ai-assistant-agentic-capabilities-c840590fa100)
