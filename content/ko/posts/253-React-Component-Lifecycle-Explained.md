---
title: "React Component Lifecycle Explained"
date: 2024-06-10T22:25:07+09:00
slug: "253-React-Component-Lifecycle-Explained"
original_url: "https://memoryhub.tistory.com/253"
tistory_id: 253
draft: false
categories: ["데브 라이브러리"]
tags: ["React"]
---

*The React component lifecycle consists of a series of methods that are invoked at different stages of a component's existence, allowing you to control its behavior from creation to destruction.*

---

### The Big Picture

Imagine you’re organizing a stage play. The lifecycle of the play involves various stages: setup (mounting), running the play (updating), and teardown (unmounting). Each stage has specific tasks to ensure the play runs smoothly. Similarly, React components go through mounting, updating, and unmounting phases, each with specific lifecycle methods you can utilize to manage their behavior.

### Core Concepts

1. **Mounting**: When a component is created and inserted into the DOM.
2. **Updating**: When a component is re-rendered due to changes in props or state.
3. **Unmounting**: When a component is removed from the DOM.

### Detailed Walkthrough

#### Mounting

Mounting is the phase when a component is created and inserted into the DOM. The main lifecycle methods in this phase are:

1. **constructor()**: Initializes the component's state and binds methods.
2. **static getDerivedStateFromProps()**: Updates the state based on initial props (rarely used).
3. **render()**: Returns the JSX that defines the component’s UI.
4. **componentDidMount()**: Invoked once the component is inserted into the DOM. Ideal for making network requests or initializing libraries.

Example:

```
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = { count: 0 };
        console.log('Constructor');
    }

    static getDerivedStateFromProps(props, state) {
        console.log('getDerivedStateFromProps');
        return null;
    }

    componentDidMount() {
        console.log('Component Did Mount');
    }

    render() {
        console.log('Render');
        return <h1>Count: {this.state.count}</h1>;
    }
}
```

#### Updating

Updating occurs when a component's state or props change, triggering a re-render. The main lifecycle methods in this phase are:

1. **static getDerivedStateFromProps()**: Also called during updates to update the state based on props.
2. **shouldComponentUpdate()**: Determines if the component should re-render based on changes in props or state. Returning `false` skips the re-render.
3. **render()**: Same as in the mounting phase; returns the JSX.
4. **getSnapshotBeforeUpdate()**: Captures some information (e.g., scroll position) before the DOM is updated.
5. **componentDidUpdate()**: Invoked after the component's updates are flushed to the DOM. Ideal for DOM manipulations or network requests based on prop changes.

Example:

```
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = { count: 0 };
    }

    static getDerivedStateFromProps(props, state) {
        return null;
    }

    shouldComponentUpdate(nextProps, nextState) {
        return nextState.count !== this.state.count;
    }

    getSnapshotBeforeUpdate(prevProps, prevState) {
        return null;
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        console.log('Component Did Update');
    }

    render() {
        return (
            <div>
                <h1>Count: {this.state.count}</h1>
                <button onClick={() => this.setState({ count: this.state.count + 1 })}>Increment</button>
            </div>
        );
    }
}
```

#### Unmounting

Unmounting is the phase when a component is removed from the DOM. The main lifecycle method in this phase is:

1. **componentWillUnmount()**: Invoked immediately before the component is removed from the DOM. Ideal for cleanup tasks such as invalidating timers, canceling network requests, or cleaning up subscriptions.

Example:

```
class MyComponent extends React.Component {
    componentWillUnmount() {
        console.log('Component Will Unmount');
    }

    render() {
        return <h1>Goodbye, World!</h1>;
    }
}
```

### Understanding Through an Example

Consider a timer component that starts counting seconds when it mounts and stops when it unmounts:

```
class Timer extends React.Component {
    constructor(props) {
        super(props);
        this.state = { seconds: 0 };
    }

    componentDidMount() {
        this.interval = setInterval(() => this.setState({ seconds: this.state.seconds + 1 }), 1000);
    }

    componentDidUpdate() {
        console.log(`Timer updated: ${this.state.seconds} seconds`);
    }

    componentWillUnmount() {
        clearInterval(this.interval);
    }

    render() {
        return <h1>Seconds: {this.state.seconds}</h1>;
    }
}
```

### Conclusion and Summary

The React component lifecycle consists of three main phases: mounting, updating, and unmounting. Each phase has specific lifecycle methods that allow you to control the behavior of components at different stages of their existence. Understanding these methods helps you manage the component's setup, update, and cleanup tasks efficiently.

### Test Your Understanding

1. What are the three main phases of the React component lifecycle?
2. What lifecycle method would you use to make an API call when the component is first rendered?
3. Write a simple component that logs a message to the console every time it updates.

### Reference

- [Official React Documentation - State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html)
- [React Component Lifecycle Methods](https://reactjs.org/docs/react-component.html#the-component-lifecycle)
