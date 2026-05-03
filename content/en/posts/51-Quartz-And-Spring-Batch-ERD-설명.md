---
title: "Quartz and Spring Batch ERD Explanation"
date: 2024-05-25T14:03:02+09:00
slug: "51-Quartz-And-Spring-Batch-ERD-설명"
original_url: "https://memoryhub.tistory.com/51"
tistory_id: 51
draft: false
---

### 🎯 Explaining Distributed Processing with Quartz and Basic Table Structure (ERD) of Spring Batch 📊

Today, we'll explore **distributed processing using Quartz** and the **basic table structures (ERD) of Quartz and Spring Batch**! I hope this helps those who want to efficiently handle, monitor, and manage scheduling tasks in a cluster environment.

---

## **1. What is a Computer Cluster? 🖥️**

A computer cluster is a collection of computers connected through a network to **operate as a single system**.

- 🔄 **Distributed Processing**: A cluster can divide and process work across multiple nodes (servers), allowing fast processing of large-scale data or providing stable services through load balancing.
- 🛡️ **High Availability**: Even if a specific server fails, other servers can take over the work, minimizing service downtime.
- 📈 **Scalability**: When workload increases, you can flexibly improve performance by adding servers.

---

## **2. Distributed Scheduling with Quartz 🎯**

### 2.1 Basic Concepts

**Quartz** is an open-source scheduler library implemented in Java that manages various **Jobs** (logic to be performed) and **Triggers** (execution timing). In a distributed environment (cluster), **Quartz can share work allocation (occupancy) and schedule data through a shared database**.

#### Traditional Approach (Single Server or Memory-Based)

- Schedule information is stored in memory.
- If multiple servers execute the same schedule logic, **duplicate execution** or conflicts can occur.
- If one server fails, scheduling tasks may stop.

#### Cluster Approach (Database-Based)

1. **Store schedule information in database**: All scheduling information including Jobs, Triggers, Cron Expressions, etc. is stored in a central database.
2. **Each server references the database**: When one server claims a trigger first, other servers recognize that it's executing and prevent duplicate execution.
3. **Fault tolerance (HA)**: Even if a specific server goes down, other servers can take over the work through the database.
4. **Load balancing**: When many jobs are registered simultaneously, multiple servers can share trigger execution.

---

### 2.2 Quartz's Main Tables (ERD Concept Overview)

![](/images/51-Quartz-And-Spring-Batch-ERD-설명/img.png)

Quartz uses the following tables to store schedule information in a database (distinguished by `QRTZ_` prefix):

1. **QRTZ_JOB_DETAILS**

   - **Role**: Stores basic information about a Job (logic to be performed).
   - **Key Columns**:
     - `JOB_NAME`, `JOB_GROUP`: Job name and group.
     - `JOB_DATA`: Data needed to execute the Job (serialized objects or parameters).
     - `JOB_CLASS_NAME`: The actual Job class path that Quartz needs to execute.
2. **QRTZ_TRIGGERS**

   - **Role**: Stores Trigger (execution timing) information connected to the Job.
   - **Key Columns**:
     - `TRIGGER_NAME`, `TRIGGER_GROUP`: Trigger name and group.
     - `JOB_NAME`, `JOB_GROUP`: Which Job to execute.
     - Previous/next execution time, priority, status, etc.
3. **QRTZ_CRON_TRIGGERS**

   - **Role**: When a Trigger operates with a Cron expression, stores the schedule information.
   - **Key Columns**:
     - `CRON_EXPRESSION`: Example) `"0 0/5 * * * ?"` (every 5 minutes)
     - `TIME_ZONE_ID`: Timezone information.
4. **QRTZ_SIMPLE_TRIGGERS**

   - **Role**: Stores Simple Trigger information with fixed repeat count or interval.
   - **Key Columns**:
     - `REPEAT_COUNT`, `REPEAT_INTERVAL`: Repeat count and interval.
5. **QRTZ_CALENDARS**

   - **Role**: Stores calendar-based schedule settings that exclude or include specific dates/times.
6. **QRTZ_LOCKS, QRTZ_SCHEDULER_STATE, QRTZ_FIRED_TRIGGERS, QRTZ_PAUSED_TRIGGER_GRPS**

   - **Role**: Manages concurrency control (locks) and executing triggers and paused states in cluster environments.
   - Example) `QRTZ_LOCKS` is used to lock triggers during occupation.

---

### 2.3 Real-World Application Examples

Below is a typical configuration example using **Spring Boot + Spring Batch + Quartz** together.

1) **Job** (Batch task) definition

```
@Bean
public Job testJob() {
    return jobBuilderFactory
            .get("testJob")
            .incrementer(new RunIdIncrementer())
            .start(testStep())
            .build();
}

@Bean
@JobScope
public Step testStep() {
    return stepBuilderFactory
            .get("testStep")
            .<TestDomain, TestDomain>chunk(100)
            .reader(testReader())       // Actual data reading
            .processor(testProcessor()) // Processing logic
            .writer(testWriter())       // Save processing results
            .build();
}
```

- `Job`: Composed of multiple `Steps`.
- `Step`: Executes in Reader -> Processor -> Writer structure.

2) **Quartz JobDetail** definition

