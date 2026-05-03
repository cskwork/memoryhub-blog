---
title: "Component Scan Introduced"
date: 2024-05-29T07:29:22+09:00
slug: "148-Component-Scan-Introduced"
original_url: "https://memoryhub.tistory.com/148"
tistory_id: 148
draft: false
---

*Component scanning in Spring is like a search party looking for specific items in a large house, ensuring that every important item is identified, registered, and ready for use when needed.*

### The Big Picture

Imagine you have a large warehouse filled with various items. Some of these items are essential for your business operations, while others are not. To streamline your workflow, you need a systematic way to find and register only the essential items so that they can be used efficiently. In Spring, this process is known as **component scanning**. It automatically discovers and registers beans (components) within the application context, ensuring that the necessary components are available and wired together without manual configuration.

### Core Concepts

1. **Beans and Components**: In Spring, a bean is an object managed by the Spring IoC (Inversion of Control) container. Components are classes annotated with `@Component`, `@Service`, `@Repository`, or `@Controller`.
2. **Component Scan**: This is a process where Spring automatically detects and registers beans within the application context.
3. **Configuration and Context**: Spring's configuration classes or XML files define the base packages to be scanned for components.

### Detailed Walkthrough

1. **Defining Base Packages**: You specify the base packages for component scanning using the `@ComponentScan` annotation in a configuration class or using XML configuration.

   **Annotation-based Configuration:**

   ```
   @Configuration
   @ComponentScan(basePackages = "com.example.app")
   public class AppConfig {
       // Configuration code
   }
   ```

   **XML-based Configuration:**

   ```
   <context:component-scan base-package="com.example.app" />
   ```
2. **Scanning Process**: During the startup of the Spring application context, the component scan mechanism searches the specified base packages for classes annotated with `@Component`, `@Service`, `@Repository`, or `@Controller`.
3. **Registration of Beans**: When these annotated classes are found, Spring automatically registers them as beans in the application context. These beans can then be autowired into other beans using `@Autowired` or constructor injection.

### Understanding Through an Example

Imagine you are setting up a smart home system:

1. **Devices (Components)**: You have various devices like lights, thermostats, and cameras, each with a specific function.
2. **Control Center (Application Context)**: This is where you manage all your devices centrally.
3. **Device Detection (Component Scan)**: When you set up your control center, it automatically detects and registers all your smart devices.

Here is how it looks in a Spring application:

**Device Classes (Components):**

```
@Component
public class Light {
    // Light-specific functionality
}

@Service
public class Thermostat {
    // Thermostat-specific functionality
}

@Controller
public class CameraController {
    // Camera control functionality
}
```

**Control Center Configuration:**

```
@Configuration
@ComponentScan(basePackages = "com.smart.home")
public class SmartHomeConfig {
    // Configuration code
}
```

When the application starts, Spring scans the `com.smart.home` package, detects the `Light`, `Thermostat`, and `CameraController` classes, and registers them as beans in the application context. Now, these components are ready to be used and wired together as needed.

### Conclusion and Summary

*Component scanning in Spring is like setting up a smart home system where the control center automatically detects and registers all smart devices, making them ready for seamless integration and management.*

- **Component Scan** automatically discovers and registers beans within specified packages.
- **Annotations** like `@Component`, `@Service`, `@Repository`, and `@Controller` mark classes for detection.
- **Configuration** can be done via annotations (`@ComponentScan`) or XML.

### Test Your Understanding

1. What annotations can be used to mark a class as a component for Spring to detect during a component scan?
2. How do you specify the base packages for component scanning in a Spring configuration class?
3. What happens if a class is not annotated with `@Component`, `@Service`, `@Repository`, or `@Controller` but exists in the base package specified for component scanning?

### Reference

For further reading on Spring component scanning, you can refer to the [official Spring documentation on component scanning](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#beans-scanning).
