---
title: "RSA Introduced"
date: 2024-06-04T12:34:28+09:00
slug: "187-RSA-Introduced"
original_url: "https://memoryhub.tistory.com/187"
tistory_id: 187
draft: false
---

*RSA is a cryptographic algorithm used to securely transmit messages and authenticate digital signatures by leveraging the mathematical properties of prime numbers.*

### The Big Picture

Imagine you have a locked box (the message) and you want to send it to a friend without anyone else being able to open it. RSA (Rivest-Shamir-Adleman) is like a method where only your friend can have the key to unlock that box, even though the box can be seen by anyone.

### Core Concepts

1. **Public Key and Private Key**: RSA uses two keys—a public key (which everyone can see) and a private key (which is kept secret). The public key locks (encrypts) the message, and only the private key can unlock (decrypt) it.
2. **Prime Numbers**: The security of RSA relies on the difficulty of factoring large numbers into their prime components.
3. **Modular Arithmetic**: RSA operates in a mathematical system where numbers wrap around after reaching a certain value (modulus).

### Detailed Walkthrough

1. **Key Generation**:

   - Choose two large prime numbers, ( p ) and ( q ).
   - Calculate their product, ( n = p \times q ). This ( n ) is part of the public key.
   - Calculate the totient, ( \phi(n) = (p-1) \times (q-1) ).
   - Choose an integer ( e ) such that ( 1 < e < \phi(n) ) and ( e ) is coprime to ( \phi(n) ). This ( e ) is also part of the public key.
   - Calculate ( d ) such that ( d \times e \equiv 1 \mod \phi(n) ). This ( d ) is the private key.
2. **Encryption**:

   - Convert the message ( M ) into an integer ( m ) such that ( 0 < m < n ).
   - Compute the ciphertext ( c ) using the public key ( (e, n) ): ( c \equiv m^e \mod n ).
3. **Decryption**:

   - Use the private key ( (d, n) ) to compute ( m ): ( m \equiv c^d \mod n ).
   - Convert the integer ( m ) back to the original message ( M ).

### Understanding Through an Example

1. **Key Generation**:

   - Let's choose ( p = 61 ) and ( q = 53 ).
   - Compute ( n = 61 \times 53 = 3233 ).
   - Compute ( \phi(n) = (61-1) \times (53-1) = 3120 ).
   - Choose ( e = 17 ) (common choice as it's often small and coprime with 3120).
   - Calculate ( d ) such that ( 17 \times d \equiv 1 \mod 3120 ). Here, ( d = 2753 ).
2. **Encryption**:

   - Convert message "HELLO" to integer (let's simplify this to a single integer for illustration, say ( m = 65 )).
   - Compute ciphertext: ( c \equiv 65^{17} \mod 3233 ), which results in ( c = 2790 ).
3. **Decryption**:

   - Use private key to compute ( m ): ( m \equiv 2790^{2753} \mod 3233 ), which results in ( m = 65 ).
   - Convert ( m ) back to "HELLO".

### Conclusion and Summary

RSA is a method for secure communication that relies on two keys: one public and one private. It involves selecting large prime numbers, performing modular arithmetic, and leveraging the difficulty of prime factorization. This ensures that while anyone can encrypt a message using the public key, only the holder of the private key can decrypt it.

### Test Your Understanding

1. Why is it difficult for an attacker to determine the private key if they only know the public key?
2. What is the role of prime numbers in RSA?
3. Explain how modular arithmetic is used in RSA encryption and decryption.

### Reference

- "Introduction to Modern Cryptography" by Jonathan Katz and Yehuda Lindell
- RSA Algorithm: <https://en.wikipedia.org/wiki/RSA_(cryptosystem)>
