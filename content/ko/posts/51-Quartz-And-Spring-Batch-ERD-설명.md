---
title: "Quartz And Spring Batch ERD 설명"
date: 2024-05-25T14:03:02+09:00
slug: "51-Quartz-And-Spring-Batch-ERD-설명"
original_url: "https://memoryhub.tistory.com/51"
tistory_id: 51
draft: false
---

### ? Quartz를 이용한 분산 처리와 Spring Batch 기본 테이블 ERD 설명 ?

오늘은 **Quartz를 이용한 분산 처리**와 함께, **Quartz와 Spring Batch의 기본 테이블 구조(ERD)**에 대해 알아보겠습니다! 클러스터 환경에서 효율적으로 스케줄링 작업을 처리하고 모니터링하고 싶은 분들께 도움이 되길 바랍니다.

---

## **1. 컴퓨터 클러스터란? ?**

컴퓨터 클러스터(Computer Cluster)는 여러 대의 컴퓨터를 네트워크로 연결하여 **하나의 시스템처럼 동작**하도록 구성한 컴퓨터 집합을 의미합니다.

- ? **분산 처리**: 클러스터는 여러 노드(서버)에서 나누어 작업을 처리할 수 있으므로 대규모 데이터를 빠르게 처리하거나, 부하 분산을 통해 안정적인 서비스를 제공할 수 있습니다.
- ? **고가용성(High Availability)**: 특정 서버에 장애가 생기더라도, 다른 서버가 업무를 대신 수행함으로써 서비스 다운타임을 최소화할 수 있습니다.
- ? **확장성(Scalability)**: 처리할 작업량이 늘어날 때 서버를 추가함으로써 유연하게 성능을 향상시킬 수 있습니다.

---

## **2. Quartz를 이용한 분산 스케줄링 ?**

### 2.1 기본 개념

**Quartz**는 Java로 구현된 오픈소스 스케줄러 라이브러리로, 다양한 **Job**(수행할 로직)과 **Trigger**(실행 타이밍)를 관리해주는 역할을 합니다.  
분산 환경(클러스터)에서 스케줄링을 사용하려면 **Quartz가 공용 DB**를 통해 **작업 점유(선점)와 스케줄 데이터를 공유**하도록 설정할 수 있습니다.

#### 기존 방식(단일 서버 또는 메모리 기반)

- 메모리에 스케줄 정보를 담아두는 방식.
- 여러 서버에서 동일 스케줄 로직을 실행하면 **중복 실행**이나 충돌 문제가 발생할 수 있음.
- 한 서버에 장애가 발생하면 스케줄링 작업이 중단될 수 있음.

#### 클러스터 방식(DB 기반)

1. **스케줄 정보를 DB에 저장**: Job, Trigger, Cron Expression 등 모든 스케줄링 정보를 중앙 DB에 저장.
2. **각 서버는 DB를 참조**: 하나의 서버가 트리거를 먼저 점유하면, 다른 서버들은 그 트리거가 실행 중임을 인지하고 중복 실행을 방지.
3. **장애 내성(HA)**: 특정 서버가 다운되더라도, 다른 서버가 DB를 통해 작업을 이어받을 수 있음.
4. **부하 분산**: 동시에 많은 작업이 등록되어도 여러 서버가 트리거를 나누어 수행할 수 있음.

---

### 2.2 Quartz의 주요 테이블 (ERD 개념 정리)

![](/images/51-Quartz-And-Spring-Batch-ERD-설명/img.png)

Quartz는 **스케줄 정보를 DB에 저장**하기 위해 기본적으로 다음과 같은 테이블들을 사용합니다(접두사 `QRTZ_`로 구분):

1. **QRTZ\_JOB\_DETAILS**

   - **역할**: Job(수행할 로직)의 기본 정보를 저장.
   - **주요 컬럼**:
     - `JOB_NAME`, `JOB_GROUP`: Job 이름과 그룹.
     - `JOB_DATA`: Job 실행 시 필요한 데이터(직렬화된 객체 혹은 파라미터).
     - `JOB_CLASS_NAME`: 실제 Quartz가 실행해야 할 Job 클래스 경로.
2. **QRTZ\_TRIGGERS**

   - **역할**: Job과 연결된 Trigger(실행 타이밍) 정보를 저장.
   - **주요 컬럼**:
     - `TRIGGER_NAME`, `TRIGGER_GROUP`: Trigger 이름과 그룹.
     - `JOB_NAME`, `JOB_GROUP`: 어떤 Job을 실행해야 하는지 연결.
     - 이전/다음 실행 시간, 우선순위, 상태 등을 포함.
