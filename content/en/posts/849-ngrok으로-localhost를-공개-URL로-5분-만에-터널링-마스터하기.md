---
title: "Make localhost public with ngrok! Master tunneling in 5 minutes"
date: 2025-10-12T23:23:39+09:00
slug: "849-ngrok으로-localhost를-공개-URL로-5분-만에-터널링-마스터하기"
original_url: "https://memoryhub.tistory.com/849"
tistory_id: 849
draft: false
---

```
    ╔══════════════════════════════════════╗
    ║                                      ║
    ║   [Localhost] ←→ [ngrok] ←→ [?]    ║
    ║                                      ║
    ║   Magic tunneling tool to           ║
    ║   instantly expose local servers    ║
    ║                                      ║
    ╚══════════════════════════════════════╝
```

Ever felt stuck trying to test webhooks? Need to quickly share API results with a frontend developer but deployment is too cumbersome? That's when ngrok comes in. Open just one port in your local environment, and an HTTPS URL accessible from anywhere in the world is generated. After reading this guide, you'll become a tunneling expert in just 5 minutes, from installation to real-world usage.

**The fastest way to safely expose a local server to the public internet beyond the firewall**

## Background

### Why choose ngrok?

ngrok is reverse proxy tunneling software that converts localhost into a publicly accessible URL. In development environments where external access is needed, it can be used immediately without port forwarding or server deployment.

### Key use scenarios

| Scenario | ngrok Usage |
| --- | --- |
| Webhook testing | Receive callbacks from external APIs to local server |
| Mobile app development | Test local backend on actual devices |
| Client demo | Instantly share local work without deployment |
| Social login development | Need public domain for OAuth redirect URL |
| API integration testing | Integrate external services with local environment |

### Core terminology

**Tunneling**: Technology that allows external access to internal networks by passing through network firewalls

**Reverse proxy**: Intermediate server that receives external requests and forwards them to internal servers

**Port forwarding**: Method to expose specific ports to the outside through router settings (ngrok eliminates this need)

## Core Concept

> ngrok is a tool that immediately exposes local servers behind NAT and firewalls to the public internet through secure tunnels

ngrok creates HTTP tunnels to instantly expose localhost to the internet, making it essential for webhook testing, API development, and building region-specific development environments.

**Key Features**

- Support for HTTP/HTTPS/TCP protocols to handle various server types
- Automatic HTTPS certificate generation providing secure connections
- Real-time traffic monitoring and replay functionality through web console (http://127.0.0.1:4040)
- Free plan supports 120 TCP connections per minute

**How it works**

The ngrok client creates a secure tunnel between local server and ngrok cloud server. External requests pass through the ngrok server and are forwarded to localhost via this tunnel.

## Hands-on Practice

### Step 1: Installation

**Mac environment (Homebrew)**

```
brew install ngrok
```

**Windows environment**

Download Windows zip file from official website (https://ngrok.com/) and extract

**Linux environment**

```
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
sudo tee /etc/apt/sources.list.d/ngrok.list && \
sudo apt update && sudo apt install ngrok
```

### Step 2: Register authentication token

By default, ngrok has a session expiration period, and the URL changes when the session expires. For stable use, sign up and register your authentication token.

1. Sign up at https://dashboard.ngrok.com/signup
2. Check Auth Token in the dashboard
3. Register token in terminal

```
ngrok authtoken [Your_Authtoken]
```

Verify token registration:

```
ngrok config edit
```

### Step 3: Create local server tunnel

Start ngrok while running the server locally.

**Basic usage**

```
# If running HTTP server on port 8080
ngrok http 8080
```

**Output screen**

The terminal will display information like this:

```
Session Status         online
Account                Your Name (Plan: Free)
Version                3.3.1
Region                 Japan (jp)
Web Interface          http://127.0.0.1:4040
Forwarding             https://abc123.ngrok-free.app -> http://localhost:8080
```

The URL shown on the Forwarding line (e.g., https://abc123.ngrok-free.app) is the external access address.

### Step 4: Monitor traffic

Visit http://127.0.0.1:4040 to see the ngrok web interface where you can monitor status and HTTP request activity in real-time.

Main features of web interface:

- View all HTTP request/response headers and body
- Replay function to resend specific requests
- Connection statistics and performance metrics

### Step 5: Database port tunneling

Beyond web servers, you can also tunnel database ports like MySQL and PostgreSQL:

```
# MySQL
ngrok tcp 3306

# PostgreSQL
ngrok tcp 5432

# MongoDB
ngrok tcp 27017
```

## Best practices and pattern comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Free plan usage | Get started instantly at no cost, provides 120 connections per minute | URL changes at session end, no fixed domain |
| Auth token registration | Unlimited session time, provides 1 free fixed domain | Requires signup |
| Web interface usage | Real-time debugging, improved development efficiency with request replay | Conflicts if local port 4040 is in use |
| TCP tunneling | Support for protocols other than HTTP like databases | Security configuration required (authentication, IP restrictions) |
| Paid plan usage | Custom domain, run multiple tunnels simultaneously | Monthly cost incurred |

## Conclusion

ngrok is the simplest solution for instantly exposing your local development environment to the outside world. An HTTPS secure tunnel is created with a single command without port forwarding configuration, significantly improving development productivity in various scenarios from webhook testing to client demos.

ngrok is an essential tool when you need to test webhook functionality or debug external API integration.

## References

- ngrok official website (https://ngrok.com/)
- ngrok official documentation (https://ngrok.com/docs)
- ngrok dashboard (https://dashboard.ngrok.com/)
- Outsider's Dev Story - Opening tunnels in local networks with ngrok (https://blog.outsider.ne.kr/1159)
- Aliencube - Tools for testing webhooks (https://blog.aliencube.org/ko/2017/06/02/tools-for-testing-webhooks/)
