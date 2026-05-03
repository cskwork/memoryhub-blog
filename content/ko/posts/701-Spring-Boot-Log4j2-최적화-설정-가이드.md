---
title: "Spring Boot Log4j2 최적화 설정 가이드"
date: 2025-06-19T13:09:20+09:00
slug: "701-Spring-Boot-Log4j2-최적화-설정-가이드"
original_url: "https://memoryhub.tistory.com/701"
tistory_id: 701
draft: false
---

Spring Boot 애플리케이션에서 Log4j2를 활용한 최적의 로깅 시스템 구축 방법을 다룹니다. 최신 Spring Boot 3.4.3 버전을 기준으로 개발부터 운영까지 전 단계의 최적화된 설정을 제공합니다.

## 1. 최신 Spring Boot + Log4j2 기본 설정

### 버전 호환성 및 의존성 관리

**Spring Boot 3.4.3** (2025년 2월 최신)에서 Log4j2 **2.17.1+** 버전이 관리되며, 보안 취약점(CVE) 해결된 안정적인 버전을 제공합니다. Spring Boot 3.x 시리즈는 Log4j2를 1급 로깅 옵션으로 지원하며, 가상 스레드 최적화와 향상된 자동 구성을 포함합니다.

**Maven 설정 (pom.xml)**:

```
<dependencies>
    <!-- Logback 제외하고 Log4j2 포함 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
        <exclusions>
            <exclusion>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-logging</artifactId>
            </exclusion>
        </exclusions>
    </dependency>

    <!-- Log4j2 스타터 -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-log4j2</artifactId>
    </dependency>

    <!-- 비동기 로깅 성능 향상 -->
    <dependency>
        <groupId>com.lmax</groupId>
        <artifactId>disruptor</artifactId>
        <version>3.4.4</version>
    </dependency>
</dependencies>
```

### 핵심 설정 파일 구조

**log4j2-spring.xml** 파일명을 사용하여 Spring Boot 확장 기능을 활용합니다. 기본 구조는 Properties, Appenders, Loggers로 구성되며, Spring 프로퍼티 조회와 프로파일 조건부 설정을 지원합니다.

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    <Properties>
        <Property name="applicationName">${spring:spring.application.name}</Property>
        <Property name="logPath">${spring:logging.file.path:-logs}</Property>
    </Properties>

    <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{yyyy-MM-dd'T'HH:mm:ss.SSSXXX} %highlight{%-5level} --- [%15.15t] %-40.40c{1.} : %m%n"/>
        </Console>
    </Appenders>

    <Loggers>
        <Root level="INFO">
            <AppenderRef ref="Console"/>
        </Root>
    </Loggers>
</Configuration>
```

## 2. 환경별 최적화 설정 전략

### 개발 환경 최적화

**개발 환경 특성**: 디버깅 편의성, 실시간 로그 확인, 상세한 스택 트레이스가 중요합니다. 콘솔 출력 중심으로 설정하고 색상 코딩을 활용하여 가독성을 높입니다.

```
<SpringProfile name="dev | local">
    <Logger name="com.yourcompany" level="DEBUG"/>
    <Logger name="org.springframework.web" level="DEBUG"/>
    <Root level="DEBUG">
        <AppenderRef ref="Console"/>
    </Root>
</SpringProfile>
```

### 운영 환경 최적화

**운영 환경 특성**: 성능, 보안, 모니터링 연동이 핵심입니다. 파일 기반 로깅과 구조화된 JSON 로그 포맷을 사용하여 중앙 집중식 로그 수집을 지원합니다.

```
<SpringProfile name="prod">
    <Logger name="com.yourcompany" level="INFO"/>
    <Logger name="org.springframework" level="WARN"/>
    <Root level="INFO">
        <AppenderRef ref="JsonFileAppender"/>
    </Root>
