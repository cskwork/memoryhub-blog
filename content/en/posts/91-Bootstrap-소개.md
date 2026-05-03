---
title: "Bootstrap Introduction"
date: 2024-05-26T10:47:18+09:00
slug: "91-Bootstrap-소개"
original_url: "https://memoryhub.tistory.com/91"
tistory_id: 91
draft: false
---

*Bootstrap is a powerful frontend framework that makes it easy to develop responsive and mobile-first websites, much like building a house with pre-designed tools and customizable components.*

### The Big Picture

Imagine building a house. Without proper tools, you'd have to make every tool and component from scratch, which would be extremely difficult. Bootstrap is like a well-equipped toolbox that provides pre-designed and customizable tools, making the process of creating a website much easier and faster. It's a popular frontend framework that includes HTML, CSS, and JavaScript components.

### Core Concepts

1. **Responsive Design**: Ensures your website looks good on all devices (desktop, tablet, mobile).
2. **Grid System**: A flexible grid layout system that helps create layouts that adapt to different screen sizes.
3. **Components**: Pre-styled elements that are easy to integrate, such as buttons, forms, navigation bars, and modals.
4. **Utilities**: Classes that let you control spacing, alignment, visibility, and more.

### Detailed Explanation

1. **Responsive Design**:

   - Bootstrap uses a mobile-first approach, designing for mobile devices first and then expanding to larger screens.
   - Uses CSS media queries to adjust the layout based on screen size.

2. **Grid System**:

   - The grid system is based on a 12-column layout, making it easy to create even complex layouts.
   - You can divide a page into rows and columns using classes like `.row`, `.col-sm-4`, `.col-md-6`, and more.
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

   - Bootstrap provides a variety of components including buttons, cards, modals, and navigation bars.
   - These components have default styling, which can be customized.
   - Example:

     ```
     <button type="button" class="btn btn-primary">Primary Button</button>
     ```

4. **Utilities**:

   - Utility classes help quickly style spacing, padding, color, alignment, and more.
   - Example:

     ```
     <div class="text-center">Center-aligned text</div>
     <div class="mt-3">Top margin 3</div>
     ```

### Understanding Through Examples

Let's create a simple responsive webpage using Bootstrap.

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
      <a class="navbar-brand" href="#">Navigation Bar</a>
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
        <p>A simple example demonstrating Bootstrap's capabilities.</p>
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

Bootstrap is like a comprehensive toolbox for web development, providing everything you need to build responsive, mobile-first websites. With a grid system for layout, pre-styled components for common UI elements, and utility classes for quick styling, Bootstrap significantly simplifies the web development process.

### Understanding Assessment

1. What is the purpose of Bootstrap's grid system?
2. How can you create a responsive navigation bar using Bootstrap?
3. Explain how to manage spacing using Bootstrap's utility classes.

### Reference Materials

For further learning, refer to the official [Bootstrap documentation](https://getbootstrap.com/docs/4.5/getting-started/introduction/).
