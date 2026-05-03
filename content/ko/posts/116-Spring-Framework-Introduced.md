---
title: "Spring Framework Introduced"
date: 2024-05-28T12:38:41+09:00
slug: "116-Spring-Framework-Introduced"
original_url: "https://memoryhub.tistory.com/116"
tistory_id: 116
draft: false
categories: ["데브 프레임워크"]
tags: ["Spring"]
---

*Spring is a powerful framework for building Java applications, focusing on simplifying the development process through dependency injection and aspect-oriented programming.*

### The Big Picture

Imagine you're trying to build a large, complex machine. Without a framework, you'd have to create every piece from scratch and figure out how to make them all fit together. Spring is like a highly organized toolkit that provides pre-built pieces and clear instructions on how to assemble your machine, making the whole process much more manageable.

### Core Concepts

1. **Dependency Injection (DI)**: This is like having a master assembler who knows exactly which parts to use and how to fit them together, so you don't have to worry about the details.
2. **Aspect-Oriented Programming (AOP)**: Think of this as a way to handle repetitive tasks (like logging or security) separately, so you can focus on the core functionality of your application without getting bogged down by these concerns.
3. **Spring Modules**: Spring is divided into several modules, each providing different functionalities:
   - **Spring Core**: The foundation of the framework, providing DI.
   - **Spring MVC**: For building web applications.
   - **Spring Data**: Simplifies data access.
   - **Spring Security**: Manages authentication and authorization.
   - **Spring Boot**: Eases the setup of new Spring applications with default configurations.

### Detailed Walkthrough

Let's break down the two main concepts in detail:

#### Dependency Injection

In traditional programming, if one object needs another, it creates the dependency itself:

```
public class Car {
    private Engine engine;

    public Car() {
        this.engine = new Engine();
    }
}
```

In Spring, the framework handles the creation and injection of dependencies:

```
public class Car {
    private Engine engine;

    @Autowired
    public Car(Engine engine) {
        this.engine = engine;
    }
}
```

Spring's container manages the lifecycle and dependencies of your objects, making your code cleaner and easier to maintain.

#### Aspect-Oriented Programming

AOP allows you to separate cross-cutting concerns (like logging) from your main business logic. Without AOP, you might see:

```
public class OrderService {
    public void placeOrder() {
        // logging
        System.out.println("Placing order");
        // actual logic
        // logging
        System.out.println("Order placed");
    }
}
```

With AOP, you define these concerns separately:

```
@Aspect
public class LoggingAspect {
    @Before("execution(* OrderService.placeOrder(..))")
    public void logBefore() {
        System.out.println("Placing order");
    }

    @After("execution(* OrderService.placeOrder(..))")
    public void logAfter() {
        System.out.println("Order placed");
    }
}
```

This keeps your business logic clean and focused.

### Understanding Through an Example

Let's consider a simple Spring Boot application. Spring Boot simplifies the setup process with an embedded server and sensible defaults.

1. **Create a Spring Boot Application**:

   ```
   @SpringBootApplication
   public class Application {
       public static void main(String[] args) {
           SpringApplication.run(Application.class, args);
       }
   }
   ```
2. **Define a REST Controller**:

   ```
   @RestController
   public class HelloController {
       @GetMapping("/hello")
       public String sayHello() {
           return "Hello, World!";
       }
   }
   ```

   This sets up a web server that responds with "Hello, World!" when you visit `http://localhost:8080/hello`.

### Conclusion and Summary

Spring simplifies Java development through DI and AOP, providing a modular framework to handle various aspects of application development. Whether you need to manage dependencies, separate cross-cutting concerns, or set up a web application, Spring offers tools to make the process smoother and more efficient.

### Test Your Understanding

1. What is Dependency Injection and how does it help in managing dependencies in a Spring application?
2. Explain Aspect-Oriented Programming and its benefits with an example.
3. What is Spring Boot and how does it simplify the development of Spring applications?

### Reference

For more detailed information, you can refer to the official [Spring Framework documentation](https://spring.io/projects/spring-framework).
