---
title: "RSA Key Cryptosystem Introduced"
date: 2024-05-31T09:10:51+09:00
slug: "163-RSA-Key-Cryptosystem-Introduced"
original_url: "https://memoryhub.tistory.com/163"
tistory_id: 163
draft: false
categories: ["데브 컨셉"]
tags: ["Web Security"]
---

*In this response, we will delve into what RSA is, explaining its core principles and functionality using analogies and technical details to make the concept clear and understandable.*

### The Big Picture

Imagine you have a secret message you want to send to a friend, but you don't want anyone else to read it. You put the message in a special lockbox and lock it with a key. However, this lockbox has a unique feature: it has two keys – one for locking (encryption) and one for unlocking (decryption). Only your friend has the key to unlock the box. This is the basic idea behind RSA (Rivest-Shamir-Adleman), a widely used public-key cryptosystem.

### Core Concepts

1. **Public and Private Keys**: In RSA, each user has a pair of keys – a public key (for encryption) and a private key (for decryption). The public key is shared with everyone, but the private key is kept secret.
2. **Prime Numbers**: RSA relies on the mathematical properties of prime numbers and the difficulty of factoring large numbers into their prime components.
3. **Encryption and Decryption**: The process of converting a message into an unreadable format using the public key (encryption) and converting it back to its original format using the private key (decryption).

### Detailed Walkthrough

1. **Generating Keys**:

   - Choose two large prime numbers, ( p ) and ( q ).
   - Compute their product ( n = p \times q ). The number ( n ) is used as the modulus for both the public and private keys.
   - Calculate the totient function ( \phi(n) = (p-1) \times (q-1) ).
   - Choose an integer ( e ) such that ( 1 < e < \phi(n) ) and ( e ) is coprime to ( \phi(n) ). The pair ((e, n)) is the public key.
   - Determine ( d ) as the modular multiplicative inverse of ( e ) modulo ( \phi(n) ). The pair ((d, n)) is the private key.
2. **Encryption**:

   - Convert the message into a number ( m ) such that ( 0 < m < n ).
   - Compute the ciphertext ( c ) using the formula ( c = m^e \mod n ).
3. **Decryption**:

   - Use the private key to compute ( m ) from ( c ) using the formula ( m = c^d \mod n ).

### Understanding Through an Example

Let's walk through an example to illustrate the RSA algorithm in Python:

```
from sympy import randprime, mod_inverse

# Step 1: Generate two large prime numbers (for simplicity, we use small primes)
p = randprime(10, 100)
q = randprime(10, 100)

# Step 2: Compute n and the totient φ(n)
n = p * q
phi_n = (p - 1) * (q - 1)

# Step 3: Choose e such that 1 < e < φ(n) and e is coprime to φ(n)
e = 65537  # Common choice for e

# Step 4: Compute d as the modular multiplicative inverse of e modulo φ(n)
d = mod_inverse(e, phi_n)

# Public key (e, n) and private key (d, n)
public_key = (e, n)
private_key = (d, n)

# Example message
message = 42  # This would be a number representing the plaintext

# Step 5: Encrypt the message
ciphertext = pow(message, e, n)

# Step 6: Decrypt the message
decrypted_message = pow(ciphertext, d, n)

print(f"Original message: {message}")
print(f"Encrypted message: {ciphertext}")
print(f"Decrypted message: {decrypted_message}")
```

### Conclusion and Summary

RSA is a public-key cryptosystem that allows secure communication by using a pair of keys: a public key for encryption and a private key for decryption. The security of RSA is based on the difficulty of factoring the product of two large prime numbers. This ensures that, even though the public key is known to everyone, only the holder of the private key can decrypt the message.

### Test Your Understanding

1. What are the main components of RSA key generation?
2. Why are prime numbers important in RSA?
3. How does the encryption process work in RSA?
4. Can you describe the decryption process in RSA?

### Reference

For further learning, you can explore detailed explanations and advanced topics related to RSA in cryptography books such as "Cryptography and Network Security" by William Stallings.
