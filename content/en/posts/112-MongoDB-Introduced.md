---
title: "MongoDB Introduced"
date: 2024-05-27T12:30:21+09:00
slug: "112-MongoDB-Introduced"
original_url: "https://memoryhub.tistory.com/112"
tistory_id: 112
draft: false
---

*MongoDB is a NoSQL database that stores data in flexible, JSON-like documents, making it different from traditional relational databases.*

### The Big Picture

Imagine you have a huge library where books are categorized not just by their title or author, but also by many other attributes like genre, publication year, and even specific keywords within the content. Each book can have its own unique set of attributes, and you can add or remove these attributes as you like without having to reorganize the entire library. This flexibility is what MongoDB offers for storing and managing data.

### Core Concepts

1. **Document-Oriented**: Instead of tables and rows, MongoDB uses documents and collections.
2. **Schema-Less**: Documents in a collection don't need to have the same structure.
3. **JSON-Like Documents**: Data is stored in BSON (Binary JSON), which supports more data types than JSON.
4. **Scalability**: Designed to scale out by distributing data across multiple servers.
5. **Indexes**: Supports secondary indexes to improve query performance.

### Detailed Walkthrough

#### Document-Oriented

In MongoDB, data is stored in documents, which are similar to JSON objects. Here's a simple example:

```
{
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Anytown"
    },
    "hobbies": ["reading", "hiking"]
}
```

A collection is a group of these documents, like a table in a relational database. However, unlike a table, the documents in a collection don't need to have the same set of fields.

#### Schema-Less

MongoDB collections are schema-less, meaning each document can have a different structure. For example, another document in the same collection might look like this:

```
{
    "name": "Jane Doe",
    "email": "jane@example.com",
    "membership": "premium"
}
```

This flexibility allows you to evolve your application's data model without requiring costly schema migrations.

#### JSON-Like Documents (BSON)

MongoDB stores data in BSON format, which is a binary representation of JSON-like documents. BSON extends JSON by adding additional data types, such as Date and Binary, that are not part of the JSON standard.

#### Scalability

MongoDB is designed to scale out. It supports horizontal scaling through a technique called sharding, where data is distributed across multiple servers. This makes it possible to handle large volumes of data and high traffic loads efficiently.

#### Indexes

Indexes in MongoDB are similar to those in relational databases. They can significantly improve the performance of queries. MongoDB supports various types of indexes, including single field, compound, multikey, geospatial, text, and hashed indexes.

### Understanding Through an Example

Consider a blogging platform where users can write and manage blog posts. In a traditional relational database, you might have tables for `Users`, `Posts`, and `Comments`. Each table has a fixed schema that you need to define upfront.

In MongoDB, you could have a `users` collection and a `posts` collection, where each document in the `posts` collection might look like this:

```
{
    "title": "My First Blog Post",
    "author": "John Doe",
    "content": "This is the content of the blog post.",
    "tags": ["introduction", "personal"],
    "comments": [
        {
            "author": "Jane Doe",
            "content": "Great post!"
        }
    ],
    "publishedAt": "2023-05-25T12:00:00Z"
}
```

Notice how each post document can embed an array of comments directly within it. This structure is much more flexible and allows you to store complex, related data together.

### Conclusion and Summary

MongoDB is a NoSQL, document-oriented database that offers flexibility, scalability, and powerful querying capabilities. It stores data in BSON format, supports schema-less collections, and is designed to handle large-scale, high-traffic applications efficiently.

### Test Your Understanding

1. **What is the main difference between MongoDB and traditional relational databases?**
2. **Explain the concept of schema-less collections in MongoDB.**
3. **How does MongoDB handle scalability?**
4. **What are some advantages of using BSON over JSON?**

### Reference

For further learning, refer to the official MongoDB documentation: [MongoDB Documentation](https://docs.mongodb.com/).
