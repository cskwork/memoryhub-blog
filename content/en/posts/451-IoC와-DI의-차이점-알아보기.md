---
title: "Understanding the Differences Between IoC and DI"
date: 2025-02-23T22:58:49+09:00
slug: "451-IoC와-DI의-차이점-알아보기"
original_url: "https://memoryhub.tistory.com/451"
tistory_id: 451
draft: false
---

Today, let's explore **IoC (Inversion of Control)** and **DI (Dependency Injection)**, two core concepts of the Spring framework. These are very important topics you must understand to truly comprehend Spring.

---

## **1. What are IoC and DI? ?**

### 1) What is IoC (Inversion of Control)?

- **IoC** means "inversion of control," which refers to the concept where **control of object creation is handled by an external entity (framework or container) rather than the developer**.
- Traditionally, the side using objects would directly create instances and manage dependencies. However, with IoC applied, **the Spring container assumes control of object creation and dependency management**.
- For example, think of a situation where the **Spring container** automatically creates objects at the "right time" and injects them, while also setting up dependencies between objects.

### 2) What is DI (Dependency Injection)?

- **DI** means "dependency injection," which is a **design pattern that concretely implements the IoC concept**.
- Literally, it's a way to **inject the dependent objects that an object needs from external sources**. In Spring, this can be easily done through annotations like `@Autowired`, `@Inject`, `@Resource`, or XML configuration.
- If IoC is a broad concept of "inversion of control," DI is a specific implementation method saying **'inject required objects from external sources'**.

> **Summary**:
>
> - **IoC**: Handing over control to the framework (Spring) - the big picture
> - **DI**: Spring injecting dependencies into objects - the specific method

---

## **2. How Does It Work? ?**

### 1) Basic Concept

To understand IoC and DI, think of it this way: **"Instead of one object directly creating another object, Spring creates that object for you"**.

When a Spring application starts, the Spring container reads the configuration file (e.g., `@Configuration` class, `applicationContext.xml`, etc.) and creates **beans**. If beans have dependencies on each other, they are appropriately connected (injected). By automatically handling this process, developers hardly need to worry about object creation.

### 2) Actual Application Example

## ? Comparison of Code Before and After Applying Dependency Injection (DI)

One of the most core concepts in Spring is **DI (Dependency Injection)**. This time, let's compare **"code with dependency injection applied"** and **"code without it"** with a simple example.

---

## 1. Code Without Dependency Injection (Creating Instances Directly)

```
public class OrderService {
    // Directly create PaymentService instance
    private PaymentService paymentService = new PaymentService();

    public void placeOrder(String productId) {
        paymentService.pay(productId);
    }
}

public class PaymentService {
    public void pay(String productId) {
        System.out.println("Payment completed: " + productId);
    }
}
```

### Characteristics

1. `OrderService` internally creates the `PaymentService` object directly with `new`.
2. If `PaymentService` changes (replaced with a different implementation, etc.), the `OrderService` code must also be modified.
3. **Coupling is relatively high**, and to **test** you must create an actual `PaymentService`.

---

## 2. Code with Dependency Injection (DI) Applied

### 2-1) **Pure Java Method** (Without Spring Framework)

```
public class OrderService {
    private final PaymentService paymentService;

    // Receive PaymentService through constructor injection
    public OrderService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    public void placeOrder(String productId) {
        paymentService.pay(productId);
    }
}

public class PaymentService {
    public void pay(String productId) {
        System.out.println("Payment completed: " + productId);
    }
}

// Calling part like main
public class Main {
    public static void main(String[] args) {
        PaymentService paymentService = new PaymentService(); // Create required object
        OrderService orderService = new OrderService(paymentService); // Inject
        orderService.placeOrder("Product-ID-123");
    }
}
```

#### Characteristics

1. `OrderService` doesn't know how to create `PaymentService`. It receives the **required dependent objects** from **outside**.
2. When you need to replace `PaymentService` with a **new class** (e.g., `TestPaymentService`), it's possible without modifying `OrderService` (only modify the injection part).
3. **Coupling is low**, **flexible**, and **testing** is convenient with Mock objects easily injected.

---

### 2-2) **Spring-based DI Example**

