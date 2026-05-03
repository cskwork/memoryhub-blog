---
title: "Connecting Local Ollama from Docker Container: Why host.docker.internal is the Answer"
date: 2025-09-16T09:01:13+09:00
slug: "779-Docker-컨테이너에서-로컬-Ollama-연결-왜-host-docker-internal이-답일까"
original_url: "https://memoryhub.tistory.com/779"
tistory_id: 779
draft: false
---

```
    ┌─────────────────────────────────────┐
    │         Host Machine                │
    │  ┌─────────────────────────────┐    │
    │  │       Ollama                │    │
    │  │    localhost:11434          │    │
    │  └─────────────────────────────┘    │
    │              ▲                      │
    │              │                      │
    │   host.docker.internal:11434        │
    │              │                      │
    │  ┌─────────────────────────────┐    │
    │  │    Docker Container         │    │
    │  │   ┌─────────────────────┐   │    │
    │  │   │   Your App          │   │    │
    │  │   │                     │   │    │
    │  │   └─────────────────────┘   │    │
    │  └─────────────────────────────┘    │
    └─────────────────────────────────────┘
```

Have you ever tried running an application in a Docker container and connecting to locally installed Ollama using localhost:11434, only to have the connection fail? I was confused at first too, but the solution turned out to be simpler than expected.

After reading this guide, you'll understand Docker's network architecture and master how to perfectly connect to your local Ollama from a container using host.docker.internal.

## Table of Contents

1. Background
2. Core Concepts Explained
3. Practice
4. Best Practices
5. Conclusion & References

---

## 1. Background

When trying to connect Docker containers to locally hosted Ollama (port 11434), network connection failures commonly occur. Many developers use localhost:11434 only to encounter "Connection refused" errors.

**Root Causes of the Problem:**

- Docker containers have isolated network environments
- Localhost within a container refers to the container itself, not the host's services
- Traditional port forwarding methods don't resolve this reverse connection issue

**Terminology:**

| Term | Definition |
| --- | --- |
| **Ollama** | A tool for running LLMs locally, using port 11434 by default |
| **host.docker.internal** | A special hostname provided by Docker that allows containers to access the host (local machine) |
| **Docker Bridge Network** | Default network enabling multiple containers on a single host to communicate with each other |

## 2. Core Concepts

> **One-Line Definition**  
> **host.docker.internal is a special domain that Docker containers use instead of localhost to access the host system.**

Docker containers have isolated network environments, so accessing host network resources from within a container requires specific methods. On Mac or Windows, containers can access the host via the DNS name host.docker.internal by default.

```
# docker-compose.yml example
version: '3.8'
services:
  my-app:
    image: my-app
    environment:
      - OLLAMA_BASE_URL=http://host.docker.internal:11434
```

## 3. Practice

### ① Environment Verification and Preparation

First, verify that Ollama is running properly on your local machine:

```
# Check Ollama service status
curl http://localhost:11434/api/version

# Example successful response
{"version":"0.1.26"}
```

### ② Default Setup on Windows/Mac

On Windows 11, simply use http://host.docker.internal:11434 as the Base URL.

```
# Docker container execution example
docker run -d \
  -e OLLAMA_API_BASE_URL=http://host.docker.internal:11434 \
  -p 8080:8080 \
  your-app:latest
```

### ③ Additional Configuration on Linux

Linux doesn't support host.docker.internal by default, requiring separate setup.

```
# Enable host.docker.internal on Linux
docker run -d \
  --add-host=host.docker.internal:host-gateway \
  -e OLLAMA_API_BASE_URL=http://host.docker.internal:11434 \
  -p 8080:8080 \
  your-app:latest
```

### ④ Docker Compose Configuration

```
# docker-compose.yml
version: '3.8'
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "8080:8080"
    extra_hosts:
      - "host.docker.internal:host-gateway"  # Linux support
    environment:
      - OLLAMA_BASE_URL=http://host.docker.internal:11434
    volumes:
      - open-webui:/app/backend/data
    restart: always

volumes:
  open-webui:
```

### ⑤ Connection Test

```
# Test connection from within the container
docker exec -it your-container-name curl http://host.docker.internal:11434/api/tags

# On success, the list of Ollama models is returned
```

## 4. Best Practices

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| **Using host.docker.internal** | Cross-platform compatibility, simple setup | Development-only; won't work in production |
| **Network bridge mode** | Performance optimization, better isolation | Complex configuration required |
| **Ollama inside container** | Complete isolation, simplified deployment | Redundant resources, larger image size |

**Environment-Specific Recommendations:**

- **Development**: Use host.docker.internal for rapid development
- **Staging**: Network bridge or separate Ollama container
- **Production**: Completely separate Ollama service or container-internal installation

**Troubleshooting Checklist:**

1. Verify Ollama service is listening on 0.0.0.0:11434
2. Check that port 11434 is open in your firewall
3. On Linux, add --add-host=host.docker.internal:host-gateway option
4. Check container logs for specific error messages

## 5. Conclusion

The key to connecting local Ollama from Docker containers is leveraging host.docker.internal. This is Docker's standard mechanism for containers in isolated network environments to access host system resources. While Linux requires additional setup, once configured, it works reliably.

**Real-World Application Tip**: Use environment variables to separate development/production environments, and leverage Docker Compose's extra_hosts setting to ensure cross-platform compatibility.

---

**References**

- Ollama Official Docker Image Guide
- Stack Overflow: Troubleshooting Ollama Connection in Docker Containers
- Docker Networking and host.docker.internal Detailed Guide
