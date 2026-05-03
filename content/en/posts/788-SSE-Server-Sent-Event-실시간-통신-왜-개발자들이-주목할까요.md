---
title: "SSE (Server-Sent Event) Real-Time Communication: Why Developers Are Paying Attention"
date: 2025-09-23T18:34:25+09:00
slug: "788-SSE-Server-Sent-Event-실시간-통신-왜-개발자들이-주목할까요"
original_url: "https://memoryhub.tistory.com/788"
tistory_id: 788
draft: false
---

```
    🌐 New Horizon of Real-Time Communication
   ┌─────────────────────────┐
   │   Client (Browser)      │
   │         ↑              │
   │    📱 Real-Time Push   │
   │         │              │  
   └─────────┴─────────────────┘
           Server (SSE)
```

While implementing notification features at work, I discovered an unexpected problem: **300,000 unnecessary API calls daily** from polling every 30 seconds. After improving with SSE, I achieved a remarkable **78% API call reduction**.

Let me provide a complete breakdown of what SSE is, when to use it, how to implement it, based on hands-on production experience.

After reading this guide, you'll master everything from real-time communication fundamentals to actual implementation.

## Table of Contents

1. Background - Why Real-Time Communication is Needed
2. Core Concepts Explained
3. Practice - Implementing SSE
4. Best Practices
5. Conclusion & References

---

## 1. Background

Traditional HTTP communication works when clients request and servers respond. Modern web applications, however, frequently need **real-time notifications, stock tickers, chat messages** and other server-to-client proactive data transmission.

### Problems with Existing Solutions

| Method | Advantages | Disadvantages |
| --- | --- | --- |
| **Polling** | Simple implementation | Excessive unnecessary requests, resource waste |
| **WebSocket** | Bidirectional communication possible | Complex implementation, heavy TCP-based |
| **Long Polling** | More efficient than polling | Server resources occupied for extended periods |

SSE emerged to solve these problems—**HTTP-based one-way real-time communication** technology. Servers actively push data to clients, eliminating unnecessary requests and ensuring real-time performance.

## 2. Core Concepts

> **SSE (Server-Sent Events) is a one-way real-time communication technology enabling servers to send events to clients through HTTP.**

### Core Features of SSE

✅ **HTTP-Based**: Leverages existing web infrastructure  
✅ **One-Way Communication**: Server → Client only  
✅ **Automatic Reconnection**: Browser automatically recovers from disconnects  
✅ **Event Stream**: Uses `text/event-stream` MIME type  
✅ **Browser Support**: EventSource API provided by all major browsers

```
// Client-side basic structure
const eventSource = new EventSource('/api/notifications');
eventSource.onmessage = (event) => {
    console.log('Received data:', event.data);
};
```

## 3. Practice

### ① Server Setup (Node.js Express)

```
app.get('/api/sse', (req, res) => {
    // Set SSE response headers
    res.writeHead(200, {
        'Content-Type': 'text/event-stream',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive'
    });

    // Real-time data transmission
    const sendEvent = (data) => {
        res.write(`data: ${JSON.stringify(data)}\n\n`);
    };

    sendEvent({ message: 'Connection successful!' });
});
```

### ② Client Implementation (JavaScript)

```
const eventSource = new EventSource('/api/sse');

eventSource.onopen = () => {
    console.log('SSE connection successful');
};

eventSource.onmessage = (event) => {
    const data = JSON.parse(event.data);
    // DOM update logic
    updateNotification(data);
};

eventSource.onerror = (error) => {
    console.error('SSE connection error:', error);
};
```

### ③ Connection Testing

In developer tools Network tab, you can confirm `EventStream` type connections. Normal connections show continuous data streams.

## 4. Best Practices

### Key Pattern Guide

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| **Real-Time Notifications** | 78% API reduction vs. polling | Connection count limits consideration |
| **Live Feed** | Immediate delivery guaranteed | Memory leak prevention |
| **Status Monitoring** | Minimal server load | Timeout configuration |

### Practical Tips

**DB Connection Pool Exhaustion Caution**: SSE maintains HTTP connections, requiring JPA's `open-in-view` property set to `false`.

**Nginx Configuration**: For SSE responses, set `proxy_buffering off` or response header `X-Accel-Buffering: no` to disable buffering.

## 5. Conclusion

SSE is a powerful tool for **real-time one-way communication** without complex WebSocket implementation. Particularly for notifications, news feeds, and monitoring dashboards, expect **70-80% traffic reduction** compared to polling.

Note that HTTP/1.1 limits 6 connections per domain; HTTP/2 adoption recommended for large-scale services.  
**In production, always implement automatic reconnection and error handling for reliability.**

**References**  
• [MDN Server-Sent Events Official Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)  
• [SSE Real-World Implementation - Sionic.ai](https://blog.sionic.ai/server-sent-event)  
• [WebSockets vs SSE Comparison - Ably](https://ably.com/blog/websockets-vs-sse)
