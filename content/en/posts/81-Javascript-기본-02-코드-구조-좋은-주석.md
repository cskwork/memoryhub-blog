---
title: "JavaScript Basics 02 - Code Structure and Good Comments"
date: 2024-05-25T17:56:44+09:00
slug: "81-Javascript-기본-02-코드-구조-좋은-주석"
original_url: "https://memoryhub.tistory.com/81"
tistory_id: 81
draft: false
---

## Summary

- Systematic analysis of JavaScript statements, semicolon usage, comment types, and writing methods
- Clear code writing is the top priority, and comments should be used only when necessary as a supporting role
- Effective comments are important for explaining architecture, documenting APIs, explaining problem-solving approaches, and helping understand complex algorithms
- Principles and practical methods for writing comments to increase code readability and maintainability

## 1. Basic Elements of JavaScript Syntax

### 1.1 Understanding Statements

A statement is an independent, executable command unit in JavaScript. Each statement instructs the JavaScript engine to perform a specific task.[^1]

```
let x = 5;          // variable declaration statement
console.log(x);     // function call statement
if (x > 0) {        // conditional statement
  x = x * 2;
}
```

### 1.2 Importance of Semicolon Usage

Each statement in JavaScript should explicitly end with a semicolon (;). While JavaScript has an Automatic Semicolon Insertion (ASI) mechanism, relying on it can cause unexpected errors.[^2]

In particular, missing semicolons can cause serious errors in situations like:

```
// Code that may cause errors
alert("First message")
[1, 2].forEach(alert)

// Correct code
alert("First message");
[1, 2].forEach(alert);
```

In the first example, the JavaScript engine may interpret the code as:

```
alert("First message")[1, 2].forEach(alert)
```

This is syntactically valid but not the intended behavior. Using semicolons explicitly prevents such ambiguity.

## 2. Types and Usage of JavaScript Comments

### 2.1 Basic Comment Format

JavaScript supports two types of comments:

1. **Single-line comments**: Text after `//` is treated as a comment.

   ```
   // This is a single-line comment
   let count = 0; // Can also be written after code like this
   ```
2. **Multi-line comments**: All text between `/*` and `*/` is treated as a comment.

   ```
   /* 
    * This is a comment
    * spanning multiple lines.
    * Useful for writing complex explanations.
    */
   ```

### 2.2 Ineffective Comment Examples

Ineffective comments can reduce code readability and increase maintenance costs.[^3] Here are examples of comments to avoid:

1. **Comments explaining obvious code behavior**

   ```
   // Increment i by 1
   i++;

   // Save the user's name to a variable
   const userName = user.name;
   ```
2. **Comments containing only code history or author information**

   ```
   // Written by Kim Developer on March 15, 2023
   // Modified on April 2, 2023
   function calculateTotal() {
     // function content
   }
   ```
3. **Preserving old code by commenting it out**

   ```
   // Old way
   // function oldMethod() {
   //   return x * y;
   // }

   // New way
   function newMethod() {
     return x * y * z;
   }
   ```

   In such cases, it's more efficient to manage code history through version control systems like Git.

## 3. Principles for Effective Comment Writing

### 3.1 Writing Self-Explanatory Code

According to Robert C. Martin's "Clean Code," the best comment is code that doesn't need comments.[^4] To achieve this:

1. **Use clear variable and function names**

   ```
   // Bad example
   const d = new Date();
   const m = d.getMonth();

   // Good example
   const currentDate = new Date();
   const currentMonth = currentDate.getMonth();
   ```
2. **Write functions that follow the Single Responsibility Principle**

   ```
   // Function doing multiple tasks (should avoid)
   function processUser(user) {
     // Performs user validation, data processing, DB saving, etc.
   }

   // Functions with single responsibility (recommended)
   function validateUser(user) { /* ... */ }
   function processUserData(userData) { /* ... */ }
   function saveUserToDatabase(processedUser) { /* ... */ }
   ```
3. **Break down complex expressions**

   ```
   // Complex expression (difficult to understand)
   if (user.age >= 18 && user.country === 'KR' && !user.isBlocked && user.subscription.isActive) {
     // code
   }

   // Broken down expression (easier to understand)
   const isAdult = user.age >= 18;
   const isKorean = user.country === 'KR';
   const isNotBlocked = !user.isBlocked;
   const hasActiveSubscription = user.subscription.isActive;

   if (isAdult && isKorean && isNotBlocked && hasActiveSubscription) {
     // code
   }
   ```