3. **QRTZ\_CRON\_TRIGGERS**

   - **역할**: Trigger가 Cron 표현식으로 작동할 경우, 해당 스케줄 정보를 저장.
   - **주요 컬럼**:
     - `CRON_EXPRESSION`: 예) `"0 0/5 * * * ?"` (매 5분 마다)
     - `TIME_ZONE_ID`: 타임존 정보.
4. **QRTZ\_SIMPLE\_TRIGGERS**

   - **역할**: 반복 회수나 간격이 정해진 Simple Trigger 정보를 저장.
   - **주요 컬럼**:
     - `REPEAT_COUNT`, `REPEAT_INTERVAL`: 반복 횟수, 간격.
5. **QRTZ\_CALENDARS**

   - **역할**: 달력을 기반으로 특정 날짜/시간대를 제외하거나 포함하는 캘린더 스케줄 설정을 저장.
6. **QRTZ\_LOCKS, QRTZ\_SCHEDULER\_STATE, QRTZ\_FIRED\_TRIGGERS, QRTZ\_PAUSED\_TRIGGER\_GRPS**

   - **역할**: 클러스터 환경에서 동시성 제어(락) 및 실행 중인 트리거, 일시 중지 상태 등을 관리.
   - 예) `QRTZ_LOCKS`는 트리거를 선점할 때 Lock을 거는 용도로 사용.

---

### 2.3 실제 적용 예시

아래 예시는 **Spring Boot + Spring Batch + Quartz**를 함께 사용하는 대표적인 구성 예시입니다.

