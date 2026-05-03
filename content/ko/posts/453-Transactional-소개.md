---
title: "@Transactional 소개"
date: 2025-02-23T23:12:06+09:00
slug: "453-Transactional-소개"
original_url: "https://memoryhub.tistory.com/453"
tistory_id: 453
draft: false
categories: ["데브 프레임워크"]
tags: ["Spring Boot"]
---

오늘은 Spring 프레임워크에서 **데이터 무결성과 일관성**을 보장하기 위해 자주 사용하는 **@Transactional** 애너테이션(Annotation)에 대해 알아보겠습니다! 데이터베이스 작업(INSERT, UPDATE, DELETE 등)이 일어나는 메서드에 트랜잭션을 적용함으로써 보다 안전한 데이터 처리를 할 수 있는데요. 함께 살펴보겠습니다.

---

## **1. @Transactional이란? ?**

**@Transactional**은 Spring에서 제공하는 **트랜잭션 관리**를 편리하게 활성화하기 위한 애너테이션입니다. 데이터베이스에 연결해 작업을 처리하는 과정에서 문제가 발생하면(예: 예외 발생) 해당 작업을 원상태로 되돌려(rollback) 애플리케이션의 무결성을 지켜줍니다.

- ? **개념 요약**  
  데이터베이스 작업은 트랜잭션 단위로 진행되며, **ACID(원자성, 일관성, 격리성, 지속성)** 같은 특성을 지켜야 합니다. @Transactional은 이러한 트랜잭션 관리를 간편하게 해주는 Spring의 기능입니다.
- ? **실생활 예시**  
  은행에서 계좌이체를 한다고 생각해봅시다. 돈이 A 계좌에서 빠져나가고 B 계좌로 들어와야 하는데, 중간에 오류가 발생해 A 계좌만 빠져나가고 B 계좌에 들어가지 않았다면 문제가 크겠죠? 트랜잭션을 통해 모든 작업을 하나의 묶음으로 처리하여 오류 시 전체 작업을 되돌릴 수 있습니다.
- ? **어떤 문제를 해결하는지?**  
  데이터 처리 시 **일부만 적용되어 데이터가 꼬이는 문제**를 예방합니다. 여러 단계를 거치는 작업에서 중간에 실패가 발생했을 때, 이미 처리된 데이터를 원복(rollback)할 수 있도록 해줍니다.

---

## **2. 어떻게 동작하나요? ?**

### 1) 기본 개념

Spring에서 @Transactional을 사용하려면, 기본적으로 **트랜잭션 매니저(PlatformTransactionManager)** 가 빈(Bean)으로 등록되어 있어야 합니다. 스프링 부트 환경이라면 일반적으로 **DataSourceTransactionManager**(관계형 DB)나 **JpaTransactionManager**(JPA/Hibernate) 등이 자동 설정됩니다.

```
@Service
public class MyService {

    @Autowired
    private MyRepository myRepository;

    @Transactional
    public void doBusinessLogic() {
        // 1. DB에서 데이터 조회
        // 2. 데이터 변경
        // 3. 변경된 데이터 저장
        myRepository.save(...);
    }
}
```

@Transactional이 선언된 `doBusinessLogic()` 메서드가 실행되면, Spring은 메서드 실행 전후로 트랜잭션을 시작/종료합니다.

- 메서드가 정상 종료되면 **commit**을 수행해 작업 내용을 DB에 반영합니다.
- 메서드 내부에서 예외가 발생해 롤백 설정이 적용되면 DB 작업을 **rollback**하여 원상태로 복구합니다.

### 2) 실제 적용 예시

```
@Service
public class OrderService {

    @Autowired
    private OrderRepository orderRepository;

    @Autowired
    private PaymentService paymentService;

    @Transactional
    public void processOrder(OrderRequest request) {
        // 1. 주문 정보 DB 저장
        Order order = new Order(request.getItemId(), request.getAmount());
        orderRepository.save(order);

        // 2. 결제 처리
        paymentService.pay(order.getId(), request.getAmount());

        // 만약 paymentService.pay() 내부에서 예외 발생 시 전체 롤백
        // 즉, orderRepository.save()로 저장한 Order 데이터도 롤백됩니다.
    }
}
```

#### ? 동작 원리

1. **트랜잭션 시작**: `processOrder()` 메서드를 호출하면, Spring이 자동으로 트랜잭션을 시작합니다.
2. **DB 작업 수행**: 주문 정보를 저장하고 결제를 시도합니다.
3. **정상 처리 시 커밋**: 모든 로직이 문제없이 처리되면 트랜잭션이 커밋됩니다.
4. **예외 발생 시 롤백**: 결제 로직에서 예외가 던져지면, Spring은 트랜잭션을 롤백합니다.

---

## **3. 주요 장점 ?**

