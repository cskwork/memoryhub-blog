---
title: "클래스 설계의 5가지 원칙 - SOLID"
date: 2024-05-25T14:52:44+09:00
slug: "67-클래스-설계의-5가지-원칙-SOLID"
original_url: "https://memoryhub.tistory.com/67"
tistory_id: 67
draft: false
categories: ["데브 컨셉"]
tags: ["정보처리기사"]
---

## GPT 설명

SOLID 원칙은 **유지보수성, 유연성 및 확장성**을 촉진하는 객체 지향 프로그래밍 및 소프트웨어 개발의 5가지 설계 원칙입니다. 이러한 원칙은 로버트 C. 마틴(일명 밥 아저씨라고도 함)에 의해 소개되었으며 소프트웨어 개발 커뮤니티에서 널리 채택되고 있습니다. SOLID의 약어는 다음과 같습니다:

**단일 책임 원칙(SRP)  
개방형/폐쇄형 원칙(OCP)  
리스코프 대체 원칙(LSP)  
인터페이스 분리 원칙(ISP)  
의존성 반전 원칙(DIP)**

각 원칙을 자세히 살펴보겠습니다:

#### 단일 책임 원칙(SRP):

클래스가 변경해야 할 이유가 하나만 있어야 한다는 원칙으로, 클래스는 하나의 책임만 가져야 한다는 의미입니다. 이 원칙을 따르면 separation of concerns로 코드를 더 모듈화하고 이해, 유지 관리 및 수정하기 쉽게 만들 수 있습니다.

#### 개방형/폐쇄형 원칙(OCP):

소프트웨어 엔티티(클래스, 모듈, 함수 등)는 확장을 위해서는 개방적이어야 하지만 수정을 위해서는 폐쇄적이어야 합니다. 즉, 기존 코드베이스를 변경하지 않고도 새로운 기능을 추가할 수 있어야 합니다. 이는 추상화, 상속, 다형성을 사용하여 달성할 수 있습니다.

#### 리스코프 대체 원칙(LSP):

바바라 리스코프의 이름을 딴 이 원칙은 파생 클래스의 객체가 프로그램의 정확성에 영향을 주지 않으면서 기본 클래스의 객체를 대체할 수 있어야 한다는 것입니다. 즉, 파생 클래스는 기본 클래스의 계약(예: 동작 및 속성)을 준수하면서 기능을 확장하거나 수정할 수 있어야 합니다.  
LSP는 기존 클래스를 확장하여 새 클래스를 만들 때 원래 클래스가 사용되는 모든 곳에서 새 클래스가 올바르게 작동하도록 하는 것입니다.

이 원리를 이해하는 데 도움이 되도록 예를 들어보겠습니다:

"fly"라는 메서드가 있는 "Bird"라는 기본 클래스가 있다고 가정해 보겠습니다. "Bird" 클래스를 상속하는 "Penguin"이라는 파생 클래스를 만든다고 가정해 보겠습니다. 펭귄은 날 수 없으므로 빈 구현이나 예외를 사용하여 "fly" 메서드를 재정의하고 싶을 수 있습니다.

그러나 그렇게 하면 "Bird" 클래스를 사용하여 날기를 기대하는 코드가 "Penguin" 객체를 대신 사용할 때 제대로 작동하지 않으므로 LSP를 위반하게 됩니다. LSP를 준수하려면 클래스 계층 구조를 수정하거나(예: 날 수 있는 새를 위해 "FlyingBird"와 같은 새로운 기본 클래스를 도입하는 등) 다양한 새의 동작을 더 잘 수용하도록 디자인을 변경할 수 있습니다.

요약하면, 리스코프 대체 원칙은 개발자가 파생 클래스가 기본 클래스의 동작을 진정으로 확장하고 예기치 않은 결과 없이 상호 교환적으로 사용할 수 있는 클래스 계층 구조를 만들도록 권장합니다. 이는 보다 견고하고 유지 관리가 쉬운 코드로 이어집니다.

#### 인터페이스 분리 원칙(ISP):

클래스가 사용하지 않는 인터페이스를 구현하도록 강요해서는 안 된다는 점을 강조합니다. 대신 더 작고 집중적인 인터페이스를 여러 개 만드는 것이 좋습니다. 이렇게 하면 관심사가 더 깔끔하게 분리되어 시스템을 더 쉽게 이해하고, 유지 관리하고, 변경할 수 있습니다.

#### 종속성 반전 원칙(DIP):

DIP는 상위 레벨 모듈이 하위 레벨 모듈에 종속되어서는 안 되며, 둘 다 추상화에 종속되어서는 안 된다는 원칙입니다. 또한 추상화는 세부 사항에 의존해서는 안 되며, 세부 사항은 추상화에 의존해야 합니다. 이 원칙은 종속성 주입과 제어의 역전 사용을 장려하며, 이를 통해 보다 유연하고 테스트 가능하며 유지 관리가 용이한 소프트웨어를 만들 수 있습니다.

