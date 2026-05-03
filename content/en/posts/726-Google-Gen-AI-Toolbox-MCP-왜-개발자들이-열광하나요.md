---
title: "? Google Gen AI Toolbox + MCP, Why Are Developers Going Crazy?"
date: 2025-07-18T03:01:08+09:00
slug: "726-Google-Gen-AI-Toolbox-MCP-왜-개발자들이-열광하나요"
original_url: "https://memoryhub.tistory.com/726"
tistory_id: 726
draft: false
categories: ["Dev Library"]
tags: ["MCP"]
---

```
        ┌─────────────────────────────────────────┐
        │      ? Developer-Defined Tools       │
        │   ┌─────────────────────────────────┐   │
        │   │ tools.yaml                      │   │
        │   │ ├─ search-hotels-by-name        │   │
        │   │ │  └─ statement: SELECT * FROM..│   │
        │   │ ├─ book-hotel                   │   │
        │   │ │  └─ statement: UPDATE hotels..│   │
        │   └─────────────────────────────────┘   │
        └─────────────────────┬───────────────────┘
                              │
        ┌─────────────────────▼───────────────────┐
        │     ? AI Agent Executes Tools           │
        │   Claude selects from defined tools     │
        └─────────────────────────────────────────┘
```

Google Gen AI Toolbox Tools define actions an agent can take. Rather than automatically converting natural language to SQL, **developers define SQL queries directly and AI selects and executes those tools**.

In the tools section of the tools.yaml file, you define the actions an agent can take: explicitly specifying what type of tool it is, what source it affects, what parameters it uses, and so on.

⚡ **TL;DR**: Google Gen AI Toolbox is a system where developers create 'tools' with manually-defined SQL queries, and AI agents select and execute tools appropriate to the situation. The key is **pre-defined safe tool combinations** rather than automatic SQL generation.

## Table of Contents

1. Background - Why is a tools-centric approach important?
2. Core concepts explained - Tools and manual query definition
3. Hands-on - Creating tools with tools.yaml
4. Best practices
5. Conclusion & References

---

## 1. Background

### Problems with Traditional Approaches

Most AI-to-database connections try to automatically convert natural language to SQL. However, connecting an LLM directly to a SQL database creates operational and security issues: unsafe query generation, poor connection lifecycle management, and exposure of sensitive credentials.

### Advantages of a Tools-Centric Approach

By having the database schema understood introspectively and exposed for use by LLMs or agents, it enables safe, schema-validated queries. **AI selects and executes pre-defined safe query templates created by developers**.

### Terminology

| Term | Explanation |
| --- | --- |
| **Tool** | An action an agent can take, such as executing a SQL statement |
| **Statement** | The actual SQL query to execute in a tool (receives parameters via $1, $2) |
| **Parameters** | Input values passed to SQL placeholders |
| **Template Parameters** | Parameters that can dynamically replace table names, column names, etc. |

## 2. Core Concepts

> **Tools are SQL tool collections defined directly by developers**  
> Developers can define tools as a map in the tools section of the tools.yaml file. Typically, tools need a source to work with.

### Core Architecture: Manual Query Definition

In tools.yaml, each tool explicitly defines kind, source, statement, and parameters:

```
tools:
  search-hotels-by-name:
    kind: postgres-sql
    source: my-pg-source  
    statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%'
    description: Search for hotels based on name.
    parameters:
      - name: name
        type: string
        description: The name of the hotel.
```

**Important point**: AI doesn't generate SQL; rather, **AI selects the appropriate tool from pre-written queries created by developers**.

## 3. Hands-on

### ① Writing a Complete tools.yaml

Let's define tools for an actual hotel reservation system:

