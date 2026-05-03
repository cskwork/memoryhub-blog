---
title: "? SSE(Server-Sent Event) 실시간 통신, 왜 개발자들이 주목할까요?"
date: 2025-09-23T18:34:25+09:00
slug: "788-SSE-Server-Sent-Event-실시간-통신-왜-개발자들이-주목할까요"
original_url: "https://memoryhub.tistory.com/788"
tistory_id: 788
draft: false
---

```
    ? 실시간 통신의 새 지평 
   ┌─────────────────────────┐
   │   클라이언트 (브라우저)     │
   │         ↑              │
   │    ? 실시간 푸시         │
   │         │              │  
   └─────────┴─────────────────┘
           서버 (SSE)
```

최근 회사에서 알림 기능을 구현하면서 30초마다 API를 호출하는 폴링 방식 때문에 **하루 30만 건**의 불필요한 통신이 발생하는 문제를 발견했습니다. 이를 SSE로 개선한 결과 **78% API 호출량 감소**라는 놀라운 성과를 얻었죠.

SSE(Server-Sent Events)가 무엇이고, 언제 사용해야 하며, 어떻게 구현하는지 실무 경험을 바탕으로 완벽 정리해드립니다.

이 글을 읽으면 실시간 통신의 핵심 원리부터 실제 구현까지 모든 것을 마스터할 수 있습니다.

## 목차

1. 배경 - 실시간 통신이 필요한 이유
2. 핵심 개념 정리
3. 실습 - SSE 구현하기
4. 모범 사례·베스트 프랙티스
5. 마치며 & 참고자료

---

## 1. 배경

전통적인 HTTP 통신은 클라이언트가 요청할 때만 서버가 응답하는 구조였습니다. 하지만 현대 웹 애플리케이션에서는 **실시간 알림, 주식 시세, 채팅 메시지** 등 서버에서 클라이언트로 능동적으로 데이터를 전송해야 하는 경우가 많아졌죠.

### 기존 해결 방법들의 문제점

| 방식 | 장점 | 단점 |
| --- | --- | --- |
| **Polling** | 구현 단순 | 불필요한 요청 다발, 리소스 낭비 |
| **WebSocket** | 양방향 통신 가능 | 복잡한 구현, TCP 기반으로 무거움 |
| **Long Polling** | 폴링 대비 효율적 | 서버 리소스 장시간 점유 |

SSE는 이러한 문제를 해결하기 위해 등장한 **HTTP 기반 단방향 실시간 통신** 기술입니다. 서버에서 클라이언트로 데이터를 능동적으로 푸시할 수 있어 불필요한 요청을 줄이고 실시간성을 보장합니다.

## 2. 핵심 개념

> **SSE(Server-Sent Events)는 HTTP를 통해 서버가 클라이언트에게 실시간으로 이벤트를 전송하는 단방향 통신 기술입니다.**

### SSE의 핵심 특징

✅ **HTTP 기반**: 기존 웹 인프라 활용 가능  
✅ **단방향 통신**: 서버 → 클라이언트만 가능  
✅ **자동 재연결**: 연결 끊김 시 브라우저가 자동 복구  
✅ **이벤트 스트림**: `text/event-stream` MIME 타입 사용  
✅ **브라우저 지원**: 모든 주요 브라우저에서 EventSource API 제공

```
// 클라이언트 측 기본 구조
const eventSource = new EventSource('/api/notifications');
eventSource.onmessage = (event) => {
    console.log('받은 데이터:', event.data);
};
```

## 3. 실습

### ① 서버 설정 (Node.js Express)

```
app.get('/api/sse', (req, res) => {
    // SSE 응답 헤더 설정
    res.writeHead(200, {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
    });

    // 실시간 데이터 전송
    const sendEvent = (data) => {
        res.write(`data: ${JSON.stringify(data)}\n\n`);
    };

    sendEvent({ message: '연결 성공!' });
});
```

### ② 클라이언트 구현 (JavaScript)

```
const eventSource = new EventSource('/api/sse');

eventSource.onopen = () => {
    console.log('SSE 연결 성공');
};

eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    // DOM 업데이트 로직
    updateNotification(data);
};

eventSource.onerror = (error) => {
    console.error('SSE 연결 오류:', error);
};
```

### ③ 연결 테스트

개발자 도구의 **Network** 탭에서 `EventStream` 타입으로 연결 상태를 확인할 수 있습니다. 정상 연결 시 지속적인 데이터 스트림을 확인할 수 있습니다.

## 4. 모범 사례

### 주요 패턴별 가이드

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **실시간 알림** | 폴링 대비 78% API 감소 | 연결 수 제한 고려 |
| **라이브 피드** | 즉시성 보장 | 메모리 누수 방지 |
| **상태 모니터링** | 서버 부하 최소화 | 타임아웃 설정 |

### 실무 팁

**DB 커넥션 풀 고갈 주의**: SSE 연결 중에는 HTTP 커넥션이 유지되므로, JPA의 `open-in-view` 속성을 `false`로 설정해야 합니다.

**Nginx 설정**: SSE 응답에 대해 `proxy_buffering off` 또는 응답 헤더에 `X-Accel-Buffering: no`를 설정하여 버퍼링을 비활성화해야 합니다.

## 5. 마치며

SSE는 복잡한 WebSocket 없이도 **실시간 단방향 통신**을 구현할 수 있는 강력한 도구입니다. 특히 알림, 뉴스 피드, 모니터링 대시보드 등에서 **폴링 방식 대비 70-80% 트래픽 감소** 효과를 기대할 수 있죠.

다만 HTTP/1.1 환경에서는 도메인당 6개 연결 제한이 있으니, 대규모 서비스에서는 HTTP/2 도입을 권장합니다.  
**실무에서는 자동 재연결과 에러 핸들링을 반드시 구현하여 안정성을 확보하세요.**

**참고자료**  
• [MDN Server-Sent Events 공식 문서](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)  
• [SSE 실무 구현 사례 - Sionic.ai](https://blog.sionic.ai/server-sent-event)  
• [WebSockets vs SSE 비교 - Ably](https://ably.com/blog/websockets-vs-sse)
