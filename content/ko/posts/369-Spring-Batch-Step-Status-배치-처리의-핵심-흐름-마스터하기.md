---
title: "Spring Batch Step & Status - 배치 처리의 핵심 흐름 마스터하기  ?"
date: 2024-11-07T09:32:11+09:00
slug: "369-Spring-Batch-Step-Status-배치-처리의-핵심-흐름-마스터하기"
original_url: "https://memoryhub.tistory.com/369"
tistory_id: 369
draft: false
---

대규모 데이터 처리와 자동화된 작업 실행이 필요한 엔터프라이즈 환경에서 Spring Batch는 필수적인 프레임워크입니다. 그중에서도 Step과 Status는 배치 작업의 흐름을 제어하는 핵심 요소입니다. 이것을 제대로 이해하지 못한다면 복잡한 배치 애플리케이션을 구축하기 어렵습니다.

여러분이 일상에서 볼 수 있는 공장의 조립 라인을 생각해보세요.

- 각 라인의 작업 스테이션이 바로 Spring Batch의 'Step'입니다.
- 작업 스테이션마다 부품을 받아(read), 가공하고(process), 다음 스테이션으로 넘기는(write) 과정이 있죠.
- 각 스테이션의 신호등(초록색: 완료, 빨간색: 실패, 노란색: 대기 중)은 Step의 'Status'와 같습니다.

## 왜 필요한가?

Spring Batch의 Step과 Status가 해결하는 문제들은 다음과 같습니다:

1. **복잡한 처리 분리**: 대규모 배치 작업을 작고 관리하기 쉬운 단위로 나눠 처리할 수 있습니다.
2. **오류 복구 메커니즘**: 특정 Step에서 오류가 발생해도 전체 작업이 실패하지 않고, 재시작 시 실패한 지점부터 계속할 수 있습니다.
3. **트랜잭션 관리**: 각 Step은 자체 트랜잭션 경계를 가지므로 데이터 무결성이 보장됩니다.
4. **진행 상황 추적**: Status를 통해 각 Step과 전체 Job의 실행 상태를 정확히 파악할 수 있습니다.
5. **조건부 실행 흐름**: Status 값에 따라 다음에 실행할 Step을 동적으로 결정할 수 있습니다.

## 기본 원리

Spring Batch의 Step과 Status의 핵심 원리를 알아볼까요?

### Step의 종류

Spring Batch에서는 두 가지 주요 Step 유형이 있습니다:

1. **Chunk-oriented Step**: 데이터를 청크(chunk) 단위로 처리하는 방식

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

2. **Tasklet Step**: 단일 작업 단위로 처리하는 방식

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

### BatchStatus와 ExitStatus

**BatchStatus**는 Step이나 Job의 실행 상태를 나타내는 열거형(Enum)입니다:

```
public enum BatchStatus {
    COMPLETED,   // 성공적으로 완료됨
    STARTING,    // 시작 중
    STARTED,     // 실행 중
    STOPPING,    // 중지 과정 중
    STOPPED,     // 중지됨
    FAILED,      // 실패함
    ABANDONED,   // 포기됨(재시작 시 건너뜀)
    UNKNOWN      // 상태 알 수 없음
}
```

**ExitStatus**는 Step 실행 완료 후의 상태를 나타내는 객체로, 기본적으로 BatchStatus와 동일한 값을 가지지만 사용자가 커스터마이징할 수 있습니다:

```
@Bean
public Step customExitStatusStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
    return new StepBuilder("customExitStatusStep", jobRepository)
        .tasklet((contribution, chunkContext) -> {
            // 비즈니스 로직 실행

            // 커스텀 ExitStatus 설정
            contribution.setExitStatus(new ExitStatus("COMPLETED_WITH_WARNINGS"));

            return RepeatStatus.FINISHED;
        }, transactionManager)
        .build();
}
```

## 실제 예제

금융 기관의 일일 결산 배치 작업을 예로 들어보겠습니다:

1. **데이터 추출 Step**: 당일 거래 데이터를 DB에서 추출 (Chunk-oriented)
2. **데이터 변환 Step**: 추출된 데이터를 회계 시스템 포맷으로 변환 (Chunk-oriented)
3. **보고서 생성 Step**: 일일 거래 요약 보고서 생성 (Chunk-oriented)
4. **이메일 발송 Step**: 생성된 보고서를 이해관계자에게 이메일로 발송 (Tasklet)
5. **임시 파일 정리 Step**: 처리 과정에서 생성된 임시 파일 삭제 (Tasklet)

