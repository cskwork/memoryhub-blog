---
title: "Why not just use Express.js Templating Engine instead of using something like react for the frontend. Why do we use react?"
date: 2024-06-11T23:23:37+09:00
slug: "275-Why-not-just-use-Express-js-Templating-Engine-instead-of-using-something-like-react-for-the-frontend-Why-do-we-use-react"
original_url: "https://memoryhub.tistory.com/275"
tistory_id: 275
draft: false
categories: ["Dev Framework"]
tags: ["ExpressJS"]
---

*While templating engines like EJS are great for generating dynamic server-rendered HTML, React offers a more powerful and flexible approach to building interactive and dynamic user interfaces by utilizing client-side rendering and component-based architecture.*

### The Big Picture

Think of traditional templating engines as a well-organized library where you can find and read static books (server-rendered HTML pages). React, on the other hand, is like an interactive digital library that not only provides the same content but also allows you to interact, search, and get recommendations in real-time, creating a much richer user experience.

### Core Concepts

1. **Server-Side Rendering (SSR):** Templating engines generate HTML on the server and send it to the client. This approach is straightforward and efficient for static content but can become cumbersome for highly interactive applications.
2. **Client-Side Rendering (CSR):** React primarily uses CSR, where the initial HTML is minimal and JavaScript takes over to dynamically update the content on the client side.
3. **Component-Based Architecture:** React's components enable reusability, modularity, and maintainability, which are crucial for building complex and interactive UIs.
4. **State Management:** React has a robust state management system that allows for efficient handling of UI changes and data flow.

### Detailed Walkthrough

#### Advantages of React over Traditional Templating Engines

1. **Interactivity and User Experience:**

   - **Dynamic Updates:** React can update the UI in real-time without requiring a full page reload, providing a smoother user experience.
   - **Single Page Applications (SPAs):** React enables the creation of SPAs where navigation between pages feels instantaneous because the application loads a single HTML page and dynamically updates as the user interacts with it.
2. **Component-Based Architecture:**

   - **Reusability:** React components are reusable pieces of UI that can be easily shared and reused across different parts of an application.
   - **Modularity:** Components encapsulate their own logic and styles, making the application more modular and easier to maintain.
3. **State Management:**

   - **Efficient State Handling:** React's state management, through hooks or libraries like Redux, allows for efficient and predictable handling of application state, making complex interactions easier to manage.
4. **Ecosystem and Tooling:**

   - **Rich Ecosystem:** React has a vast ecosystem of libraries and tools that support various needs, from routing (React Router) to state management (Redux) to server-side rendering (Next.js).
   - **Developer Experience:** Tools like React DevTools and Create React App enhance the development experience by providing powerful debugging and scaffolding capabilities.

### Understanding Through an Example

Let's compare a simple task of displaying a list of items using EJS and React.

#### Using EJS

1. **Server Setup:**

   ```
   const express = require('express');
   const app = express();

   app.set('view engine', 'ejs');
   app.set('views', './views');

   app.get('/', (req, res) => {
     const items = ['Item 1', 'Item 2', 'Item 3'];
     res.render('index', { items });
   });

   app.listen(3000, () => {
     console.log('Server is running on port 3000');
   });
   ```
2. **EJS Template (views/index.ejs):**

   ```
   <!DOCTYPE html>
   <html>
   <head>
     <title>Item List</title>
   </head>
   <body>
     <h1>Items</h1>
     <ul>
       <% items.forEach(item => { %>
         <li><%= item %></li>
       <% }) %>
     </ul>
   </body>
   </html>
   ```

#### Using React

1. **React Component:**

   ```
   import React from 'react';

   function App() {
     const items = ['Item 1', 'Item 2', 'Item 3'];

     return (
       <div>
         <h1>Items</h1>
         <ul>
           {items.map(item => (
             <li key={item}>{item}</li>
           ))}
         </ul>
       </div>
     );
   }

   export default App;
   ```
2. **Rendering in the Browser:**

   ```
   import React from 'react';
   import ReactDOM from 'react-dom';
   import App from './App';

   ReactDOM.render(<App />, document.getElementById('root'));
   ```

### Conclusion and Summary

While templating engines like EJS are suitable for rendering static and server-generated HTML, React provides a more powerful approach for building interactive and dynamic web applications. React's client-side rendering, component-based architecture, efficient state management, and rich ecosystem offer significant advantages for modern web development, especially for applications that require high interactivity and a seamless user experience.

### Test Your Understanding

1. What are the main differences between server-side rendering and client-side rendering?
2. How does React's component-based architecture improve code maintainability?
3. What are some use cases where a templating engine like EJS would be more appropriate than React?

### Reference

For further reading and official documentation, refer to [React Official Documentation](https://reactjs.org/docs/getting-started.html) and [Express.js Templating Engines](https://expressjs.com/en/guide/using-template-engines.html).
