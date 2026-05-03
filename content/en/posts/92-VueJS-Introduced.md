---
title: "VueJS Introduced"
date: 2024-05-26T10:49:08+09:00
slug: "92-VueJS-Introduced"
original_url: "https://memoryhub.tistory.com/92"
tistory_id: 92
draft: false
categories: ["Dev Framework"]
tags: ["VueJS"]
---

*Vue.js is a progressive JavaScript framework for building user interfaces, designed to be incrementally adoptable, meaning you can use as much or as little of it as you want. Let's break it down step by step.*

### The Big Picture

Imagine building a web application is like constructing a house. Vue.js is a toolset that helps you build this house with reusable parts, making it easier and faster to develop and maintain. Just like using prefabricated walls or modular furniture, Vue.js allows you to create components that can be reused throughout your application.

### Core Concepts

1. **Vue Instance**: The Vue instance is like the foundation of your house. It's where everything begins and provides the structure for your application.
2. **Template**: Think of the template as the blueprint of your house. It defines what the final structure will look like.
3. **Data**: Data in Vue.js is like the raw materials used to build your house. It's the information that drives the appearance and behavior of your application.
4. **Methods**: Methods are the tools you use to shape your raw materials. They define how you interact with and manipulate your data.
5. **Computed Properties**: These are like automatic systems in your house (e.g., heating or lighting systems) that adjust themselves based on certain conditions.
6. **Components**: Components are the prefabricated parts of your house. Each component is a self-contained part of the application with its own structure, data, and behavior.

### Detailed Walkthrough

#### 1. Vue Instance

The Vue instance is created using the `new Vue()` constructor. This is where you define the core parts of your Vue application, such as the element to mount to, the data, methods, and lifecycle hooks.

```
new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
});
```

#### 2. Template

The template is an HTML-like syntax that Vue uses to define your user interface. It's part of your Vue instance and can be directly written in the `template` property or in the HTML file.

```
<div id="app">
  {{ message }}
</div>
```

#### 3. Data

Data in Vue.js is an object that holds the application's state. When data changes, Vue updates the DOM to reflect these changes.

```
data: {
  message: 'Hello Vue!'
}
```

#### 4. Methods

Methods are functions defined within the Vue instance. They are used to perform actions and manipulate data.

```
methods: {
  reverseMessage: function() {
    this.message = this.message.split('').reverse().join('');
  }
}
```

#### 5. Computed Properties

Computed properties are used for values that depend on other data properties. They are cached based on their dependencies and only re-evaluate when those dependencies change.

```
computed: {
  reversedMessage: function() {
    return this.message.split('').reverse().join('');
  }
}
```

#### 6. Components

Components are reusable instances with their own data and methods. They allow you to split your application into smaller, more manageable pieces.

```
Vue.component('todo-item', {
  template: '<li>This is a todo</li>'
});
```

### Understanding Through an Example

Let's create a simple Vue.js application that displays a list of to-dos and allows you to add new ones.

```
<!DOCTYPE html>
<html>
<head>
  <title>Vue.js Example</title>
  <script src="https://cdn.jsdelivr.net/npm/vue@2"></script>
</head>
<body>
  <div id="app">
    <ul>
      <li v-for="todo in todos">{{ todo.text }}</li>
    </ul>
    <input v-model="newTodoText" placeholder="Add a todo">
    <button @click="addTodo">Add</button>
  </div>

  <script>
    new Vue({
      el: '#app',
      data: {
        todos: [
          { text: 'Learn JavaScript' },
          { text: 'Learn Vue.js' },
          { text: 'Build something awesome' }
        ],
        newTodoText: ''
      },
      methods: {
        addTodo: function() {
          this.todos.push({ text: this.newTodoText });
          this.newTodoText = '';
        }
      }
    });
  </script>
</body>
</html>
```

### Conclusion and Summary

We started with the big picture analogy of building a house to understand Vue.js as a framework that allows for modular and incremental development. We covered the core concepts: Vue Instance, Template, Data, Methods, Computed Properties, and Components. Then we walked through detailed code examples to illustrate these concepts in action. Finally, we applied our knowledge to build a simple to-do application.

### Test Your Understanding

1. What is the role of the Vue instance in a Vue.js application?
2. How do templates work in Vue.js, and what is their purpose?
3. Explain the difference between methods and computed properties in Vue.js.
4. Describe how components help in building a Vue.js application.
5. Modify the provided to-do list example to allow deleting items from the list.

### Reference

For further learning, you can explore the [official Vue.js documentation](https://vuejs.org/v2/guide/) which provides comprehensive guides and examples.