1) **Job**(Batch 작업)의 정의

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
            .reader(testReader())       // 실제 데이터 읽기
            .processor(testProcessor()) // 처리 로직
            .writer(testWriter())       // 처리 결과 저장
            .build();
}
```

- `Job`: 여러 `Step`을 묶어서 구성.
- `Step`: Reader -> Processor -> Writer 구조로 실행.

2) **Quartz JobDetail** 정의

```
@Bean
public JobDetail jobDetail() {
    JobDataMap jobDataMap = new JobDataMap();
    jobDataMap.put("jobName", "testJob"); // 실행할 Batch Job의 이름

    return JobBuilder.newJob(CustomQuartzJobBean.class)
            .withIdentity("testJob", null)
            .setJobData(jobDataMap)
            .storeDurably()
            .build();
}
```

- `JobDataMap`: Quartz Job 실행 시 필요한 데이터(여기서는 ‘testJob’ 이름)를 전달.

3) **Quartz Trigger** 등록

```
@Bean
public Trigger jobTrigger() {
    // 예: 매 분 0초에 실행
    CronScheduleBuilder scheduleBuilder = CronScheduleBuilder.cronSchedule("0 * * * * ?");

    return TriggerBuilder
            .newTrigger()
            .forJob(jobDetail().getKey())
            .withIdentity("jobTrigger", null)
            .withSchedule(scheduleBuilder)
            .build();
}
```

- Cron 표현식 `"0 * * * * ?"`은 **매 분 정각(초단위로 0초)에 실행**한다는 의미.

---

## **3. Spring Batch의 기본 테이블 구조 ?**

![](/images/51-Quartz-And-Spring-Batch-ERD-설명/img_1.png)

Spring Batch는 Job과 Step의 실행 이력을 추적하기 위해 자체적인 메타데이터 테이블을 사용합니다:

1. **BATCH\_JOB\_INSTANCE**

   - **역할**: 한 번 실행된 배치 Job은 고유한 `Job Instance`가 생성되며, 이 정보를 기록.
   - **주요 컬럼**: `JOB_INSTANCE_ID`, `JOB_NAME` 등.
2. **BATCH\_JOB\_EXECUTION**

   - **역할**: Job 실행에 대한 시작/종료 시간, 상태, 배치 결과(성공/실패) 등을 기록.
   - **주요 컬럼**: `JOB_EXECUTION_ID`, `START_TIME`, `END_TIME`, `STATUS` 등.
3. **BATCH\_JOB\_EXECUTION\_CONTEXT**, **BATCH\_JOB\_EXECUTION\_PARAMS**

   - **역할**: Job 실행 시 파라미터나 컨텍스트 정보를 저장.
   - **예**: 특정 날짜 범위, 사용자 지정 파라미터 등.
4. **BATCH\_STEP\_EXECUTION**

   - **역할**: Step 단위 실행 정보를 저장. 어떤 Step이 언제 시작/종료되었는지, 몇 개 레코드가 처리되었는지 등을 포함.
   - **주요 컬럼**: `STEP_EXECUTION_ID`, `COMMIT_COUNT`, `READ_COUNT`, `WRITE_COUNT` 등.
5. **BATCH\_STEP\_EXECUTION\_CONTEXT**

   - **역할**: Step 실행 시 사용되는 추가 컨텍스트(상태) 정보를 저장.

---

## **4. 주요 장점 ?**

1. **안정성(고가용성)**

   - 분산된 서버들로 하여금 동일한 스케줄 정보를 공유하게 하여, 특정 서버 다운 시 다른 서버가 이어서 작업을 수행할 수 있습니다.
2. **중복 실행 방지**

   - DB Lock 메커니즘을 통해 **단일 스케줄(Job+Trigger)**가 여러 서버에서 동시에 실행되지 않도록 합니다.
3. **유연한 스케줄 관리**

   - Cron, Simple, Calendar 등 **다양한 Trigger 타입**을 지원.
   - Batch 메타 테이블을 통해 **실행 로그**까지 손쉽게 모니터링 가능.
4. **확장성**

   - 작업량이 많아지면 서버 노드를 추가해 부하를 분산할 수 있습니다.
   - Quartz와 Spring Batch 모두 규모가 커져도 안정적으로 동작하도록 설계됨.

---

## **5. 주의할 점 ⚠️**

1. **DB 테이블 생성 및 설정**

   - Quartz 테이블과 Spring Batch 테이블은 사전에 **DDL**을 실행해서 생성해야 합니다.
   - Quartz는 DB 벤더(Oracle, MySQL, PostgreSQL 등)에 맞는 DDL 스크립트를 제공.
2. **트랜잭션 관리**

   - Quartz가 JDBC JobStore를 쓸 때, 트랜잭션 설정이 복잡할 수 있음.
   - Spring Boot 사용 시에는 적절한 `DataSource`와 트랜잭션 매니저 설정 필요.
3. **Lock 정리**

   - 클러스터 환경에서 스케줄을 잡아두었다가 실제로 돌리지 않는 경우 Lock이 걸려있는지, 트리거가 일시 중지된 상태인지 모니터링이 필요.
4. **동시성 이슈**

   - 각 서버 시간이 정확히 동기화(NTP)되어 있지 않을 경우 미묘한 실행 타이밍 오차가 발생할 수도 있으므로 주의.

---

## **6. 실제 사용 예시 ?**

아래는 Quartz + Spring Batch를 클러스터 환경에서 구성할 때의 **설정 파일**(application.yml 혹은 application.properties) 예시입니다.

```
spring:
  quartz:
    job-store-type: jdbc         # Quartz가 DB를 통해 스케줄 관리
    properties:
      org.quartz.jobStore.driverDelegateClass: org.quartz.impl.jdbcjobstore.StdJDBCDelegate
      org.quartz.jobStore.useProperties: false
      org.quartz.jobStore.misfireThreshold: 60000
      org.quartz.jobStore.isClustered: true  # 클러스터 모드 활성화
      org.quartz.scheduler.instanceId: AUTO
      org.quartz.scheduler.instanceName: MyClusteredScheduler
```

- `isClustered: true`로 설정하면 여러 인스턴스에서 동시에 Quartz를 띄웠을 때도 DB Lock을 통해 중복 실행을 방지합니다.

---

## **7. 마치며 ?**

오늘은 **Quartz를 이용한 분산 스케줄링**과 **Spring Batch의 기본 테이블** 구조에 대해 살펴보았습니다.

- 분산 환경에서 스케줄링 시스템을 안정적으로 운영해야 한다면, Quartz에 **DB 클러스터 모드**를 적용하는 방법이 매우 유용합니다.
- Job 실행 결과를 관리해야 한다면, **Spring Batch**의 메타테이블을 이용해 **상태 및 이력**을 손쉽게 모니터링할 수 있습니다.

**클러스터링된 Quartz 스케줄링 + Spring Batch**를 함께 사용하면, **고가용성**과 **부하 분산**, 그리고 **편리한 배치 이력 관리**를 한 번에 해결할 수 있습니다!

---

### **참고 자료 및 출처**

- [Quartz 공식 문서](https://www.quartz-scheduler.org/documentation)
- [Spring Batch 공식 문서](https://docs.spring.io/spring-batch/docs/current/reference/html)
- [Spring Boot Reference](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/)

위 자료들을 참고하면 더욱 상세한 예제와 설정 방법을 확인하실 수 있습니다.  
앞으로 클러스터 환경에서 더 안정적이고 확장성 있는 스케줄링 시스템을 구성해보시길 바랍니다!
