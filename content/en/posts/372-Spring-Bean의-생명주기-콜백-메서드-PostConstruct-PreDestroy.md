---
title: "Spring Bean Lifecycle Callbacks (@PostConstruct & @PreDestroy)?"
date: 2024-11-14T12:32:25+09:00
slug: "372-Spring-Bean의-생명주기-콜백-메서드-PostConstruct-PreDestroy"
original_url: "https://memoryhub.tistory.com/372"
tistory_id: 372
draft: false
---

Hello! Today, let's explore the callback methods that are executed when Spring Beans are initialized and destroyed.

## Why Do We Need Bean Lifecycle Callbacks?

There are cases where special work is needed right after a Bean is created or just before it's destroyed, such as database connections, cache initialization, and external resource loading.

For example:

- Loading configuration files required when the application starts
- Initializing database connection pools
- Cleaning up temporary files
- Releasing resources

## @PostConstruct?

A method that executes after a Bean is created and dependency injection is complete.

```
@Service
public class UserService {

    private Cache cache;

    @PostConstruct
    public void init() {
        System.out.println("UserService initialization started");
        cache = new Cache();
        // Cache warm-up
        cache.preloadData();
    }
}
```

### @PostConstruct Characteristics

1. **Execution Timing**

   - After constructor is called
   - After dependency injection is complete
   - Before the Bean is actually used
2. **Use Cases**

   - Loading initial data
   - Connecting to external resources
   - Cache warm-up

## @PreDestroy?

A method that executes before the Spring container shuts down.

```
@Component
public class DatabaseManager {

    private Connection conn;

    @PreDestroy
    public void cleanup() {
        System.out.println("Resource cleanup started");
        if(conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                // Exception handling
            }
        }
    }
}
```

### @PreDestroy Characteristics

1. **Execution Timing**

   - Just before Spring container shuts down
   - Just before Bean is deleted
2. **Use Cases**

   - Closing connections (DB, network)
   - Deleting temporary files
   - Cleaning up cache

## Practical Examples?

### 1. S3 File Caching Service

```
@Service
public class FileService {

    private Map<String, byte[]> fileCache;

    @PostConstruct
    public void initializeCache() {
        fileCache = new HashMap<>();
        // Pre-download frequently used files from S3
        downloadFrequentlyUsedFiles();
    }

    @PreDestroy
    public void clearCache() {
        fileCache.clear();
        // Delete temporary files
        deleteTempFiles();
    }
}
```

### 2. Database Connection Pool Management

```
@Component
public class DatabaseConnectionPool {

    private List<Connection> connectionPool;

    @PostConstruct
    public void initialize() {
        connectionPool = new ArrayList<>();
        // Create initial connections
        createInitialConnections();
    }

    @PreDestroy
    public void disconnect() {
        // Close all connections
        connectionPool.forEach(this::closeConnection);
    }
}
```

## Precautions ⚠️

1. **@PostConstruct**

   - Dependency injection is not yet complete in the constructor
   - Recommended to run heavy operations on separate threads
2. **@PreDestroy**

   - Will not execute if the application is forcibly terminated
   - Consider alternative methods if execution is mandatory

## Closing Remarks?

By properly utilizing Bean lifecycle callbacks, you can efficiently manage your application's resources. Implement initialization and cleanup operations cleanly!

---

References:

- Spring Framework Documentation: <https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#beans-factory-lifecycle>
- Java EE Tutorial: <https://javaee.github.io/tutorial/resource-creation.html>
- Spring Boot Documentation: <https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-application-lifecycle-callbacks>
