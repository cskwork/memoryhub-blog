---
title: "Anthropic의 Model Context Protocol(MCP) 완벽 가이드 ?"
date: 2025-02-26T23:09:50+09:00
slug: "456-Anthropic의-Model-Context-Protocol-MCP-완벽-가이드"
original_url: "https://memoryhub.tistory.com/456"
tistory_id: 456
draft: false
categories: ["데브 라이브러리"]
tags: ["Claude"]
---

안녕하세요! 오늘은 Anthropic이 개발한 Model Context Protocol(MCP)에 대해 알아보고, 개발자들이 실제로 활용할 수 있는 인기 있는 서버들과 그 용도를 소개해드릴게요.

## MCP가 뭔가요? ?

여러분이 AI 비서에게 "내 컴퓨터에 있는 파일을 읽어줘"라고 요청했다고 상상해보세요.

- 일반적으로 AI는 여러분의 컴퓨터 파일에 접근할 수 없어요
- 하지만 MCP가 있다면? 안전하게 파일을 읽고 처리할 수 있어요!

Model Context Protocol(MCP)는 바로 이런 역할을 합니다!

- AI 모델(Claude)이 외부 도구나 데이터 소스에 안전하게 접근할 수 있게 해주는 표준화된 프로토콜
- 마치 AI에게 USB-C 포트를 제공하는 것과 같은 연결 통로 ✨

## 어떻게 동작하나요? ?

### 기본 아키텍처

```
사용자 → Claude → MCP 클라이언트 → MCP 서버 → 외부 서비스/데이터 → Claude → 사용자
```

1. 사용자가 질문합니다: "내 문서 폴더에 있는 영수증.pdf 파일을 분석해줘"
2. Claude는 파일 시스템 MCP 서버에 요청을 전달합니다
3. MCP 서버는 여러분의 컴퓨터에서 해당 파일을 안전하게 읽어옵니다
4. Claude는 받은 정보를 바탕으로 분석 결과를 사용자에게 제공합니다

## 인기 있는 실제 MCP 서버 10+ ?

### 1. 파일 시스템 MCP

```
npx @modelcontextprotocol/server-filesystem /path/to/allowed/files
```

- **기능**: 로컬 파일을 읽고, 쓰고, 검색할 수 있는 기능 제공
- **개발자 활용**: 프로젝트 파일 분석, 코드 리뷰, 문서 처리 자동화

### 2. 코드 인터프리터 MCP

```
npx @anthropic-ai/mcp-code-interpreter
```

- **기능**: Python 코드 실행, 데이터 분석, 시각화 기능 제공
- **개발자 활용**: 데이터 분석, 알고리즘 프로토타이핑, 문제 해결 자동화

### 3. Git MCP

```
uvx mcp-server-git
```

- **기능**: Git 저장소 읽기, 검색, 비교 기능 제공
- **개발자 활용**: 코드 변경 이력 분석, PR 리뷰, 코드베이스 이해 도움

### 4. GitHub MCP

```
npx @modelcontextprotocol/server-github
```

- **기능**: GitHub 저장소 관리, 이슈 관리, PR 생성 등 기능
- **개발자 활용**: 이슈 관리 자동화, 문서 업데이트, 코드 리뷰 도움

### 5. 웹 브라우저 MCP (Puppeteer)

```
npx @modelcontextprotocol/server-puppeteer
```

- **기능**: 웹 페이지 탐색, 스크린샷, 자동화 기능 제공
- **개발자 활용**: 웹 테스트 자동화, 데이터 수집, UI 분석

### 6. PostgreSQL MCP

```
npx @modelcontextprotocol/server-postgres
```

- **기능**: PostgreSQL 데이터베이스 쿼리, 스키마 검사 기능
- **개발자 활용**: 데이터 분석, 쿼리 최적화, 스키마 설계 도움

### 7. SQLite MCP

```
npx @modelcontextprotocol/server-sqlite
```

