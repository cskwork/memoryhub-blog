---
title: "Kubernetes Ingress - the core of managing external cluster traffic"
date: 2025-04-23T13:29:57+09:00
slug: "559-쿠버네티스-인그레스-Ingress-클러스터-외부-트래픽-관리의-핵심"
original_url: "https://memoryhub.tistory.com/559"
tistory_id: 559
draft: false
---

Hello Kubernetes travelers! Have you ever felt overwhelmed while trying to configure access from outside the cluster to internal services? Like a building security guard managing multiple doors, connecting multiple services to the external world is quite a challenging task. Today, let's explore Kubernetes' clever gatekeeper, **Ingress**, in an easy and fun way!

## Background: Once upon a time, traffic management was... 

Before Kubernetes emerged, or before the Ingress concept was established, accessing services inside a cluster from outside typically required two methods.

1. **NodePort**: Opens a specific port on each node (server), and when external requests come to that port, they're forwarded to a designated service. It's like opening multiple side doors from each room to the outside. As the number of managed ports increases, and when a node's IP changes, external access addresses have to change too, which is inconvenient.
2. **LoadBalancer (cloud-provided)**: Creates a load balancer from cloud service providers (AWS, GCP, Azure, etc.) to distribute external requests to services. It's the most stable and convenient, but each service might need a separate load balancer, which can increase costs.

These methods work fine in small environments, but as services increase and become more complex, management points multiply and costs rise. The question "Can't we neatly split incoming requests from a single external IP and port to multiple internal services?" led to the emergence of Ingress!

## Ingress characteristics/uses: What does it solve?

Ingress is a set of rules that connects HTTP/HTTPS requests coming from outside the cluster to internal services. Like an intelligent traffic officer, it looks at the address (hostname) or path of incoming requests and directs them to the appropriate service. Here are the main problems Ingress solves:

1. **Provides a single entry point**: Multiple services don't need their own external IPs or ports; instead, Ingress receives external requests through a single IP address and port. Management points are reduced and external exposure is minimized.
2. **URL-based routing (Path/Host-based Routing)**: Requests can be forwarded to different services based on the hostname (`mysite.com`, `api.mysite.com`) or path (`/login`, `/products`) in the request URL. For example, `mysite.com/login` goes to the login service, while `mysite.com/products` goes to the product listing service.
3. **SSL/TLS termination**: Handles HTTPS requests at the Ingress level, and services inside the cluster can communicate with unencrypted HTTP. This reduces the burden of configuring and managing SSL certificates for each service.
4. **Load balancing**: Ingress performs load balancing by distributing incoming requests across multiple pods, either directly or through connected services.

## Core principle: How does Ingress work?

For Ingress to actually work, two core components are needed:

1. **Ingress Resource**: A Kubernetes object created by users. It defines rules for how external requests should be routed to services. For example, you might write a rule like "forward requests coming to example.com/api to the api-service" in a YAML file and apply it to Kubernetes. Think of this as a 'request' or 'configuration directive'.
2. **Ingress Controller**: The actual _application_ that receives external requests and routes traffic according to the rules defined in the Ingress resource. Just creating an Ingress resource doesn't cause anything to happen! This controller must be running in the cluster. There are various types of Ingress controllers like Nginx, HAProxy, and Traefik. This controller usually runs behind a load balancer service that has an IP accessible from outside the cluster.

**Traffic flow visualization:**

```
# External request (user)
External Request (User @ Internet)
      |
      v
+-----------------------+
|  Load Balancer (Cloud)|  <-- IP/Port where Ingress controller is exposed
| (e.g., AWS ELB, GCP LB)|
+-----------------------+
      |
      v
+-------------------------------------------------+
| Kubernetes Cluster                              |
| +---------------------------------------------+ |
| | Ingress Controller (e.g., Nginx, Traefik)   | | <--- Checks Ingress resource rules
| |  - Reads Ingress Resource Rules             | |
| |  - Routes traffic based on Host/Path        | |
| +---------------------------------------------+ |
|      |        |        |                      |
|      v        v        v                      |
| +--------+ +--------+ +--------+             |
| | Service A| | Service B| | Service C|             | <--- Delivers traffic based on rules
| +--------+ +--------+ +--------+             |
+-------------------------------------------------+
```

