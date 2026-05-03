---
title: "⚡ 10 JavaScript One-Liner Tips: The Magic That Cuts Code Length in Half!"
date: 2024-06-10T23:58:05+09:00
slug: "260-JavaScript-한-줄-꿀팁-10선-코드-길이가-반으로-줄어드는-마법"
original_url: "https://memoryhub.tistory.com/260"
tistory_id: 260
draft: false
categories: ["Dev Language"]
tags: ["Javascript"]
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

"Wouldn't it be simpler to just use a `for` loop?" I used to think the same way. For the familiar task of extracting specific elements from an array and creating a new array, I mechanically wrote three or four lines of code. But one day, when reviewing a colleague's code, I saw a single line that gave me a fresh shock. It was concise, elegant, and even the intent was crystal clear.

Are you still solving repetitive logic only in outdated ways? After reading this article, your code will become unrecognizably cleaner and more refined.

**⚡ TL;DR**

1. We introduce 10 practical examples for dramatically reducing code using the latest JavaScript syntax.
2. We share best practices for coding 'like a pro' without sacrificing readability.

## Table of Contents

1. Background: Why One-Liner Code Matters?
2. Core Concepts: 10 Magic One-Liner Tricks
3. Practice: Before & After Comparative Analysis
4. Best Practices: The Aesthetics of Restraint
5. Conclusion & Resources

---

## 1. Background: Why One-Liner Code Matters?

There's a saying that "shorter code is better." Of course, code that's just short isn't always the solution. However, as JavaScript has evolved and introduced various syntax features (ES6+), they go beyond simply reducing code length. They **improve readability and help developers express their intent clearly**.

For example, declarative code using methods like `map` and `filter` focuses more on "what" you're doing compared to imperative code using `for` loops. This paradigm shift is the core philosophy of one-liner code.

✅ **Terminology**

- **Arrow Function**: Syntax for expressing functions more concisely without the `function` keyword. `(a, b) => a + b;`
- **Destructuring Assignment**: An expression that decomposes the properties of arrays or objects and assigns their values to variables.
- **Spread Syntax**: Syntax using `...` to expand arrays or objects.
- **Ternary Operator**: The only operator that can abbreviate `if-else` statements into a single line. `condition ? value_if_true : value_if_false;`

## 2. Core Concepts: 10 Magic One-Liner Tricks

Now let's explore 10 one-liner code examples that will make your code shine. Each example compares the old way with a one-liner, showing how much cleaner the code becomes.

### ① Swapping Two Variables

> **[a, b] = [b, a];**  
> Using array destructuring assignment, you can immediately swap the values of two variables without a temporary variable.

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

### ② Removing Duplicate Elements from an Array

> **[...new Set(array)]**  
> Using the Set object's characteristic of having all unique values and spread syntax, create a new array with duplicates removed.

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

### ③ Conditionally Adding Object Properties

> **{ ...baseObject, ...(condition && { conditionalProp: 'value' }) }**  
> Using the logical AND (&&) operator's short-circuiting and spread syntax, add properties to an object only when the condition is true.

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

### ④ Shuffling an Array

> **array.sort(() => Math.random() - 0.5)**  
> By having the comparison function in the sort method return a random value, you randomly shuffle array elements. (Useful for simple shuffles)

```
const items = [1, 2, 3, 4, 5, 6];

// After ✨
const shuffledItems = items.sort(() => Math.random() - 0.5);
console.log(shuffledItems); // e.g., [ 4, 1, 6, 3, 5, 2 ]
```

### ⑤ Creating a Number Array in a Specific Range

> **Array.from({ length: N }, (_, i) => i)**  
> Using `Array.from`, create an array of the desired length (N) and fill it with numbers from 0 to N-1 using a callback function.

```
const n = 5; // Create array from 0 to 4

// Before
const range = [];
for (let i = 0; i < n; i++) {
  range.push(i);
}
// [0, 1, 2, 3, 4]

// After ✨
const rangeOneLiner = Array.from({ length: n }, (_, i) => i);
// [0, 1, 2, 3, 4]
```

### ⑥ Checking All/Some Elements in an Array Against a Condition

> **array.every(condition) / array.some(condition)**  
> `every` returns `true` only if all elements satisfy the condition. `some` returns `true` if at least one element satisfies the condition.

