---
title: "Provide an example of when you would use an API route in Next.js."
date: 2024-06-11T23:26:07+09:00
slug: "276-Provide-an-example-of-when-you-would-use-an-API-route-in-Next-js"
original_url: "https://memoryhub.tistory.com/276"
tistory_id: 276
draft: false
categories: ["데브 프레임워크"]
tags: ["NextJS"]
---

*An API route in Next.js is used to create serverless functions that handle backend logic, such as fetching data from a database or an external API, without the need for a separate backend server.*

### The Big Picture

Imagine you have a vending machine (your application) that provides different types of snacks (data). An API route in Next.js acts like the internal mechanism of the vending machine, handling the process of selecting and dispensing snacks based on the user's request. It abstracts away the complex inner workings, providing a simple interface for the user to interact with.

### Core Concepts

1. **Serverless Functions:** Next.js API routes are serverless functions that run on-demand, handling backend tasks without maintaining a server.
2. **Integration with Frontend:** They allow seamless integration between frontend and backend logic within the same Next.js application.
3. **Data Fetching:** API routes can be used to fetch data from databases, external APIs, or perform any server-side logic needed by the frontend.

### Detailed Walkthrough

#### Setting Up an API Route in Next.js

To create an API route in Next.js, you need to add a file to the `pages/api` directory. Each file in this directory corresponds to an API endpoint.

#### Example Scenario: Fetching Weather Data

Let's create an API route that fetches weather data from an external API.

1. **Create the API Route**

   Create a new file `pages/api/weather.js`:

   ```
   // pages/api/weather.js
   import fetch from 'node-fetch';

   export default async function handler(req, res) {
     const { city } = req.query;

     if (!city) {
       res.status(400).json({ error: 'City parameter is required' });
       return;
     }

     try {
       const response = await fetch(`https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=${city}`);
       const data = await response.json();

       if (response.ok) {
         res.status(200).json(data);
       } else {
         res.status(response.status).json({ error: data.error.message });
       }
     } catch (error) {
       res.status(500).json({ error: 'Internal Server Error' });
     }
   }
   ```

   In this example:

   - The API route fetches weather data for a given city.
   - The city name is expected as a query parameter (`req.query.city`).
   - The route uses the `node-fetch` library to make the HTTP request to an external weather API.
   - Appropriate responses are sent back based on the success or failure of the request.
2. **Using the API Route in a Next.js Page**

   Next, create a page that uses this API route to display weather data. Create a new file `pages/weather.js`:

   ```
   // pages/weather.js
   import { useState } from 'react';

   export default function Weather() {
     const [city, setCity] = useState('');
     const [weather, setWeather] = useState(null);
     const [error, setError] = useState(null);

     const fetchWeather = async () => {
       setError(null);
       setWeather(null);
       try {
         const response = await fetch(`/api/weather?city=${city}`);
         const data = await response.json();
         if (response.ok) {
           setWeather(data);
         } else {
           setError(data.error);
         }
       } catch (error) {
         setError('Failed to fetch weather data');
       }
     };

     return (
       <div>
         <h1>Weather App</h1>
         <input
           type="text"
           value={city}
           onChange={(e) => setCity(e.target.value)}
           placeholder="Enter city name"
         />
         <button onClick={fetchWeather}>Get Weather</button>
         {error && <p style={{ color: 'red' }}>{error}</p>}
         {weather && (
           <div>
             <h2>{weather.location.name}</h2>
             <p>{weather.current.temp_c}°C</p>
             <p>{weather.current.condition.text}</p>
           </div>
         )}
       </div>
     );
   }
   ```

   In this example:

   - A text input allows the user to enter the city name.
   - A button triggers the `fetchWeather` function to call the API route.
   - The fetched weather data is displayed, or an error message is shown if something goes wrong.

### Conclusion and Summary

API routes in Next.js are used to handle backend logic within a Next.js application. They enable you to:

- Create serverless functions that run on-demand.
- Fetch data from databases or external APIs.
- Integrate seamlessly with frontend components, providing a simple interface for complex operations.

### Test Your Understanding

1. How do you handle query parameters in a Next.js API route?
2. What are the benefits of using serverless functions for backend logic?
3. How can you handle errors gracefully in an API route?

### Reference

For further reading and official documentation, refer to [Next.js API Routes](https://nextjs.org/docs/api-routes/introduction).
