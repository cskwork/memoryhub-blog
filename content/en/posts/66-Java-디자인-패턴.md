---
title: "Java - Design Patterns"
date: 2024-05-25T14:51:50+09:00
slug: "66-Java-디자인-패턴"
original_url: "https://memoryhub.tistory.com/66"
tistory_id: 66
draft: false
---

![](/images/66-Java-디자인-패턴/img.png)

## Summary

How do we create, structure, and manage product (object) factories? Like instruction manuals.

**Creational Patterns**  
**Use interface at access points, separate roles**

- Abstract Factory Pattern: **Provide an interface for creating independent objects** based on which concrete classes are specified
- Builder Pattern: **Separate the creation process and representation of complex objects** to create diverse representations from the same creation process
- Factory Method Pattern: Child classes create objects and parent classes **only declare creation methods** serving as an **interface**
- Singleton Pattern: **Guarantee a class has only one instance and provide a global access point** to it

**Structural Patterns**  
**Use alternate purposes, tree structures, unified interfaces**

- Adapter Pattern: Use an **adapter class that changes interfaces** to suit usage. Used when developed elsewhere or difficult to modify.
- Composite Pattern: Branches (leaf) implement an interface and composite class defines functions to manage child classes. **Represent part-whole hierarchies as tree structures**
- Facade Pattern: Create a **unified interface** to easily access/use subsystems. All for One

**Behavioral Patterns**  
Recognize state changes, integrate operations/requests

- Observer Pattern: **Event listener** pattern. Recognize state changes in one object, and when changed call other objects dependent on that object to update information.
- Strategy Pattern: Define multiple action logic and **bundle and manage** them as one.
- State Pattern: Object behavior changes according to internal state
- Memento Pattern: Pre-record/save state then restore, overhead from saving previous values

# Creational Patterns

## Abstract Factory Pattern (Object)

![](/images/66-Java-디자인-패턴/img_1.png)

### Definition

#### AbstractFactory

- Interface for object creation classes
- **Interface for opertations** that creates abstract Product objects without specifing concrete classes

#### ConcreteFactory

- Object creation class
- Implements AbstractFactory to **create Product objects**.

#### Product

- Object created from factory class
- Implements AbstractProduct interface, defines  
  **objects made by ConcreteFactory**.

#### Client

- UI using factory and (abstracted) objects made from
- Uses interfaces made by AbstractFactory and  
  AbstractProduct classes.

### Advantages

- when client doesn't know exactly what type to create.
- Isolation of concrete classes
- Exchanging Product Families easily
- Promoting consistency among products

### Disadvantages

- Difficult to support new kinds of products

### Code Application

```
// Java Program to demonstrate the
// working of Abstract Factory Pattern

enum CarType
{
	MICRO, MINI, LUXURY
}

// Abstract Product
abstract class Car
{
	Car(CarType model, Location location)
	{
		this.model = model;
		this.location = location;
	}

	abstract void construct();

	CarType model = null;
	Location location = null;

	CarType getModel()
	{
		return model;
	}

	void setModel(CarType model)
	{
		this.model = model;
	}

	Location getLocation()
	{
		return location;
	}

	void setLocation(Location location)
	{
		this.location = location;
	}

	@Override
	public String toString()
	{
		return "CarModel - "+model + " located in "+location;
	}
}

// Product
class LuxuryCar extends Car
{
	LuxuryCar(Location location)
	{
		super(CarType.LUXURY, location);
		construct();
	}
	@Override
	protected void construct()
	{
		System.out.println("Connecting to luxury car");
	}
}

// Product
class MicroCar extends Car
{
	MicroCar(Location location)
	{
		super(CarType.MICRO, location);
		construct();
	}
	@Override
	protected void construct()
	{
		System.out.println("Connecting to Micro Car ");
	}
}

// Product
class MiniCar extends Car
{
	MiniCar(Location location)
	{
		super(CarType.MINI,location );
		construct();
	}

	@Override
	void construct()
	{
		System.out.println("Connecting to Mini car");
	}
}

enum Location
{
DEFAULT, USA, INDIA
}

// Concrete Factory
class INDIACarFactory
{
	static Car buildCar(CarType model)
	{
		Car car = null;
		switch (model)
		{
			case MICRO:
				car = new MicroCar(Location.INDIA);
				break;

			case MINI:
				car = new MiniCar(Location.INDIA);
				break;

			case LUXURY:
				car = new LuxuryCar(Location.INDIA);
				break;

				default:
				break;

		}
		return car;
	}
}

// Concrete Factory
class DefaultCarFactory
{
	public static Car buildCar(CarType model)
	{
		Car car = null;
		switch (model)
		{
			case MICRO:
				car = new MicroCar(Location.DEFAULT);
				break;

			case MINI:
				car = new MiniCar(Location.DEFAULT);
				break;

			case LUXURY:
				car = new LuxuryCar(Location.DEFAULT);
				break;

				default:
				break;

		}
		return car;
	}
}

// Concrete Factory
class USACarFactory
{
	public static Car buildCar(CarType model)
	{
		Car car = null;
		switch (model)
		{
			case MICRO:
				car = new MicroCar(Location.USA);
				break;

			case MINI:
				car = new MiniCar(Location.USA);
				break;

			case LUXURY:
				car = new LuxuryCar(Location.USA);
				break;

				default:
				break;

		}
		return car;
	}
}

// Abstract Factory
class CarFactory
{
	private CarFactory()
	{

	}
	public static Car buildCar(CarType type)
	{
		Car car = null;
		// We can add any GPS Function here which
		// read location property somewhere from configuration
		// and use location specific car factory
		// Currently I'm just using INDIA as Location
		Location location = Location.INDIA;

		switch(location)
		{
			case USA:
				car = USACarFactory.buildCar(type);
				break;

			case INDIA:
				car = INDIACarFactory.buildCar(type);
				break;

			default:
				car = DefaultCarFactory.buildCar(type);

		}

		return car;

	}
}

class AbstractDesign
{
	public static void main(String[] args)
	{
		System.out.println(CarFactory.buildCar(CarType.MICRO));
		System.out.println(CarFactory.buildCar(CarType.MINI));
		System.out.println(CarFactory.buildCar(CarType.LUXURY));
	}
}

/*
OUTPUT

Connecting to Micro Car 
CarModel - MICRO located in INDIA
Connecting to Mini car
CarModel - MINI located in INDIA
Connecting to luxury car
CarModel - LUXURY located in INDIA
*/
```

