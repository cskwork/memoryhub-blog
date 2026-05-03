---
title: "📦 Prisma ORM - The Database Tool for Node.js and TypeScript"
date: 2024-06-12T13:46:27+09:00
slug: "285-Prisma-ORM-Node-js와-TypeScript를-위한-데이터베이스-도구"
original_url: "https://memoryhub.tistory.com/285"
tistory_id: 285
draft: false
---

```
  ____  ____   _   _  ____    _    
 |  _ \|  _ \ / \ | |/ ___|  / \   
 | |_) | |_) / _ \| | |  _  / _ \  
 |  __/|  __/ ___ \ | |_| |/ ___ \ 
 |_|   |_| /_/   \_\|_|\____/_/   \_\

[DB]  {TypeScript}
```

Every time you start a new project, you struggle with SQL queries and the mismatch between objects and relational databases. We all know that pain, right? Here comes Prisma, a next-generation ORM that makes database work for Node.js and TypeScript developers 'fun and safe'[6][7][10].

⚡ **TL;DR:** Prisma integrates perfectly with TypeScript using a schema-centric approach, maximizing development productivity and data safety[1][7]. By the time you finish reading this article, you'll understand Prisma's core concepts and be able to apply them immediately to your projects.

---

### Table of Contents

1. Background: Why Prisma?
2. Core Concepts Overview
3. Practice: Prisma Taste Test in 5 Minutes
4. Best Practices
5. Conclusion & Resources

---

## 1. Background: Why Prisma?

Traditional ORMs (Object-Relational Mappers) often suffered from the paradigm mismatch between object-oriented code and relational databases—the 'object-relational impedance mismatch'[8]. This forced developers to write complex mapping logic, leading to reduced productivity and potential runtime errors.

Prisma emerged as a 'next-generation ORM' to solve these problems[8]. Instead of mapping tables to classes, it treats a single file called `schema.prisma` as the 'Single Source of Truth,' managing database schema and application models in one place[5][8].

✅ **Terminology**

- **ORM (Object-Relational Mapping)**: A technology that automatically maps objects in object-oriented programming languages to data (schemas) in relational databases[2].
- **Type Safety**: The ability to catch type errors at compile time before code execution, greatly reducing the likelihood of runtime errors. Prisma maximizes this advantage when combined with TypeScript[7].
- **Prisma Schema**: Prisma's core configuration file (`schema.prisma`) that contains database connection information, data model definitions, and client generator settings[5].

## 2. Core Concepts Overview

> **Prisma is a next-generation ORM that revolutionizes database work through an auto-generated type-safe client, intuitive schema, and powerful migration tools[5][6][8].**

Prisma consists of three main components[5][6][8].

- **Prisma Client**: An auto-generated type-safe query builder from the `schema.prisma` file. It can be used anywhere in Node.js and TypeScript environments[5].
- **Prisma Migrate**: A declarative data modeling and migration system. You can safely modify and manage database structure simply by editing the schema file without writing complex SQL statements[2][6].
- **Prisma Studio**: A GUI tool for visually viewing and editing database data. It's also useful for collaboration with non-developers[2][5].

All of this is defined through a `schema.prisma` file like this:

```
// schema.prisma

// 1. Database connection settings
datasource db {
  provider = "postgresql" // Database type to use (PostgreSQL, MySQL, SQLite, etc[9])
  url      = env("DATABASE_URL") // Connection info managed in .env file
}

// 2. Prisma Client generator settings
generator client {
  provider = "prisma-client-js"
}

// 3. Data model definition
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[] // Define relationship with Post model
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  published Boolean  @default(false)
  author    User?    @relation(fields: [authorId], references: [id])
  authorId  Int?
}
```

## 3. Practice: Prisma Taste Test in 5 Minutes

A picture is worth a thousand words! Let's feel Prisma's power through a simple hands-on practice.

### ① Project Setup and Prisma Installation

First, create a new project folder and install Prisma. For this simple practice, we'll use `SQLite`.

```
# Initialize project
npm init -y
# Install Prisma CLI
npm install prisma --save-dev

# Initialize Prisma project (using SQLite)
npx prisma init --datasource-provider sqlite
```

Running the above commands creates a `prisma/schema.prisma` file and a `.env` file containing database connection information[7].

### ② Schema Definition and Migration

Now open the `prisma/schema.prisma` file and add the `User` and `Post` models we saw earlier.

```
// prisma/schema.prisma

datasource db {
  provider = "sqlite"
  url      = env("DATABASE_URL")
}

generator client {
  provider = "prisma-client-js"
}

model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[]
}

model Post {
  id        Int      @id @default(autoincrement())
  title     String
  content   String?
  published Boolean  @default(false)
  author    User?    @relation(fields: [authorId], references: [id])
  authorId  Int?
}
```