</SpringProfile>
```

### 하이브리드 접근법

Properties 파일로 기본 설정을 관리하고 XML로 고급 기능을 구현하는 방식이 권장됩니다. 환경 변수를 통한 외부화와 XML의 강력한 기능을 동시에 활용할 수 있습니다.

```
# application.properties
spring.application.name=myapp
logging.config=classpath:log4j2-spring.xml
logging.level.root=${LOG_LEVEL:INFO}
logging.file.path=${LOG_PATH:/var/logs}
```

## 3. 비동기 로깅 성능 최적화

### AsyncLogger 아키텍처

Log4j2는 두 가지 비동기 방식을 제공합니다. **전체 비동기 모드**는 모든 로거가 비동기로 작동하여 최대 성능을 제공하며, **혼합 모드**는 로거별로 선택적 비동기를 적용할 수 있습니다.

**전체 비동기 설정**:

```
-DLog4jContextSelector=org.apache.logging.log4j.core.async.AsyncLoggerContextSelector
```

```
<Configuration status="WARN">
    <Appenders>
        <RollingRandomAccessFile name="AsyncFile" 
                fileName="logs/app.log"
                immediateFlush="false">
            <PatternLayout pattern="%d{HH:mm:ss.SSS} %-5level - %msg%n"/>
            <Policies>
                <SizeBasedTriggeringPolicy size="100MB"/>
            </Policies>
        </RollingRandomAccessFile>
    </Appenders>
</Configuration>
```

### 성능 튜닝 파라미터

**Ring Buffer 크기 최적화**: 높은 처리량 애플리케이션에서는 1M 이상의 링 버퍼 크기를 권장합니다. Wait Strategy는 성능과 CPU 사용량의 균형을 고려하여 선택합니다.

```
# 최고 성능 설정
log4j2.asyncLoggerRingBufferSize=1048576
log4j2.asyncLoggerWaitStrategy=Yield
log4j2.formatMsgAsync=true
log4j2.enableThreadLocals=true
log4j2.enableDirectEncoders=true
```

**성능 비교 데이터**: AsyncLogger는 동기식 로깅 대비 **10-100배** 향상된 처리량을 제공하며, 64개 스레드 환경에서 **18,000,000+ 메시지/초** 처리 성능을 보입니다. 레이턴시는 마이크로초 단위로 감소합니다.

## 4. 로그 레벨 및 패키지별 관리

### 계층적 로거 구성

로그 레벨은 패키지 단위로 세밀하게 제어할 수 있으며, 프레임워크와 애플리케이션 로그를 분리하여 관리합니다. **additivity="false"** 설정으로 중복 로깅을 방지하고 성능을 최적화합니다.

```
<Loggers>
    <!-- 프레임워크 로거 -->
    <Logger name="org.springframework" level="INFO" additivity="false">
        <AppenderRef ref="FrameworkAppender"/>
    </Logger>
    <Logger name="org.hibernate" level="WARN" additivity="false">
        <AppenderRef ref="DatabaseAppender"/>
    </Logger>

    <!-- 애플리케이션 로거 -->
    <Logger name="com.company.service" level="DEBUG">
        <AppenderRef ref="ServiceAppender"/>
    </Logger>
    <Logger name="com.company.dao" level="INFO">
        <AppenderRef ref="DatabaseAppender"/>
    </Logger>

    <!-- 고성능 비동기 로거 -->
    <AsyncLogger name="com.company.performance" level="TRACE" includeLocation="false">
        <AppenderRef ref="PerformanceAppender"/>
    </AsyncLogger>
</Loggers>
```

### 동적 로그 레벨 제어

운영 중에도 `monitorInterval` 설정을 통해 설정 파일 변경을 자동으로 감지하고 적용할 수 있습니다. JMX를 통한 실시간 레벨 조정도 가능합니다.

```
<Configuration status="WARN" monitorInterval="300">
    <!-- 5분마다 설정 파일 변경 확인 -->
</Configuration>
```

## 5. 로그 파일 롤링 정책 및 아카이빙

### 복합 롤링 정책

시간 기반과 크기 기반 롤링을 결합하여 효율적인 로그 관리를 구현합니다. 자동 압축과 보관 기간 설정으로 디스크 공간을 최적화합니다.

```
<RollingFile name="CompoundRolling" 
             fileName="logs/app.log"
             filePattern="logs/app-%d{yyyy-MM-dd}-%i.log.gz">
    <PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
    <Policies>
        <OnStartupTriggeringPolicy/>
        <SizeBasedTriggeringPolicy size="50MB"/>
        <TimeBasedTriggeringPolicy/>
    </Policies>
    <DefaultRolloverStrategy max="10">
        <Delete basePath="logs" maxDepth="2">
            <IfFileName glob="*/app-*.log.gz"/>
            <IfLastModified age="P7D"/>
        </Delete>
    </DefaultRolloverStrategy>
