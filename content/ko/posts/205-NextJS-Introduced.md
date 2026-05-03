---
title: "NextJS Introduced"
date: 2024-06-07T13:53:11+09:00
slug: "205-NextJS-Introduced"
original_url: "https://memoryhub.tistory.com/205"
tistory_id: 205
draft: false
---

*Next.js is a powerful framework for building React applications, offering features like server-side rendering, static site generation, and more.*

---

### The Big Picture

Imagine you have a restaurant. You have a kitchen (server) where chefs prepare dishes (data) and a dining area (client) where customers enjoy their meals (user interface). In a typical setup, customers order from a menu, wait for the food to be prepared, and then enjoy their meal. Similarly, in traditional web applications, the client requests data from the server, which processes and sends it back to the client.

Next.js is like a high-tech restaurant where some dishes are pre-prepared and ready to serve instantly, while others are made fresh to order. This approach ensures that your customers (users) get a fast and seamless experience, whether they are ordering a popular dish (static content) or something more specialized (dynamic content).

---

### Core Concepts

1. **Server-Side Rendering (SSR)**:

   - The server generates the HTML for a page on each request.
   - Example: When you order a custom-made dish, the chef prepares it fresh each time.
2. **Static Site Generation (SSG)**:

   - HTML is generated at build time and reused for each request.
   - Example: Popular dishes are pre-prepared and ready to serve instantly.
3. **Client-Side Rendering (CSR)**:

   - The browser handles rendering after loading the initial HTML.
   - Example: A salad bar where customers mix their own salads using pre-prepared ingredients.
4. **API Routes**:

   - Define API endpoints within the application.
   - Example: A special request service in the restaurant that handles custom orders.
5. **File-based Routing**:

   - Pages and routes are created by placing files in the `pages` directory.
   - Example: A menu where each section (Appetizers, Main Course, Desserts) is easily accessible.

---

### Detailed Walkthrough

1. **Server-Side Rendering (SSR)**:

   - When a user requests a page, the server generates the complete HTML and sends it back. This is useful for dynamic content that changes frequently. For example:

     ```
     export async function getServerSideProps(context) {
       const res = await fetch('https://api.example.com/data');
       const data = await res.json();
       return { props: { data } };
     }
     function Page({ data }) {
       return <div>{data.content}</div>;
     }
     export default Page;
     ```
2. **Static Site Generation (SSG)**:

   - Pages are pre-rendered at build time and served as static HTML files. This is ideal for content that doesn’t change often. For example:

     ```
     export async function getStaticProps() {
       const res = await fetch('https://api.example.com/data');
       const data = await res.json();
       return { props: { data } };
     }
     function Page({ data }) {
       return <div>{data.content}</div>;
     }
     export default Page;
     ```
3. **Client-Side Rendering (CSR)**:

   - The initial HTML is loaded and JavaScript takes over to render the rest of the page. This approach is common in single-page applications (SPAs).

     ```
     import { useEffect, useState } from 'react';
     function Page() {
       const [data, setData] = useState(null);
       useEffect(() => {
         fetch('https://api.example.com/data')
           .then((res) => res.json())
           .then((data) => setData(data));
       }, []);
       return <div>{data ? data.content : 'Loading...'}</div>;
     }
     export default Page;
     ```
4. **API Routes**:

   - Next.js allows you to create API endpoints by adding files to the `pages/api` directory. For example:

     ```
     // pages/api/hello.js
     export default function handler(req, res) {
       res.status(200).json({ message: 'Hello World' });
     }
     ```
5. **File-based Routing**:

   - Each file in the `pages` directory automatically becomes a route. For example, `pages/about.js` becomes `/about` in the URL.

---

### Understanding Through an Example

Let's say you want to build a blog with Next.js. You have a mix of static pages (like the homepage and about page) and dynamic pages (individual blog posts). Here's how you could structure it:

1. **Homepage and About Page (SSG)**:

   - Pre-render these pages at build time since their content doesn't change often.
2. **Blog Posts (SSG with dynamic data)**:

   - Pre-render blog post pages using data fetched from a CMS during the build process.
3. **Comments Section (SSR)**:

   - Fetch and render comments dynamically whenever a blog post page is requested to ensure the latest comments are displayed.

---

### Conclusion and Summary

Next.js is a versatile framework that enhances the development of React applications by offering multiple rendering methods: SSR for dynamic content, SSG for static content, and CSR for client-heavy interactions. Its file-based routing and built-in API support streamline the development process, making it easier to create performant and scalable web applications.

---

### Test Your Understanding

1. Explain the difference between SSR and SSG in Next.js.
2. How does client-side rendering differ from server-side rendering?
3. Provide an example of when you would use an API route in Next.js.
4. Describe a scenario where static site generation would be more beneficial than server-side rendering.

---

### Reference

For more details, you can explore the [Next.js official documentation](https://nextjs.org/docs).
