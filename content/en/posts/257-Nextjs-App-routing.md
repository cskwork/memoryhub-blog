---
title: "Nextjs App routing"
date: 2024-06-10T22:40:38+09:00
slug: "257-Nextjs-App-routing"
original_url: "https://memoryhub.tistory.com/257"
tistory_id: 257
draft: false
categories: ["Dev Framework"]
tags: ["NextJS"]
---

*Next.js App Router introduces a more flexible, component-based routing system, leveraging React Server Components and advanced data fetching methods, providing a modern and powerful way to manage routing in complex applications.*

---

### The Big Picture

Imagine building a skyscraper where each floor (route) can have its unique layout and functionality. The Next.js App Router allows you to define and manage these floors dynamically, integrating the latest web technologies like React Server Components to ensure efficient and scalable construction.

### Core Concepts

1. **React Server Components**: Server-side rendering with React components.
2. **File and Folder-based Routing**: Organizing routes in a more flexible, component-centric way.
3. **Layouts and Nested Routes**: Advanced layout management with nested routes.
4. **Data Fetching**: Colocated, granular data fetching methods.
5. **Server and Client Components**: Differentiation between server-rendered and client-rendered components.

### Detailed Walkthrough

#### React Server Components

React Server Components (RSC) allow parts of your app to be rendered on the server, improving performance and reducing the amount of JavaScript sent to the client. They enable seamless integration of server-side logic directly within React components.

Example:

```
// app/page.js
import React from 'react';

export default function HomePage() {
    return <h1>Home Page</h1>;
}
```

In the above example, `HomePage` is a server component. You can fetch data within this component and render it server-side.

#### File and Folder-based Routing

The App Router uses a more flexible, component-based routing system where each file and folder in the `app` directory corresponds to a route. This structure allows for colocating components, layouts, and data fetching logic.

Example Structure:

```
app/
  ├── layout.js
  ├── page.js
  ├── about/
  │   ├── layout.js
  │   └── page.js
  └── dashboard/
      ├── layout.js
      ├── page.js
      └── settings/
          └── page.js
```

#### Layouts and Nested Routes

The App Router provides advanced layout management by allowing nested layouts. Each directory can have its own `layout.js` file, which defines the layout for all nested routes.

Example:

```
// app/layout.js
export default function RootLayout({ children }) {
    return (
        <html>
            <body>
                <nav>/* Navigation */</nav>
                {children}
            </body>
        </html>
    );
}

// app/about/layout.js
export default function AboutLayout({ children }) {
    return (
        <div>
            <header>About Header</header>
            {children}
        </div>
    );
}
```

In this example, `RootLayout` provides a base layout for the entire application, while `AboutLayout` defines a specific layout for the `/about` route.

#### Data Fetching

Data fetching in the App Router is more granular and colocated with the components that need the data. This allows for better organization and reduces the need for global state management.

Example:

```
// app/page.js
import React from 'react';

async function fetchData() {
    const res = await fetch('https://api.example.com/data');
    return res.json();
}

export default function HomePage() {
    const data = fetchData();
    return <h1>Home Page: {data.message}</h1>;
}
```

In this example, `fetchData` is called directly within the `HomePage` component, making the data fetching logic easy to understand and maintain.

#### Server and Client Components

The App Router differentiates between server-rendered and client-rendered components. By default, components in the `app` directory are server components. You can explicitly define client components when needed.

Example:

```
// app/page.js
import React from 'react';

// Client Component
'use client';

function ClientComponent() {
    return <button>Click me</button>;
}

// Server Component
export default function HomePage() {
    return (
        <div>
            <h1>Home Page</h1>
            <ClientComponent />
        </div>
    );
}
```

### Understanding Through an Example

Consider a simple application with a home page and an about page, each with its own layout and data fetching logic.

```
app/
  ├── layout.js
  ├── page.js
  ├── about/
  │   ├── layout.js
  │   └── page.js
```

```
// app/layout.js
export default function RootLayout({ children }) {
    return (
        <html>
            <body>
                <nav>/* Navigation */</nav>
                {children}
            </body>
        </html>
    );
}

// app/page.js
import React from 'react';

async function fetchHomePageData() {
    const res = await fetch('https://api.example.com/home');
    return res.json();
}

export default function HomePage() {
    const data = fetchHomePageData();
    return <h1>Home Page: {data.message}</h1>;
}

// app/about/layout.js
export default function AboutLayout({ children }) {
    return (
        <div>
            <header>About Header</header>
            {children}
        </div>
    );
}

// app/about/page.js
import React from 'react';

async function fetchAboutPageData() {
    const res = await fetch('https://api.example.com/about');
    return res.json();
}

export default function AboutPage() {
    const data = fetchAboutPageData();
    return <h1>About Page: {data.message}</h1>;
}
```

### Conclusion and Summary

The Next.js App Router provides a modern, flexible routing system using React Server Components. It supports advanced layout and nested routing, colocated data fetching, and differentiates between server and client components. This approach enhances performance, code organization, and scalability, making it suitable for complex applications.

### Test Your Understanding

1. What are the key differences between the App Router and the traditional Pages Router in Next.js?
2. How does the App Router handle data fetching differently from the Pages Router?
3. Write a simple example using the App Router with a nested layout and data fetching logic.

### Reference

- [Next.js Documentation - Routing](https://nextjs.org/docs/routing/introduction)
- [Next.js 13 Introduction to the App Router](https://nextjs.org/docs/app)
