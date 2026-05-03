---
title: "HashMap Introduced"
date: 2024-05-29T08:08:58+09:00
slug: "162-HashMap-Introduced"
original_url: "https://memoryhub.tistory.com/162"
tistory_id: 162
draft: false
categories: ["Dev Library"]
tags: ["DS And Algorithm"]
---

*In this response, we will explore what a hashmap is, using analogies to make the concept clear and understandable.*

### The Big Picture

Imagine you have a library with thousands of books, and you need a way to find any specific book quickly. Instead of searching through each shelf and book, you have a special catalog that tells you exactly where the book is located based on its title. This catalog allows you to jump directly to the correct shelf and spot. This is similar to how a hashmap works in programming.

### Core Concepts

A hashmap is a data structure that allows you to store data in key-value pairs, enabling very fast retrieval of values when you know the key. The core components of a hashmap include:

1. **Keys and Values**: Each piece of data (value) is associated with a unique identifier (key).
2. **Hash Function**: A function that takes a key and computes an index in an array, where the value associated with the key is stored.
3. **Buckets**: The array where values are stored. Each position in the array is called a bucket.
4. **Collisions**: Situations where different keys generate the same index. These are handled using techniques like chaining or open addressing.

### Detailed Walkthrough

1. **Keys and Values**:

   - Think of a key as a book title and the value as the location of the book in the library.
2. **Hash Function**:

   - A hash function takes the key (book title) and converts it into an index (shelf number). For instance, the title "Harry Potter" might be converted to the number 7, meaning you would look on shelf 7 for the book.
3. **Buckets**:

   - The buckets are the actual shelves where books are stored. Each bucket can hold multiple books in case of collisions.
4. **Collisions**:

   - If two book titles generate the same shelf number, they both go on the same shelf. To handle this, we might keep a list of books on each shelf, so you can still find "Harry Potter" and "Hobbit" on shelf 7, but they are listed one after the other.

### Understanding Through an Example

Let's walk through an example in Python to illustrate how a hashmap works:

```
# Define a simple hash function
def simple_hash(key, bucket_size):
    return hash(key) % bucket_size

# Create a hashmap with a fixed number of buckets
bucket_size = 10
hashmap = [[] for _ in range(bucket_size)]

# Function to insert a key-value pair
def insert(hashmap, key, value):
    index = simple_hash(key, bucket_size)
    bucket = hashmap[index]
    for kv in bucket:
        if kv[0] == key:
            kv[1] = value
            return
    bucket.append([key, value])

# Function to retrieve a value by key
def get(hashmap, key):
    index = simple_hash(key, bucket_size)
    bucket = hashmap[index]
    for kv in bucket:
        if kv[0] == key:
            return kv[1]
    return None

# Inserting key-value pairs
insert(hashmap, "Harry Potter", "Shelf 7")
insert(hashmap, "Hobbit", "Shelf 7")

# Retrieving values
print(get(hashmap, "Harry Potter"))  # Output: Shelf 7
print(get(hashmap, "Hobbit"))        # Output: Shelf 7
```

### Conclusion and Summary

A hashmap is like a special library catalog that lets you find books quickly by converting book titles (keys) into shelf numbers (indices) using a hash function. The books are stored on shelves (buckets), and when two books land on the same shelf, we handle this collision by keeping a list of books on that shelf.

### Test Your Understanding

1. What is a key in the context of a hashmap?
2. How does a hash function work, and why is it important?
3. What is a collision, and how can it be handled in a hashmap?
4. Can you write a Python function to delete a key-value pair from the hashmap?

### Reference

For further learning, you can explore detailed explanations and advanced topics related to hashmaps in data structures books such as "Introduction to Algorithms" by Cormen, Leiserson, Rivest, and Stein.
