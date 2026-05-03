---
title: "Log4j2 Configuration Mastery - Stop Using System.out.println() Now!"
date: 2025-06-15T11:55:01+09:00
slug: "688-Log4j2-설정-완벽-정복-이제-System-out-println-그만-쓰세요"
original_url: "https://memoryhub.tistory.com/688"
tistory_id: 688
draft: false
categories: ["Dev Framework"]
tags: ["Logback"]
---

```
╔═══════════════════════════════════════════════╗
║     📜 LOG4J2 CONFIGURATION                   ║
╠═══════════════════════════════════════════════╣
║   ┌─────────┐    ┌─────────┐   ┌─────────┐   ║
║   │ CONSOLE │────│ FILE    │───│ ROLLING │   ║
║   └────┬────┘    └────┬────┘   └────┬────┘   ║
║        │              │              │        ║
║        └──────────────┴──────────────┘        ║
║                       │                       ║
║                  ┌────▼────┐                  ║
║                  │ LOGGER  │                  ║
║                  └─────────┘                  ║
╚═══════════════════════════════════════════════╝
```

Hello! Recently, while debugging on a production server, I broke into a cold sweat seeing legacy code peppered with System.out.println(). 😅

Have you ever experienced a log file exceeding 100GB and crashing the server? Or missed an important error log and couldn't find the cause of the outage?

Today, I'm sharing **everything about Log4j2 configuration** that I learned through 3 years of trial and error. After reading this article, you'll never have to stay up late debugging logs again!

⚡ **TL;DR**

- Building an efficient logging system with Log4j2
- File size management and performance optimization all in one!

## Table of Contents

