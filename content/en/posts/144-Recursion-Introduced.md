---
title: "Recursion Introduced"
date: 2024-05-27T19:56:41+09:00
slug: "144-Recursion-Introduced"
original_url: "https://memoryhub.tistory.com/144"
tistory_id: 144
draft: false
---

*Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem, typically used to break down complex problems into simpler sub-problems.*

### The Big Picture

Imagine you are looking at yourself in a series of mirrors that are facing each other. The image in each mirror reflects infinitely, getting smaller and smaller. Similarly, recursion involves a function calling itself, each time working on a smaller version of the original problem until a base condition is met.

### Core Concepts

1. **Base Case**: The condition under which the recursion stops. Without a base case, the function would call itself indefinitely, leading to a stack overflow.
2. **Recursive Case**: The part of the function where the recursion happens, i.e., the function calls itself with a smaller or simpler argument.

### Detailed Walkthrough

Let's break down recursion using an example: calculating the factorial of a number.

#### Factorial Example

The factorial of a number ( n ) (denoted as ( n! )) is the product of all positive integers less than or equal to ( n ).

[ n! = n \times (n-1) \times (n-2) \times \cdots \times 1 ]

#### Step-by-Step Explanation

1. **Base Case**:

   - If ( n = 1 ), then ( 1! = 1 ).
   - This stops the recursion since the factorial of 1 is defined and does not need further recursive calls.
2. **Recursive Case**:

   - For ( n > 1 ), the factorial of ( n ) can be defined as:  
     [ n! = n \times (n-1)! ]
   - This means to calculate ( n! ), you multiply ( n ) by the factorial of ( (n-1) ).

Here's how the function would look in Python:

```
def factorial(n):
    if n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case
```

When you call `factorial(5)`, the following happens:

- `factorial(5)` calls `factorial(4)`
- `factorial(4)` calls `factorial(3)`
- `factorial(3)` calls `factorial(2)`
- `factorial(2)` calls `factorial(1)`
- `factorial(1)` returns `1`
- `factorial(2)` returns `2 * 1 = 2`
- `factorial(3)` returns `3 * 2 = 6`
- `factorial(4)` returns `4 * 6 = 24`
- `factorial(5)` returns `5 * 24 = 120`

### Understanding Through an Example

Let's consider another example: calculating the nth Fibonacci number. The Fibonacci sequence is defined as:

[ F(n) = F(n-1) + F(n-2) ]  
[ F(0) = 0, F(1) = 1 ]

Here's the recursive function in Python:

```
def fibonacci(n):
    if n == 0:  # Base case
        return 0
    elif n == 1:  # Base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive case
```

### Conclusion and Summary

Recursion simplifies complex problems by breaking them down into smaller, manageable sub-problems. Key components include the base case to stop the recursion and the recursive case where the function calls itself. Understanding recursion involves recognizing how the function reduces the problem at each step until reaching the base case.

### Test Your Understanding

1. What is the base case in recursion, and why is it important?
2. Explain the recursive case in the context of the factorial example.
3. Can you write a recursive function to sum all the numbers in a list?

### Reference

- "Structure and Interpretation of Computer Programs" by Harold Abelson and Gerald Jay Sussman
- [Khan Academy: Recursion](https://www.khanacademy.org/computing/computer-science/algorithms/recursive-algorithms/a/recursion)
