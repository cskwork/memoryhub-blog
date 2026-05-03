---
title: "⚡️ JavaScript 한 줄 꿀팁 10선, 코드 길이가 반으로 줄어드는 마법!"
date: 2024-06-10T23:58:05+09:00
slug: "260-JavaScript-한-줄-꿀팁-10선-코드-길이가-반으로-줄어드는-마법"
original_url: "https://memoryhub.tistory.com/260"
tistory_id: 260
draft: false
---

```
     /$$ /$$$$$$$$ /$$
    | $$| $$_____/|__/
 /$$$$$$$| $$       /$$ /$$$$$$$
|__  $$__| $$$$$   | $$| $$__  $$
   | $$  | $$__/   | $$| $$  \ $$
   | $$  | $$      | $$| $$  | $$
   | $$  | $$$$$$$$| $$| $$  | $$
   |__/  |________/|__/|__/  |__/
------------------------------------
       One Line of Code
```

"이거 그냥 `for`문 돌리면 되는 거 아니야?" 저도 그랬습니다. 배열에서 특정 조건의 요소만 뽑아 새로운 배열을 만드는, 너무나 익숙한 작업을 위해 서너 줄의 코드를 기계적으로 작성하곤 했죠. 하지만 어느 날 동료의 코드 리뷰에서 본 단 한 줄의 코드는 제게 신선한 충격을 주었습니다. 간결하고, 우아하고, 심지어 의도까지 명확했죠.

혹시 여러분도 반복되는 로직을 구시대적인 방식으로만 해결하고 계신가요? 이 글을 다 읽고 나면, 여러분의 코드는 몰라보게 간결하고 세련돼질 겁니다.

**⚡️ TL;DR**

1. 자바스크립트 최신 문법을 활용해 코드를 드라마틱하게 줄이는 10가지 실용 예제를 소개합니다.
2. 가독성을 해치지 않으면서 '고수처럼' 코딩하는 베스트 프랙티스를 알려드립니다.

## 목차

1. 배경: 왜 한 줄 코드가 중요한가?
2. 핵심 개념: 한 줄 코드 10가지 마법
3. 실습: Before & After 비교 분석
4. 모범 사례: '절제'의 미학
5. 마치며 & 참고자료

---

## 1. 배경: 왜 한 줄 코드가 중요한가?

"코드는 짧을수록 좋다"는 말이 있습니다. 물론, 무조건 짧기만 한 코드가 능사는 아닙니다. 하지만 JavaScript가 발전하면서 도입된 여러 문법(ES6+)은 단순히 코드 길이를 줄이는 것을 넘어, **가독성을 높이고 개발자의 의도를 명확하게 표현**하도록 돕습니다.

가령, `for` 루프를 사용하는 명령형 코드보다 `map`, `filter` 같은 메서드를 사용한 선언형 코드는 "무엇을" 하는지에 더 집중하게 해줍니다. 이런 패러다임의 변화가 바로 한 줄 코드의 핵심 철학입니다.

✅ **관련 용어 정리**

- **화살표 함수 (Arrow Function)**: `function` 키워드 없이 함수를 더 간결하게 표현하는 문법. `(a, b) => a + b;`
- **구조 분해 할당 (Destructuring Assignment)**: 배열이나 객체의 속성을 분해해서 그 값을 변수에 담을 수 있게 하는 표현식.
- **전개 구문 (Spread Syntax)**: `...`을 사용하여 배열이나 객체를 확장하는 문법.
- **삼항 연산자 (Ternary Operator)**: `if-else` 문을 한 줄로 축약할 수 있는 유일한 연산자. `조건 ? 참일_때_값 : 거짓일_때_값;`

## 2. 핵심 개념: 한 줄 코드 10가지 마법

이제 여러분의 코드를 빛나게 해줄 10가지 한 줄 코드 예제를 만나보시죠. 각 예제는 기존 방식과 한 줄 코드를 비교하여 얼마나 코드가 간결해지는지 보여줍니다.

### ① 두 변수 값 교환하기

> **[a, b] = [b, a];**  
> 임시 변수 없이 배열의 구조 분해 할당을 이용해 두 변수의 값을 즉시 교환합니다.

