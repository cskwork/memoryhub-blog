---
title: "? Log4j2 설정 완벽 정복 - 이제 System.out.println() 그만 쓰세요!"
date: 2025-06-15T11:55:01+09:00
slug: "688-Log4j2-설정-완벽-정복-이제-System-out-println-그만-쓰세요"
original_url: "https://memoryhub.tistory.com/688"
tistory_id: 688
draft: false
---

```
╔═══════════════════════════════════════════════╗
║     ? LOG4J2 CONFIGURATION                   ║
╠═══════════════════════════════════════════════╣
║   ┌─────────┐    ┌─────────┐   ┌─────────┐   ║
║   │ CONSOLE │────│ FILE    │───│ ROLLING │   ║
║   └────┬────┘    └────┬────┘   └────┬────┘   ║
║        │              │              │        ║
║        └──────────────┴──────────────┘        ║
║                       │                       ║
║                  ┌────▼────┐                  ║
║                  │ LOGGER  │                  ║
║                  └─────────┘                  ║
╚═══════════════════════════════════════════════╝
```

안녕하세요! 최근 프로덕션 서버에서 디버깅하다가 System.out.println()으로 도배된 레거시 코드를 보고 식은땀을 흘렸습니다. ?

여러분도 혹시 로그 파일이 100GB를 넘어서 서버가 다운된 경험이 있으신가요? 아니면 중요한 에러 로그를 놓쳐서 장애 원인을 못 찾은 적은요?

오늘은 제가 3년간 삽질하며 터득한 **Log4j2 설정의 모든 것**을 공유합니다. 이 글을 읽고 나면 로깅 때문에 야근하는 일은 없을 거예요!

⚡ **TL;DR**

- Log4j2로 효율적인 로깅 시스템 구축하기
- 파일 크기 관리와 성능 최적화까지 한 번에!

## 목차