</RollingFile>
```

### 고성능 RollingRandomAccessFile

**RollingRandomAccessFile** 어펜더는 **BufferedIO**와 **RandomAccessFile**을 활용하여 최고의 I/O 성능을 제공합니다. 대용량 로그 처리 시 권장되는 방식입니다.

```
<RollingRandomAccessFile name="HighPerformanceRolling" 
        fileName="logs/highperf.log"
        filePattern="logs/highperf-%d{yyyy-MM-dd-HH}-%i.log.gz"
        immediateFlush="false">
    <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{1} - %msg%n"/>
    <Policies>
        <TimeBasedTriggeringPolicy interval="1"/>
        <SizeBasedTriggeringPolicy size="500MB"/>
    </Policies>
    <DefaultRolloverStrategy max="20"/>
</RollingRandomAccessFile>
```

## 6. 로그 패턴 최적화

### 성능 중심 패턴 설계

패턴 요소별 성능 영향을 고려하여 설계합니다. **위치 정보**(`%L`, `%M`, `%l`)는 높은 오버헤드를 가지므로 운영 환경에서 피하고, **가비지 프리 로깅**을 위해 스레드 로컬을 활성화합니다.

| 패턴 요소 | 성능 영향 | 용도 |
| --- | --- | --- |
| `%d{HH:mm:ss.SSS}` | 낮음 | 운영 환경 |
| `%t` | 낮음 | 스레드 식별 |
| `%logger{1}` | 낮음 | 클래스명 (짧게) |
| `%L` | **높음** | 개발 환경만 |
| `%M` | **높음** | 개발 환경만 |
| `%l` | **매우 높음** | 비동기에서 사용 금지 |

**최적화된 패턴 예시**:

```
<!-- 운영 환경: 고성능 -->
<PatternLayout pattern="%d{HH:mm:ss.SSS} %-5level - %msg%n"/>

<!-- 개발 환경: 상세 정보 -->
<PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-5level %logger{36}:%L - %msg%n"/>

<!-- 가비지 프리 최적화 -->
<PatternLayout pattern="%d{DEFAULT} %-5p [%t] %c{1} - %m%n"/>
```

## 7. MDC 활용 방법

### 요청 추적을 위한 MDC 구현

**MDC**(Mapped Diagnostic Context)는 스레드별로 컨텍스트 정보를 저장하여 분산 시스템에서 요청을 추적할 수 있게 합니다. Spring Boot에서 필터를 통해 자동으로 MDC를 설정하고 정리합니다.

```
@Component
@Slf4j
public class RequestLoggingFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, 
                        FilterChain chain) throws IOException, ServletException {

        HttpServletRequest httpRequest = (HttpServletRequest) request;

        // MDC 설정
        MDC.put("requestId", UUID.randomUUID().toString());
        MDC.put("sessionId", httpRequest.getSession().getId());
        MDC.put("userAgent", httpRequest.getHeader("User-Agent"));
        MDC.put("clientIP", getClientIP(httpRequest));
        MDC.put("requestURI", httpRequest.getRequestURI());

        try {
            log.info("Request started: {} {}", httpRequest.getMethod(), httpRequest.getRequestURI());
            chain.doFilter(request, response);
            log.info("Request completed");
        } finally {
            MDC.clear(); // 메모리 누수 방지
        }
    }
}
```

### 비동기 환경에서의 MDC 전파

비동기 처리에서 MDC 컨텍스트를 전파하기 위해 **TaskDecorator**를 구현합니다. 스레드 풀 실행 시 부모 스레드의 MDC를 자식 스레드로 복사합니다.

```
@Configuration
@EnableAsync
public class AsyncConfig {

    @Bean
    public TaskExecutor taskExecutor() {
        ThreadPoolTaskExecutor executor = new ThreadPoolTaskExecutor();
        executor.setCorePoolSize(5);
        executor.setMaxPoolSize(10);
        executor.setTaskDecorator(new MDCTaskDecorator());
        executor.initialize();
        return executor;
    }
}

