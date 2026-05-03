---
title: "Code Smell: Change Preventers - Factors That Hinder Code Modification 🚫"
date: 2025-03-22T22:30:31+09:00
slug: "509-코드-스멜-Change-Preventers-코드-변경을-방해하는-요소들"
original_url: "https://memoryhub.tistory.com/509"
tistory_id: 509
draft: false
categories: ["Dev Concepts"]
tags: ["Clean Code"]
---

Have you ever tried to fix code, thinking you only needed to change one place, but ended up having to modify multiple locations? Or have you experienced having to understand an entire class just to make a simple change because it was doing too much?

These problems are related to a phenomenon known as 'Change Preventers' among code smells. It's like when things aren't properly organized in a house, making even simple repairs difficult!

- Think of a restaurant menu. If you had to reprint the entire menu every time you changed a price, how inconvenient would that be?
- Similarly, poorly designed code incurs huge costs even for small changes.

## Why Is This Needed?

The problems that Change Preventers solve include:

1. **Decreased maintainability**: When code changes are difficult, maintenance costs increase and development speed slows down.
2. **Bug risk**: When multiple locations need simultaneous modification, missing even one location causes bugs.
3. **Developer morale**: Even simple feature additions or bug fixes become complex tasks, demoralizing developers.

## Basic Principles

Let's explore the three types of Change Preventers and their solutions.

### 1. Divergent Change 📊

**Definition**: A single class needs to be changed frequently for multiple unrelated reasons.

**Analogy**: It's like trying to do all cooking tasks with a single kitchen tool. Using one knife for vegetable chopping, meat preparation, fish cleaning, bread slicing, etc. is inefficient. Each task needs its own appropriate tool.

**Problem Code**:

```
public class User {
    private String name;
    private String email;

    // User info related methods
    public void changeName(String newName) { this.name = newName; }

    // Database related methods
    public void saveToDatabase() { /* DB save logic */ }

    // Report generation related methods
    public String generateUserReport() { /* Report generation logic */ }
}
```

**Solution**: Separate each responsibility into its own class through class extraction.

**Improved Code**:

```
public class User {
    private String name;
    private String email;

    public void changeName(String newName) { this.name = newName; }
}

public class UserRepository {
    public void save(User user) { /* DB save logic */ }
}

public class UserReportGenerator {
    public String generateReport(User user) { /* Report generation logic */ }
}
```

### 2. Shotgun Surgery 🔫

**Definition**: A single change requires modifying multiple classes simultaneously.

**Analogy**: It's like having to flip through an entire recipe book to change one recipe. If you want to use 'margarine' instead of 'butter', you have to find and modify every recipe.

**Problem Code**:

```
public class Customer {
    public void sendEmail(String message) {
        // Email sending logic (with logging)
        System.out.println("Sending email: " + message);
        System.out.println("Email sent at: " + new Date());
    }
}

public class Order {
    public void notifyShipped() {
        // Similar email sending logic (with logging)
        System.out.println("Sending shipping notification");
        System.out.println("Email sent at: " + new Date());
    }
}
```

**Solution**: Unify common functionality in one place through method movement and class extraction.

**Improved Code**:

```
public class EmailService {
    public void sendEmail(String email, String message) {
        // Centralized email sending logic (with logging)
        System.out.println("Sending email to " + email + ": " + message);
        System.out.println("Email sent at: " + new Date());
    }
}

public class Customer {
    private EmailService emailService;

    public void sendEmail(String message) {
        emailService.sendEmail(this.email, message);
    }
}
```

### 3. Parallel Inheritance Hierarchies 🏗️

**Definition**: Every time you create a subclass of one class, you must also create a subclass of another class.

**Analogy**: It's like the relationship between a building and its maintenance manual. Every time a new type of building is created, you have to separately create a corresponding maintenance manual.

**Problem Code**:

```
// Shape hierarchy
public abstract class Shape {
    public abstract double area();
}

public class Circle extends Shape {
    private double radius;
    @Override
    public double area() { return Math.PI * radius * radius; }
}

// ShapeRenderer hierarchy (parallel to Shape hierarchy)
public abstract class ShapeRenderer {
    public abstract void render();
}

public class CircleRenderer extends ShapeRenderer {
    private Circle circle;
    @Override
    public void render() { /* Circle rendering logic */ }
}
```

**Solution**: Merge the two hierarchies or use composition instead of inheritance.

**Improved Code**:

```
public abstract class Shape {
    private Renderer renderer;

    public Shape(Renderer renderer) {
        this.renderer = renderer;
    }

    public abstract double area();

    public void render() {
        renderer.renderShape(this);
    }
}

public interface Renderer {
    void renderShape(Shape shape);
}
```

## Real-World Examples

How do these code smells appear in real business environments? For example, consider an e-commerce system.

### Divergent Change Real-World Example

If an order processing class handles order creation, payment processing, shipping handling, and notification sending all together:

1. Every time a new payment method is added, the class needs modification
2. When adding new shipping methods, modification is needed
3. When notification channels are added, modification is needed

By separating by responsibility:

```
public class OrderService { /* Order creation and management */ }
public class PaymentService { /* Payment processing */ }
public class ShippingService { /* Shipping handling */ }
public class NotificationService { /* Notification sending */ }
```

## Cautions and Tips 🚀

⚠️ **These are critical points!**

1. **Over-separation**: Separating classes into too-small units can actually increase complexity.
   - Keep related features together, but separate only elements that change for different reasons.
   - Always consider SOLID principles.
2. **Excessive abstraction**: Introducing too much abstraction anticipating changes can unnecessarily complicate code.
   - Remember the YAGNI (You Aren't Gonna Need It) principle.

💡 **Useful Tips**

- Identify parts where changes occur frequently and refactor them first.
- During code review, if the scope of change is wide, check for these code smells.
- Write tests first, then refactor—this allows safe changes.

## Conclusion

We've explored Change Preventers that hinder code modifications. Good code is code where only the relevant parts need modification when changes are necessary. By adhering to the Single Responsibility Principle (SRP), maintaining high cohesion among related features, and removing unnecessary dependencies, code changes become much easier.

Do you see these patterns in your own code? Please share how you solved them in the comments!

## References 📚

- [Refactoring: Improving the Design of Existing Code (Martin Fowler)](https://product.kyobobook.co.kr/detail/S000001810241)
- [Refactoring.Guru - Change Preventers](https://refactoring.guru/refactoring/smells/change-preventers)
- [Code Smells and Refactoring Techniques](https://luzkan.github.io/smells/divergent-change/)

---

#CodeSmell #Refactoring #CleanCode #SoftwareDesign
