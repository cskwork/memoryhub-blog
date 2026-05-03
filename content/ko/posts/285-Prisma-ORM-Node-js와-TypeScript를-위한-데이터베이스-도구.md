---
title: "? Prisma ORM - Node.js와 TypeScript를 위한 데이터베이스 도구"
date: 2024-06-12T13:46:27+09:00
slug: "285-Prisma-ORM-Node-js와-TypeScript를-위한-데이터베이스-도구"
original_url: "https://memoryhub.tistory.com/285"
tistory_id: 285
draft: false
categories: ["데브 옵스"]
tags: ["Node"]
---

```
  ____  ____   _   _  ____    _    
 |  _ \|  _ \ / \ | |/ ___|  / \   
 | |_) | |_) / _ \| | |  _  / _ \  
 |  __/|  __/ ___ \ | |_| |/ ___ \ 
 |_|   |_| /_/   \_\|_|\____/_/   \_\

[DB]  {TypeScript}
```

매번 새로운 프로젝트를 시작할 때마다 SQL 쿼리문과 씨름하고, 객체와 관계형 데이터베이스 사이의 불일치 때문에 골머리를 앓았던 경험, 다들 한 번쯤 있으시죠? 여기, Node.js와 TypeScript 개발자들의 데이터베이스 작업을 '재미있고 안전하게' 만들어주는 차세대 ORM, Prisma가 있습니다[6][7][10].

⚡ **TL;DR:** Prisma는 스키마 중심 접근 방식으로 타입스크립트와 완벽하게 통합되어, 개발 생산성과 데이터 안정성을 극대화합니다[1][7]. 이 글을 끝까지 읽으시면 Prisma의 핵심 컨셉을 이해하고 실제 프로젝트에 바로 적용할 수 있게 됩니다.

---

### 목차

1. 배경: 왜 Prisma인가?
2. 핵심 개념 정리
3. 실습: 5분 만에 Prisma 맛보기
4. 모범 사례 (Best Practices)
5. 마치며 & 참고자료

---

## 1. 배경: 왜 Prisma인가?

기존의 전통적인 ORM(Object-Relational Mapper)은 객체 지향 코드와 관계형 데이터베이스 사이의 패러다임 불일치 문제, 즉 '객체-관계 임피던스 불일치'를 겪는 경우가 많았습니다[8]. 이로 인해 개발자는 복잡한 매핑 로직을 작성해야 했고, 이는 생산성 저하와 잠재적인 런타임 오류로 이어지곤 했습니다.

Prisma는 이러한 문제들을 해결하기 위해 등장한 '차세대 ORM'입니다[8]. 테이블을 클래스에 매핑하는 대신, `schema.prisma`라는 단일 파일을 '진실의 원천(Single Source of Truth)'으로 삼아 데이터베이스 스키마와 애플리케이션 모델을 한 곳에서 관리합니다[5][8].

✅ **관련 용어 정리**

- **ORM (Object-Relational Mapping)**: 객체 지향 프로그래밍 언어의 객체(Object)와 관계형 데이터베이스의 데이터(Schema)를 자동으로 매핑해주는 기술입니다[2].
- **타입 안정성 (Type Safety)**: 코드를 실행하기 전인 컴파일 시점에 타입 오류를 미리 잡아내 런타임 에러 발생 가능성을 크게 줄여주는 기능입니다. Prisma는 TypeScript와 결합될 때 이 장점이 극대화됩니다[7].
- **Prisma 스키마 (Prisma Schema)**: 데이터베이스 연결 정보, 데이터 모델 정의, 클라이언트 생성기 설정을 포함하는 Prisma의 핵심 설정 파일(`schema.prisma`)입니다[5].

## 2. 핵심 개념 정리

> **Prisma는 자동 생성되는 타입 세이프 클라이언트와 직관적인 스키마, 그리고 강력한 마이그레이션 도구를 통해 데이터베이스 작업을 혁신하는 차세대 ORM입니다[5][6][8].**

Prisma는 크게 세 가지 핵심 요소로 구성됩니다[5][6][8].

- **Prisma Client**: `schema.prisma` 파일로부터 자동 생성되는 타입 세이프 쿼리 빌더입니다. Node.js와 TypeScript 환경 어디서든 사용할 수 있습니다[5].
- **Prisma Migrate**: 선언적인 데이터 모델링 및 마이그레이션 시스템입니다. 복잡한 SQL문 없이 스키마 파일 수정만으로 데이터베이스 구조를 안전하게 변경하고 관리할 수 있습니다[2][6].
- **Prisma Studio**: 데이터베이스의 데이터를 시각적으로 보고 편집할 수 있는 GUI 도구입니다. 비개발자와의 협업에도 유용합니다[2][5].

이 모든 것은 아래와 같은 `schema.prisma` 파일을 통해 정의됩니다.

```
// schema.prisma

// 1. 데이터베이스 연결 설정
datasource db {
  provider = "postgresql" // 사용할 데이터베이스 종류 (PostgreSQL, MySQL, SQLite 등[9])
  url      = env("DATABASE_URL") // 연결 정보는 .env 파일에서 관리
}

// 2. Prisma Client 생성기 설정
generator client {
  provider = "prisma-client-js"
}

// 3. 데이터 모델 정의
model User {
  id    Int     @id @default(autoincrement())
  email String  @unique
  name  String?
  posts Post[] // Post 모델과의 관계 정의
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

## 3. 실습: 5분 만에 Prisma 맛보기

백문이 불여일견! 간단한 실습을 통해 Prisma의 강력함을 직접 느껴보겠습니다.

### ① 프로젝트 설정 및 Prisma 설치

먼저, 새로운 프로젝트 폴더를 만들고 Prisma를 설치합니다. 여기서는 간단한 실습을 위해 `SQLite`를 사용하겠습니다.

```
# 프로젝트 초기화
npm init -y
# Prisma CLI 설치
npm install prisma --save-dev

