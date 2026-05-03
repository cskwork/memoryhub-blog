---
title: "IoC와 DI의 차이점 알아보기"
date: 2025-02-23T22:58:49+09:00
slug: "451-IoC와-DI의-차이점-알아보기"
original_url: "https://memoryhub.tistory.com/451"
tistory_id: 451
draft: false
categories: ["데브 프레임워크"]
tags: ["Spring"]
---

오늘은 스프링(Spring) 프레임워크의 핵심 개념 중 하나인 **IoC(Inversion of Control)**와 **DI(Dependency Injection)**에 대해 알아보겠습니다. 이 두 개념은 스프링을 제대로 이해하기 위해 반드시 짚고 넘어가야 할 아주 중요한 토픽입니다.

---

## **1. IoC와 DI란? ?**

### 1) IoC(Inversion of Control)란?

- **IoC**는 '제어의 역전'이라는 뜻으로, **객체의 제어 권한을 개발자가 아닌 외부(프레임워크 또는 컨테이너)가 담당**하도록 하는 개념을 말합니다.
- 전통적으로는 객체를 사용하는 쪽에서 직접 인스턴스를 생성하고, 의존성을 관리해왔습니다. 하지만 IoC를 적용하면, **객체 생성과 의존성 관리의 제어권을 스프링 컨테이너**가 담당하게 됩니다.
- 예를 들어, **스프링 컨테이너**가 객체를 ‘필요한 시점’에 알아서 만들어서 주입하고, 객체 간의 의존관계도 대신 설정해주는 방식을 생각해볼 수 있습니다.

### 2) DI(Dependency Injection)란?

- **DI**는 '의존성 주입'이라는 뜻으로, **IoC 개념을 구체적으로 구현하는 디자인 패턴**입니다.
- 말 그대로 객체가 필요로 하는 **의존 객체를 외부에서 주입**해주는 방식으로, 스프링에서는 `@Autowired`, `@Inject`, `@Resource` 등의 어노테이션이나 XML 설정을 통해 이 작업을 손쉽게 할 수 있습니다.
- IoC가 “제어 역전”이라는 넓은 개념이라면, DI는 그 중에서도 **‘필요한 객체를 외부에서 주입한다’**는 구체적인 구현 방법이라고 볼 수 있습니다.

> **정리**:
>
> - **IoC**: 제어권을 프레임워크(스프링)에게 넘기는 큰 그림
> - **DI**: 스프링이 객체에게 의존성을 주입해주는 구체적 방법

---

## **2. 어떻게 동작하나요? ?**

### 1) 기본 개념

IoC와 DI를 이해하려면, **"어떤 객체가 다른 객체를 직접 생성하는 대신, 그 객체를 스프링이 대신 만들어준다"** 라고 생각하시면 됩니다.

스프링 애플리케이션이 시작될 때, 스프링 컨테이너는 설정파일(예: `@Configuration` 클래스, `applicationContext.xml` 등)을 참고하여 **빈(Bean)**을 생성하고, 빈들이 서로 의존하는 부분이 있다면 적절히 연결(주입)해줍니다. 이 과정을 자동으로 처리함으로써 개발자는 객체 생성을 직접 신경 쓸 필요가 거의 없어집니다.

### 2) 실제 적용 예시

## ? 의존성 주입(DI) 적용 전후 코드 비교

스프링에서 가장 핵심이 되는 개념 중 하나가 **DI(Dependency Injection)**입니다. 이번에는 **"의존성 주입이 적용된 코드"**와 **"적용되지 않은 코드"**를 간단한 예제로 비교해보겠습니다.

---

## 1. 의존성 주입이 없는 코드 (직접 인스턴스 생성)

```
public class OrderService {
    // 직접 PaymentService 인스턴스를 생성
    private PaymentService paymentService = new PaymentService();

    public void placeOrder(String productId) {
        paymentService.pay(productId);
    }
}

public class PaymentService {
    public void pay(String productId) {
        System.out.println("결제 완료: " + productId);
    }
}
```

### 특징

