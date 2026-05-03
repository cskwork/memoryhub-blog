---
title: "Hibernate Introduced"
date: 2024-05-28T10:07:38+09:00
slug: "147-Hibernate-Introduced"
original_url: "https://memoryhub.tistory.com/147"
tistory_id: 147
draft: false
categories: ["Dev Framework"]
tags: ["Spring"]
---

*Hibernate is a framework that simplifies the interaction between Java applications and relational databases by providing a powerful object-relational mapping (ORM) solution, making database operations more intuitive and less error-prone.*

### The Big Picture

Imagine you have a library with thousands of books, each with different attributes like title, author, and publication year. If you wanted to manage this library with a computer program, you'd need a way to store and retrieve information about the books efficiently. Hibernate helps you do this by bridging the gap between your Java objects (like your book objects) and the database where this information is stored.

### Core Concepts

1. **Object-Relational Mapping (ORM):** This is the technique Hibernate uses to map Java objects to database tables. It allows you to manipulate data in the database using Java objects without writing complex SQL queries.
2. **Session:** In Hibernate, a session is a connection between the application and the database. It is used to execute CRUD (Create, Read, Update, Delete) operations.
3. **Transaction:** Transactions in Hibernate ensure that a series of operations are executed as a single unit. This means either all operations succeed, or none do, maintaining data integrity.
4. **Configuration:** Hibernate requires configuration files to connect to the database and define mappings between Java classes and database tables.
5. **Query Language (HQL):** Hibernate provides its own query language, HQL, which is similar to SQL but operates on Java objects rather than database tables.

### Detailed Walkthrough

#### Object-Relational Mapping (ORM)

- **Java Classes and Database Tables:** Hibernate maps each Java class to a corresponding table in the database. For example, if you have a `Book` class in Java, Hibernate can map it to a `books` table in your database.
- **Attributes and Columns:** Each attribute of the Java class corresponds to a column in the database table. For instance, the `title` attribute of the `Book` class maps to a `title` column in the `books` table.

#### Session and Transaction

- **Session:** A session is created from a `SessionFactory`, which is configured using Hibernate's configuration files. This session is used to perform database operations.
- **Transaction:** A transaction is started from the session. You can perform multiple operations within a transaction, and if anything goes wrong, you can roll back the entire transaction to ensure the database remains consistent.

#### Configuration

- **Hibernate Configuration File (hibernate.cfg.xml):** This file contains database connection settings, such as URL, username, and password, as well as Hibernate-specific settings like dialect (which specifies the type of database you are using).
- **Mapping Files:** These XML files define the mappings between Java classes and database tables. Alternatively, you can use annotations in your Java classes to specify these mappings.

#### HQL (Hibernate Query Language)

- **HQL:** Hibernate's query language, HQL, is similar to SQL but it works with Java objects instead of database tables. For example, to fetch all books by a specific author, you might write:

  ```
  String hql = "FROM Book WHERE author = :authorName";
  Query query = session.createQuery(hql);
  query.setParameter("authorName", "J.K. Rowling");
  List<Book> books = query.list();
  ```

### Understanding Through an Example

Let's say we have a `Book` class:

```
@Entity
@Table(name = "books")
public class Book {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "title")
    private String title;

    @Column(name = "author")
    private String author;

    // Getters and setters
}
```

Here's how you might use Hibernate to save a new book to the database:

```
Session session = sessionFactory.openSession();
Transaction transaction = session.beginTransaction();

Book book = new Book();
book.setTitle("Harry Potter and the Philosopher's Stone");
book.setAuthor("J.K. Rowling");

session.save(book);
transaction.commit();
session.close();
```

### Conclusion and Summary

Hibernate simplifies database interactions in Java applications by using ORM to map Java classes to database tables. Sessions and transactions help manage the lifecycle and integrity of database operations. Configuration files or annotations specify how these mappings should be done, while HQL allows querying the database using Java object-oriented syntax.

### Test Your Understanding

1. What is Object-Relational Mapping (ORM) in Hibernate?
2. How does a Hibernate session differ from a transaction?
3. Explain the purpose of the Hibernate configuration file.
4. Write a simple HQL query to fetch all books published by "George Orwell".

### Reference

For further learning, you can refer to the official Hibernate documentation: [Hibernate ORM Documentation](https://hibernate.org/orm/documentation/)