public class MDCTaskDecorator implements TaskDecorator {
    @Override
    public Runnable decorate(Runnable runnable) {
        Map<String, String> contextMap = MDC.getCopyOfContextMap();
        return () -> {
            try {
                if (contextMap != null) {
                    MDC.setContextMap(contextMap);
                }
                runnable.run();
            } finally {
                MDC.clear();
            }
        };
    }
}
```

### MDC 패턴 활용

로그 패턴에서 MDC 값을 활용하여 구조화된 로깅을 구현합니다. JSON 형태로 출력하여 로그 분석 도구와의 연동을 최적화합니다.

```
<!-- 패턴에서 MDC 활용 -->
<PatternLayout pattern="%d [%X{requestId}] [%X{userId}] %-5level %logger - %msg%n"/>

<!-- JSON 형태로 MDC 출력 -->
<JsonTemplateLayout>
    <EventTemplateAdditionalField key="request_id" value="${mdc:requestId}"/>
    <EventTemplateAdditionalField key="user_id" value="${mdc:userId}"/>
    <EventTemplateAdditionalField key="session_id" value="${mdc:sessionId}"/>
</JsonTemplateLayout>
```

## 8. 운영 환경 로그 수집 및 모니터링 연동

### ELK Stack 연동

**Elasticsearch, Logstash, Kibana** 스택과의 연동을 위해 JSON 형태의 구조화된 로그를 생성합니다. **JsonTemplateLayout**을 사용하여 ECS(Elastic Common Schema) 호환 형태로 로그를 출력합니다.

```
<!-- ELK Stack용 JSON 로그 -->
<RollingFile name="JSONFile" 
             fileName="/var/log/app/app.log"
             filePattern="/var/log/app/app-%d{yyyy-MM-dd}-%i.log">
    <JsonTemplateLayout eventTemplateUri="classpath:EcsLayout.json"/>
    <Policies>
        <TimeBasedTriggeringPolicy/>
        <SizeBasedTriggeringPolicy size="50MB"/>
    </Policies>
