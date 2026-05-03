---
title: "PostgreSQL Introduced"
date: 2024-05-27T12:31:38+09:00
slug: "113-PostgreSQL-Introduced"
original_url: "https://memoryhub.tistory.com/113"
tistory_id: 113
draft: false
categories: ["Dev Database"]
tags: ["PostgreSQL"]
---

*PostgreSQL is a powerful, open-source object-relational database system known for its robustness, feature set, and extensibility.*

### The Big Picture

Imagine you have a giant library where all the books are perfectly organized, indexed, and can be accessed quickly by anyone who knows how to look for them. This library can store not just books, but any kind of document, audio, video, and even the metadata about these items. PostgreSQL is like this library, but for data. It's a database management system (DBMS) that helps you store, manage, and retrieve data efficiently.

### Core Concepts

1. **Database**: A collection of organized data that can be easily accessed, managed, and updated.
2. **Table**: Think of a table as a spreadsheet where data is stored in rows and columns.
3. **Row**: Each entry in a table, similar to a row in a spreadsheet.
4. **Column**: Each field in a table, similar to a column in a spreadsheet, representing a particular type of data.
5. **SQL (Structured Query Language)**: A language used to interact with the database. It includes commands for querying, inserting, updating, and deleting data.
6. **Relational Database**: A type of database that organizes data into tables which can be linked—or related—based on data they share.

### Detailed Walkthrough

#### Setting Up PostgreSQL

1. **Installation**: PostgreSQL can be installed on various operating systems, including Windows, macOS, and Linux. The installation process typically involves downloading the appropriate version from the official PostgreSQL website and following the setup instructions.
2. **Database Creation**: Once PostgreSQL is installed, you can create a database using the `createdb` command or through a graphical interface like pgAdmin. For example, in a command line, you might run:

   ```
   createdb mydatabase
   ```
3. **Connecting to the Database**: You can connect to your database using the `psql` command-line tool or through an application that supports PostgreSQL. For example:

   ```
   psql mydatabase
   ```

#### Basic SQL Commands

1. **Creating a Table**: To create a table, you define the columns and their data types. For example:

   ```
   CREATE TABLE books (
       id SERIAL PRIMARY KEY,
       title VARCHAR(100),
       author VARCHAR(100),
       published_date DATE
   );
   ```
2. **Inserting Data**: To add data to a table, you use the `INSERT` command:

   ```
   INSERT INTO books (title, author, published_date)
   VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', '1925-04-10');
   ```
3. **Querying Data**: To retrieve data, you use the `SELECT` command:

   ```
   SELECT * FROM books;
   ```
4. **Updating Data**: To modify existing data, you use the `UPDATE` command:

   ```
   UPDATE books
   SET author = 'Fitzgerald'
   WHERE id = 1;
   ```
5. **Deleting Data**: To remove data, you use the `DELETE` command:

   ```
   DELETE FROM books
   WHERE id = 1;
   ```

### Understanding Through an Example

Let's say you manage a library's catalog. You can create a PostgreSQL database to store information about the books, authors, and patrons. Each table will represent different entities in your library. For instance:

- **Books Table**: Stores details about each book.
- **Authors Table**: Stores details about authors.
- **Patrons Table**: Stores details about people who borrow books.

These tables can be related using foreign keys. For example, the `Books` table might have a foreign key that references the `Authors` table to indicate who wrote each book.

### Conclusion and Summary

PostgreSQL is a robust, open-source database management system that supports a wide range of data types and operations. It allows you to store, manage, and retrieve data efficiently using SQL. By understanding the basic concepts and commands, you can set up and interact with a PostgreSQL database to manage your data effectively.

### Test Your Understanding

1. What is a relational database, and how does PostgreSQL fit this definition?
2. Can you explain the difference between a row and a column in a PostgreSQL table?
3. Write a SQL command to create a table named `members` with columns for `id`, `name`, and `membership_date`.

### Reference

For further learning, refer to the [official PostgreSQL documentation](https://www.postgresql.org/docs/).