SOLID 원칙을 준수함으로써 개발자는 보다 견고하고 유지 관리가 용이하며 변화에 적응할 수 있는 소프트웨어를 만들 수 있습니다. 이 원칙은 모든 경우에 적용할 수 있는 솔루션은 아니지만 효율적이고 체계적인 방식으로 코드를 설계하고 구조화하는 데 유용한 지침을 제공합니다.

## SRP (Single Responsibility Principle)

- 한 클래스는 하나의 책임을 가져야 한다.

### SRP 적용 전

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

    // Product의 내용을 변경하는 책임
    public void update(Production production, int price) {
        //validate price
        validatePrice(price);

        //update price
        production.updatePrice(price);
    }
	// 가격의 유효성 검증을 하는 validatePrice()는 ProductionUpdateService 의 책임이라고 볼 수 있을까 ???
    private void validatePrice(int price) {
        if (price < 1000) {
            throw new IllegalArgumentException("최소가격은 1000원 이상입니다.");
        }
    }

}
```

가격의 유효성을 검증하는 작업은 실제 가격의 정보를 바꾸는 Production의 책임으로 보는게 더 맞지 않을까?

그럼 이를 토대로 유효성 검증이라는 책임을 Production로 옮겼다!!!

### SRP 적용 후

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
            throw new IllegalArgumentException(String.format("최소가격은 %d원 이상입니다.", MINIMUM_PRICE));
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

- 소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다.

### OCP 적용 전

```
public class Production {
    private String name;
    private int price;
    // N(일반) ,E(전자티켓) ,L(지역상품)...
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

// 확장성이 제한적이고 쉬운 변경이(인터페이스 부재) 가능한 validator
public class ProductionValidator {
    public void validateProduction(Production production) throws IllegalArgumentException {

        if (production.getOption().equals("N")) {
            if (production.getNameLength() < 3) {
                throw new IllegalArgumentException("일반 상품의 이름은 3글자보다 길어야 합니다.");
            }
        } else if (production.getOption().equals("E")) {
            if (production.getNameLength() < 10) {
                throw new IllegalArgumentException("전자티켓 상품의 이름은 10글자보다 길어야 합니다.");
            }
        } else if (production.getOption().equals("L")) {
            if (production.getNameLength() < 20) {
                throw new IllegalArgumentException("지역 상품의 이름은 20글자보다 길어야 합니다.");
            }
        }

    }
}
```

### OCP 원칙 적용 후

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
            throw new IllegalArgumentException("일반 상품의 이름은 3글자보다 길어야 합니다.");
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
            throw new IllegalArgumentException("전자티켓 상품의 이름은 10글자보다 길어야 합니다.");
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
            throw new IllegalArgumentException("지역 상품의 이름은 20글자보다 길어야 합니다.");
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

- 자식 클래스는 최소한 자신의 부모 클래스에서 가능한 행위는 수행할 수 있어야 한다.
- 상위 타입의 객체를 하위 타입의 객체로 치환해도 상위 타입을 사용하는 프로그램은 정상적으로 동작해야 한다

### Example code of Liscov Substitution Principle:

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

### LSP 적용 전

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

// 부모클래스에서 쓰는 행위 수행 불가. 
const rec2: Rectangle = new Square();
rec2.width = 3;
rec2.height = 4;

console.log(rec.area === 12); // false
```

자식 클래스 Square는 부모 클래스 Rectangle의 area() 기능을 제대로 하지 못하고 있음

### LSP 적용 후

```
// Shape 인터페이스는 넓이를 구할 수 있는 것(기하학 관점의 면)이라고 가정한다.
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

- 특정 클라이언트를 위한 여러 인터페이스가 범용 인터페이스 하나보다 낫다.

### ISP 적용 전

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

인쇄의 역할을 담당하는 print는 override되었지만 나머지 기능은 구현할 필요가 없기 때문에 UnsupportedOperationException 발생.  
이런 경우, 인터페이스만 알고 있는 클라이언트는 printer에서 copy기능이 구현되어 있는지 안되어있는지 모르기 때문에 예상치 못한 오류를 만날 수 있다.

### ISP 적용 후

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

// 구현한 객체
public class PrinterMachine implements PrinterDevice {
	@Override
 	public void print() {
    		System.out.println("print");
	}
}

		// 클라이언트가 사용할 경우
@DisplayName("하나의 기능만을 필요로 한다면 하나의 인터페이스만 구현하도록 하자")
@Test
void singleInterface() {
    PrinterDevice printer = new SmartMachine();
    printer.print();
}
```

## 5 DIP (Dependency Inversion Principle)

- 소프트웨어는 추상화에 의존해야지, 구체화에 의존하면 안된다.

### DIP 적용 전

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

### DIP 적용 후

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

### 출처

<https://bottom-to-top.tistory.com/27>  
<https://medium.com/humanscape-tech/solid-%EB%B2%95%EC%B9%99-%E4%B8%AD-lid-fb9b89e383ef>