- **기능**: SQLite 데이터베이스 접근, 쿼리, 분석 기능
- **개발자 활용**: 로컬 데이터 분석, 데이터베이스 설계, 보고서 생성

### 8. Memory MCP

```
npx @modelcontextprotocol/server-memory
```

- **기능**: 지식 그래프 기반 영구 메모리 시스템 제공
- **개발자 활용**: 장기 대화 컨텍스트 유지, 프로젝트 지식 저장

### 9. 웹 콘텐츠 가져오기 (Fetch MCP)

```
npx @modelcontextprotocol/server-fetch
```

- **기능**: 웹 콘텐츠 가져오기 및 LLM에 최적화된 변환
- **개발자 활용**: API 문서 참조, 웹 콘텐츠 분석, 정보 검색

### 10. 구글 드라이브 MCP

```
npx @modelcontextprotocol/server-gdrive
```

- **기능**: 구글 드라이브 파일 접근, 검색, 관리 기능
- **개발자 활용**: 문서 관리, 팀 문서 분석, 콘텐츠 요약

### 11. Slack MCP

```
npx @modelcontextprotocol/server-slack
```

- **기능**: Slack 채널 관리, 메시지 전송, 검색 기능
- **개발자 활용**: 팀 커뮤니케이션 자동화, 알림 관리, 정보 추적

### 12. Docker MCP (커뮤니티)

```
npx mcp-server-docker
```

- **기능**: Docker 컨테이너, 이미지, 볼륨 관리 기능
- **개발자 활용**: 컨테이너 관리 자동화, 배포 과정 간소화

## 개발자를 위한 활용 방법 ?

### 1. 코드 리뷰 및 분석 보조

```
// Git과 GitHub MCP를 활용한 코드 리뷰 워크플로우
// 1. 저장소 클론 및 분석
await gitServer.cloneRepository('https://github.com/user/repo.git');
await gitServer.analyzeChanges('main', 'feature-branch');

// 2. GitHub PR 생성 및 코멘트
await githubServer.createPullRequestComment({
  owner: 'user',
  repo: 'repo',
  pull_number: 123,
  body: '코드 분석 결과: 성능 개선점 3개 발견'
});
```

### 2. 데이터베이스 작업 자동화

```
-- PostgreSQL MCP를 활용한 데이터베이스 최적화
-- 1. 스키마 분석
SELECT * FROM information_schema.tables WHERE table_schema = 'public';

-- 2. 성능 문제 쿼리 식별
SELECT query, total_time, calls
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 10;

-- 3. 인덱스 제안
-- Claude가 인덱스 생성 스크립트를 자동으로 생성
```

### 3. 로컬 개발 환경 지원

```
# 파일 시스템 MCP와 코드 인터프리터 MCP 조합 예시
npx @modelcontextprotocol/server-filesystem ~/projects
npx @anthropic-ai/mcp-code-interpreter

# Claude에게 요청:
# "내 프로젝트 코드에서 메모리 누수 가능성이 있는 부분을 찾아줘"
# "이 데이터셋에 대한 시각화를 만들어줘"
```

### 4. 웹 서비스 통합 및 자동화

```
// GitHub와 Slack MCP 연동 예시
async function createWeeklyReport() {
  // 1. GitHub에서 주간 커밋 정보 가져오기
  const commits = await githubServer.getCommits({
    owner: 'team',
    repo: 'project',
    since: getLastWeek()
  });

  // 2. 커밋 분석 및 보고서 생성
  const report = analyzeCommits(commits);

  // 3. Slack에 보고서 전송
  await slackServer.postMessage({
    channel: 'dev-team',
    text: '주간 개발 현황 리포트',
    blocks: formatReportForSlack(report)
  });
}
```

## 실제 활용 시나리오 ?

### 1. 풀스택 개발 보조

파일 시스템, Git, 코드 인터프리터, 데이터베이스 MCP를 함께 사용하여:

- 프론트엔드와 백엔드 코드 동시 분석
- API 엔드포인트와 데이터베이스 스키마 정합성 검증
- 새로운 기능 구현을 위한 코드 스니펫 생성

```
"내 프로젝트에서 사용자 인증 관련 코드를 모두 찾아서 보안 취약점이 있는지 검사해줘"
```

### 2. 데이터 파이프라인 구축

PostgreSQL, 코드 인터프리터, 파일 시스템 MCP를 활용하여:

- 데이터베이스 쿼리 결과 분석
- Python으로 데이터 변환 및 처리
- 결과를 파일로 저장하고 시각화

```
"DB에서 지난 달 판매 데이터를 가져와서, 지역별 매출 추이 그래프를 생성하고 리포트를 작성해줘"
```

### 3. 문서화 및 지식 관리

Memory MCP, 파일 시스템, GitHub MCP를 조합하여:

- 프로젝트 문서 자동 생성
- 코드 변경에 따른 README 업데이트
- 팀 지식 베이스 구축

```
"지난 스프린트에서 변경된 모든 코드를 분석해서 API 문서를 업데이트해줘"
```

## MCP 서버 설치 및 구성 ?

### 1. Claude 데스크톱에서 MCP 사용하기

```
// config.json 파일 생성
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your_token_here"
      }
    }
  }
}
```

### 2. 자신만의 MCP 서버 만들기

```
// TypeScript로 간단한 MCP 서버 만들기
import { createServer, Tools } from '@modelcontextprotocol/typescript-sdk';

// 도구 정의
const tools: Tools = {
  getWeather: {
    description: '특정 도시의 현재 날씨 정보를 가져옵니다',
    parameters: {
      type: 'object',
      properties: {
        city: { type: 'string', description: '도시 이름 (예: 서울)' }
      },
      required: ['city']
    },
    handler: async ({ city }) => {
      // 날씨 API 호출 로직
      return { temperature: '23°C', condition: '맑음' };
    }
  }
};

// 서버 시작
const server = createServer({ tools });
server.listen(3000, () => {
  console.log('MCP 서버가 3000번 포트에서 실행 중입니다');
});
```

## 주의할 점 ⚠️

1. **보안 고려사항**

   - MCP 서버는 로컬 리소스에 접근할 수 있으므로 액세스 권한 설정에 주의
   - 신뢰할 수 있는 소스의 MCP 서버만 사용
   - API 키와 인증 토큰은 환경 변수로 안전하게 관리
2. **리소스 관리**

   - 여러 MCP 서버를 동시에 실행할 경우 시스템 리소스 사용량 모니터링
   - 브라우저 자동화와 같은 무거운 서버는 필요할 때만 실행
3. **호환성 고려**

   - MCP 서버는 다른 애플리케이션과 포트 충돌이 발생할 수 있음
   - 최신 버전의 MCP SDK로 업데이트하여 호환성 유지

## 마치며 ?

Model Context Protocol(MCP)은 AI와 외부 세계를 연결하는 강력한 다리 역할을 합니다. 개발자에게는 반복적인 작업을 자동화하고, 복잡한 문제 해결을 도와주는 든든한 조수가 될 수 있습니다.

이 프로토콜은 계속 발전하고 있으며, 개발자 커뮤니티에서 다양한 MCP 서버를 만들고 공유하고 있습니다. 여러분도 직접 MCP 서버를 만들어 AI의 가능성을 확장해보세요!

---

궁금하신 점 있으시다면 댓글로 남겨주세요! ?

#Anthropic #Claude #ModelContextProtocol #MCP #AI개발 #AITools

---

### 참고 자료

1. Model Context Protocol 공식 사이트: <https://modelcontextprotocol.io>
2. MCP GitHub 저장소: <https://github.com/modelcontextprotocol>
3. Anthropic Claude 문서: <https://docs.anthropic.com/claude/docs/agents-and-tools/mcp>
4. MCP 예제 서버 모음: <https://modelcontextprotocol.io/examples>
