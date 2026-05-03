---
title: "What is the role of a templating engine in an Express.js application?"
date: 2024-06-11T23:22:20+09:00
slug: "274-What-is-the-role-of-a-templating-engine-in-an-Express-js-application"
original_url: "https://memoryhub.tistory.com/274"
tistory_id: 274
draft: false
---

*In an Express.js application, a templating engine generates HTML dynamically, allowing you to embed variables and logic within your HTML pages for dynamic content rendering.*

### The Big Picture

Think of a templating engine like a master chef who can prepare a variety of dishes (web pages) from a standard set of ingredients (data). Instead of creating static HTML pages for every possible outcome, the templating engine mixes and matches content dynamically based on the data provided, producing customized dishes for each customer (user).

### Core Concepts

1. **Dynamic Content:** Templating engines allow you to generate HTML pages dynamically by embedding JavaScript logic and variables within HTML.
2. **Separation of Concerns:** They help separate your application's logic from its presentation, making the codebase cleaner and easier to manage.
3. **Reusability:** You can create reusable components and templates, reducing redundancy and improving maintainability.

### Detailed Walkthrough

#### How Templating Engines Work

A templating engine takes an HTML template file and data provided by the server to produce a final HTML page that is sent to the client. Here's a basic flow:

1. **Template File:** Contains placeholders for dynamic content (e.g., `<%= title %>` in EJS).
2. **Data:** Server-side data that fills in the placeholders.
3. **Rendered HTML:** The final HTML page after the placeholders have been replaced with actual data.

#### Popular Templating Engines

1. **EJS (Embedded JavaScript):** Simple and easy to use. Syntax is close to HTML.
2. **Pug (formerly Jade):** Uses indentation-based syntax, which can be more concise.
3. **Handlebars:** Known for its logic-less philosophy, focusing on minimal logic in templates.

### Understanding Through an Example

Let's walk through an example using EJS as our templating engine.

#### 1. **Setting Up EJS in Express**

First, install EJS:

```
npm install ejs
```

Set up EJS in your Express application:

```
const express = require('express');
const app = express();

// Set EJS as the templating engine
app.set('view engine', 'ejs');
app.set('views', './views'); // Specify the directory for views
```

#### 2. **Creating an EJS Template**

Create a file named `index.ejs` in the `views` directory:

```
<!DOCTYPE html>
<html>
<head>
  <title><%= title %></title>
</head>
<body>
  <h1>Welcome, <%= user %>!</h1>
</body>
</html>
```

#### 3. **Rendering the Template with Data**

In your Express route, render the `index.ejs` template with dynamic data:

```
app.get('/', (req, res) => {
  res.render('index', { title: 'Home Page', user: 'Alice' });
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

When a user visits the home page, Express uses the EJS templating engine to generate the HTML by replacing `<%= title %>` with "Home Page" and `<%= user %>` with "Alice".

### Conclusion and Summary

A templating engine in an Express.js application:

- Generates dynamic HTML content by embedding JavaScript logic within HTML templates.
- Separates presentation logic from business logic, enhancing code maintainability.
- Provides reusable components and templates, making the application more modular.

### Test Your Understanding

1. What are the benefits of using a templating engine in a web application?
2. How do you pass data to an EJS template in an Express route?
3. Can you name two other templating engines besides EJS and explain their key differences?

### Reference

For further reading and official documentation, refer to [Express.js: Using Template Engines](https://expressjs.com/en/guide/using-template-engines.html).
