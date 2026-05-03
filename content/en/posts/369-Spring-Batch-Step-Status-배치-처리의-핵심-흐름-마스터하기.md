---
title: "Spring Batch Step & Status - Mastering the Core Flow of Batch Processing"
date: 2024-11-07T09:32:11+09:00
slug: "369-Spring-Batch-Step-Status-배치-처리의-핵심-흐름-마스터하기"
original_url: "https://memoryhub.tistory.com/369"
tistory_id: 369
draft: false
---

In enterprise environments requiring large-scale data processing and automated task execution, Spring Batch is an essential framework. Among its components, Step and Status are core elements that control the flow of batch operations. Without a proper understanding of these concepts, it's difficult to build complex batch applications.

Think of an assembly line in a factory that you see every day:

- Each work station on the line is like a 'Step' in Spring Batch.
- At each station, there's a process of receiving parts (read), processing them, and passing them to the next station (write).
- The traffic light at each station (green: complete, red: failure, yellow: waiting) is similar to the Step's 'Status'.

## Why Is It Necessary?

The problems that Spring Batch's Step and Status solve are as follows:

1. **Complex Process Separation**: You can break down large batch jobs into smaller, manageable units.
2. **Error Recovery Mechanism**: If an error occurs in a specific Step, the entire job doesn't fail. Upon restart, it can continue from the point of failure.
3. **Transaction Management**: Each Step has its own transaction boundary, ensuring data integrity.
4. **Progress Tracking**: Through Status, you can precisely understand the execution state of each Step and the entire Job.
5. **Conditional Execution Flow**: You can dynamically determine which Step to execute next based on the Status value.

## Basic Principles

Let's explore the core principles of Step and Status in Spring Batch:

### Types of Steps

Spring Batch has two main Step types:

1. **Chunk-oriented Step**: A method of processing data in chunk units

```
@Bean
public Step chunkStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
    return new StepBuilder("chunkStep", jobRepository)
        .<Customer, CustomerDTO>chunk(10, transactionManager)
        .reader(customerItemReader())
        .processor(customerItemProcessor())
        .writer(customerItemWriter())
        .build();
}
```

2. **Tasklet Step**: A method of processing in single task units

```
@Bean
public Step taskletStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
    return new StepBuilder("taskletStep", jobRepository)
        .tasklet(new FileCleanupTasklet(), transactionManager)
        .build();
}

public class FileCleanupTasklet implements Tasklet {
    @Override
    public RepeatStatus execute(StepContribution contribution, ChunkContext chunkContext) throws Exception {
        File directory = new File("/temp/processing");
        File[] files = directory.listFiles();

        for (File file : files) {
            file.delete();
        }

        return RepeatStatus.FINISHED;
    }
}
```

### BatchStatus and ExitStatus

**BatchStatus** is an enumeration representing the execution state of a Step or Job:

```
public enum BatchStatus {
    COMPLETED,   // Successfully completed
    STARTING,    // Starting
    STARTED,     // Running
    STOPPING,    // Stopping
    STOPPED,     // Stopped
    FAILED,      // Failed
    ABANDONED,   // Abandoned (skipped on restart)
    UNKNOWN      // Unknown state
}
```

**ExitStatus** is an object representing the state after Step execution. By default, it has the same value as BatchStatus, but users can customize it:

```
@Bean
public Step customExitStatusStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
    return new StepBuilder("customExitStatusStep", jobRepository)
        .tasklet((contribution, chunkContext) -> {
            // Execute business logic

            // Set custom ExitStatus
            contribution.setExitStatus(new ExitStatus("COMPLETED_WITH_WARNINGS"));

            return RepeatStatus.FINISHED;
        }, transactionManager)
        .build();
}
```

## Practical Example

Let's look at an example of a daily settlement batch job for a financial institution:

1. **Data Extraction Step**: Extract transaction data from DB for the day (Chunk-oriented)
2. **Data Transformation Step**: Convert extracted data into accounting system format (Chunk-oriented)
3. **Report Generation Step**: Generate daily transaction summary report (Chunk-oriented)
4. **Email Sending Step**: Send the generated report to stakeholders via email (Tasklet)
5. **Temporary File Cleanup Step**: Delete temporary files created during processing (Tasklet)

### Basic Usage

```
@Configuration
@EnableBatchProcessing
public class DailySettlementJobConfig {

    @Bean
    public Job dailySettlementJob(JobRepository jobRepository) {
        return new JobBuilder("dailySettlementJob", jobRepository)
            .start(dataExtractionStep())
            .next(dataTransformationStep())
            .next(reportGenerationStep())
            .next(emailSendingStep())
            .next(tempFileCleanupStep())
            .build();
    }

    @Bean
    public Step dataExtractionStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
        return new StepBuilder("dataExtractionStep", jobRepository)
            .<Transaction, Transaction>chunk(100, transactionManager)
            .reader(transactionReader())
            .writer(transactionWriter())
            .build();
    }

    // Other Step bean definitions...
}
```