### 3.2 Situations Where Effective Comments Are Needed

While writing self-explanatory code is important, effective comments are needed in the following situations:

#### 3.2.1 Architecture Explanation Comments

Comments explaining the high-level structure and interaction between components of a system are very helpful for developers encountering the codebase for the first time.

```
/**
 * User authentication module
 * 
 * This module consists of three main components:
 * 1. AuthManager: Coordinates the entire authentication process
 * 2. TokenService: Responsible for JWT token creation and validation
 * 3. UserValidator: Responsible for validating user credentials
 * 
 * Authentication flow:
 * Client request → UserValidator → AuthManager → TokenService → Response
 */
```

#### 3.2.2 Function API Documentation (JSDoc)

JSDoc is a standardized way to document a function's purpose, parameters, and return values in code.[^5] This enables IDE auto-completion and type checking features.

```
/**
 * Calculates the power of a given number.
 *
 * @param {number} base - The base number to raise to a power
 * @param {number} exponent - The exponent (must be a positive integer)
 * @returns {number} The calculated power value
 * @throws {Error} Throws an error if the exponent is not a positive integer
 * 
 * @example
 * // Returns 8
 * power(2, 3);
 */
function power(base, exponent) {
  if (exponent < 0 || !Number.isInteger(exponent)) {
    throw new Error('Exponent must be a positive integer');
  }

  let result = 1;
  for (let i = 0; i < exponent; i++) {
    result *= base;
  }
  return result;
}
```

#### 3.2.3 Explanation of Non-Intuitive Solutions

When code solves a problem in a non-obvious way, a comment explaining the reason is necessary.

```
// Use manual parsing instead of regular expressions.
// Regular expressions can have exponential time complexity for this specific input format,
// which can cause performance issues with large inputs.
function parseCustomFormat(input) {
  // Manual parsing implementation
}
```

#### 3.2.4 Complex Algorithm Explanation

For complex algorithms, comments explaining how the code works and the purpose of each step are useful.

```
/**
 * QuickSort algorithm implementation
 * Time complexity: Average O(n log n), Worst O(n²)
 * Space complexity: O(log n)
 */
function quickSort(array, left = 0, right = array.length - 1) {
  // Base condition: when the subarray size is 1 or less
  if (left >= right) {
    return;
  }

  // Pivot selection and partitioning process
  const pivotIndex = partition(array, left, right);

  // Recursively sort the two subarrays based on the pivot
  quickSort(array, left, pivotIndex - 1);
  quickSort(array, pivotIndex + 1, right);

  return array;
}

function partition(array, left, right) {
  // Implementation details
}
```

## 4. Practical Comment Writing Guidelines

Practical guidelines for effective comment writing are as follows:

1. **Start with design comments before writing code**

   - Write comments about the function or module's purpose, input/output, and constraints before implementation
   - This helps find logical errors during the design phase
2. **Maintain consistency between comments and code**

   - Update related comments whenever code is changed
   - Outdated comments can hinder code understanding
3. **Focus on the 'Why'**

   - Code itself should make clear what it does
   - Comments should focus on why it was implemented that way
4. **Document boundary conditions and exceptions**

   - Use comments to explain special cases or constraints that the code handles
   - Reduce risks when future developers modify the code

## 5. Conclusion

Effective code writing and comment usage in JavaScript directly impact code readability, maintainability, and team collaboration efficiency. The best code is understandable without comments, but appropriate comments are essential in complex systems and algorithms.

Effective comments provide intent and context that are difficult to express in code alone, playing an important role especially in API documentation, architecture explanation, and explaining the rationale for non-intuitive solutions. Remember that comments are a means of communication with other developers and a record for your future self.

## References

[^1]: Mozilla Developer Network. "JavaScript Statements." MDN Web Docs. <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements>

[^2]: Mozilla Developer Network. "Automatic Semicolon Insertion." MDN Web Docs. <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion>

[^3]: Wulf, D. S., & Bertacchini, F. (2022). "Measuring Comment Quality in Software Development Projects." IEEE Transactions on Software Engineering, 48(1), 106-121.

[^4]: Martin, R. C. (2008). Clean Code: A Handbook of Agile Software Craftsmanship. Prentice Hall.

[^5]: JSDoc. "Using JSDoc." <https://jsdoc.app/>

[^6]: JavaScript.info. "Code structure." <https://javascript.info/structure>

[^7]: JavaScript.info. "Comments." <https://javascript.info/comments>
