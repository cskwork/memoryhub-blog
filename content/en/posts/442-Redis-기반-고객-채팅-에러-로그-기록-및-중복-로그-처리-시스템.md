---
title: "Redis-Based Customer Chat Error Logging and Duplicate Log Handling System"
date: 2025-02-09T01:40:01+09:00
slug: "442-Redis-기반-고객-채팅-에러-로그-기록-및-중복-로그-처리-시스템"
original_url: "https://memoryhub.tistory.com/442"
tistory_id: 442
draft: false
categories: ["Dev Database"]
tags: ["Redis"]
---

Today, I'll show you how to use **Redis** to efficiently record customer chat errors in your production environment and create a system that returns existing logs when duplicates occur. This post is written in technical blog format, explaining a simple yet scalable structure using Redis with example code.

---

## **1. What is a Customer Chat Error Logging and Duplicate Log Handling System?**

In typical chat services, the following problems occur:

1. **Large-scale logs generated in real-time**: As users increase, error logs grow exponentially.
2. **Duplicate log handling**: When specific errors occur repeatedly, storage space and analysis efficiency suffer.
3. **Fast access and search**: When issues arise, logs need to be checked quickly.

This system uses **Redis** to **record customer chat errors in real-time** and **minimize duplicate processing by returning existing error logs when they occur again**.

---

## **2. How Does It Work?**

### **1) Basic Structure**

Redis is used as a data store, with the main data flow as follows:

1. **Error occurs**: When an error occurs in the customer chat service, error information (error code, message, occurrence time, etc.) is structured and sent as a log.
2. **Redis check**: Check if the error message already exists in Redis.
   - If it exists: Return the cached error log as is.
   - If it doesn't exist: Save it as a new error log in Redis.
3. **Return and additional processing**:
   - If the error log already exists: Return the existing log information from Redis, and optionally increase the count or update only the most recent occurrence time.
   - For new error logs: Can forward the error information to a log server (e.g., Elasticsearch, Logstash) or monitoring system.

### **2) Basic Data Model**

Assuming a key-value structure in Redis:

- **Key**: A unique string that identifies the error message (or error code)
- **Value**: JSON or Hash containing additional information (occurrence time, count, detailed message, etc.)

Here's an example using a hash structure:

```
# key: "error:{errorCodeOrMessage}"
HSET "error:DB_CONNECTION_FAIL"
    "message" "DB connection timed out."
    "first_occurrence" "2025-02-01 10:00:00"
    "last_occurrence" "2025-02-01 10:00:00"
    "count" 1
```

### **3) Practical Example (Java assumed)**

```
import redis.clients.jedis.Jedis;

public class ChatErrorLogger {

    private Jedis jedis;

    public ChatErrorLogger(String redisHost, int redisPort) {
        jedis = new Jedis(redisHost, redisPort);
    }

    public ErrorLog logError(ErrorLog errorLog) {
        String key = "error:" + errorLog.getErrorCode(); 
        // Parse error code or message uniquely and set as key

        if (jedis.exists(key)) {
            // Error already exists, so retrieve the log
            String lastOccurrence = jedis.hget(key, "last_occurrence");
            int count = Integer.parseInt(jedis.hget(key, "count"));

            // Increase count
            jedis.hset(key, "count", String.valueOf(count + 1));

            // Update last_occurrence (current time)
            String currentTime = getCurrentTime();
            jedis.hset(key, "last_occurrence", currentTime);

            // Retrieve value from Redis and return
            return new ErrorLog(
                errorLog.getErrorCode(),
                jedis.hget(key, "message"),
                jedis.hget(key, "first_occurrence"),
                currentTime,
                count + 1
            );

        } else {
            // New error log, save to Redis
            jedis.hset(key, "message", errorLog.getMessage());
            String currentTime = getCurrentTime();
            jedis.hset(key, "first_occurrence", currentTime);
            jedis.hset(key, "last_occurrence", currentTime);
            jedis.hset(key, "count", "1");

            // Return immediately with entered content
            return new ErrorLog(
                errorLog.getErrorCode(),
                errorLog.getMessage(),
                currentTime,
                currentTime,
                1
            );
        }
    }

    // Example method for formatting current time
    private String getCurrentTime() {
        // Use SimpleDateFormat, etc.
        return "2025-02-09 12:00:00";
    }
}

// Simple DTO example for holding error log information
class ErrorLog {
    private String errorCode;
    private String message;
    private String firstOccurrence;
    private String lastOccurrence;
    private int count;

    public ErrorLog(String errorCode, String message,
                    String firstOccurrence, String lastOccurrence, int count) {
        this.errorCode = errorCode;
        this.message = message;
        this.firstOccurrence = firstOccurrence;
        this.lastOccurrence = lastOccurrence;
        this.count = count;
    }

    // Getter, Setter
}
```