Here's a table summarizing BatchStatus values and their meanings:

| Status | Description | Typical Situation |
| --- | --- | --- |
| COMPLETED | Step completed successfully | Normal execution completion |
| STARTING | Step is starting or hasn't begun processing yet | Job execution initialization |
| STARTED | Step has started executing | Data processing in progress |
| STOPPING | Step is in the process of stopping | User request or system-initiated stop |
| STOPPED | Step has stopped (restartable) | Stop completed state |
| FAILED | Step failed with an error | Exception thrown, business rule violation, etc. |
| ABANDONED | Step is abandoned (skipped on restart) | Unrecoverable error |
| UNKNOWN | Step state cannot be determined | System failure, abnormal termination, etc. |

## Important Notes and Tips

Warning: **Pay Attention to These!**

1. **Understanding the Difference Between BatchStatus and ExitStatus**

   - BatchStatus is an enumeration used internally by the framework
   - ExitStatus is a value used for flow control and can be customized
   - The `on()` method for flow control references ExitStatus
2. **Considering Restart Scenarios**

   - By default, Steps with COMPLETED status are not re-executed
   - If needed, configure `allowStartIfComplete(true)`

```
    @Bean
    public Step restartableStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
        return new StepBuilder("restartableStep", jobRepository)
            .tasklet(myTasklet(), transactionManager)
            .allowStartIfComplete(true)
            .build();
    }
```

3. **Setting Appropriate Chunk Size**

   - Too small: Increases transaction overhead
   - Too large: Increases memory usage, expands rollback range
   - Generally, values between 10-100 are appropriate, adjusted based on data characteristics

Tip: **Pro Tips**

- **Utilizing Step Execution Listeners**

```
    public class MyStepExecutionListener implements StepExecutionListener {
        @Override
        public void beforeStep(StepExecution stepExecution) {
            // Logic before Step execution
        }

        @Override
        public ExitStatus afterStep(StepExecution stepExecution) {
            // Logic after Step execution
            return stepExecution.getExitStatus();
        }
    }
```

- **Conditional Flow Control**

```
    @Bean
    public Job conditionalFlowJob(JobRepository jobRepository) {
        return new JobBuilder("conditionalFlowJob", jobRepository)
            .start(firstStep())
            .on("COMPLETED").to(successStep())
            .from(firstStep()).on("FAILED").to(recoveryStep())
            .from(firstStep()).on("*").to(defaultStep())
            .end()
            .build();
    }
```

- **Implementing Error Handling Strategy**

  ```
    @Bean
    public Step robustStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
        return new StepBuilder("robustStep", jobRepository)
            .<InputData, OutputData>chunk(10, transactionManager)
            .reader(itemReader())
            .processor(itemProcessor())
            .writer(itemWriter())
            .faultTolerant()
            .skipLimit(3)  // Skip up to 3 items
            .skip(DataFormatException.class)  // Skip this exception
            .noSkip(FileNotFoundException.class)  // Don't skip this exception
            .retryLimit(3)  // Retry up to 3 times
            .retry(TransientDataAccessException.class)  // Retry on transient DB exceptions
            .build();
    }
  ```

## Conclusion

We've explored Spring Batch's Step and Status in detail. While it may seem complex, when properly understood and applied, it enables you to build robust and flexible batch applications. Step is the execution unit of a batch job, while Status is the key to controlling its flow.

Leverage the powerful features of Spring Batch to efficiently implement large-scale data processing, automated workflows, and complex business logic processing. While the initial setup and concept understanding takes time, you'll gain significant advantages in maintainability and scalability in the long term.

If you have any questions or want to know more, please leave a comment.

## Reference Materials

- [Spring Batch Official Documentation - Step Configuration](https://docs.spring.io/spring-batch/reference/step.html)
- [Spring Batch Official Documentation - Flow Control](https://docs.spring.io/spring-batch/reference/step/controlling-flow.html)
- [Baeldung - Spring Batch Conditional Flow](https://www.baeldung.com/spring-batch-conditional-flow)
- [Baeldung - Tasklet vs Chunks](https://www.baeldung.com/spring-batch-tasklet-chunk)
- [Spring Batch - Error Handling Methods](https://www.geeksforgeeks.org/spring-batch-configuring-retry-and-skip-logic/)

---

#SpringBatch #BatchProcessing #JavaFramework #SpringBoot #DataProcessing