```
// Before
let a = 'World';
let b = 'Hello';
let temp;

temp = a;
a = b;
b = temp;
// a: 'Hello', b: 'World'

// After ✨
[a, b] = [b, a];
// a: 'Hello', b: 'World'
```

### ② 배열 중복 요소 제거하기

> **[...new Set(array)]**  
> 모든 값이 유일한 `Set` 객체의 특성과 전개 구문을 활용하여 중복을 제거한 새 배열을 만듭니다.

```
const numbers = [1, 2, 3, 3, 4, 5, 5, 5];

// Before
const uniqueNumbers = [];
for (const number of numbers) {
  if (!uniqueNumbers.includes(number)) {
    uniqueNumbers.push(number);
  }
}
// [1, 2, 3, 4, 5]

// After ✨
const uniqueNumbersOneLiner = [...new Set(numbers)];
// [1, 2, 3, 4, 5]
```

### ③ 조건부로 객체 속성 추가하기

> **{ ...baseObject, ...(condition && { conditionalProp: 'value' }) }**  
> 논리곱(&&) 연산자의 단축 평가(short-circuiting)와 전개 구문을 이용해 조건이 참일 때만 객체에 속성을 추가합니다.

```
const user = { id: 1, name: 'John Doe' };
const shouldAddEmail = true;

// Before
let userWithEmail = { ...user };
if (shouldAddEmail) {
  userWithEmail.email = 'john@example.com';
}
// { id: 1, name: 'John Doe', email: 'john@example.com' }

// After ✨
const userWithEmailOneLiner = {
  ...user,
  ...(shouldAddEmail && { email: 'john@example.com' }),
};
// { id: 1, name: 'John Doe', email: 'john@example.com' }
```

### ④ 배열 섞기 (Shuffle)

> **array.sort(() => Math.random() - 0.5)**  
> `sort` 메서드의 비교 함수에 무작위 값을 반환하게 하여 배열 요소를 무작위로 섞습니다. (간단한 셔플에 유용)

```
const items = [1, 2, 3, 4, 5, 6];

// After ✨
const shuffledItems = items.sort(() => Math.random() - 0.5);
console.log(shuffledItems); // e.g., [ 4, 1, 6, 3, 5, 2 ]
```

### ⑤ 특정 범위의 숫자 배열 생성하기

> **Array.from({ length: N }, (\_, i) => i)**  
> `Array.from`을 사용해 원하는 길이(N)의 배열을 만들고, 콜백 함수로 0부터 N-1까지의 숫자를 채웁니다.

```
const n = 5; // 0부터 4까지의 배열 생성

// Before
const range = [];
for (let i = 0; i  i);
// [0, 1, 2, 3, 4]
```

### ⑥ 배열의 모든/일부 요소 조건 확인하기

> **array.every(condition) / array.some(condition)**  
> `every`는 모든 요소가 조건을 만족해야 `true`, `some`은 하나라도 만족하면 `true`를 반환합니다.

```
const ages = [22, 31, 19, 45, 17];

// 모든 사람이 성인인지?
const allAdults = ages.every(age => age >= 18); // false

// 미성년자가 한 명이라도 있는지?
const hasMinors = ages.some(age => age  **nestedArray.flat()**  
> `flat()` 메서드는 한 단계의 중첩 배열을 손쉽게 평탄화합니다. 더 깊은 배열은 `flat(Infinity)`로 처리 가능합니다.

```javascript
const nested = [1, [2, 3], [4, [5]]];

// 1단계 평탄화 ✨
const flattened = nested.flat(); // [1, 2, 3, 4, [5]]

// 모든 하위 배열 평탄화 ✨
const deepFlattened = nested.flat(Infinity); // [1, 2, 3, 4, 5]
```

### ⑧ 파일 경로에서 파일명/확장자 추출하기

> **path.split('/').pop()**  
> 문자열 메서드를 연달아 사용하여 경로를 분리하고 마지막 요소를 가져옵니다.

```
const filePath = '/Users/dev/project/src/index.js';

// 파일명 추출 ✨
const fileName = filePath.split('/').pop(); // 'index.js'

// 확장자 추출 ✨
const extension = filePath.split('.').pop(); // 'js'
```

### ⑨ `if-else`를 삼항 연산자로 바꾸기

> **const result = condition ? 'value1' : 'value2';**  
> 간단한 조건부 값 할당은 삼항 연산자로 명료하게 표현할 수 있습니다.

```
const isAuthenticated = true;

