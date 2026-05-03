---
title: "How do you specify the base packages for component scanning in a Spring configuration class?"
date: 2024-05-29T07:30:55+09:00
slug: "149-How-do-you-specify-the-base-packages-for-component-scanning-in-a-Spring-configuration-class"
original_url: "https://memoryhub.tistory.com/149"
tistory_id: 149
draft: false
categories: ["데브 프레임워크"]
tags: ["Spring"]
---

*To specify the base packages for component scanning in a Spring configuration class, you use the `@ComponentScan` annotation with the `basePackages` attribute to indicate which packages should be scanned for components.*

### The Big Picture

Specifying base packages for component scanning in a Spring configuration class is akin to giving precise instructions to a search party on where to look for important items in a large house. By doing this, you ensure that only the relevant sections are scanned, making the process efficient and organized.

### Core Concepts

1. **ComponentScan Annotation**: This annotation tells Spring which packages to scan for annotated components.
2. **Base Packages**: These are the directories where Spring looks for classes annotated with `@Component`, `@Service`, `@Repository`, or `@Controller`.

### Detailed Walkthrough

1. **Using @ComponentScan in a Configuration Class**: The `@ComponentScan` annotation is applied to a configuration class. This class is usually annotated with `@Configuration` to indicate that it provides Spring configuration.
2. **Specifying Base Packages**: You use the `basePackages` attribute of the `@ComponentScan` annotation to list the packages that should be scanned. You can specify one or more packages.

   **Single Package Example:**

   ```
   @Configuration
   @ComponentScan(basePackages = "com.example.app")
   public class AppConfig {
       // Configuration code
   }
   ```

   **Multiple Packages Example:**

   ```
   @Configuration
   @ComponentScan(basePackages = {"com.example.app", "com.example.services"})
   public class AppConfig {
       // Configuration code
   }
   ```
3. **Wildcard Support**: You can use wildcard patterns to specify package scanning.

   **Wildcard Example:**

   ```
   @Configuration
   @ComponentScan(basePackages = "com.example.*")
   public class AppConfig {
       // Configuration code
   }
   ```
4. **Default Package**: If no `basePackages` are specified, Spring scans the package of the class annotated with `@ComponentScan`.

   **Default Package Example:**

   ```
   @Configuration
   @ComponentScan
   public class AppConfig {
       // Configuration code
   }
   ```

### Understanding Through an Example

Consider you have an application with the following package structure:

- `com.example.app`
- `com.example.services`
- `com.example.controllers`

You want Spring to scan `com.example.app` and `com.example.services` for components. Here's how you do it:

**Configuration Class:**

```
@Configuration
@ComponentScan(basePackages = {"com.example.app", "com.example.services"})
public class AppConfig {
    // Configuration code
}
```

With this setup, when the application context is initialized, Spring will scan the `com.example.app` and `com.example.services` packages, detect any components (classes annotated with `@Component`, `@Service`, etc.), and register them as beans.

### Conclusion and Summary

*In a Spring configuration class, you specify the base packages for component scanning using the `@ComponentScan` annotation with the `basePackages` attribute, ensuring that Spring efficiently discovers and registers only the relevant components.*

- **@ComponentScan**: Annotation used to define the packages to scan.
- **basePackages**: Attribute used to specify one or more packages.
- **Default Behavior**: If no packages are specified, the package of the annotated class is scanned.

### Test Your Understanding

1. How would you specify multiple base packages for component scanning?
2. What is the default behavior if no `basePackages` are specified in `@ComponentScan`?
3. How can you use wildcards with the `basePackages` attribute?

### Reference

For more details on specifying base packages for component scanning, refer to the [official Spring documentation on `@ComponentScan`](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/context/annotation/ComponentScan.html).
