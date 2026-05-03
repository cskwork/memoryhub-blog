---
title: "코드 스멜: Change Preventers 코드 변경을 방해하는 요소들 ?"
date: 2025-03-22T22:30:31+09:00
slug: "509-코드-스멜-Change-Preventers-코드-변경을-방해하는-요소들"
original_url: "https://memoryhub.tistory.com/509"
tistory_id: 509
draft: false
categories: ["데브 컨셉"]
tags: ["Clean Code"]
---

코드를 수정하려고 했는데 한 군데만 바꾸면 될 줄 알았던 것이 여러 곳을 동시에 수정해야 하는 상황을 경험해 보셨나요? 혹은 하나의 클래스가 너무 많은 일을 담당해서 간단한 변경 하나를 위해 전체 클래스를 이해해야만 했던 경험이 있으신가요?

이러한 문제는 코드 스멜(Code Smell) 중에서도 특히 '변경 방해 요소(Change Preventers)'라고 불리는 현상과 관련이 있습니다. 마치 집 안의 물건이 제자리에 정리되어 있지 않아서 간단한 수리 작업조차 어려워지는 것과 같은 상황이죠!

- 음식점 메뉴판을 생각해보세요. 메뉴 가격을 변경할 때마다 전체 메뉴판을 새로 인쇄해야 한다면 얼마나 번거로울까요?
- 이와 마찬가지로 잘못 설계된 코드는 작은 변경에도 큰 비용이 발생합니다.

## 왜 필요한가?

Change Preventers가 해결하는 문제들은 다음과 같습니다:

1. **유지보수성 저하**: 코드 변경이 어려워지면 유지보수 비용이 증가하고 개발 속도가 느려집니다.
2. **버그 발생 위험**: 여러 곳을 동시에 수정해야 할 때 일부 위치를 놓치면 버그가 발생합니다.
3. **개발자 사기 저하**: 간단한 기능 추가나 버그 수정도 복잡한 작업이 되어 개발자의 사기를 떨어뜨립니다.

## 기본 원리

Change Preventers의 세 가지 유형과 해결 방법을 알아볼까요?

### 1. Divergent Change (발산적 변경) ?

**정의**: 하나의 클래스가 서로 다른 여러 이유로 자주 변경되어야 하는 경우입니다.

**비유**: 하나의 주방 도구로 모든 요리 작업을 하려는 것과 같습니다. 칼 하나로 야채 자르기, 고기 손질, 생선 손질, 빵 자르기 등을 모두 하려면 효율이 떨어지죠. 각 용도에 맞는 도구가 필요합니다.

**문제 코드**:

```
public class User {
    private String name;
    private String email;

    // 사용자 정보 관련 메서드
    public void changeName(String newName) { this.name = newName; }

    // 데이터베이스 관련 메서드
    public void saveToDatabase() { /* DB 저장 로직 */ }

    // 보고서 생성 관련 메서드
    public String generateUserReport() { /* 보고서 생성 로직 */ }
}
```

**해결 방법**: 클래스 추출(Extract Class)을 통해 각 책임을 별도의 클래스로 분리

**개선된 코드**:

```
public class User {
    private String name;
    private String email;

    public void changeName(String newName) { this.name = newName; }
}

public class UserRepository {
    public void save(User user) { /* DB 저장 로직 */ }
}

public class UserReportGenerator {
    public String generateReport(User user) { /* 보고서 생성 로직 */ }
}
```

### 2. Shotgun Surgery (산탄총 수술) ?

**정의**: 하나의 변경을 위해 여러 클래스를 동시에 수정해야 하는 경우입니다.

**비유**: 하나의 레시피를 변경하기 위해 요리책 전체를 뒤적여야 하는 상황입니다. '버터' 대신 '마가린'을 사용하려면 모든 레시피를 찾아 수정해야 합니다.

**문제 코드**:

```
public class Customer {
    public void sendEmail(String message) {
        // 이메일 전송 로직 (로깅 포함)
        System.out.println("Sending email: " + message);
        System.out.println("Email sent at: " + new Date());
    }
}

public class Order {
    public void notifyShipped() {
        // 유사한 이메일 전송 로직 (로깅 포함)
        System.out.println("Sending shipping notification");
        System.out.println("Email sent at: " + new Date());
    }
}
```

