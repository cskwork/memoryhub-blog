---
title: "Google Calendar MCP 서버 코드 상세 분석"
date: 2025-03-21T14:41:56+09:00
slug: "494-Google-Calendar-MCP-서버-코드-상세-분석"
original_url: "https://memoryhub.tistory.com/494"
tistory_id: 494
draft: false
---

이 코드는 Model Context Protocol(MCP)을 기반으로 대규모 언어 모델(LLM)이 Google Calendar API와 직접 상호작용할 수 있도록 하는 Node.js 서버를 구현합니다. 복잡한 OAuth2 인증 처리와 표준화된 도구 인터페이스를 통해 AI 시스템이 사용자 달력을 안전하게 관리할 수 있게 합니다.

#### 참조 코드 :

<https://github.com/MCP-Mirror/GongRzhe_Calendar-MCP-Server>

## 1. 기술적 아키텍처 및 주요 구성요소

### 1.1 Model Context Protocol(MCP) 구조

MCP는 AI 모델이 외부 도구와 상호작용하기 위한 표준화된 프로토콜입니다.

```
클라이언트(AI 모델)   <-->   MCP 서버   <-->   외부 서비스(Google Calendar)
    요청/응답               요청/응답
```

### 1.2 주요 라이브러리 구성

- **@modelcontextprotocol/sdk**: MCP 서버 구현을 위한 핵심 라이브러리
  - `Server`: MCP 서버 인스턴스 생성
  - `StdioServerTransport`: 표준 입출력 기반 통신 계층
  - `CallToolRequestSchema`, `ListToolsRequestSchema`: 요청 스키마 정의
- **googleapis**: Google API 접근을 위한 공식 클라이언트 라이브러리
  - `google.calendar`: Calendar API v3 클라이언트
- **zod**: 런타임 타입 검증 라이브러리
  - 데이터 구조 스키마 정의 및 검증
- **google-auth-library**: OAuth2 인증 처리
  - `OAuth2Client`: OAuth 2.0 인증 흐름 관리

## 2. 인증 메커니즘 상세 분석

### 2.1 OAuth2 인증 설정

```
const CLIENT_ID = process.env.GOOGLE_CLIENT_ID;
const CLIENT_SECRET = process.env.GOOGLE_CLIENT_SECRET;
const REFRESH_TOKEN = process.env.GOOGLE_REFRESH_TOKEN;
const REDIRECT_URI = 'http://localhost';
```

- **환경 변수**: 민감한 인증 정보를 코드와 분리하여 보안 강화
- **Refresh Token 사용**: 장기적인 API 접근 권한 유지 (사용자 재인증 불필요)

### 2.2 OAuth2 클라이언트 초기화

```
const oauth2Client = new OAuth2Client(
    CLIENT_ID,
    CLIENT_SECRET,
    REDIRECT_URI
);

oauth2Client.setCredentials({
    refresh_token: REFRESH_TOKEN
});
```

- **인증 흐름**:
  1. Refresh Token으로 접근 토큰(Access Token) 자동 갱신
  2. 만료된 토큰 자동 갱신 처리
  3. API 요청마다 유효한 접근 토큰 첨부

## 3. 스키마 시스템 심층 분석

### 3.1 Zod 스키마 정의

각 API 작업에 대한 입력 구조를 엄격하게 정의합니다.

```
const CreateEventSchema = z.object({
    summary: z.string().describe("Event title"),
    start: z.object({
        dateTime: z.string().describe("Start time (ISO format)"),
        timeZone: z.string().optional().describe("Time zone"),
    }),
    end: z.object({
        dateTime: z.string().describe("End time (ISO format)"),
        timeZone: z.string().optional().describe("Time zone"),
    }),
    description: z.string().optional().describe("Event description"),
    location: z.string().optional().describe("Event location"),
});
```

- **필수/선택 필드 구분**: `.optional()`로 선택적 필드 표시
- **필드 설명**: `.describe()`로 각 필드의 용도 문서화
- **중첩 객체**: 복잡한 데이터 구조를 정확히 모델링

### 3.2 JSON 스키마 변환

```
inputSchema: zodToJsonSchema(CreateEventSchema)
```

- **목적**: Zod 스키마를 JSON 스키마로 변환하여 MCP에서 사용
- **장점**:
  1. 클라이언트(AI 모델)에 스키마 정보 제공
  2. 타입스크립트/자바스크립트 개발 환경과 MCP 간의 일관성 유지

## 4. 도구 구현 상세 분석

### 4.1 도구 등록 프로세스

```
server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: [
        {
            name: "create_event",
            description: "Creates a new event in Google Calendar",
            inputSchema: zodToJsonSchema(CreateEventSchema),
        },
        // 기타 도구들...
    ],
}));
```

- **도구 메타데이터**: 이름, 설명, 입력 스키마를 포함하는 정형화된 정보
- **도구 발견(Discovery)**: AI 모델이 사용 가능한 도구와 사용법을 동적으로 발견

### 4.2 도구별 상세 기능 분석

#### 4.2.1 create\_event