```
@Bean
public JobDetail jobDetail() {
    JobDataMap jobDataMap = new JobDataMap();
    jobDataMap.put("jobName", "testJob"); // Name of the Batch Job to execute

    return JobBuilder.newJob(CustomQuartzJobBean.class)
            .withIdentity("testJob", null)
            .setJobData(jobDataMap)
            .storeDurably()
            .build();
}
```

- `JobDataMap`: Passes data needed for Quartz Job execution (here, the name 'testJob').

3) **Quartz Trigger** registration

```
@Bean
public Trigger jobTrigger() {
    // Example: Execute at second 0 of every minute
    CronScheduleBuilder scheduleBuilder = CronScheduleBuilder.cronSchedule("0 * * * * ?");

    return TriggerBuilder
            .newTrigger()
            .forJob(jobDetail().getKey())
            .withIdentity("jobTrigger", null)
            .withSchedule(scheduleBuilder)
            .build();
}
```

- Cron expression `"0 * * * * ?"` means **execute at second 0 of every minute**.

---

## **3. Spring Batch's Basic Table Structure 📋**

![](/images/51-Quartz-And-Spring-Batch-ERD-설명/img_1.png)

Spring Batch uses its own metadata tables to track Job and Step execution history:

1. **BATCH_JOB_INSTANCE**

   - **Role**: Records information about each unique `Job Instance` created when a batch Job is executed once.
   - **Key Columns**: `JOB_INSTANCE_ID`, `JOB_NAME`, etc.
2. **BATCH_JOB_EXECUTION**

   - **Role**: Records start/end time, status, batch results (success/failure) for Job execution.
   - **Key Columns**: `JOB_EXECUTION_ID`, `START_TIME`, `END_TIME`, `STATUS`, etc.
3. **BATCH_JOB_EXECUTION_CONTEXT**, **BATCH_JOB_EXECUTION_PARAMS**

   - **Role**: Stores parameters and context information used during Job execution.
   - **Example**: Specific date ranges, user-defined parameters, etc.
4. **BATCH_STEP_EXECUTION**

   - **Role**: Stores Step-level execution information. When each Step started/ended, how many records were processed, etc.
   - **Key Columns**: `STEP_EXECUTION_ID`, `COMMIT_COUNT`, `READ_COUNT`, `WRITE_COUNT`, etc.
5. **BATCH_STEP_EXECUTION_CONTEXT**

   - **Role**: Stores additional context (state) information used during Step execution.

---

## **4. Key Advantages 🎉**

1. **Stability (High Availability)**

   - Distributed servers share identical schedule information, so if a specific server goes down, another server can take over task execution.
2. **Prevent Duplicate Execution**

   - Through the database lock mechanism, **a single schedule (Job+Trigger)** won't execute simultaneously on multiple servers.
3. **Flexible Schedule Management**

   - Supports **various Trigger types** like Cron, Simple, Calendar.
   - **Easily monitor** execution logs through Batch metadata tables.
4. **Scalability**

   - When workload increases, you can distribute load by adding server nodes.
   - Both Quartz and Spring Batch are designed to operate stably as scale grows.

---

## **5. Points to Watch ⚠️**

1. **Database Table Creation and Configuration**

   - Quartz and Spring Batch tables must be **created in advance by executing DDL**.
   - Quartz provides DDL scripts matching different database vendors (Oracle, MySQL, PostgreSQL, etc.).
2. **Transaction Management**

   - When Quartz uses JDBC JobStore, transaction configuration can be complex.
   - When using Spring Boot, proper `DataSource` and transaction manager configuration is needed.
3. **Lock Cleanup**

   - In cluster environments, monitoring is needed to check if locks are held while schedules aren't actually running, or if triggers are in paused state.
4. **Concurrency Issues**

   - If server times aren't precisely synchronized (NTP), subtle execution timing errors may occur. Be careful.

---

## **6. Real-World Usage Example 💡**

Below is a **configuration file example** (application.yml or application.properties) for setting up Quartz + Spring Batch in a cluster environment:

```
spring:
  quartz:
    job-store-type: jdbc         # Quartz manages schedules through database
    properties:
      org.quartz.jobStore.driverDelegateClass: org.quartz.impl.jdbcjobstore.StdJDBCDelegate
      org.quartz.jobStore.useProperties: false
      org.quartz.jobStore.misfireThreshold: 60000
      org.quartz.jobStore.isClustered: true  # Enable cluster mode
      org.quartz.scheduler.instanceId: AUTO
      org.quartz.scheduler.instanceName: MyClusteredScheduler
```

- When `isClustered: true` is set, even if you start Quartz on multiple instances simultaneously, database locks prevent duplicate execution.

---

## **7. Conclusion 🎯**

Today we explored **distributed scheduling using Quartz** and **Spring Batch's basic table structure**.

- If you need to operate a scheduling system stably in a distributed environment, applying **Quartz's database cluster mode** is very useful.
- If you need to manage Job execution results, you can **easily monitor status and history** using **Spring Batch's metadata tables**.

By using **clustered Quartz scheduling + Spring Batch** together, you can solve **high availability**, **load balancing**, and **convenient batch history management** all at once!

---

### **References and Sources**

- [Quartz Official Documentation](https://www.quartz-scheduler.org/documentation)
- [Spring Batch Official Documentation](https://docs.spring.io/spring-batch/docs/current/reference/html)
- [Spring Boot Reference](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/)

You can find more detailed examples and configuration methods by referring to the above resources.

I hope you build more stable and scalable scheduling systems in cluster environments going forward!
