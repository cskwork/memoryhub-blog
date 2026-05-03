---
title: "Vue 3 component structure - script first vs template first"
date: 2025-04-22T18:27:04+09:00
slug: "557-Vue-3-컴포넌트-구조-script-먼저-vs-template-먼저"
original_url: "https://memoryhub.tistory.com/557"
tistory_id: 557
draft: false
---

When creating components in Vue.js, you sometimes wonder about the order of `<template>`, `<script>`, and `<style>` blocks within a `.vue` file. Some people write `<template>` first, while others write `<script>` first. Does this order have any special meaning? And what order does Vue 3 recommend? Let's find out together!

## Background: Meeting past and present

In early Vue versions (Vue 2) or when primarily using the Options API, it was common to place the `<template>` block at the top. Similar to traditional HTML documents, it would show the visual structure first, followed by the script handling data, and finally the styles. 

```
<template>
  <div>{{ message }}</div>
</template>

<script>
export default {
  data() {
    return {
      message: 'Hello!'
    }
  }
}
</script>

<style scoped>
div {
  color: blue;
}
</style>
```

However, with Vue 3 came the **Composition API** and **`<script setup>`**, changing things somewhat. Using `<script setup>` allows variables and functions defined in the `<script>` block to be directly used in the `<template>`, making the `<script>` block's role much more important. Now, logic and state definitions often become the core starting point of components.

## Core principle: Does order matter?

To get straight to the point, the Vue compiler correctly interprets and builds components **regardless of** the order of `<template>`, `<script>`, and `<style>` blocks. That is, technically, no matter what order you write them in, it doesn't affect the component's functionality.

But from a **readability** and **maintainability** perspective, it's a different story. The order you follow can change how developers read and understand the code.

**1. Template-first approach (`template` > `script` > `style`)**

- **Advantages:**
  - You can understand the final HTML structure of the component first.
  - It can be more intuitive for developers accustomed to HTML-centric thinking.
- **Disadvantages:**
  - When using `<script setup>`, you need to scroll down to see the definitions of variables and functions used in the template.
  - It can be harder to understand the component's logic or state first.

```
+---------------------+
|     <template>      |  <-- Visual structure first!
+---------------------+
|      <script>       |
+---------------------+
|      <style>        |
+---------------------+
```

**2. Script-first approach (`script` > `template` > `style`)**

- **Advantages:**
  - As soon as you open the component, you immediately know what state and logic it uses and what external modules it imports.
  - When used with `<script setup>`, it's easy to follow the flow of how defined variables/functions are used in the `<template>` just below.
  - **This is the approach recommended by the official Vue 3 style guide!** (especially when using `<script setup>`)
  - Linting tools (like ESLint) often recommend or enforce this by default.
- **Disadvantages:**
  - Seeing logic before visual structure can feel a bit awkward for imagining the UI result first.

```
+---------------------+
|      <script>       |  <-- Logic/state first!
+---------------------+
|     <template>      |
+---------------------+
|      <style>        |
+---------------------+
```

**Recommended order from Vue's official style guide:**

The Vue team **strongly recommends** the following order to maintain consistency and take advantage of `<script setup>`:

1. `<script setup>` (Composition API logic)
2. `<script>` (Options API or additional configuration if needed)
3. `<template>` (template markup)
4. `<style>` (styles)

## Cautions and tips

⚠️ **Keep this in mind!**

1. **Consistency is important!**
   - Just because the order isn't technically important doesn't mean you should mix multiple styles within a project. It can confuse colleagues reading the code (or your future self!).
   - It's important to establish one convention at the team or project level and follow it consistently.

Tip

- **Use a linter!** Tools like ESLint and `eslint-plugin-vue` let you automatically check and fix code style. Setting the `vue/block-order` rule to enforce the order your team decides (preferably the official recommended order) goes a long way in maintaining consistency.

## Closing thoughts

So far, we've explored the block order within Vue 3 components. While there's no functional difference, considering the latest Vue development trends and readability, **placing the `<script>` block (especially `<script setup>`) at the top is currently the most recommended approach**. What order do you use in your projects? Share your thoughts in the comments!

## References

- Vue 3 official style guide - Component/Instance Order: <https://vuejs.org/style-guide/rules-recommended>
- Vue 3 official style guide - Element Attribute Order: <https://vuejs.org/style-guide/rules-strongly-recommended.html#element-attribute-order> (not directly related to component block order, but demonstrates the importance of consistent ordering)
- eslint-plugin-vue - `vue/block-order` rule: <https://eslint.vuejs.org/rules/block-order.html>

---

#Vue3 #Component #SFC #ScriptSetup #CodingConvention #VueStyleGuide
