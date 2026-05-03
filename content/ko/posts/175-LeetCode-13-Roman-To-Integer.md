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
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
   ```

   This dictionary maps each Roman numeral character to its corresponding integer value.
2. **Variable Initialization:**

   ```
    total = 0
    prev_value = 0
   ```

   `total` will hold the final integer value, and `prev_value` keeps track of the value of the previous Roman numeral character processed.
3. **Processing the Roman Numeral String in Reverse:**

   ```
    for char in reversed(s):
   ```

   The string `s` is reversed to handle Roman numeral subtraction rules more easily (e.g., IV = 4 is processed as VI where I < V).
4. **Character Processing:**

   ```
        value = roman_to_int[char]
   ```

   For each character in the reversed string, retrieve its integer value from the dictionary.
5. **Subtraction or Addition Logic:**

   ```
        if value < prev_value:
            total -= value
        else:
            total += value
   ```

   If the current value is less than the previous value (e.g., I before V), subtract it from `total`. Otherwise, add it to `total`.
6. **Update `prev_value`:**

   ```
        prev_value = value
   ```

   Update `prev_value` to the current value for the next iteration.
7. **Return the Result:**

   ```
    return total
   ```

### Examples

1. **"III":**
   - Reversed: "III"
   - Processing: 1 + 1 + 1 = 3
   - Output: 3
2. **"LVIII":**
   - Reversed: "IIIVL"
   - Processing: 1 + 1 + 1 + 5 + 50 = 58
   - Output: 58
3. **"MCMXCIV":**
   - Reversed: "VICXMCM"
   - Processing: 5 + 1 (5-1=4) + 10 + 100 (100-10=90) + 1000 + 100 (1000-100=900) = 1994
   - Output: 1994

### Understanding Through an Example

Let's take the string "MCMXCIV":

1. Start with the last character 'V' which is 5:
   - `total = 5`
2. Next character 'I' which is 1 (less than previous value 5):
   - `total = 5 - 1 = 4`
3. Next character 'C' which is 100 (greater than previous value 1):
   - `total = 4 + 100 = 104`
4. Next character 'X' which is 10 (less than previous value 100):
   - `total = 104 - 10 = 94`
5. Next character 'M' which is 1000 (greater than previous value 10):
   - `total = 94 + 1000 = 1094`
6. Next character 'C' which is 100 (less than previous value 1000):
   - `total = 1094 - 100 = 994`
7. Last character 'M' which is 1000 (greater than previous value 100):
   - `total = 994 + 1000 = 1994`

### Conclusion and Summary

By iterating through the string and applying the rules for Roman numerals, we can accurately convert a Roman numeral string to its integer equivalent. This method effectively handles both simple additions and the more complex subtraction cases.

### Test Your Understanding

Here's the complete Python function to achieve this:

```
def roman_to_int(s: str) -> int:
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_to_int[char]

        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total

# Examples
print(roman_to_int("III"))     # Output: 3
print(roman_to_int("LVIII"))   # Output: 58
print(roman_to_int("MCMXCIV")) # Output: 1994
```

### Reference

For more detailed information on Roman numerals and their rules, you can refer to the [Wikipedia page on Roman numerals](https://en.wikipedia.org/wiki/Roman_numerals).
