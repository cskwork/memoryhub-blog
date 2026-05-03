---
title: "Observer Pattern with Java"
date: 2024-05-30T18:29:14+09:00
slug: "122-Observer-Pattern-with-Java"
original_url: "https://memoryhub.tistory.com/122"
tistory_id: 122
draft: false
categories: ["Dev Concepts"]
tags: ["Design Pattern"]
---

*The observer pattern is like a subscription service where subscribers get updates whenever there is a change or new information.*

### The Big Picture

Imagine you subscribe to a magazine. Whenever there's a new issue, the magazine company sends it to all its subscribers. You don't have to keep checking if a new issue is out; it comes to you automatically. Similarly, in programming, the observer pattern allows objects (observers) to get notified of changes in another object (subject) without constantly checking for updates.

### Core Concepts

1. **Subject**: The object that holds the state and notifies observers about changes.
2. **Observer**: The object that wants to be notified when the subject's state changes.
3. **ConcreteSubject**: A specific implementation of the subject.
4. **ConcreteObserver**: A specific implementation of the observer.

### Detailed Walkthrough

Let's break down the observer pattern with a Java example.

#### Step 1: Define the Observer Interface

```
public interface Observer {
    void update(String message);
}
```

The `Observer` interface has a method `update` that gets called when the subject changes.

#### Step 2: Define the Subject Interface

```
import java.util.ArrayList;
import java.util.List;

public interface Subject {
    void registerObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers();
}
```

The `Subject` interface has methods to register, remove, and notify observers.

#### Step 3: Create a Concrete Subject

```
public class MagazinePublisher implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private String latestIssue;

    @Override
    public void registerObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(latestIssue);
        }
    }

    public void newIssueReleased(String issue) {
        this.latestIssue = issue;
        notifyObservers();
    }
}
```

`MagazinePublisher` maintains a list of observers and notifies them whenever a new issue is released.

#### Step 4: Create Concrete Observers

```
public class Subscriber implements Observer {
    private String name;

    public Subscriber(String name) {
        this.name = name;
    }

    @Override
    public void update(String message) {
        System.out.println(name + " received new issue: " + message);
    }
}
```

`Subscriber` implements the `Observer` interface and prints a message when it gets updated.

### Understanding Through an Example

Here's how you can use the observer pattern in your application:

```
public class Main {
    public static void main(String[] args) {
        MagazinePublisher publisher = new MagazinePublisher();

        Observer subscriber1 = new Subscriber("Alice");
        Observer subscriber2 = new Subscriber("Bob");

        publisher.registerObserver(subscriber1);
        publisher.registerObserver(subscriber2);

        publisher.newIssueReleased("Issue 1");  // Both Alice and Bob get notified

        publisher.removeObserver(subscriber1);

        publisher.newIssueReleased("Issue 2");  // Only Bob gets notified
    }
}
```

### Conclusion and Summary

The observer pattern allows objects to get notified of changes in another object without needing to constantly check for updates. This is particularly useful for implementing distributed event handling systems. In Java, this pattern typically involves creating `Subject` and `Observer` interfaces and concrete implementations for each.

### Test Your Understanding

1. **What are the main advantages of using the observer pattern?**
2. **Can you think of a real-world scenario (besides magazines) where the observer pattern might be useful?**
3. **How would you modify the `MagazinePublisher` to send additional information, such as the release date of the issue, to the observers?**

### Reference

For further reading and examples, you can refer to the official [Oracle documentation on design patterns](https://docs.oracle.com/javase/tutorials/).
