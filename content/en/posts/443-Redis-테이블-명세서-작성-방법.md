---
title: "Redis Table Specification Writing Method"
date: 2025-02-09T01:42:45+09:00
slug: "443-Redis-테이블-명세서-작성-방법"
original_url: "https://memoryhub.tistory.com/443"
tistory_id: 443
draft: false
---

Today, let's explore **Redis table (or schema) specification writing methods** and several **examples**. Unlike typical relational databases (RDBMS), Redis doesn't have clear "table" or "schema" concepts. However, to **design Redis data structures systematically** and make them easy to understand and maintain, it's important to establish **guidelines similar to table specifications**.

---

## 1. What is a Redis Table (Schema) Specification?

Just as we define table structure and columns in relational databases through `CREATE TABLE`, `ALTER TABLE`, etc., **in Redis, we can also systematically document keys (Key), data structures (data types), and values (Value) like a "table"**.

However, since **Redis doesn't have an explicit column concept**, people often create a "table specification" by defining the following elements:

- **Key Prefix** or **Key Pattern**: e.g., `user:{userId}`, `product:{productId}`, `session:{sessionId}`
- **Data structure type to store**: String, Hash, List, Set, Sorted Set, etc.
- **Value structure**: Hash case with fields/values, JSON format, etc.
- **Whether to set expiration time (TTL)**
- **Use of index keys (Secondary Key)**: e.g., Set or Sorted Set for searching or filtering

### Simple Example

- **Key**: `user:1001`
- **Type**: Hash
- **Fields**: `name`, `age`, `email`, …
- **TTL**: None
- **Description**: User information management

With these rules documented, any team member can easily understand **what data goes into Redis, in what structure**, and maintenance becomes easier.

---

## 2. How to Write a Table Specification (Schema)

### 1) Basic Concept

When structuring a Redis table specification, consider and document these elements:

1. **Key Naming Convention**

   - Redis is fundamentally a Key-Value structure, so **the Key is the core of data distinction**.
   - Generally use prefixes and curly braces like `app_name:domain_name:{id}` or `domain_name:{id}`.
   - Examples: `myApp:user:{userId}`, `myApp:order:{orderId}`
2. **Data Structure Selection**

   - Redis offers various data structures: String, Hash, List, Set, Sorted Set, etc.
   - Which structure to use depends on data's **access patterns (retrieval, insertion, modification, deletion, sorting, etc.)**.
3. **Define Key-Value (or Hash) Structure**

   - For Hash type, **clearly specify what fields to store**.
   - Also need information about each field's value type (number, string, JSON, etc.).
4. **TTL (Expiration Time) Setting**

   - For caching purposes, setting expiration time is standard.
   - Example: `EXPIRE 3600` (1 hour)
5. **Index Key (Secondary Key) Design**

   - For frequent searching, sorting, filtering, separate Set or Sorted Set can be operated as **'index'**.
6. **Exception Cases and Precautions**

   - Points with data loss concerns (e.g., data persistence issues on server restart)
   - Large-scale data insertion causing memory shortage, etc.

### 2) Actual Table (Schema) Specification Document Example

Let's write a Redis table specification for the **User domain** as an example:

| Item | Content |
| --- | --- |
| **Key Prefix** | `user:{userId}` |
| **Data Structure** | Hash |
| **Fields** | - **name** (String)   - **age** (Integer)   - **email** (String)   - **joined_at** (Timestamp) |
| **TTL** | None (no expiration needed) |
| **Index Key** | `user:all` (Set) – stores all userIds (for search/list retrieval) |
| **Description** | Hash schema for Redis user information storage |
| **Example Command** | `HSET user:1001 name "Alice" age 30 email "alice@example.com" joined_at 1672531200` |
| **Precautions** | - age field value recommends integer type   - email value needs uniqueness guarantee; consider separate index if needed |

---

## 3. How Does This Schema Work?

### 1) Basic Example

```
# Create user information
HSET user:1001 name "Alice" age 30 email "alice@example.com" joined_at 1672531200

# Add index key for managing entire user list
SADD user:all 1001

# Retrieve user information
HGETALL user:1001
# Example output:
# 1) "name"
# 2) "Alice"
# 3) "age"
# 4) "30"
# 5) "email"
# 6) "alice@example.com"
# 7) "joined_at"
# 8) "1672531200"
```

