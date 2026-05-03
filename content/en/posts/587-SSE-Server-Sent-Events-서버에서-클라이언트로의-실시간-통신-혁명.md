---
title: "SSE (Server-Sent Events) - Real-time Communication Revolution from Server to Client!"
date: 2025-05-14T16:36:19+09:00
slug: "587-SSE-Server-Sent-Events-서버에서-클라이언트로의-실시간-통신-혁명"
original_url: "https://memoryhub.tistory.com/587"
tistory_id: 587
draft: false
---

*Have you ever seen websites that display stock prices or notifications in real-time? Ever wondered how it works without refreshing? Today, we'll explore SSE, one of the secrets behind this magic!*

## Background

In traditional web communication, the client (browser) sent requests to the server, and the server responded with data. However, this approach had several limitations when displaying real-time data.

In the past, real-time data was handled in the following ways:

1. **Full page refresh**: In the 90s, pages or frames were refreshed periodically.
2. **Polling**: Ajax was used to request data from the server periodically.
3. **Long Polling**: The connection was maintained until the server responded.

However, these methods resulted in unnecessary requests and server load. That's why HTML5 introduced SSE (Server-Sent Events) to enable one-way communication from server to client. SSE was first specified as part of WHATWG Web Applications 1.0 starting in 2004 and is now supported by most modern browsers.

[Problems SSE solves]:

1. **Real-time updates**: The server can push data to the client at any time.
2. **Network efficiency**: Unlike periodic polling, data is transmitted only when needed.
3. **Automatic reconnection**: Automatically reconnects if the connection drops.

## Core Principles

SSE's operational principle is simple. Basically, the server streams events through an open HTTP connection between the server and client.

```
Client                                    Server
   |                                         |
   |--- HTTP Request (Create EventSource) -->|
   |                                         |
   |<---- HTTP Response (Infinite Stream) ---|
   |                                         |
   |<---- Event Data 1 ----------------------|
   |                                         |
   |<---- Event Data 2 ----------------------|
   |                                         |
   |       (Connection maintained)           |
```

**Client-side Code Example (JavaScript):**

```javascript
// Connect to server using EventSource interface
const eventSource = new EventSource('/events');

// Add message event listener
eventSource.onmessage = function(event) {
  console.log('New message:', event.data);
  // Update UI with received data
};

// Connection open event
eventSource.onopen = function() {
  console.log('Connected');
};

// Error handling
eventSource.onerror = function() {
  console.error('SSE connection error');
};

// Receive specific event type
eventSource.addEventListener('customEvent', function(e) {
  console.log('Custom event:', e.data);
});

// Close connection (if needed)
// eventSource.close();
```

**Server-side Code Example (Node.js/Express):**

```javascript
const express = require('express');
const app = express();

app.get('/events', (req, res) => {
  // Set headers required for SSE setup
  res.writeHead(200, {
    'Content-Type': 'text/event-stream',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive'
  });

  // Send comment for connection maintenance (optional)
  setInterval(() => {
    res.write(': Connection keep-alive comment\n\n');
  }, 15000);

  // Example of data transmission
  let count = 0;
  const intervalId = setInterval(() => {
    count++;
    // Set event ID (used for reconnection)
    res.write(`id: ${count}\n`);
    // Specify event type (optional)
    res.write('event: message\n');
    // Actual data
    res.write(`data: {"count": ${count}, "time": "${new Date().toISOString()}"}\n\n`);
  }, 1000);

  // Cleanup when client connection closes
  req.on('close', () => {
    clearInterval(intervalId);
    console.log('Client connection closed');
  });
});

app.listen(3000, () => {
  console.log('Server started: http://localhost:3000');
});
```

**SSE Message Format** (transmitted from server to client):

```
id: EventID
event: EventType
data: Actual data content
retry: Reconnection time (milliseconds)
```

Each message is separated by two empty lines (`\n\n`).

## SSE vs WebSocket Comparison

| Feature | SSE | WebSocket |
| --- | --- | --- |
| Protocol | HTTP | WS/WSS |
| Communication Direction | One-way (server→client) | Two-way |
| Implementation Complexity | Simple | Complex |
| Automatic Reconnection | Natively supported | Must implement manually |
| Data Format | Text (UTF-8) | Text/Binary |
| Firewall Compatibility | Good | Possible restrictions |
| Concurrent Connections | 6 per browser (HTTP/1.1) | More connections possible |

## Cautions and Tips

⚠️ **Watch out for these!**

1. **Connection Limit**
   - HTTP/1.1 has a 6-connection limit per domain per browser.
   - Solution: Up to 100 connections possible when using HTTP/2.
2. **Memory Management**
   - Memory leaks can occur when managing many connections on the server.
   - Solution: Always clean up resources when connections terminate (clearInterval, etc.).
3. **Data Format Limitation**
   - SSE can only transmit text (UTF-8) data.
   - Solution: Encode binary data in base64 or consider using WebSocket.

💡 **Pro Tips**

- Sending periodic empty comments (`: comment\n\n`) from the server prevents connection drops.
- Using event IDs allows you to receive missed messages when the connection drops and reconnects.
- Using the `withCredentials` option on the `EventSource` object allows you to include cookies in CORS requests.
- Monitoring SSE connections in the network tab during development helps with debugging.

## SSE Use Cases

SSE is suitable for the following real-time applications:

1. **Real-time notifications** - Social media notifications, email arrival alerts
2. **Real-time dashboards** - Stock prices, sports scores, server monitoring
3. **Collaboration tools** - Document updates, collaborative editing status
4. **Chat applications** - One-way announcements
5. **Progress updates** - File uploads, long-running task processing status

## Conclusion

We've explored SSE (Server-Sent Events) today. If you need one-way real-time communication and a simple implementation solution, SSE is an excellent choice. Use WebSocket if you need two-way communication, or SSE if you only need simple one-way updates.

SSE is easy to understand and implement, but in real production environments, there are additional considerations like scaling, security, and authentication. Nevertheless, in appropriate use cases, it's a very effective real-time communication method!

## Reference Materials

- [MDN: Server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- [MDN: Using server-sent events](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events)
- [DigitalOcean: How To Use SSE in Node.js](https://www.digitalocean.com/community/tutorials/nodejs-server-sent-events-build-realtime-app)
- [Mastering JS: Server-Sent Events with Express](https://masteringjs.io/tutorials/express/server-sent-events)

---

#SSE #ServerSentEvents #RealtimeCommunication #WebDevelopment #HTML5
