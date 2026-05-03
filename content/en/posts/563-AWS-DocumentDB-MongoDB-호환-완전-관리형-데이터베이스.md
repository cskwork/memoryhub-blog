---
title: "AWS DocumentDB - MongoDB-Compatible Fully Managed Database"
date: 2025-04-25T10:16:24+09:00
slug: "563-AWS-DocumentDB-MongoDB-호환-완전-관리형-데이터베이스"
original_url: "https://memoryhub.tistory.com/563"
tistory_id: 563
draft: false
---

Hello! Today, I'd like to introduce you to Amazon DocumentDB, one of AWS's powerful NoSQL database services. Have you ever used MongoDB, or do you need a flexible and scalable database? If so, DocumentDB could be a great choice for you!

Think of it like an intelligent assistant (AWS) perfectly managing your flexible file cabinet (DocumentDB) while also understanding the language of another popular file system (MongoDB). Easy to understand, right?

## Background

In the past, relational databases (RDBMS) dominated when dealing with structured data. However, as web and mobile applications exploded in growth, unstructured and semi-structured data increased significantly, and fast data processing at massive scales and rapid development speed became critical. NoSQL databases emerged to meet these demands.

Among them, MongoDB gained great popularity with its document-based flexible schema (in BSON format similar to JSON) and excellent scalability. However, operating MongoDB directly required managing servers, scaling, backups, high availability configurations, and more. Quite a handful!

That's when AWS introduced **Amazon DocumentDB**. It maintains MongoDB compatibility while combining the advantages of AWS cloud - **fully managed service, excellent scalability, strong durability, and security**. It was created to help existing MongoDB users migrate to the AWS environment with minimal changes and reduce operational burden.

## DocumentDB Features/Use Cases - Solving These Problems!

1. **MongoDB Compatibility**: You can use your existing MongoDB application code, drivers, and tools almost as-is. (Note: 100% compatibility is not guaranteed, see the cautions below!)
2. **Fully Managed Service**: AWS handles all the tedious and repetitive management tasks like hardware provisioning, software patching, configuration, and backups. You can focus solely on application development!
3. **Excellent Scalability**: You can independently scale computing (processing power) and storage (storage space). Storage automatically grows up to 128 TiB, and it can handle millions of read/write requests per second. (Especially when using Elastic Cluster)
4. **High Availability and Durability**: Data is replicated 6 times across 3 availability zones (AZs). Even if a specific data center (AZ) has issues, services continue without data loss, and recovery is nearly instantaneous if failures occur. Robust to the core!
5. **Strong Security**: Running within Amazon VPC enables network access control, encryption of data at rest and in transit, and fine-grained access permission management through IAM. Various security features are provided.

## Core Architecture

How does DocumentDB provide such powerful performance and stability? The key lies in the **separation of storage and computing** architecture.

```
# AWS DocumentDB Cluster Architecture (Overview)

+-----------------------------------+      +------------------------+
|        Application / Client       | ---> | Cluster Endpoint       |
| (MongoDB Driver)                  |      | (Request Distribution) |
|                                   |      |                        |
+-----------------------------------+      +----------+-------------+
                                                     |
       +---------------------------------------------+---------------------------------------------+
       | AWS Region (Multiple Data Centers in One Region)                                     |
       |                                             |                                             |
       |  +-----------------+  Reads/Writes         +-----------------+  Reads                    |
       |  | Primary Instance|<----------------------| Replica Instance|                           |
       |  | (Write/Read)    |---------------------->| (Read-Only)     |                           |
       |  +-------▲---------+                      +--------▲--------+                           |
       |          | Writes/Reads                            | Reads                             |
       |          | (Request Processing)                    | (Request Processing)              |
       |  +-------+-----------------------------------------+--------------------------------+  |
       |  |                  Cluster Volume (Distributed Storage System)                    |  |
       |  | ------------------------------------------------------------------------------- |  |
       |  | | AZ-A Data Copy 1 | | AZ-A Data Copy 2 | | AZ-B Data Copy 3 | | AZ-B Data Copy 4 | |  |
       |  | ------------------------------------------------------------------------------- |  |
       |  | | AZ-C Data Copy 5 | | AZ-C Data Copy 6 |                                       |  |
       |  | ------------------------------------------------------------------------------- |  |
       |  +-----------------------------------------------------------------------------------+  |
       +-----------------------------------------------------------------------------------------+
```