#### Summary of Operation

1. **Redis key lookup**: Check if the error code/message is stored via `jedis.exists(key)`.
2. **Duplicate log handling**: If it exists, increase the `count` value and update only `last_occurrence`.
3. **New log handling**: If it's a new log, save it to Redis as a hash structure.
4. **Return result**: Finally return the stored information as an object so the system can handle subsequent tasks.

---

## **3. Key Advantages**

1. **Real-time processing**: Since Redis is memory-based, error logs can be written and read quickly.
2. **Saving duplicate data**: For error logs that already exist, prevent duplicate recording and only process count increases, using storage space efficiently.
3. **Scalability**: Redis clustering is possible, so horizontal scaling is easy even with increased users or exploding logs.
4. **Analysis-friendly**: By managing duplicate occurrences and recent occurrence times, error occurrence patterns are easy to identify.

---

## **4. Things to Watch Out For ⚠️**

1. **Data persistence**: Redis is basically memory-based, so data can be lost at restart if persistence (AOF, RDB) is not properly configured.
2. **Key expiration policy**: If you don't need to keep all error logs indefinitely, consider using `EXPIRE` setting to auto-delete after a certain time.
3. **Log analysis system integration**: Redis is not a permanent log storage, so integration with other log management systems like Elasticsearch, S3, etc. is necessary if search or long-term retention is needed.
4. **Memory usage management**: If logs accumulate long-term, Redis memory can run out. Periodic backups or expiration strategies are important.

---

## **5. Practical Usage Example**

Below is a simple example scenario:

1. **User A** generates "DB_CONNECTION_FAIL" error for the first time -> Create new log key in Redis, `count = 1`, `first_occurrence = now`, `last_occurrence = now`
2. One minute later, **User B** also has the same error -> Key already exists, so `count = 2`, `last_occurrence` updated
3. 10 minutes later, **User C** generates a new "API_TIMEOUT" error -> Create another key in Redis ("error:API_TIMEOUT")

Multiple users, but identical errors are not stored duplicated—only the count increases. Monitoring dashboard or tools like Kibana can visualize data retrieved from Redis (error occurrence frequency, recent occurrence time), making **error analysis much more efficient**.

```
public class ChatErrorLogTest {
    public static void main(String[] args) {
        ChatErrorLogger logger = new ChatErrorLogger("localhost", 6379);

        ErrorLog log1 = logger.logError(new ErrorLog("DB_CONNECTION_FAIL", 
            "DB connection timed out.", null, null, 0));
        System.out.println("First log occurred: " + log1.getCount()); // count = 1

        ErrorLog log2 = logger.logError(new ErrorLog("DB_CONNECTION_FAIL", 
            "DB connection timed out.", null, null, 0));
        System.out.println("Duplicate log occurred: " + log2.getCount()); // count = 2

        ErrorLog log3 = logger.logError(new ErrorLog("API_TIMEOUT", 
            "External API did not respond.", null, null, 0));
        System.out.println("New error log occurred: " + log3.getCount()); // count = 1
    }
}
```

---

## **6. Conclusion**

Using Redis makes **real-time error logging** convenient and allows **efficient operation of log storage** through **duplicate log handling**. Additionally, by using simple key-value and hash structures, you can quickly update important information such as **occurrence frequency** and **recent occurrence time**.

With this technology, you can **easily solve duplicate log problems** and **quickly query data** needed for **log analysis and monitoring** processes. Furthermore, if you transmit logs requiring permanent retention to subsequent systems (Elasticsearch, S3, etc.) and use expiration policies properly in Redis, you can build a **more stable and scalable log processing system**.

---

### **References and Sources**

- [Redis Official Documentation](https://redis.io/docs/)
- [Jedis Library GitHub](https://github.com/redis/jedis)
- [Elastic Stack (Elasticsearch) Official Documentation](https://www.elastic.co/guide/index.html)

That concludes the **Redis-based customer chat error logging and duplicate log handling system** specification. When applying to actual production environments, I recommend also considering Redis configuration, log monitoring system integration, and security issues (access control, TLS, etc.)!
