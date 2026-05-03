---
title: "Spring 스케줄링 ⏰"
date: 2024-11-07T09:29:58+09:00
slug: "367-Spring-스케줄링"
original_url: "https://memoryhub.tistory.com/367"
tistory_id: 367
draft: false
---

안녕하세요! 오늘은 Spring에서 반복 작업을 자동화하는 Spring 스케줄링 대해 알아보겠습니다.

## Spring Task가 뭔가요? ?

매일 아침 알람을 맞춰놓는 것처럼:

- 특정 시간에 자동으로 실행되는 작업
- 주기적으로 반복되는 작업
- 비동기로 처리해야 하는 작업

Spring Task는 이런 자동화된 작업을 쉽게 구현할 수 있게 해주는 프레임워크입니다!

## 핵심 기능 ?

### 1. @Scheduled 애노테이션

```
@Component
public class ScheduledTasks {

    // 매일 자정에 실행
    @Scheduled(cron = "0 0 0 * * ?")
    public void dailyTask() {
        System.out.println("매일 자정에 실행되는 작업");
    }

    // 5초마다 실행
    @Scheduled(fixedRate = 5000)
    public void everyFiveSeconds() {
        System.out.println("5초마다 실행되는 작업");
    }

    // 이전 작업 완료 후 3초 후에 실행
    @Scheduled(fixedDelay = 3000)
    public void afterPreviousTask() {
        System.out.println("이전 작업 완료 3초 후 실행");
    }
}
```

### 2. 비동기 처리 (@Async)

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
        // 비동기로 처리될 작업
        return new AsyncResult<>("작업 완료!");
    }
}
```

## 스케줄링 표현식 ?

### 1. Cron 표현식

```
* * * * * *
│ │ │ │ │ │
│ │ │ │ │ └─ 요일 (0-7) (0,7=일요일, 1=월요일, ...)
│ │ │ │ └─── 월 (1-12)
│ │ │ └───── 일 (1-31)
│ │ └─────── 시 (0-23)
│ └───────── 분 (0-59)
└─────────── 초 (0-59)
```

예시:

```
// 매일 오전 10시 30분
@Scheduled(cron = "0 30 10 * * ?")

// 매주 월요일 오전 9시
@Scheduled(cron = "0 0 9 ? * MON")

// 매월 1일 자정
@Scheduled(cron = "0 0 0 1 * ?")
```

## 실전 활용 예시 ?

### 1. 일일 리포트 생성

```
@Component
@Slf4j
public class DailyReportScheduler {

    @Scheduled(cron = "0 0 1 * * ?") // 매일 새벽 1시
    public void generateDailyReport() {
        log.info("일일 리포트 생성 시작");
        // 리포트 생성 로직
        log.info("일일 리포트 생성 완료");
    }
}
```

### 2. 캐시 갱신

```
@Component
public class CacheRefreshScheduler {

    @Scheduled(fixedRate = 600000) // 10분마다
    public void refreshCache() {
        // 캐시 갱신 로직
    }
}
```

### 3. 비동기 이메일 발송

```
@Service
public class EmailService {

    @Async
    public Future<Boolean> sendBulkEmail(List<String> recipients) {
        // 대량 이메일 발송 로직
        return new AsyncResult<>(true);
    }
}
```

## 장점 ?

1. **간단한 설정**
   - 애노테이션 기반 설정
   - 직관적인 문법
   - Spring Boot 자동 설정
2. **유연성**
   - 다양한 스케줄링 옵션
   - 비동기 처리 지원
   - 쉬운 커스터마이징
3. **모니터링 및 관리**
   - 스케줄링 상태 확인
   - 에러 처리
   - 로깅 지원

## 주의사항 ⚠️

1. **리소스 관리**
   - 적절한 쓰레드 풀 크기 설정
   - 메모리 사용량 모니터링
   - 타임아웃 설정
2. **에러 처리**
3. `@Scheduled(fixedRate = 5000)
   public void scheduledTask() {
   try {
   // 작업 로직
   } catch (Exception e) {
   log.error("스케줄된 작업 실행 중 에러 발생", e);
   }
   }`
4. **클러스터 환경**
   - 중복 실행 방지
   - 분산 환경 고려
   - 락(Lock) 메커니즘 활용

## 설정 예시 ⚙️

### 기본 설정

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

## References ?

1. Spring Framework Documentation  
   <https://docs.spring.io/spring-framework/docs/current/reference/html/integration.html#scheduling>
2. Baeldung Spring Task Tutorial  
   <https://www.baeldung.com/spring-scheduled-tasks>
3. Spring @Async Documentation  
   <https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/scheduling/annotation/Async.html>
