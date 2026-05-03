---
title: "How would you send a JSON response in Express.js?"
date: 2024-06-11T23:20:27+09:00
slug: "273-How-would-you-send-a-JSON-response-in-Express-js"
original_url: "https://memoryhub.tistory.com/273"
tistory_id: 273
draft: false
categories: ["데브 프레임워크"]
tags: ["ExpressJS"]
---

*To send a JSON response in Express.js, you can use the `res.json()` method, which sends a JSON response with the appropriate `Content-Type` header.*

### The Big Picture

Imagine a restaurant serving food. The kitchen (server) prepares the food (data) and the waiters (Express.js) deliver it to the customers (clients). In this analogy, sending a JSON response is like presenting the food in a specific format that the customer expects and understands. JSON is one of these formats, commonly used because it's easy for both humans and machines to read and write.

### Core Concepts

1. **JSON Format:** JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
2. **Express.js Response Object:** The `res` object in Express.js has methods for sending different types of responses, including JSON.
3. **HTTP Headers:** When sending a JSON response, the `Content-Type` header is automatically set to `application/json`.

### Detailed Walkthrough

#### Using `res.json()`

The `res.json()` method in Express.js is used to send a JSON response. It converts a JavaScript object or array into JSON format and sets the appropriate `Content-Type` header.

Here's a basic example:

```
const express = require('express');
const app = express();

app.get('/data', (req, res) => {
  const responseData = {
    message: 'Hello, world!',
    date: new Date()
  };
  res.json(responseData); // Sends a JSON response
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

In this example:

- The server listens on port 3000.
- When a GET request is made to the `/data` endpoint, the server responds with a JSON object containing a message and the current date.

### Understanding Through an Example

Let's extend this with a more complex example involving a list of users:

```
const express = require('express');
const app = express();

const users = [
  { id: 1, name: 'Alice', email: 'alice@example.com' },
  { id: 2, name: 'Bob', email: 'bob@example.com' },
  { id: 3, name: 'Charlie', email: 'charlie@example.com' }
];

app.get('/users', (req, res) => {
  res.json(users); // Sends the array of users as a JSON response
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

### Conclusion and Summary

To send a JSON response in Express.js:

- Use the `res.json()` method.
- Pass the JavaScript object or array you want to send as JSON.

This method ensures that the `Content-Type` header is set to `application/json`, and the response is formatted correctly for the client to process.

### Test Your Understanding

1. What method would you use to send a plain text response in Express.js?
2. How can you send a status code along with a JSON response?
3. What header does Express automatically set when using `res.json()`?

### Reference

For further reading and official documentation, refer to [Express.js: res.json()](https://expressjs.com/en/api.html#res.json).