```
const ages = [22, 31, 19, 45, 17];

// Are all people adults?
const allAdults = ages.every(age => age >= 18); // false

// Is there at least one minor?
const hasMinors = ages.some(age => age < 18); // true
```

### ⑦ Flattening Nested Arrays

> **nestedArray.flat()**  
> The `flat()` method easily flattens one level of nested arrays. Deeper arrays can be handled with `flat(Infinity)`.

```javascript
const nested = [1, [2, 3], [4, [5]]];

// Flattening one level ✨
const flattened = nested.flat(); // [1, 2, 3, 4, [5]]

// Flattening all nested arrays ✨
const deepFlattened = nested.flat(Infinity); // [1, 2, 3, 4, 5]
```

### ⑧ Extracting Filename/Extension from File Path

> **path.split('/').pop()**  
> By chaining string methods, separate the path and get the last element.

```
const filePath = '/Users/dev/project/src/index.js';

// Extract filename ✨
const fileName = filePath.split('/').pop(); // 'index.js'

// Extract extension ✨
const extension = filePath.split('.').pop(); // 'js'
```

### ⑨ Converting `if-else` to Ternary Operator

> **const result = condition ? 'value1' : 'value2';**  
> Simple conditional value assignment can be expressed clearly with a ternary operator.

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

### ⑩ Simple Calculations with Arrow Functions

> **const add = (a, b) => a + b;**  
> Functions with only simple return statements can be made extremely concise with arrow functions.

```
// Before
function multiply(a, b) {
  return a * b;
}

// After ✨
const multiplyOneLiner = (a, b) => a * b;

console.log(multiplyOneLiner(5, 7)); // 35
```

## 3. Practice: Before & After Comparative Analysis

We've already confirmed the effects by comparing the `Before` and `After` of each one-liner in section 2 above. The key is the shift from **imperative programming (instructing how to do it)** to **declarative programming (declaring what you want)**.

- A `for` loop instructs the **method**: "iterate through the array, if the condition matches, add the value to a new array."
- The `filter` method **declares**: "I want only values that match this condition."

Understanding this paradigm shift allows you to use one-liner code more effectively.

## 4. Best Practices: The Aesthetics of Restraint

One-liner code is powerful, but overusing it can become harmful. You must follow principles to write "code anyone can understand," not "code only I understand."

| Pattern | Advantage | Caution |
| --- | --- | --- |
| **Method Chaining** | The logic flow naturally feels like water flowing. | Chaining 3-4 or more makes debugging difficult and reduces readability. |
| **Ternary Operator** | Shortens simple `if-else` statements very concisely. | Nesting creates "ternary operator hell," damaging readability. |
| **Short-Circuiting (&&, \|\|)** | Useful for conditional rendering/execution. | Unfamiliar developers may not intuitively grasp the logic. |

> **Core Principle: Don't reduce code at the expense of readability.** If a one-liner needs explanation to your colleagues, it's probably not good code.

## 5. Conclusion

Today we learned how to make code cleaner and more elegant through 10 JavaScript one-liner techniques.

- Modern JavaScript syntax like arrow functions and destructuring assignment is the key to code reduction.
- Using array methods like `map`, `filter`, and `reduce` allows you to write declarative code.
- The most important thing is balancing 'conciseness' and 'readability.'

Now go back to your projects and find `for` loops worth refactoring. Your small attempt to replace them with today's one-liner code will make you a better developer.

**If this article was helpful, please ❤️ and leave a comment! If you know any cool one-liners, please share them with us!**

---

### References

- [MDN: Arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
- [MDN: Destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
- [MDN: Array methods](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
- (Sample repo) [github.com/your-username/js-one-liners-example](https://github.com/your-username/js-one-liners-example)
- Further reading
  1. [You Don't Know JS: ES6 & Beyond](https://github.com/getify/You-Dont-Know-JS/blob/1st-ed/es6%20&%20beyond/README.md)
  2. [JavaScript — The Conditional (Ternary) Operator](https://www.freecodecamp.org/news/javascript-ternary-operator/)
  3. [Functional Programming in JavaScript](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-functional-programming-7f218c68b3a0)
