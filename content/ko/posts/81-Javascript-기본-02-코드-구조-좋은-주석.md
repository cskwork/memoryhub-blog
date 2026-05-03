---
title: "Javascript 기본 02 - 코드 구조, 좋은 주석"
date: 2024-05-25T17:56:44+09:00
slug: "81-Javascript-기본-02-코드-구조-좋은-주석"
original_url: "https://memoryhub.tistory.com/81"
tistory_id: 81
draft: false
---

## 요약

- JavaScript의 문(statement), 세미콜론 사용법, 주석 유형과 작성 방식에 대한 체계적 분석
- 명확한 코드 작성이 최우선이며, 주석은 보조적 역할로 필요한 경우에만 사용해야 함
- 효과적인 주석은 아키텍처 설명, API 문서화, 문제 해결 접근법 설명, 복잡한 알고리즘 이해를 돕는 데 중요함
- 코드의 가독성과 유지보수성을 높이기 위한 주석 작성 원칙과 실제 활용 방법 제시

## 1. JavaScript 문법의 기본 요소

### 1.1 문(Statement)의 이해

문(statement)은 JavaScript에서 실행 가능한 최소 단위의 독립적인 명령어입니다. 각 문은 특정 작업을 수행하도록 JavaScript 엔진에 지시합니다.[^1]

```
let x = 5;          // 변수 선언 문
console.log(x);     // 함수 호출 문
if (x > 0) {        // 조건 문
  x = x * 2;
}
```

### 1.2 세미콜론(;) 사용의 중요성

JavaScript에서 각 문의 끝에는 세미콜론(;)을 사용하여 문의 종료를 명시적으로 표시해야 합니다. JavaScript는 자동 세미콜론 삽입(ASI, Automatic Semicolon Insertion) 메커니즘을 갖고 있으나, 이에 의존하는 것은 예기치 않은 오류를 발생시킬 수 있습니다.[^2]

특히 다음과 같은 상황에서는 세미콜론 누락이 심각한 오류를 일으킬 수 있습니다:

```
// 오류 발생 가능 코드
alert("첫 번째 메시지")
[1, 2].forEach(alert)

// 올바른 코드
alert("첫 번째 메시지");
[1, 2].forEach(alert);
```

첫 번째 예시에서 JavaScript 엔진은 코드를 다음과 같이 해석할 수 있습니다:

```
alert("첫 번째 메시지")[1, 2].forEach(alert)
```

이는 문법적으로 유효하지만 의도한 동작이 아닙니다. 세미콜론을 명시적으로 사용하면 이러한 모호성을 방지할 수 있습니다.

## 2. JavaScript 주석의 유형과 사용법

### 2.1 주석의 기본 형식

JavaScript에서는 두 가지 유형의 주석이 지원됩니다:

1. **한 줄 주석**: `//` 기호 이후의 텍스트가 주석으로 처리됩니다.

   ```
   // 이것은 한 줄 주석입니다
   let count = 0; // 이렇게 코드 뒤에도 작성 가능합니다
   ```
2. **여러 줄 주석**: `/*`와 `*/` 사이의 모든 텍스트가 주석으로 처리됩니다.

   ```
   /* 
    * 이것은 여러 줄에 걸친
    * 주석입니다.
    * 복잡한 설명을 작성할 때 유용합니다.
    */
   ```

### 2.2 비효율적인 주석 사례

효과적이지 않은 주석은 코드의 가독성을 저하시키고 유지보수 비용을 증가시킬 수 있습니다.[^3] 다음은 지양해야 할 주석 사례입니다:

1. **코드의 명백한 동작을 설명하는 주석**

   ```
   // i 변수를 1씩 증가시킵니다
   i++;

   // 사용자의 이름을 변수에 저장합니다
   const userName = user.name;
   ```
2. **코드 이력이나 작성자 정보만 포함하는 주석**

   ```
   // 김개발이 2023년 3월 15일에 작성
   // 2023년 4월 2일 수정됨
   function calculateTotal() {
     // 함수 내용
   }
   ```