1. [Background - Why Log4j2?](#1-background)
2. [Core Concepts](#2-core-concepts)
3. [Practical Guide - Step by Step](#3-practical-guide)
4. [Best Practices](#4-best-practices)
5. [Conclusion & References](#5-conclusion--references)

---

## 1. Background

### 🔍 Why Choose Log4j2?

Spring Boot projects come with Logback by default. So why should you switch to Log4j2?

| Feature | Logback | Log4j2 |
| --- | --- | --- |
| **Async Logging Performance** | Normal | Very Fast (3-10x) |
| **Memory Usage** | High | Low (Lower GC pressure) |
| **Lambda Expressions** | Not supported | Supported ✅ |
| **Configuration Format** | XML only | XML, JSON, YAML, Properties |

### 📌 Key Terminology

✅ **Logger**: Entity that creates logs  
✅ **Appender**: Determines where logs are output (console, file, etc.)  
✅ **Layout**: Defines log message format  
✅ **Level**: Importance of logs (TRACE < DEBUG < INFO < WARN < ERROR < FATAL)

## 2. Core Concepts

> **Log4j2 is a high-performance Java logging framework that supports asynchronous logging and lambda expressions, achieving both performance and convenience.**

### 🏗️ Understanding Architecture

```
// Create logger - one per class
private static final Logger logger = LogManager.getLogger(MyClass.class);

// Optimize performance with lambda expressions
logger.debug("Processing request for user {} took {} ms", 
    () -> getUserName(),  // Only executes when debug level is enabled
    () -> calculateTime()
);
```

## 3. Practical Guide

### ① Set up Log4j2 in Spring Boot Project

**Step 1: Add Dependencies**

```
// build.gradle
configurations {
    all {
        // Exclude Logback
        exclude group: 'org.springframework.boot', module: 'spring-boot-starter-logging'
    }
}

dependencies {
    // Add Log4j2
    implementation 'org.springframework.boot:spring-boot-starter-log4j2'

    // Disruptor for async logging (optional but highly recommended!)
    implementation 'com.lmax:disruptor:3.4.4'
}
```

### ② Create log4j2.xml

**Step 2: Create src/main/resources/log4j2.xml**

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN" monitorInterval="30">
    <!-- Properties: Define reusable variables -->
    <Properties>
        <Property name="LOG_PATTERN">
            %d{yyyy-MM-dd HH:mm:ss.SSS} %highlight{%-5level} [%t] %style{%C{1.}}{cyan} : %msg%n%throwable
        </Property>
        <Property name="LOG_DIR">./logs</Property>
    </Properties>

    <Appenders>
        <!-- Console output configuration -->
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="${LOG_PATTERN}" disableAnsi="false"/>
        </Console>

        <!-- File output configuration (daily rolling) -->
        <RollingFile name="RollingFile" 
                     fileName="${LOG_DIR}/app.log"
                     filePattern="${LOG_DIR}/app-%d{yyyy-MM-dd}-%i.log.gz">
            <PatternLayout pattern="${LOG_PATTERN}"/>
            <Policies>
                <!-- Roll at midnight daily -->
                <TimeBasedTriggeringPolicy />
                <!-- Roll if file size exceeds 100MB -->
                <SizeBasedTriggeringPolicy size="100MB" />
            </Policies>
            <!-- Keep maximum 30 files, total 3GB limit -->
            <DefaultRolloverStrategy max="30">
                <Delete basePath="${LOG_DIR}" maxDepth="1">
                    <IfFileName glob="app-*.log.gz" />
                    <IfLastModified age="30d" />
                </Delete>
            </DefaultRolloverStrategy>
        </RollingFile>

        <!-- Error-only file -->
        <RollingFile name="ErrorFile"
                     fileName="${LOG_DIR}/error.log"
                     filePattern="${LOG_DIR}/error-%d{yyyy-MM-dd}.log.gz">
            <PatternLayout pattern="${LOG_PATTERN}"/>
            <ThresholdFilter level="ERROR" onMatch="ACCEPT" onMismatch="DENY"/>
            <Policies>
                <TimeBasedTriggeringPolicy />
            </Policies>
        </RollingFile>

        <!-- Async logging configuration (performance improvement) -->
        <Async name="AsyncFile">
            <AppenderRef ref="RollingFile"/>
        </Async>
    </Appenders>

    <Loggers>
        <!-- Application logger -->
        <Logger name="com.myapp" level="DEBUG" additivity="false">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="AsyncFile"/>
            <AppenderRef ref="ErrorFile"/>
        </Logger>

        <!-- Adjust log levels for external libraries -->
        <Logger name="org.springframework" level="INFO"/>
        <Logger name="org.hibernate" level="WARN"/>

        <!-- SQL logging (recommended for development only) -->
        <Logger name="org.hibernate.SQL" level="DEBUG"/>
        <Logger name="org.hibernate.type.descriptor.sql.BasicBinder" level="TRACE"/>

        <!-- Root logger -->
        <Root level="INFO">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="AsyncFile"/>
        </Root>
    </Loggers>
</Configuration>
```

### ③ Use in Actual Code

**Step 3: Logger Usage Example**

```
package com.myapp.service;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    // Create logger per class
    private static final Logger logger = LogManager.getLogger(UserService.class);

    public User createUser(UserDto userDto) {
        logger.info("Starting user creation: {}", userDto.getEmail());

        try {
            // Debug log - using lambda expressions
            logger.debug("Validation started - email: {}, name: {}", 
                () -> userDto.getEmail(), 
                () -> userDto.getName()
            );

            User user = User.builder()
                .email(userDto.getEmail())
                .name(userDto.getName())
                .build();

            // Business logic...

            logger.info("User creation completed - ID: {}", user.getId());
            return user;

        } catch (Exception e) {
            // Error logging - includes stack trace
            logger.error("User creation failed - email: {}", userDto.getEmail(), e);
            throw new ServiceException("User creation failed", e);
        }
    }

    // Performance measurement logging example
    public List<User> findAllUsers() {
        long startTime = System.currentTimeMillis();

        try {
            List<User> users = userRepository.findAll();
            return users;
        } finally {
            long elapsed = System.currentTimeMillis() - startTime;
            // Warn if execution takes more than 1 second
            if (elapsed > 1000) {
                logger.warn("User retrieval performance degradation - execution time: {}ms", elapsed);
            } else {
                logger.debug("User retrieval completed - execution time: {}ms", elapsed);
            }
        }
    }
}
```

## 4. Best Practices

| Pattern | Advantage | Caution |
| --- | --- | --- |
| **MDC (Mapped Diagnostic Context)** | Request-specific trace IDs for easy debugging in distributed environments | Beware of context loss during thread switching |
| **Async Logging** | 3-10x performance improvement | Possible log loss during application shutdown |
| **Conditional Logging** | Prevent unnecessary string operations | Use lambda expressions recommended |
| **Structured Logging** | Easy use with log analysis tools | Consider JSON format |

### 🚀 Recommended Production Settings

```
<!-- Production-specific settings -->
<Configuration status="ERROR" monitorInterval="300">
    <Properties>
        <!-- Environment-specific log path -->
        <Property name="LOG_DIR">${env:LOG_PATH:-/var/log/myapp}</Property>
    </Properties>

    <!-- Async configuration for performance -->
    <Appenders>
        <Async name="AsyncAll" bufferSize="512" blocking="false">
            <AppenderRef ref="RollingFile"/>
        </Async>
    </Appenders>
</Configuration>
```

### 🔗 MDC Usage Example

```
@Component
public class RequestLoggingFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, 
                                  HttpServletResponse response, 
                                  FilterChain filterChain) throws ServletException, IOException {
        // Generate unique ID per request
        String requestId = UUID.randomUUID().toString();

        try {
            // Add to MDC - automatically included in all logs
            MDC.put("requestId", requestId);
            MDC.put("userId", getUserId(request));

            filterChain.doFilter(request, response);
        } finally {
            // Must clean up!
            MDC.clear();
        }
    }
}
```

## 5. Conclusion

Today, we've explored Log4j2 configuration from A to Z.

**✨ Key Takeaways:**

- Log4j2 is superior to Logback in both performance and features
- Optimize performance with async logging and lambda expressions
- MDC enables effective debugging even in distributed environments

**💡 Practical Tip:** Don't try to create perfect configuration from the start. Begin with basic settings and improve incrementally as needed.

If this article was helpful, please give it a ❤️ heart and leave a comment! Feel free to ask if you have any questions. 🙏

---

### 📚 References

- [Log4j2 Official Documentation](https://logging.apache.org/log4j/2.x/)
- [Sample Project (GitHub)](https://github.com/apache/logging-log4j2/tree/master/log4j-samples)
- Additional Reading:
  - [Log4j2 Performance Benchmark](https://logging.apache.org/log4j/2.x/performance.html)
  - [Spring Boot Logging Guide](https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.logging)
  - [Distributed Tracing with MDC](https://www.baeldung.com/mdc-in-log4j-2-logback)
