---
title: "NodeJS Introduced"
date: 2024-06-06T07:18:28+09:00
slug: "196-NodeJS-Introduced"
original_url: "https://memoryhub.tistory.com/196"
tistory_id: 196
draft: false
---

*Node.js is a runtime environment that allows you to run JavaScript code on the server side, outside of a web browser.*

### The Big Picture

Think of JavaScript as a language typically spoken in browsers. Node.js is like giving JavaScript the ability to speak outside of the browser, letting it work on servers, computers, and other environments. This opens up a world of possibilities for using JavaScript to build server-side applications, like web servers or APIs.

### Core Concepts

1. **JavaScript Runtime**: Node.js allows JavaScript to run on the server side.
2. **Non-blocking I/O**: Node.js uses an event-driven, non-blocking I/O model, making it efficient and suitable for real-time applications.
3. **NPM (Node Package Manager)**: A vast ecosystem of open-source libraries and tools that you can easily integrate into your Node.js applications.
4. **V8 Engine**: The high-performance JavaScript engine developed by Google, which Node.js uses to execute JavaScript code.

### Detailed Walkthrough

1. **JavaScript Runtime**:

   - **Analogy**: Imagine JavaScript as a chef who has only been working in a pastry shop (the browser). Node.js lets this chef work in a full kitchen (server) where they can cook a variety of dishes (applications).
   - **Detail**: Node.js extends JavaScript's capabilities by providing server-side APIs like file system access, network communications, and more, enabling the development of backend applications.
2. **Non-blocking I/O**:

   - **Analogy**: Think of a restaurant where the chef can start cooking one dish, and while it's cooking, they can start preparing another dish without waiting. This makes the kitchen very efficient.
   - **Detail**: Node.js handles operations asynchronously. Instead of waiting for one operation to complete before starting another, it uses callbacks, promises, or async/await to handle multiple operations concurrently. This non-blocking approach is ideal for I/O-heavy tasks like web servers.
3. **NPM (Node Package Manager)**:

   - **Analogy**: NPM is like a massive library of pre-made recipes (packages) that chefs (developers) can use to quickly add functionality to their kitchen (application).
   - **Detail**: NPM hosts thousands of libraries and modules that can be easily installed and managed in your Node.js project. It helps in sharing and reusing code across the community.
4. **V8 Engine**:

   - **Analogy**: The V8 engine is like a high-performance blender that processes ingredients (JavaScript code) incredibly fast, making the kitchen (server) more efficient.
   - **Detail**: Developed by Google for Chrome, the V8 engine compiles JavaScript into native machine code, providing fast execution. Node.js leverages this engine to run JavaScript code efficiently on the server.

### Understanding Through an Example

Imagine you want to create a simple web server using Node.js:

1. **Setup Node.js**:

   ```
   mkdir myserver
   cd myserver
   npm init -y
   npm install express
   ```
2. **Create a Web Server**:

   ```
   // Import the Express module
   const express = require('express');
   const app = express();
   const port = 3000;

   // Define a route for the home page
   app.get('/', (req, res) => {
       res.send('Hello, world!');
   });

   // Start the server
   app.listen(port, () => {
       console.log(`Server running at http://localhost:${port}/`);
   });
   ```
3. **Run the Server**:

   ```
   node server.js
   ```

When you visit `http://localhost:3000` in your browser, you'll see "Hello, world!" displayed, which is served by your Node.js server.

### Conclusion and Summary

Node.js is a powerful runtime environment that allows JavaScript to run on the server side, enabling the development of efficient and scalable backend applications. Its non-blocking I/O model and extensive package ecosystem (NPM) make it a popular choice for building web servers, APIs, and real-time applications.

### Test Your Understanding

1. What makes Node.js suitable for real-time applications?
2. How does the non-blocking I/O model in Node.js improve performance?
3. What role does the V8 engine play in Node.js?
4. How can you manage and install packages in a Node.js project?

### Reference

- [Node.js Official Documentation](https://nodejs.org/en/docs/)
