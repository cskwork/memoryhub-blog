---
title: "Everything about Nginx: A Lightweight and Powerful Web Server"
date: 2024-11-17T08:57:39+09:00
slug: "384-Nginx의-모든-것_-가볍고-강력한-웹-서버"
original_url: "https://memoryhub.tistory.com/384"
tistory_id: 384
draft: false
---

Hello! Today, let's take a detailed look at **Nginx**, an essential tool that cannot be missing in modern web services. Let's understand Nginx by comparing it to a coffee shop analogy.

- **Customers (Clients)**: The entities sending requests from web browsers or mobile apps
- **Employees (Nginx)**: Receive requests and distribute them appropriately while controlling the processing flow
- **Kitchen (Backend Servers)**: Actually processes requests and generates responses

The Nginx employee, like a coffee shop worker, efficiently handles multiple customers even during busy "peak times". When necessary, distributing work to other employees (servers) provides fast and stable service.

---

## 1. Core Concepts of Nginx?

Nginx is a high-performance server software that can function as both a **web server and a reverse proxy**. As a **"web server"**, it rapidly serves static content (HTML, CSS, JS, images, etc.), and as a **"reverse proxy"**, it acts as an intermediary for backend servers and performs load balancing to distribute server load efficiently.

### What Problems Does It Solve?

- **High-performance Processing**: Efficiently handle numerous concurrent requests to prevent server overload
- **Load Balancing**: Distribute requests across multiple servers to prevent excessive load on specific servers
- **Security & SSL Termination**: Manage certificates for HTTPS connections and serve as an SSL/TLS endpoint
- **Flexible Routing**: Support various routing scenarios including URL mapping, redirection, and API gateway functions

---

## 2. How Does It Work??

Let's dive deeper into how Nginx operates.

### 1) Event-Driven Architecture