1. **Computing Layer (Instances)**:
   - **Primary Instance (1)**: Handles all data write operations and read operations.
   - **Replica Instances (0-15)**: Handle read-only operations. Distributes read requests to improve performance, and serves as a failover for primary instance failures to increase availability.
2. **Storage Layer (Cluster Volume)**:
   - Data is stored in a **virtual storage volume** distributed across multiple availability zones (AZs).
   - When writing data, the Primary instance records data to this distributed storage volume, and the storage system automatically creates 6 replicas across 3 AZs.
   - Thanks to this structure, you can independently scale/shrink computing (instance specifications) and storage (data capacity), and data durability and availability become very high.
3. **MongoDB Compatibility Layer**:
   - Applications send requests (queries) through MongoDB drivers, which DocumentDB receives and internally translates to match its own storage engine. Currently compatible with MongoDB 3.6, 4.0, and 5.0 APIs.

## Important Cautions and Tips

⚠️ **Be Careful About These!**

1. **MongoDB Compatibility is Not 100%**: While most MongoDB features are compatible, some operators (specific $lookup features, $where, etc.) or administrative commands may not be supported or may behave differently. Before migrating an existing MongoDB application, you must check the [official documentation](https://docs.aws.amazon.com/documentdb/latest/developerguide/compatibility.html) and conduct thorough testing.
2. **Understand the Cost Structure**: DocumentDB charges based on usage. Main cost items are:
   - **Instance Costs**: Charged based on running instance specifications and time.
   - **Storage Costs**: Charged monthly based on stored data volume.
   - **I/O Costs**: Charged based on the number of data read/write operations. (Cost per million operations)
   - *Caution!*: I/O costs in particular can exceed expectations depending on workload patterns. Using instances with insufficient memory increases disk I/O and can cause costs to surge, so be careful.
3. **Performance Optimization is Essential**:
   - **Instance Size**: Choosing an instance with appropriate RAM capacity so that data and indexes (working set) to process can fit in memory is very important for performance.
   - **Indexing**: Just like with MongoDB, you must design and create appropriate indexes to improve query performance.
4. **Managed Service ≠ Fully Automatic**: While AWS manages many aspects, users are still responsible for setting maintenance windows, performance monitoring, cost optimization, security configuration, etc.

💡 **Pro Tips**

- **Application Connection**: It's better to connect to the **cluster endpoint** rather than specific instance endpoints. The cluster endpoint internally routes requests to the Primary instance or distributes read requests to Replica instances through read settings. During failover, it maintains stable connections without changing application code. Using the `secondaryPreferred` read setting helps distribute read load.
- **Leverage Monitoring**: Actively use AWS CloudWatch and Performance Insights to continuously monitor database performance metrics (CPU, memory, I/O, etc.) and slow queries, identify bottlenecks, and improve them. This greatly helps with cost optimization.
- **Backup Strategy**: Verify that automatic backup is enabled and adjust the backup retention period if needed. Point-in-Time Recovery (PITR) supports recovery up to 5 minutes ago, so you can prepare for any emergencies.

## Conclusion

We've explored AWS DocumentDB. Based on MongoDB compatibility, it's an attractive database service where you can enjoy AWS's management convenience, scalability, and stability. It might seem somewhat complex at first, but I hope this article has helped you understand DocumentDB!

If you've used DocumentDB or have any questions, please leave a comment!

## References

- [What is Amazon DocumentDB (MongoDB-compatible)?](https://docs.aws.amazon.com/documentdb/latest/developerguide/what-is.html)
- [Amazon DocumentDB FAQ](https://aws.amazon.com/documentdb/faqs/)
- [Amazon DocumentDB Best Practices](https://docs.aws.amazon.com/documentdb/latest/developerguide/best_practices.html)
- [Amazon DocumentDB MongoDB Compatibility](https://docs.aws.amazon.com/documentdb/latest/developerguide/compatibility.html)
- [Amazon DocumentDB Architecture](https://docs.aws.amazon.com/whitepapers/latest/get-started-documentdb/amazon-documentdb-architecture.html)

---

#AWSDocumentDB #DocumentDB #NoSQL #MongoDB #CloudDatabase #AWS #FullyManaged
