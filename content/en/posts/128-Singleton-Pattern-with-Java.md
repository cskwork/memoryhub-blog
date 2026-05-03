---
title: "Singleton Pattern with Java"
date: 2024-05-28T22:51:49+09:00
slug: "128-Singleton-Pattern-with-Java"
original_url: "https://memoryhub.tistory.com/128"
tistory_id: 128
draft: false
---

*The Singleton Pattern ensures a class has only one instance and provides a global point of access to that instance, like having a single captain of a ship who is the only one steering it.*

### The Big Picture

Imagine you have a ship, and you want to make sure there's only one captain in charge. If there were multiple captains, they'd give conflicting orders, causing chaos. In programming, sometimes we want to ensure that a class has only one instance to avoid inconsistent states or conflicts. This is where the Singleton Pattern comes in.

### Core Concepts

1. **Single Instance**: The Singleton Pattern restricts the instantiation of a class to one "single" instance.
2. **Global Access**: Provides a global point of access to that instance.
3. **Lazy Initialization**: The instance is created only when it is needed for the first time.

### Detailed Walkthrough

Let's break down how we implement the Singleton Pattern in Java step-by-step:

1. **Private Constructor**: Ensure the class constructor is private so no other class can instantiate it.
2. **Static Instance**: Create a static instance of the class within the class itself.
3. **Public Method to Access Instance**: Provide a public method that returns the instance of the class, creating it if it doesn't already exist.

Here's a basic implementation:

```java
public class Singleton {
    // Step 2: Create a static instance of the class
    private static Singleton instance;

    // Step 1: Private constructor to prevent instantiation
    private Singleton() {}

    // Step 3: Public method to provide access to the instance
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

### Understanding Through an Example

Let's enhance our analogy with a code example. Imagine we have a `Captain` class for our ship:

```java
public class Captain {
    private static Captain captain;

    // Private constructor
    private Captain() {
        System.out.println("A captain is appointed.");
    }

    // Public method to get the single instance
    public static Captain getCaptain() {
        if (captain == null) {
            captain = new Captain();
        }
        return captain;
    }

    public void giveOrder(String order) {
        System.out.println("Captain's order: " + order);
    }
}

public class Ship {
    public static void main(String[] args) {
        // Try to get two captains
        Captain captain1 = Captain.getCaptain();
        Captain captain2 = Captain.getCaptain();

        // Both should be the same instance
        System.out.println("Captain1: " + captain1);
        System.out.println("Captain2: " + captain2);

        // Captain gives an order
        captain1.giveOrder("Full speed ahead!");
    }
}
```

### Conclusion and Summary

The Singleton Pattern ensures a class has only one instance and provides a global point of access to it. This is achieved by:

1. Making the constructor private.
2. Creating a static instance within the class.
3. Providing a public method to access this instance.

In our example, the `Captain` class ensures there's only one captain for the ship, avoiding conflicts and maintaining consistent command.

### Test Your Understanding

1. Why is the constructor of a Singleton class made private?
2. What would happen if the `getInstance` method was not synchronized in a multithreaded environment?
3. Can you modify the Singleton implementation to make it thread-safe?

### Reference

For further reading, you can refer to the official [Java documentation on Singleton Pattern](https://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html) or explore the concept in the book "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides.
