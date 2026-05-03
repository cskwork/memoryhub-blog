---
title: "Python Loop String"
date: 2024-06-01T21:46:44+09:00
slug: "174-Python-Loop-String"
original_url: "https://memoryhub.tistory.com/174"
tistory_id: 174
draft: false
---

*Let's explore how to loop through each character in a string in Python, using different methods to iterate over the characters.*

### The Big Picture

Looping through each character in a string is like examining each letter in a word one by one. This allows you to perform operations on each character, such as counting occurrences, transforming characters, or finding specific characters.

### Core Concepts

1. **For Loop**: The most common method to iterate over characters in a string.
2. **While Loop**: An alternative method using an index to access characters.
3. **Enumerate Function**: To get both the index and character during iteration.

### Detailed Walkthrough

#### Using a For Loop

The simplest and most common way to loop through each character in a string is using a `for` loop.

```
# Using a for loop to iterate through each character in a string
word = "Python"
```
