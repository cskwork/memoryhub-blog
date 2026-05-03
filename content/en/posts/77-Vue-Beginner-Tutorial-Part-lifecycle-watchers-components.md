---
title: "Vue Beginner Tutorial Part (lifecycle, watchers, components)"
date: 2024-05-25T17:51:10+09:00
slug: "77-Vue-Beginner-Tutorial-Part-lifecycle-watchers-components"
original_url: "https://memoryhub.tistory.com/77"
tistory_id: 77
draft: false
categories: ["Dev Framework"]
tags: ["VueJS"]
cover:
  image: "images/77-Vue-Beginner-Tutorial-Part-lifecycle-watchers-components/img.png"
  relative: false
  hidden: false
---

## Lifecycle Hooks and Template Refs

> Lifecycle Hooks are used to manually and timely manipulate the DOM.

Vue has been handling all the DOM updates for us, due to reactivity and declarative rendering.

However, inevitably there will be cases where we need to **manually work with the DOM.**

We can request a template ref - i.e. a reference to an element in the template - using the special ref attribute:

A lifecycle hook it allows us to register a callback to be **called at certain times**of the component's lifecycle.

There are other hooks such as created and updated.

The mounted hook can be used to run code **after the component has finished the initial rendering and created the DOM nodes**.

All lifecycle hooks are called with their this context pointing to the current active instance invoking it.

```
<script>
export default {
  mounted() {
    this.$refs.p.textContent = 'CHANGED'
  }
}
</script>

<template>
  <p ref="p">hello</p>
</template>
```

![](/images/77-Vue-Beginner-Tutorial-Part-lifecycle-watchers-components/img.png)

## Watchers

> Functions that react to changes in data properties

Used to perform side effects reactively such as logging a number to the console when it changes.

Watchers are declared in the component using the watch option and take the new and old values of the watched property as arguments.

#### Side effects

1 DOM Mutation - Manual application state change due to some event or action  
EX) Change state based on result of async operation.

Fetch new data when ID Changes.

```
<script>
export default {
  data() {
    return {
      todoId: 1,
      todoData: null
    }
  },
  methods: {
    async fetchData() {
      this.todoData = null
      const res = await fetch(
        `https://jsonplaceholder.typicode.com/todos/${this.todoId}`
      )
      this.todoData = await res.json()
    }
  },
  mounted() {
    this.fetchData()
  },
  watch: {
    todoId() {
      this.fetchData()
    }
  }
}
</script>

<template>
  <p>Todo id: {{ todoId }}</p>
  <button @click="todoId++">Fetch next todo</button>
  <p v-if="!todoData">Loading...</p>
  <pre v-else>{{ todoData }}</pre>
</template>
```

![](/images/77-Vue-Beginner-Tutorial-Part-lifecycle-watchers-components/img_1.png)

## Components

> Components are reusable pieces of UI that can contain data, methods, and template.

Components are defined using the <script> and <template> tags and imported into other components using the import statement. Components are registered using the components option and rendered using their tag name.

In the web page context, the ChildComp component is defined in a separate file and imported into the parent component. The parent component registers the ChildComp component and renders it in its template:

```
<script>
import ChildComp from './ChildComp.vue'
export default {
  // register child component
  components: {
    ChildComp
  }
}
</script>

<template>
  <!-- render child component -->
  <ChildComp />
</template>
```

![](/images/77-Vue-Beginner-Tutorial-Part-lifecycle-watchers-components/img_2.png)

## Props

> Input data that a child component can receive from its parent component.

#### Method

Props are declared in the child component using the props option and passed from the parent component using attributes or v-bind syntax.

```
<script>
import ChildComp from './ChildComp.vue'

export default {
  components: {
    ChildComp
  },
  data() {
    return {
      greeting: 'Hello from parent'
    }
  }
}
</script>

<template>
  <ChildComp :msg="greeting" />
</template>
```

![](/images/77-Vue-Beginner-Tutorial-Part-lifecycle-watchers-components/img_3.png)

## Emits

> Events that a child component can send to its parent component.

Emits are triggered in the child component using the this.$emit method and received by the parent component using v-on or @ syntax.

In the web page context, the ChildComp component emits an event named response with a message as an argument and the parent component listens to it using @response and assigns the message to its local state:

```
<script>
import ChildComp from './ChildComp.vue'

export default {
  components: {
    ChildComp
  },
  data() {
    return {
      childMsg: 'No child msg yet'
    }
  }
}
</script>

<template>
  <ChildComp @response="(msg) => childMsg = msg" />
  <p>{{ childMsg }}</p>
</template>
```

![](/images/77-Vue-Beginner-Tutorial-Part-lifecycle-watchers-components/img_4.png)

## Slots

> Template fragments that a parent component can pass down to its child component.

Slots are defined in the child component using the <slot> element and filled by the parent component using any content inside the child component tag.

For example, in the web page context, the ChildComp component defines a slot and the parent component passes down a message as slot content

```
<script>
import ChildComp from './ChildComp.vue'

export default {
  components: {
    ChildComp
  },
  data() {
    return {
      msg: 'from parent'
    }
  }
}
</script>

<template>
  <ChildComp>Message: {{ msg }}</ChildComp>
</template>
```

![](/images/77-Vue-Beginner-Tutorial-Part-lifecycle-watchers-components/img_5.png)

## Reference

<https://vuejs.org/tutorial>

<https://vuejs.org/guide/essentials/lifecycle.html#lifecycle-diagram>

<https://vuejs.org/guide/essentials/watchers.html>