```
@Service
public class OrderService {
    private final PaymentService paymentService;

    // Constructor injection
    @Autowired
    public OrderService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    public void placeOrder(String productId) {
        paymentService.pay(productId);
    }
}

@Service
public class PaymentService {
    public void pay(String productId) {
        System.out.println("Payment completed: " + productId);
    }
}

// Spring Boot main example
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

- When Spring Boot runs, it scans classes marked with `@Service` and registers them as **beans**.
- Recognizing that `OrderService`'s constructor parameter needs a `PaymentService` type, it automatically creates the `PaymentService` bean and **injects** it.
- Developers don't need to directly create "`OrderService` with which `PaymentService`" but simply leave it to the **Spring container**.

---

### 3. Summary of Differences Between the Two Codes

| Aspect | Direct Instance Creation | Dependency Injection (DI) |
| --- | --- | --- |
| **Object Creation Subject** | Class creates directly with `new` | Created & injected by Spring container (or external) |
| **Coupling** | High: object creation logic fixed internally | Low: external injection, flexible replacement |
| **Maintainability** | Must modify classes for changes | Only modify injection part, more flexible |
| **Test Convenience** | Difficult to inject Mock objects | Mock objects easily replaceable |
| **Extensibility** | Many code changes to switch implementations | Just replace dependent objects, excellent extensibility |

---

- **Before DI**: "`OrderService` directly creates and uses `PaymentService` with `new`."
- **After DI**: "`OrderService` receives `PaymentService` 'injected' from outside and uses it."

As a result, when **DI** is applied, code **flexibility** increases and **testing** and **maintenance** become much easier.  
When using the Spring framework, the **Spring container (IoC)** manages object creation and dependency injection for you, reducing "what developers need to handle directly".

**Key Points**:

- Code "without dependency injection" directly creates needed objects → **high coupling**
- Code "with dependency injection applied" receives needed objects from **external source** → **low coupling** and high maintainability

---

## **3. Key Advantages ?**

1. **Reduced Coupling Between Objects**

   - When a new object is needed, the Spring container automatically connects it, so you don't need to directly create implementations in code. Through this, you can secure a **flexible structure** and **high extensibility**.
2. **Test Convenience**

   - You can easily replace with Mock objects or different implementations for testing, making **unit tests** and **integration tests** convenient.
3. **Improved Maintainability**

   - Object creation logic is separated from code and managed through configuration files (or annotations), so **changes have less impact on core business logic**.

---

## **4. Cautions ⚠️**

1. **Complex Configuration Management**

   - Excessively many bean configurations or complex dependency relationships can make initial setup complicated. Avoid situations where complexity makes configuration files or annotations hard to understand.
2. **Circular Dependency**

   - When situations like object A needing B and object B needing A occur, where **they mutually need to inject each other**, dependency injection fails. Be careful during structure design.
3. **Excessive Abstraction**

   - DI is different from mindlessly adding abstraction layers. You must balance **'flexibility' and 'simplicity'**.

---

## **5. Actual Usage Example ?**

### Example: Using `@Configuration` and `@Bean`

```
@Configuration
public class AppConfig {

    @Bean
    public PaymentService paymentService() {
        return new PaymentService();
    }

    @Bean
    public OrderService orderService() {
        return new OrderService(paymentService());
    }
}
```

```
public static void main(String[] args) {
    ApplicationContext context = 
        new AnnotationConfigApplicationContext(AppConfig.class);

    OrderService orderService = context.getBean(OrderService.class);
    orderService.placeOrder("Product-ID-123");
}
```

- In the `AppConfig` class, **directly create dependent objects** through `@Bean` methods (leaving this part to the container).
- `AnnotationConfigApplicationContext` looks at this `AppConfig`, creates `beans`, and establishes their relationships.
- This way, **object creation (Bean registration) and dependency injection** are separated, keeping business logic and configuration logic clean.

---

## **6. Conclusion ?**

In Spring, **IoC** and **DI** can be easily understood as "the structure where the side using objects doesn't directly create them, but the framework creates them automatically". Among them, DI (Dependency Injection) is a method that **concretely practices** the IoC concept through dependency injection.

When these concepts are properly utilized, you can **reduce code coupling**, **make testing and maintenance much easier**. As Spring applications become increasingly complex, you'll acutely feel the necessity of IoC/DI.

**Summary**:

- **IoC** is handing over **object creation control** from developers to the **Spring container** in the big picture
- **DI** is a representative way to implement this by **injecting dependencies between objects from external sources**

**Therefore**, understanding IoC and DI well allows you to maximize Spring's advantages and build more robust and maintainable applications!

---

### Reference Materials and Sources

- [Spring Official Documentation](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#beans-introduction)
- [Toby's Spring](https://book.naver.com/bookdb/book_detail.nhn?bid=7006516) (In-depth Spring Framework Analysis Book)
