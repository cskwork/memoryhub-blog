---
title: "NestJS Introduced"
date: 2024-06-12T13:54:06+09:00
slug: "286-NestJS-Introduced"
original_url: "https://memoryhub.tistory.com/286"
tistory_id: 286
draft: false
categories: ["데브 프레임워크"]
tags: ["NestJS"]
---

*NestJS is a progressive Node.js framework for building efficient, reliable, and scalable server-side applications.*

### The Big Picture

Think of NestJS as a well-organized toolkit for building the backend of web applications. It's like having a well-structured blueprint for constructing a house, where every part has a specific place and function, ensuring everything fits together seamlessly.

### Core Concepts

1. **Modules**: These are like the rooms in your house. Each room has a specific purpose (kitchen, bedroom, bathroom), and together they make the house functional.
2. **Controllers**: These are the doors to your rooms. They allow you to interact with the different parts of your house.
3. **Providers**: Think of these as the utilities (water, electricity) that your rooms need to function. They provide the necessary services.
4. **Decorators**: These are like the labels on your house's blueprint, marking what each part does and how it should behave.

### Detailed Walkthrough

#### Modules

A module in NestJS groups related components together, similar to how a kitchen module might include a fridge, stove, and sink.

```
import { Module } from '@nestjs/common';
import { CatsController } from './cats.controller';
import { CatsService } from './cats.service';

@Module({
  controllers: [CatsController],
  providers: [CatsService],
})
export class CatsModule {}
```

#### Controllers

Controllers handle incoming requests and return responses to the client. They are like the doors that give access to different rooms (functionalities) of your house.

```
import { Controller, Get } from '@nestjs/common';
import { CatsService } from './cats.service';

@Controller('cats')
export class CatsController {
  constructor(private readonly catsService: CatsService) {}

  @Get()
  findAll(): string {
    return this.catsService.findAll();
  }
}
```

#### Providers

Providers are the core of your business logic and can be injected into controllers. They are like the plumbing and wiring that keep everything running smoothly.

```
import { Injectable } from '@nestjs/common';

@Injectable()
export class CatsService {
  findAll(): string {
    return 'This action returns all cats';
  }
}
```

#### Decorators

Decorators are special kinds of declarations that can be attached to classes, methods, and properties to modify their behavior. They are like the tags on a blueprint that explain what each part of the design does.

```
import { Injectable, Controller, Get } from '@nestjs/common';

// @Injectable() decorator marks CatsService as a provider.
@Injectable()
export class CatsService {
  findAll(): string {
    return 'This action returns all cats';
  }
}

// @Controller() decorator marks CatsController as a controller.
@Controller('cats')
export class CatsController {
  constructor(private readonly catsService: CatsService) {}

  // @Get() decorator marks the findAll() method as a handler for GET requests.
  @Get()
  findAll(): string {
    return this.catsService.findAll();
  }
}
```

### Understanding Through an Example

Let's say you want to create a NestJS application to manage a library. You would have:

- **Module**: LibraryModule
- **Controller**: BooksController (to handle book-related requests)
- **Provider**: BooksService (to handle the logic for managing books)

```
// books.module.ts
import { Module } from '@nestjs/common';
import { BooksController } from './books.controller';
import { BooksService } from './books.service';

@Module({
  controllers: [BooksController],
  providers: [BooksService],
})
export class BooksModule {}

// books.controller.ts
import { Controller, Get } from '@nestjs/common';
import { BooksService } from './books.service';

@Controller('books')
export class BooksController {
  constructor(private readonly booksService: BooksService) {}

  @Get()
  findAll(): string {
    return this.booksService.findAll();
  }
}

// books.service.ts
import { Injectable } from '@nestjs/common';

@Injectable()
export class BooksService {
  findAll(): string {
    return 'This action returns all books';
  }
}
```

### Conclusion and Summary

NestJS organizes your server-side application into cohesive modules, each containing controllers, providers, and decorators to manage functionality efficiently. Think of it as building a house with well-defined rooms, doors, and utilities.

### Test Your Understanding

1. **What is the purpose of a module in NestJS?**
2. **How does a controller in NestJS relate to HTTP requests?**
3. **What role do providers play in a NestJS application?**
4. **How do decorators enhance the functionality of classes and methods in NestJS?**

### Reference

For further reading and a deeper dive into NestJS, visit the [official NestJS documentation](https://docs.nestjs.com/).
