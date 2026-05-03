---
title: "? Java Optional.flatMap(), what's really different from map()?"
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

Remember the frustration of null checks like `if (user != null)` followed by `if (user.getAddress() != null)`... a chain of null checks linked one after another? When Java 8 introduced `Optional`, a path out of this "null hell" finally opened. But as you use `Optional`, you'll encounter two methods: `map()` and `flatMap()`. Both seem to transform values, but they have different names and it's often unclear when to use which one.

After reading this article all the way through, you'll understand the decisive difference between `map()` and `flatMap()` clearly, and you'll know how to elegantly handle nested `Optional`s.

⚡ **TL;DR**

- **`map()`**: Wraps the result returned by the transformation function in `Optional` **one more time.** (`T -> Optional`)
- **`flatMap()`**: Returns the `Optional` returned by the transformation function **as-is, flattening it.** (`Optional -> Optional`)

---

### Table of Contents

1. Background: Why did `Optional` appear?
2. Core Concept: `map` vs `flatMap`
3. Practice: Handling nested `Optional`
4. Best Practices: When should you use `flatMap`?
5. Conclusion & References

---

### 1. Background: Why did `Optional` appear?

`Optional` is a wrapper class that wraps an object that may be null[5]. By using `Optional`, developers explicitly signal that the variable can be null and force null handling logic, preventing `NullPointerException`(NPE).

- ✅ **`Optional`**: A container object that wraps a `T` type object that may be null, forcing explicit null handling[5].
- ✅ **`map()`**: If a value exists in `Optional`, applies the given function and returns the result wrapped in `Optional`[1].
- ✅ **`flatMap()`**: Similar to `map()`, but when the result of the given function is already `Optional`, returns that result as-is, preventing nesting[1].

### 2. Core Concept: `map` vs `flatMap`

> **Unlike `map()`, `flatMap()` doesn't double-wrap when the transformation function's return type is already `Optional`; instead, it flattens the result.**[1][9]

The biggest difference between the two methods is the **return type of the mapping function**[2].

```
// map's mapping function takes type T and returns type U
public Optional map(Function mapper);

// flatMap's mapping function takes type T and returns Optional type
public Optional flatMap(Function> mapper);
```

`map()` always wraps the value returned by the mapping function (`U`) in `Optional` to create `Optional`[6]. On the other hand, `flatMap()` returns `Optional` directly from the function without additional wrapping since the function already returns `Optional`[2][6].

Because of this difference, if the mapping function's result is already `Optional`, using `map()` creates unwanted nested `Optional`.

```
// 1. Using map(): Result becomes Optional>
Optional> nestedOptional = Optional
    .of("string")
    .map(s -> Optional.of("STRING")); // Returns Optional containing "STRING"

// 2. Using flatMap(): Result is flattened to Optional
Optional flatOptional = Optional
    .of("string")
    .flatMap(s -> Optional.of("STRING")); // Returns Optional containing "STRING"
```

### 3. Practice: Handling Nested `Optional`

Imagine a scenario where you traverse `Product` → `Person` → `Job` in a chained object reference structure to get the job name. Each reference is wrapped in `Optional`[3].

#### ① DTO Preparation

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

#### ② The Problem with Using Only `map()`

What happens if you try to get the job name using only `map()`?

```
Optional optProduct = /* ... initialize product object ... */;

// Compilation error!
Optional jobName = optProduct
    .map(Product::getPerson) // Return type: Optional>
    .map(Person::getJob)     // Error! Need to call getJob() on Optional
    .map(Job::getJobName);
```

The first `map(Product::getPerson)` call causes the problem. The `Product::getPerson` method returns `Optional`, but `map` wraps this result again in `Optional`, creating `Optional>` type[3][5]. The double-wrapped `Optional` doesn't have the `Person`'s `getJob` method, so a compilation error occurs in the next chain.

#### ③ Solution with `flatMap()`

This is where `flatMap()` comes in. `flatMap()` exists for functions that return `Optional` and flattens the result so you can continue the chain[1][9].

```
Optional optProduct = /* ... initialize product object ... */;

// Use flatMap to resolve the nesting structure
Optional jobName = optProduct
    .flatMap(Product::getPerson) // Return type: Optional
    .flatMap(Person::getJob)     // Return type: Optional
    .map(Job::getJobName);      // Return type: Optional

System.out.println(jobName.orElse("Job information not available"));
```

- `optProduct.flatMap(Product::getPerson)`: Since `getPerson` returns `Optional`, `flatMap` receives it and returns `Optional` as-is.
- `.flatMap(Person::getJob)`: Similarly, returns the `Optional` that is the return type of `getJob` as-is.
- `.map(Job::getJobName)`: Finally, `getJobName` returns a `String`. This `String` value needs to be wrapped in `Optional` at the end, so using `map` is natural here[3][6].

### 4. Best Practices: When should you use `flatMap()`?

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| **Consecutive `map()`** | Good for simple value transformations where the transformation function doesn't return `Optional`, and the code is concise[6]. | If the transformation function returns `Optional`, you get an `Optional>` structure that becomes complex[5]. |
| **Using `flatMap()`** | Prevents nesting when chaining functions that return `Optional`, keeping code clean. Essential for domain object traversal[2][9]. | If the transformation function returns a regular value instead of `Optional`, using `flatMap()` causes a compilation error. |
| **Mixing `map()` and `flatMap()`** | Flexible combination: use `flatMap()` for intermediate steps returning `Optional`, and `map()` for final steps returning regular values[3]. | Must clearly understand each method's return type to avoid confusion. |

### 5. Conclusion

Today we explored Java `Optional`'s `map()` and `flatMap()` in depth.

1. `Optional` is a powerful tool for handling `null` safely and explicitly.
2. `map()` always wraps transformation results in `Optional`, while `flatMap()` flattens the result when the return value is already `Optional`.
3. When calling methods that return `Optional` one after another, like traversing an object graph, use `flatMap()` to make your code concise and elegant[9].

In your actual projects, try refactoring null check logic with `Optional` and `flatMap()`. You'll be able to write much more declarative and readable code, freed from the hell of `if` statements.

If this article was helpful, please leave a ❤️ and a comment!

---

#### References

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
