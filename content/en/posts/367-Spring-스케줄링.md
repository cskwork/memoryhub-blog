---
title: "Spring Scheduling"
date: 2024-11-07T09:29:58+09:00
slug: "367-Spring-스케줄링"
original_url: "https://memoryhub.tistory.com/367"
tistory_id: 367
draft: false
categories: ["Dev Framework"]
tags: ["Spring"]
---

Hello! Today we'll explore Spring scheduling, which automates repetitive tasks in Spring.

## What is Spring Task?

Just like setting an alarm every morning:

- Tasks that run automatically at specific times
- Tasks that repeat periodically
- Tasks that need to be processed asynchronously

Spring Task is a framework that makes it easy to implement these automated tasks!

## Core Features

### 1. @Scheduled Annotation

```
@Component
public class ScheduledTasks {

    // Run every day at midnight
    @Scheduled(cron = "0 0 0 * * ?")
    public void dailyTask() {
        System.out.println("Task executed daily at midnight");
    }

    // Run every 5 seconds
    @Scheduled(fixedRate = 5000)
    public void everyFiveSeconds() {
        System.out.println("Task executed every 5 seconds");
    }

    // Run 3 seconds after previous task completes
    @Scheduled(fixedDelay = 3000)
    public void afterPreviousTask() {
        System.out.println("Task executed 3 seconds after previous task completes");
    }
}
```

### 2. Asynchronous Processing (@Async)

```
@EnableAsync
@Configuration
public class AsyncConfig {

    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(10);
        executor.setQueueCapacity(25);
        return executor;
    }
}

@Service
public class AsyncService {

    @Async
    public Future<String> asyncMethod() {
        // Asynchronously processed task
        return new AsyncResult<>("Task completed!");
    }
}
```

## Scheduling Expressions

### 1. Cron Expressions

```
* * * * * *
│ │ │ │ │ │
│ │ │ │ │ └─ Day of week (0-7) (0,7=Sunday, 1=Monday, ...)
│ │ │ │ └─── Month (1-12)
│ │ │ └───── Day (1-31)
│ │ └─────── Hour (0-23)
│ └───────── Minute (0-59)
└─────────── Second (0-59)
```

Examples:

```
// Every day at 10:30 AM
@Scheduled(cron = "0 30 10 * * ?")

// Every Monday at 9:00 AM
@Scheduled(cron = "0 0 9 ? * MON")

// Every 1st of month at midnight
@Scheduled(cron = "0 0 0 1 * ?")
```

## Real-World Usage Examples

### 1. Daily Report Generation

```
@Component
@Slf4j
public class DailyReportScheduler {

    @Scheduled(cron = "0 0 1 * * ?") // Every day at 1 AM
    public void generateDailyReport() {
        log.info("Starting daily report generation");
        // Report generation logic
        log.info("Daily report generation completed");
    }
}
```

### 2. Cache Refresh

```
@Component
public class CacheRefreshScheduler {

    @Scheduled(fixedRate = 600000) // Every 10 minutes
    public void refreshCache() {
        // Cache refresh logic
    }
}
```

### 3. Asynchronous Email Sending

```
@Service
public class EmailService {

    @Async
    public Future<Boolean> sendBulkEmail(List<String> recipients) {
        // Bulk email sending logic
        return new AsyncResult<>(true);
    }
}
```

## Advantages

1. **Simple Configuration**
   - Annotation-based setup
   - Intuitive syntax
   - Spring Boot auto-configuration
2. **Flexibility**
   - Various scheduling options
   - Asynchronous processing support
   - Easy customization
3. **Monitoring and Management**
   - Check scheduling status
   - Error handling
   - Logging support

## Cautions

1. **Resource Management**
   - Set appropriate thread pool size
   - Monitor memory usage
   - Set timeouts
2. **Error Handling**
   - `@Scheduled(fixedRate = 5000)
     public void scheduledTask() {
     try {
     // Task logic
     } catch (Exception e) {
     log.error("Error executing scheduled task", e);
     }
     }`
3. **Cluster Environment**
   - Prevent duplicate execution
   - Consider distributed environment
   - Use lock mechanisms

## Configuration Examples

### Basic Configuration

```
@Configuration
@EnableScheduling
@EnableAsync
public class TaskConfig {

    @Bean
    public TaskScheduler taskScheduler() {
        ThreadPoolTaskScheduler scheduler = new ThreadPoolTaskScheduler();
        scheduler.setPoolSize(10);
        scheduler.setThreadNamePrefix("my-scheduler-");
        return scheduler;
    }
}
```

## References

1. Spring Framework Documentation  
   <https://docs.spring.io/spring-framework/docs/current/reference/html/integration.html#scheduling>
2. Baeldung Spring Task Tutorial  
   <https://www.baeldung.com/spring-scheduled-tasks>
3. Spring @Async Documentation  
   <https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/scheduling/annotation/Async.html>
