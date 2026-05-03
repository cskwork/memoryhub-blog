---
title: "Simple example using the App Router with a nested layout and data fetching logic."
date: 2024-06-10T22:41:59+09:00
slug: "258-Simple-example-using-the-App-Router-with-a-nested-layout-and-data-fetching-logic"
original_url: "https://memoryhub.tistory.com/258"
tistory_id: 258
draft: false
---

Sure! Here’s a simple example using the Next.js App Router with a nested layout and data fetching logic. We’ll create a basic structure with a home page, an about page, and nested routing for an "info" section within the about page.

### Project Structure

```
app/
  ├── layout.js
  ├── page.js
  ├── about/
  │   ├── layout.js
  │   ├── page.js
  │   └── info/
  │       └── page.js
```

### Root Layout (`app/layout.js`)

This is the root layout that wraps around all pages.

```
export default function RootLayout({ children }) {
    return (
        <html>
            <body>
                <nav>
                    <a href="/">Home</a> | <a href="/about">About</a>
                </nav>
                {children}
            </body>
        </html>
    );
}
```

### Home Page (`app/page.js`)

This is the home page component with data fetching.

```
async function fetchHomePageData() {
    const res = await fetch('https://jsonplaceholder.typicode.com/posts/1');
    return res.json();
}

export default async function HomePage() {
    const data = await fetchHomePageData();
    return (
        <div>
            <h1>Home Page</h1>
            <p>{data.title}</p>
            <p>{data.body}</p>
        </div>
    );
}
```

### About Layout (`app/about/layout.js`)

This is the layout specific to the about section, which can have nested routes.

```
export default function AboutLayout({ children }) {
    return (
        <div>
            <header>About Header</header>
            {children}
        </div>
    );
}
```

### About Page (`app/about/page.js`)

This is the about page component with data fetching.

```
async function fetchAboutPageData() {
    const res = await fetch('https://jsonplaceholder.typicode.com/posts/2');
    return res.json();
}

export default async function AboutPage() {
    const data = await fetchAboutPageData();
    return (
        <div>
            <h1>About Page</h1>
            <p>{data.title}</p>
            <p>{data.body}</p>
            <a href="/about/info">More Info</a>
        </div>
    );
}
```

### Info Page (`app/about/info/page.js`)

This is the nested info page under the about section with its own data fetching.

```
async function fetchInfoPageData() {
    const res = await fetch('https://jsonplaceholder.typicode.com/posts/3');
    return res.json();
}

export default async function InfoPage() {
    const data = await fetchInfoPageData();
    return (
        <div>
            <h1>Info Page</h1>
            <p>{data.title}</p>
            <p>{data.body}</p>
        </div>
    );
}
```

### Summary

1. **Root Layout**: Wraps around all pages, providing a navigation bar.
2. **Home Page**: Fetches and displays data from an API.
3. **About Layout**: Specific layout for the about section, allowing for nested routes.
4. **About Page**: Fetches and displays data from an API, includes a link to a nested route.
5. **Info Page**: Nested under the about section, fetches and displays its own data.

This example demonstrates how to set up a Next.js project using the App Router with nested layouts and colocated data fetching logic, making your application more modular and easier to maintain.
