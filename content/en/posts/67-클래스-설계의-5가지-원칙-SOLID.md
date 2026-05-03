---
title: "5 Class Design Principles - SOLID"
date: 2024-05-25T14:52:44+09:00
slug: "67-클래스-설계의-5가지-원칙-SOLID"
original_url: "https://memoryhub.tistory.com/67"
tistory_id: 67
draft: false
categories: ["Dev Concepts"]
tags: ["Info Processing Cert"]
---

## GPT Explanation

SOLID principles are 5 design principles in object-oriented programming and software development that promote **maintainability, flexibility, and extensibility**. These principles were introduced by Robert C. Martin (also known as Uncle Bob) and have been widely adopted in the software development community. The SOLID acronym stands for:

**Single Responsibility Principle (SRP)  
Open/Closed Principle (OCP)  
Liskov Substitution Principle (LSP)  
Interface Segregation Principle (ISP)  
Dependency Inversion Principle (DIP)**

Let's examine each principle in detail:

#### Single Responsibility Principle (SRP):

A principle that a class should have only one reason to change, meaning a class should have only one responsibility. By following this principle, you can modularize code through separation of concerns and make it easier to understand, maintain, and modify.

#### Open/Closed Principle (OCP):

Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means new functionality should be added without changing the existing codebase. This can be achieved through abstraction, inheritance, and polymorphism.

#### Liskov Substitution Principle (LSP):

Named after Barbara Liskov, this principle states that objects of a derived class should be replaceable with objects of the base class without affecting the correctness of the program. In other words, derived classes should extend or modify functionality while adhering to the contract (e.g., behavior and properties) of the base class.

LSP ensures that when you create a new class by extending an existing class, the new class works correctly everywhere the original class is used.

To help understand this principle, let's use an example:

Suppose we have a base class called "Bird" with a method called "fly". We're creating a derived class called "Penguin" that inherits from the "Bird" class. Since penguins cannot fly, we might want to override the "fly" method using an empty implementation or by throwing an exception.

However, doing so violates LSP because code that expects to fly using the "Bird" class won't work properly when using a "Penguin" object instead. To comply with LSP, you can modify the class hierarchy (e.g., introduce a new base class like "FlyingBird" for birds that can fly) or change the design to better accommodate the behavior of different birds.

In summary, the Liskov Substitution Principle encourages developers to create class hierarchies where derived classes truly extend the behavior of the base class and can be used interchangeably without unexpected results. This leads to more robust and maintainable code.

#### Interface Segregation Principle (ISP):

Emphasizes that classes should not be forced to implement interfaces they don't use. Instead, it's better to create multiple smaller, more focused interfaces. This provides cleaner separation of concerns, making the system easier to understand, maintain, and change.

#### Dependency Inversion Principle (DIP):

DIP is a principle that high-level modules should not depend on low-level modules; rather, both should depend on abstractions. Additionally, abstractions should not depend on details; details should depend on abstractions. This principle encourages the use of dependency injection and inversion of control, enabling more flexible, testable, and maintainable software.

By adhering to SOLID principles, developers can create more robust, maintainable, and adaptable software. While these principles are not one-size-fits-all solutions, they provide useful guidelines for designing and structuring code in an efficient and systematic way.

## SRP (Single Responsibility Principle)

- A class should have only one responsibility.

### Before applying SRP

```
public class Production {

    private String name;
    private int price;

    public Production(String name, int price) {
        this.name = name;
        this.price = price;
    }

    public void updatePrice(int price) {
        this.price = price;
    }
}

public class ProductionUpdateService {

    // Responsibility of changing Product contents
    public void update(Production production, int price) {
        //validate price
        validatePrice(price);

        //update price
        production.updatePrice(price);
    }
	// Is validating price validity a responsibility of ProductionUpdateService? ???
    private void validatePrice(int price) {
        if (price < 1000) {
            throw new IllegalArgumentException("Minimum price must be 1000 won or more.");
        }
    }

}
```

Isn't it more appropriate to see validating price as the responsibility of Production, which actually changes price information?

So based on this, we moved the responsibility of validation to Production!

### After applying SRP

