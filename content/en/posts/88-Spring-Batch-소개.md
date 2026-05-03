---
title: "Introduction to Spring Batch"
date: 2024-05-26T10:29:34+09:00
slug: "88-Spring-Batch-소개"
original_url: "https://memoryhub.tistory.com/88"
tistory_id: 88
draft: false
categories: ["Dev Framework"]
tags: ["Spring Batch"]
---

*Spring Batch is a powerful framework for batch processing, processing tasks in bulk rather than executing individual operations one at a time. This is like an efficient assembly line in a factory that processes work in large quantities.*

### The Big Picture

Imagine processing items in a factory. Instead of processing one item at a time, the factory processes multiple items in groups—batches. This approach is much faster and more efficient when handling large quantities of work. Similarly, Spring Batch is a framework that helps process large amounts of data in batches. Since Spring Batch is part of the Spring Framework, you can leverage all of Spring's features such as dependency injection and transaction management.

### Core Concepts

- **Job**: A high-level abstraction representing the entire batch process. It consists of one or more steps.
- **Step**: A single phase of a Job, representing an individual part of the batch process. Each step typically includes reading, processing, and writing data.
- **ItemReader**: Responsible for reading data from a source (e.g., database, file).
- **ItemProcessor**: Processes the data read by ItemReader. This can include data transformation, calculations, and more.
- **ItemWriter**: Writes processed data to a destination (e.g., database, file).

### Detailed Explanation

- **Job**: A Job is like the blueprint of a batch process. It defines the entire workflow and consists of multiple steps. For example, a Job that processes orders might include steps that read orders from a database, process each order, and then write results back to the database.
- **Step**: Each step of a Job is a smaller, more manageable part of the entire batch process. Steps are typically defined as either tasklet (simple single-operation steps) or chunk-oriented processing. Spring Batch excels at chunk-oriented processing, which divides data into chunks and processes each chunk in a loop.
- **Chunk-Oriented Processing**: This involves dividing data into chunks and processing each chunk iteratively. For example, if you have a million records, you can process them 1000 at a time. This makes the process more efficient and easier to manage.

### ItemReader, ItemProcessor, ItemWriter:

- **ItemReader**: Like the input conveyor belt of a factory, it fetches raw materials (data) from external sources (files, databases, web services, etc.).
- **ItemProcessor**: Like a factory workbench, it assembles or modifies raw materials. It processes each item to prepare it for the next step.
- **ItemWriter**: An output conveyor belt that sends the final product (processed data) to its destination. It writes to a database or file.

### Understanding Through Example

Let's look at an example that processes customer orders from a CSV file and updates order status in a database:

- **ItemReader**: Reads orders from a CSV file.
- **ItemProcessor**: Validates and processes each order (e.g., calculates discounts, updates order status).
- **ItemWriter**: Writes updated order information to the database.

```java
@Configuration
@EnableBatchProcessing
public class BatchConfiguration {

    @Bean
    public FlatFileItemReader<Order> reader() {
        return new FlatFileItemReaderBuilder<Order>()
            .name("orderItemReader")
            .resource(new ClassPathResource("orders.csv"))
            .delimited()
            .names(new String[]{"orderId", "product", "quantity", "price"})
            .fieldSetMapper(new BeanWrapperFieldSetMapper<Order>() {{
                setTargetType(Order.class);
            }})
            .build();
    }

    @Bean
    public OrderItemProcessor processor() {
        return new OrderItemProcessor();
    }

    @Bean
    public JdbcBatchItemWriter<Order> writer(DataSource dataSource) {
        return new JdbcBatchItemWriterBuilder<Order>()
            .itemSqlParameterSourceProvider(new BeanPropertyItemSqlParameterSourceProvider<>())
            .sql("UPDATE orders SET status = :status WHERE order_id = :orderId")
            .dataSource(dataSource)
            .build();
    }

    @Bean
    public Job importOrderJob(JobBuilderFactory jobBuilderFactory, StepBuilderFactory stepBuilderFactory) {
        return jobBuilderFactory.get("importOrderJob")
            .incrementer(new RunIdIncrementer())
            .flow(step1(stepBuilderFactory))
            .end()
            .build();
    }

    @Bean
    public Step step1(StepBuilderFactory stepBuilderFactory) {
        return stepBuilderFactory.get("step1")
            .<Order, Order>chunk(10)
            .reader(reader())
            .processor(processor())
            .writer(writer(null))
            .build();
    }
}
```

### Conclusion and Summary

Spring Batch enables efficient processing of large amounts of data by dividing work into manageable chunks. It uses concepts such as Job, Step, and chunk-oriented processing, and ensures scalability and reliability through components like ItemReader, ItemProcessor, and ItemWriter.

### Comprehension Check

1. What are the main components of a Spring Batch Job?
2. How does chunk-oriented processing work in Spring Batch?
3. Can you explain scenarios where using Spring Batch is advantageous?

Reference:

Spring Batch Official Documentation