**Ingress vs other service exposure methods comparison:**

| Feature | NodePort | LoadBalancer (Cloud) | Ingress |
| --- | --- | --- | --- |
| **Primary use** | Development/testing, simple exposure | Needs external load balancer per service | HTTP/S routing, single entry point |
| **External IP** | Uses node IP | Cloud-provided load balancer IP | Ingress controller's load balancer IP (usually 1) |
| **Port management** | Possible port conflicts per node | Load balancer management per service | Mainly uses ports 80/443 |
| **L7 routing** | Not possible | Not possible (L4 level) | Possible (Host, Path-based) |
| **SSL/TLS termination** | Not possible (handled at service level) | Possible (load balancer level) | Possible (Ingress controller level) |
| **Cost** | Low | Increases with number of services | Relatively efficient (1 shared load balancer) |
| **Required component** | None | Cloud environment | Ingress controller |

## Cautions and tips

⚠️ **Keep these in mind!**

1. **Ingress controller is essential!**: Even if you define an Ingress resource, without an Ingress controller installed and running in the cluster to interpret and execute it, it has no effect.
   - **Detailed explanation**: The Ingress controller is a separate component that must be deployed. Various open-source and commercial solutions exist, such as Nginx Ingress Controller, Traefik, and HAProxy Ingress. Cloud environments (EKS, GKE, AKS) sometimes provide managed controllers.
   - **Solution**: Choose an appropriate Ingress controller for your environment and deploy it to your cluster. Consult the official documentation for installation guides.
2. **Networking complexity**: Ingress configuration sometimes requires complex networking knowledge. This is especially true when using advanced features like SSL/TLS setup, redirects, and authentication.
   - **Detailed explanation**: Understanding the interactions between Ingress rules, controller configuration (annotations, etc.), and underlying network infrastructure (CNI plugins, cloud load balancer settings, etc.) makes troubleshooting easier.
   - **Solution**: Study official documentation and community resources thoroughly, and start with simple configurations before progressively applying more complex features.

Tip

- **Utilize Annotations**: Using annotations in Ingress resources allows fine-grained control over specific Ingress controller behaviors (e.g., SSL redirect, CORS settings, timeout settings). Different controllers support different annotations, so be sure to check the documentation for your controller!
- **Wildcard hosts**: Use wildcard hosts like `*.example.com` to define rules for multiple subdomains at once. (Requires a wildcard certificate, though)
- **Use IngressClass**: When you want to use multiple types of Ingress controllers in a single cluster, or explicitly specify which controller manages a particular Ingress resource, use the `IngressClass` resource.

## Closing remarks

We've explored Kubernetes' external traffic manager, Ingress. It goes beyond the limitations of NodePort and LoadBalancer approaches, providing a more flexible and efficient way to expose services externally. Especially when operating multiple services, needing URL-based routing, or managing SSL, Ingress can be a powerful solution.

Initially, the Ingress controller concept and resource definition might feel unfamiliar, but I hope you'll experience its convenience through hands-on use! Feel free to leave any questions or topics you'd like to know more about in the comments!

## References

- **Kubernetes official documentation - Ingress**: <https://kubernetes.io/docs/concepts/services-networking/ingress/>
- **Kubernetes official documentation - Ingress Controllers**: <https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/>
- **Nginx Ingress Controller documentation**: [check official site]
- **(Blog) What is Kubernetes Ingress?**: [search results for appropriate blog links]
- **(Video) Kubernetes Ingress Explained**: [search results for appropriate video links]

---

#Kubernetes #Ingress #Networking #Cloud #DevOps #Microservices #CloudNative
