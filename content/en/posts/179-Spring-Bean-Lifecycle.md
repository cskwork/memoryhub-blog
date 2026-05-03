---
title: "Spring Bean Lifecycle"
date: 2024-06-02T15:03:40+09:00
slug: "179-Spring-Bean-Lifecycle"
original_url: "https://memoryhub.tistory.com/179"
tistory_id: 179
draft: false
---

*Spring's IoC container manages the lifecycle of beans by creating, configuring, and assembling them during application startup, and by managing their states and dependencies through the entire runtime.*

### The Big Picture

Think of the IoC container as a sophisticated manager in a large corporation. This manager is responsible for hiring employees (creating beans), assigning them tasks (configuring beans), and ensuring they have everything they need to perform their tasks effectively (managing dependencies). The IoC container does this for your application components (beans), handling their lifecycle from creation to destruction.

### Core Concepts

1. **Bean Definition**: A bean definition contains the information needed to create and configure a bean.
2. **Bean Scope**: The scope determines the lifecycle and visibility of a bean.
   - **Singleton**: A single instance per Spring IoC container.
