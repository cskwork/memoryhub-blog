---
title: "MERN Stack Introduced"
date: 2024-06-06T07:13:22+09:00
slug: "193-MERN-Stack-Introduced"
original_url: "https://memoryhub.tistory.com/193"
tistory_id: 193
draft: false
---

*The MERN stack is a set of JavaScript-based technologies used to build full-stack web applications, comprising MongoDB, Express.js, React, and Node.js.*

### The Big Picture

Imagine building a web application like constructing a house. You need materials (data), a way to transport those materials, a structure to live in, and a person to manage everything. The MERN stack is like this, where:

- **MongoDB** is your building materials (data storage),
- **Express.js** is the transportation (backend framework),
- **React** is the structure (frontend framework),
- **Node.js** is the project manager (runtime environment).

### Core Concepts

1. **MongoDB**: A NoSQL database where data is stored in JSON-like documents.
2. **Express.js**: A web application framework for Node.js, handling HTTP requests and responses.
3. **React**: A JavaScript library for building user interfaces, especially single-page applications.
4. **Node.js**: A JavaScript runtime that allows you to run JavaScript on the server side.

### Detailed Walkthrough

1. **MongoDB**:

   - **Analogy**: Think of MongoDB as a huge filing cabinet where you store various documents (data records).
   - **Detail**: It stores data in flexible, JSON-like documents rather than traditional table-based relational databases, making it easier to scale and adapt.
2. **Express.js**:

   - **Analogy**: Express.js is like a delivery service that knows the best routes to take your building materials (data) from the warehouse (database) to the construction site (frontend).
   - **Detail**: It provides a simple interface to handle routing, requests, and middleware.
3. **React**:

   - **Analogy**: React is like the blueprints and construction methods used to build the rooms and features of your house (user interface).
   - **Detail**: It allows you to build complex UIs from small, reusable components, making your application easier to manage and develop.
4. **Node.js**:

   - **Analogy**: Node.js is the project manager who ensures everything runs smoothly by coordinating the backend operations and handling requests.
   - **Detail**: It uses an event-driven, non-blocking I/O model, making it efficient and suitable for building scalable network applications.

### Understanding Through an Example

Imagine you want to build a simple blog application using the MERN stack:

1. **MongoDB**: Stores blog posts as documents, each containing fields like title, content, author, and date.
2. **Express.js**: Handles routes like `/posts` to fetch all blog posts or `/posts/:id` to fetch a specific post.
3. **React**: Displays the blog posts to the user, allows them to create new posts, and updates the UI dynamically when new posts are added.
4. **Node.js**: Manages the server, processes API requests, and connects to the MongoDB database to fetch or store data.

### Conclusion and Summary

The MERN stack is a powerful and efficient way to build full-stack web applications entirely using JavaScript. Each component has a specific role: MongoDB for data storage, Express.js for backend routing and middleware, React for the user interface, and Node.js for server-side execution.

### Test Your Understanding

1. Can you explain how MongoDB stores data differently compared to a traditional relational database?
2. What are the main responsibilities of Express.js in the MERN stack?
3. How does React help in building user interfaces?
4. Why is Node.js suitable for handling backend operations in a web application?

### Reference

- [MERN Stack Documentation](https://www.mongodb.com/mern-stack)
