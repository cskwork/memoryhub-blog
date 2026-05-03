---
title: "Advanced Python Syntax (type hint)"
date: 2024-06-01T21:33:12+09:00
slug: "171-Advanced-Python-Syntax-type-hint"
original_url: "https://memoryhub.tistory.com/171"
tistory_id: 171
draft: false
---

*Let's explain the syntax and structure for the function definition `def romanToInt(self, s: str) -> int:` in Python, highlighting advanced syntax elements.*

### The Big Picture

Understanding advanced function definitions in Python, especially those involving type hints, is like mastering complex sentence structures in a language. It allows you to write clearer, more maintainable code and leverage the power of Python’s typing system.

### Core Concepts

1. **Function Definition**: How to define a function in Python.
2. **Method**: Understanding `self` in class methods.
3. **Type Hints**: Specifying the expected types of parameters and return values.
4. **Return Annotations**: Indicating the type of value a function returns.

### Detailed Walkthrough

#### Function Definition

The syntax `def function_name(parameters):` is used to define a function in Python. The function `romanToInt` is defined within a class and takes two parameters: `self` and `s`.

```
def romanToInt(self, s: str) -> int:
```

*Analogy*: Think of a function as a specific task you can call upon anytime, like a recipe for a dish. This recipe might require certain ingredients (parameters).

#### Method and `self`

In Python, functions defined within a class are called methods. The first parameter of a method is usually `self`, which refers to the instance of the class. It allows the method to access attributes and other methods of the class.

```
class RomanConverter:
    def romanToInt(self, s: str) -> int:
        # Method implementation
```

*Analogy*: `self` is like referring to "my" or "this" within a recipe book of a particular cuisine, allowing the recipe to refer to other recipes or ingredients in the same book.

#### Type Hints

Type hints provide a way to indicate the expected types of parameters and return values. They do not enforce type checking at runtime but help with code readability and debugging.

- `s: str` indicates that the parameter `s` should be a string.
- `-> int` indicates that the function should return an integer.

```
def romanToInt(self, s: str) -> int:
```

*Analogy*: Type hints are like labels on the ingredients list of a recipe, specifying that "flour" should be used as opposed to "sugar".

### Full Example with Implementation

Let's implement a class `RomanConverter` with the `romanToInt` method. This method will convert a Roman numeral string to an integer.

```
class RomanConverter:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        prev_value = 0

        for char in reversed(s):
            current_value = roman_to_int[char]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value

        return total

# Example usage:
converter = RomanConverter()
result = converter.romanToInt("XIV")
print(result)  # Output: 14
```

*Explanation*: This method:

1. Maps Roman numeral characters to their integer values.
2. Iterates over the string in reverse.
3. Adds or subtracts the value based on the previous numeral's value to handle cases like IV (4) and IX (9).

### Conclusion and Summary

We explored the advanced syntax involved in defining a function within a class with type hints and return annotations. This helps in writing clean, maintainable, and well-documented code.

### Test Your Understanding

1. Modify the `romanToInt` method to handle invalid Roman numerals by raising an exception if an invalid character is encountered.
2. Add a type hint to a function that takes a list of integers and returns a list of their squares.

Feel free to try these exercises and let me know if you need any help!

### Reference

For more details, you can visit the official [Python Documentation on Type Hints](https://docs.python.org/3/library/typing.html) and [Python Documentation on Classes](https://docs.python.org/3/tutorial/classes.html).