# Prisma 프로젝트 초기화 (SQLite 사용)
npx prisma init --datasource-provider sqlite
```

위 명령을 실행하면 `prisma/schema.prisma` 파일과 데이터베이스 연결 정보를 담은 `.env` 파일이 생성됩니다[7].

### ② 스키마 정의 및 마이그레이션

이제 `prisma/schema.prisma` 파일을 열어 위에서 봤던 `User`와 `Post` 모델을 추가해 봅시다.

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

스키마 작성이 끝났다면, 아래 명령어로 데이터베이스에 변경사항을 적용(마이그레이션)하고 Prisma Client를 생성합니다.

```
# 스키마를 기반으로 데이터베이스 마이그레이션을 실행하고 Prisma Client를 생성
npx prisma migrate dev --name init
```

이 명령 한 줄로 `dev.db`라는 SQLite 파일이 생성되고, 스키마에 정의된 테이블이 만들어지며, 타입스크립트에서 사용할 수 있는 Prisma Client가 최신 상태로 업데이트됩니다[2][6].

### ③ Prisma Client로 데이터 다루기

이제 `script.ts` 파일을 만들어 Prisma Client를 사용해 데이터를 생성하고 조회해 보겠습니다.

```
# Prisma Client 라이브러리 설치
npm install @prisma/client

# TypeScript 관련 패키지 설치
npm install typescript ts-node @types/node --save-dev
```

```
// script.ts
import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

async function main() {
  // 새로운 User와 Post 생성
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

  // 모든 User 조회
  const allUsers = await prisma.user.findMany({
    include: { posts: true }, // 관련된 posts도 함께 조회
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

아래 명령어로 스크립트를 실행해 보세요.

```
# TypeScript 파일 실행
npx ts-node script.ts
```

### ④ Prisma Studio 실행하기

터미널에 다음 명령어를 입력하면 GUI 데이터베이스 뷰어인 Prisma Studio가 실행됩니다.

```
npx prisma studio
```

웹 브라우저에서 방금 생성한 데이터를 눈으로 직접 확인하고 편집할 수 있습니다[2][6].

## 4. 모범 사례 (Best Practices)

Prisma를 더 효과적으로 사용하기 위한 몇 가지 패턴입니다.

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **스키마 우선 개발** | 명확한 단일 진실 공급원(SSoT)을 확보하여[8], API와 DB 모델 간 일관성을 유지하고 팀 전체가 데이터 구조를 쉽게 이해할 수 있습니다. | 초기 설계의 중요성이 커지며, 대규모 스키마 변경 시 마이그레이션 계획을 신중하게 세워야 합니다. |
| **TypeScript와 함께 사용** | 자동 완성, 타입 추론, 컴파일 시점 에러 체크 등 TypeScript의 장점을 100% 활용하여 생산성과 코드 안정성을 극대화합니다[1][7]. | TypeScript에 익숙하지 않은 팀이라면 초기 학습 곡선이 존재할 수 있습니다. |
| **`Prisma Studio` 활용** | 비개발 직군(기획자, QA 등)도 데이터 상태를 쉽게 확인하고 간단한 데이터를 직접 입력할 수 있어 협업 효율이 높아집니다[2]. | 프로덕션 데이터베이스를 직접 수정하는 것은 위험하므로, 읽기 전용으로 제공하거나 권한 관리에 유의해야 합니다. |

## 5. 마치며

오늘 우리는 Prisma가 왜 차세대 ORM으로 불리는지, 그리고 어떻게 사용하는지 알아보았습니다.

- Prisma는 `schema.prisma`라는 단일 파일을 중심으로 데이터베이스 관련 작업을 극도로 단순화합니다.
- 자동 생성되는 타입 세이프 클라이언트는 개발자의 실수를 줄여주고, 자신감 있게 코드를 작성하도록 돕습니다.
- `Prisma Migrate`와 `Prisma Studio`는 복잡한 데이터베이스 관리와 팀 협업을 매우 편리하게 만듭니다.

**? 실제 프로젝트 적용 팁:** `.env` 파일을 통해 데이터베이스 연결 정보를 안전하게 관리하고[5], CI/CD 파이프라인에 `prisma generate`와 `prisma migrate deploy` 명령어를 포함시켜 배포 과정을 자동화하는 것을 강력히 추천합니다.

이 글이 Prisma를 시작하려는 분들께 좋은 가이드가 되었기를 바랍니다.

**❤️와 댓글은 더 좋은 글을 쓰는 데 큰 힘이 됩니다!**

---

### 참고자료

- **Prisma 공식 문서**: <https://www.prisma.io/docs/orm>
- **GitHub 저장소**: <https://github.com/prisma/prisma>
- **추가 읽을거리**
  - [Is Prisma an ORM? (Prisma 공식 블로그)](https://www.prisma.io/docs/orm/overview/prisma-in-your-stack/is-prisma-an-orm)
  - [Prisma in 100 Seconds (YouTube)](https://www.youtube.com/watch?v=rLRIB6AF2Dg)
  - [Node.js/TypeScript용 ORM Prisma 살펴보기 (Outsider's Dev Story)](https://blog.outsider.ne.kr/1614)

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
