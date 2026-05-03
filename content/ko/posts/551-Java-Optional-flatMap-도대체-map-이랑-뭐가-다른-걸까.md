---
title: "? Java Optional.flatMap(), 도대체 map()이랑 뭐가 다른 걸까?"
date: 2025-04-14T13:47:49+09:00
slug: "551-Java-Optional-flatMap-도대체-map-이랑-뭐가-다른-걸까"
original_url: "https://memoryhub.tistory.com/551"
tistory_id: 551
draft: false
---

```
+-----------------------+      +---------------+
| +-------------------+ |      |               |
| | Optional  | | ---> | Optional |
| +-------------------+ |      |               |
+-----------------------+      +---------------+
  Optional>  flatMap   Optional
```

`if (user != null)`로 시작해서 `if (user.getAddress() != null)`... 이렇게 `null` 체크가 꼬리에 꼬리를 물었던 경험, 다들 한 번쯤 있으시죠? Java 8에서 `Optional`이 등장하며 이런 "Null 지옥"에서 벗어날 길이 열렸습니다. 그런데 `Optional`을 쓰다 보면 `map()`과 `flatMap()`이라는 두 가지 메서드를 만나게 됩니다. 둘 다 값을 변환하는 것 같은데, 왜 이름이 다르고 언제 뭘 써야 할지 헷갈릴 때가 많습니다.

이 글을 끝까지 읽으시면 `map()`과 `flatMap()`의 결정적인 차이를 명확히 이해하고, 중첩된 `Optional`을 우아하게 처리하는 방법을 알게 되실 겁니다.

⚡ **TL;DR**

- **`map()`**: 변환 함수가 반환한 결과를 `Optional`로 **한 번 더 감쌉니다.** (`T -> Optional`)
- **`flatMap()`**: 변환 함수가 반환한 `Optional`을 **그대로 반환하여 평탄화**합니다. (`Optional -> Optional`)

---

### 목차

1. 배경: `Optional`은 왜 등장했을까?
2. 핵심 개념 정리: `map` vs `flatMap`
3. 실습: 중첩된 `Optional` 다루기
4. 모범 사례: 언제 `flatMap`을 써야 할까?
5. 마치며 & 참고자료

---

### 1. 배경: `Optional`은 왜 등장했을까?

`Optional`은 `null`일 수도 있는 객체를 감싸는 래퍼 클래스입니다[5]. `Optional`을 사용하면 개발자가 해당 변수가 `null`일 수 있다는 사실을 명시적으로 알리고, `null` 처리 로직을 강제하여 `NullPointerException`(NPE)을 예방할 수 있습니다.

- ✅ **`Optional`**: `null`일 수도 있는 `T` 타입의 객체를 감싸, `null` 처리를 명시적으로 다루게 하는 컨테이너 객체[5].
- ✅ **`map()`**: `Optional`에 담긴 값이 존재할 경우, 주어진 함수를 적용하고 그 결과를 `Optional`로 감싸서 반환[1].
- ✅ **`flatMap()`**: `map()`과 유사하지만, 주어진 함수의 결과가 이미 `Optional`일 때 그 결과를 그대로 반환하여 중첩을 막음[1].

### 2. 핵심 개념 정리: `map` vs `flatMap`

> **`flatMap`은 `map`과 달리, 변환 함수의 반환 타입이 이미 `Optional`일 때 이중으로 감싸지 않고 결과를 평탄화(flatten)합니다.**[1][9]

두 메서드의 가장 큰 차이점은 **매핑 함수(mapper)의 반환 타입**에 있습니다[2].

```
// map의 매핑 함수는 T 타입을 받아 U 타입을 반환
public Optional map(Function mapper);

// flatMap의 매핑 함수는 T 타입을 받아 Optional 타입을 반환
public Optional flatMap(Function> mapper);
```

`map()`은 매핑 함수가 반환한 값(`U`)을 무조건 `Optional`로 감싸서 `Optional`를 만듭니다[6]. 반면 `flatMap()`은 매핑 함수가 처음부터 `Optional`를 반환하므로, 추가적인 포장 없이 그대로 `Optional`를 반환합니다[2][6].

이 차이 때문에, 매핑 함수의 결과가 이미 `Optional`인 경우 `map()`을 쓰면 원치 않는 중첩 `Optional`이 생겨납니다.

```
// 1. map() 사용 시: 결과가 Optional>이 됨
Optional> nestedOptional = Optional
    .of("string")
    .map(s -> Optional.of("STRING")); // "STRING"을 감싼 Optional을 반환

// 2. flatMap() 사용 시: 결과가 Optional으로 평탄화됨
Optional flatOptional = Optional
    .of("string")
    .flatMap(s -> Optional.of("STRING")); // "STRING"을 감싼 Optional을 반환
```

### 3. 실습: 중첩된 `Optional` 다루기

`Product` → `Person` → `Job`으로 이어지는 객체 참조 구조에서 직업 이름을 가져오는 상황을 가정해봅시다. 각 참조는 `Optional`로 감싸져 있습니다[3].

#### ① DTO 준비

```
class Product {
    private Optional person;
    public Optional getPerson() { return person; }
    // ...
}

class Person {
    private Optional job;
    public Optional getJob() { return job; }
    // ...
}

class Job {
    private String jobName;
    public String getJobName() { return jobName; }
    // ...
}
```

#### ② `map()`으로 인한 문제 상황

만약 `map()`만 사용해서 직업 이름을 가져오려고 하면 어떻게 될까요?

```
Optional optProduct = /* ... product 객체 초기화 ... */;

// 컴파일 에러 발생!
Optional jobName = optProduct
    .map(Product::getPerson) // 반환 타입: Optional>
    .map(Person::getJob)     // 에러! Optional에 getJob()을 호출해야 함
    .map(Job::getJobName);
```

