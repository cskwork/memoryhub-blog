---
title: "How does the virtual DOM improve performance?"
date: 2024-06-12T00:38:52+09:00
slug: "279-How-does-the-virtual-DOM-improve-performance"
original_url: "https://memoryhub.tistory.com/279"
tistory_id: 279
draft: false
categories: ["Dev Library"]
tags: ["React"]
---

*The virtual DOM improves performance by minimizing direct updates to the real DOM, making updates more efficient and reducing the computational load on the browser.*

### The Big Picture

Imagine you are organizing a large stack of papers. If you had to update each piece of paper individually, it would be time-consuming and tedious. Instead, you create a checklist of changes to make and then apply all changes at once. This way, you reduce the number of interruptions and make the process much more efficient.

### Core Concepts

1. **Real DOM**: The Document Object Model represents the structure of a web page. Manipulating it directly can be slow because it requires recalculating styles, layouts, and rendering updates.
2. **Virtual DOM**: A lightweight copy of the real DOM used by React to batch and optimize updates before applying them to the real DOM.
3. **Diffing Algorithm**: A method used by React to compare the virtual DOM with the real DOM to determine the most efficient way to update the UI.

### Detailed Walkthrough

1. **Initial Rendering**: When a React application loads, the entire UI is represented as a virtual DOM tree.
2. **State Changes**: When the state of a component changes, a new virtual DOM tree is created to reflect the updated UI.
3. **Diffing**: React compares the new virtual DOM tree with the previous one to find the differences.
4. **Batch Updates**: Instead of updating the real DOM for every small change, React collects all the differences and applies them in a single batch.

### Understanding Through an Example

1. **Initial Rendering**:

   - React creates a virtual DOM tree that represents the initial state of the UI.
   - This virtual DOM tree is then used to generate the real DOM, which is rendered to the screen.
2. **State Changes**:

   - Suppose you have a component that displays a list of items. When an item is added or removed, the state of the component changes.
   - React creates a new virtual DOM tree that reflects this change.
3. **Diffing**:

   - React compares the new virtual DOM tree with the previous one. Let's say the only change is the addition of one new item to the list.
   - The diffing algorithm identifies this single change, noting that a new item has been added.
4. **Batch Updates**:

   - Instead of re-rendering the entire list, React updates only the part of the real DOM that has changed (the newly added item).
   - This minimizes the number of operations on the real DOM, making the update process faster and more efficient.

### Conclusion and Summary

The virtual DOM improves performance by:

1. **Creating a virtual representation** of the UI that is more efficient to update.
2. **Using a diffing algorithm** to identify changes between the virtual DOM and the real DOM.
3. **Batching updates** to the real DOM, reducing the number of direct manipulations.

By minimizing the number of changes to the real DOM and making updates in batches, React reduces the computational load on the browser and improves the performance of web applications.

### Test Your Understanding

1. Why is updating the real DOM directly considered slow?
2. How does the virtual DOM help in reducing the number of operations on the real DOM?
3. What is the role of the diffing algorithm in the virtual DOM?

### Reference

For further reading on the virtual DOM and how it improves performance, you can refer to the official React documentation: [React Virtual DOM](https://reactjs.org/docs/faq-internals.html#what-is-the-virtual-dom).
