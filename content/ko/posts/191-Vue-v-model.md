---
title: "Vue (v-model)"
date: 2024-06-05T09:25:23+09:00
slug: "191-Vue-v-model"
original_url: "https://memoryhub.tistory.com/191"
tistory_id: 191
draft: false
---

*In this explanation, we'll explore how Vue.js' `v-model` works, its core concepts, and its use through a detailed walkthrough and example, akin to understanding the workings of a two-way mirror.*

### The Big Picture

Imagine `v-model` as a two-way mirror. Just like a two-way mirror reflects images on both sides, `v-model` creates a two-way data binding between a form input and a piece of data in the Vue instance. Changes in the input update the data, and changes in the data update the input.

### Core Concepts

1. **Two-Way Data Binding**: This means that any changes to the input element are instantly reflected in the Vue instance data, and vice versa.
2. **Syntactic Sugar**: `v-model` is essentially a shorthand for binding a value and emitting input events.
3. **Modifiers**: `v-model` can use modifiers to tweak the behavior of the data binding, such as `lazy`, `number`, and `trim`.

### Detailed Walkthrough

#### Basic Usage

The simplest way to use `v-model` is within an input element. Here's a basic example:

```
<div id="app">
  <input v-model="message">
  <p>The message is: {{ message }}</p>
</div>

<script>
new Vue({
  el: '#app',
  data: {
    message: ''
  }
})
</script>
```

In this example:

- The input field is bound to the `message` data property using `v-model`.
- When the user types into the input, the `message` property is updated.
- The paragraph displays the current value of `message`.

#### How It Works

Under the hood, `v-model` does two main things:

1. **Binds the Value**: It binds the value of the input element to a data property.
2. **Listens for Events**: It listens for input events to update the data property.

This is similar to manually writing:

```
<input :value="message" @input="message = $event.target.value">
```

#### Modifiers

Modifiers are special postfixes denoted by a dot (.) that can be appended to `v-model` directives to alter their behavior.

- **`.lazy`**: Updates the data only after the `change` event, instead of on `input`.
- `<input v-model.lazy="message">`
- **`.number`**: Automatically converts the input value to a number.
- `<input v-model.number="age">`
- **`.trim`**: Automatically trims whitespace from the input value.
- `<input v-model.trim="name">`

### Understanding Through an Example

Let's build a simple form with `v-model` that includes these features:

```
<div id="app">
  <form @submit.prevent="submitForm">
    <label for="name">Name:</label>
    <input id="name" v-model.trim="name">

    <label for="age">Age:</label>
    <input id="age" v-model.number="age">

    <label for="comments">Comments:</label>
    <textarea id="comments" v-model.lazy="comments"></textarea>

    <button type="submit">Submit</button>
  </form>

  <p>Name: {{ name }}</p>
  <p>Age: {{ age }}</p>
  <p>Comments: {{ comments }}</p>
</div>

<script>
new Vue({
  el: '#app',
  data: {
    name: '',
    age: null,
    comments: ''
  },
  methods: {
    submitForm() {
      console.log('Form Submitted', this.name, this.age, this.comments);
    }
  }
})
</script>
```

### Conclusion and Summary

`v-model` in Vue.js acts like a two-way mirror, creating a bidirectional data binding between form inputs and Vue instance data. It simplifies the process of keeping data and input elements in sync by bundling value binding and event listening. Modifiers like `.lazy`, `.number`, and `.trim` enhance its functionality by altering the behavior of this binding to suit different needs.

### Test Your Understanding

1. What is `v-model` in Vue.js?
2. How does `v-model` simplify two-way data binding?
3. What are some modifiers available with `v-model`, and what do they do?

### Reference

For more details, refer to the [official Vue.js documentation on `v-model`](https://vuejs.org/v2/guide/forms.html).
