---
title: "Python Map(Dictionary) Manipulation"
date: 2024-06-01T21:38:47+09:00
slug: "173-Python-Map-Dictionary-Manipulation"
original_url: "https://memoryhub.tistory.com/173"
tistory_id: 173
draft: false
---

*Let's explore how to declare and use maps (dictionaries) in Python, which are collections of key-value pairs.*

### The Big Picture

A dictionary in Python is like a real-world dictionary, where you look up a word (key) and find its meaning (value). This allows you to store and retrieve data efficiently using meaningful keys.

### Core Concepts

1. **Dictionary Declaration**: How to create dictionaries in Python.
2. **Accessing and Modifying Elements**: How to work with dictionary entries.
3. **Adding and Removing Elements**: How to dynamically update dictionaries.

### Detailed Walkthrough

#### Dictionary Declaration

In Python, you create a dictionary by enclosing key-value pairs in curly braces `{}`, with each pair separated by a colon `:`.

```
# Declare a dictionary
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 88
}
```

*Analogy*: Think of a dictionary as a contact list on your phone, where each contact name (key) maps to a phone number (value).

#### Accessing and Modifying Elements

You can access the value associated with a key using the key in square brackets. To modify a value, you can assign a new value to an existing key.

```
# Accessing a value
alice_grade = student_grades["Alice"]
print(alice_grade)  # Output: 85

# Modifying a value
student_grades["Alice"] = 90
print(student_grades)  # Output: {'Alice': 90, 'Bob': 92, 'Charlie': 78, 'David': 88}
```

#### Adding and Removing Elements

You can add new key-value pairs or remove existing ones using the `del` keyword or `pop` method.

```
# Adding a new key-value pair
student_grades["Eve"] = 95
print(student_grades)  # Output: {'Alice': 90, 'Bob': 92, 'Charlie': 78, 'David': 88, 'Eve': 95}

# Removing a key-value pair by key
del student_grades["Charlie"]
print(student_grades)  # Output: {'Alice': 90, 'Bob': 92, 'David': 88, 'Eve': 95}

# Removing a key-value pair using pop
removed_grade = student_grades.pop("Bob")
print(removed_grade)  # Output: 92
print(student_grades)  # Output: {'Alice': 90, 'David': 88, 'Eve': 95}
```

### Understanding Through an Example

Let's create a dictionary to store the prices of different fruits and perform various operations on it.

```
# Dictionary of fruit prices
fruit_prices = {
    "apple": 1.2,
    "banana": 0.5,
    "cherry": 2.5,
    "date": 3.0
}

# Accessing the price of a banana
banana_price = fruit_prices["banana"]
print(f"The price of a banana is ${banana_price}")  # Output: The price of a banana is $0.5

# Modifying the price of a cherry
fruit_prices["cherry"] = 2.8
print(fruit_prices)  # Output: {'apple': 1.2, 'banana': 0.5, 'cherry': 2.8, 'date': 3.0}

# Adding a new fruit
fruit_prices["elderberry"] = 1.5
print(fruit_prices)  # Output: {'apple': 1.2, 'banana': 0.5, 'cherry': 2.8, 'date': 3.0, 'elderberry': 1.5}

# Removing a fruit by key
del fruit_prices["date"]
print(fruit_prices)  # Output: {'apple': 1.2, 'banana': 0.5, 'cherry': 2.8, 'elderberry': 1.5}

# Removing a fruit using pop
removed_price = fruit_prices.pop("banana")
print(removed_price)  # Output: 0.5
print(fruit_prices)  # Output: {'apple': 1.2, 'cherry': 2.8, 'elderberry': 1.5}
```

### Conclusion and Summary

We have covered how to declare and manipulate dictionaries (maps) in Python. Dictionaries are versatile data structures that allow you to store and manage key-value pairs efficiently.

### Test Your Understanding

1. Create a dictionary to store the capital cities of different countries.
2. Add a new country-capital pair to the dictionary.
3. Modify the capital of an existing country.
4. Remove a country from the dictionary using its key.
5. Access and print the capital of a specific country.

Feel free to try these exercises and let me know if you need any help!

### Reference

For more details, you can visit the official [Python Documentation on Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).