Once you've written the schema, run the command below to apply changes to the database (migration) and generate the Prisma Client.

```
# Run database migration based on schema and generate Prisma Client
npx prisma migrate dev --name init
```

With this single command, an SQLite file named `dev.db` is created, tables defined in the schema are created, and a Prisma Client usable in TypeScript is updated to the latest state[2][6].

### ③ Working with Data Using Prisma Client

Now let's create a `script.ts` file and use the Prisma Client to create and fetch data.

```
# Install Prisma Client library
npm install @prisma/client

# Install TypeScript-related packages
npm install typescript ts-node @types/node --save-dev
```

```
// script.ts
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  // Create a new User and Post
  const newUser = await prisma.user.create({
    data: {
      name: 'Alice',
      email: 'alice@prisma.io',
      posts: {
        create: {
          title: 'Hello World',
          content: 'This is my first post!',
        },
      },
    },
  })
  console.log('Created new user: ', newUser)

  // Fetch all Users
  const allUsers = await prisma.user.findMany({
    include: { posts: true }, // Also fetch related posts
  })
  console.log('All users: ')
  console.dir(allUsers, { depth: null })
}

main()
  .catch((e) => {
    throw e
  })
  .finally(async () => {
    await prisma.$disconnect()
  })
```

Try running the script with the command below.

```
# Run TypeScript file
npx ts-node script.ts
```

### ④ Running Prisma Studio

Enter the following command in the terminal to run Prisma Studio, the GUI database viewer.

```
npx prisma studio
```

You can directly view and edit the data you just created in the web browser[2][6].

## 4. Best Practices

Here are some patterns for using Prisma more effectively.

| Pattern | Advantage | Caution |
| --- | --- | --- |
| **Schema-First Development** | By establishing a clear single source of truth (SSoT)[8], you maintain consistency between API and DB models, and the entire team can easily understand the data structure. | The importance of initial design increases, and for large schema changes, migration plans must be carefully considered. |
| **Use with TypeScript** | Maximize TypeScript's advantages—auto-completion, type inference, compile-time error checking—to maximize productivity and code stability[1][7]. | Teams unfamiliar with TypeScript may face an initial learning curve. |
| **Leverage `Prisma Studio`** | Non-developers (planners, QA, etc.) can easily check data status and directly input simple data, improving collaboration efficiency[2]. | Directly modifying production databases is risky, so provide read-only access or be mindful of permission management. |

## 5. Conclusion

Today we explored why Prisma is called a next-generation ORM and how to use it.

- Prisma dramatically simplifies database-related tasks centered around a single `schema.prisma` file.
- The auto-generated type-safe client reduces developer mistakes and helps write code with confidence.
- `Prisma Migrate` and `Prisma Studio` make complex database management and team collaboration very convenient.

**📦 Real Project Implementation Tips:** Safely manage database connection information through `.env` files[5], and strongly recommend including `prisma generate` and `prisma migrate deploy` commands in your CI/CD pipeline to automate the deployment process.

I hope this article has been a good guide for those starting with Prisma.

**❤️ and comments are great motivation for writing better articles!**

---

### References

- **Prisma Official Documentation**: <https://www.prisma.io/docs/orm>
- **GitHub Repository**: <https://github.com/prisma/prisma>
- **Further Reading**
  - [Is Prisma an ORM? (Prisma Official Blog)](https://www.prisma.io/docs/orm/overview/prisma-in-your-stack/is-prisma-an-orm)
  - [Prisma in 100 Seconds (YouTube)](https://www.youtube.com/watch?v=rLRIB6AF2Dg)
  - [Exploring Prisma ORM for Node.js/TypeScript (Outsider's Dev Story)](https://blog.outsider.ne.kr/1614)

[1] <https://www.prisma.io>  
[2] <https://velog.io/@ltnscp9028/Prisma-%EB%84%8C-%EB%88%84%EA%B5%AC%EB%8B%88-gr0ecme3>  
[3] <https://blog.codefactory.ai/prisma/deploy-prisma-in-five-minutes/>  
[4] <https://github.com/prisma/prisma>  
[5] <https://www.prisma.io/docs/orm/overview/introduction/what-is-prisma>  
[6] <https://www.pingcap.com/article/understanding-prisma-orm/>  
[7] <https://blockchain.oodles.io/dev-blog/prisma-orm/>  
[8] <https://www.prisma.io/docs/orm/overview/prisma-in-your-stack/is-prisma-an-orm>  
[9] <https://blog.outsider.ne.kr/1614>  
[10] <https://www.youtube.com/watch?v=rLRIB6AF2Dg>  
[11] <https://github.com/prisma>  
[12] <https://www.prisma.io/orm>  
[13] <https://www.prisma.io/docs/orm/overview/introduction>  
[14] <https://console.prisma.io/sign-up>  
[15] <https://app.prisma.io>
