---
title: "Vue.js Lifecycle Explained"
date: 2024-06-10T22:26:43+09:00
slug: "254-Vue-js-Lifecycle-Explained"
original_url: "https://memoryhub.tistory.com/254"
tistory_id: 254
draft: false
categories: ["데브 프레임워크"]
tags: ["VueJS"]
---

*The Vue.js lifecycle consists of a series of events or hooks that run at different stages of a component's existence, allowing developers to execute code at specific moments from creation to destruction.*

---

### The Big Picture

Imagine you are baking a cake. The cake goes through various stages: preparation (mixing ingredients), baking, and decorating (cooling and icing). Each stage has specific tasks to ensure the cake turns out perfectly. Similarly, Vue.js components go through different stages: creation, mounting, updating, and destruction, each with lifecycle hooks to manage these stages efficiently.

### Core Concepts

1. **Creation**: When the component is being initialized.
2. **Mounting**: When the component is added to the DOM.
3. **Updating**: When reactive data changes and the component needs to re-render.
4. **Destruction**: When the component is being removed from the DOM.

### Detailed Walkthrough

#### Creation

The creation phase involves the initialization of the component. The main lifecycle hooks in this phase are:

1. **beforeCreate()**: Called after the instance is initialized but before data observation and event/watcher setup.
2. **created()**: Called after the instance is created. Data observation, computed properties, and watchers are set up. However, the component is not yet mounted.

Example:

```
new Vue({
    data() {
        return {
            message: 'Hello, world!'
        };
    },
    beforeCreate() {
        console.log('beforeCreate');
    },
    created() {
        console.log('created');
        console.log(this.message); // 'Hello, world!'
    }
});
```

#### Mounting

The mounting phase involves inserting the component into the DOM. The main lifecycle hooks in this phase are:

1. **beforeMount()**: Called right before the mounting begins.
2. **mounted()**: Called after the component is mounted. This is where you can perform DOM-dependent operations, such as fetching data.

Example:

```
new Vue({
    data() {
        return {
            message: 'Hello, world!'
        };
    },
    beforeMount() {
        console.log('beforeMount');
    },
    mounted() {
        console.log('mounted');
        // Perform DOM-dependent operations here
    },
    template: '<div>{{ message }}</div>'
}).$mount('#app');
```

#### Updating

The updating phase occurs whenever reactive data changes, triggering a re-render. The main lifecycle hooks in this phase are:

1. **beforeUpdate()**: Called before the data changes are applied to the DOM.
2. **updated()**: Called after the data changes are applied to the DOM.

Example:

```
new Vue({
    data() {
        return {
            message: 'Hello, world!'
        };
    },
    beforeUpdate() {
        console.log('beforeUpdate');
    },
    updated() {
        console.log('updated');
    },
    methods: {
        updateMessage() {
            this.message = 'Hello, Vue!';
        }
    },
    template: '<div>{{ message }} <button @click="updateMessage">Update</button></div>'
}).$mount('#app');
```

#### Destruction

The destruction phase involves tearing down the component. The main lifecycle hooks in this phase are:

1. **beforeDestroy()**: Called right before the component is destroyed. This is where you can perform cleanup, such as invalidating timers or canceling network requests.
2. **destroyed()**: Called after the component is destroyed. The component's directives and event listeners are removed.

Example:

```
new Vue({
    data() {
        return {
            message: 'Hello, world!'
        };
    },
    beforeDestroy() {
        console.log('beforeDestroy');
    },
    destroyed() {
        console.log('destroyed');
    },
    methods: {
        destroyComponent() {
            this.$destroy();
        }
    },
    template: '<div>{{ message }} <button @click="destroyComponent">Destroy</button></div>'
}).$mount('#app');
```

### Understanding Through an Example

Consider a simple Vue.js component that fetches data when mounted and cleans up when destroyed:

```
new Vue({
    data() {
        return {
            message: 'Loading...',
            intervalId: null
        };
    },
    mounted() {
        this.intervalId = setInterval(() => {
            this.message = 'Data fetched at ' + new Date().toLocaleTimeString();
        }, 1000);
    },
    beforeDestroy() {
        clearInterval(this.intervalId);
    },
    template: '<div>{{ message }}</div>'
}).$mount('#app');
```

In this example, the component sets an interval to update the message every second when mounted and clears the interval when the component is about to be destroyed.

### Conclusion and Summary

The Vue.js lifecycle consists of creation, mounting, updating, and destruction phases, each with specific hooks (`beforeCreate`, `created`, `beforeMount`, `mounted`, `beforeUpdate`, `updated`, `beforeDestroy`, `destroyed`) that allow you to control the component's behavior at different stages. Understanding these hooks helps manage tasks such as data fetching, DOM updates, and cleanup.

### Test Your Understanding

1. What are the four main phases of the Vue.js component lifecycle?
2. Which lifecycle hook would you use to fetch data when the component is inserted into the DOM?
3. Write a simple Vue.js component that logs messages to the console at each lifecycle hook.

### Reference

- [Official Vue.js Documentation - Lifecycle Hooks](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram)