**해결 방법**: 메서드 이동(Move Method)과 클래스 추출(Extract Class)을 통해 공통 기능을 한 곳으로 통합

**개선된 코드**:

```
public class EmailService {
    public void sendEmail(String email, String message) {
        // 중앙화된 이메일 전송 로직 (로깅 포함)
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

### 3. Parallel Inheritance Hierarchies (병렬 상속 계층) ?️

**정의**: 한 클래스의 서브클래스를 만들 때마다 다른 클래스의 서브클래스도 생성해야 하는 경우입니다.

**비유**: 건물과 유지보수 매뉴얼의 관계입니다. 새로운 유형의 건물이 생길 때마다 그에 맞는 유지보수 매뉴얼을 별도로 만들어야 하는 상황입니다.

**문제 코드**:

```
// Shape 계층
public abstract class Shape {
    public abstract double area();
}

public class Circle extends Shape {
    private double radius;
    @Override
    public double area() { return Math.PI * radius * radius; }
}

// ShapeRenderer 계층 (Shape 계층과 병렬 구조)
public abstract class ShapeRenderer {
    public abstract void render();
}

public class CircleRenderer extends ShapeRenderer {
    private Circle circle;
    @Override
    public void render() { /* 원 렌더링 로직 */ }
}
```

**해결 방법**: 두 계층을 합치거나, 상속 대신 합성(Composition)을 사용

**개선된 코드**:

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

## 실제 예제

실제 비즈니스 환경에서는 이런 코드 스멜이 어떻게 나타날까요? 예를 들어, 전자상거래 시스템을 생각해봅시다.

### Divergent Change 실제 사례

주문 처리 클래스가 주문 생성, 결제 처리, 배송 처리, 알림 발송 등 모든 기능을 담당하게 되면:

1. 결제 방식이 추가될 때마다 클래스를 수정해야 함
2. 새로운 배송 방법 추가시에도 수정 필요
3. 알림 채널이 추가될 때도 수정 필요

이를 각 책임별로 분리하면:

```
public class OrderService { /* 주문 생성 및 관리 */ }
public class PaymentService { /* 결제 처리 */ }
public class ShippingService { /* 배송 처리 */ }
public class NotificationService { /* 알림 발송 */ }
```

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **과도한 분리**: 너무 작은 단위로 클래스를 분리하면 오히려 복잡도가 증가할 수 있습니다.
   - 관련성 있는 기능은 함께 유지하되, 서로 다른 이유로 변경되는 요소만 분리하세요.
   - 항상 SOLID 원칙을 고려하세요.
2. **지나친 추상화**: 변경을 예상하고 너무 많은 추상화를 도입하면 코드가 불필요하게 복잡해집니다.
   - YAGNI(You Aren't Gonna Need It) 원칙을 기억하세요.

? **꿀팁**

- 변경이 자주 발생하는 부분을 식별하고 먼저 리팩토링하세요.
- 코드 리뷰 시 변경의 범위가 넓다면 이런 코드 스멜이 있는지 검토하세요.
- 테스트 코드를 먼저 작성하고 리팩토링하면 안전하게 변경할 수 있습니다.

## 마치며

지금까지 코드 변경을 방해하는 요소들(Change Preventers)에 대해 알아보았습니다. 좋은 코드는 변경이 필요할 때 해당 부분만 수정하면 되는 코드입니다. 단일 책임 원칙(SRP)을 지키고, 관련된 기능끼리 응집도를 높이며, 불필요한 의존성을 제거하면 코드 변경이 훨씬 쉬워집니다.

혹시 여러분의 코드에서도 이런 패턴이 발견되나요? 어떤 방식으로 해결하셨는지 댓글로 공유해주세요!

## 참고 자료 ?

- [리팩토링: 코드 품질을 개선하는 기술 (마틴 파울러)](https://product.kyobobook.co.kr/detail/S000001810241)
- [Refactoring.Guru - Change Preventers](https://refactoring.guru/refactoring/smells/change-preventers)
- [코드 스멜과 리팩토링 기법](https://luzkan.github.io/smells/divergent-change/)

---

#코드스멜 #리팩토링 #클린코드 #소프트웨어설계
