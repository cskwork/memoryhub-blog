---
title: "Spring Bean Lifecycle"
date: 2024-06-02T15:03:40+09:00
slug: "179-Spring-Bean-Lifecycle"
original_url: "https://memoryhub.tistory.com/179"
tistory_id: 179
draft: false
categories: ["데브 프레임워크"]
tags: ["Spring"]
---

*Spring's IoC container manages the lifecycle of beans by creating, configuring, and assembling them during application startup, and by managing their states and dependencies through the entire runtime.*

### The Big Picture

Think of the IoC container as a sophisticated manager in a large corporation. This manager is responsible for hiring employees (creating beans), assigning them tasks (configuring beans), and ensuring they have everything they need to perform their tasks effectively (managing dependencies). The IoC container does this for your application components (beans), handling their lifecycle from creation to destruction.

### Core Concepts

1. **Bean Definition**: A bean definition contains the information needed to create and configure a bean.
2. **Bean Scope**: The scope determines the lifecycle and visibility of a bean.
   - **Singleton**: A single instance per Spring IoC container.
   - **Prototype**: A new instance every time a bean is requested.
   - Other scopes like `request`, `session`, etc., for web applications.
3. **Bean Lifecycle Callbacks**: Methods that can be called at specific points in a bean's lifecycle.
   - **Initialization**: Methods called after a bean is created and its dependencies are set.
   - **Destruction**: Methods called before a bean is destroyed.

### Detailed Walkthrough

#### Bean Creation and Initialization

When the Spring IoC container starts, it performs the following steps for each bean:

1. **Instantiate**: The container creates an instance of the bean.
2. **Populate Properties**: The container injects the dependencies into the bean's properties.
3. **Set Bean Name**: If the bean implements `BeanNameAware`, the container passes the bean's name.
4. **Set Bean Factory**: If the bean implements `BeanFactoryAware`, the container passes a reference to itself.
5. **Pre-Initialization**: The container calls `BeanPostProcessor`'s `postProcessBeforeInitialization` methods.
6. **Initialize Bean**: The container calls custom initialization methods specified via `@PostConstruct`, `InitializingBean`'s `afterPropertiesSet()`, or a custom init-method.
7. **Post-Initialization**: The container calls `BeanPostProcessor`'s `postProcessAfterInitialization` methods.

#### Bean Destruction

When the Spring IoC container shuts down or a singleton bean is removed, it performs the following steps:

1. **Pre-Destruction**: The container calls custom destruction methods specified via `@PreDestroy`, `DisposableBean`'s `destroy()`, or a custom destroy-method.

### Example

Here's an example demonstrating these steps using annotations and Java-based configuration.

*Java Configuration:*

```
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {

    @Bean(initMethod = "customInit", destroyMethod = "customDestroy")
    public MyBean myBean() {
        return new MyBean();
    }
}
```

*MyBean Class:*

```
import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

public class MyBean {

    public MyBean() {
        System.out.println("Bean instantiated");
    }

    @PostConstruct
    public void init() {
        System.out.println("PostConstruct method called");
    }

    public void customInit() {
        System.out.println("Custom init-method called");
    }

    @PreDestroy
    public void destroy() {
        System.out.println("PreDestroy method called");
    }

    public void customDestroy() {
        System.out.println("Custom destroy-method called");
    }
}
```

*Main Class:*

```
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(AppConfig.class);
        MyBean myBean = context.getBean(MyBean.class);
        context.close(); // This triggers the destruction lifecycle
    }
}
```

### Understanding Through an Example

In this example:

1. The `MyBean` instance is created when `myBean()` method is called.
2. `@PostConstruct` method is called after the bean is fully initialized.
3. Custom `init-method` is called after `@PostConstruct`.
4. When the context is closed, `@PreDestroy` method is called.
5. Custom `destroy-method` is called after `@PreDestroy`.

### Conclusion and Summary

Spring's IoC container manages the lifecycle of beans by handling their creation, initialization, and destruction. It provides hooks for customization through lifecycle callbacks and bean scopes, allowing fine-grained control over how beans are managed. This results in a more flexible and maintainable application structure.

### Test Your Understanding

1. Describe the difference between Singleton and Prototype scopes in Spring.
2. What methods can be used to define custom initialization and destruction logic for a bean?
3. Create a bean with a custom initialization method and demonstrate its lifecycle in a Spring application.

### Reference

- Spring Framework Documentation on Bean Lifecycle: [Bean Lifecycle](https://docs.spring.io/spring-framework/docs/current/spring-framework-reference/core.html#beans-factory-lifecycle)

Would you like to explore any specific lifecycle aspect or have any questions on the examples provided?
