---
title: "ElasticSearch Introduced"
date: 2024-06-09T13:37:08+09:00
slug: "235-ElasticSearch-Introduced"
original_url: "https://memoryhub.tistory.com/235"
tistory_id: 235
draft: false
categories: ["Dev AWS"]
tags: ["ElasticSearch"]
cover:
  image: "/images/235-ElasticSearch-Introduced/img.png"
  relative: false
  hidden: false
---

*ElasticSearch is a distributed search engine that can quickly find information within large datasets, similar to how you might find a book in a vast library using an advanced catalog system.*

### The Big Picture

Imagine you have a giant library with millions of books, and you need to find all the books that mention "quantum physics" within seconds. Doing this manually would be nearly impossible. ElasticSearch is like a super-efficient librarian with an advanced catalog system that can search through all the books quickly and accurately.

### Core Concepts

- **History and Evolution**:
  - **Lucene**: The foundational search library created by Doug Cutting, using an inverted index for efficient search.
  - **Solr**: Built on Lucene, enabling distributed processing, dominated the search engine market before ElasticSearch.
  - **ElasticSearch**: Also built on Lucene, it has become the dominant search engine since 2016.
- **Data Structures**:
  - **Index**: Comparable to a database, storing and organizing documents.
  - **Shard**: Subdivision of an index, distributed across nodes for parallel processing.
  - **Document**: Basic unit of data in JSON format, akin to a row in RDBMS.
  - **Field**: Component of a document, similar to columns in RDBMS.
- **Key Features**:
  - **Inverted Index**: Maps terms to their locations in documents, allowing fast full-text searches.
  - **Distributed Architecture**: Uses shards and replicas for scalability and fault tolerance.
  - **RESTful API**: Facilitates interaction via HTTP, allowing JSON-based requests and responses.
  - **Schemaless**: Automatically indexes unstructured data, flexible and adaptable.

1. **Indexing**: Think of an index as a catalog in a library. ElasticSearch creates an index to store and organize data, making it easier to search through.
2. **Documents**: In ElasticSearch, data is stored in documents, which are like individual books. Each document contains various fields that hold the data.
3. **Shards and Replicas**: To handle large amounts of data and ensure reliability, ElasticSearch splits the index into smaller pieces called shards. Replicas are copies of these shards that provide fault tolerance.
4. **Querying**: ElasticSearch uses a powerful querying language to search through the indexed data. It can handle both simple and complex queries.
5. **Inverted Index**: This is the core data structure that allows ElasticSearch to perform quick full-text searches. It’s like having an advanced glossary that maps every word to the books (documents) that contain them.

### Detailed Walkthrough

1. **Indexing Data**:
   - When data is added to ElasticSearch, it’s indexed. This process involves breaking down the data into a structured format.
   - For example, adding a document about a book on quantum physics would involve indexing terms like "quantum," "physics," "author," "publication date," etc.
2. **Inverted Index**:
   - ElasticSearch uses an inverted index to allow fast full-text searches. An inverted index is a data structure that maps terms to their locations in documents.
   - Imagine you have a book about "quantum physics" and another about "classical physics." The inverted index would have entries like:
     - "quantum" -> Document 1
     - "classical" -> Document 2
     - "physics" -> Document 1, Document 2

![](/images/235-ElasticSearch-Introduced/img.png)

1. **Sharding and Replication**:
   - An index is divided into shards, allowing ElasticSearch to distribute data across multiple nodes (servers). This improves search performance and storage capacity.
   - Each shard can have replicas, ensuring data is not lost if a node fails. If one node goes down, another node with the replica can take over.
2. **Querying**:
   - ElasticSearch allows various types of queries: match queries, term queries, range queries, and more.
   - A match query for "quantum physics" would search through the indexed terms and retrieve documents containing those words.

## ES vs RDBMS

![](/images/235-ElasticSearch-Introduced/img_1.png)

2

### Features and Advantages

1. **Open Source**: Active community improving the tool.
2. **Full-Text Search**: Indexes entire content for comprehensive searches.
3. **Statistical Analysis**: Collects and analyzes log data, integrates with Kibana for visualization.
4. **Schemaless**: Automatically indexes various data types.
5. **RESTful API**: Ensures compatibility across platforms.
6. **Multi-Tenancy**: Supports multiple indexes with common search fields.
7. **Document-Oriented**: Supports hierarchical document storage and querying.
8. **Scalability**: Distributes data across shards for efficient processing.

### Drawbacks

1. **Near Real-Time**: Indexed data is searchable after a slight delay.
2. **No Transaction Rollback**: Lacks support for transaction rollback to enhance performance.
3. **Update Cost**: Updates are costly as they involve deleting and recreating documents.

### Understanding Through an Example

Let's say you have a dataset of scientific papers. You want to find all papers that mention "dark matter" in the title and were published after 2015. Here’s how ElasticSearch handles this:

1. **Indexing**:
   - Each paper is indexed with fields like "title," "author," "publication\_date," and "content."
   - The term "dark matter" and publication dates are indexed.
2. **Querying**:
   - You create a query: `{"query": {"bool": {"must": [{"match": {"title": "dark matter"}}, {"range": {"publication_date": {"gt": "2015-01-01"}}}]}}}`
   - ElasticSearch searches through the inverted index for "dark matter" in the title field and filters out papers published before 2015.
3. **Result**:
   - The query returns a list of papers matching the criteria, thanks to the efficient indexing and querying system.

### Conclusion and Summary

ElasticSearch works by creating an index of documents, breaking down the data into searchable terms using an inverted index, and distributing the data across multiple shards and replicas for scalability and fault tolerance. Queries are then run against this index, allowing for fast and efficient search results even in large datasets.

### Test Your Understanding

1. What is an inverted index, and why is it crucial for ElasticSearch?
2. How does sharding improve the performance of ElasticSearch?
3. Describe the role of replicas in ElasticSearch.

### Reference

For further learning, refer to the [ElasticSearch Definitive Guide](https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html).

[https://jaemunbro.medium.com/elastic-search-%EA%B8%B0%EC%B4%88-%EC%8A%A4%ED%84%B0%EB%94%94-ff01870094f0](https://jaemunbro.medium.com/elastic-search-%EA%B8%B0%EC%B4%88-%EC%8A%A4%ED%84%B0%EB%94%94-ff01870094f0 "Elastic Search Medium")