Traditional servers (like Apache's prefork method) allocate **'1 process (or thread) per request'**. However, with many incoming requests, processes or threads multiply exponentially, creating significant system burden.

In contrast, **Nginx adopts an event-driven (asynchronous) architecture**.

- **A single employee (worker process) handles events (connections/requests) with non-blocking I/O**, allowing many requests to be processed simultaneously.
- Internally, it uses a **Master-Worker process structure** where the Master process handles configuration file loading and worker process management, while actual request processing is handled by multiple worker processes.

```
# Example
events {
    worker_connections 1024; # Maximum concurrent connections a single worker process can handle
}
```

### 2) Asynchronous Processing and Non-blocking I/O

Nginx detects **read/write events** occurring on network sockets through an event loop, which worker processes handle. By performing data processing **without blocking (Non-blocking)** during request I/O, high concurrency can be achieved.

### 3) Internal Module Structure

- **HTTP Module**: HTTP request processing, static file serving, compression (Gzip), caching, etc.
- **Stream Module**: TCP/UDP traffic proxying and load balancing
- **Mail Module**: Email protocol (SMTP, IMAP, POP3) proxying

Each component can independently add or remove modules like plugins, maintaining a **lightweight and flexible structure**.

---

## 3. Key Features ⭐

1. **Event-Driven Architecture**
   - High concurrent connection handling with minimal resources
   - CPU efficiency maximized through non-blocking I/O
2. **Asynchronous Processing**
   - Worker processes efficiently handle multiple requests
   - High performance and scalability secured
3. **Lightweight Resource Usage**
   - Lower memory and CPU usage compared to traditional web servers (Apache, etc.)
   - Significant cost savings relative to performance

---

## 4. Main Features?

### 1) Static File Serving

Nginx excels at rapidly providing static content (HTML, CSS, JS, images, etc.). The following configuration serves requests coming to the `/images/` path from `/var/www/static` and maintains browser caching for 30 days.

```
location /images/ {
    root /var/www/static;
    expires 30d; # Browser caching for 30 days
}
```

### 2) Load Balancing (Upstream)

When operating multiple backend servers, using Nginx as a load balancer prevents load concentration on a specific server. The following example registers 3 servers in an upstream group called `backend`.

```
upstream backend {
    server backend1.example.com:8080;
    server backend2.example.com:8080;
    server backend3.example.com:8080;
}

server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://backend;
    }
}
```

You can also set **load balancing algorithms** to `least_conn`, `ip_hash`, `weighted round robin`, etc., allowing you to choose the optimal method for your traffic characteristics.

### 3) SSL/TLS Termination

When using HTTPS protocol, if Nginx handles certificate management and SSL/TLS connections, **backend servers can reduce SSL processing burden**.

```
server {
    listen 443 ssl;
    server_name secure.example.com;

    ssl_certificate     /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;

    location / {
        proxy_pass http://backend;
    }
}
```

### 4) URL Rewriting

Useful when routing old-version URLs or specific request patterns to new paths.

```
location /old-page {
    rewrite ^/old-page(.*)$ /new-page$1 permanent;
}
```

---

## 5. Practical Configuration Examples?

### 1) Basic Web Server Configuration

```
http {
    server {
        listen       80;
        server_name  example.com;

        location / {
            root   /var/www/html;
            index  index.html;
        }

        # Enable Gzip compression
        gzip on;
        gzip_types text/plain text/css application/json application/javascript;

        # Error page configuration
        error_page 404 /404.html;
    }
}
```

- **root**: Root directory for serving static files
- **index**: Default document
- **gzip on**: Improve transmission efficiency and reduce page load time
- **error_page 404**: Provide user-friendly error pages

### 2) API Reverse Proxy Configuration

```
location /api/ {
    proxy_pass http://backend;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

- **proxy_pass**: Forward requests coming to `/api/` to the backend server
- **proxy_set_header**: Pass actual host information and client IP to the backend

---

## 6. Performance Optimization Tips?

### 1) Worker Processes and File Descriptor Limits

```
worker_processes auto;
worker_rlimit_nofile 65535;
```

- **worker_processes auto**: Allocate appropriate worker processes according to CPU core count
- **worker_rlimit_nofile**: Increase the maximum number of files (sockets) Nginx can open to prepare for large-scale traffic

### 2) Buffer and Request Size Configuration

```
client_body_buffer_size 10K;
client_max_body_size 8m;
```

- **client_body_buffer_size**: Buffer size for temporarily storing request bodies
- **client_max_body_size**: Limit uploadable request (file) size

### 3) Caching Configuration

```
proxy_cache_path /path/to/cache levels=1:2 keys_zone=my_cache:10m;
location / {
    proxy_cache my_cache;
    proxy_cache_valid 200 1m;
    proxy_cache_valid any 10s;
    proxy_pass http://backend;
}
```

- **proxy_cache_path**: Define caching location, directory structure, key zone, etc.
- **proxy_cache_valid**: Specify caching duration by response code

---

## 7. Precautions ⚠️

1. **Configuration File Syntax Checking**
   - Mistakes like missing semicolons (`;`) and unmatched braces (`{}`) are common
   - Develop the habit of checking for syntax errors with the `nginx -t` command after making configuration changes
2. **Security Configuration**
   - **Hide Version Information**: `server_tokens off;`
   - Block unnecessary HTTP methods (`TRACE`, `TRACK`, etc.)
   - Consider integrating with WAF (Web Application Firewall) or additional security modules
3. **Log Management**
   - Properly rotate logs to manage disk space
   - Adjust `access_log` and `error_log` levels to match your use case
4. **Upstream Health Checks**
   - When load balancing, periodically check the status of backend servers to detect failures
   - Can utilize the `health_check` module or integrate with separate solutions

---

## 8. Closing Remarks?

We've examined Nginx from core concepts through main features, configuration methods, and performance optimization tips.

- Thanks to concurrent processing and event-driven architecture, **high performance and stability** can be secured, and
- By providing various functions like load balancing, SSL/TLS processing, and static file serving simultaneously, **flexible infrastructure construction** is possible.

If you're operating a service requiring high traffic and fast response times, or want to efficiently manage multiple backend servers, **we highly recommend actively considering Nginx**!

---

### Reference Materials and Sources

- **Nginx Official Documentation**: <https://nginx.org/en/docs/>
- **Nginx Blog**: <https://www.nginx.com/blog/>
- **DigitalOcean Nginx Guide**: <https://www.digitalocean.com/community/tutorials?q=nginx>

Remember that with good use of **Nginx**, you can deliver amazing performance even with minimal resources!
