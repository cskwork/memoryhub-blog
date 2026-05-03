---
title: "Bootstrap Introduced"
date: 2024-05-26T10:45:38+09:00
slug: "90-Bootstrap-Introduced"
original_url: "https://memoryhub.tistory.com/90"
tistory_id: 90
draft: false
categories: ["Dev Framework"]
tags: ["Bootstrap"]
---

*Bootstrap is a powerful front-end framework used for developing responsive and mobile-first websites with ease, akin to a toolkit that helps build a house with pre-designed and customizable tools.*

### The Big Picture

Imagine you are building a house. Without proper tools, it would be a laborious task requiring you to create every single tool and component from scratch. Bootstrap is like a well-stocked toolkit that provides you with pre-designed and customizable tools, making the process of building a website much simpler and faster. It's a popular front-end framework that includes HTML, CSS, and JavaScript components.

### Core Concepts

1. **Responsive Design**: Ensures that your website looks good on all devices (desktops, tablets, and phones).
2. **Grid System**: A flexible grid layout system that helps in creating layouts for various screen sizes.
3. **Components**: Pre-styled elements like buttons, forms, navigation bars, and modals that you can easily integrate into your site.
4. **Utilities**: Classes that you can use to control spacing, alignment, visibility, and more.

### Detailed Walkthrough

1. **Responsive Design**:

   - Bootstrap uses a mobile-first approach, meaning it designs for mobile devices first and then scales up to larger screens.
   - Media queries in CSS are employed to adjust the layout based on the screen size.
2. **Grid System**:

   - The grid system is based on a 12-column layout, allowing for complex layouts to be created with ease.
   - You can divide your page into rows and columns using classes like `.row`, `.col-sm-4`, `.col-md-6`, etc.
   - Example:

     ```
     <div class="container">
       <div class="row">
         <div class="col-sm-4">Column 1</div>
         <div class="col-sm-4">Column 2</div>
         <div class="col-sm-4">Column 3</div>
       </div>
     </div>
     ```
3. **Components**:

   - Bootstrap provides a variety of components such as buttons, cards, modals, navbars, and more.
   - These components come with default styles that can be customized.
   - Example:

     ```
     <button type="button" class="btn btn-primary">Primary Button</button>
     ```
4. **Utilities**:

   - Utility classes help in quick styling for margin, padding, color, alignment, and more.
   - Example:

     ```
     <div class="text-center">Centered Text</div>
     <div class="mt-3">Margin Top 3</div>
     ```

### Understanding Through an Example

Let's build a simple responsive webpage with Bootstrap.

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
  <title>Bootstrap Example</title>
</head>
<body>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="row mt-4">
      <div class="col-md-8">
        <h1>Welcome to Bootstrap</h1>
        <p>This is a simple example to demonstrate Bootstrap's capabilities.</p>
      </div>
      <div class="col-md-4">
        <button type="button" class="btn btn-success">Click Me</button>
      </div>
    </div>
  </div>
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

### Conclusion and Summary

Bootstrap is like a comprehensive toolkit for web development, providing you with everything you need to create responsive, mobile-first websites. It includes a grid system for layout, pre-styled components for common UI elements, and utility classes for quick styling. By leveraging these tools, you can significantly streamline your web development process.

### Test Your Understanding

1. What is the purpose of Bootstrap's grid system?
2. How would you create a responsive navbar using Bootstrap?
3. Explain how utility classes in Bootstrap can be used to manage spacing.

### Reference

For further learning, you can refer to the official [Bootstrap Documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/).
