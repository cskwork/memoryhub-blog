---
title: "NestJS VS ExpressJS"
date: 2024-06-12T13:58:25+09:00
slug: "287-NestJS-VS-ExpressJS"
original_url: "https://memoryhub.tistory.com/287"
tistory_id: 287
draft: false
categories: ["Dev Framework"]
tags: ["NestJS"]
---

*In this response, we'll compare NestJS and ExpressJS, two popular Node.js frameworks, focusing on their architectures, features, and use cases to help you understand which one might be better suited for your projects.*

### The Big Picture

Imagine you need to build a house. ExpressJS is like having a set of basic tools: a hammer, nails, and wood. You can build a house, but you have to design and construct everything from scratch. NestJS, on the other hand, is like having a pre-fabricated house kit with all the materials and instructions included. It's more structured and gives you a solid starting point, but it might take longer to learn how to use the kit effectively.

### Core Concepts

1. **ExpressJS**:

   - **Minimalistic and Unopinionated**: ExpressJS provides a thin layer of fundamental web application features, without dictating how to organize your application.
   - **Flexibility**: You have complete control over how you build your application, but with great power comes great responsibility. You need to make all architectural decisions.
   - **Middleware**: Central to ExpressJS is the middleware concept, where functions handle requests and responses.
2. **NestJS**:

   - **Modular and Opinionated**: NestJS enforces a specific way of organizing your code into modules, controllers, and services, which promotes good design patterns.
   - **Built-in Features**: It includes a lot of features out of the box, like dependency injection, a powerful CLI, and integration with TypeScript.
   - **Extensible**: While it enforces structure, it's built on top of Express (or optionally Fastify), meaning you can still use Express middleware and packages.

### Detailed Walkthrough

#### Architecture

- **ExpressJS**:

  - It's a thin layer on top of Node.js, providing a simple API to create web servers and handle routing.
  - Example setup:

    ```
    const express = require('express');
    const app = express();

    app.get('/', (req, res) => res.send('Hello World!'));

    app.listen(3000, () => console.log('Server running on port 3000'));
    ```
- **NestJS**:

  - It follows a modular architecture inspired by Angular. Applications are divided into modules, each encapsulating related components (controllers, services, etc.).
  - Example setup:

    ```
    import { Module } from '@nestjs/common';
    import { AppController } from './app.controller';
    import { AppService } from './app.service';

    @Module({
      imports: [],
      controllers: [AppController],
      providers: [AppService],
    })
    export class AppModule {}

    import { NestFactory } from '@nestjs/core';
    import { AppModule } from './app.module';

    async function bootstrap() {
      const app = await NestFactory.create(AppModule);
      await app.listen(3000);
    }
    bootstrap();
    ```

#### Dependency Injection

- **ExpressJS**:

  - No built-in dependency injection system. You have to manage dependencies manually.
- **NestJS**:

  - Built-in dependency injection container. This makes it easier to manage and inject dependencies, promoting loose coupling and easier testing.

#### TypeScript Support

- **ExpressJS**:

  - TypeScript support is available but requires additional setup and configuration.
- **NestJS**:

  - Designed with TypeScript in mind, providing excellent support and integration out of the box.

### Understanding Through an Example

Consider building a RESTful API for managing a library of books.

- **ExpressJS**:

  - You manually define routes and handlers.

    ```
    const express = require('express');
    const app = express();
    app.use(express.json());
    ```

  let books = [{ id: 1, title: '1984', author: 'George Orwell' }];

  app.get('/books', (req, res) => res.json(books));  
  app.post('/books', (req, res) => {  
   const book = { id: books.length + 1, ...req.body };  
   books.push(book);  
   res.status(201).json(book);  
  });

  app.listen(3000, () => console.log('Server running on port 3000'));
- **NestJS**:

  - You define modules, controllers, and services.

    ```
    import { Controller, Get, Post, Body } from '@nestjs/common';
    ```

  @Controller('books')  
  export class BooksController {  
   private books = [{ id: 1, title: '1984', author: 'George Orwell' }];

  @Get()  
   getBooks() {

  ```
  return this.books;
  ```

  }

  @Post()  
   addBook(@Body() book) {

  ```
  const newBook = { id: this.books.length + 1, ...book };
  this.books.push(newBook);
  return newBook;
  ```

  }  
  }

  import { Module } from '@nestjs/common';  
  import { BooksController } from './books.controller';

  @Module({  
   controllers: [BooksController],  
  })  
  export class BooksModule {}

### Conclusion and Summary

- **ExpressJS**: Best for simple, lightweight applications where you need full control and flexibility.
- **NestJS**: Ideal for larger applications where maintainability, scalability, and built-in features like dependency injection and TypeScript support are beneficial.

**Test Your Understanding**

1. Can you explain the main differences between ExpressJS and NestJS in terms of their architectural design?
2. How does dependency injection work in NestJS, and why is it beneficial?
3. Create a simple NestJS module with a controller that handles GET and POST requests for a new resource.

### Reference

- [NestJS Official Documentation](https://docs.nestjs.com/)
- [ExpressJS Official Documentation](https://expressjs.com/)
