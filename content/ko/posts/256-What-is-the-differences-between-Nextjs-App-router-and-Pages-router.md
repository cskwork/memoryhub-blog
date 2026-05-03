---
title: "What is the differences between Nextjs App router and Pages router?"
date: 2024-06-10T22:37:10+09:00
slug: "256-What-is-the-differences-between-Nextjs-App-router-and-Pages-router"
original_url: "https://memoryhub.tistory.com/256"
tistory_id: 256
draft: false
categories: ["데브 프레임워크"]
tags: ["NextJS"]
---

*Next.js provides two routing systems: the App Router and the Pages Router. The App Router leverages the newer React Server Components and offers more granular data fetching and layout control, while the Pages Router follows a more traditional, file-based routing system.*

---

### The Big Picture

Think of the Pages Router as a straightforward roadmap where each destination (page) is clearly marked and follows a direct path. The App Router, on the other hand, is like a dynamic GPS that adapts to new routes, offers real-time updates, and integrates more seamlessly with modern web technologies like React Server Components.

### Core Concepts

1. **Pages Router**: Traditional file-based routing.
2. **App Router**: Newer, feature-rich routing with React Server Components.
3. **Data Fetching**: Differences in how data is fetched and managed.
4. **Layouts and Nested Routes**: Handling layouts and nested routes.
5. **Performance and Optimization**: Variations in performance features and optimizations.

### Detailed Walkthrough

#### Pages Router

The Pages Router follows a traditional file-based approach where the file structure in the `pages` directory defines the routes:

1. **File-based Routing**:

   - Each file in the `pages` directory corresponds to a route.
   - For example, `pages/index.js` maps to the home route (`/`), and `pages/about.js` maps to `/about`.
2. **Data Fetching Methods**:

   - `getStaticProps`: Fetches data at build time.
   - `getServerSideProps`: Fetches data on each request.
   - `getStaticPaths`: Generates paths for dynamic routes at build time.
3. **Simple Layouts**:

   - Layouts are typically implemented using custom `_app.js` and wrapping components within it.

Example:

```
// pages/index.js
function HomePage() {
    return <h1>Home Page</h1>;
}

export async function getStaticProps() {
    // Fetch data at build time
    return { props: { data: 'some data' } };
}

export default HomePage;
```

#### App Router

The App Router offers more advanced routing capabilities using React Server Components and the `app` directory:

1. **File and Folder-based Routing**:

   - The `app` directory is used instead of `pages`.
   - Supports colocated components, layouts, and templates.
2. **React Server Components**:

   - Introduces support for React Server Components, allowing for better server-side rendering and data fetching.
   - Components can be designated as client or server components.
3. **Enhanced Layouts and Nested Routes**:

   - Layouts are more flexible and can be nested, allowing for better organization and reusability.
   - The `layout.js` file can define layouts for nested routes.
4. **Data Fetching**:

   - Uses `fetch` or other async data fetching mechanisms directly in server components.
   - Data fetching is more granular and can be colocated with components.

Example:

```
// app/page.js
export default function HomePage() {
    return <h1>Home Page</h1>;
}

// app/layout.js
export default function RootLayout({ children }) {
    return (
        <html>
            <body>{children}</body>
        </html>
    );
}
```

#### Key Differences

1. **Routing System**:

   - **Pages Router**: File-based, conventional routing.
   - **App Router**: Flexible, component-based routing with nested routes.
2. **Data Fetching**:

   - **Pages Router**: Uses `getStaticProps`, `getServerSideProps`, and `getStaticPaths`.
   - **App Router**: Uses React Server Components and colocated fetch calls.
3. **Layouts**:

   - **Pages Router**: Simple, with a single `_app.js`.
   - **App Router**: Advanced, with nested and colocated `layout.js` files.
4. **Performance and Optimization**:

   - **Pages Router**: Good for straightforward use cases and smaller projects.
   - **App Router**: Better for complex applications with enhanced performance due to server-side rendering and React Server Components.

### Understanding Through an Example

#### Pages Router Example

```
// pages/about.js
function AboutPage() {
    return <h1>About Page</h1>;
}

export async function getServerSideProps() {
    // Fetch data on each request
    const res = await fetch('https://api.example.com/data');
    const data = await res.json();
    return { props: { data } };
}

export default AboutPage;
```

#### App Router Example

```
// app/page.js
export default function HomePage() {
    return <h1>Home Page</h1>;
}

// app/layout.js
export default function RootLayout({ children }) {
    return (
        <html>
            <body>{children}</body>
        </html>
    );
}
```

### Conclusion and Summary

Next.js provides two routing systems: the Pages Router and the App Router. The Pages Router is traditional and file-based, suitable for straightforward routing needs. The App Router, on the other hand, is more flexible and modern, leveraging React Server Components and offering better data fetching and layout control. Choosing between them depends on the complexity and requirements of your application.

### Test Your Understanding

1. What are the primary differences between the Pages Router and the App Router in Next.js?
2. How does data fetching differ between the two routing systems?
3. Write a simple example using the App Router that includes a nested layout.

### Reference

- [Official Next.js Documentation - Routing](https://nextjs.org/docs/routing/introduction)
- [Next.js 13 Introduction to the App Router](https://nextjs.org/docs/app)
