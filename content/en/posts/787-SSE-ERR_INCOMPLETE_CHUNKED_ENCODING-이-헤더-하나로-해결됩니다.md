---
title: "SSE ERR_INCOMPLETE_CHUNKED_ENCODING: Solved with This One Header"
date: 2025-09-23T18:25:50+09:00
slug: "787-SSE-ERR_INCOMPLETE_CHUNKED_ENCODING-이-헤더-하나로-해결됩니다"
original_url: "https://memoryhub.tistory.com/787"
tistory_id: 787
draft: false
---

```
        🔧 SSE Connection Error Resolution
    ┌─────────────────────────┐
    │  Client  ←─────→ Nginx  │
    │    ❌      🔌    🔌     │
    │ chunked   buffer   api   │ 
    └─────────────────────────┘
          Real-time Data Transfer
```

Have you ever experienced perfect SSE (Server-Sent Events) connections in local environments suddenly breaking in production? Especially when `ERR_INCOMPLETE_CHUNKED_ENCODING` errors flood the browser console, making real-time notifications or chat features completely unresponsive?

Many developers have experienced SSE connections that work flawlessly locally breaking under production environments with Nginx. After reading this article, you'll be able to **completely resolve this issue with a single header line**.

## Table of Contents

1. Background - Why Local Works but Server Doesn't
2. Core Concepts - Chunked Transfer Encoding and Proxy Buffering
3. Practice - Resolving with X-Accel-Buffering Header
4. Best Practices and Additional Configuration
5. Conclusion & References

---

## 1. Background

### Problem Analysis

SSE (Server-Sent Events) is a technology for real-time data transmission from server to client using Transfer-Encoding: chunked. The problem lies in **Nginx's proxy buffering feature**.

Nginx's proxy buffering defaults to ON, causing SSE connections to drop when real-time transmission is required. Local environments don't experience this because they don't go through Nginx.

### Related Technology Terminology

| Term | Explanation |
| --- | --- |
| **SSE** | Server-Sent Events, one-way server→client real-time communication |
| **Chunked Transfer Encoding** | HTTP transmission method when response size is unknown in advance |
| **Proxy Buffering** | Proxy server buffers data and sends once a certain amount accumulates |
| **X-Accel-Buffering** | Header controlling buffering for specific responses in Nginx |

## 2. Core Concepts

> **Core of ERR_INCOMPLETE_CHUNKED_ENCODING Error**  
> **Occurs when Nginx buffers SSE streams and delivers incomplete chunk data to clients**

In SSE communication, servers inherently use Transfer-Encoding: chunked because SSE streams dynamically generated content where content size is unknown in advance.

Nginx stores server responses in a buffer and transmits to clients once the buffer fills or the server completes sending all data. This causes reduced real-time performance or connection drops.

## 3. Practice

### ① Set Headers in Server Code

**Spring Boot Example:**

```
@GetMapping(value = "/stream", produces = "text/event-stream")
public SseEmitter streamEvents(HttpServletResponse response) {
    // Core solution: Set X-Accel-Buffering header
    response.setHeader("Cache-Control", "no-cache");
    response.setHeader("X-Accel-Buffering", "no");

    SseEmitter emitter = new SseEmitter(Long.MAX_VALUE);
    // SSE logic...
    return emitter;
}
```

**Node.js Example:**

```
app.get('/events', (req, res) => {
    res.writeHead(200, {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'X-Accel-Buffering': 'no'  // Key!
    });
});
```

### ② Nginx Configuration (Additional Setup)

```
location /api/stream {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Connection '';
    proxy_read_timeout 86400s;  # 24 hours
    # Optional per-API buffering disable
    # proxy_buffering off;
}
```

### ③ Testing and Verification

In browser developer tools Network tab:

- Status: 200 OK (continuous)
- Type: eventsource
- Response Headers contain `X-Accel-Buffering: no`

## 4. Best Practices

| Approach | Advantages | Cautions |
| --- | --- | --- |
| **X-Accel-Buffering Header** | SSE-only selective buffering disable | Requires server code modification |
| **Nginx proxy_buffering off** | Configuration-only solution | May impact all API performance |
| **proxy_read_timeout Increase** | Improved connection stability | Increased resource occupancy time |

### Recommended Configuration Combination

Best approach: Add X-Accel-Buffering: no to response headers to disable buffering only for SSE responses:

**Essential Headers:**

- `Content-Type: text/event-stream`
- `Cache-Control: no-cache`
- `X-Accel-Buffering: no`

**Additional Considerations:**  
Recommend implementing a ping mechanism to prevent connections from lasting too long.

## 5. Conclusion

**ERR_INCOMPLETE_CHUNKED_ENCODING** errors mostly result from conflicts between Nginx proxy buffering and SSE chunked encoding. A single **X-Accel-Buffering: no** header solves it and doesn't affect other API performance—the cleanest solution.

In actual projects, consider **timeout settings** and **ping mechanisms** together for stable real-time communication implementation.

---

## References

- Nginx SSE Configuration Guide - Server Fault
- Nopebook Team SSE Implementation and Troubleshooting
- Spring Server-Sent-Events Implementation - Tecoble
- X-Accel-Buffering Header Application
- MDN Server-sent Events Official Documentation
- <https://velog.io/@damongsanga/ERRINCOMPLETECHUNKEDENCODING-SSE-통신-끊어짐-에러-해결-Nginx-Springboot-설정>