### 2) Operation Principle

1. **Set Key**

   - Use key format like `user:1001` to store information for user with userId (1001) as a hash.
2. **Field-by-field data management**

   - Store fields like `name`, `age`, `email` as hash format, allowing retrieval of specific fields only or partial updates.
3. **Manage all users through index key**

   - Commands like `SADD user:all 1001` store new user ID in the `user:all` Set.
   - Later, to retrieve all users, get the ID list with `SMEMBERS user:all`, then query each user key individually.

---

## 4. Key Advantages

1. **Simplified data structure**

   - Since Redis schema is flexible, you can quickly add/delete only needed fields.
   - Unlike relational DBs, no need to modify (DDL) tables, enabling agile response.
2. **High performance**

   - In-memory based, so retrieval speed is very fast, making it great for caching layers or session storage.
3. **Various data structures available**

   - Hash, List, Set, Sorted Set, etc. can be chosen to fit your purpose.

---

## 5. Things to Watch Out For ⚠️

1. **No explicit schema, so documentation is essential for teamwork**

   - Since Redis freely adds/deletes fields, **documenting which fields are stored** prevents later confusion.
2. **Memory usage management**

   - Redis uses a lot of memory, so incorrect table schema or index key settings can quickly run out of capacity.
   - Store only necessary fields and regularly delete unnecessary keys or use TTL.
3. **Persistence (Persistence) Setting**

   - By default, RDB snapshots, AOF logs exist, but **data can be lost depending on settings**.
   - If you need to guarantee persistence, combine with RDB or establish appropriate backup policies.
4. **Limits of atomic operations**

   - Multi-key operations can break atomicity, so Lua script processing may be needed when necessary.

---

## 6. Practical Usage Example

Below is an example of implementing the **Product domain** using Redis. Store individual information with `product:{productId}` key and use a `product:all` Set for querying all products.

```
# 1. Create product information hash
HSET product:2001 name "Laptop" price 1200000 stock 25 created_at 1672531200

# 2. Index for managing all products
SADD product:all 2001

# 3. Update specific fields only
HSET product:2001 stock 23

# 4. Check all products list
SMEMBERS product:all
# --> 1) "2001"

# 5. Query product details
HGETALL product:2001
# --> 1) "name"
#     2) "Laptop"
#     3) "price"
#     4) "1200000"
#     5) "stock"
#     6) "23"
#     7) "created_at"
#     8) "1672531200"
```

**Table (Schema) Specification Example**:

| Item | Content |
| --- | --- |
| **Key Prefix** | `product:{productId}` |
| **Data Structure** | Hash |
| **Fields** | - **name** (String)   - **price** (Integer)   - **stock** (Integer)   - **created_at** (Timestamp) |
| **TTL** | None |
| **Index Key** | `product:all` (Set) – manages all productIds |
| **Description** | Hash structure for storing product information (name, price, inventory, etc.) |
| **Example Command** | `HSET product:2001 name "Laptop" price 1200000 stock 25 created_at 1672531200` |
| **Precautions** | - use integer type for price and stock   - if stock becomes 0 or negative, inventory management logic is needed |

---

## 7. Conclusion

Although Redis doesn't have schema like relational DBs, **systematically defining keys and data structures**, and **documenting them for everyone to understand**, allows much safer and more efficient operation.

- **Classify data with consistent Key Prefix**
- **Define Hash fields clearly to prevent confusion during teamwork**
- **Control memory and performance through TTL and index configuration**

Following this "table specification" approach allows **quick retrieval of necessary data**, and **flexibility and scalability** can be achieved in diverse applications like **caching layers** and **session storage**.

---

### References

- **Redis Official Documentation**: <https://redis.io/documentation>
- **Redis Commands**: <https://redis.io/commands>
- **Naming Conventions**(Redis Best Practices):
  - [Redis Labs Blog](https://redis.com/blog)
  - [AWS Redis Key Naming Best Practices](https://aws.amazon.com/blogs/) (not official guide, reference case)
- **Redis Schema Design Methods**:
  - [Redis in Action](https://www.manning.com/books/redis-in-action) (Book)

Good Redis design gives you both ultra-high performance and flexible structure. Going forward, please master **table (schema) specification writing methods** to effectively utilize Redis in your projects!