</RollingFile>
```

**ECS 호환 JSON 템플릿**:

```
{
  "@timestamp": {
    "$resolver": "timestamp",
    "pattern": {"format": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'", "timeZone": "UTC"}
  },
  "log.level": {"$resolver": "level", "field": "name"},
  "message": {"$resolver": "message", "stringified": true},
  "service.name": "${env:SERVICE_NAME:-unknown}",
  "service.version": "${env:SERVICE_VERSION:-unknown}",
  "trace.id": "${mdc:traceId:-}",
  "span.id": "${mdc:spanId:-}"
}
```

### Datadog APM 연동

**Datadog APM**과의 연동을 위해 트레이스 ID와 스팬 ID를 MDC에서 추출하여 로그에 포함시킵니다. 분산 추적과 로그를 연결하여 완전한 관찰 가능성을 제공합니다.

```
<JsonTemplateLayout>
    <EventTemplateAdditionalField key="dd.trace_id" value="${mdc:dd.trace_id}"/>
    <EventTemplateAdditionalField key="dd.span_id" value="${mdc:dd.span_id}"/>
    <EventTemplateAdditionalField key="service" value="${env:DD_SERVICE}"/>
    <EventTemplateAdditionalField key="env" value="${env:DD_ENV}"/>
</JsonTemplateLayout>
```

### Kubernetes 환경 로그 수집

**사이드카 패턴**을 활용하여 로그를 공유 볼륨에 저장하고 별도의 로그 수집 컨테이너가 중앙 집중식 로그 시스템으로 전송합니다.

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: log4j2-config
data:
  log4j2.xml: |
    <Configuration>
      <Appenders>
        <File name="JsonFile" fileName="/shared-logs/app.log">
          <JsonTemplateLayout eventTemplateUri="classpath:kubernetes-template.json"/>
        </File>
      </Appenders>
    </Configuration>
```

## 9. 보안을 위한 민감정보 마스킹

### PII 데이터 마스킹 구현

**개인식별정보**(PII) 보호를 위해 커스텀 패턴 컨버터를 구현하여 이메일, 전화번호, 신용카드 번호 등을 자동으로 마스킹합니다.

```
@Plugin(name = "PIIMaskingConverter", category = "Converter")
public class PIIMaskingConverter extends LogEventPatternConverter {

    private static final Pattern EMAIL_PATTERN = 
        Pattern.compile("\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b");
    private static final Pattern PHONE_PATTERN = 
        Pattern.compile("\\b\\d{3}-\\d{3}-\\d{4}\\b");

    @Override
    public void format(LogEvent event, StringBuilder toAppendTo) {
        String message = event.getMessage().getFormattedMessage();
        message = EMAIL_PATTERN.matcher(message).replaceAll("***@***.***");
        message = PHONE_PATTERN.matcher(message).replaceAll("***-***-****");
        toAppendTo.append(message);
    }
}
```

### 보안 정책 기반 필터링

**RewritePolicy**를 활용하여 JSON 구조에서 특정 필드를 제거하거나 마스킹합니다. GDPR 및 개인정보보호법 준수를 위한 포괄적인 데이터 보호 전략을 구현합니다.

```
<Rewrite name="RewriteAppender">
    <AppenderRef ref="FileAppender"/>
    <MaskPolicies>
        <MaskPolicy type="JSON" enabled="true">
            <Exclusions>
                <Exclusion value="$.creditCard"/>
                <Exclusion value="$.ssn"/>
                <Exclusion value="$.password"/>
            </Exclusions>
        </MaskPolicy>
    </MaskPolicies>
</Rewrite>
```

### 보안 모범 사례

**JsonTemplateLayout** 사용을 권장하며, **PatternLayout**보다 안전한 출력 형식을 보장합니다. 사용자 제어 입력을 로그에 기록할 때는 **%encode** 컨버터를 사용하여 로그 인젝션 공격을 방지합니다.

```
<!-- 안전한 패턴 사용 -->
<PatternLayout pattern="%d [%t] %-5level %logger - %encode{%msg}{CRLF}%n"/>
```

## 10. 실제 사용 예제 및 완전한 설정

### 완전한 운영 환경 설정

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN" monitorInterval="300">
    <Properties>
        <Property name="LOG_PATTERN">%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-5level %logger{1} - %msg%n</Property>
        <Property name="LOG_DIR">${sys:log.dir:-logs}</Property>
    </Properties>

    <Appenders>
        <!-- 콘솔 - 에러만 출력 -->
        <Console name="Console" target="SYSTEM_OUT" direct="true">
            <PatternLayout pattern="${LOG_PATTERN}"/>
            <ThresholdFilter level="ERROR" onMatch="ACCEPT" onMismatch="DENY"/>
        </Console>

        <!-- 고성능 애플리케이션 로그 -->
        <RollingRandomAccessFile name="AppLog" 
                fileName="${LOG_DIR}/application.log"
                filePattern="${LOG_DIR}/application-%d{yyyy-MM-dd-HH}-%i.log.gz"
                immediateFlush="false">
            <JsonTemplateLayout eventTemplateUri="classpath:production-template.json"/>
            <Policies>
                <TimeBasedTriggeringPolicy interval="1"/>
                <SizeBasedTriggeringPolicy size="500MB"/>
            </Policies>
            <DefaultRolloverStrategy max="24">
                <Delete basePath="${LOG_DIR}" maxDepth="2">
                    <IfFileName glob="*/application-*.log.gz"/>
                    <IfLastModified age="P7D"/>
                </Delete>
            </DefaultRolloverStrategy>
        </RollingRandomAccessFile>

        <!-- 에러 전용 로그 -->
        <RollingFile name="ErrorLog" 
                fileName="${LOG_DIR}/error.log"
                filePattern="${LOG_DIR}/error-%d{yyyy-MM-dd}.log.gz">
            <PatternLayout pattern="${LOG_PATTERN}"/>
            <LevelRangeFilter minLevel="ERROR" maxLevel="ERROR" onMatch="ACCEPT" onMismatch="DENY"/>
            <Policies>
                <TimeBasedTriggeringPolicy/>
                <SizeBasedTriggeringPolicy size="50MB"/>
            </Policies>
        </RollingFile>

        <!-- 성능 모니터링 로그 -->
        <RollingFile name="PerfLog" 
                fileName="${LOG_DIR}/performance.log"
                filePattern="${LOG_DIR}/performance-%d{yyyy-MM-dd}.log.gz">
            <PatternLayout pattern="%d{HH:mm:ss.SSS} [%X{requestId}] [%X{operation}] - %msg%n"/>
            <Policies>
                <TimeBasedTriggeringPolicy/>
            </Policies>
        </RollingFile>
    </Appenders>

    <Loggers>
        <!-- 성능 중요 비동기 로거 -->
        <AsyncLogger name="com.company.performance" level="INFO" includeLocation="false">
            <AppenderRef ref="PerfLog"/>
        </AsyncLogger>

        <!-- 애플리케이션 로거 -->
        <AsyncLogger name="com.company" level="DEBUG" includeLocation="false">
            <AppenderRef ref="AppLog"/>
        </AsyncLogger>

        <!-- 프레임워크 로거 -->
        <Logger name="org.springframework" level="INFO" additivity="false">
            <AppenderRef ref="AppLog"/>
        </Logger>
        <Logger name="org.hibernate" level="WARN" additivity="false">
            <AppenderRef ref="AppLog"/>
        </Logger>

        <Root level="WARN">
            <AppenderRef ref="Console"/>
            <AppenderRef ref="AppLog"/>
            <AppenderRef ref="ErrorLog"/>
        </Root>
    </Loggers>
</Configuration>
```

### 애플리케이션 코드 구현

```
@RestController
@Slf4j
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        // MDC 설정으로 요청 추적
        MDC.put("operation", "getUser");
        MDC.put("userId", id.toString());

        try {
            log.info("사용자 정보 조회 시작: {}", id);

            User user = userService.findById(id);
            log.debug("사용자 조회 성공: {}", user.getName());

            return ResponseEntity.ok(user);
        } catch (UserNotFoundException e) {
            log.error("사용자 찾을 수 없음: {}", id, e);
            return ResponseEntity.notFound().build();
        } catch (Exception e) {
            log.error("사용자 조회 중 예상치 못한 오류 발생", e);
            return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();
        } finally {
            MDC.clear();
        }
    }
}

