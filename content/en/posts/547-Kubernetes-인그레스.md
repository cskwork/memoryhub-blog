---
title: "Kubernetes Ingress"
date: 2025-04-13T11:57:40+09:00
slug: "547-Kubernetes-인그레스"
original_url: "https://memoryhub.tistory.com/547"
tistory_id: 547
draft: false
categories: ["Dev Ops"]
tags: ["Kubernetes"]
---

Welcome to the world of Kubernetes! Have you ever wondered how to make it easy for external users to access the multiple services you've created? Just like an information desk at a large shopping mall entrance guiding visitors to their desired stores, Kubernetes needs a gatekeeper to intelligently connect external requests to various internal services. That's exactly what **Ingress** does! Today, let's understand what Ingress is and why it's needed in a simple and enjoyable way!

## What is Kubernetes Ingress?

**Ingress** is a Kubernetes API object that manages external HTTP/HTTPS access to services running within a cluster. It acts as an intelligent router or load balancer that directs incoming traffic to appropriate backend services based on rules you define.

### The Problem Ingress Solves

Before Ingress, exposing Kubernetes services to external traffic had limitations:

**Using NodePort:**
- Exposes service on a high port (30000-32767) on each node
- Users must remember and type the port (e.g., http://example.com:30500)
- Managing multiple services requires managing multiple ports
- Not user-friendly

**Using LoadBalancer:**
- Requires a LoadBalancer service for each application
- Creates separate load balancers (costs add up!)
- Difficult to manage multiple applications

**Solution: Ingress**
- Single entry point for all HTTP/HTTPS traffic
- Route based on hostnames and paths
- Manage SSL/TLS certificates centrally
- One ingress controller manages multiple services
- Much more user-friendly and cost-effective

## Ingress Architecture

```
                    User Request
                         |
                    www.myapp.com
                         |
                         v
                   ┌─────────────┐
                   │  Ingress    │
                   │  Controller │
                   └─────────────┘
                         |
        ┌────────────────┼────────────────┐
        |                |                |
        v                v                v
   ┌─────────┐    ┌─────────┐    ┌─────────┐
   │Service1 │    │Service2 │    │Service3 │
   └─────────┘    └─────────┘    └─────────┘
        |                |                |
        v                v                v
  ┌──────────┐     ┌──────────┐    ┌──────────┐
  │Pods (App1)│   │Pods (App2)│   │Pods (App3)│
  └──────────┘     └──────────┘    └──────────┘
```

## Ingress Components

### 1. Ingress Resource
Kubernetes manifest defining routing rules:
- Hostnames (domains)
- URL paths
- Backend services
- TLS certificates
- etc.

### 2. Ingress Controller
Component that implements the Ingress:
- Watches Ingress resources
- Configures load balancer/reverse proxy
- Common controllers: NGINX, HAProxy, Traefik, etc.
- Must be installed separately in the cluster

## Ingress Resource Example

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    kubernetes.io/ingress.class: "nginx"
spec:
  rules:
  - host: "api.myapp.com"
    http:
      paths:
      - path: /users
        pathType: Prefix
        backend:
          service:
            name: user-service
            port:
              number: 8080
      - path: /products
        pathType: Prefix
        backend:
          service:
            name: product-service
            port:
              number: 8080
  - host: "www.myapp.com"
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 3000
  tls:
  - hosts:
    - api.myapp.com
    - www.myapp.com
    secretName: myapp-tls-cert
```

## Key Features Explained

### 1. Host-based Routing
Route traffic to different services based on hostname:
```yaml
- host: "api.example.com"
- host: "web.example.com"
```

### 2. Path-based Routing
Route traffic to different services based on URL path:
```yaml
- path: /api
  backend: api-service
- path: /static
  backend: static-service
```

### 3. TLS/SSL Support
Secure HTTPS connections:
```yaml
tls:
- hosts:
  - example.com
  secretName: tls-secret
```

### 4. Default Backend
Fallback service for unmatched requests:
```yaml
defaultBackend:
  service:
    name: default-service
    port:
      number: 80
```

## Setting Up Ingress

### Step 1: Install Ingress Controller
```bash
# For NGINX Ingress Controller
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.0.0/deploy/static/provider/baremetal/deploy.yaml
```

### Step 2: Create Ingress Resource
```bash
kubectl apply -f ingress.yaml
```

### Step 3: Configure DNS
Point your domain to the Ingress IP:
```bash
# Get Ingress IP
kubectl get ingress

# Add DNS record pointing domain to Ingress IP
```

## Ingress vs Service Types

| Feature | Ingress | NodePort | LoadBalancer |
| --- | --- | --- | --- |
| Protocol | HTTP/HTTPS | Any | Any |
| URL Routing | Yes (host/path based) | No | No |
| TLS Management | Yes (centralized) | No | Requires external setup |
| Cost | Low (one ingress multiple services) | Medium | High (one LB per service) |
| User Experience | Excellent (memorable URLs) | Poor (remembering ports) | Good |
| Complexity | Medium | Low | High |

## Common Ingress Controllers

1. **NGINX Ingress**: Most popular, feature-rich
2. **Traefik**: Cloud-native, dynamic configuration
3. **HAProxy**: High performance, reliable
4. **Istio**: Advanced service mesh features
5. **Kong**: API gateway functionality

## Best Practices

1. **Use meaningful hostnames**: map-api.myapp.com, www.myapp.com
2. **Organize rules logically**: Group related services
3. **Use TLS everywhere**: Secure all traffic
4. **Monitor ingress**: Track request rates, errors
5. **Use annotations wisely**: For controller-specific features
6. **Plan capacity**: Ingress controller can become bottleneck
7. **Use health checks**: Ensure backends are available

## Advanced Features

### URL Rewriting
Modify request paths before forwarding to backend:
```yaml
annotations:
  nginx.ingress.kubernetes.io/rewrite-target: /
```

### Rate Limiting
Control request rates:
```yaml
annotations:
  nginx.ingress.kubernetes.io/limit-rps: "10"
```

### CORS Configuration
Handle cross-origin requests:
```yaml
annotations:
  nginx.ingress.kubernetes.io/enable-cors: "true"
```

## Conclusion

Kubernetes Ingress is the gateway between your cluster and the outside world. It transforms how external users access your services from awkward port-based URLs to clean, memorable domain names. With proper Ingress configuration:

- Users enjoy seamless access to your applications
- Operations become simplified with centralized routing
- SSL/TLS management becomes straightforward
- Your infrastructure scales gracefully

Start with basic host and path-based routing, then explore advanced features as your needs grow. Ingress is a foundational component of any production Kubernetes deployment.

Happy routing!
