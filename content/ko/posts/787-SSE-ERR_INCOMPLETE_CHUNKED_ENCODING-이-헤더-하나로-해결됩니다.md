---
title: "? SSE ERR_INCOMPLETE_CHUNKED_ENCODING, 이 헤더 하나로 해결됩니다"
date: 2025-09-23T18:25:50+09:00
slug: "787-SSE-ERR_INCOMPLETE_CHUNKED_ENCODING-이-헤더-하나로-해결됩니다"
original_url: "https://memoryhub.tistory.com/787"
tistory_id: 787
draft: false
categories: ["데브 옵스"]
tags: ["네트워크 이론"]
---

```
        ? SSE 연결 에러 해결
    ┌─────────────────────────┐
    │  Client  ←─────→ Nginx  │
    │    ❌      ?     ?     │
    │ chunked   buffer   api   │ 
    └─────────────────────────┘
          실시간 데이터 전송
```

로컬에서는 완벽하게 작동하던 SSE(Server-Sent Events) 연결이 운영 환경에만 가면 갑자기 끊어지는 경험, 있으신가요? 특히 `ERR_INCOMPLETE_CHUNKED_ENCODING` 에러가 브라우저 콘솔을 가득 채우며 실시간 알림이나 채팅 기능이 먹통이 되는 상황 말입니다.

실제로 많은 개발자들이 로컬에서는 문제없이 작동하는 SSE가 Nginx를 통한 운영 환경에서 연결이 끊어지는 문제를 겪고 있습니다. 이 글을 읽으면 **단 한 줄의 헤더 설정**으로 이 문제를 완전히 해결할 수 있습니다.

## 목차

1. 배경 - 왜 로컬에서는 되는데 서버에서는 안 될까?
2. 핵심 개념 정리 - Chunked Transfer Encoding과 Proxy Buffering
3. 실습 - X-Accel-Buffering 헤더로 해결하기
4. 모범 사례 및 추가 설정
5. 마치며 & 참고자료

---

## 1. 배경

### 문제 상황의 원인 분석

SSE(Server-Sent Events)는 서버에서 클라이언트로 실시간 데이터를 전송하는 기술로, Transfer-Encoding: chunked 방식을 사용합니다. 문제는 **Nginx의 proxy buffering 기능**에 있습니다.

Nginx의 proxy buffering 기능은 default 값이 ON으로 설정되어 있어, 실시간 전송이 되어야 하는 SSE에서 연결이 끊어집니다. 로컬 환경에서는 Nginx를 거치지 않기 때문에 이 문제가 발생하지 않았던 것입니다.

### 관련 기술 용어 정리

| 용어 | 설명 |
| --- | --- |
| **SSE** | Server-Sent Events, 서버→클라이언트 단방향 실시간 통신 |
| **Chunked Transfer Encoding** | 응답 크기를 미리 알 수 없을 때 사용하는 HTTP 전송 방식 |
| **Proxy Buffering** | 프록시 서버가 데이터를 버퍼에 모아두었다가 일정량이 되면 전송하는 방식 |
| **X-Accel-Buffering** | Nginx에서 특정 응답의 버퍼링을 제어하는 헤더 |

## 2. 핵심 개념

> **ERR\_INCOMPLETE\_CHUNKED\_ENCODING 에러의 핵심**  
> **Nginx가 SSE 스트림을 버퍼링하면서 완전하지 않은 청크 데이터를 클라이언트에 전달할 때 발생**

SSE 통신에서 서버는 기본적으로 응답에 Transfer-Encoding: chunked를 사용합니다. SSE는 서버에서 동적으로 생성된 컨텐츠를 스트리밍하기 때문에 본문의 크기를 미리 알 수 없기 때문입니다.

Nginx는 서버의 응답을 버퍼에 저장해두었다가 버퍼가 차거나 서버가 응답 데이터를 모두 보내면 클라이언트로 전송하게 됩니다. 이로 인해 실시간성이 떨어지거나 연결이 끊어지는 문제가 발생합니다.

## 3. 실습

### ① 서버 코드에서 헤더 설정

**Spring Boot 예시:**

```
@GetMapping(value = "/stream", produces = "text/event-stream")
public SseEmitter streamEvents(HttpServletResponse response) {
    // 핵심 해결책: X-Accel-Buffering 헤더 설정
    response.setHeader("Cache-Control", "no-cache");
    response.setHeader("X-Accel-Buffering", "no");

    SseEmitter emitter = new SseEmitter(Long.MAX_VALUE);
    // SSE 로직...
    return emitter;
}
```

**Node.js 예시:**

```
app.get('/events', (req, res) => {
    res.writeHead(200, {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'X-Accel-Buffering': 'no'  // 핵심!
    });
});
```

### ② Nginx 설정 (추가 설정)

```
location /api/stream {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Connection '';
    proxy_read_timeout 86400s;  # 24시간
    # 개별 API용 버퍼링 해제 (선택사항)
    # proxy_buffering off;
}
```

### ③ 테스트 및 확인

브라우저 개발자 도구의 Network 탭에서 확인:

- Status: 200 OK (지속)
- Type: eventsource
- Response Headers에 `X-Accel-Buffering: no` 포함 확인

## 4. 모범 사례

| 접근 방법 | 장점 | 주의점 |
| --- | --- | --- |
| **X-Accel-Buffering 헤더** | SSE만 선택적 버퍼링 해제 | 서버 코드 수정 필요 |
| **Nginx proxy\_buffering off** | 설정만으로 해결 | 모든 API 성능 저하 가능 |
| **proxy\_read\_timeout 증가** | 연결 안정성 향상 | 리소스 점유 시간 증가 |

### 권장 설정 조합

가장 좋은 방법은 X-Accel-Buffering: no를 응답 헤더에 추가하여 SSE 응답만 버퍼링을 하지 않도록 설정하는 것입니다:

**필수 헤더:**

- `Content-Type: text/event-stream`
- `Cache-Control: no-cache`
- `X-Accel-Buffering: no`

**추가 고려사항:**  
연결이 너무 오래 유지되지 않도록 ping 메커니즘 구현을 권장합니다.

## 5. 마치며

**ERR\_INCOMPLETE\_CHUNKED\_ENCODING** 에러는 대부분 Nginx의 proxy buffering과 SSE의 chunked encoding 간 충돌로 발생합니다. **X-Accel-Buffering: no** 헤더 한 줄로 해결할 수 있으며, 이는 다른 API 성능에 영향주지 않는 가장 깔끔한 해결책입니다.

실제 프로젝트에서는 **timeout 설정**과 **ping 메커니즘**도 함께 고려하여 안정적인 실시간 통신을 구현하시기 바랍니다.

⸻

## 참고자료

- Nginx SSE 설정 가이드 - Server Fault
- 공책팀 SSE 구현 및 트러블슈팅
- Spring Server-Sent-Events 구현 - Tecoble
- X-Accel-Buffering 헤더 활용법
- MDN Server-sent Events 공식 문서
- <https://velog.io/@damongsanga/ERRINCOMPLETECHUNKEDENCODING-SSE-%ED%86%B5%EC%8B%A0-%EB%81%8A%EC%96%B4%EC%A7%90-%EC%97%90%EB%9F%AC-%ED%95%B4%EA%B2%B0-Nginx-Springboot-%EC%84%A4%EC%A0%95>
