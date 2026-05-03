---
title: "Introduction to @Transactional"
date: 2025-02-23T23:12:06+09:00
slug: "453-Transactional-소개"
original_url: "https://memoryhub.tistory.com/453"
tistory_id: 453
draft: false
---

Today, let's explore the **@Transactional** annotation frequently used in the Spring framework to ensure **data integrity and consistency**! By applying transactions to methods where database operations (INSERT, UPDATE, DELETE, etc.) occur, you can handle data more safely. Let's take a look together.

---

## **1. What is @Transactional? ?**

**@Transactional** is an annotation provided by Spring to conveniently enable **transaction management**. When issues occur during database operations (e.g., exceptions are thrown), it rolls back the work to its original state, protecting application integrity.

- ? **Concept Summary**  
  Database operations proceed in transaction units, and must maintain characteristics like **ACID (Atomicity, Consistency, Isolation, Durability)**. @Transactional makes managing such transactions convenient in Spring.
- ? **Real-life Example**  
  Imagine a bank account transfer. Money must leave account A and enter account B. If an error occurs midway where A is debited but B isn't credited, there's a big problem, right? Through transactions, all operations are processed as one package, and errors can roll back the entire operation.
- ? **What Problem Does It Solve?**  
  It prevents **partial application of data causing corruption**. When work involving multiple steps fails midway, it can recover the already-processed data (rollback).

---

## **2. How Does It Work? ?**

### 1) Basic Concept

To use @Transactional in Spring, basically a **transaction manager (PlatformTransactionManager)** must be registered as a bean. In a Spring Boot environment, typically **DataSourceTransactionManager** (relational DB) or **JpaTransactionManager** (JPA/Hibernate) are auto-configured.

```
@Service
public class MyService {

    @Autowired
    private MyRepository myRepository;

    @Transactional
    public void doBusinessLogic() {
        // 1. Query data from DB
        // 2. Modify data
        // 3. Save modified data
        myRepository.save(...);
    }
}
```

When the `doBusinessLogic()` method with @Transactional declared executes, Spring starts/ends transactions before and after method execution.

- When the method ends normally, it performs **commit** to reflect the work in the DB.
- If an exception occurs inside the method and rollback setting is applied, DB operations are **rolled back** to recover the original state.

### 2) Actual Application Example

```
@Service
public class OrderService {

    @Autowired
    private OrderRepository orderRepository;

    @Autowired
    private PaymentService paymentService;

    @Transactional
    public void processOrder(OrderRequest request) {
        // 1. Save order information to DB
        Order order = new Order(request.getItemId(), request.getAmount());
        orderRepository.save(order);

        // 2. Process payment
        paymentService.pay(order.getId(), request.getAmount());

        // If an exception occurs inside paymentService.pay(), entire rollback
        // That is, the Order data saved by orderRepository.save() is also rolled back.
    }
}
```

#### ? How It Works

1. **Start Transaction**: When calling the `processOrder()` method, Spring automatically starts a transaction.
2. **Perform DB Operations**: Save order information and attempt payment.
3. **Commit on Normal Processing**: If all logic processes without issues, the transaction commits.
4. **Rollback on Exception**: If an exception is thrown in the payment logic, Spring rolls back the transaction.

---

## **3. Key Advantages ?**

1. **Convenience**  
   Without writing transaction management logic yourself, you can simply apply it by attaching an annotation.
2. **Explicit and Intuitive Structure**  
   Since transactions are declaratively applied at the method level, it's easy to see which logic is wrapped in transactions.
3. **Easy Recovery on Error**  
   When an exception occurs, Spring automatically rolls back, ensuring data integrity.

---

## **4. Cautions ⚠️**

1. **Proxy-Based Operation**  
   Since it operates based on Spring AOP (proxy), **method calls within the same class** may not have transactions applied. Example: `this.someInnerMethod()`. For transactions to apply, **the method must be called from external sources**.
2. **Checked Exception vs Unchecked Exception**  
   By default, unchecked exceptions (RuntimeException, Error, etc.) trigger rollback, while checked exceptions (Exception) don't. To rollback checked exceptions, specify like `@Transactional(rollbackFor = Exception.class)`.
3. **Read-Only Transactions**  
   Setting `@Transactional(readOnly = true)` offers benefits like JPA cache optimization, but if you actually modify data, exceptions may occur or some implementations may not work properly, so be careful.
4. **Caution with Large DB Operations**  
   The longer the transaction scope (large-scale processing), the longer locks persist or performance issues occur. If needed, use Batch processing or subdivide transaction scopes.
5. **Avoid Using @Transactional on Simple Queries**  
   Often, simple query methods (where no changes occur) don't need to be wrapped with @Transactional. Since transactions consume more DB resources, apply only where truly needed.

---

## **5. Actual Usage Example ?**

### (1) Using in Service Logic Composed of Multiple Methods

```
@Service
public class CartService {

    @Autowired
    private CartRepository cartRepository;

    @Autowired
    private ItemService itemService;

    @Transactional
    public void addToCart(Long userId, Long itemId) {
        // 1. Check item stock
        itemService.checkStock(itemId);

        // 2. Add item to cart
        Cart cart = cartRepository.findByUserId(userId);
        cart.addItem(itemId);
        cartRepository.save(cart);

        // If an exception occurs midway, rollback!
    }
}
```

### (2) When You Need to Apply Partial Rollback

If you want rollback to apply only to specific work within one service method, you need to separate structures or apply separate dedicated transaction configuration.

```
@Service
public class MixedOperationService {

    @Transactional
    public void processOperations() {
        // A: Work that must be rolled back
        doCriticalOperation();

        // B: Work unrelated to rollback
        doNonCriticalOperation();
    }

    @Transactional(rollbackFor = Exception.class)
    public void doCriticalOperation() {
        // Critical work
    }

    public void doNonCriticalOperation() {
        // Simple work (no separate transaction needed)
    }
}
```

---

## **6. Conclusion ?**

Transactions are an essential concept for maintaining data integrity and consistency. Through **@Transactional**, **developers can focus only on business logic**, while leaving transaction management to Spring, gaining big advantages. However, when applying transactions to important logic like **shopping carts and payments**, you must carefully consider **data lock time** and **rollback strategies**.

When using this technology well, you can easily prevent problems like **data loss or integrity corruption** and expand to better code structures. Apply @Transactional appropriately only where needed to build safe and efficient applications!

---

### Reference Materials and Sources

- Spring Official Documentation: [Transaction Management](https://docs.spring.io/spring-framework/docs/current/reference/html/data-access.html#transaction)
- Spring Boot Official Documentation: [Spring Boot Transaction Support](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#boot-features-transaction)
