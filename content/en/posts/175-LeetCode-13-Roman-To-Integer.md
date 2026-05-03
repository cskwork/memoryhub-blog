---
title: "LeetCode - 13. Roman To Integer"
date: 2024-06-01T22:04:53+09:00
slug: "175-LeetCode-13-Roman-To-Integer"
original_url: "https://memoryhub.tistory.com/175"
tistory_id: 175
draft: false
---

*To convert a Roman numeral to an integer in Python, we'll use a dictionary to map Roman symbols to their integer values and process the string from left to right while handling the special subtraction cases.*

### The Big Picture

The task involves converting a string representation of a Roman numeral into its corresponding integer value. Roman numerals use combinations of seven symbols (I, V, X, L, C, D, M) where subtraction is used for certain cases like IV (4) and IX (9).

### Core Concepts

1. **Mapping Symbols to Values**: Use a dictionary to store the values of Roman numeral symbols.
2. **Iterate Through String**: Loop through the string, adding or subtracting values based on the symbol's position and its neighboring symbols.
3. **Subtraction Cases**: Identify when a symbol is placed before a larger symbol to handle the subtraction case correctly.

### Detailed Walkthrough

Let's break down how the `roman_to_int` function converts a Roman numeral string into an integer.

1. **Dictionary Initialization:**

   ```
    roman_to_int = {
        'I': 1,
   ```
