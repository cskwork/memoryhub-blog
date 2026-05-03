---
title: "NextJS App Router Web app Example"
date: 2024-06-22T11:51:34+09:00
slug: "307-NextJS-App-Router-Web-app-Example"
original_url: "https://memoryhub.tistory.com/307"
tistory_id: 307
draft: false
---

*Imagine a bustling city with well-planned districts, efficient transportation, and clear signage - that's the essence of a well-organized Next.js app using the App Router web applications.*

**The Big Picture:**  
Next.js's App Router represents a paradigm shift in how React applications are structured and routed. It's like upgrading from a simple street grid to a multi-level, interconnected city infrastructure. This new approach emphasizes a file-system based routing, co-location of related files, and built-in support for server-side rendering and API routes. For production-grade complex commercial web applications, this translates to improved performance, better code organization, and enhanced developer experience.

**Core Concepts:**

1. File-system based routing
2. Server Components and Client Components
3. Data Fetching and Caching
4. Layouts and Nested Routing
5. Route Handlers (API Routes)
6. Middleware
7. Project Structure and Organization

**Detailed Walkthrough:**

**1. File-system based routing:**  
In the App Router, your file structure directly maps to your URL structure. It's like a city where the street names and building numbers directly correspond to the services they offer.

For example:

```
app/
  dashboard/
    page.js
    layout.js
  blog/
    [slug]/
      page.js
    page.js
  page.js
```

Here, `app/dashboard/page.js` would correspond to the `/dashboard` route, and `app/blog/[slug]/page.js` would handle dynamic blog post URLs like `/blog/my-first-post`.

**2. Server Components and Client Components:**  
Next.js 13+ introduces a clear distinction between Server and Client Components. This is like having specialized zones in a city - some areas (Server Components) are pre-built and highly efficient, while others (Client Components) are interactive and customizable on the spot.

Server Component example:

```
async function BlogPosts() {
  const posts = await fetchBlogPosts(); // This runs on the server
  return (
    <ul>
      {posts.map(post => <li key={post.id}>{post.title}</li>)}
    </ul>
  );
}
```

Client Component example:

```
'use client'; // This directive marks it as a Client Component

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  );
}
```

**3. Data Fetching and Caching:**  
Next.js provides powerful data fetching mechanisms with built-in caching. It's like having a smart delivery system in your city that knows when to fetch fresh goods and when to use stored supplies.

```
async function getData() {
  const res = await fetch('https://api.example.com/data', { next: { revalidate: 60 } });
  return res.json();
}

export default async function Page() {
  const data = await getData();
  return <main>{/* use data */}</main>;
}
```

**4. Layouts and Nested Routing:**  
Layouts allow you to define common UI elements for multiple pages. It's like designing a consistent architectural style for different districts in your city.

```
// app/dashboard/layout.js
export default function DashboardLayout({ children }) {
  return (
    <div>
      <nav>{/* Dashboard navigation */}</nav>
      <main>{children}</main>
    </div>
  );
}
```

**5. Route Handlers (API Routes):**  
Route Handlers are the new way to create API endpoints. They're like specialized service centers in your city, handling specific requests efficiently.

```
// app/api/users/route.js
export async function GET(request) {
  const users = await getUsers();
  return new Response(JSON.stringify(users));
}
```

**6. Middleware:**  
Middleware in Next.js allows you to run code before a request is completed. It's like having security checkpoints or traffic controllers in your city.

```
// middleware.js
import { NextResponse } from 'next/server';

export function middleware(request) {
  if (request.nextUrl.pathname.startsWith('/api/')) {
    return NextResponse.next();
  }
  return NextResponse.redirect(new URL('/home', request.url));
}
```

**7. Project Structure and Organization:**  
For complex commercial applications, a well-organized project structure is crucial. Here's an example:

```
src/
  app/
    (auth)/
      login/
        page.js
      register/
        page.js
    (dashboard)/
      layout.js
      page.js
      analytics/
        page.js
      settings/
        page.js
    api/
      users/
        route.js
    layout.js
    page.js
  components/
    ui/
      Button.js
      Card.js
    forms/
      LoginForm.js
  lib/
    utils.js
    api.js
  styles/
    globals.css
  types/
    index.ts
```

This structure uses route groups (parentheses in folder names) to organize related routes without affecting the URL structure. It also separates reusable components, utility functions, and types for better maintainability.

**Understanding Through an Example:**  
Let's create a simple dashboard page for our complex web application:

```
// src/app/(dashboard)/page.js
import { Suspense } from 'react';
import Loading from '@/components/ui/Loading';
import DashboardMetrics from '@/components/dashboard/DashboardMetrics';
import RecentActivity from '@/components/dashboard/RecentActivity';

export default function DashboardPage() {
  return (
    <div className="dashboard-container">
      <h1>Welcome to Your Dashboard</h1>
      <Suspense fallback={<Loading />}>
        <DashboardMetrics />
      </Suspense>
      <Suspense fallback={<Loading />}>
        <RecentActivity />
      </Suspense>
    </div>
  );
}

// src/components/dashboard/DashboardMetrics.js
async function fetchMetrics() {
  // Fetch data from your API
}

export default async function DashboardMetrics() {
  const metrics = await fetchMetrics();
  return (
    <div className="metrics-grid">
      {metrics.map(metric => (
        <div key={metric.id} className="metric-card">
          <h3>{metric.name}</h3>
          <p>{metric.value}</p>
        </div>
      ))}
    </div>
  );
}

// src/components/dashboard/RecentActivity.js
'use client';
import { useState, useEffect } from 'react';
import { fetchRecentActivity } from '@/lib/api';

export default function RecentActivity() {
  const [activities, setActivities] = useState([]);

  useEffect(() => {
    fetchRecentActivity().then(setActivities);
  }, []);

  return (
    <ul className="activity-list">
      {activities.map(activity => (
        <li key={activity.id}>{activity.description}</li>
      ))}
    </ul>
  );
}
```

This example demonstrates:

- Use of Server Components for data fetching (`DashboardMetrics`)
- Client Components for interactive elements (`RecentActivity`)
- Suspense for loading states
- Separation of concerns with modular components

**Conclusion and Summary:**  
Organizing a Next.js app with App Router for complex commercial applications involves leveraging file-system based routing, separating server and client components, efficient data fetching and caching, and thoughtful project structure. It's about creating a well-organized, performant, and maintainable codebase that can scale with your application's growing complexity.

**Test Your Understanding:**

1. How does file-system based routing in Next.js App Router differ from the traditional pages directory approach?
2. What are the key differences between Server Components and Client Components, and when would you use each?
3. How can you implement data fetching and caching in a Next.js App Router project?
4. Describe a scenario where you would use route handlers (API routes) in a complex commercial web application

**Reference:**  
For the most up-to-date and comprehensive information on Next.js App Router and best practices for complex applications, I recommend referring to the official Next.js documentation: <https://nextjs.org/docs>. This resource is continuously updated with the latest features, patterns, and examples for building production-grade applications with Next.js.

---
