---
title: "What is a React component, and how does it differ from a regular JavaScript function?"
date: 2024-06-10T22:23:31+09:00
slug: "252-What-is-a-React-component-and-how-does-it-differ-from-a-regular-JavaScript-function"
original_url: "https://memoryhub.tistory.com/252"
tistory_id: 252
draft: false
categories: ["Dev Library"]
tags: ["React"]
---

*React components are special JavaScript functions or classes that return JSX to define the structure and behavior of a user interface, whereas regular JavaScript functions do not inherently have this UI-focused capability.*

---

### The Big Picture

Think of a React component as a self-contained, reusable building block for a web application, much like a LEGO piece that can be used to build complex structures. In contrast, a regular JavaScript function is more like a tool in your toolbox: it performs specific tasks but isn't inherently designed to be a piece of a larger, visual structure.

### Core Concepts

1. **Definition and Purpose**: React components are specifically designed to manage and display parts of a user interface.
2. **Return Value**: React components return JSX, which is a mix of HTML-like syntax and JavaScript.
3. **State and Props**: React components manage their own state and receive data via props, allowing them to dynamically update the UI.
4. **Lifecycle Methods**: Class-based React components have lifecycle methods to manage their behavior at different stages (mounting, updating, unmounting).

### Detailed Walkthrough

#### Definition and Purpose

A React component can be defined as a function or a class. Its primary purpose is to describe what the UI should look like:

```
// Functional component
function Welcome(props) {
    return <h1>Hello, {props.name}!</h1>;
}

// Class component
class Welcome extends React.Component {
    render() {
        return <h1>Hello, {this.props.name}!</h1>;
    }
}
```

In contrast, a regular JavaScript function performs computations or manipulates data:

```
function add(a, b) {
    return a + b;
}
```

#### Return Value

A React component returns JSX:

```
function Greeting() {
    return <h1>Good Morning!</h1>;
}
```

A regular JavaScript function returns a value, which could be a string, number, object, etc.:

```
function getGreeting() {
    return "Good Morning!";
}
```

#### State and Props

React components can have state and receive props:

```
function Counter() {
    const [count, setCount] = React.useState(0);
    return (
        <div>
            <p>You clicked {count} times</p>
            <button onClick={() => setCount(count + 1)}>Click me</button>
        </div>
    );
}
```

Regular JavaScript functions don't manage state in this way:

```
let count = 0;
function incrementCount() {
    count += 1;
    console.log(count);
}
```

#### Lifecycle Methods

Class-based React components have lifecycle methods such as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` to manage their behavior at different stages:

```
class Timer extends React.Component {
    constructor(props) {
        super(props);
        this.state = { seconds: 0 };
    }

    tick() {
        this.setState(state => ({
            seconds: state.seconds + 1
        }));
    }

    componentDidMount() {
        this.interval = setInterval(() => this.tick(), 1000);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render() {
        return (
            <div>
                Seconds: {this.state.seconds}
            </div>
        );
    }
}
```

Regular JavaScript functions don't have lifecycle methods:

```
let seconds = 0;
function tick() {
    seconds += 1;
    console.log(seconds);
}
setInterval(tick, 1000);
```

### Understanding Through an Example

Consider a simple React component that displays a greeting message:

```
function Greeting(props) {
    return <h1>Hello, {props.name}!</h1>;
}

const element = <Greeting name="Alice" />;
ReactDOM.render(element, document.getElementById('root'));
```

In this example, `Greeting` is a React component that takes a `name` prop and returns JSX to display a message. It can be reused with different `name` values to display different messages.

### Conclusion and Summary

A React component is a special kind of JavaScript function or class designed to manage and display parts of a user interface. Unlike regular JavaScript functions, React components return JSX, manage their own state, and can utilize props to dynamically update the UI. They are integral to building interactive, reusable pieces of a web application.

### Test Your Understanding

1. What is the main purpose of a React component?
2. How does a React component handle state and props differently from a regular JavaScript function?
3. Write a simple React component that takes a `title` and `content` prop and displays them inside an `<h2>` and a `<p>` tag, respectively.

### Reference

- [Official React Documentation - Components and Props](https://reactjs.org/docs/components-and-props.html)
