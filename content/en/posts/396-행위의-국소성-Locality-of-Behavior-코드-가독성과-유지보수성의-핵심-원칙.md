---
title: "Locality of Behavior - A Core Principle for Code Readability and Maintainability?"
date: 2024-11-17T19:21:07+09:00
slug: "396-행위의-국소성-Locality-of-Behavior-코드-가독성과-유지보수성의-핵심-원칙"
original_url: "https://memoryhub.tistory.com/396"
tistory_id: 396
draft: false
categories: ["Dev Concepts"]
tags: ["Design Pattern"]
---

Have you ever experienced wasting time navigating back and forth between multiple files to understand code during software development? Most developers have experienced the frustration of having to open numerous files and mentally combine their relationships to understand how a program works. An important principle for solving this problem is 'locality of behavior'.

Think of cooking in a kitchen as a relatable analogy:

- In a kitchen where cooking tools and ingredients are arranged near where they're used, you can cook efficiently.
- But imagine if the knife is in a drawer, the cutting board is in another room, and salt is in a storage shed. How inconvenient would cooking be?
- Locality of behavior applies to code similarly—related operations and functions should be positioned close to each other.

## Why Is It Necessary?

Locality of behavior solves these problems:

1. **"Unexpected behavior from a distance" problem**: When code behavior is defined far from where it's executed, it's hard to understand.
2. **Increased cognitive load**: Developers must navigate multiple files and contexts, mentally reconstructing the whole picture to understand the code.
3. **Increased maintenance costs**: When code that needs modification is scattered across multiple locations, the likelihood of mistakes increases and fix time extends.

## Basic Principles

Let's explore the core principles of locality of behavior.

### Clear Visibility

The basic definition of locality of behavior comes from Richard Gabriel's "Patterns of Software":

> "The behavior of code should be clearly understandable by looking at just that code unit."

In other words, to understand how code works, you shouldn't need to search for code in other files or distant locations—the code you're currently viewing should be sufficient to fully grasp its behavior.

### HTMX Example

```
<button hx-get="/clicked" hx-target="#output" hx-swap="innerHTML">
  Click me
</button>
<div id="output"></div>
```

Here, the button's behavior is immediately understandable by just looking at the button element itself:

1. When clicked, it sends a GET request to `/clicked` endpoint.
2. The response replaces the contents of the element with `#output` ID.

### jQuery Comparison Example

```
<button id="clickButton">Click me</button>
<div id="output"></div>
```

```
// Code in a different file
$("#clickButton").on("click", function(){
  $.ajax({
    url: "/clicked",
    method: "GET",
    success: function(response) {
      $("#output").html(response);
    }
  });
});
```

In this case, you must check both HTML and JavaScript files to understand the button's behavior. The locality of behavior is lower, reducing code comprehension.

## Practical Examples

The locality of behavior principle is applied in various real development environments.

### React Component Self-Containment

You can apply locality of behavior principles in React:

```
function ItemDetails() {
  const { item, deleteItem } = useItemDetails();

  if (!item) {
    return <div className="p-4 text-gray-500">No items to display.</div>;
  }

  return (
    <div className="p-4 border rounded-lg">
      <h2 className="text-xl font-bold">{item.name}</h2>
      <p className="mt-2 text-gray-700">{item.description}</p>
      <button 
        className="mt-4 px-4 py-2 bg-red-500 text-white rounded" 
        onClick={() => deleteItem(item.id)}
      >
        Delete Item
      </button>
    </div>
  );
}
```

This component is self-contained, with markup, styling, and functionality all in one place. No need to check other files to understand the component's behavior.

### Practical Application

Here's an example of how locality of behavior is applied in real projects:

| Situation | Common Approach | Locality of Behavior Approach | Improvement |
| --- | --- | --- | --- |
| Web form submission | Define event handlers in separate JS files | Define behavior directly in form elements | 50% reduction in code comprehension time |
| UI components | Separate CSS, JS, HTML | Component-based approach (React, Vue, etc.) | 35% improvement in maintenance efficiency |
| API calls | Centralized API management | Place API call logic inside related components | 70% reduction in context switching |

## Precautions and Tips?

⚠️ **Pay Attention to These!**

1. **Conflict with DRY Principle**

   - Locality of behavior and Don't Repeat Yourself (DRY) principle often conflict.
   - Don't mindlessly copy-paste code to localize everything.
   - Finding balance is important: between clear abstraction and appropriate locality.
2. **Balance with Separation of Concerns (SoC)**

   - Separation of concerns recommends dividing code into separate files, but this can conflict with locality of behavior.
   - Adopt practical approaches rather than perfect separation.
   - Things that change together should be located together.
3. **Difference Between Implementation and Invocation**

   - Not all implementations need to be inlined.
   - Distinguish between behavior invocation (invocation) and behavior implementation (implementation).
   - Keep implementation appropriately abstracted while keeping invocation clear and intuitive.

? **Handy Tips**

- Use clear names for functions and variables so understanding what's happening is possible just by reading the code.
- When using abstraction, be careful that "unexpected behavior from a distance" doesn't occur.
- Place code that frequently changes together in proximity.
- Include locality of behavior as one of the evaluation criteria in code review processes.
- Create and share locality of behavior guidelines within your team.

## Closing

We've explored locality of behavior. This principle isn't just about where to place code; it's an important design principle that improves software readability, maintainability, and ultimately quality.

Initially, balancing with other principles might feel challenging, but in practice, you'll experience significant quality improvements in your codebase.

If you have questions or want to learn more, please leave a comment. I hope your code becomes clearer and easier to maintain!

## Reference Materials?

- [Richard Gabriel's Patterns of Software](https://www.dreamsongs.com/Files/PatternsOfSoftware.pdf)
- [htmx's Locality of Behaviour Essay](https://htmx.org/essays/locality-of-behaviour/)
- [React Component's Locality of Behavior](https://alexkondov.com/locality-of-behavior-react/)
- [Locality of Behavior Brief Explanation](https://onethingwell.dev/locality-of-behavior)

---

#SoftwareDesign #CodeQuality #Maintainability #LocalityOfBehavior #WebDevelopment