1. [배경 - 왜 Log4j2인가?](#1-%EB%B0%B0%EA%B2%BD)
2. [핵심 개념 정리](#2-%ED%95%B5%EC%8B%AC-%EA%B0%9C%EB%85%90)
3. [실습 - 단계별 설정](#3-%EC%8B%A4%EC%8A%B5)
4. [베스트 프랙티스](#4-%EB%B2%A0%EC%8A%A4%ED%8A%B8-%ED%94%84%EB%9E%99%ED%8B%B0%EC%8A%A4)
5. [마치며 & 참고자료](#5-%EB%A7%88%EC%B9%98%EB%A9%B0)

---

## 1. 배경

### ? 왜 Log4j2를 선택해야 할까?

Spring Boot 프로젝트를 시작하면 기본으로 Logback이 포함되어 있죠. 그런데 왜 굳이 Log4j2로 바꿔야 할까요?

| 특징 | Logback | Log4j2 |
| --- | --- | --- |
| **비동기 로깅 성능** | 보통 | 매우 빠름 (3-10배) |
| **메모리 사용량** | 높음 | 낮음 (GC 압박 ↓) |
| **람다 표현식** | 미지원 | 지원 ✅ |
| **설정 파일 형식** | XML만 | XML, JSON, YAML, Properties |

### ? 핵심 용어 정리

✅ **Logger**: 로그를 생성하는 주체  
✅ **Appender**: 로그를 어디에 출력할지 결정 (콘솔, 파일 등)  
✅ **Layout**: 로그 메시지 형식 정의  
✅ **Level**: 로그의 중요도 (TRACE < DEBUG < INFO < WARN < ERROR < FATAL)

## 2. 핵심 개념

> **Log4j2는 고성능 Java 로깅 프레임워크로, 비동기 로깅과 람다 표현식을 지원하여 성능과 편의성을 모두 잡았다.**

### ?️ 아키텍처 이해하기

```
// 로거 생성 - 클래스별로 하나씩
private static final Logger logger = LogManager.getLogger(MyClass.class);

// 람다 표현식으로 성능 최적화
logger.debug("사용자 {} 의 요청 처리 시간: {} ms", 
    () -> getUserName(),  // 디버그 레벨일 때만 실행됨
    () -> calculateTime()
);
```

## 3. 실습

### ① Spring Boot 프로젝트에 Log4j2 설정하기

**1단계: 의존성 추가**

```
// build.gradle
configurations {
    all {
        // Logback 제외
        exclude group: 'org.springframework.boot', module: 'spring-boot-starter-logging'
    }
}

dependencies {
    // Log4j2 추가
    implementation 'org.springframework.boot:spring-boot-starter-log4j2'

    // 비동기 로깅을 위한 Disruptor (선택사항이지만 강력 추천!)
    implementation 'com.lmax:disruptor:3.4.4'
}
```

### ② log4j2.xml 작성하기

**2단계: src/main/resources/log4j2.xml 생성**

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN" monitorInterval="30">
    <!-- Properties: 재사용 가능한 변수 정의 -->
    <Properties>
        <Property name="LOG_PATTERN">
            %d{yyyy-MM-dd HH:mm:ss.SSS} %highlight{%-5level} [%t] %style{%C{1.}}{cyan} : %msg%n%throwable
        </Property>
        <Property name="LOG_DIR">./logs</Property>
    </Properties>

    <Appenders>
        <!-- 콘솔 출력 설정 -->
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="${LOG_PATTERN}" disableAnsi="false"/>
        </Console>

        <!-- 파일 출력 설정 (일별 롤링) -->
        <RollingFile name="RollingFile" 
                     fileName="${LOG_DIR}/app.log"
                     filePattern="${LOG_DIR}/app-%d{yyyy-MM-dd}-%i.log.gz">
            <PatternLayout pattern="${LOG_PATTERN}"/>
            <Policies>
                <!-- 매일 자정에 롤링 -->
                <TimeBasedTriggeringPolicy />
                <!-- 파일 크기가 100MB 넘으면 롤링 -->
                <SizeBasedTriggeringPolicy size="100MB" />
            </Policies>
            <!-- 최대 30개 파일 유지, 총 3GB 제한 -->
            <DefaultRolloverStrategy max="30">
                <Delete basePath="${LOG_DIR}" maxDepth="1">
                    <IfFileName glob="app-*.log.gz" />
                    <IfLastModified age="30d" />
                </Delete>
            </DefaultRolloverStrategy>
        </RollingFile>

        <!-- 에러 전용 파일 -->
        <RollingFile name="ErrorFile"
                     fileName="${LOG_DIR}/error.log"
                     filePattern="${LOG_DIR}/error-%d{yyyy-MM-dd}.log.gz">
            <PatternLayout pattern="${LOG_PATTERN}"/>
            <ThresholdFilter level="ERROR" onMatch="ACCEPT" onMismatch="DENY"/>
            <Policies>
                <TimeBasedTriggeringPolicy />
            </Policies>
        </RollingFile>

        <!-- 비동기 로깅 설정 (성능 향상) -->
        <Async name="AsyncFile">
            <AppenderRef ref="RollingFile"/>
        </Async>
    </Appenders>

    <Loggers>
        <!-- 애플리케이션 로거 -->
        <Logger name="com.myapp" level="DEBUG" additivity="false">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="AsyncFile"/>
            <AppenderRef ref="ErrorFile"/>
        </Logger>

        <!-- 외부 라이브러리 로그 레벨 조정 -->
        <Logger name="org.springframework" level="INFO"/>
        <Logger name="org.hibernate" level="WARN"/>

        <!-- SQL 로깅 (개발 환경에서만 사용 권장) -->
        <Logger name="org.hibernate.SQL" level="DEBUG"/>
        <Logger name="org.hibernate.type.descriptor.sql.BasicBinder" level="TRACE"/>

        <!-- Root 로거 -->
        <Root level="INFO">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="AsyncFile"/>
        </Root>
    </Loggers>
</Configuration>
```

### ③ 실제 코드에서 사용하기

**3단계: 로거 사용 예제**

```
package com.myapp.service;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    // 클래스별 로거 생성
    private static final Logger logger = LogManager.getLogger(UserService.class);

    public User createUser(UserDto userDto) {
        logger.info("사용자 생성 시작: {}", userDto.getEmail());

        try {
            // 디버그 로그 - 람다 표현식 사용
            logger.debug("검증 시작 - 이메일: {}, 이름: {}", 
                () -> userDto.getEmail(), 
                () -> userDto.getName()
            );

            User user = User.builder()
                .email(userDto.getEmail())
                .name(userDto.getName())
                .build();

            // 비즈니스 로직...

            logger.info("사용자 생성 완료 - ID: {}", user.getId());
            return user;

        } catch (Exception e) {
            // 에러 로깅 - 스택트레이스 포함
            logger.error("사용자 생성 실패 - 이메일: {}", userDto.getEmail(), e);
            throw new ServiceException("사용자 생성 실패", e);
        }
    }

    // 성능 측정 로깅 예제
    public List<User> findAllUsers() {
        long startTime = System.currentTimeMillis();

        try {
            List<User> users = userRepository.findAll();
            return users;
        } finally {
            long elapsed = System.currentTimeMillis() - startTime;
            // 실행 시간이 1초 이상이면 경고
            if (elapsed > 1000) {
                logger.warn("사용자 조회 성능 저하 - 실행시간: {}ms", elapsed);
            } else {
                logger.debug("사용자 조회 완료 - 실행시간: {}ms", elapsed);
            }
        }
    }
}
```

## 4. 모범 사례

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **MDC (Mapped Diagnostic Context)** | 요청별 추적 ID로 분산 환경 디버깅 용이 | 스레드 전환 시 컨텍스트 유실 주의 |
| **비동기 로깅** | 3-10배 성능 향상 | 애플리케이션 종료 시 로그 유실 가능 |
| **조건부 로깅** | 불필요한 문자열 연산 방지 | 람다 표현식 사용 권장 |
| **구조화된 로깅** | 로그 분석 도구 활용 용이 | JSON 형식 고려 |

### ? 프로덕션 환경 권장 설정

```
<!-- 프로덕션용 추가 설정 -->
<Configuration status="ERROR" monitorInterval="300">
    <Properties>
        <!-- 환경별 로그 경로 -->
        <Property name="LOG_DIR">${env:LOG_PATH:-/var/log/myapp}</Property>
    </Properties>

    <!-- 성능을 위한 비동기 설정 -->
    <Appenders>
        <Async name="AsyncAll" bufferSize="512" blocking="false">
            <AppenderRef ref="RollingFile"/>
        </Async>
    </Appenders>
</Configuration>
```

### ? MDC 활용 예제

```
@Component
public class RequestLoggingFilter extends OncePerRequestFilter {

    @Override
    protected void doFilterInternal(HttpServletRequest request, 
                                  HttpServletResponse response, 
                                  FilterChain filterChain) throws ServletException, IOException {
        // 요청별 고유 ID 생성
        String requestId = UUID.randomUUID().toString();

        try {
            // MDC에 추가 - 모든 로그에 자동 포함됨
            MDC.put("requestId", requestId);
            MDC.put("userId", getUserId(request));

            filterChain.doFilter(request, response);
        } finally {
            // 반드시 정리!
            MDC.clear();
        }
    }
}
```

## 5. 마치며

오늘은 Log4j2 설정의 A to Z를 살펴봤습니다.

**✨ 핵심 정리:**

- Log4j2는 성능과 기능 면에서 Logback보다 우수합니다
- 비동기 로깅과 람다 표현식으로 성능을 최적화할 수 있습니다
- MDC를 활용하면 분산 환경에서도 효과적인 디버깅이 가능합니다

**? 실무 적용 팁:** 처음부터 완벽한 설정을 만들려 하지 마세요. 기본 설정으로 시작해서 필요에 따라 점진적으로 개선하는 것이 좋습니다.

이 글이 도움이 되셨다면 ❤️ 하트와 댓글 부탁드려요! 궁금한 점이 있다면 편하게 물어봐 주세요. ?

---

### ? 참고자료

- [Log4j2 공식 문서](https://logging.apache.org/log4j/2.x/)
- [샘플 프로젝트 (GitHub)](https://github.com/apache/logging-log4j2/tree/master/log4j-samples)
- 추가 읽을거리:
  - [Log4j2 성능 벤치마크](https://logging.apache.org/log4j/2.x/performance.html)
  - [Spring Boot Logging 가이드](https://docs.spring.io/spring-boot/docs/current/reference/html/features.html#features.logging)
  - [MDC를 활용한 분산 추적](https://www.baeldung.com/mdc-in-log4j-2-logback)