### 기본 사용법

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

    // 다른 Step 빈 정의...
}
```

다음은 표로 정리한 BatchStatus 값과 의미입니다:

| 상태 | 설명 | 일반적인 상황 |
| --- | --- | --- |
| COMPLETED | 스텝이 성공적으로 완료됨 | 정상 실행 완료 |
| STARTING | 스텝이 시작 중이나 아직 처리를 시작하지 않음 | Job 실행 초기화 |
| STARTED | 스텝이 실행을 시작함 | 데이터 처리 중 |
| STOPPING | 스텝이 중지 과정 중임 | 사용자 요청이나 시스템에 의한 중지 |
| STOPPED | 스텝이 중지됨 (재시작 가능) | 중지 완료 상태 |
| FAILED | 스텝이 오류로 실패함 | 예외 발생, 비즈니스 룰 위반 등 |
| ABANDONED | 스텝이 포기됨 (재시작 시 건너뜀) | 재시작 불가능한 오류 |
| UNKNOWN | 스텝 상태를 확인할 수 없음 | 시스템 장애, 비정상 종료 등 |

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **BatchStatus와 ExitStatus의 차이 이해하기**

   - BatchStatus는 프레임워크가 내부적으로 사용하는 열거형
   - ExitStatus는 흐름 제어에 사용되는 값으로 커스터마이징 가능
   - 흐름 제어 시 `on()` 메서드는 ExitStatus를 참조함
2. **재시작 시나리오 고려하기**

   - 기본적으로 COMPLETED 상태의 Step은 재실행되지 않음
   - 필요한 경우 `allowStartIfComplete(true)` 설정 필요

```
    @Bean
    public Step restartableStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
        return new StepBuilder("restartableStep", jobRepository)
            .tasklet(myTasklet(), transactionManager)
            .allowStartIfComplete(true)
            .build();
    }
```

3. **적절한 청크 크기 설정하기**

   - 너무 작으면 트랜잭션 오버헤드가 커짐
   - 너무 크면 메모리 사용량 증가, 롤백 범위 확대
   - 일반적으로 10-100 사이 값이 적절하며 데이터 특성에 맞게 조정

? **꿀팁**

- **Step 실행 리스너 활용하기**

```
    public class MyStepExecutionListener implements StepExecutionListener {
        @Override
        public void beforeStep(StepExecution stepExecution) {
            // Step 실행 전 로직
        }

        @Override
        public ExitStatus afterStep(StepExecution stepExecution) {
            // Step 실행 후 로직
            return stepExecution.getExitStatus();
        }
    }
```

- **조건부 흐름 제어하기**

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

- **오류 처리 전략 구현하기**

  ```
    @Bean
    public Step robustStep(JobRepository jobRepository, PlatformTransactionManager transactionManager) {
        return new StepBuilder("robustStep", jobRepository)
            .<InputData, OutputData>chunk(10, transactionManager)
            .reader(itemReader())
            .processor(itemProcessor())
            .writer(itemWriter())
            .faultTolerant()
            .skipLimit(3)  // 최대 3개까지 건너뛰기
            .skip(DataFormatException.class)  // 이 예외는 건너뛰기
            .noSkip(FileNotFoundException.class)  // 이 예외는 건너뛰지 않음
            .retryLimit(3)  // 최대 3번 재시도
            .retry(TransientDataAccessException.class)  // 일시적 DB 예외는 재시도
            .build();
    }
  ```

## 마치며

지금까지 Spring Batch의 Step과 Status에 대해 알아보았습니다. 복잡해 보일 수 있지만, 적절히 이해하고 활용하면 견고하고 유연한 배치 애플리케이션을 구축할 수 있습니다. Step은 배치 작업의 실행 단위이며, Status는 그 흐름을 제어하는 열쇠입니다.

Spring Batch의 강력한 기능을 활용하여 대용량 데이터 처리, 자동화된 워크플로우, 복잡한 비즈니스 로직 처리를 효율적으로 구현해보세요. 초기 설정과 개념 이해에 시간이 들더라도, 장기적으로는 유지보수와 확장성 측면에서 큰 이점을 얻을 수 있습니다.

혹시 궁금한 점이 있으시거나, 더 알고 싶은 내용이 있으시면 댓글로 남겨주세요.

## 참고 자료 ?

- [Spring Batch 공식 문서 - Step 설정](https://docs.spring.io/spring-batch/reference/step.html)
- [Spring Batch 공식 문서 - 흐름 제어](https://docs.spring.io/spring-batch/reference/step/controlling-flow.html)
- [Baeldung - Spring Batch 조건부 흐름](https://www.baeldung.com/spring-batch-conditional-flow)
- [Baeldung - Tasklet vs Chunks](https://www.baeldung.com/spring-batch-tasklet-chunk)
- [Spring Batch - 오류 처리 방법](https://www.geeksforgeeks.org/spring-batch-configuring-retry-and-skip-logic/)

---

#SpringBatch #배치처리 #JavaFramework #SpringBoot #데이터처리
