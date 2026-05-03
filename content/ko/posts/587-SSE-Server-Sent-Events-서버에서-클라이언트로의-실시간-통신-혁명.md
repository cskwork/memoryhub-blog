---
title: "SSE(Server-Sent Events) - 서버에서 클라이언트로의 실시간 통신 혁명! ?"
date: 2025-05-14T16:36:19+09:00
slug: "587-SSE-Server-Sent-Events-서버에서-클라이언트로의-실시간-통신-혁명"
original_url: "https://memoryhub.tistory.com/587"
tistory_id: 587
draft: false
---

*여러분은 실시간으로 주식 가격이 업데이트되거나 알림이 자동으로 표시되는 웹사이트를 본 적이 있나요? 새로고침 없이 어떻게 작동하는지 궁금하셨나요? 오늘은 그 비밀 중 하나인 SSE에 대해 알아보겠습니다!*

## 등장 배경

전통적인 웹 통신에서는 클라이언트(브라우저)가 서버에 요청을 보내고, 서버가 응답하는 방식으로 데이터를 주고받았습니다. 그러나 이런 방식은 실시간 데이터를 표시해야 하는 상황에서 몇 가지 문제점이 있었죠.

과거에는 다음과 같은 방법으로 실시간 데이터를 처리했습니다:

1. **전체 페이지 새로고침**: 90년대에는 페이지나 프레임을 주기적으로 새로고침하는 방식을 사용했습니다.
2. **폴링(Polling)**: Ajax를 사용해 주기적으로 서버에 데이터를 요청했습니다.
3. **롱 폴링(Long Polling)**: 서버가 응답할 때까지 연결을 유지하는 방식이었습니다.

하지만 이러한 방식들은 불필요한 요청과 서버 부하를 초래했습니다. 그래서 HTML5에서는 SSE(Server-Sent Events)가 도입되어 서버에서 클라이언트로 단방향 통신이 가능해졌습니다. SSE는 2004년부터 WHATWG Web Applications 1.0 제안의 일부로 처음 명세되었고, 현재는 대부분의 모던 브라우저에서 지원됩니다.

[SSE가 해결하는 문제점]:

1. **실시간 업데이트**: 서버가 언제든지 클라이언트에게 데이터를 푸시할 수 있습니다.
2. **네트워크 효율성**: 주기적인 폴링과 달리 필요할 때만 데이터를 전송합니다.
3. **자동 재연결**: 연결이 끊어져도 자동으로 다시 연결합니다.

## 핵심 원리

SSE의 작동 원리는 간단합니다. 기본적으로 서버와 클라이언트 간에 열린 HTTP 연결을 통해 서버가 이벤트를 스트리밍하는 방식입니다.

```
클라이언트                                서버
   |                                       |
   |--- HTTP 요청 (EventSource 생성) ---->|
   |                                       |
   |<---- HTTP 응답 (무한 스트림) ---------|
   |                                       |
   |<---- 이벤트 데이터 1 ----------------|
   |                                       |
   |<---- 이벤트 데이터 2 ----------------|
   |                                       |
   |       (연결 유지됨)                   |
```

**클라이언트 측 코드 예시 (JavaScript):**

```
// EventSource 인터페이스를 사용하여 서버에 연결
const eventSource = new EventSource('/events');

// 메시지 이벤트 리스너 추가
eventSource.onmessage = function(event) {
  console.log('새 메시지:', event.data);
  // 받은, 데이터로 UI 업데이트
};

// 연결 열림 이벤트
eventSource.onopen = function() {
  console.log('연결됨');
};

// 오류 처리
eventSource.onerror = function() {
  console.error('SSE 연결 오류');
};

// 특정 이벤트 타입 수신
eventSource.addEventListener('customEvent', function(e) {
  console.log('커스텀 이벤트:', e.data);
});

// 연결 종료 (필요한 경우)
// eventSource.close();
```

**서버 측 코드 예시 (Node.js/Express):**

