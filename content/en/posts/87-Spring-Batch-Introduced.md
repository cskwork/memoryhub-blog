---
title: "Spring Batch Introduced"
date: 2024-05-26T10:23:21+09:00
slug: "87-Spring-Batch-Introduced"
original_url: "https://memoryhub.tistory.com/87"
tistory_id: 87
draft: false
categories: ["Dev Framework"]
tags: ["Spring Batch"]
---

*Spring Batch is a robust framework for batch processing, which involves executing a series of jobs in a batch rather than one-by-one. Think of it as a highly efficient assembly line in a factory where tasks are processed in bulk.*

### **The Big Picture**

Imagine you have a factory that processes items. Instead of working on one item at a time, the factory processes many items in groups, or batches. This approach is much faster and more efficient for large volumes of work. Similarly, Spring Batch is a framework that helps you process large amounts of data in batches. It is part of the Spring Framework, which means it leverages all the features of Spring, such as dependency injection and transaction management.

### **Core Concepts**

1. **Job**: The high-level abstraction representing the entire batch process. It consists of one or more steps.
2. **Step**: A phase in a job, representing a discrete part of the batch process. Each step typically involves reading, processing, and writing data.
3. **ItemReader**: Responsible for reading data from a source (e.g., a database, a file).
4. **ItemProcessor**: Processes the data read by the ItemReader. This can involve transforming data, performing calculations, etc.
5. **ItemWriter**: Writes the processed data to a destination (e.g., a database, a file).

### **Detailed Walkthrough**

1. **Job**: Think of a job as a blueprint for the batch process. It defines the overall workflow and is made up of multiple steps. For example, processing orders could be a job that includes steps for reading orders from a database, processing each order, and then writing the results back to the database.
2. **Step**: Each step in a job is a smaller, manageable part of the overall batch process. Steps are typically defined by a tasklet (simple single-task step) or chunk-oriented processing. Chunk-oriented processing is where Spring Batch excels; it breaks down the data processing into chunks.
3. **Chunk-Oriented Processing**: This involves dividing the data into chunks and processing each chunk in a loop. For instance, if you have a million records, you can process them in chunks of 1000 records. This makes the process more efficient and easier to manage.
4. **ItemReader, ItemProcessor, ItemWriter**:
   - **ItemReader**: Think of this as the input conveyor belt in the factory. It brings in raw materials (data) from an external source like a file, database, or web service.
   - **ItemProcessor**: This is like the workstations on the factory floor where the raw materials are assembled or modified. It processes each item and prepares it for the next stage.
   - **ItemWriter**: Finally, this is the output conveyor belt that sends the finished product (processed data) to its destination, like writing it to a database or a file.

### **Understanding Through an Example**

Let's take an example of processing customer orders from a CSV file and updating the order status in a database:

1. **ItemReader**: Reads orders from a CSV file.
2. **ItemProcessor**: Validates and processes each order (e.g., calculates discounts, updates order status).
3. **ItemWriter**: Writes the updated order information back to a database.

Here's a simplified code example:

```
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

### **Conclusion and Summary**

Spring Batch allows you to efficiently process large volumes of data by breaking down the process into manageable chunks. It does so using jobs, steps, and chunk-oriented processing with components like ItemReader, ItemProcessor, and ItemWriter. This approach ensures scalability and reliability in batch processing applications.

### **Test Your Understanding**

1. What are the primary components of a Spring Batch job?
2. How does chunk-oriented processing work in Spring Batch?
3. Can you describe a scenario where using Spring Batch would be beneficial?

For further reading, check out the [official Spring Batch documentation](https://docs.spring.io/spring-batch/docs/current/reference/html/index.html).
