---
title: "Blockchain Introduced"
date: 2024-06-04T12:30:04+09:00
slug: "185-Blockchain-Introduced"
original_url: "https://memoryhub.tistory.com/185"
tistory_id: 185
draft: false
---

*Blockchain technology is a decentralized digital ledger that records transactions across many computers in a way that the registered transactions cannot be altered retroactively.*

---

### The Big Picture

Imagine a notebook that multiple people can write in simultaneously, but no one can erase or alter anything that's already been written. Each page of this notebook is a "block," and the entire notebook is the "chain." This is essentially what blockchain technology is—a chain of blocks, where each block contains a list of transactions. These blocks are linked and secured using cryptographic principles, making the data within them immutable and transparent.

### Core Concepts

1. **Decentralization**: Unlike traditional databases that are controlled by a single entity, blockchains are decentralized and distributed across a network of computers (nodes). Each node has a copy of the entire blockchain.
2. **Immutability**: Once a transaction is recorded in a block and the block is added to the blockchain, it cannot be changed or deleted. This is enforced through cryptographic hashes that link each block to the previous one.
3. **Consensus Mechanisms**: To agree on the validity of transactions and the state of the blockchain, networks use consensus mechanisms like Proof of Work (PoW) or Proof of Stake (PoS).
4. **Transparency and Security**: All transactions are visible to all nodes in the network, promoting transparency. The cryptographic methods used ensure the security and integrity of the data.

### Detailed Walkthrough

#### 1. **Decentralization**

In a centralized system, a single entity (like a bank) holds all the data and verifies transactions. In a decentralized system, many nodes participate in verifying and recording transactions. This makes the system more resilient to failures and attacks.

**Analogy**: Imagine a single library (centralized) versus multiple libraries in different cities (decentralized). If the single library burns down, all the books are lost. But if one library in the decentralized system burns down, the books are still available in the other libraries.

#### 2. **Immutability**

Each block contains a list of transactions and a unique code called a hash. A block also contains the hash of the previous block, linking them together. If someone tries to alter a transaction in a block, the hash would change, breaking the chain and alerting the network.

**Analogy**: Think of a chain of paper rings. Each ring represents a block. If you change one ring, it breaks the chain.

#### 3. **Consensus Mechanisms**

- **Proof of Work (PoW)**: Nodes (miners) solve complex mathematical problems to validate transactions and create new blocks. This process requires significant computational power and energy.

  **Analogy**: It’s like a Sudoku puzzle where the first person to solve it gets a reward, and the puzzle solution is added to the ledger.
- **Proof of Stake (PoS)**: Validators are chosen to create new blocks based on the number of coins they hold and are willing to "stake" as collateral. This is more energy-efficient than PoW.

  **Analogy**: Imagine a lottery where the more tickets (coins) you have, the higher your chances of being picked to validate a transaction and earn a reward.

#### 4. **Transparency and Security**

All transactions are publicly recorded on the blockchain, but the identities of the participants are anonymized through cryptographic addresses. Security is maintained by cryptographic algorithms that make it extremely difficult to alter the data.

**Analogy**: It’s like a public bulletin board where everyone can see the messages posted, but only the person with the right key can post or read the original message.

### Understanding Through an Example

Let's walk through a simple example of a Bitcoin transaction:

1. Alice wants to send 1 Bitcoin to Bob.
2. Alice's transaction is broadcast to the Bitcoin network.
3. Nodes in the network verify the transaction using a consensus mechanism (e.g., PoW).
4. Once verified, the transaction is added to a new block.
5. The new block is added to the blockchain, making the transaction permanent and visible to all nodes.
6. Bob receives the Bitcoin, and the blockchain is updated to reflect the new state.

### Conclusion and Summary

Blockchain technology is a decentralized, immutable, transparent, and secure way of recording transactions. It uses cryptographic techniques to ensure the integrity of the data and consensus mechanisms to agree on the state of the blockchain. By distributing the ledger across many nodes, it provides resilience against attacks and failures.

### Test Your Understanding

1. How does blockchain ensure the immutability of transactions?
2. What are the main differences between Proof of Work and Proof of Stake?
3. How does decentralization enhance the security and reliability of a blockchain?

Feel free to ask if you need further clarification on any of these points!

### Reference

For further learning, check out [Bitcoin's white paper by Satoshi Nakamoto](https://bitcoin.org/bitcoin.pdf), which laid the foundation for modern blockchain technology.
