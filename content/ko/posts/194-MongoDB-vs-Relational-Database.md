---
title: "MongoDB vs Relational Database"
date: 2024-06-06T07:14:44+09:00
slug: "194-MongoDB-vs-Relational-Database"
original_url: "https://memoryhub.tistory.com/194"
tistory_id: 194
draft: false
categories: ["데브 데이터베이스"]
tags: ["MongoDB"]
---

*MongoDB stores data in a flexible, JSON-like format called BSON (Binary JSON), unlike traditional relational databases that use tables with fixed schemas.*

### The Big Picture

Imagine two different ways of organizing information about people in a city. One way is like a grid where every row is a person and every column is a specific attribute (name, age, address). This is a traditional relational database. The other way is like a collection of personal files where each file contains information about a person, and each file can have different kinds of information. This is MongoDB.

### Core Concepts

1. **Traditional Relational Databases**:

   - **Tables**: Data is organized into tables with rows and columns.
   - **Schema**: Each table has a fixed schema, meaning each row in a table has the same set of columns.
   - **SQL**: Structured Query Language (SQL) is used for querying and managing data.
2. **MongoDB**:

   - **Collections**: Data is stored in collections, which are like folders.
   - **Documents**: Each collection contains documents, which are like files. Each document is a JSON-like object (BSON).
   - **Flexible Schema**: Documents in the same collection can have different structures.

### Detailed Walkthrough

1. **Relational Database Structure**:

   - **Tables and Rows**: Think of it like a spreadsheet. Each table represents an entity (e.g., customers, orders), and each row represents a record.
   - **Columns and Schema**: The table has a predefined set of columns, and every record must conform to this schema.
   - **Relationships**: Tables can be related through foreign keys, allowing complex queries across multiple tables.
2. **MongoDB Structure**:

   - **Collections and Documents**: Collections are like folders, and documents are like individual files inside those folders. Each document can store data in a nested, hierarchical structure.
   - **BSON Format**: Documents are stored in BSON format, which is a binary representation of JSON, allowing for more efficient storage and retrieval.
   - **Schema Flexibility**: Unlike tables, collections do not enforce a schema. Each document can have different fields, types, and structures.

### Understanding Through an Example

Imagine you have a database to store information about books and authors.

**Relational Database**:

- **Books Table**:
  - Columns: `BookID`, `Title`, `AuthorID`, `PublishedYear`
  - Each row must have values for these columns.
- **Authors Table**:
  - Columns: `AuthorID`, `Name`, `BirthYear`
  - Each row must have values for these columns.
- **Relationships**: `AuthorID` in the Books table links to `AuthorID` in the Authors table.

**MongoDB**:

- **Books Collection**:
  - Document 1: `{ "title": "Book Title 1", "author": { "name": "Author Name", "birthYear": 1970 }, "publishedYear": 2020 }`
  - Document 2: `{ "title": "Book Title 2", "author": "Author Name", "publishedYear": 2019, "genres": ["Fiction", "Mystery"] }`
  - Notice how Document 1 and Document 2 have different structures. Document 1 embeds the author information directly, while Document 2 references it as a simple string and includes an additional `genres` field.

### Conclusion and Summary

MongoDB offers a flexible, document-oriented approach to data storage, allowing each record (document) to have a different structure and enabling easier representation of complex data. This contrasts with traditional relational databases, which require a fixed schema and organize data into tables with rows and columns. This flexibility makes MongoDB particularly suitable for applications that deal with diverse and evolving data structures.

### Test Your Understanding

1. How does the structure of documents in MongoDB allow for flexibility compared to the rows in a relational database table?
2. What are the benefits of using a flexible schema like in MongoDB?
3. How would you represent a one-to-many relationship in MongoDB versus a relational database?

### Reference

- [MongoDB vs. Relational Databases](https://www.mongodb.com/compare/mongodb-vs-sql-databases)
