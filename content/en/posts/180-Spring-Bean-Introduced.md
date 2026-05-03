---
title: "Spring Bean Introduced"
date: 2024-06-02T15:06:07+09:00
slug: "180-Spring-Bean-Introduced"
original_url: "https://memoryhub.tistory.com/180"
tistory_id: 180
draft: false
categories: ["Dev Framework"]
tags: ["Spring"]
---

*Spring Beans are the backbone of a Spring application, representing objects that are created and managed by the Spring IoC container, ensuring efficient dependency management and configuration.*

### The Big Picture

Imagine you have a smart home system where different devices (like lights, thermostats, and security cameras) are all controlled by a central hub. The central hub knows how to turn on the lights, adjust the thermostat, and monitor the security cameras based on your preferences. In the Spring Framework, this central hub is like the Spring IoC (Inversion of Control) container, and the devices are like Spring Beans. The IoC container controls the lifecycle and interactions of these beans.

### Core Concepts

- **Spring IoC Container**: The central hub that manages the creation, configuration, and lifecycle of beans.
- **Spring Bean**: A Java object that is instantiated, configured, and managed by the Spring IoC container. It is the fundamental building block of a Spring application.
- **Bean Configuration**: Instructions on how to create and configure beans, provided through XML files, Java annotations, or Java configuration classes.
