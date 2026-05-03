---
title: "DB Isolation Levels - Understanding with AICC Call Center Examples"
date: 2025-02-15T10:27:59+09:00
slug: "449-DB-격리-수준-Isolation-Levels-을-AICC-콜센터-예제와-함께-알아보기"
original_url: "https://memoryhub.tistory.com/449"
tistory_id: 449
draft: false
---

Today, let's explore the isolation levels of database transactions. In AICC call center systems, **multiple customers access simultaneously**, and **multiple consultants handle chats, calls, and consultations concurrently**. How **transaction isolation levels** are applied is crucial for safely guaranteeing this **concurrency (Concurrency)**.

---

## 1. What is Isolation Level?

**Isolation Level** is a rule that determines whether each transaction can see **intermediate computation results of other transactions** when the database processes multiple transactions simultaneously.

- **Why is it needed?**
   When many transactions execute simultaneously, you must maintain **data integrity and consistency** while also achieving **maximum performance** (concurrency).

Typically, database systems provide four basic isolation levels (ANSI/ISO standard):

1. **READ UNCOMMITTED**
2. **READ COMMITTED**
3. **REPEATABLE READ**
4. **SERIALIZABLE**

---

## 2. AICC Call Center Scenario

Let's think about situations frequently occurring in AICC call center systems.

1. Multiple customers **open chat sessions simultaneously** and exchange messages.
2. Multiple consultants **simultaneously check customer information** or **update consultation status**.
3. A module exists for **querying and analyzing consultation history** in real-time.

In such situations, if one transaction (e.g., "INSERT chat log for customer A") doesn't finish before another transaction (e.g., "Administrator SELECTs current chat log for customer A") accesses, you must decide **"at which point"** to show the data. This is precisely what **isolation level** controls.

---

## 3. Characteristics and AICC Cases for Each Isolation Level

### 3.1 READ UNCOMMITTED

The **lowest** isolation level, where **uncommitted (UNCOMMITTED) changes of one transaction** can be read by other transactions.

- **Advantage**: Highest concurrency (almost no locks).
- **Disadvantage**: **Dirty Read** occurs.
  - Dirty Read: A situation where another transaction reads data not yet committed.
  - If rollback occurs, the read data becomes incorrect.

#### AICC Call Center Example

- Consultant A is entering new customer information into DB (before commit), and Consultant B queries the "new customer" list.
- But if Consultant A encounters error and **rolls back** during entry? The new customer information Consultant B saw is **actually non-existent** data.

> **For this reason**, READ UNCOMMITTED is almost never used in real production environments.

---

### 3.2 READ COMMITTED

**One of the most widely used default** isolation levels, restricting reading to **only committed (Committed) data**.

- **Dirty Read** is prevented (cannot see uncommitted data).
- But **Non-Repeatable Read** can still occur.
  - Non-Repeatable Read: When one transaction queries the same query twice, if another transaction modifies and commits the data in between, results differ.

#### AICC Call Center Example

