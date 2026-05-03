---
title: "Oracle DBMS Introduced"
date: 2024-05-28T12:18:25+09:00
slug: "107-Oracle-DBMS-Introduced"
original_url: "https://memoryhub.tistory.com/107"
tistory_id: 107
draft: false
categories: ["데브 데이터베이스"]
tags: ["Oracle"]
---

*Oracle DBMS (Database Management System) is a robust software suite that facilitates the creation, management, and interaction with databases, allowing users to store, retrieve, and manipulate data efficiently.*

### The Big Picture

Imagine a library where all the books (data) are meticulously organized and indexed so that you can find any book you need quickly. An Oracle DBMS is like the librarian who manages this library, ensuring that books are stored properly, easily accessible, and kept up-to-date. It's a comprehensive system that allows users to interact with the data seamlessly.

### Core Concepts

1. **Database**: A collection of structured information or data, typically stored electronically.
2. **SQL (Structured Query Language)**: A language used to interact with the database, enabling tasks like querying data, updating records, and managing database objects.
3. **Instance**: The set of Oracle software processes and memory structures that manage the database files.
4. **Schema**: A collection of database objects associated with a particular user, including tables, views, indexes, and procedures.
5. **Tablespace**: Logical storage units within an Oracle database, grouping related logical structures together.
6. **PL/SQL (Procedural Language/SQL)**: Oracle's procedural extension for SQL, allowing the creation of complex queries, functions, and procedures.

### Detailed Walkthrough

1. **Database Architecture**:

   - **Physical and Logical Storage**: The physical storage is where data files reside, while logical storage is how data is organized within the database.
   - **Tables and Indexes**: Tables are collections of related data entries, while indexes are used to speed up data retrieval.
2. **Instance Components**:

   - **Memory Structures**: Includes the System Global Area (SGA) and Program Global Area (PGA).
     - **SGA**: Shared by all server and background processes, it stores data and control information for the Oracle instance.
     - **PGA**: Private to each server process, it contains data and control information exclusive to that process.
   - **Background Processes**: Includes processes like DBWn (Database Writer), LGWR (Log Writer), CKPT (Checkpoint), and others that handle various tasks necessary for database operation.
3. **Transaction Management**:

   - **ACID Properties**: Ensures reliable processing of database transactions (Atomicity, Consistency, Isolation, Durability).
   - **Rollback and Commit**: Mechanisms to either save or undo changes made during transactions.
4. **Backup and Recovery**:

   - **RMAN (Recovery Manager)**: A tool for backup and recovery of the database.
   - **Archiving**: Ensures that the transaction logs are saved for recovery purposes.
5. **Security**:

   - **User Authentication**: Verifies the identity of users.
   - **Privileges and Roles**: Controls what users can and cannot do within the database.

### Understanding Through an Example

Imagine you own a bookstore, and you want to track your inventory, sales, and customers. You can use an Oracle DBMS to create a database for your bookstore.

- **Tables**: You create tables for books, customers, and sales.
- **SQL**: You use SQL to add new books, record sales, and retrieve customer purchase history.
- **Indexes**: You create indexes on the book titles and customer names to speed up search queries.
- **PL/SQL**: You write PL/SQL procedures to automatically update stock levels and generate sales reports.
- **Backup and Recovery**: You use RMAN to backup your data daily, ensuring you can recover your database in case of a failure.

### Conclusion and Summary

Oracle DBMS is a sophisticated system designed to handle large amounts of data efficiently and securely. It supports a variety of tasks from basic data entry to complex transaction processing and recovery. Key components include the database itself, SQL for interaction, memory structures, and transaction management processes. Understanding its architecture and functionality is crucial for effectively managing and utilizing data.

### Test Your Understanding

1. What are the key components of an Oracle instance?
2. Explain the difference between physical and logical storage in Oracle DBMS.
3. What are ACID properties and why are they important in a database system?
4. How does Oracle ensure data recovery in case of a failure?

### Reference

For more detailed information, you can refer to the official Oracle documentation: [Oracle Database Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/).