## Builder Pattern

![](/images/66-Java-디자인-패턴/img_2.png)

### Definition

#### Product

- Define the type of object to be generated
- Defines the type of object to be generated

#### Builder

- Define the process for object creation
- Abstract base class that defines all steps needed to create product.

#### ConcreteBuilder

- Inherit builder class and create objects
- Inherits builder and has function to create objects

#### Director

- Control the algorithm that creates the final product object
- Controls algorithm that makes final product object.

### Advantages

- highly readable due to minimal constructor parameters
- objects build with minimal complex logic

### Disadvantages

- code lines increase
- requires create separate ConcreteBuilder for each different type of product

### Code Application

```
// Abstract Product
interface HousePlan
{
	public void setBasement(String basement);

	public void setStructure(String structure);

	public void setRoof(String roof);

	public void setInterior(String interior);
}

// Product
class House implements HousePlan
{

	private String basement;
	private String structure;
	private String roof;
	private String interior;

	public void setBasement(String basement)
	{
		this.basement = basement;
	}

	public void setStructure(String structure)
	{
		this.structure = structure;
	}

	public void setRoof(String roof)
	{
		this.roof = roof;
	}

	public void setInterior(String interior)
	{
		this.interior = interior;
	}

}

// Builder
interface HouseBuilder
{

	public void buildBasement();

	public void buildStructure();

	public void buildRoof();

	public void buildInterior();

	public House getHouse();
}

// Concrete Builder
class IglooHouseBuilder implements HouseBuilder
{
	private House house;

	public IglooHouseBuilder()
	{
		this.house = new House();
	}

	public void buildBasement()
	{
		house.setBasement("Ice Bars");
	}

	public void buildStructure()
	{
		house.setStructure("Ice Blocks");
	}

	public void buildInterior()
	{
		house.setInterior("Ice Carvings");
	}

	public void buildRoof()
	{
		house.setRoof("Ice Dome");
	}

	public House getHouse()
	{
		return this.house;
	}
}

// Concrete Builder
class TipiHouseBuilder implements HouseBuilder
{
	private House house;

	public TipiHouseBuilder()
	{
		this.house = new House();
	}

	public void buildBasement()
	{
		house.setBasement("Wooden Poles");
	}

	public void buildStructure()
	{
		house.setStructure("Wood and Ice");
	}

	public void buildInterior()
	{
		house.setInterior("Fire Wood");
	}

	public void buildRoof()
	{
		house.setRoof("Wood, caribou and seal skins");
	}

	public House getHouse()
	{
		return this.house;
	}

}

// Director
class CivilEngineer
{

	private HouseBuilder houseBuilder;

	public CivilEngineer(HouseBuilder houseBuilder)
	{
		this.houseBuilder = houseBuilder;
	}

	public House getHouse()
	{
		return this.houseBuilder.getHouse();
	}

	public void constructHouse()
	{
		this.houseBuilder.buildBasement();
		this.houseBuilder.buildStructure();
		this.houseBuilder.buildRoof();
		this.houseBuilder.buildInterior();
	}
}

class Builder
{
	public static void main(String[] args)
	{
		HouseBuilder iglooBuilder = new IglooHouseBuilder();
		CivilEngineer engineer = new CivilEngineer(iglooBuilder);

		engineer.constructHouse();

		House house = engineer.getHouse();

		System.out.println("Builder constructed: "+ house);
	}
}
/*
Output : 
Builder constructed: House@6d06d69c
*/
```

