---
title: "Spring Batch 소개"
date: 2024-05-26T10:29:34+09:00
slug: "88-Spring-Batch-소개"
original_url: "https://memoryhub.tistory.com/88"
tistory_id: 88
draft: false
categories: ["데브 프레임워크"]
tags: ["Spring Batch"]
---

*Spring Batch는 일괄 처리(batch processing)를 위한 강력한 프레임워크로, 개별 작업을 하나씩 실행하는 대신 일괄로 작업을 수행합니다. 이는 마치 공장에서 작업을 대량으로 처리하는 효율적인 조립 라인과 같습니다.*

### 전체적인 그림

공장에서 아이템을 처리하는 것을 상상해보세요. 하나의 아이템을 한 번에 처리하는 대신, 공장은 여러 아이템을 그룹, 즉 배치로 처리합니다. 이러한 접근 방식은 대량의 작업을 처리할 때 훨씬 빠르고 효율적입니다. 이와 유사하게, Spring Batch는 대량의 데이터를 배치로 처리하는 데 도움을 주는 프레임워크입니다. Spring Batch는 Spring Framework의 일부이므로, 의존성 주입 및 트랜잭션 관리와 같은 Spring의 모든 기능을 활용할 수 있습니다.

### 핵심 개념

- **Job**: 전체 배치 프로세스를 나타내는 상위 수준의 추상화입니다. 하나 이상의 단계로 구성됩니다.
- **Step**: Job의 한 단계로, 배치 프로세스의 개별 부분을 나타냅니다. 각 단계는 일반적으로 데이터를 읽고, 처리하고, 쓰는 과정을 포함합니다.
- **ItemReader**: 소스(예: 데이터베이스, 파일)에서 데이터를 읽는 역할을 합니다.
- **ItemProcessor**: ItemReader가 읽은 데이터를 처리합니다. 이는 데이터 변환, 계산 등을 포함할 수 있습니다.
- **ItemWriter**: 처리된 데이터를 목적지(예: 데이터베이스, 파일)에 씁니다.

### 상세한 설명

- **Job**: Job은 배치 프로세스의 청사진과 같습니다. 전체 워크플로우를 정의하며 여러 단계로 구성됩니다. 예를 들어, 주문을 처리하는 Job은 데이터베이스에서 주문을 읽고, 각 주문을 처리한 다음 결과를 데이터베이스에 다시 쓰는 단계를 포함할 수 있습니다.
- **Step**: Job의 각 단계는 전체 배치 프로세스의 더 작고 관리 가능한 부분입니다. 단계는 일반적으로 tasklet(단순한 단일 작업 단계) 또는 chunk 지향 처리로 정의됩니다. Spring Batch는 chunk 지향 처리에서 뛰어납니다. 이는 데이터를 청크로 나누어 각 청크를 루프로 처리하는 방식입니다.
- **Chunk 지향 처리**: 이는 데이터를 청크로 나누고 각 청크를 반복하여 처리하는 것을 포함합니다. 예를 들어, 백만 개의 레코드가 있으면 이를 1000개씩 청크로 처리할 수 있습니다. 이는 프로세스를 더 효율적이고 관리하기 쉽게 만듭니다.

### ItemReader, ItemProcessor, ItemWriter:

- **ItemReader**: 공장의 입력 컨베이어 벨트와 같습니다. 외부 소스(파일, 데이터베이스, 웹 서비스 등)에서 원자재(데이터)를 가져옵니다.
- **ItemProcessor**: 공장 작업대와 같아서 원자재를 조립하거나 수정합니다. 각 아이템을 처리하여 다음 단계로 준비합니다.
- **ItemWriter**: 최종 제품(처리된 데이터)을 목적지로 보내는 출력 컨베이어 벨트입니다. 데이터베이스나 파일에 기록합니다.

### 예제를 통한 이해

CSV 파일에서 고객 주문을 처리하고 데이터베이스에서 주문 상태를 업데이트하는 예제를 살펴보겠습니다:

- **ItemReader**: CSV 파일에서 주문을 읽습니다.
- **ItemProcessor**: 각 주문을 검증하고 처리합니다(예: 할인 계산, 주문 상태 업데이트).
- **ItemWriter**: 업데이트된 주문 정보를 데이터베이스에 씁니다.

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

### 결론 및 요약

Spring Batch는 작업을 관리 가능한 청크로 나누어 대량의 데이터를 효율적으로 처리할 수 있도록 합니다. 이는 Job, Step, Chunk 지향 처리와 같은 개념을 사용하며, ItemReader, ItemProcessor, ItemWriter와 같은 구성 요소를 통해 확장성과 신뢰성을 보장합니다.

### 이해 점검

1. Spring Batch Job의 주요 구성 요소는 무엇인가요?
2. Spring Batch에서 chunk 지향 처리는 어떻게 작동하나요?
3. Spring Batch를 사용하는 것이 유리한 시나리오를 설명할 수 있나요?

참고:

Spring Batch 공식 문서