// Before
let status;
if (isAuthenticated) {
  status = 'Logged In';
} else {
  status = 'Logged Out';
}
// 'Logged In'

// After ✨
const statusOneLiner = isAuthenticated ? 'Logged In' : 'Logged Out';
// 'Logged In'
```

### ⑩ 화살표 함수로 간단한 계산하기

> **const add = (a, b) => a + b;**  
> 단순한 반환문만 있는 함수는 화살표 함수로 극도로 간결하게 만들 수 있습니다.

```
// Before
function multiply(a, b) {
  return a * b;
}

// After ✨
const multiplyOneLiner = (a, b) => a * b;

console.log(multiplyOneLiner(5, 7)); // 35
```

## 3. 실습: Before & After 비교 분석

위 2번 항목에서 각 한 줄 코드의 `Before`와 `After`를 비교하며 그 효과를 이미 확인했습니다. 핵심은 **명령형 프로그래밍(어떻게 할지 지시)**에서 **선언형 프로그래밍(무엇을 원하는지 선언)**으로의 전환입니다.

- `for` 루프는 "배열을 순회하면서, 조건에 맞으면, 새 배열에 값을 넣어라"는 **방법**을 지시합니다.
- `filter` 메서드는 "이 조건에 맞는 값들만 **원한다**"고 선언합니다.

이러한 패러다임의 변화를 이해하면 한 줄 코드를 더욱 효과적으로 사용할 수 있습니다.

## 4. 모범 사례: '절제'의 미학

한 줄 코드는 강력하지만, 남용하면 오히려 독이 될 수 있습니다. "나만 아는 암호"가 아닌 "누구나 이해하는 코드"를 위한 원칙을 지켜야 합니다.

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **메서드 체이닝** | 로직의 흐름이 물 흐르듯 자연스럽게 이어진다. | 3~4개 이상 체이닝하면 디버깅이 어렵고 가독성이 떨어진다. |
| **삼항 연산자** | 간단한 `if-else`를 매우 간결하게 만든다. | 중첩해서 사용하면 '지옥의 삼항 연산자'가 되어 가독성을 해친다. |
| **단축 평가(&&, ||)** | 조건부 렌더링/실행에 유용하다. | 익숙하지 않은 개발자에게는 로직 파악이 직관적이지 않을 수 있다. |

> ? **핵심 원칙: 가독성을 희생하면서까지 코드를 줄이지 마세요.** 한 줄로 줄인 코드가 동료에게 설명이 필요하다면, 그건 좋은 코드가 아닐 확률이 높습니다.

## 5. 마치며

오늘 우리는 10가지 JavaScript 한 줄 코드 기법을 통해 코드를 더 간결하고 우아하게 만드는 법을 배웠습니다.

- 화살표 함수, 구조 분해 할당 등 모던 JavaScript 문법은 코드 단축의 핵심입니다.
- `map`, `filter`, `reduce`와 같은 배열 메서드를 활용하면 선언적인 코드를 작성할 수 있습니다.
- 가장 중요한 것은 '간결함'과 '가독성' 사이의 균형을 맞추는 것입니다.

이제 여러분의 프로젝트로 돌아가서 리팩토링할 만한 `for` 루프를 찾아보세요. 오늘 배운 한 줄 코드로 바꿔보는 작은 시도가 여러분을 더 나은 개발자로 만들어 줄 겁니다.

**이 글이 유용하셨다면 ❤️와 댓글 부탁드립니다! 여러분이 알고 있는 멋진 한 줄 코드가 있다면 공유해주세요!**

---

### 참고자료

- [MDN: Arrow functions](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [MDN: Destructuring assignment](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
- [MDN: Array methods](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array)
- (샘플 레포) [github.com/your-username/js-one-liners-example](https://github.com/your-username/js-one-liners-example)
- 추가 읽을거리
  1. [You Don't Know JS: ES6 & Beyond](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/es6%20&%20beyond/README.md)
  2. [JavaScript — The Conditional (Ternary) Operator](https://www.freecodecamp.org/news/javascript-ternary-operator/)
  3. [Functional Programming in JavaScript](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0)