## Singleton Pattern

- When an instance is needed, don't create the same instance again but use the existing instance.
- Create the instance in memory only once when the app starts

**Why use it?**

- Prevent memory waste and share with other class instances

### Advantages

**When is it commonly used?**

- When common objects need to be created multiple times, database connection pools, thread pools, caches, log recording objects, etc.

### Disadvantages

- If a singleton instance does too many things alone or shares too much data, coupling between other classes increases, violating the Open-Closed Principle
- In multi-threaded environments when synchronization isn't handled, two instances can be created

![](/images/66-Java-디자인-패턴/img_3.png)

VS

![](/images/66-Java-디자인-패턴/img_4.png)

### Code Application

**How to Create Thread-Safe Singleton in Multi-threaded Environment**

```
//1 Lazy Initialization (Delayed Initialization)
public class ThreadSafe_Lazy_Initialization{

    private static ThreadSafe_Lazy_Initialization instance;

    private ThreadSafe_Lazy_Initialization(){}

    public static synchronized ThreadSafe_Lazy_Initialization getInstance(){
        if(instance == null){
            instance = new ThreadSafe_Lazy_Initialization();
        }
        return instance;
    }

}

//2 Lazy Initialization + Double-checked Locking (Mitigate Performance Degradation)
public class ThreadSafe_Lazy_Initialization{
    private volatile static ThreadSafe_Lazy_Initialization instance;

    private ThreadSafe_Lazy_Initialization(){}

    public static ThreadSafe_Lazy_Initialization getInstance(){
    	if(instance == null) {
        	synchronized (ThreadSafe_Lazy_Initialization.class){
                if(instance == null){
                    instance = new ThreadSafe_Lazy_Initialization();
                }
            }
        }
        return instance;
    }
}

//3 Initialization on demand holder idiom (Initialization by holder) - General and Most Used!
public class Something {
    private Something() {
    }

    private static class LazyHolder {
        public static final Something INSTANCE = new Something();
    }

    public static Something getInstance() {
        return LazyHolder.INSTANCE;
    }
}
```

**Explanation of #3**

- Don't use synchronization to delegate singleton initialization responsibility to JVM
- Instance declared in holder is static, so called only once at class loading time
- Using final ensures value is not reassigned

## Factory Method Pattern (Method)

Object creation is delegated to subclass.  
In other words, parent serves as class interface and child handles creation with interface

```
public abstract class RobotFactory {
	abstract Robot createRobot(String name);
}
```

```
public class SuperRobotFactory extends RobotFactory {
	@Override
	Robot createRobot(String name) {
		switch(name) {
		case "super" :
			return new SuperRobot();
		case "power" :
			return new PowerRobot();
		}
		return null;
	}
}
```

# Structural Patterns

## Adapter Pattern

- Convert incompatible interfaces with adapter to make them compatible.

![](/images/66-Java-디자인-패턴/img_5.png)

![](/images/66-Java-디자인-패턴/img_6.png)

### Code Application

```
package AdapterPattern;

public interface Duck {
	public void quack();
	public void fly();
}
```

```
package AdapterPattern;

public interface Turkey {
	public void gobble();
	public void fly();
}
```

```
package AdapterPattern;

public class WildTurkey implements Turkey {

	@Override
	public void gobble() {
		System.out.println("Gobble gobble");
	}

	@Override
	public void fly() {
		System.out.println("I'm flying a short distance");
	}
}
```

```
package AdapterPattern;

public class TurkeyAdapter implements Duck {

	Turkey turkey;

	public TurkeyAdapter(Turkey turkey) {
		this.turkey = turkey;
	}

	@Override
	public void quack() {
		turkey.gobble();
	}

	@Override
	public void fly() {
		turkey.fly();
	}

}
```