```
const express = require('express');
const app = express();

app.get('/events', (req, res) => {
  // SSE 설정에 필요한 헤더 설정
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive'
  });

  // 연결 유지를 위한 주석 전송 (선택사항)
  setInterval(() => {
    res.write(': 연결 유지용 주석\n\n');
  }, 15000);

  // 데이터 전송 예시
  let count = 0;
  const intervalId = setInterval(() => {
    count++;
    // 이벤트 ID 설정 (재연결시 사용)
    res.write(`id: ${count}\n`);
    // 이벤트 타입 지정 (선택사항)
    res.write('event: message\n');
    // 실제 데이터
    res.write(`data: {"count": ${count}, "time": "${new Date().toISOString()}"}\n\n`);
  }, 1000);

  // 클라이언트 연결 종료 시 청소
  req.on('close', () => {
    clearInterval(intervalId);
    console.log('클라이언트 연결 종료');
  });
});

app.listen(3000, () => {
  console.log('서버 시작: http://localhost:3000');
});
```

**SSE 메시지 형식** (서버에서 클라이언트로 전송):

```
id: 이벤트ID
event: 이벤트타입
data: 실제 데이터 내용
retry: 재연결 시간(밀리초)
```

각 메시지는 빈 줄 두 개(`\n\n`)로 구분됩니다.

## SSE vs WebSocket 비교

| 특징 | SSE | WebSocket |
| --- | --- | --- |
| 프로토콜 | HTTP | WS/WSS |
| 통신 방향 | 단방향(서버→클라이언트) | 양방향 |
| 구현 복잡도 | 단순함 | 복잡함 |
| 자동 재연결 | 기본 지원 | 직접 구현 필요 |
| 데이터 형식 | 텍스트(UTF-8) | 텍스트/바이너리 |
| 방화벽 호환성 | 좋음 | 가능한 제한 |
| 동시 연결 수 | 브라우저당 6개 제한(HTTP/1.1) | 더 많은 연결 가능 |

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **연결 제한**
   - HTTP/1.1에서는 브라우저당 도메인별로 6개 연결 제한이 있습니다.
   - 해결법: HTTP/2 사용 시 최대 100개까지 연결 가능합니다.
2. **메모리 관리**
   - 서버에서 많은 연결을 관리할 때 메모리 누수가 발생할 수 있습니다.
   - 해결법: 연결 종료 시 항상 리소스를 정리하세요(clearInterval 등).
3. **데이터 형식 제한**
   - SSE는 텍스트(UTF-8) 데이터만 전송 가능합니다.
   - 해결법: 바이너리 데이터는 base64로 인코딩하거나 WebSocket 사용을 고려하세요.

? **꿀팁**

- 서버에서 주기적으로 빈 주석(`: 주석\n\n`)을 보내면 연결이 끊어지는 것을 방지할 수 있습니다.
- 이벤트 ID를 사용하면 연결이 끊어졌다가 다시 연결될 때 놓친 메시지를 다시 받을 수 있습니다.
- `EventSource` 객체의 `withCredentials` 옵션을 사용하면 CORS 요청에 쿠키를 포함할 수 있습니다.
- 개발 시 네트워크 탭에서 SSE 연결을 모니터링하면 디버깅에 도움이 됩니다.

## SSE 활용 사례

SSE는 다음과 같은 실시간 애플리케이션에 적합합니다:

1. **실시간 알림** - 소셜 미디어 알림, 이메일 도착 알림
2. **실시간 대시보드** - 주식 시세, 스포츠 점수, 서버 모니터링
3. **협업 도구** - 문서 업데이트, 공동 편집 상태
4. **채팅 응용 프로그램** - 일방향 공지 메시지
5. **진행 상태 업데이트** - 파일 업로드, 긴 작업 처리 상태

## 마치며

지금까지 SSE(Server-Sent Events)에 대해 알아보았습니다. 단방향 실시간 통신이 필요하고 구현이 간단한 솔루션을 찾고 있다면 SSE는 훌륭한 선택입니다. 양방향 통신이 필요하다면 WebSocket을, 단순한 일방향 업데이트만 필요하다면 SSE를 선택하는 것이 좋습니다. ?

SSE는 이해하기 쉽고 구현하기 쉬운 기술이지만, 실제 프로덕션 환경에서는 스케일링, 보안, 인증 등 추가 고려사항이 있습니다. 그럼에도 불구하고 적절한 사용 사례에서는 매우 효과적인 실시간 통신 방법입니다!

## 참고 자료 ?

- [MDN: Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- [MDN: Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)
- [DigitalOcean: How To Use SSE in Node.js](https://www.digitalocean.com/community/tutorials/nodejs-server-sent-events-build-realtime-app)
- [Mastering JS: Server-Sent Events with Express](https://masteringjs.io/tutorials/express/server-sent-events)

---

#SSE #ServerSentEvents #실시간통신 #웹개발 #HTML5
