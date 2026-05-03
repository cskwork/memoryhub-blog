---
title: "JSX Introduced"
date: 2024-06-10T22:19:49+09:00
slug: "251-JSX-Introduced"
original_url: "https://memoryhub.tistory.com/251"
tistory_id: 251
draft: false
---

*JSX is a syntax extension for JavaScript that looks similar to XML or HTML and is used in React to describe the UI structure in a declarative way.*

---

### The Big Picture

Imagine you are describing the layout of a house. Traditional JavaScript lets you describe each element individually, like writing a list of instructions for a builder. JSX, on the other hand, allows you to draw a blueprint where you can see the entire layout at once, making it easier to understand and visualize the final product.

### Core Concepts

1. **JSX Syntax**: Allows you to write HTML-like code directly in JavaScript.
2. **Embedding Expressions**: You can embed JavaScript expressions inside JSX.
3. **Components**: JSX is used to define components in React.
4. **Attributes and Props**: JSX allows you to pass data to components using attributes, which are called props in React.
5. **Conditional Rendering**: JSX supports conditional rendering to dynamically display different UI elements.

### Detailed Walkthrough

#### JSX Syntax

JSX lets you write HTML-like syntax in JavaScript:

```
const element = <h1>Hello, world!</h1>;
```

This syntax is transformed by tools like Babel into standard JavaScript that React can understand.

#### Embedding Expressions

You can embed any JavaScript expression inside JSX using curly braces `{}`:

```
const name = "Alice";
const element = <h1>Hello, {name}!</h1>;
```

Here, `{name}` is replaced by the value of the `name` variable.

#### Components

JSX is used to define React components. A component is a function or class that returns JSX:

```
function Welcome(props) {
    return <h1>Hello, {props.name}!</h1>;
}
```

This `Welcome` component can be used like a regular HTML tag:

```
const element = <Welcome name="Alice" />;
```

#### Attributes and Props

JSX allows you to pass attributes to components, which are known as props:

```
function Welcome(props) {
    return <h1>Hello, {props.name}!</h1>;
}

const element = <Welcome name="Alice" />;
```

Here, `name="Alice"` is a prop passed to the `Welcome` component.

#### Conditional Rendering

JSX supports conditional rendering, allowing you to display different UI elements based on certain conditions:

```
function Greeting(props) {
    if (props.isLoggedIn) {
        return <h1>Welcome back!</h1>;
    } else {
        return <h1>Please sign up.</h1>;
    }
}

const element = <Greeting isLoggedIn={true} />;
```

### Understanding Through an Example

Consider a simple example where you want to display a list of items:

```
function ItemList(props) {
    const items = props.items;
    return (
        <ul>
            {items.map((item) => <li key={item.toString()}>{item}</li>)}
        </ul>
    );
}

const items = ["Apple", "Banana", "Cherry"];
const element = <ItemList items={items} />;
```

In this example, `ItemList` is a component that takes an array of items as a prop and displays each item in a list. The `map` function is used to transform each item into a `<li>` element.

### Conclusion and Summary

JSX is a syntax extension for JavaScript that allows you to write HTML-like code directly within your JavaScript. It makes it easier to visualize and build the UI by combining the power of JavaScript with the declarative nature of HTML. Key features of JSX include embedding expressions, defining components, passing props, and conditional rendering.

### Test Your Understanding

1. What is the purpose of JSX in React?
2. How do you embed a JavaScript expression inside JSX?
3. Write a simple JSX component that takes a `title` prop and displays it inside an `<h2>` tag.

### Reference

- [Official React Documentation - Introducing JSX](https://reactjs.org/docs/introducing-jsx.html)
