---
title: "Reverse Proxy Introduced"
date: 2024-05-27T12:08:52+09:00
slug: "102-Reverse-Proxy-Introduced"
original_url: "https://memoryhub.tistory.com/102"
tistory_id: 102
draft: false
categories: ["Dev Ops"]
tags: ["Nginx"]
---

*A reverse proxy is a server that sits between client devices and backend servers, forwarding client requests to appropriate servers and then returning the server's response to the client, enhancing load balancing, security, and performance.*

### The Big Picture

Imagine a large hotel with a concierge desk. When guests arrive, they don't go directly to their rooms or different facilities. Instead, they first interact with the concierge, who directs them to the right place, be it a room, restaurant, or gym. Similarly, a reverse proxy acts as the "concierge" of a network, directing client requests to the appropriate backend servers.

### Core Concepts

1. **Client-Server Model**: In a typical client-server model, clients (like web browsers) send requests directly to a server. A reverse proxy changes this interaction by sitting between the clients and servers.
2. **Load Balancing**: Distributing incoming requests across multiple servers to prevent any single server from becoming overwhelmed.
3. **Security**: Adding an additional layer to filter malicious traffic, mask backend server details, and implement SSL/TLS encryption.
4. **Caching**: Storing copies of responses to serve repeated requests more quickly.
5. **Anonymity**: Hiding the identity and structure of the backend servers from clients.

### Detailed Walkthrough

#### How a Reverse Proxy Works

When a client sends a request (e.g., to load a webpage), the reverse proxy receives the request first. It then determines which backend server is best suited to handle the request based on factors like server load and availability. After forwarding the request to the selected server, the reverse proxy receives the server’s response and sends it back to the client. This process is transparent to the client, which interacts with the reverse proxy as if it were the actual server.

#### Load Balancing

A reverse proxy can distribute incoming requests across multiple servers. For example, if you have three servers handling requests for a popular website, the reverse proxy can direct each incoming request to the least busy server, ensuring even distribution of traffic and preventing any single server from becoming a bottleneck.

#### Security

Reverse proxies enhance security by acting as a barrier between clients and backend servers. They can filter out malicious traffic, provide SSL/TLS encryption to protect data in transit, and mask the IP addresses of backend servers to make it harder for attackers to target them directly.

#### Caching

Reverse proxies can store copies of frequently requested resources, like images or web pages. When a client requests a cached resource, the reverse proxy can serve it directly without querying the backend server, reducing load and speeding up response times.

#### Anonymity

By handling all client requests and responses, a reverse proxy hides the details of backend servers. Clients only interact with the reverse proxy, not knowing the internal structure of the network. This can provide additional security and flexibility in managing the backend infrastructure.

### Understanding Through an Example

Consider a large e-commerce site with multiple servers handling different functions—one for the main website, another for the checkout process, and a third for user account management.

1. A user visits the website and requests a product page.
2. The reverse proxy receives this request.
3. Based on the request type, the reverse proxy forwards it to the server responsible for handling product pages.
4. The server processes the request and sends the response back to the reverse proxy.
5. The reverse proxy delivers the response to the user.

If multiple users request the same product page, the reverse proxy can cache the page and serve it directly, reducing the load on the product page server.

### Conclusion and Summary

A reverse proxy acts like a concierge in a large hotel, efficiently directing client requests to the appropriate backend servers, enhancing load balancing, security, caching, and anonymity. By sitting between clients and servers, it ensures that the network runs smoothly and efficiently.

### Test Your Understanding

1. What are the primary functions of a reverse proxy?
2. How does a reverse proxy improve security?
3. Can you explain how caching works in the context of a reverse proxy?

### Reference

For more detailed information, you can explore the [NGINX reverse proxy documentation](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/).
