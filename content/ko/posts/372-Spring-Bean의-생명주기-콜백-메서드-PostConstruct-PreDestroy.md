---
title: "Spring Bean의 생명주기 콜백 메서드 (@PostConstruct & @PreDestroy) ?"
date: 2024-11-14T12:32:25+09:00
slug: "372-Spring-Bean의-생명주기-콜백-메서드-PostConstruct-PreDestroy"
original_url: "https://memoryhub.tistory.com/372"
tistory_id: 372
draft: false
categories: ["데브 프레임워크"]
tags: ["Spring"]
---

안녕하세요! 오늘은 Spring Bean의 초기화와 소멸 시점에 실행되는 콜백 메서드에 대해 알아보겠습니다.

## Bean 생명주기 콜백이 필요한 이유 ?

데이터베이스 연결, 캐시 초기화, 외부 리소스 로딩 등 Bean이 생성된 직후나 소멸되기 직전에 특별한 작업이 필요한 경우가 있습니다.

예를 들어볼까요?

- 애플리케이션 시작 시 필요한 설정 파일 로딩
- 데이터베이스 커넥션 풀 초기화
- 임시 파일 정리
- 리소스 해제

## @PostConstruct ?

Bean이 생성되고 의존성 주입이 완료된 후 실행되는 메서드입니다.

```
@Service
public class UserService {

    private Cache cache;

    @PostConstruct
    public void init() {
        System.out.println("UserService 초기화 작업 시작");
        cache = new Cache();
        // 캐시 워밍업
        cache.preloadData();
    }
}
```

### @PostConstruct 특징

1. **실행 시점**

   - 생성자 호출 후
   - 의존성 주입 완료 후
   - 실제 사용되기 전
2. **사용 케이스**

   - 초기 데이터 로딩
   - 외부 리소스 연결
   - 캐시 워밍업

## @PreDestroy ?

스프링 컨테이너가 종료되기 전에 실행되는 메서드입니다.

```
@Component
public class DatabaseManager {

    private Connection conn;

    @PreDestroy
    public void cleanup() {
        System.out.println("리소스 정리 시작");
        if(conn != null) {
            try {
                conn.close();
            } catch (SQLException e) {
                // 예외 처리
            }
        }
    }
}
```

### @PreDestroy 특징

1. **실행 시점**

   - 스프링 컨테이너 종료 직전
   - Bean 삭제 직전
2. **사용 케이스**

   - 연결 종료 (DB, 네트워크)
   - 임시 파일 삭제
   - 캐시 정리

## 실제 활용 예시 ?

### 1. S3 파일 캐싱 서비스

```
@Service
public class FileService {

    private Map<String, byte[]> fileCache;

    @PostConstruct
    public void initializeCache() {
        fileCache = new HashMap<>();
        // S3에서 자주 사용하는 파일들을 미리 다운로드
        downloadFrequentlyUsedFiles();
    }

    @PreDestroy
    public void clearCache() {
        fileCache.clear();
        // 임시 파일 삭제
        deleteTempFiles();
    }
}
```

### 2. 데이터베이스 커넥션 풀 관리

```
@Component
public class DatabaseConnectionPool {

    private List<Connection> connectionPool;

    @PostConstruct
    public void initialize() {
        connectionPool = new ArrayList<>();
        // 초기 커넥션 생성
        createInitialConnections();
    }

    @PreDestroy
    public void disconnect() {
        // 모든 커넥션 종료
        connectionPool.forEach(this::closeConnection);
    }
}
```

## 주의사항 ⚠️

1. **@PostConstruct**

   - 생성자에서는 의존성이 아직 주입되지 않은 상태
   - 무거운 작업은 별도 스레드로 실행 권장
2. **@PreDestroy**

   - 애플리케이션이 강제 종료되면 실행되지 않음
   - 반드시 실행이 필요한 로직은 다른 방법 고려

## 마치며 ?

Bean 생명주기 콜백을 잘 활용하면 애플리케이션의 리소스를 효율적으로 관리할 수 있습니다. 초기화와 정리 작업을 깔끔하게 구현해보세요!

---

References:

- Spring Framework Documentation: <https://docs.spring.io/spring-framework/docs/current/reference/html/core.html#beans-factory-lifecycle>
- Java EE Tutorial: <https://javaee.github.io/tutorial/resource-creation.html>
- Spring Boot Documentation: <https://docs.spring.io/spring-boot/docs/current/reference/html/spring-boot-features.html#boot-features-application-lifecycle-callbacks>
