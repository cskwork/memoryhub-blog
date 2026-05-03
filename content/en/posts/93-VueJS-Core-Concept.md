---
title: "VueJS Core Concept"
date: 2024-05-26T10:52:00+09:00
slug: "93-VueJS-Core-Concept"
original_url: "https://memoryhub.tistory.com/93"
tistory_id: 93
draft: false
---

*Let's dive deeper into each core concept of Vue.js, exploring their technical details, advanced usage, and best practices.*

### The Big Picture

Imagine building a web application like managing a complex garden. Vue.js helps you organize, water, and grow each plant (component) efficiently, ensuring a healthy and manageable garden (application).

### Core Concepts

1. **Vue Instance**
2. **Template**
3. **Data**
4. **Methods**
5. **Computed Properties**
6. **Components**

### Detailed Walkthrough

#### 1. Vue Instance

The Vue instance is the core of any Vue application. It is created by calling `new Vue()` and can include various options such as `data`, `methods`, `computed`, `watch`, `template`, `el`, and lifecycle hooks (`created`, `mounted`, etc.).

```
new Vue({
  el: '#app', // element to mount the Vue instance
  data: {
    message: 'Hello Vue!'
  },
  methods: {
    greet: function() {
      alert(this.message);
    }
  },
  created: function() {
    console.log('Vue instance created!');
  }
});
```

- **el**: The DOM element that the Vue instance will be mounted on.
- **data**: An object containing application data.
- **methods**: Functions for user-defined actions.
- **created**: A lifecycle hook called after the instance is created.

#### 2. Template

Templates in Vue.js use an HTML-based syntax that integrates with the Vue instance. They allow you to declaratively bind the DOM to the instance's data. Vue templates support directives like `v-bind`, `v-model`, `v-for`, and `v-if`.

```
<div id="app">
  <p>{{ message }}</p>
  <button @click="greet">Greet</button>
</div>
```

- **Directives**: Special tokens prefixed with `v-` used in templates to reactively update the DOM.
  - `v-bind`: Dynamically bind an attribute to an expression.
  - `v-model`: Create a two-way binding on an input element.
  - `v-for`: Render a list of items using an array.
  - `v-if`: Conditionally render an element.

#### 3. Data

Data is central to Vue's reactivity system. When data changes, the view updates automatically. Data can be simple variables or complex objects.

```
data: {
  message: 'Hello Vue!',
  todos: [
    { text: 'Learn JavaScript' },
    { text: 'Learn Vue.js' },
    { text: 'Build something awesome' }
  ]
}
```

#### 4. Methods

Methods are functions defined within the Vue instance that can be used for event handling, data manipulation, and more.

```
methods: {
  addTodo: function() {
    this.todos.push({ text: this.newTodoText });
    this.newTodoText = '';
  },
  deleteTodo: function(index) {
    this.todos.splice(index, 1);
  }
}
```

- **`this` keyword**: Refers to the Vue instance, giving access to data properties and other methods.

#### 5. Computed Properties

Computed properties are derived from data properties and are cached based on their dependencies. They are recalculated only when their dependencies change.

```
computed: {
  reversedMessage: function() {
    return this.message.split('').reverse().join('');
  },
  todoCount: function() {
    return this.todos.length;
  }
}
```

- **Caching**: Computed properties are cached until their dependencies change, making them efficient for performance.

#### 6. Components

Components are reusable, self-contained Vue instances with their own data, methods, and lifecycle hooks. They help break the application into smaller, manageable pieces.

**Defining a Component**:

```
Vue.component('todo-item', {
  props: ['todo'],
  template: '<li>{{ todo.text }}</li>'
});
```

- **Props**: Short for properties, they allow parent components to pass data to child components.
- **Template**: Defines the structure of the component.

**Using a Component**:

```
<div id="app">
  <ol>
    <todo-item v-for="item in todos" :todo="item" :key="item.id"></todo-item>
  </ol>
</div>
```

### Advanced Topics

#### Directives

Vue provides a set of built-in directives, and you can also create custom directives.

```
Vue.directive('focus', {
  inserted: function(el) {
    el.focus();
  }
});
```

**Usage**:

```
<input v-focus>
```

#### Mixins

Mixins are a flexible way to distribute reusable functionalities in Vue components.

```
var myMixin = {
  created: function() {
    this.hello();
  },
  methods: {
    hello: function() {
      console.log('Hello from mixin!');
    }
  }
};

new Vue({
  mixins: [myMixin]
});
```

#### Vue Router

Vue Router is the official router for Vue.js, enabling navigation between different pages in a single-page application.

```
const routes = [
  { path: '/home', component: Home },
  { path: '/about', component: About }
];

const router = new VueRouter({
  routes
});

new Vue({
  router,
  render: h => h(App)
}).$mount('#app');
```

#### Vuex

Vuex is a state management pattern + library for Vue.js applications. It serves as a centralized store for all the components in an application.

```
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment(state) {
      state.count++;
    }
  }
});

new Vue({
  store,
  computed: {
    count() {
      return this.$store.state.count;
    }
  },
  methods: {
    increment() {
      this.$store.commit('increment');
    }
  }
}).$mount('#app');
```

### Conclusion and Summary

We have gone deeper into Vue.js, covering advanced aspects such as directives, mixins, Vue Router, and Vuex. By understanding the core concepts and their advanced applications, you can build more efficient and maintainable applications.

### Test Your Understanding

1. Explain the role of directives in Vue.js and how you can create a custom directive.
2. Describe the purpose of mixins and provide an example of how they can be used.
3. How does Vue Router help in building single-page applications?
4. What is Vuex, and why would you use it in a Vue.js application?
5. Modify the provided to-do list example to include a filter that shows only completed tasks.

### Reference

For further learning, explore the [official Vue.js documentation](https://vuejs.org/v2/guide/) and [Vuex documentation](https://vuex.vuejs.org/), which provide comprehensive guides and examples.