```
package AdapterPattern;

public class DuckTest {

	public static void main(String[] args) {

		MallardDuck duck = new MallardDuck();
		WildTurkey turkey = new WildTurkey();
		Duck turkeyAdapter = new TurkeyAdapter(turkey);

		System.out.println("The turkey says...");
		turkey.gobble();
		turkey.fly();

		System.out.println("The Duck says...");
		testDuck(duck);

		System.out.println("The TurkeyAdapter says...");
		testDuck(turkeyAdapter);

	}

	public static void testDuck(Duck duck) {

		duck.quack();
		duck.fly();

	}
}
```

## Composite Pattern

### Definition

- Compose objects into tree structures to represent part-whole hierarchies. Each node in the tree performs a task.
- Composition object create 'has-a' relationship between objects. Grouped objects of similar functions.

#### Component

- Makes interface for objects in composition and to access child components

#### Leaf

- Defines behavior for primitive objects

#### Composite

- Stores child components and implements child related operations

#### Client

- Manipulates objects in compositions.

### Advantages:

- children management functions declared in Composite class providing Safety

### Disadvantages:

- Calling children management function from Leaf class causes runtime exception

![](/images/66-Java-디자인-패턴/img_7.png)

"Client" class references common interface "Component" rather than directly referencing "Leaf" and "Composite" classes.

"Leaf" class implements "Component" interface.

"Composite" class maintains "Component" child objects and passes requests like operation() to children.

![](/images/66-Java-디자인-패턴/img_8.png)

### Code Application

```
// A Java program to demonstrate working of
// Composite Design Pattern with example
// of a company with different
// employee details

import java.util.ArrayList;
import java.util.List;

// A common interface for all employee

// Interface Component
interface Employee
{
	public void showEmployeeDetails();
}

// Leaf 1
class Developer implements Employee
{
	private String name;
	private long empId;
	private String position;

	public Developer(long empId, String name, String position)
	{
		// Assign the Employee id,
		// name and the position
		this.empId = empId;
		this.name = name;
		this.position = position;
	}

	@Override
	public void showEmployeeDetails()
	{
		System.out.println(empId+" " +name+ " " + position );
	}
}

// Leaf 2
class Manager implements Employee
{
	private String name;
	private long empId;
	private String position;

	public Manager(long empId, String name, String position)
	{
		this.empId = empId;
		this.name = name;
		this.position = position;
	}

	@Override
	public void showEmployeeDetails()
	{
		System.out.println(empId+" " +name+ " " + position );
	}
}

// Class used to get Employee List
// and do the opertions like
// add or remove Employee

// Composite
class CompanyDirectory implements Employee
{
	private List<Employee> employeeList = new ArrayList<Employee>();

	@Override
	public void showEmployeeDetails()
	{
		for(Employee emp:employeeList)
		{
			emp.showEmployeeDetails();
		}
	}

	public void addEmployee(Employee emp)
	{
		employeeList.add(emp);
	}

	public void removeEmployee(Employee emp)
	{
		employeeList.remove(emp);
	}
}

// Driver class

// Client
public class Company
{
	public static void main (String[] args)
	{
		Developer dev1 = new Developer(100, "Lokesh Sharma", "Pro Developer");
		Developer dev2 = new Developer(101, "Vinay Sharma", "Developer");
		CompanyDirectory engDirectory = new CompanyDirectory();
		engDirectory.addEmployee(dev1);
		engDirectory.addEmployee(dev2);

		Manager man1 = new Manager(200, "Kushagra Garg", "SEO Manager");
		Manager man2 = new Manager(201, "Vikram Sharma ", "Kushagra's Manager");

		CompanyDirectory accDirectory = new CompanyDirectory();
		accDirectory.addEmployee(man1);
		accDirectory.addEmployee(man2);

		CompanyDirectory directory = new CompanyDirectory();
		directory.addEmployee(engDirectory);
		directory.addEmployee(accDirectory);
		directory.showEmployeeDetails();
	}
}
```

#### Output

```
100 Lokesh Sharma Pro Developer
101 Vinay Sharma Developer
200 Kushagra Garg SEO Manager
201 Vikram Sharma  Kushagra's Manager
```

## Facade Pattern

- Provide an integrated and simplified interface to subsystems for easy access/use. All for One

![](/images/66-Java-디자인-패턴/img_9.png)

### Advantages

- Isolation of complexity
- Testing Process - process of testing convenient
- Loose Coupling between client and subsystem.

### Disadvantages

- change in method requires change in facade
- costly process of establishing facade method
- violation of rules during facade construction

### Code Application

