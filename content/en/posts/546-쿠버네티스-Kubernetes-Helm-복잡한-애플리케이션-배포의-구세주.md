---
title: "Kubernetes Helm - The Savior of Complex Application Deployment!"
date: 2025-04-12T10:35:57+09:00
slug: "546-쿠버네티스-Kubernetes-Helm-복잡한-애플리케이션-배포의-구세주"
original_url: "https://memoryhub.tistory.com/546"
tistory_id: 546
draft: false
categories: ["Dev Ops"]
tags: ["Kubernetes"]
---

Kubernetes is truly a powerful and amazing tool! But doesn't managing and deploying multiple resources get headache-inducing with so many YAML files? It's like trying to assemble numerous LEGO pieces without instructions. That's exactly where **Helm** comes in! Helm will make your Kubernetes journey much easier and more enjoyable. Ready to explore the world of Helm?

## What is Helm? The Package Manager for Kubernetes

Helm is the package manager for Kubernetes. Just as package managers like npm (for Node.js), pip (for Python), or apt (for Ubuntu) make installing and managing software packages simple and convenient, Helm makes managing complex Kubernetes applications straightforward.

Think of Helm as a "recipe manager for Kubernetes." A Helm Chart is like a recipe that includes all the ingredients (Kubernetes manifests/YAML files), instructions (metadata), and customization options (values) needed to run an application on Kubernetes.

### Why Do We Need Helm?

**Problem Before Helm:**
- Managing dozens of YAML files becomes chaotic
- Duplicating similar configurations across environments (dev, staging, prod)
- Sharing applications with others requires explaining complex YAML structures
- Updating applications across multiple environments is error-prone
- No standardized way to package and distribute Kubernetes applications

**Solution with Helm:**
- Bundle all manifests into a single "Chart"
- Reuse charts across different environments with simple parameter changes
- Version control for applications
- Easy sharing and installation via Helm repositories
- Simplified updates and rollbacks

## Core Helm Concepts

### 1. Chart: Application Recipe
A Helm Chart is a packaged Kubernetes application that includes:
- Metadata about the application (name, description, version)
- All necessary Kubernetes manifests (Deployments, Services, ConfigMaps, etc.)
- Default configuration values
- Dependencies on other charts

### 2. Repository: Chart Store
A Helm repository is a place (HTTP server) that stores and distributes Helm Charts. The official Helm repository is Artifact Hub, where thousands of public charts are available.

### 3. Release: Deployed Instance
A Release is an installed instance of a Chart in a Kubernetes cluster. You can install the same Chart multiple times with different configurations, creating multiple Releases.

### 4. Values: Customization Parameters
Values allow you to customize Chart behavior without modifying the Chart itself. Provide environment-specific values (database host, image version, replicas, etc.) when installing a Chart.

## Helm Architecture

```
Helm Client
    |
    ├─> Chart (Repository/Local)
    |
    ├─> Values
    |
    └─> Generate Kubernetes Manifests
             |
             └─> kubectl apply
                  |
                  └─> Kubernetes Cluster
```

## Basic Helm Commands

### Finding and Installing Charts
```bash
# Search for a chart in repositories
helm search repo mysql

# Add a repository
helm repo add bitnami https://charts.bitnami.com/bitnami

# Update repository cache
helm repo update

# Install a chart
helm install my-mysql bitnami/mysql

# Install with custom values
helm install my-mysql bitnami/mysql --values custom-values.yaml
```

### Managing Releases
```bash
# List installed releases
helm list

# Get release details
helm show values bitnami/mysql

# Upgrade a release
helm upgrade my-mysql bitnami/mysql --values custom-values.yaml

# Rollback to previous version
helm rollback my-mysql 1

# Uninstall a release
helm uninstall my-mysql
```

## Creating Your Own Helm Chart

### Chart Structure
```
my-app/
├── Chart.yaml          # Chart metadata
├── values.yaml         # Default values
├── templates/          # Kubernetes manifest templates
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
│   └── ingress.yaml
└── charts/             # Dependencies (subchart)
```

### Example Chart.yaml
```yaml
apiVersion: v2
name: my-app
description: A Helm chart for deploying my-app
type: application
version: 0.1.0
appVersion: "1.0"
```

### Example values.yaml
```yaml
replicaCount: 3

image:
  repository: my-registry/my-app
  tag: "1.0"
  pullPolicy: IfNotPresent

service:
  type: ClusterIP
  port: 8080

resources:
  limits:
    cpu: 500m
    memory: 512Mi
  requests:
    cpu: 250m
    memory: 256Mi
```

### Example Deployment Template
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "my-app.fullname" . }}
spec:
  replicas: {{ .Values.replicaCount }}
  template:
    metadata:
      labels:
        app: {{ .Chart.Name }}
    spec:
      containers:
      - name: {{ .Chart.Name }}
        image: "{{ .Values.image.repository }}:{{ .Values.image.tag }}"
        ports:
        - containerPort: 8080
        resources:
          {{- toYaml .Values.resources | nindent 12 }}
```

## Benefits of Using Helm

1. **Simplification**: One command to deploy complex applications
2. **Reusability**: Share charts across teams and projects
3. **Version Control**: Track application versions and configurations
4. **Environment Management**: Easy customization per environment
5. **Community**: Access thousands of pre-made charts
6. **Rollback**: Simple version rollback if issues occur
7. **Templating**: DRY principle for YAML configurations

## Advanced Helm Features

### Helm Hooks
Execute scripts at specific points in a release lifecycle (pre-install, post-upgrade, etc.)

### Subcharts
Include and manage dependent charts within your main chart

### Chart Testing
Test your charts to ensure they deploy correctly

### Security
Encrypt sensitive values, manage secrets securely

## Conclusion

Helm transforms Kubernetes application management from complex YAML juggling to simple, elegant package management. Whether you're deploying a single application or managing a entire infrastructure, Helm simplifies your workflow.

Start with public charts from Helm repositories, then progress to creating your own charts as your Kubernetes expertise grows. Helm is the bridge between Kubernetes power and operational simplicity.

Happy Helming!
