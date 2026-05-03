---
title: "Can you explain the difference between app.use() and app.get() in Express.js?"
date: 2024-06-22T12:10:11+09:00
slug: "308-Can-you-explain-the-difference-between-app-use-and-app-get-in-Express-js"
original_url: "https://memoryhub.tistory.com/308"
tistory_id: 308
draft: false
categories: ["데브 프레임워크"]
tags: ["ExpressJS"]
---

---

*Imagine a busy restaurant with different staff roles. `app.use()` is like the general staff that greets and assists all customers, while `app.get()` is like a specialized chef who only prepares specific dishes when ordered.*

### The Big Picture

In Express.js, both `app.use()` and `app.get()` are methods used for handling requests, but they serve different purposes and behave differently in terms of when and how they are executed.

### Core Concepts

1. Middleware (`app.use()`)
2. Route handlers (`app.get()`)
3. Request matching
4. Order of execution

### Detailed Walkthrough

#### 1. app.use()

- **Purpose:** Used to mount middleware functions.
- **Scope:** Applies to all requests that come to the server, regardless of HTTP method (GET, POST, etc.).
- **Path matching:** If a path is specified, it matches that path and any sub-paths.
- **Execution:** Always executes for every request unless a response is sent or `next()` isn't called.

**Example:**

```
app.use((req, res, next) => {
  console.log('Time:', Date.now());
  next();
});

app.use('/user', (req, res, next) => {
  console.log('Request Type:', req.method);
  next();
});
```

#### 2. app.get()

- **Purpose:** Used to define route handlers for GET requests.
- **Scope:** Only applies to HTTP GET requests.
- **Path matching:** Matches the exact specified path.
- **Execution:** Only executes when the path and HTTP method match.

**Example:**

```
app.get('/user', (req, res) => {
  res.send('Got a GET request at /user');
});
```

#### 3. Request Matching

- **`app.use()`:** Matches partial paths. For example, `app.use('/user', ...)` will match '/user', '/user/profile', '/user/settings', etc.
- **`app.get()`:** Matches exact paths. `app.get('/user', ...)` will only match '/user', not '/user/profile'.

#### 4. Order of Execution

The order in which you define these methods matters significantly:

```
app.use((req, res, next) => {
  console.log('This will run for every request');
  next();
});

app.get('/user', (req, res) => {
  res.send('GET /user');
});

app.use('/user', (req, res, next) => {
  console.log('This will not run for GET /user');
  next();
});
```

In this example, the first `app.use()` will run for all requests. The `app.get('/user')` will handle GET requests to '/user'. The last `app.use('/user')` will not run for GET requests to '/user' because the previous route handler already sent a response.

### Understanding Through an Example

Let's create a simple Express application that demonstrates the differences:

```
const express = require('express');
const app = express();

// Middleware for all routes
app.use((req, res, next) => {
  console.log('Time:', Date.now());
  next();
});

// Middleware for /user and its sub-paths
app.use('/user', (req, res, next) => {
  console.log('Accessing user route');
  next();
});

// GET route handler for /user
app.get('/user', (req, res) => {
  res.send('Got a GET request at /user');
});

// POST route handler for /user
app.post('/user', (req, res) => {
  res.send('Got a POST request at /user');
});

// Middleware that won't run for GET or POST /user
app.use('/user', (req, res, next) => {
  console.log('This won\'t run for GET or POST /user');
  next();
});

app.listen(3000, () => console.log('Server running on port 3000'));
```

In this example:

1. The first `app.use()` runs for every request.
2. The second `app.use('/user')` runs for any request to '/user' or its sub-paths.
3. `app.get('/user')` only handles GET requests to '/user'.
4. `app.post('/user')` only handles POST requests to '/user'.
5. The last `app.use('/user')` won't run for GET or POST requests to '/user' because the previous handlers already sent responses.

### Conclusion and Summary

`app.use()` is a general-purpose middleware method that can handle all types of HTTP requests and can match partial paths. It's great for applying middleware to groups of routes. `app.get()` is specific to GET requests and matches exact paths, making it ideal for handling specific endpoints in your application. Understanding the difference and the order of execution is crucial for properly structuring your Express.js application.

### Test Your Understanding

1. If you have `app.use('/api', ...)` followed by `app.get('/api/users', ...)`, which one will handle a GET request to '/api/users'?
2. How would you use `app.use()` to apply middleware only to a specific group of routes?
3. Can you think of a scenario where you might want to use both `app.use()` and `app.get()` for the same path?

*Before we proceed, could you share your experience with building web servers or APIs? This will help me provide more relevant examples or explanations.*

### Reference

For more detailed information and best practices on using middleware and routing in Express.js, I recommend checking the official Express.js documentation: <https://expressjs.com/en/guide/using-middleware.html> and <https://expressjs.com/en/guide/routing.html>. These resources provide comprehensive guides on middleware usage and routing in Express.js.

---
