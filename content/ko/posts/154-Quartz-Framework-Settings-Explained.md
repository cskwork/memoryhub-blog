---
title: "Quartz Framework Settings Explained"
date: 2024-05-29T07:56:06+09:00
slug: "154-Quartz-Framework-Settings-Explained"
original_url: "https://memoryhub.tistory.com/154"
tistory_id: 154
draft: false
categories: ["데브 프레임워크"]
tags: ["Spring Batch"]
---

*The Quartz framework's settings, managed through properties, allow you to configure various aspects of scheduling and job execution, making it versatile and adaptable for different use cases.*

### The Big Picture

Imagine Quartz as a sophisticated alarm clock that can set up multiple alarms (jobs) with different schedules (triggers). The properties in Quartz are like the settings of this alarm clock, enabling you to control when and how these alarms go off and how they interact with each other.

### Core Concepts

1. **Scheduler Configuration**
2. **Thread Pool Configuration**
3. **Job Store Configuration**
4. **Miscellaneous Configuration**

### Detailed Walkthrough

#### 1. Scheduler Configuration

These properties configure the main scheduler, controlling its behavior:

```
org.quartz.scheduler.instanceName=MyScheduler
org.quartz.scheduler.instanceId=AUTO
org.quartz.scheduler.skipUpdateCheck=true
org.quartz.scheduler.jmx.export=true
```

- **org.quartz.scheduler.instanceName:** Name of the scheduler instance.
- **org.quartz.scheduler.instanceId:** Unique ID for the scheduler instance. `AUTO` generates a unique ID automatically.
- **org.quartz.scheduler.skipUpdateCheck:** Disables checking for updates.
- **org.quartz.scheduler.jmx.export:** Enables JMX export for management and monitoring.

#### 2. Thread Pool Configuration

Quartz uses a thread pool to manage concurrent job execution:

```
org.quartz.threadPool.class=org.quartz.simpl.SimpleThreadPool
org.quartz.threadPool.threadCount=10
org.quartz.threadPool.threadPriority=5
org.quartz.threadPool.threadsInheritContextClassLoaderOfInitializingThread=true
```

- **org.quartz.threadPool.class:** Class name of the thread pool implementation.
- **org.quartz.threadPool.threadCount:** Number of threads in the pool.
- **org.quartz.threadPool.threadPriority:** Priority of the threads (1 to 10).
- **org.quartz.threadPool.threadsInheritContextClassLoaderOfInitializingThread:** Ensures threads inherit the context class loader.

#### 3. Job Store Configuration

Quartz supports various job stores for persisting job and trigger information:

```
org.quartz.jobStore.class=org.quartz.impl.jdbcjobstore.JobStoreTX
org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.StdJDBCDelegate
org.quartz.jobStore.dataSource=myDS
org.quartz.jobStore.tablePrefix=QRTZ_
org.quartz.jobStore.isClustered=true
```

- **org.quartz.jobStore.class:** Class name of the job store implementation.
- **org.quartz.jobStore.driverDelegateClass:** JDBC delegate class for database operations.
- **org.quartz.jobStore.dataSource:** Name of the data source.
- **org.quartz.jobStore.tablePrefix:** Prefix for Quartz tables in the database.
- **org.quartz.jobStore.isClustered:** Enables clustering for high availability.

#### 4. Miscellaneous Configuration

Additional settings for fine-tuning Quartz behavior:

```
org.quartz.plugin.triggHistory.class=org.quartz.plugins.history.LoggingTriggerHistoryPlugin
org.quartz.plugin.shutdownhook.class=org.quartz.plugins.management.ShutdownHookPlugin
org.quartz.plugin.shutdownhook.cleanShutdown=true
```

- **org.quartz.plugin.triggHistory.class:** Plugin class for logging trigger history.
- **org.quartz.plugin.shutdownhook.class:** Plugin class for handling shutdown hooks.
- **org.quartz.plugin.shutdownhook.cleanShutdown:** Ensures a clean shutdown.

### Understanding Through an Example

Suppose you need to configure a Quartz scheduler with a JDBC job store, a custom thread pool, and logging plugins. Your `application.properties` file would include:

```
# Scheduler Configuration
org.quartz.scheduler.instanceName=MyScheduler
org.quartz.scheduler.instanceId=AUTO
org.quartz.scheduler.skipUpdateCheck=true
org.quartz.scheduler.jmx.export=true

# Thread Pool Configuration
org.quartz.threadPool.class=org.quartz.simpl.SimpleThreadPool
org.quartz.threadPool.threadCount=10
org.quartz.threadPool.threadPriority=5
org.quartz.threadPool.threadsInheritContextClassLoaderOfInitializingThread=true

# Job Store Configuration
org.quartz.jobStore.class=org.quartz.impl.jdbcjobstore.JobStoreTX
org.quartz.jobStore.driverDelegateClass=org.quartz.impl.jdbcjobstore.StdJDBCDelegate
org.quartz.jobStore.dataSource=myDS
org.quartz.jobStore.tablePrefix=QRTZ_
org.quartz.jobStore.isClustered=true

# Miscellaneous Configuration
org.quartz.plugin.triggHistory.class=org.quartz.plugins.history.LoggingTriggerHistoryPlugin
org.quartz.plugin.shutdownhook.class=org.quartz.plugins.management.ShutdownHookPlugin
org.quartz.plugin.shutdownhook.cleanShutdown=true
```

### Conclusion and Summary

Configuring Quartz through properties allows you to tailor the scheduler's behavior to match your application's requirements. From specifying the scheduler instance and thread pool settings to configuring the job store and adding useful plugins, these settings provide flexibility and control.

### Test Your Understanding

1. How would you configure Quartz to use an in-memory job store?
2. What property would you set to ensure the Quartz scheduler uses 20 threads?
3. How can you enable JMX export for managing the Quartz scheduler?

### Reference

For further details, refer to the [Quartz Scheduler Documentation](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/configuration/).

---

By effectively configuring these properties, you can ensure your Quartz-based scheduling system operates smoothly and efficiently, catering to your specific needs and operational constraints.