```
public class Production {

    private static final int MINIMUM_PRICE = 1000;

    private String name;
    private int price;

    public Production(String name, int price) {
        this.name = name;
        this.price = price;
    }

    public void updatePrice(int price) {
        validatePrice(price);
        this.price = price;
    }

    private void validatePrice(int price) {
        if (price < MINIMUM_PRICE) {
            throw new IllegalArgumentException(String.format("Minimum price must be %d won or more.", MINIMUM_PRICE));
        }
    }
}

public class ProductionUpdateService {

    public void update(Production production, int price) {
        //update price
        production.updatePrice(price);
    }

}
```

## 2 OCP (Open-Closed Principle)

- Software elements should be open for extension but closed for modification.

### Before applying OCP

```
public class Production {
    private String name;
    private int price;
    // N(General), E(E-ticket), L(Local products)...
    private String option;

    public Production(String name, int price, String option) {
        this.name = name;
        this.price = price;
        this.option = option;
    }

    public int getNameLength() {
        return name.length();
    }

    public String getOption() {
        return option;
    }
}

// Validator with limited extensibility and easy modification (no interface)
public class ProductionValidator {
    public void validateProduction(Production production) throws IllegalArgumentException {

        if (production.getOption().equals("N")) {
            if (production.getNameLength() < 3) {
                throw new IllegalArgumentException("General product name must be longer than 3 characters.");
            }
        } else if (production.getOption().equals("E")) {
            if (production.getNameLength() < 10) {
                throw new IllegalArgumentException("E-ticket product name must be longer than 10 characters.");
            }
        } else if (production.getOption().equals("L")) {
            if (production.getNameLength() < 20) {
                throw new IllegalArgumentException("Local product name must be longer than 20 characters.");
            }
        }

    }
}
```

### After applying OCP principle

```
public interface Validator {

    boolean support(Production production);

    void validate(Production production) throws IllegalArgumentException;

}

public class DefaultValidator implements Validator {
    @Override
    public boolean support(Production production) {
        return production.getOption().equals("N");
    }

    @Override
    public void validate(Production production) throws IllegalArgumentException {
        if (production.getNameLength() < 3) {
            throw new IllegalArgumentException("General product name must be longer than 3 characters.");
        }
    }
}

public class ETicketValidator implements Validator {
    @Override
    public boolean support(Production production) {
        return production.getOption().equals("E");
    }

    @Override
    public void validate(Production production) throws IllegalArgumentException {
        if (production.getNameLength() < 10) {
            throw new IllegalArgumentException("E-ticket product name must be longer than 10 characters.");
        }
    }
}

public class LocalValidator implements Validator {
    @Override
    public boolean support(Production production) {
        return production.getOption().equals("L");
    }

    @Override
    public void validate(Production production) throws IllegalArgumentException {
        if (production.getNameLength() < 20) {
            throw new IllegalArgumentException("Local product name must be longer than 20 characters.");
        }
    }
}

public class ProductValidator {

    private final List<Validator> validators = Arrays.asList(new DefaultValidator(), new ETicketValidator(), new LocalValidator());

    public void validate(Production production) {
        Validator productionValidator = new DefaultValidator();

        for (Validator localValidator : validators) {
            if (localValidator.support(production)) {
                productionValidator = localValidator;
                break;
            }
        }

        productionValidator.validate(production);
    }
}
```

## 3 LSP (Liskov Substitution Principle)

- A child class must be able to perform at least the behavior that is possible in its parent class.
- A parent type object must be replaceable with a child type object without affecting the correctness of the program using the parent type.

### Example code of Liskov Substitution Principle:

```
// Parent Class
class Animal {
    public void makeSound() {
        System.out.println("Generic animal sound");
    }
}

// SubClass Of Animal Called Dog
class Dog extends Animal {
    public void makeSound() {
        System.out.println("Bark!");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog();  // LSP - using an object of type Dog as an object of type Animal
        animal.makeSound();  // this will call the Dog's makeSound() method
    }
}
```

### Benefits of Liskov Substitution Principle

- Allows for more flexible and maintainable code.

By ensuring that objects of a subclass can be used interchangeably with objects of its superclass, we can write code that is more modular and reusable.  
This makes it easier to update and modify the code over time, as we can add new subclasses without having to change the existing code that uses the superclass.

Additionally, following the LSP can help catch potential errors or issues early on in the development process. If a subclass violates the LSP and does not behave in the same way as its superclass, it can cause unexpected behavior or errors when used in place of the superclass.  
By adhering to the LSP, we can catch these issues early and ensure that the code works correctly and predictably.

Overall, following the LSP can lead to more maintainable and robust code that is easier to work with and modify over time.

### Before applying LSP

