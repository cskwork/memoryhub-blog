---
title: "What are the main responsibilities of middleware functions in Express.js?"
date: 2024-06-11T23:11:18+09:00
slug: "272-What-are-the-main-responsibilities-of-middleware-functions-in-Express-js"
original_url: "https://memoryhub.tistory.com/272"
tistory_id: 272
draft: false
---

*Middleware functions in Express.js are the backbone of handling requests and responses in a web application, enabling flexible and efficient request processing.*

### The Big Picture

Imagine building a house. Middleware functions in Express.js are like different workers (plumbers, electricians, carpenters) that prepare the house at various stages before it's ready for the occupants (the users). Each worker has a specific job to ensure the house meets the occupants' needs. Similarly, middleware functions handle different aspects of a request before it's finally sent as a response.

### Core Concepts

1. **Request and Response Handling:** Middleware functions process requests before they reach the final route handler and modify responses before sending them to the client.
2. **Chaining:** Middleware functions are chained together, each performing specific tasks and then passing control to the next middleware in the sequence.
3. **Execution Order:** Middleware functions are executed in the order they are defined in the Express application.
4. **Modularity:** Middleware allows for modular and reusable code, improving the maintainability of the application.

### Detailed Walkthrough

#### 1. **Pre-processing Requests**

Middleware functions can pre-process requests to handle tasks like parsing request bodies, handling cookies, and managing sessions. For example:

- **Body Parsing:** Middleware like `body-parser` parses incoming request bodies and makes the data available under `req.body`.

  ```
  const bodyParser = require('body-parser');
  app.use(bodyParser.json());
  ```
- **Cookie Handling:** Middleware for parsing cookies and populating `req.cookies`.

  ```
  const cookieParser = require('cookie-parser');
  app.use(cookieParser());
  ```

#### 2. **Routing Control**

Middleware can control the flow of the application by conditionally passing control to the next middleware or ending the response cycle.

- **Authentication:** Middleware can check if a user is authenticated before proceeding to protected routes.

  ```
  function isAuthenticated(req, res, next) {
    if (req.isAuthenticated()) {
      return next();
    } else {
      res.redirect('/login');
    }
  }
  app.use('/protected', isAuthenticated);
  ```

#### 3. **Response Modification**

Middleware can modify the response before sending it back to the client.

- **Compression:** Middleware can compress responses to reduce payload size.

  ```
  const compression = require('compression');
  app.use(compression());
  ```

#### 4. **Error Handling**

Special middleware functions are used to handle errors and send appropriate responses to the client.

- **Error Handling Middleware:** These are defined with four parameters (err, req, res, next).

  ```
  function errorHandler(err, req, res, next) {
    res.status(500).send({ error: err.message });
  }
  app.use(errorHandler);
  ```

### Understanding Through an Example

Let's say you have an Express application that needs to log requests, check if the user is authenticated, and handle errors. Here's how middleware functions could be used:

```
const express = require('express');
const app = express();

// Logging Middleware
function logRequests(req, res, next) {
  console.log(`${req.method} ${req.url}`);
  next(); // Passes control to the next middleware
}

// Authentication Middleware
function checkAuth(req, res, next) {
  if (req.isAuthenticated()) {
    next(); // User is authenticated, proceed to next middleware
  } else {
    res.status(401).send('Unauthorized'); // End response cycle
  }
}

// Error Handling Middleware
function errorHandler(err, req, res, next) {
  console.error(err.stack);
  res.status(500).send('Something broke!');
}

// Use the middlewares
app.use(logRequests);
app.use(checkAuth);
app.use(errorHandler);

// Define a route
app.get('/', (req, res) => {
  res.send('Hello, world!');
});

// Start the server
app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

### Conclusion and Summary

Middleware functions in Express.js are crucial for:

- Pre-processing requests (e.g., parsing data, handling cookies).
- Controlling routing flow (e.g., authentication checks).
- Modifying responses (e.g., compression).
- Handling errors gracefully.

They are executed in the order they are defined, enabling a structured and organized request-response lifecycle.

### Test Your Understanding

1. What happens if a middleware function does not call `next()` or send a response?
2. How would you handle logging of requests only for specific routes?
3. Can middleware functions be asynchronous, and how would you handle errors in such functions?

### Reference

For further reading and official documentation, refer to [Express.js Middleware](https://expressjs.com/en/guide/using-middleware.html).