1. `OrderService` 내부에서 `PaymentService` 객체를 직접 `new`로 생성합니다.
2. `PaymentService`가 바뀔 경우(`PaymentService`의 다른 구현체로 교체 등) `OrderService` 코드도 수정해야 합니다.
3. **결합도**가 상대적으로 높고, **테스트**를 하려면 실제 `PaymentService`를 반드시 생성해야만 합니다.

---

## 2. 의존성 주입(DI) 적용 코드

### 2-1) **일반 자바 방식** (스프링 프레임워크 사용 X)

```
public class OrderService {
    private final PaymentService paymentService;

    // 생성자를 통해 PaymentService를 주입받음
    public OrderService(PaymentService paymentService) {
        this.paymentService = paymentService;
    }

    public void placeOrder(String productId) {
        paymentService.pay(productId);
    }
}

public class PaymentService {
    public void pay(String productId) {
        System.out.println("결제 완료: " + productId);
    }
}

// main 등 호출부
public class Main {
    public static void main(String[] args) {
        PaymentService paymentService = new PaymentService(); // 필요 객체 생성
        OrderService orderService = new OrderService(paymentService); // 주입
        orderService.placeOrder("상품ID-123");
    }
}
```

#### 특징

1. `OrderService`는 `PaymentService`를 어떻게 생성하는지 모릅니다. **필요한 의존 객체**를 **외부**에서 받아서 사용합니다.
2. `PaymentService`를 **새로운 클래스**(예: `TestPaymentService`)로 교체해야 할 때, `OrderService`를 수정하지 않고도 가능(주입부만 수정).
3. **결합도**가 낮고, **유연**하며, Mock 객체 등을 쉽게 넣어 **테스트**가 편리해집니다.

---

### 2-2) **스프링 기반 DI 예시**

```
@Service
public class OrderService {
    private final PaymentService paymentService;

    // 생성자 주입
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
        System.out.println("결제 완료: " + productId);
    }
}

// 스프링 부트 메인 예시
@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

- 스프링 부트가 실행되면서, `@Service`가 붙은 클래스들을 스캔해 **빈(Bean)**으로 등록합니다.
- `OrderService`의 생성자 파라미터에 `PaymentService` 타입이 필요한 것을 인지하고, **자동으로 `PaymentService` 빈**을 만들어 주입(Injection)해줍니다.
- 개발자는 “`OrderService`가 어떤 `PaymentService`를 쓰는지”를 직접 `new`로 만드는 대신, **스프링 컨테이너**에 맡기기만 하면 됩니다.

---

### 3. 두 코드의 차이점 정리

| 구분 | 직접 인스턴스 생성 | 의존성 주입(DI) |
| --- | --- | --- |
| **객체 생성 주체** | 클래스 자신이 `new`로 직접 생성 | 스프링 컨테이너(또는 외부)에서 생성 & 주입 |
| **결합도** | 높음: 내부에서 생성 로직 고정 | 낮음: 외부 주입, 교체 유연 |
| **유지보수성** | 변화에 따라 작성 클래스 수정 필수 | 주입부만 수정하면 되므로 유연성 높음 |
| **테스트 용이성** | Mock 객체를 주입하기 어려움 | Mock 객체 등을 쉽게 교체 가능 |
| **확장성** | 다른 구현체로 바꾸려면 코드 변경 많음 | 의존 객체만 교체하면 되므로 확장성 우수 |

---

- **DI 전**: “`OrderService`가 `PaymentService`를 직접 `new`로 생성해 사용.”
- **DI 후**: “`OrderService`가 `PaymentService`를 외부에서 ‘주입(Injection)’받아 사용.”

결과적으로 **DI**가 적용되면, 코드의 **유연성**이 올라가고 **테스트** 및 **유지보수**가 훨씬 쉬워집니다.  
스프링 프레임워크를 활용하면, **스프링 컨테이너(IoC)**가 객체 생성과 의존성 주입을 대신 관리해주기 때문에 “개발자가 직접 신경 쓸 부분”이 줄어듭니다.

**요점**:

- “의존성 주입이 없는 코드”는 필요한 객체를 **직접** 생성 -> **결합도**가 높음
- “의존성 주입이 적용된 코드”는 필요한 객체를 **외부**에서 받음 -> **결합도**가 낮고 유지보수성↑

---

## **3. 주요 장점 ?**

1. **객체 간 결합도 감소**

   - 새로운 객체가 필요하면 스프링 컨테이너가 알아서 연결해주므로, 코드 상에서 직접 구현체를 생성하지 않아도 됩니다. 이를 통해 **유연한 구조**와 **높은 확장성**을 확보할 수 있습니다.
2. **테스트 용이성**

   - Mock 객체를 사용하거나 다른 구현체로 쉽게 대체하여 테스트할 수 있기 때문에 **단위 테스트**와 **통합 테스트**를 간편하게 수행할 수 있습니다.
3. **유지보수성 향상**

   - 객체 생성 로직이 코드에서 분리되어 설정 파일(혹은 어노테이션)로 관리되므로, **변경이 발생해도 주요 비즈니스 로직에 미치는 영향이 적습니다.**

---

## **4. 주의할 점 ⚠️**

1. **복잡한 설정 관리**

   - 지나치게 많은 빈 구성이나 복잡한 의존 관계는 초기 셋업이 복잡할 수 있습니다. 설정 파일이나 어노테이션만으로 쉽게 파악이 안 될 정도로 복잡해지는 것은 피해야 합니다.
2. **순환 의존성(Circular dependency)**

   - A 객체가 B를 필요로 하고 B 객체가 다시 A를 필요로 하는 경우처럼, **서로가 서로를 주입**해야 하는 상황이 발생하면 의존성 주입이 실패하게 됩니다. 구조 설계 시 꼭 주의가 필요합니다.
3. **과도한 추상화**

   - DI는 무분별하게 추상화 레이어를 늘리는 것과는 다릅니다. **'유연성'과 '단순성' 사이의 균형**을 맞춰야 합니다.

---

## **5. 실제 사용 예시 ?**

### 예시: `@Configuration`과 `@Bean`을 사용하는 방법

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
    orderService.placeOrder("프로덕트ID-123");
}
```

