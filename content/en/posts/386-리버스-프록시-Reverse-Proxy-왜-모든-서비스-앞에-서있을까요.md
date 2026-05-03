---
title: "Reverse Proxy, Why Does It Stand in Front of Every Service?"
date: 2024-11-17T09:00:05+09:00
slug: "386-리버스-프록시-Reverse-Proxy-왜-모든-서비스-앞에-서있을까요"
original_url: "https://memoryhub.tistory.com/386"
tistory_id: 386
draft: false
categories: ["Dev Ops"]
tags: ["Nginx"]
---

```
          +------------+      +-------------------+      +-----------------+
          |            |      |                   |      |                 |
User   |  Internet  |   |   Reverse Proxy   |  |  Backend Server |
          |            |      | (e.g., NGINX)     |      |  (e.g., Node.js)|
          +------------+      +-------------------+      +-----------------+
```

Have you ever wondered, "Now that I've deployed my project to `localhost:3000`, how do I safely and quickly make it available for external users?" Exposing the server IP and port directly raises security concerns, and you worry whether the server can handle traffic surges. This is when we meet our reliable gatekeeper.

This article explores reverse proxy (Reverse Proxy), a core technology that secures stability, security, and performance for web services.

TL;DR

- A reverse proxy is a 'intermediary server' that receives client requests on behalf of and forwards them to backend servers.
- This approach achieves three objectives: server load distribution, security enhancement, and performance improvement.

---

### Table of Contents

1. **Background: What is a Proxy?**
2. **Core Concept: How Reverse Proxy Works**
3. **Practice: Building Reverse Proxy with NGINX**
4. **Best Practices: 200% Reverse Proxy Utilization**
5. **Closing & Resources**

---

### 1. Background: What is a Proxy?

To understand reverse proxies, we must first understand the concept of 'proxy'. Proxy means 'representative' in plain language and refers to an intermediary that handles network communication on behalf of clients or servers. Proxies are divided into forward proxies and reverse proxies depending on their role.

- **Forward Proxy (Forward Proxy)**: A representative **for the client**. It's a server that internal network clients pass through when accessing the internet, serving to hide client identity or control access. The server communicates with the proxy server and doesn't know who the real client is.
- **Reverse Proxy (Reverse Proxy)**: A representative **for the server**. When internet clients send requests to web servers, it's a server that receives those requests instead. Clients think the reverse proxy is the real server, while the existence of the actual backend server is hidden from the outside world.

### 2. Core Concept: How Reverse Proxy Works

> **A reverse proxy is an intermediary server positioned between clients and one or more web servers that intercepts all client requests and forwards them to backend servers.**

The operation flow is straightforward.

1. **Request Reception**: When a client (user) sends a request to a web service, the request arrives first at the reverse proxy server, not the backend server.
2. **Request Evaluation and Forwarding**: The reverse proxy analyzes the request. If cached data exists, it responds immediately. Otherwise, according to predetermined rules (routing, load balancing), it forwards the request to the most appropriate backend server.
3. **Response Reception and Forwarding**: The backend server processes the request and sends the response to the reverse proxy.
4. **Final Response**: The reverse proxy ultimately delivers the backend server's response to the client. During this process, it can also cache or compress response data.

Thanks to this structure, clients communicate with a single entry point (reverse proxy) without needing to understand the complex structure of numerous backend servers.

### 3. Practice: Building Reverse Proxy with NGINX

Let's set up a reverse proxy using NGINX, the most popular open-source reverse proxy solution. NGINX is renowned for high performance and low memory usage.

**① Basic Reverse Proxy Configuration**

This example configures a Node.js application running on port 3000 in the local environment to be accessible on port 80.

```
# /etc/nginx/sites-available/default or nginx.conf

server {
    # Listen for requests on port 80.
    listen 80;

    location / {
        # Forward all requests to http://127.0.0.1:3000
        # This is where the actual application is running.
        proxy_pass http://127.0.0.1:3000;

        # Forward client's real IP, protocol, and header information to the backend server.
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**② Load Balancing Application**

Suppose traffic increases and you've expanded to multiple servers. Using the `upstream` directive allows you to distribute incoming requests across multiple servers.

```
http {
    # Define a server group named 'backend_servers'.
    upstream backend_servers {
        # List of servers to distribute requests to.
        # Default strategy is round-robin.
        server 127.0.0.1:3001;
        server 127.0.0.1:3002;
        server 127.0.0.1:3003;
    }

    server {
        listen 80;

        location / {
            # Forward requests to the 'backend_servers' group.
            proxy_pass http://backend_servers;
        }
    }
}
```

Now NGINX fairly distributes requests to ports 3001, 3002, and 3003, preventing load concentration on a single server.

### 4. Best Practices: 200% Reverse Proxy Utilization

Reverse proxies offer advanced features beyond simple request forwarding to significantly enhance service quality.

| Feature | Advantage | Key NGINX Configuration |
| --- | --- | --- |
| **Load Balancing** | Distribute traffic across multiple servers to reduce load and prevent service interruption if a specific server fails. | `upstream` block definition and `proxy_pass` directive |
| **Security Enhancement** | Hide backend server IPs and structure, filter malicious requests. Only the reverse proxy is exposed externally. | `allow` and `deny` directives to control access by specific IPs |
| **SSL/TLS Encryption** | Configure SSL certificates only on the reverse proxy for unified management and reduced encryption/decryption burden on backend servers (SSL Termination). | `listen 443 ssl;` `ssl_certificate` configurations |
| **Caching** | Cache static content (images, CSS, etc.) to increase response speed and significantly reduce backend server load. | `proxy_cache_path` and `proxy_cache` directives |
| **API Gateway** | Serve as a single entry point for multiple APIs in microservice architectures and handle routing and authentication centrally. | Configure `location` blocks differently by path to forward to different backends |

### 5. Closing

The reverse proxy has now become an essential element in modern web architecture, not an option.

- A reverse proxy plays the essential 'gatekeeper' role between clients and servers.
- Beyond simple request forwarding, it provides core functions like load balancing, security, and caching that enhance service stability and performance.
- With powerful tools like NGINX, you can build robust reverse proxy environments without complex configuration.

**Practical Application Tips**: In actual production environments, it's important to configure high availability (High Availability) for the reverse proxy server itself so that service isn't interrupted even if the reverse proxy goes down.

If you found this article helpful, please give us a heart and comment! Your feedback is invaluable in helping us write better content.

---

**References**

- NGINX Reverse Proxy Official Documentation
- Understanding Reverse Proxy (Cloudflare)
- What is Reverse Proxy? (Various sources)

[1] <https://www.cloudflare.com/ko-kr/learning/cdn/glossary/reverse-proxy/>
[2] <https://aday7.tistory.com/entry/%EB%A6%AC%EB%B2%84%EC%8A%A4-%ED%94%84%EB%A1%9D%EC%8B%9CReverse-Proxy-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-%EA%B0%9C%EB%85%90%EB%B6%80%ED%84%B0-%ED%95%84%EC%9A%94%EC%84%B1-%EC%98%A4%ED%94%88-%EC%86%8C%EC%8A%A4-%EC%86%94%EB%A3%A8%EC%85%98%EA%B9%8C%EC%A7%80>
[3] <https://narup.tistory.com/238>
[4] <https://api7.ai/ko/learning-center/api-gateway-guide/api-gateway-vs-reverse-proxy-vs-load-balancer>
[5] <https://brightdata.com/blog/proxy-101/reverse-proxy-defined>
[6] <https://en.wikipedia.org/wiki/Reverse_proxy>