첫 번째 `map(Product::getPerson)` 호출에서 문제가 발생합니다. `Product::getPerson` 메서드는 `Optional`을 반환하는데, `map`은 이 결과를 다시 `Optional`로 감싸 `Optional>` 타입을 만들어버립니다[3][5]. 이중으로 감싸진 `Optional`에는 `Person`의 `getJob` 메서드가 존재하지 않으므로 다음 체인에서 컴파일 에러가 발생합니다.

#### ③ `flatMap()`으로 해결

이럴 때 `flatMap`이 등장합니다. `flatMap`은 `Optional`을 반환하는 함수를 위해 존재하며, 결과를 평탄하게 만들어 체인을 이어나갈 수 있게 해줍니다[1][9].

```
Optional optProduct = /* ... product 객체 초기화 ... */;

// flatMap으로 중첩 구조를 해결
Optional jobName = optProduct
    .flatMap(Product::getPerson) // 반환 타입: Optional
    .flatMap(Person::getJob)     // 반환 타입: Optional
    .map(Job::getJobName);      // 반환 타입: Optional

System.out.println(jobName.orElse("직업 정보 없음"));
```

- `optProduct.flatMap(Product::getPerson)`: `getPerson`이 `Optional`을 반환하므로, `flatMap`이 이를 그대로 받아 `Optional`을 반환합니다.
- `.flatMap(Person::getJob)`: 마찬가지로 `getJob`의 반환 타입인 `Optional`을 그대로 반환합니다.
- `.map(Job::getJobName)`: 마지막으로 `getJobName`은 `String`을 반환합니다. 이 `String` 값을 최종적으로 `Optional`로 감싸야 하므로 여기서는 `map`을 사용하는 것이 자연스럽습니다[3][6]

### 4. 모범 사례: 언제 `flatMap`을 써야 할까?

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **연속된 `map()`** | 변환 함수가 `Optional`을 반환하지 않는 단순 값 변환에 적합하며 코드가 간결합니다[6]. | 변환 함수가 `Optional`을 반환하면 `Optional>` 구조가 되어 복잡해집니다[5]. |
| **`flatMap()` 사용** | `Optional`을 반환하는 함수를 체이닝할 때 중첩을 막아 코드를 깔끔하게 유지합니다. 도메인 객체 탐색에 필수적입니다[2][9]. | 변환 함수가 `Optional`이 아닌 일반 값을 반환하는 경우 `flatMap`을 사용하면 컴파일 에러가 발생합니다. |
| **`map()`과 `flatMap()` 혼용** | `Optional`을 반환하는 중간 단계는 `flatMap`으로, 마지막에 일반 값을 반환하는 단계는 `map`으로 처리하는 등 유연한 조합이 가능합니다[3]. | 각 메서드의 반환 타입을 명확히 이해하고 사용해야 혼란을 막을 수 있습니다. |

### 5. 마치며

오늘은 Java `Optional`의 `map`과 `flatMap`에 대해 깊이 알아봤습니다.

1. `Optional`은 `null`을 안전하고 명시적으로 다루기 위한 강력한 도구입니다.
2. `map`은 변환 결과를 항상 `Optional`로 감싸고, `flatMap`은 반환값이 이미 `Optional`일 때 이를 평탄화합니다.
3. 객체 그래프를 탐색하는 것처럼 `Optional`을 반환하는 메서드를 연달아 호출할 때는 `flatMap`을 사용하여 코드를 간결하고 우아하게 만드세요[9].

실제 프로젝트에서 `null` 체크 로직을 `Optional`과 `flatMap`으로 리팩토링해보세요. `if`문 지옥에서 벗어나 훨씬 더 선언적이고 읽기 좋은 코드를 작성할 수 있을 겁니다.

이 글이 도움이 되셨다면 ❤️(하트)와 댓글 부탁드립니다!

---

#### 참고자료

- [Baeldung: The Difference Between `map()` and `flatMap()` in Java Optional](https://www.baeldung.com/java-difference-map-and-flatmap)
- [Ryan-Blog: [Java] Optional map flatMap 차이점](https://ryanwoo.tistory.com/48)
- [bada-log: Optional 의 Map, flatMap 사용하기](https://devfunny.tistory.com/468)

[1] <https://dev-gallery.tistory.com/25>  
[2] <https://ryanwoo.tistory.com/48>  
[3] <https://devfunny.tistory.com/468>  
[4] <https://blog.naver.com/fbfbf1/223090482441>  
[5] <https://github.com/ckddn9496/modern-java-in-action/blob/main/contents/Chapter%2011%20-%20null%20%EB%8C%80%EC%8B%A0%20Optional%20%ED%81%B4%EB%9E%98%EC%8A%A4.md>  
[6] <https://unhosted.tistory.com/84>  
[7] <https://velog.io/@kjgi73k/JAVA-Optional%EC%97%90-%EB%8C%80%ED%95%B4-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90>  
[8] <https://www.inflearn.com/community/questions/555667/flatmap-optional%EA%B3%BC-stream%EC%97%90%EC%84%9C%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%A0%90%EC%9D%84-%EC%A0%9C%EA%B0%80-%EC%9E%98-%EC%9D%B4%ED%95%B4%ED%96%88%EB%8A%94%EC%A7%80-%ED%97%B7%EA%B0%88%EB%A6%BD%EB%8B%88%EB%8B%A4>  
[9] <https://burningfalls.github.io/java/how-to-use-optional-class/>  
[10] <https://write-read.tistory.com/entry/JAVA8-Optional>