```
sources:
  my-pg-source:
    kind: postgres
    host: 127.0.0.1
    port: 5432
    database: toolbox_db
    user: ${USER_NAME}
    password: ${PASSWORD}

tools:
  search-hotels-by-name:
    kind: postgres-sql
    source: my-pg-source
    description: Search for hotels based on name.
    statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%'
    parameters:
      - name: name
        type: string
        description: The name of the hotel.

  book-hotel:
    kind: postgres-sql  
    source: my-pg-source
    description: Book a hotel by its ID.
    statement: UPDATE hotels SET booked = B'1' WHERE id = $1
    parameters:
      - name: hotel_id
        type: string
        description: The ID of the hotel to book.

  cancel-hotel:
    kind: postgres-sql
    source: my-pg-source  
    description: Cancel a hotel by its ID.
    statement: UPDATE hotels SET booked = B'0' WHERE id = $1
    parameters:
      - name: hotel_id
        type: string
        description: The ID of the hotel to cancel.

toolsets:
  hotel-management:
    - search-hotels-by-name
    - book-hotel
    - cancel-hotel
```

### ② Using Template Parameters

Template parameters allow dynamic replacement of table names and column names, but they're vulnerable to SQL injection. Basic parameters are recommended for performance and security:

```
select-columns-from-table:
  kind: postgres-sql
  source: my-pg-instance
  statement: SELECT {{array .columnNames}} FROM {{.tableName}}
  templateParameters:
    - name: tableName
      type: string
    - name: columnNames  
      type: array
      items:
        name: column
        type: string
```

### ③ Running and Testing the Server

```
./toolbox --tools-file "tools.yaml"
```

## 4. Best Practices

| Pattern | Benefits | Considerations |
| --- | --- | --- |
| **Using basic parameters** | Preferred for performance and security | Limited flexibility |
| **Tools requiring authentication** | Check authentication with authRequired field | Increased configuration complexity |
| **Automatic authentication parameters** | Automatically extract user info from ID token | Requires token setup |

### Security Considerations

**Using authenticated parameters:**

```
search-flights-by-user-id:
  kind: postgres-sql
  statement: SELECT * FROM flights WHERE user_id = $1
  parameters:
    - name: user_id
      type: string
      authServices:
        - name: my-google-auth
          field: sub  # OIDC user ID claim
```

### Real-world Use Cases

Customer service agents that search user information from relational databases in real-time, BI assistants that query analytical databases to answer business metric questions, and DevOps bots that monitor database status and report anomalies.

## 5. Conclusion

**What we learned:**

- Google Gen AI Toolbox's core is **systematic management of pre-defined tools** rather than automatic SQL generation
- AI selects and executes SQL tools directly defined by developers in tools.yaml based on the situation
- This approach greatly enhances security and stability while giving developers complete control

**Tips for real-world projects**: Define tools in YAML files like "search movies" or "check customer rentals" and design the LLM to select and execute tools based on user queries.

⸻

## References

**Official Documentation**

- [Tools Definition Guide](https://googleapis.github.io/genai-toolbox/resources/tools/)
- [Python Quickstart](https://googleapis.github.io/genai-toolbox/getting-started/local_quickstart/)

**Sample Repository**

- [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox)

**Additional Reading**

- [Google Cloud's Gen AI Toolbox Announcement](https://cloud.google.com/blog/products/ai-machine-learning/announcing-gen-ai-toolbox-for-databases-get-started-today)
- [DVD Rental Chatbot Hands-on Guide](https://medium.com/google-cloud/building-a-dvd-rental-chatbot-using-llamaindex-agentworkflow-google-genai-toolbox-postgresql-5d6e806d5891)
- [AlloyDB and MCP Toolbox Integration](https://codelabs.developers.google.com/genai-toolbox-for-alloydb)

---

### ? Glossary (Easy Enough for Kids to Understand)

**Tools**: Pre-made tasks that AI can use (like Lego blocks)  
**Statement**: A special language you use to tell the database "find this for me"  
**Parameters**: Specific information you pass to a tool (e.g., the hotel name "Holiday Inn")  
**Template Parameters**: Special settings that can change the shape of a tool itself  
**Toolsets**: A box of related tools grouped together