```
class Rectangle {
  protected _width: number = -1;
  protected _height: number = -1;

  public get width() {
    return this._width;
  }
  public set width(w: number) {
    this._width = w;
  }

  public get height() {
    return this._height;
  }
  public set height(h: number) {
    this._height = h;
  }

  public get area() {
    return this._width * this._height;
  }
}

class Square extends Rectangle {
  public set width(w: number) {
    this._width = w;
    this._height = w;
  }

  public set height(h: number) {
    this._width = h;
    this._height = h;
  }
}

const rec: Rectangle = new Rectangle();
rec.width = 3;
rec.height = 4;

console.log(rec.area === 12); // true

// Child class cannot perform the behavior used in parent class.
const rec2: Rectangle = new Square();
rec2.width = 3;
rec2.height = 4;

console.log(rec.area === 12); // false
```

The child class Square is not performing the area() functionality of the parent class Rectangle properly.

### After applying LSP

```
// The Shape interface is assumed to be something that can calculate area (face from a geometric perspective).
interface Shape {
  readonly area: number;
}

class Rectangle implements Shape {
  constructor(public width: number, public height: number) {}

  public get area() {
    return this.width * this.height;
  }
}

class Square implements Shape {
  constructor(public width: number) {}

  public get area() {
    return this.width ** 2;
  }
}

const rec: Shape = new Rectangle(3, 4);
console.log(rec.area); // 12

const sq: Shape = new Square(4);
console.log(sq.area);  // 16
```

## 4 ISP (Integration Segregation Principle)

- Multiple interfaces for a specific client is better than one general-purpose interface.

### Before applying ISP

```
public interface AllInOneDevice {
    void print();

    void copy();

    void fax();
}

public class SmartMachine implements AllInOneDevice {
    @Override
    public void print() {
        System.out.println("print");
    }

    @Override
    public void copy() {
        System.out.println("copy");
    }

    @Override
    public void fax() {
        System.out.println("fax");
    }
}

package solid.isp.before;

public class PrinterMachine implements AllInOneDevice {
    @Override
    public void print() {
        System.out.println("print");
    }

    @Override
    public void copy() {
        throw new UnsupportedOperationException();
    }

    @Override
    public void fax() {
        throw new UnsupportedOperationException();
    }
}
```

The print method, which is responsible for printing, is overridden, but the remaining functions don't need to be implemented, so UnsupportedOperationException is thrown.  
In this case, a client that only knows the interface cannot know whether the printer has the copy function implemented or not, so it may encounter unexpected errors.

### After applying ISP

```
public interface PrinterDevice {
    void print();
}

public interface CopyDevice {
    void copy();
}

public interface FaxDevice {
    void fax();
}

public class SmartMachine implements PrinterDevice, CopyDevice, FaxDevice {
    @Override
    public void print() {
        System.out.println("print");
    }

    @Override
    public void copy() {
        System.out.println("copy");
    }

    @Override
    public void fax() {
        System.out.println("fax");
    }
}

// Implemented object
public class PrinterMachine implements PrinterDevice {
	@Override
 	public void print() {
    		System.out.println("print");
	}
}

		// When used by client
@DisplayName("If only one function is needed, implement only one interface")
@Test
void singleInterface() {
    PrinterDevice printer = new SmartMachine();
    printer.print();
}
```

## 5 DIP (Dependency Inversion Principle)

- Software should depend on abstractions, not on concretes.

### Before applying DIP

```
public class ProductionService {

    private final LocalValidator localValidator;

    public ProductionService(LocalValidator localValidator) {
        this.localValidator = localValidator;
    }

    public void validate(Production production) {
        localValidator.validate(production);
    }

}

public class LocalValidator {

    public void validate(Production production) {
        //validate
    }
}
```

### After applying DIP

```
public interface Validator {
    void validate(Production production);
}

public class LocalValidator implements Validator {
    @Override
    public void validate(Production production) {
        //validate
    }
}

public class ETicketValidator implements Validator {
    @Override
    public void validate(Production production) {
        //validate
    }
}

public class ProductionService {

    private final Validator validator;

    public ProductionService(Validator validator) {
        this.validator = validator;
    }

    public void validate(Production production) {
        validator.validate(production);
    }
}
```

### References

<https://bottom-to-top.tistory.com/27>  
<https://medium.com/humanscape-tech/solid-%EB%B2%95%EC%B9%99-%E4%B8%AD-lid-fb9b89e383ef>