```
case "create_event": {
    const validatedArgs = CreateEventSchema.parse(args);
    const response = await calendar.events.insert({
        calendarId,
        requestBody: validatedArgs,
    });
    return {
        content: [
            {
                type: "text",
                text: `Event created with ID: ${response.data.id}\n` +
                      `Title: ${validatedArgs.summary}\n` +
                      `Start: ${validatedArgs.start.dateTime}\n` +
                      `End: ${validatedArgs.end.dateTime}`,
            },
        ],
    };
}
```

- **입력 검증**: Zod을 통한 입력값 유효성 검사 및 타입 강제
- **API 호출**: 검증된 파라미터로 Google Calendar API 호출
- **응답 구성**: 사용자 친화적인 응답 메시지 포맷팅

#### 4.2.2 get\_event

특정 ID의 이벤트 상세 정보를 JSON 형식으로 반환합니다.

#### 4.2.3 update\_event

이벤트 ID와 함께 업데이트할 필드만 선택적으로 전송합니다.

```
const { eventId, ...updates } = validatedArgs;
const response = await calendar.events.patch({
    calendarId,
    eventId,
    requestBody: updates,
});
```

- **부분 업데이트**: 객체 구조 분해를 통해 변경된 필드만 전송
- **효율성**: 불필요한 데이터 전송 최소화

#### 4.2.4 delete\_event

이벤트 ID를 검증하고 삭제를 수행합니다.

#### 4.2.5 list\_events

```
const response = await calendar.events.list({
    calendarId,
    timeMin: validatedArgs.timeMin,
    timeMax: validatedArgs.timeMax,
    maxResults: validatedArgs.maxResults || 10,
    orderBy: validatedArgs.orderBy || 'startTime',
    singleEvents: true,
});
```

- **기본값 설정**: 선택적 파라미터에 대한 기본값 제공
- **단일 이벤트 변환**: `singleEvents: true`로 반복 이벤트를 개별 이벤트로 확장

## 5. 요청 처리 흐름 상세 분석

### 5.1 도구 호출 요청 처리

```
server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    try {
        switch (name) {
            // 각 도구별 케이스 처리
        }
    } catch (error) {
        return {
            content: [
                {
                    type: "text",
                    text: `Error: ${error instanceof Error ? error.message : String(error)}`,
                },
            ],
            isError: true,
        };
    }
});
```

- **요청 파싱**: 도구 이름과 인자 추출
- **도구 디스패치**: 도구 이름에 따라 적절한 핸들러로 라우팅
- **오류 처리**: 모든 예외를 포착하여 구조화된 오류 응답으로 변환
  - **오류 분류**: Error 인스턴스와 기타 예외 구분 처리
  - **오류 표시**: `isError: true` 플래그로 오류 상태 명시

### 5.2 데이터 흐름 단계

1. **입력 수신**: MCP 요청 수신 (도구 이름, 인수)
2. **스키마 검증**: Zod를 통한 인수 검증 및 타입 변환
3. **API 호출**: Google Calendar API 호출
4. **응답 변환**: API 응답을 MCP 응답 형식으로 변환
5. **결과 반환**: 구조화된 응답 또는 오류 반환

## 6. 서버 통신 방식

```
const transport = new StdioServerTransport();
server.connect(transport).catch((error) => {
    console.error("Fatal error running server:", error);
    process.exit(1);
});
```

- **StdioServerTransport**: 표준 입출력(stdin/stdout)을 통한 통신
  - **장점**: 다양한 환경에서 쉽게 통합 가능
  - **작동 방식**: JSON 형식 메시지를 stdin으로 읽고 stdout으로 쓰기
- **오류 처리**: 치명적 오류 발생 시 서버 종료 및 오류 로깅

## 7. 보안 고려사항

### 7.1 인증 및 권한 관리

- **OAuth2 인증**: 표준 인증 프로토콜 사용
- **권한 범위 제한**: Google Calendar API에 필요한 최소 권한만 요청
- **환경 변수**: 민감한 인증 정보를 코드와 분리

### 7.2 입력 검증 및 위생 처리

- **스키마 검증**: 모든 입력에 대한 엄격한 구조 및 타입 검증
- **런타임 검증**: Zod를 통한 실행 시점 데이터 검증

## 8. 확장성 및 유지보수성

### 8.1 모듈화 구조

- **도구별 분리**: 각 기능을 독립적인 도구로 구현
- **스키마 중심 설계**: 데이터 구조를 명확히 정의하여 인터페이스 명확화

### 8.2 향후 확장 가능성

- **새로운 도구 추가**: 추가 Calendar API 기능을 쉽게 통합 가능
- **다른 Google API 통합**: 유사한 패턴으로 Gmail, Drive 등 확장 가능

## 9. 결론

이 코드는 Model Context Protocol을 통해 AI 모델과 Google Calendar API 사이의 안전하고 구조화된 인터페이스를 제공합니다. 엄격한 타입 검증, 오류 처리, OAuth2 인증을 통합하여 높은 신뢰성을 보장합니다. 이러한 구현 방식은 AI 시스템이 사용자의 자연어 요청을 실제 캘린더 작업으로 변환하는 데 필수적인 기술적 연결고리를 제공합니다.