```
// Product Interface 
package structural.facade;
public interface Hotel
{
	public Menus getMenus();
}

// Product
package structural.facade;

public class NonVegRestaurant implements Hotel
{
	public Menus getMenus()
	{
		NonVegMenu nv = new NonVegMenu();
		return nv;
	}
}

// Product
package structural.facade;

public class VegRestaurant implements Hotel
{
	public Menus getMenus()
	{
		VegMenu v = new VegMenu();
		return v;
	}
}

// Product
package structural.facade;

public class VegNonBothRestaurant implements Hotel
{
	public Menus getMenus()
	{
		Both b = new Both();
		return b;
	}
}

// Facade
package structural.facade;

public class HotelKeeper
{
	public VegMenu getVegMenu()
	{
		VegRestaurant v = new VegRestaurant();
		VegMenu vegMenu = (VegMenu)v.getMenus();
		return vegMenu;
	}

	public NonVegMenu getNonVegMenu()
	{
		NonVegRestaurant v = new NonVegRestaurant();
		NonVegMenu NonvegMenu = (NonVegMenu)v.getMenus();
		return NonvegMenu;
	}

	public Both getVegNonMenu()
	{
		VegNonBothRestaurant v = new VegNonBothRestaurant();
		Both bothMenu = (Both)v.getMenus();
		return bothMenu;
	}	
}

// Client
package structural.facade;

public class Client
{
	public static void main (String[] args)
	{
		HotelKeeper keeper = new HotelKeeper();

		VegMenu v = keeper.getVegMenu();
		NonVegMenu nv = keeper.getNonVegMenu();
		Both = keeper.getVegNonMenu();

	}
}
```

# Behavioral Patterns

## Observer Pattern

- Subject object that maintains state & Observer object that needs to know state changes
- Immediately performs predefined actions whenever an event occurs
- Observer pattern defines a 1:N (or 1:1) relationship where when one object's state changes, dependent objects are notified and automatically have their information updated
- Class A instantiates class B to receive B's events, then B calls methods in class A whenever events occur
- In Android development, things like OnClickListener are Observer pattern applications (Button (Publisher) changes state when clicked, notifying Observer OnClickListener)

```
// Inherit this interface and implement methods to call whenever events occur
interface EventListener {
    fun onEvent(count: Int)
}

// Counter that fires events when multiples of 5 are detected
class Counter(var listener: EventListener) { // Receive EventListener through constructor
    fun count() {
        for (i in 1..100) {  // Count 1 to 100
            if (i % 5 == 0) {
                listener.onEvent(i)
            }
        }
    }
}

// EventPrinter that receives events and prints multiples of 5 to screen
class EventPrinter: EventListener {
	  // Inherit listener and implement callback method (print multiples of 5)
    override fun onEvent(count: Int) {
        print("${count}-")
    }

    fun start(){
        // Pass EventListener implementation through this (polymorphism!)
        Counter(this).count()  // 
    }
}

// EventPrinter: Listener implementation that receives and prints events
// Counter: Class that counts numbers and fires events when detecting multiples of 5
// EventListener: Observer connecting above two elements

fun main() {
    EventPrinter().start()
}
```

![](/images/66-Java-디자인-패턴/img_10.png)

![](/images/66-Java-디자인-패턴/img_11.png)

## Strategy Pattern (Strategy Pattern)

- Manage logic independently, declare classes containing behavior, and manage by connecting to interfaces
- Enables efficient change when adding or modifying new logic  
  ![](/images/66-Java-디자인-패턴/img.png)

### References

[Singleton Pattern Explanation](https://velog.io/@haero_kim/%ED%98%B9%EC%8B%9C-%EC%8B%B1%EA%B8%80%ED%86%A4%EC%9D%B4%EC%84%B8%EC%9A%94-%EC%A0%80%EB%8A%94-%EB%B2%99%EA%B8%80%ED%86%A4%EC%9D%B4%EC%97%90%EC%9A%94-%E3%85%8B%E3%85%8B%E3%85%8B)

[Observer Pattern Explanation](https://velog.io/@haero_kim/%EC%98%B5%EC%A0%80%EB%B2%84-%ED%8C%A8%ED%84%B4-%EA%B0%9C%EB%85%90-%EB%96%A0%EB%A8%B9%EC%97%AC%EB%93%9C%EB%A6%BD%EB%8B%88%EB%8B%A4)

<https://github.com/gyoogle/tech-interview-for-developer/blob/master/Design%20Pattern/Observer%20pattern.md>

<https://mygumi.tistory.com/343>

<https://www.geeksforgeeks.org/software-design-patterns/>

<https://coding-factory.tistory.com/708>
