---
title: "Clean Architecture"
date: 2024-05-28T22:53:17+09:00
slug: "129-Clean-Architecture"
original_url: "https://memoryhub.tistory.com/129"
tistory_id: 129
draft: false
---

*Clean Architecture is a software design philosophy that aims to create systems that are easy to maintain, flexible, and scalable by organizing code into layers with clear separation of concerns.*

### The Big Picture

Imagine building a house. You wouldn't want the plumbing mixed with the electrical wiring, or the living room walls made of random materials without a clear structure. Clean Architecture is similar; it's about organizing your code in such a way that each part has a clear role and doesn't get mixed up with others.

### Core Concepts

1. **Separation of Concerns**: Each layer of your application should have a distinct responsibility.
2. **Dependency Rule**: High-level modules (business logic) should not depend on low-level modules (frameworks or databases); instead, both should depend on abstractions.
3. **Independence from Frameworks**: The core logic should be free from any framework dependencies.
4. **Testability**: The architecture should make it easy to test the business logic without the need for external systems.

### Detailed Walkthrough

Clean Architecture typically divides the system into several concentric layers:

1. **Entities**: These are the core business objects of the application. They are the most general and abstract.
2. **Use Cases**: This layer contains application-specific business rules. It orchestrates the flow of data to and from the entities.
3. **Interface Adapters**: This layer transforms data from the format most convenient for the use cases and entities to the format most convenient for external agencies like databases, the web, etc.
4. **Frameworks and Drivers**: This is the outermost layer, containing details like UI frameworks, database access, etc.

### Understanding Through an Example

Let's consider building a simple e-commerce system. Here's how Clean Architecture would structure it:

- **Entities**: You might have classes like `Product`, `Order`, and `Customer`. These classes don't know anything about the database or the user interface; they just represent the core business logic.
- **Use Cases**: You'd have use cases like `AddProductToCart`, `PlaceOrder`, and `ProcessPayment`. These use cases interact with the entities to perform specific business operations.
- **Interface Adapters**: This layer might include a `ProductRepository` interface that defines methods for retrieving and storing products. The actual implementation of this interface will be done in the outer layer.
- **Frameworks and Drivers**: Here you'd have the database connection, web server, UI framework, etc. For instance, the `ProductRepositoryImpl` class would implement the `ProductRepository` interface and contain the actual database logic.

### Conclusion and Summary

Clean Architecture helps to build systems that are robust, maintainable, and adaptable to changes. By keeping business logic at the center and abstracting away details like databases and UI frameworks, you can ensure that changes in technology or external systems don't ripple through your entire codebase.

### Test Your Understanding

1. Why is it important to keep the business logic independent of frameworks?
2. How does Clean Architecture help in making a system testable?
3. What role do interface adapters play in Clean Architecture?

### Reference

- [Clean Architecture: A Craftsman's Guide to Software Structure and Design by Robert C. Martin](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/)
