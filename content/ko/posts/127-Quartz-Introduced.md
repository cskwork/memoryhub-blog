---
title: "Quartz Introduced"
date: 2024-05-27T22:50:08+09:00
slug: "127-Quartz-Introduced"
original_url: "https://memoryhub.tistory.com/127"
tistory_id: 127
draft: false
categories: ["데브 프레임워크"]
tags: ["Spring Batch"]
---

*Quartz is a job scheduling library that can be integrated into a wide range of Java applications to manage and schedule tasks.*

### The Big Picture

Imagine you have a factory where different tasks need to be performed at specific times or intervals, like assembling parts, packaging products, and maintenance checks. To manage this efficiently, you would need a system that can schedule these tasks automatically. Quartz Framework is like that scheduling system, but for Java applications. It allows you to define jobs (tasks) and schedule them to run at specified times or intervals.

### Core Concepts

1. **Scheduler**: The main engine of the Quartz framework that orchestrates the execution of jobs.
2. **Job**: A unit of work that you want to execute.
3. **JobDetail**: Contains the definition and configuration of the job.
4. **Trigger**: Defines when and how often a job should be executed.
5. **JobStore**: Manages the storage of job, trigger, and scheduling data.

### Detailed Walkthrough

1. **Scheduler**:

   - Think of the Scheduler as the manager that coordinates all the tasks in your factory. It starts, stops, and monitors the jobs.
   - Example code to create a scheduler:

     ```
     SchedulerFactory schedulerFactory = new StdSchedulerFactory();
     Scheduler scheduler = schedulerFactory.getScheduler();
     scheduler.start();
     ```
2. **Job**:

   - A Job is a specific task that needs to be done, like a worker performing a task.
   - To define a job, you create a class that implements the `Job` interface.
   - Example code for a simple job:

     ```
     public class MyJob implements Job {
         public void execute(JobExecutionContext context) throws JobExecutionException {
             System.out.println("Job is executing!");
         }
     }
     ```
3. **JobDetail**:

   - JobDetail holds the information about the job, such as its name, group, and the actual job class.
   - Example code to create a JobDetail:

     ```
     JobDetail jobDetail = JobBuilder.newJob(MyJob.class)
                                     .withIdentity("myJob", "group1")
                                     .build();
     ```
4. **Trigger**:

   - Triggers determine when the job should be executed. There are different types of triggers like SimpleTrigger and CronTrigger.
   - Example code to create a simple trigger that fires every 10 seconds:

     ```
     Trigger trigger = TriggerBuilder.newTrigger()
                                     .withIdentity("myTrigger", "group1")
                                     .startNow()
                                     .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                                                                       .withIntervalInSeconds(10)
                                                                       .repeatForever())
                                     .build();
     ```
5. **JobStore**:

   - JobStore is like a database where Quartz keeps the job and trigger configurations. It can be RAM-based or JDBC-based.

### Understanding Through an Example

Let's put it all together with a complete example:

```
import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

public class QuartzExample {
    public static void main(String[] args) throws SchedulerException {
        // Create Scheduler
        SchedulerFactory schedulerFactory = new StdSchedulerFactory();
        Scheduler scheduler = schedulerFactory.getScheduler();

        // Define Job
        JobDetail jobDetail = JobBuilder.newJob(MyJob.class)
                                        .withIdentity("myJob", "group1")
                                        .build();

        // Define Trigger
        Trigger trigger = TriggerBuilder.newTrigger()
                                        .withIdentity("myTrigger", "group1")
                                        .startNow()
                                        .withSchedule(SimpleScheduleBuilder.simpleSchedule()
                                                                          .withIntervalInSeconds(10)
                                                                          .repeatForever())
                                        .build();

        // Schedule the Job
        scheduler.scheduleJob(jobDetail, trigger);

        // Start the Scheduler
        scheduler.start();
    }

    public static class MyJob implements Job {
        public void execute(JobExecutionContext context) throws JobExecutionException {
            System.out.println("Job is executing!");
        }
    }
}
```

### Conclusion and Summary

Quartz Framework is a powerful and flexible job scheduling library for Java applications. It allows you to define jobs and schedule them using various triggers. The key components include the Scheduler, Job, JobDetail, Trigger, and JobStore. By understanding these components and how they interact, you can effectively manage and automate tasks within your application.

### Test Your Understanding

1. What is the role of the `Scheduler` in Quartz?
2. How do you define a job in Quartz?
3. What is the purpose of a `Trigger`?
4. Can you explain the difference between a `JobDetail` and a `Job`?

### Reference

- [Quartz Scheduler Documentation](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/)
