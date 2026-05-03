---
title: "Bitwise XOR Introduced"
date: 2024-06-06T07:35:44+09:00
slug: "201-Bitwise-XOR-Introduced"
original_url: "https://memoryhub.tistory.com/201"
tistory_id: 201
draft: false
categories: ["데브 라이브러리"]
tags: ["DS And Algorithm"]
---

*In this explanation, we will explore the concept of Bitwise XOR, starting with a big-picture analogy, followed by core concepts, a detailed walkthrough, an example, a conclusion, and a test to gauge understanding.*

### The Big Picture

Imagine you have two sets of light switches, A and B. Each switch can be either ON or OFF. You want to create a new set of light switches, C, where each switch in C is ON if the corresponding switches in A and B are in different states (one ON and one OFF), and OFF if they are in the same state (both ON or both OFF). This operation of combining switches based on their states is analogous to the Bitwise XOR operation in binary numbers.

### Core Concepts

- **Bitwise Operation**: An operation that acts on binary digits (bits) at the individual bit level.
- **XOR (Exclusive OR)**: A binary operation that outputs true (1) if the inputs are different, and false (0) if the inputs are the same.

### Detailed Walkthrough

#### XOR Truth Table

The XOR operation works according to the following truth table:

| A | B | A XOR B |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

#### Properties of XOR

1. **Self-Inverse**: A XOR A = 0. This means that XOR-ing a number with itself results in 0.
2. **Identity**: A XOR 0 = A. This means that XOR-ing a number with 0 leaves the number unchanged.
3. **Commutative**: A XOR B = B XOR A. The order of operands does not matter.
4. **Associative**: A XOR (B XOR C) = (A XOR B) XOR C. Grouping of operations does not matter.

### Understanding Through an Example

Let's take two 4-bit binary numbers:

- A = 1101
- B = 1011

Performing the XOR operation bit by bit:

- 1 XOR 1 = 0
- 1 XOR 0 = 1
- 0 XOR 1 = 1
- 1 XOR 1 = 0

Result: A XOR B = 0110

#### Step-by-Step Calculation:

1. First bit: 1 XOR 1 = 0
2. Second bit: 1 XOR 0 = 1
3. Third bit: 0 XOR 1 = 1
4. Fourth bit: 1 XOR 1 = 0

Final result: 0110

### Practical Applications

1. **Data Encryption**: XOR is used in simple encryption algorithms due to its reversible property.
2. **Checksum Calculations**: XOR helps in detecting errors in data transmission.
3. **Bitwise Manipulations**: XOR can be used to toggle specific bits in binary data.

### Conclusion and Summary

Bitwise XOR is a fundamental binary operation that compares two bits and outputs 1 if they are different and 0 if they are the same. Its properties, such as being self-inverse and having an identity element, make it useful in various computational tasks, from encryption to error detection.

### Test Your Understanding

1. What is the result of XOR-ing any number with itself?
2. How does the commutative property of XOR simplify operations?
3. Write a Python function to perform a bitwise XOR on two integers.

### Reference

For further reading on Bitwise XOR operations, you can refer to:

- [GeeksforGeeks on Bitwise Operators](https://www.geeksforgeeks.org/bitwise-operators-in-c-cpp/)
- [Khan Academy on Binary Operations](https://www.khanacademy.org/computing/computer-science/cryptography/modern-crypt/v/bitwise-operators)
