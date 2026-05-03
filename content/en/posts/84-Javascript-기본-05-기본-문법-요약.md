---
title: "JavaScript Basics 05 - Basic Syntax Summary"
date: 2024-05-25T17:57:48+09:00
slug: "84-Javascript-기본-05-기본-문법-요약"
original_url: "https://memoryhub.tistory.com/84"
tistory_id: 84
draft: false
---

### Code structure

Multiple statements can be separated by semicolons:

```
alert('Hello'); alert('World');
```

Line breaks also separate multiple statements:

```
alert('Hello')
alert('World')
```

This behavior is called 'automatic semicolon insertion'. However, there are cases where automatic semicolon insertion doesn't work:

```
alert("An error will occur after this message is printed.")
[1, 2].forEach(alert)
```

> Most code style guidelines like coding conventions recommend placing a semicolon at the end of statements.

You don't need to add a semicolon at the end of code blocks ({...}) or syntax that works with code blocks (like loops):

```
function f() {
  // No semicolon needed at the end of function declarations.
}

for(;;) {
  // No semicolon needed at the end of loops.
}
```

Even if you add an 'extra' semicolon where it's not needed, it will be ignored, so no error occurs.

## Strict mode

To enable all modern JavaScript features, you must write 'use strict' at the top of your script:

```
'use strict';
...
```

'use strict' must be at the top of a script or at the top of a function body.  
Code works fine even without 'use strict'. However, it runs in the old way, not the modern way ('backward compatibility'). Some modern features like classes automatically enable strict mode.

## Variables

let - Variables are declared using the following keyword  
const – Defines a constant that cannot be changed once a value is assigned.  
var – A keyword used in the past (global variable).

### Variable naming rules

- Use numbers and letters, but the first character cannot be a number.
- Only $and _ can be used as special characters.
- Characters from non-Latin languages or pictographs can be used, but aren't common.
- JavaScript allows dynamic typing, so you can assign values with changing data types. TypeScript emerged as a syntax for pre-declaring types due to type issues.

### JavaScript's eight basic data types

- **Number type** – used to store integers and floating-point numbers
- **BigInt type** – can store very large numbers
- **String type** – used to store strings
- **Boolean type** – used to store logical values true/false
- **null** – an independent data type for the null value representing 'empty' or 'non-existent'
- **undefined** – an independent data type for the undefined value representing an uninitialized state
- **Object type** used to store complex data structures, and **Symbol type** used to create unique identifiers
- The typeof operator returns the data type of a value.

However, there are two exceptions:

```
typeof null == "object" // Language bug
typeof function(){} == "function" // Functions are treated specially.
```

## Interaction

When the host environment is a browser, you can interact with users using the following UI functions:

#### prompt(question, [default])

Shows the user a prompt dialog with the question parameter. Returns the value entered by the user when 'OK' is clicked, and null when 'Cancel' is clicked.

#### confirm(question)

Shows the user a confirm dialog with the question parameter. Returns true if the user clicks 'OK', false otherwise.

#### alert(message)

Shows an alert dialog containing the message.  
All three functions display modal windows. Code execution pauses until the modal window closes. Users cannot interact with anything on the page outside the modal window.

Example:

```
let userName = prompt("Please tell me your name.", "Alice");
let isTeaWanted = confirm("Would you like a cup of tea?");

alert( "Visitor: " + userName ); // Alice
alert( "Tea ordered: " + isTeaWanted ); // true
```

## Operators

JavaScript provides various operators:

#### Arithmetic operators

Operators related to basic arithmetic: \* + - /, the remainder operator %, and the exponentiation operator \*\* are typical arithmetic operators.

#### Binary addition operator

+ converts the other operand to a string and concatenates the two strings when one of the operands is a string:

```
alert( '1' + 2 ); // '12', string
alert( 1 + '2' ); // '12', string
```

#### Assignment operator

Assignment operators like a = b and compound assignment operators like a \*= 2.

#### Bitwise operators

Bitwise operators convert arguments to 32-bit integers and perform binary operations.

#### Conditional operator

The conditional operator is the only JavaScript operator with 3 parameters.  
Used in the form cond ? resultA : resultB,  
Returns resultA if cond is true, otherwise returns resultB.

#### Logical operators

The AND operator && and OR operator || perform short-circuit evaluation, returning the value at the point where evaluation stops  
(doesn't have to be true or false).  
The NOT operator ! converts the operand's data type to boolean and returns its negation.

#### Nullish coalescing operator

The nullish coalescing operator ?? is used to find the operand that actually has a defined value.  
If a is not null or undefined, the result of a ?? b is a; if a is null or undefined, the result of a ?? b is b.

#### Comparison operators

The equality operator == converts operands to numbers when comparing values of different types. null and undefined return true when compared with each other, but false when compared with other types:

```
alert( 0 == false ); // true
alert( 0 == '' ); // true
```

Other comparison operators < > <= >= also convert operands to numbers before comparison.

#### Strict equality operator

=== does not convert operand types. If types are different, it always evaluates as different.

null and undefined are special values. Comparing them with the == operator returns true, but comparing with other values always returns false.

When a string is an operand in a comparison operator for size, comparison is done character by character. When values of other types are entered, they are converted to numbers before comparison.

#### Other operators

There are other operators like the comma operator.

## Loops

while, do-while, and for statements can be written as follows:

```
// 1
while (condition) {
  ...
}

// 2
do {
  ...
} while (condition);

// 3
for(let i = 0; i < 10; i++) {
  ...
}
```

A variable declared inside for(let...) can only be used within the loop. You can also omit let and use an existing variable.

The break and continue statements are used to exit the entire loop or exit the current iteration. Labels are used to exit nested loops.

'switch' statement  
A 'switch' statement can be rewritten using an if statement. The 'switch' statement uses the strict equality operator === internally for comparison.

Example:

```
let age = prompt('Please tell me your age.', 18);

switch (age) {
  case 18:
    alert("Won't work"); // prompt always returns a string, so this case is never reached.
    break;

  case "18":
    alert("You're 18 years old!");
    break;

  default:
    alert("This doesn't match any case.");
}
```

## Functions

You can create functions in three ways:

**Function declaration**: Takes up the main code flow

```
function sum(a, b) {
  let result = a + b;

  return result;
}
```

**Function expression**: A function declared in expression form

```
let sum = function(a, b) {
  let result = a + b;

  return result;
};
```

**Arrow function**:

```
// Expression on the right side of the arrow (=>)
let sum = (a, b) => a + b;

// Using braces { ... } allows multiple lines of code in the body. A return statement is required.
let sum = (a, b) => {
  // ...
  return a + b;
}

// No parameters
let sayHi = () => alert("Hello");

// One parameter
let double = n => n * 2;
```

Functions can have local variables. Local variables are variables declared in the function body and can only be accessed inside the function.  
You can set default values for parameters:

Syntax:

```
function sum(a = 1, b = 2) {...}
```

Functions always return something. If there is no return statement, it returns undefined.

## References

<https://ko.javascript.info/javascript-specials>