3. **오래된 코드를 주석 처리하여 보존하는 경우**

   ```
   // 옛날 방식
   // function oldMethod() {
   //   return x * y;
   // }

   // 새로운 방식
   function newMethod() {
     return x * y * z;
   }
   ```

   이러한 경우 버전 관리 시스템(Git 등)을 통해 코드 이력을 관리하는 것이 더 효율적입니다.

## 3. 효과적인 주석 작성 원칙

### 3.1 자기 설명적인 코드 작성

Robert C. Martin의 "Clean Code"에 따르면, 가장 좋은 주석은 주석이 필요 없는 코드를 작성하는 것입니다.[^4] 이를 위해서는:

1. **명확한 변수명과 함수명 사용**

   ```
   // 좋지 않은 예
   const d = new Date();
   const m = d.getMonth();

   // 좋은 예
   const currentDate = new Date();
   const currentMonth = currentDate.getMonth();
   ```
2. **단일 책임 원칙을 따르는 함수 작성**

   ```
   // 여러 작업을 하는 함수 (지양해야 함)
   function processUser(user) {
     // 사용자 검증, 데이터 처리, DB 저장 등을 모두 수행
   }

   // 단일 책임을 가진 함수들 (권장)
   function validateUser(user) { /* ... */ }
   function processUserData(userData) { /* ... */ }
   function saveUserToDatabase(processedUser) { /* ... */ }
   ```
3. **복잡한 표현식 분해**

   ```
   // 복잡한 표현식 (이해하기 어려움)
   if (user.age >= 18 && user.country === 'KR' && !user.isBlocked && user.subscription.isActive) {
     // 코드
   }

   // 분해된 표현식 (더 이해하기 쉬움)
   const isAdult = user.age >= 18;
   const isKorean = user.country === 'KR';
   const isNotBlocked = !user.isBlocked;
   const hasActiveSubscription = user.subscription.isActive;

   if (isAdult && isKorean && isNotBlocked && hasActiveSubscription) {
     // 코드
   }
   ```

### 3.2 효과적인 주석이 필요한 상황

자기 설명적인 코드를 작성하는 것이 중요하지만, 다음과 같은 상황에서는 효과적인 주석이 필요합니다:

#### 3.2.1 아키텍처 설명 주석

시스템의 고수준 구조와 컴포넌트 간 상호작용을 설명하는 주석은 코드베이스를 처음 접하는 개발자에게 큰 도움이 됩니다.

```
/**
 * 사용자 인증 모듈
 * 
 * 이 모듈은 다음 세 가지 주요 구성 요소로 이루어져 있습니다:
 * 1. AuthManager: 전체 인증 프로세스를 조정
 * 2. TokenService: JWT 토큰 생성 및 검증 담당
 * 3. UserValidator: 사용자 자격 증명 검증 담당
 * 
 * 인증 흐름:
 * 클라이언트 요청 → UserValidator → AuthManager → TokenService → 응답
 */
```

#### 3.2.2 함수 API 문서화 (JSDoc)

JSDoc은 코드에서 함수의 목적, 매개변수, 반환 값을 문서화하는 표준화된 방법입니다.[^5] 이를 통해 IDE의 자동 완성 기능 및 타입 검사 기능을 활용할 수 있습니다.

```
/**
 * 주어진 숫자의 거듭제곱을 계산합니다.
 *
 * @param {number} base - 거듭제곱할 기본 숫자
 * @param {number} exponent - 제곱 지수 (양의 정수여야 함)
 * @returns {number} 계산된 거듭제곱 값
 * @throws {Error} 지수가 양의 정수가 아닌 경우 예외 발생
 * 
 * @example
 * // 8 반환
 * power(2, 3);
 */
function power(base, exponent) {
  if (exponent < 0 || !Number.isInteger(exponent)) {
    throw new Error('지수는 양의 정수여야 합니다');
  }

  let result = 1;
  for (let i = 0; i < exponent; i++) {
    result *= base;
  }
  return result;
}
```

#### 3.2.3 비직관적인 해결 방법에 대한 설명

