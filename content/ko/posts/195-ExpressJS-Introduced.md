---
title: "ExpressJS Introduced"
date: 2024-06-06T07:16:04+09:00
slug: "195-ExpressJS-Introduced"
original_url: "https://memoryhub.tistory.com/195"
tistory_id: 195
draft: false
categories: ["데브 프레임워크"]
tags: ["ExpressJS"]
---

*Imagine a skilled traffic controller efficiently directing cars through a bustling intersection. Express.js is like that controller for web traffic, organizing and routing HTTP requests with minimal fuss.*

### The Big Picture

Express.js is a minimal and flexible web application framework for Node.js. It's like a Swiss Army knife for building web applications and APIs, providing a robust set of features for web and mobile applications. Express simplifies the process of handling HTTP requests, routing, and middleware integration, making it easier to create server-side applications.

### Core Concepts

1. Routing
2. Middleware
3. Request and Response handling
4. Template engines
5. Error handling
6. Static file serving

### Detailed Walkthrough

#### 1. Routing

Express provides a simple way to define routes for your application. It's like creating a map for your web application, telling it how to respond to different URLs and HTTP methods.

```
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.post('/api/users', (req, res) => {
  // Create a new user
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

#### 2. Middleware

Middleware functions are like checkpoints in your application. They have access to the request and response objects, and can execute any code, make changes to the request and response objects, end the request-response cycle, or call the next middleware function.

```
app.use((req, res, next) => {
  console.log('Time:', Date.now());
  next();
});
```

#### 3. Request and Response handling

Express extends Node's req and res objects, providing more convenient methods for handling HTTP requests and responses. It's like giving your traffic controller a set of advanced tools to manage the flow more effectively.

```
app.get('/api/users/:id', (req, res) => {
  const userId = req.params.id;
  // Fetch user data
  res.json({ id: userId, name: 'John Doe' });
});
```

#### 4. Template engines

Express can be used with various template engines to generate HTML for the client. This is like having a document generator that can create custom responses based on data and predefined templates.

```
app.set('view engine', 'pug');

app.get('/profile', (req, res) => {
  res.render('profile', { name: 'John Doe' });
});
```

#### 5. Error handling

Express provides a way to handle errors that occur in your application. It's like having a safety net that catches and manages unexpected issues.

```
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});
```

#### 6. Static file serving

Express can serve static files like images, CSS, and JavaScript files. It's like having a dedicated delivery service for your application's assets.

```
app.use(express.static('public'));
```

### Understanding Through an Example

Let's create a simple Express application that demonstrates these concepts:

```
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

// Middleware
app.use(bodyParser.json());
app.use(express.static('public'));

// Custom middleware
app.use((req, res, next) => {
  console.log(`${req.method} request for ${req.url}`);
  next();
});

// Routes
app.get('/', (req, res) => {
  res.send('Welcome to our API!');
});

app.get('/api/users', (req, res) => {
  // In a real app, this would fetch from a database
  res.json([
    { id: 1, name: 'Alice' },
    { id: 2, name: 'Bob' }
  ]);
});

app.post('/api/users', (req, res) => {
  const newUser = req.body;
  // In a real app, this would save to a database
  console.log('Creating new user:', newUser);
  res.status(201).json({ message: 'User created', user: newUser });
});

// Error handling
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something went wrong!');
});

// Start the server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
```

This example demonstrates:

- Setting up an Express server
- Using middleware (bodyParser and static file serving)
- Defining routes for different HTTP methods
- Handling JSON responses
- Basic error handling

### Conclusion and Summary

Express.js is a powerful yet lightweight framework for building web applications and APIs in Node.js. It provides a simple, intuitive interface for handling HTTP requests, middleware integration, and routing. Its flexibility allows developers to structure their applications as they see fit, making it suitable for both small projects and large-scale applications.

### Test Your Understanding

1. How does routing in Express.js work, and how is it different from traditional server-side routing?
2. What is middleware in Express.js, and can you give an example of when you might use custom middleware?
3. How would you handle file uploads in an Express.js application?
4. Can you explain the difference between `app.use()` and `app.get()` in Express.js?

### Reference

For comprehensive and up-to-date information on Express.js, including advanced topics and best practices, I recommend referring to the official Express documentation: <https://expressjs.com/>. This resource provides detailed guides, API references, and examples to help you master Express.js for building robust web applications.

---
