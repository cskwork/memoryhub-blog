---
title: "What are the differences and similiarties between Vue and React Lifecycle?"
date: 2024-06-10T22:28:13+09:00
slug: "255-What-are-the-differences-and-similiarties-between-Vue-and-React-Lifecycle"
original_url: "https://memoryhub.tistory.com/255"
tistory_id: 255
draft: false
---

*Vue and React both have component lifecycles that manage stages from creation to destruction, but they differ in terminology, structure, and the specifics of their lifecycle hooks.*

---

### The Big Picture

Imagine managing a project with two different sets of guidelines. Both sets aim to organize the project's tasks effectively, but they use different terms and approaches to achieve this. Similarly, Vue and React manage component lifecycles with similar goals but different methodologies and terminologies.

### Core Concepts

1. **Lifecycle Phases**: Both frameworks have phases for creation, updating, and destruction.
2. **Lifecycle Hooks**: Both provide hooks to perform actions at various stages of a component's lifecycle.
3. **Differences in Hook Names and Execution Timing**: Vue and React have different names for similar hooks and sometimes execute them at slightly different times.
4. **Class vs. Functional Components**: React has moved towards functional components with hooks, while Vue traditionally uses a more declarative approach with options objects.

### Detailed Walkthrough

#### Similarities

1. **Phases**:

   - **Creation**: Both frameworks have hooks that are called before and after the component is created.
   - **Updating**: Hooks are available to manage behavior when component state or props change.
   - **Destruction**: Both provide hooks for cleanup tasks before a component is removed.
2. **Lifecycle Hooks**:

   - **Initialization**: `constructor` in React (for class components) and `beforeCreate`/`created` in Vue.
   - **Mounting**: `componentDidMount` in React and `mounted` in Vue.
   - **Updating**: `componentDidUpdate` in React and `updated` in Vue.
   - **Unmounting**: `componentWillUnmount` in React and `beforeDestroy`/`destroyed` in Vue.

#### Differences

1. **Terminology and Hook Names**:

   - **React**:
     - `constructor`
     - `componentDidMount`
     - `shouldComponentUpdate`
     - `componentDidUpdate`
     - `componentWillUnmount`
   - **Vue**:
     - `beforeCreate`
     - `created`
     - `beforeMount`
     - `mounted`
     - `beforeUpdate`
     - `updated`
     - `beforeDestroy`
     - `destroyed`
2. **Functional Components**:

   - **React**: Uses hooks like `useEffect` for managing lifecycle in functional components.
   - **Vue**: Lifecycle hooks are used within the options object or the `setup` function for composition API.
3. **Data and State Management**:

   - **React**: State is managed using `useState` and `useEffect` in functional components.
   - **Vue**: Reactive data is managed using `data`, `methods`, and `computed` properties.

### Understanding Through Examples

#### React Class Component

```
class MyComponent extends React.Component {
    constructor(props) {
        super(props);
        this.state = { count: 0 };
        console.log('Constructor');
    }

    componentDidMount() {
        console.log('Component Did Mount');
    }

    componentDidUpdate(prevProps, prevState) {
        console.log('Component Did Update');
    }

    componentWillUnmount() {
        console.log('Component Will Unmount');
    }

    render() {
        return <h1>Count: {this.state.count}</h1>;
    }
}
```

#### React Functional Component with Hooks

```
function MyComponent() {
    const [count, setCount] = React.useState(0);

    React.useEffect(() => {
        console.log('Component Did Mount');
        return () => {
            console.log('Component Will Unmount');
        };
    }, []);

    React.useEffect(() => {
        console.log('Component Did Update');
    }, [count]);

    return <h1>Count: {count}</h1>;
}
```

#### Vue Component

```
new Vue({
    data() {
        return {
            count: 0
        };
    },
    beforeCreate() {
        console.log('beforeCreate');
    },
    created() {
        console.log('created');
    },
    beforeMount() {
        console.log('beforeMount');
    },
    mounted() {
        console.log('mounted');
    },
    beforeUpdate() {
        console.log('beforeUpdate');
    },
    updated() {
        console.log('updated');
    },
    beforeDestroy() {
        console.log('beforeDestroy');
    },
    destroyed() {
        console.log('destroyed');
    },
    template: '<div>{{ count }}</div>'
}).$mount('#app');
```

### Conclusion and Summary

Both Vue and React have similar lifecycle phases: creation, updating, and destruction. However, they use different terminologies and hook names, and their approaches to managing these phases differ. React supports both class and functional components, with hooks like `useEffect` for lifecycle management in functional components. Vue uses a more declarative approach with an options object or the composition API.

### Test Your Understanding

1. What are the main phases of the Vue and React component lifecycles?
2. Name the equivalent Vue lifecycle hooks for React's `componentDidMount` and `componentWillUnmount`.
3. Write a simple Vue component that logs messages to the console at each lifecycle hook.

### Reference

- [Official Vue.js Documentation - Lifecycle Hooks](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram)
- [Official React Documentation - State and Lifecycle](https://reactjs.org/docs/state-and-lifecycle.html)
