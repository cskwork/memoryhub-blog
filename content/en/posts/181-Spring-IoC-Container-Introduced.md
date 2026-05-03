---
title: "Spring IoC Container Introduced"
date: 2024-06-02T15:08:50+09:00
slug: "181-Spring-IoC-Container-Introduced"
original_url: "https://memoryhub.tistory.com/181"
tistory_id: 181
draft: false
---

*The Spring IoC (Inversion of Control) container is a powerful tool in the Spring Framework that handles the creation, configuration, and management of beans, thereby promoting loose coupling and flexibility in your applications.*

### The Big Picture

Think of the Spring IoC container as a factory with a highly intelligent management system. In this factory, various components (beans) are produced, assembled, and managed automatically according to predefined instructions (configuration metadata). This factory ensures that each component is properly constructed, dependencies are supplied, and lifecycle processes are managed efficiently. This automation allows developers to focus on the logic of their applications without worrying about the nitty-gritty details of object creation and dependency management.

### Core Concepts

- **Inversion of Control (IoC)**: This principle flips the control of object creation and dependency management from the application code to an external entity (the IoC container).
- **Dependency Injection (DI)**: A design pattern used by the IoC container to provide the required dependencies to a bean, ensuring that the bean does not need to create these dependencies itself.
- **Spring Bean**: An object whose lifecycle is managed by the IoC container. Beans are the core components of a Spring application.