코드가 직관적이지 않은 방식으로 문제를 해결하는 경우, 그 이유를 설명하는 주석이 필요합니다.

```
// 정규 표현식 대신 수동 파싱을 사용합니다.
// 이 특정 입력 형식에서는 정규 표현식이 지수적 시간 복잡도를 가질 수 있어
// 큰 입력에서 성능 문제가 발생할 수 있기 때문입니다.
function parseCustomFormat(input) {
  // 수동 파싱 구현
}
```

#### 3.2.4 복잡한 알고리즘 설명

복잡한 알고리즘의 경우, 코드의 작동 방식과 각 단계의 목적을 설명하는 주석이 유용합니다.

```
/**
 * 퀵 정렬 알고리즘 구현
 * 시간 복잡도: 평균 O(n log n), 최악 O(n²)
 * 공간 복잡도: O(log n)
 */
function quickSort(array, left = 0, right = array.length - 1) {
  // 기저 조건: 부분 배열의 크기가 1 이하일 때
  if (left >= right) {
    return;
  }

  // 피벗 선택 및 파티션 과정
  const pivotIndex = partition(array, left, right);

  // 피벗을 기준으로 두 부분 배열에 대해 재귀적으로 정렬 수행
  quickSort(array, left, pivotIndex - 1);
  quickSort(array, pivotIndex + 1, right);

  return array;
}

function partition(array, left, right) {
  // 구현 내용
}
```

## 4. 실용적인 주석 작성 가이드라인

효과적인 주석 작성을 위한 실용적인 가이드라인은 다음과 같습니다:

1. **코드 작성 전에 설계 주석부터 시작하기**

   - 구현하기 전에 함수나 모듈의 목적, 입출력, 제약 조건 등을 주석으로 작성
   - 이는 설계 단계에서 논리적 오류를 발견하는 데 도움이 됨
2. **주석과 코드의 일치성 유지하기**

   - 코드가 변경되면 관련 주석도 함께 업데이트
   - 오래된 주석은 코드 이해에 방해가 될 수 있음
3. **'왜'에 초점 맞추기**

   - 코드가 '무엇'을 하는지는 코드 자체로 명확해야 함
   - 주석은 '왜' 그런 방식으로 구현했는지에 초점을 맞춤
4. **경계 조건과 예외 상황 문서화하기**

   - 코드가 처리하는 특별한 경우나 제약 조건을 주석으로 설명
   - 미래의 개발자가 코드를 수정할 때 발생할 수 있는 위험을 줄임

## 5. 결론

JavaScript에서 효과적인 코드 작성과 주석 사용은 코드의 가독성, 유지보수성, 그리고 팀 협업 효율성에 직접적인 영향을 미칩니다. 가장 좋은 코드는 주석 없이도 이해할 수 있는 코드지만, 복잡한 시스템과 알고리즘에서는 적절한 주석이 필수적입니다.

효과적인 주석은 코드 자체로는 표현하기 어려운 의도와 맥락을 제공하며, 특히 API 문서화, 아키텍처 설명, 비직관적 해결책의 근거를 설명하는 데 중요한 역할을 합니다. 주석은 다른 개발자와의 의사소통 수단이자, 미래의 자신을 위한 기록이라는 점을 기억하며 작성해야 합니다.

## 참고 문헌

[^1]: Mozilla Developer Network. "JavaScript 문(Statements)." MDN Web Docs. <https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements>

[^2]: Mozilla Developer Network. "세미콜론 자동 삽입." MDN Web Docs. <https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion>

[^3]: Wulf, D. S., & Bertacchini, F. (2022). "Measuring Comment Quality in Software Development Projects." IEEE Transactions on Software Engineering, 48(1), 106-121.

[^4]: Martin, R. C. (2008). Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.

[^5]: JSDoc. "JSDoc 사용 가이드." <https://jsdoc.app/>

[^6]: JavaScript.info. "코드 구조." <https://ko.javascript.info/structure>

[^7]: JavaScript.info. "주석." <https://ko.javascript.info/comments>