- Consultant A queries customer information (e.g., "Younghee Kim" customer's phone number).
- After the query, Consultant B modifies the same customer information (phone number change) and commits.
- When Consultant A **queries again** for "Younghee Kim" information, they get **different from first query results**.
- Though not a major issue for call center work itself, if requirement is **"must see consistent information within same transaction"**, it could be inconvenient.

> **READ COMMITTED** shows the latest committed data at the moment "SELECT is executed" for each transaction.

---

### 3.3 REPEATABLE READ

**Default** in many systems like MySQL InnoDB.

- To prevent **Non-Repeatable Read**, within one transaction **data already read (SELECTed)** guarantees **same as first read even on re-read**.
- But **Phantom Read** can still occur.
  - Phantom Read: When new rows matching WHERE condition are inserted and committed midway, result set row count differs from previous SELECT.

#### AICC Call Center Example

- Consultant A starts a transaction querying "today's newly received chat sessions".
- First query resulted in 5 chat sessions.
- **Meanwhile** Consultant B adds new chat session and commits.
- When Consultant A **queries again** for "today's newly received chat sessions", the newly created session (6th) might **appear**. This is **Phantom Read**.

> MySQL InnoDB's REPEATABLE READ prevents **Non-Repeatable Read** through MVCC (Multi-Version Concurrency Control), but cannot prevent "rows themselves" from being added/deleted through INSERT/DELETE, so "phantom records" can appear.

---

### 3.4 SERIALIZABLE

**Most rigorous** isolation level, guaranteeing **multiple transactions serialize** (executed sequentially in same way).

- Both **Non-Repeatable Read** and **Phantom Read** can be prevented.
- But **uses many locks**, significantly reducing concurrency. **Performance** is important consideration in systems where this is rarely used.

#### AICC Call Center Example

- Suppose all operations like consultation history inquiry, customer information modification must be processed sequentially in strict order, then Serializable level can be used.
- But in high-traffic call center systems where multiple consultants must simultaneously update data, inter-transaction wait times lengthen, causing **response delays**.

---

## 4. Summary of Issues Occurring in Each Isolation Level

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Typical Use |
| --- | --- | --- | --- | --- |
| READ UNCOMMITTED | Occurs | Occurs | Occurs | Almost never used |
| READ COMMITTED | Prevented | Occurs | Occurs | Oracle, MSSQL default |
| REPEATABLE READ | Prevented | Prevented | Occurs | MySQL InnoDB default |
| SERIALIZABLE | Prevented | Prevented | Prevented | Most rigorous; performance↓ |

---

## 5. Which Isolation Level to Choose for AICC Call Centers? ⚖️

1. **READ COMMITTED**

   - **Most commonly used** in real work. Prevents Dirty Read while securing **adequate concurrency**.
   - Sufficient for typical transaction processing like consultation history inquiry, customer information modification.
2. **REPEATABLE READ**

   - MySQL InnoDB default. Prevents Non-Repeatable Read so **same SELECT query results are consistent within one transaction**.
   - However, "phantom records" can occur, so **caution needed** if wanting to see aggregation or statistics precisely at "fixed point".
3. **SERIALIZABLE**

   - Can be used in places where **integrity is absolutely critical**, like bank transactions or airline reservation systems where "people's lives are at stake".
   - But risks dramatic performance degradation in call centers with high concurrent traffic.

---

## 6. Practical Implementation Example

Below is how to set **global transaction isolation level** in MySQL.

```
-- Check current isolation level
SELECT @@GLOBAL.tx_isolation, @@tx_isolation;

-- Set to REPEATABLE READ (MySQL InnoDB default)
SET GLOBAL TRANSACTION ISOLATION LEVEL REPEATABLE READ;

-- Set isolation level for specific session only
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

Other DBMS like **Oracle** and **PostgreSQL** allow similar adjustments to transaction isolation levels.

---

## 7. Conclusion

In **multi-user** and **real-time processing** environments like AICC call centers, performance and data integrity vary significantly depending on **how database transaction isolation level is configured**.

- **READ UNCOMMITTED** has performance advantages but **Dirty Read** issues make it not recommended for production.
- Most cases are sufficiently handled by **READ COMMITTED** or **REPEATABLE READ**.
- **SERIALIZABLE** is most stable but **can have worst performance**; keep this in mind.

Ultimately, **isolation level** should be determined by synthesizing AICC call center system's characteristics (traffic volume, data integrity requirement degree, analysis vs. real-time processing ratio, etc.).

Finding **balance** between **concurrency** and **data stability** through appropriate isolation level selection means consultants can **smoothly** handle multiple customers, and customers can **experience service without delays**.

---

### **References and Sources**

- [MySQL Official Documentation - Transaction Isolation Levels](https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-isolation-levels.html)
- [Oracle Database Concepts - Isolation Levels](https://docs.oracle.com/en/database/)
- [PostgreSQL Official Documentation - Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html)

Refer to above materials to wisely choose **isolation level** matching your AICC system design!