- `AppConfig` 클래스에서 `@Bean` 메서드를 통해 **직접 의존 객체를 생성**(이 부분을 컨테이너에 맡기는 방식).
- `AnnotationConfigApplicationContext`가 이 `AppConfig`를 보고 `Bean`들을 만들고 관계를 연결해줍니다.
- 이런 식으로 **객체 생성(Bean 등록)과 의존 관계 주입**이 분리되어, 비즈니스 로직과 설정 로직이 깔끔하게 분리됩니다.

---

## **6. 마치며 ?**

스프링에서의 **IoC**와 **DI**는 “사용하는 쪽에서 직접 객체를 만들지 않고, 프레임워크가 알아서 만들어주는 구조”라고 이해하면 쉽습니다. 그중에서도 DI(Dependency Injection)는 의존성 주입을 통해 IoC 개념을 **구체적으로 실천**하는 방법입니다.

이러한 개념들을 올바르게 활용하면, **코드의 결합도를 낮추고**, **테스트와 유지보수를 훨씬 수월하게** 만들 수 있습니다. 스프링 애플리케이션 구조가 점점 복잡해질수록 IoC/DI의 필요성을 절실히 느끼게 될 것입니다.

**정리**:

- **IoC**는 큰 틀에서 **객체 생성 제어권**을 개발자가 아닌 **스프링 컨테이너**에 넘기는 것
- **DI**는 이를 구현하는 대표적인 방안으로, **객체 간 의존 관계를 외부에서 주입**받는 형태

**따라서** IoC와 DI를 잘 이해하면 스프링만의 장점을 극대화하여 더 견고하고 유지보수하기 쉬운 애플리케이션을 만들 수 있습니다!

---

### 참고 자료 및 출처

- [Spring 공식 문서](https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#beans-introduction)
- [토비의 스프링](https://book.naver.com/bookdb/book_detail.nhn?bid=7006516) (스프링 프레임워크 심층 분석서)
