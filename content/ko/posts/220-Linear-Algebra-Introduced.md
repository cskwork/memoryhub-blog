---
title: "Linear Algebra Introduced"
date: 2024-06-08T00:45:02+09:00
slug: "220-Linear-Algebra-Introduced"
original_url: "https://memoryhub.tistory.com/220"
tistory_id: 220
draft: false
categories: ["데브 컨셉"]
tags: ["Mathematics"]
cover:
  image: "/images/220-Linear-Algebra-Introduced/img.png"
  relative: false
  hidden: false
---

*Linear algebra is a branch of mathematics that deals with vectors, matrices, and systems of linear equations, enabling the understanding and manipulation of high-dimensional data.*

### The Big Picture

Imagine a large room filled with objects like chairs, tables, and boxes. Each object can be described by its position in the room using coordinates. Linear algebra helps us understand how to describe, manipulate, and transform these positions in a structured way. It's like having a toolkit that allows you to move and rotate objects, change their scale, and solve puzzles involving their arrangement.

### Core Concepts

1. **Scalars, Vectors, and Matrices**:
   - **Scalars**: Single numbers (e.g., 3, -5, 0.7).
   - **Vectors**: Ordered lists of numbers representing points or directions in space (e.g., ([2, 3]), ([-1, 4, 0])).
   - **Matrices**: Rectangular arrays of numbers used to represent linear transformations

     ![](/images/220-Linear-Algebra-Introduced/img.png)
2. **Vector Spaces and Subspaces**:
   - **Vector Space**: A collection of vectors that can be added together and multiplied by scalars while remaining within the collection.
   - **Subspace**: A subset of a vector space that is itself a vector space.
3. **Linear Transformations**:
   - Functions that map vectors to other vectors while preserving vector addition and scalar multiplication (e.g., rotating or scaling vectors).
4. **Systems of Linear Equations**:
   - Collections of equations that describe relationships between multiple variables. They can be written in matrix form and solved using various methods.

### Detailed Walkthrough

#### Scalars, Vectors, and Matrices

**Vectors**:  
Think of a vector as an arrow pointing from the origin (0,0) to a point (x,y) in 2D space, or from (0,0,0) to (x,y,z) in 3D space. For example, the vector ([3, 4]) represents a point 3 units along the x-axis and 4 units along the y-axis.

**Matrices**:  
A matrix can be seen as a table of numbers that can transform vectors. For instance, the matrix ([1, 2, 3, 4])) can be used to scale and rotate vectors in a 2D space.

**Matrix Multiplication**:  
When you multiply a matrix by a vector, you apply a linear transformation to the vector. For example:

![](/images/220-Linear-Algebra-Introduced/img_1.png)

#### Vector Spaces and Subspaces

A vector space is like a playground where vectors can freely move. Any vector in this space can be added to another vector, or scaled by a number (scalar), and it will still be in the same space.

#### Linear Transformations

A linear transformation can be visualized as a function that takes every vector in a space and maps it to another vector, possibly changing its direction and length but preserving the linear structure. Matrices represent these transformations.

For example, rotating a vector ([x, y]) by 90 degrees can be represented by the matrix:

![](/images/220-Linear-Algebra-Introduced/img_2.png)

#### Systems of Linear Equations

These are sets of equations with multiple variables that can be represented in matrix form. For example:

![](/images/220-Linear-Algebra-Introduced/img_3.png)

This system can be written as a matrix equation:

![](/images/220-Linear-Algebra-Introduced/img_4.png)

### Understanding Through an Example

Let's solve the system of linear equations mentioned above. We use matrix techniques like Gaussian elimination or matrix inversion to find the values of (x) and (y).

Using matrix inversion, we find:

![](/images/220-Linear-Algebra-Introduced/img_5.png)

### Conclusion and Summary

Linear algebra provides powerful tools for dealing with high-dimensional data, transformations, and systems of equations. By understanding vectors, matrices, and their operations, we can solve complex problems in fields like physics, engineering, and computer science.

### Test Your Understanding

1. What is a vector space, and how does it differ from a subspace?
2. How do you represent a system of linear equations using matrices?
3. Explain how matrix multiplication represents a linear transformation.

### Reference

For further learning, you can explore [Khan Academy's Linear Algebra](https://www.khanacademy.org/math/linear-algebra) course, which provides detailed explanations and exercises.