@Service
@Slf4j
public class UserService {

    public User createUser(UserDto userDto) {
        log.info("새 사용자 생성: {}", userDto.getEmail());

        // 성능 로깅
        long startTime = System.currentTimeMillis();

        try {
            User user = userRepository.save(new User(userDto));

            long duration = System.currentTimeMillis() - startTime;
            log.info("사용자 생성 완료 - ID: {}, 소요시간: {}ms", user.getId(), duration);

            return user;
        } catch (Exception e) {
            log.error("사용자 생성 실패: {}", userDto.getEmail(), e);
            throw new UserCreationException("사용자 생성 중 오류 발생", e);
        }
    }
}
```

### JVM 튜닝 파라미터

```
# 최적 성능을 위한 JVM 설정
-DLog4jContextSelector=org.apache.logging.log4j.core.async.AsyncLoggerContextSelector
-Dlog4j2.asyncLoggerRingBufferSize=1048576
-Dlog4j2.asyncLoggerWaitStrategy=Yield
-Dlog4j2.formatMsgAsync=true
-Dlog4j2.enableThreadLocals=true
-Dlog4j2.enableDirectEncoders=true

# GC 최적화
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200
-XX:+DisableExplicitGC
-XX:G1HeapRegionSize=16m
```

이 종합 가이드는 Spring Boot에서 Log4j2의 모든 핵심 기능을 다루며, 개발부터 운영까지 각 단계에서 최적화된 로깅 시스템 구축을 지원합니다. **비동기 로깅으로 10-100배 성능 향상**, **구조화된 로깅으로 효율적인 모니터링**, **보안 강화를 통한 개인정보 보호**를 동시에 달성할

수 있습니다.

핵심 권장사항은 다음과 같습니다: 운영 환경에서는 AsyncLogger와 JsonTemplateLayout 사용, 개발 환경에서는 상세한 디버깅 정보 포함, MDC 활용한 분산 추적, 그리고 정기적인 보안 감사와 성능 모니터링입니다.
