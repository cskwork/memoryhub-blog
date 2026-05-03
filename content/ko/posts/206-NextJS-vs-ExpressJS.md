---
title: "NextJS vs ExpressJS"
date: 2024-06-07T14:02:15+09:00
slug: "206-NextJS-vs-ExpressJS"
original_url: "https://memoryhub.tistory.com/206"
tistory_id: 206
draft: false
categories: ["데브 프레임워크"]
tags: ["NextJS"]
---

*Express.js and Next.js are both powerful frameworks for building web applications, but they serve different purposes and have distinct features.*

---

### The Big Picture

Think of Express.js as a versatile toolkit for building the foundation of your house (web application). It provides the basic tools and materials, allowing you to create a custom structure tailored to your needs. You can decide how to lay out the rooms, where the windows should go, and what materials to use.

On the other hand, Next.js is like a pre-designed house with customizable options. It comes with built-in rooms (features) like server-side rendering, static site generation, and file-based routing, making it quicker and easier to build a complete and efficient house with less effort.

---

### Core Concepts

1. **Purpose and Usage**:

   - **Express.js**: A minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. It is primarily used for building server-side applications and APIs.
   - **Next.js**: A React framework for building user interfaces with features like server-side rendering, static site generation, and client-side rendering. It is used for building full-stack web applications with React.
2. **Rendering Methods**:

   - **Express.js**: Does not provide built-in rendering methods; you have to integrate your own templating engine or frontend framework.
   - **Next.js**: Provides server-side rendering (SSR), static site generation (SSG), and client-side rendering (CSR) out of the box.
3. **Routing**:

   - **Express.js**: Routing is defined manually using its routing methods.

     ```
     const express = require('express');
     const app = express();
     app.get('/', (req, res) => {
       res.send('Hello World');
     });
     app.listen(3000);
     ```
   - **Next.js**: Uses file-based routing where each file in the `pages` directory corresponds to a route.

     ```
     // pages/index.js
     export default function Home() {
       return <h1>Hello World</h1>;
     }
     ```
4. **API Handling**:

   - **Express.js**: Primarily used to create APIs with flexible routing and middleware support.

     ```
     app.get('/api/data', (req, res) => {
       res.json({ message: 'Hello API' });
     });
     ```
   - **Next.js**: Supports API routes by placing files in the `pages/api` directory.

     ```
     // pages/api/data.js
     export default function handler(req, res) {
       res.status(200).json({ message: 'Hello API' });
     }
     ```
5. **Middleware**:

   - **Express.js**: Extensive middleware ecosystem that allows adding functionalities like authentication, logging, and more.

     ```
     const morgan = require('morgan');
     app.use(morgan('dev'));
     ```
   - **Next.js**: Limited built-in middleware support, primarily relies on custom API routes for backend logic.

---

### Detailed Walkthrough

1. **Building a Simple API**:

   - **Express.js**:

     ```
     const express = require('express');
     const app = express();
     app.get('/api/hello', (req, res) => {
       res.json({ message: 'Hello from Express' });
     });
     app.listen(3000, () => {
       console.log('Server running on http://localhost:3000');
     });
     ```
   - **Next.js**:

     ```
     // pages/api/hello.js
     export default function handler(req, res) {
       res.status(200).json({ message: 'Hello from Next.js' });
     }
     ```
2. **Creating a Web Page**:

   - **Express.js**: Requires setting up a templating engine or serving static files.

     ```
     const path = require('path');
     app.get('/', (req, res) => {
       res.sendFile(path.join(__dirname, 'index.html'));
     });
     ```
   - **Next.js**: Directly create a React component in the `pages` directory.

     ```
     // pages/index.js
     export default function Home() {
       return <h1>Hello from Next.js</h1>;
     }
     ```
3. **Middleware Integration**:

   - **Express.js**:

     ```
     const bodyParser = require('body-parser');
     app.use(bodyParser.json());
     app.post('/api/data', (req, res) => {
       res.json({ received: req.body });
     });
     ```
   - **Next.js**: Typically handled within API routes.

     ```
     // pages/api/data.js
     export default function handler(req, res) {
       if (req.method === 'POST') {
         res.status(200).json({ received: req.body });
       } else {
         res.status(405).json({ message: 'Method Not Allowed' });
       }
     }
     ```

---

### Conclusion and Summary

- **Express.js** is a flexible and unopinionated framework focused on building server-side applications and APIs, requiring more manual setup and integration.
- **Next.js** is a comprehensive framework for building full-stack React applications with built-in support for SSR, SSG, and CSR, providing a streamlined development experience with less configuration.

---

### Test Your Understanding

1. What are the main differences in routing between Express.js and Next.js?
2. How does Next.js handle server-side rendering compared to Express.js?
3. Give an example of when you would choose Express.js over Next.js and vice versa.

---

### Reference

For more information, you can visit the official documentation for [Express.js](https://expressjs.com/) and [Next.js](https://nextjs.org/docs).
