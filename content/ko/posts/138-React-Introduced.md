---
title: "React Introduced"
date: 2024-05-27T19:37:07+09:00
slug: "138-React-Introduced"
original_url: "https://memoryhub.tistory.com/138"
tistory_id: 138
draft: false
---

*React is a JavaScript library for building user interfaces, especially for single-page applications where data changes over time.*

### The Big Picture

Imagine building a complex structure with Lego blocks. Each block can be customized, and you can piece them together to form various structures. In the world of web development, React allows you to create user interfaces in a similar modular way, where each "block" or component can be independently created and managed.

### Core Concepts

1. **Components**: These are the building blocks of a React application. Think of them as individual Lego blocks that can be combined to create a complex UI.
2. **JSX**: JavaScript XML, a syntax extension that allows you to write HTML-like code within JavaScript.
3. **State**: An object that determines how a component renders and behaves.
4. **Props**: Short for properties, these are read-only attributes that are passed from parent components to child components.
5. **Virtual DOM**: A lightweight copy of the real DOM that React uses to optimize rendering and improve performance.

### Detailed Walkthrough

1. **Components**: In React, a component can be a function or a class. Here’s a simple functional component:

   ```
   function Welcome(props) {
       return <h1>Hello, {props.name}</h1>;
   }
   ```

   This component takes `props` (properties) and returns a React element.
2. **JSX**: It looks like HTML but it's actually JavaScript.

   ```
   const element = <h1>Hello, world!</h1>;
   ```

   Under the hood, this is transformed into JavaScript calls:

   ```
   const element = React.createElement('h1', null, 'Hello, world!');
   ```
3. **State**: State is used to store data that might change over time. Here’s an example with a class component:

   ```
   class Clock extends React.Component {
       constructor(props) {
           super(props);
           this.state = {date: new Date()};
       }

       componentDidMount() {
           this.timerID = setInterval(
               () => this.tick(),
               1000
           );
       }

       componentWillUnmount() {
           clearInterval(this.timerID);
       }

       tick() {
           this.setState({
               date: new Date()
           });
       }

       render() {
           return (
               <div>
                   <h1>Hello, world!</h1>
                   <h2>It is {this.state.date.toLocaleTimeString()}.</h2>
               </div>
           );
       }
   }
   ```

   Here, the `Clock` component updates its `state` every second.
4. **Props**: Props are passed to components like this:

   ```
   function App() {
       return <Welcome name="Sara" />;
   }
   ```

   The `Welcome` component receives `props.name` and renders "Hello, Sara".
5. **Virtual DOM**: React keeps a virtual representation of the UI in memory and syncs it with the real DOM. This process is called reconciliation. When the state of an object changes, React updates the virtual DOM first, calculates the minimal set of changes needed to update the real DOM, and then makes those changes. This approach significantly boosts performance.

### Understanding Through an Example

Let's create a simple counter component that increments a number when a button is clicked.

```
import React, { useState } from 'react';

function Counter() {
    const [count, setCount] = useState(0);

    return (
        <div>
            <p>You clicked {count} times</p>
            <button onClick={() => setCount(count + 1)}>
                Click me
            </button>
        </div>
    );
}

export default Counter;
```

Here, `useState` is a Hook (a special function in React) that lets you add state to functional components. Clicking the button updates the `count` state, which causes the component to re-render with the new value.

### Conclusion and Summary

React is a powerful library for building user interfaces using components, which can be thought of as modular Lego blocks. It uses JSX for a more readable syntax, state and props for managing data, and the virtual DOM for efficient updates. By understanding these core concepts and seeing how they interact, you can build dynamic and responsive web applications.

### Test Your Understanding

1. What is a React component, and how does it differ from a regular JavaScript function?
2. Explain how JSX is transformed into JavaScript.
3. How does the virtual DOM improve performance?
4. Create a simple React component that displays a message passed as a prop.

For further learning, you can refer to the [React official documentation](https://reactjs.org/docs/getting-started.html).
