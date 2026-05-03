---
title: "SHA Introduced"
date: 2024-06-04T12:35:06+09:00
slug: "188-SHA-Introduced"
original_url: "https://memoryhub.tistory.com/188"
tistory_id: 188
draft: false
categories: ["데브 컨셉"]
tags: ["Web Security"]
---

*SHA (Secure Hash Algorithm) is a family of cryptographic hash functions designed to securely process data into a fixed-size output that appears random.*

### The Big Picture

Imagine you have a huge pile of documents and you need a quick way to create a unique "fingerprint" for each document. SHA (Secure Hash Algorithm) creates such fingerprints, called hash values, that uniquely represent your documents. Even a tiny change in the document will produce a completely different fingerprint.

### Core Concepts

1. **Hash Function**: A process that takes an input (or 'message') and returns a fixed-size string of bytes.
2. **Fixed-size Output**: No matter the size of the input, the output hash is always the same size (e.g., SHA-256 always produces a 256-bit hash).
3. **Deterministic**: The same input will always produce the same output.
4. **Avalanche Effect**: A small change in the input drastically changes the output.
5. **Collision Resistance**: It’s infeasible to find two different inputs that produce the same output.

### Detailed Walkthrough

1. **Input Processing**: The input message is divided into fixed-size blocks.
2. **Initial State**: The algorithm starts with an initial state (a set of initial values).
3. **Compression Function**: Each block is processed through a compression function that mixes the data with the current state.
4. **Final Output**: After all blocks are processed, the final state is transformed into the hash value.

### Types of SHA

1. **SHA-1**: Produces a 160-bit hash value. It's no longer considered secure for many applications.
2. **SHA-2**: Includes SHA-224, SHA-256, SHA-384, and SHA-512, producing 224, 256, 384, and 512-bit hash values respectively.
3. **SHA-3**: A newer standard with similar hash sizes to SHA-2 but different internal algorithms.

### Understanding Through an Example

Let's say we use SHA-256 to hash the message "HELLO".

1. **Initial Message**: "HELLO"
2. **Padding**: The message is padded to ensure its length is a multiple of the block size (512 bits for SHA-256).
3. **Initial Hash Values**: SHA-256 starts with specific constants.
4. **Processing**:

   - The message is split into blocks.
   - Each block is processed through a series of logical functions and mixed with the current state.
5. **Final Hash**: The result after processing all blocks might look like: `185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969`

### Conclusion and Summary

SHA is a family of cryptographic hash functions used to produce fixed-size, unique fingerprints of data. These functions ensure data integrity by providing a way to detect changes to the original input, due to their deterministic nature, fixed-size output, and resistance to collisions.

### Test Your Understanding

1. Why is it important that a hash function exhibits the avalanche effect?
2. What are the differences between SHA-1, SHA-2, and SHA-3?
3. How does collision resistance contribute to the security of a hash function?

### Reference

- "Cryptography and Network Security" by William Stallings
- Secure Hash Algorithm: <https://en.wikipedia.org/wiki/Secure_Hash_Algorithm>
