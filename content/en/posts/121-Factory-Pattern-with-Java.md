---
title: "Factory Pattern with Java"
date: 2024-05-27T18:25:19+09:00
slug: "121-Factory-Pattern-with-Java"
original_url: "https://memoryhub.tistory.com/121"
tistory_id: 121
draft: false
---

*The factory pattern in Java is like a factory in real life where you create different products (objects) without specifying the exact class of the object that will be created.*

### The Big Picture

Imagine you own a toy factory. This factory can produce different types of toys, but you don't want to worry about the details of how each toy is made every time you need a new toy. Instead, you have a method in your factory that takes a type of toy and produces it for you. This is the essence of the factory pattern in programming: it provides a way to create objects without specifying the exact class of the object that will be created.

### Core Concepts

1. **Factory Method**: A method for creating objects, typically in a way that allows subclasses to alter the type of objects that will be created.
2. **Product**: The object that the factory method creates.
3. **ConcreteProduct**: A specific type of product created by the factory.
4. **Creator**: The class that contains the factory method.
5. **ConcreteCreator**: A subclass of Creator that overrides the factory method to return an instance of a ConcreteProduct.

### Detailed Walkthrough

Let's break down the factory pattern with a Java example.

#### Step 1: Define an Interface for the Products

```
public interface Toy {
    void play();
}
```

This interface defines the common behavior for all toys.

#### Step 2: Create Concrete Products

```
public class Car implements Toy {
    @Override
    public void play() {
        System.out.println("Playing with a car!");
    }
}

public class Doll implements Toy {
    @Override
    public void play() {
        System.out.println("Playing with a doll!");
    }
}
```

Here, `Car` and `Doll` are concrete implementations of the `Toy` interface.

#### Step 3: Create a Factory Class with a Factory Method

```
public class ToyFactory {
    public Toy createToy(String type) {
        if (type.equals("Car")) {
            return new Car();
        } else if (type.equals("Doll")) {
            return new Doll();
        }
        throw new IllegalArgumentException("Unknown toy type");
    }
}
```

The `ToyFactory` class contains a method `createToy` that takes a `String` indicating the type of toy and returns an instance of `Toy`.

### Understanding Through an Example

Here's how you can use the `ToyFactory` in your application:

```
public class Main {
    public static void main(String[] args) {
        ToyFactory factory = new ToyFactory();

        Toy car = factory.createToy("Car");
        car.play();  // Output: Playing with a car!

        Toy doll = factory.createToy("Doll");
        doll.play();  // Output: Playing with a doll!
    }
}
```

### Conclusion and Summary

The factory pattern allows you to create objects without specifying the exact class of the object that will be created. This is particularly useful when the creation process is complex or when the specific type of object isn't known until runtime. In Java, this is typically implemented using a factory class with a factory method that returns objects based on input parameters.

### Test Your Understanding

1. **What is the main advantage of using the factory pattern?**
2. **Can you extend the `ToyFactory` to create a new type of toy, such as a `Robot`? How would you modify the factory method?**
3. **Why might you choose a factory pattern over directly instantiating objects using `new`?**

### Reference

For further reading and examples, you can refer to the official [Oracle documentation on design patterns](https://docs.oracle.com/javase/tutorials/).