1. **편의성**  
   트랜잭션 관리 로직을 직접 짜지 않아도, 애너테이션만 붙이면 간단히 적용할 수 있습니다.
2. **명시적이고 직관적인 구조**  
   메서드 단위로 트랜잭션을 선언적으로 적용하므로, 어떤 로직이 트랜잭션으로 묶여 있는지 쉽게 파악할 수 있습니다.
3. **에러 시 손쉬운 복구**  
   예외가 발생하면 Spring이 자동으로 롤백해주어 데이터 무결성을 보장합니다.

---

## **4. 주의할 점 ⚠️**

1. **프록시(Proxy) 기반 동작**  
   Spring AOP(프록시) 기반으로 동작하기 때문에, **同 클래스 내의 메서드 호출**은 트랜잭션이 적용되지 않을 수 있습니다. 예: `this.someInnerMethod()`. 트랜잭션이 적용되려면 **외부에서 해당 메서드를 호출**해야 합니다.
2. **체크 예외 vs 언체크 예외**  
   기본적으로 언체크 예외(RuntimeException, Error 등)가 발생하면 롤백되고, 체크 예외(Exception)는 롤백되지 않습니다. 체크 예외 역시 롤백하려면 `@Transactional(rollbackFor = Exception.class)`와 같이 지정해야 합니다.
3. **읽기 전용 트랜잭션**  
   `@Transactional(readOnly = true)`로 설정하면 JPA 캐시 최적화 등의 이점이 있지만, 실제로 데이터를 수정하면 예외가 발생하거나 일부 구현체에서 제대로 동작하지 않을 수 있으므로 주의해야 합니다.
4. **대량의 DB 작업 시 주의**  
   트랜잭션 범위가 길수록(대용량 처리) 잠금이 오래 걸리거나 성능 문제가 발생할 수 있습니다. 필요한 경우 Batch 처리나 트랜잭션 범위를 세분화해야 합니다.
5. **단순 조회에 불필요한 @Transactional 사용 자제**  
   단순 조회 쿼리(변경이 일어나지 않는)에서는 굳이 @Transactional로 감쌀 필요가 없는 경우가 많습니다. 트랜잭션이 생기면 DB 자원 등을 더 소비하므로 꼭 필요한 곳에만 적용하는 것이 좋습니다.

---

## **5. 실제 사용 예시 ?**

### (1) 여러 메서드로 구성된 서비스 로직에서의 사용

```
@Service
public class CartService {

    @Autowired
    private CartRepository cartRepository;

    @Autowired
    private ItemService itemService;

    @Transactional
    public void addToCart(Long userId, Long itemId) {
        // 1. 아이템 재고 확인
        itemService.checkStock(itemId);

        // 2. 장바구니에 상품 추가
        Cart cart = cartRepository.findByUserId(userId);
        cart.addItem(itemId);
        cartRepository.save(cart);

        // 중간에 예외 발생 시 롤백!
    }
}
```

### (2) 부분 롤백을 적용해야 할 때

한 서비스 메서드 내에서 특정 작업만 롤백을 적용하고 싶은 경우, 구조를 분리하거나 별도의 전용 트랜잭션 설정을 해야 합니다.

```
@Service
public class MixedOperationService {

    @Transactional
    public void processOperations() {
        // A: 꼭 롤백해야 하는 작업
        doCriticalOperation();

        // B: 롤백과 무관한 작업
        doNonCriticalOperation();
    }

    @Transactional(rollbackFor = Exception.class)
    public void doCriticalOperation() {
        // 심각한 작업
    }

    public void doNonCriticalOperation() {
        // 단순한 작업 (별도의 트랜잭션 불필요)
    }
}
```

---

## **6. 마치며 ?**

트랜잭션은 데이터 무결성과 일관성을 유지하기 위해 필수적인 개념입니다. **@Transactional**을 통해 **개발자는 비즈니스 로직에만 집중**하고, 트랜잭션 관리는 Spring에 맡길 수 있어 큰 이점을 얻을 수 있습니다. 하지만 **장바구니, 결제** 등 중요한 로직에 트랜잭션을 적용할 때는 **데이터 잠금 시간**, **롤백 전략** 등을 잘 고려해야 합니다.

이 기술을 잘 활용하면 **데이터 손실이나 무결성 깨짐 같은 문제**를 간편히 예방할 수 있고, 더 나은 코드 구조로 확장할 수 있습니다. 꼭 필요한 곳에만 적절히 @Transactional을 사용해 안전하고 효율적인 애플리케이션을 만들어보세요!

---

### 참고 자료 및 출처

- Spring 공식 문서: [Transaction Management](https://docs.spring.io/spring-framework/docs/current/reference/html/data-access.html#transaction)
- Spring Boot 공식 문서: [Spring Boot Transaction Support](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#boot-features-transaction)
