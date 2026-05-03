---
title: "Spring Boot Log4j2 Optimization Configuration Guide"
date: 2025-06-19T13:09:20+09:00
slug: "701-Spring-Boot-Log4j2-최적화-설정-가이드"
original_url: "https://memoryhub.tistory.com/701"
tistory_id: 701
draft: false
---

This guide covers building an optimal logging system using Log4j2 in Spring Boot applications. Based on the latest Spring Boot 3.4.3 version, it provides optimized configurations for all stages from development to production.

## 1. Latest Spring Boot + Log4j2 Basic Configuration

### Version Compatibility and Dependency Management

**Spring Boot 3.4.3** (latest as of February 2025) manages Log4j2 **2.17.1+** version, providing stable versions with resolved security vulnerabilities (CVE). Spring Boot 3.x series supports Log4j2 as a first-class logging option, including virtual thread optimization and improved auto-configuration.

**Maven Configuration (pom.xml)**:

```
<dependencies>
    <!-- Exclude Logback and include Log4j2 -->
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

    <!-- Log4j2 Starter -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-log4j2</artifactId>
    </dependency>

    <!-- Async logging performance enhancement -->
    <dependency>
        <groupId>com.lmax</groupId>
        <artifactId>disruptor</artifactId>
        <version>3.4.4</version>
    </dependency>
</dependencies>
```

### Core Configuration File Structure

Use **log4j2-spring.xml** filename to leverage Spring Boot extended features. The basic structure consists of Properties, Appenders, and Loggers, supporting Spring property lookup and profile-based conditional configuration.

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

## 2. Environment-Specific Optimization Strategies

### Development Environment Optimization

**Development Environment Characteristics**: Debug convenience, real-time log verification, and detailed stack traces are important. Configure with console output focus and use color coding for improved readability.

```
<SpringProfile name="dev | local">
    <Logger name="com.yourcompany" level="DEBUG"/>
    <Logger name="org.springframework.web" level="DEBUG"/>
    <Root level="DEBUG">
        <AppenderRef ref="Console"/>
    </Root>
</SpringProfile>
```

### Production Environment Optimization

**Production Environment Characteristics**: Performance, security, and monitoring integration are critical. Use file-based logging and structured JSON log format to support centralized log collection.

```
<SpringProfile name="prod">
    <Logger name="com.yourcompany" level="INFO"/>
    <Logger name="org.springframework" level="WARN"/>
    <Root level="INFO">
        <AppenderRef ref="JsonFileAppender"/>
    </Root>
</SpringProfile>
```

### Hybrid Approach

Managing basic configuration with Properties files while implementing advanced features with XML is recommended. You can simultaneously leverage external configuration through environment variables and the powerful features of XML.

```
# application.properties
spring.application.name=myapp
logging.config=classpath:log4j2-spring.xml
logging.level.root=${LOG_LEVEL:INFO}
logging.file.path=${LOG_PATH:/var/logs}
```

## 3. Async Logging Performance Optimization

### AsyncLogger Architecture

Log4j2 provides two asynchronous modes. **Fully async mode** runs all loggers asynchronously for maximum performance, while **mixed mode** allows selective async application per logger.

**Fully async configuration**:

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

### Performance Tuning Parameters

**Ring Buffer Size Optimization**: For high-throughput applications, ring buffer sizes of 1M or larger are recommended. Wait Strategy should be selected considering the balance between performance and CPU usage.

```
# Maximum performance configuration
log4j2.asyncLoggerRingBufferSize=1048576
log4j2.asyncLoggerWaitStrategy=Yield
log4j2.formatMsgAsync=true
log4j2.enableThreadLocals=true
log4j2.enableDirectEncoders=true
```

**Performance Comparison Data**: AsyncLogger provides **10-100x** improved throughput compared to synchronous logging, with **18,000,000+ messages/second** processing performance in 64-thread environments. Latency reduces to microsecond levels.

## 4. Log Level and Package-Specific Management

### Hierarchical Logger Configuration

Log levels can be finely controlled per package, with framework and application logs managed separately. The **additivity="false"** setting prevents duplicate logging and optimizes performance.

```
<Loggers>
    <!-- Framework loggers -->
    <Logger name="org.springframework" level="INFO" additivity="false">
        <AppenderRef ref="FrameworkAppender"/>
    </Logger>
    <Logger name="org.hibernate" level="WARN" additivity="false">
        <AppenderRef ref="DatabaseAppender"/>
    </Logger>

    <!-- Application loggers -->
    <Logger name="com.company.service" level="DEBUG">
        <AppenderRef ref="ServiceAppender"/>
    </Logger>
    <Logger name="com.company.dao" level="INFO">
        <AppenderRef ref="DatabaseAppender"/>
    </Logger>

    <!-- High-performance async logger -->
    <AsyncLogger name="com.company.performance" level="TRACE" includeLocation="false">
        <AppenderRef ref="PerformanceAppender"/>
    </AsyncLogger>
</Loggers>
```

### Dynamic Log Level Control

During operation, configuration file changes can be automatically detected and applied through `monitorInterval` setting. Real-time level adjustment via JMX is also possible.

```
<Configuration status="WARN" monitorInterval="300">
    <!-- Check for configuration file changes every 5 minutes -->
</Configuration>
```

## 5. Log File Rolling Policies and Archiving

### Compound Rolling Policies

Combining time-based and size-based rolling enables efficient log management. Auto-compression and retention period settings optimize disk space.

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

### High-Performance RollingRandomAccessFile

**RollingRandomAccessFile** appender provides the best I/O performance by utilizing **BufferedIO** and **RandomAccessFile**. This approach is recommended for large-scale log processing.

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

## 6. Log Pattern Optimization

### Performance-Focused Pattern Design

Pattern elements are designed considering their performance impact. **Location information** (`%L`, `%M`, `%l`) carries high overhead and should be avoided in production environments. Enable **garbage-free logging** by activating thread locals.

| Pattern Element | Performance Impact | Usage |
| --- | --- | --- |
| `%d{HH:mm:ss.SSS}` | Low | Production |
| `%t` | Low | Thread identification |
| `%logger{1}` | Low | Class name (short) |
| `%L` | **High** | Development only |
| `%M` | **High** | Development only |
| `%l` | **Very High** | Avoid in async |

**Optimized Pattern Examples**:

```
<!-- Production: High performance -->
<PatternLayout pattern="%d{HH:mm:ss.SSS} %-5level - %msg%n"/>

<!-- Development: Detailed information -->
<PatternLayout pattern="%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-5level %logger{36}:%L - %msg%n"/>

<!-- Garbage-free optimization -->
<PatternLayout pattern="%d{DEFAULT} %-5p [%t] %c{1} - %m%n"/>
```

## 7. MDC Usage Methods

### MDC Implementation for Request Tracing

**MDC** (Mapped Diagnostic Context) stores context information per thread, enabling request tracing in distributed systems. Spring Boot automatically sets up and cleans up MDC through filters.

```
@Component
@Slf4j
public class RequestLoggingFilter implements Filter {

    @Override
    public void doFilter(ServletRequest request, ServletResponse response, 
                        FilterChain chain) throws IOException, ServletException {

        HttpServletRequest httpRequest = (HttpServletRequest) request;

        // Set MDC
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
            MDC.clear(); // Prevent memory leaks
        }
    }
}
```

### MDC Propagation in Async Environments

Implement **TaskDecorator** to propagate MDC context in async processing. Copy the parent thread's MDC to child threads during thread pool execution.

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

### MDC Pattern Usage

Utilize MDC values in log patterns to implement structured logging. Output in JSON format to optimize integration with log analysis tools.

```
<!-- Use MDC in pattern -->
<PatternLayout pattern="%d [%X{requestId}] [%X{userId}] %-5level %logger - %msg%n"/>

<!-- Output MDC in JSON format -->
<JsonTemplateLayout>
    <EventTemplateAdditionalField key="request_id" value="${mdc:requestId}"/>
    <EventTemplateAdditionalField key="user_id" value="${mdc:userId}"/>
    <EventTemplateAdditionalField key="session_id" value="${mdc:sessionId}"/>
</JsonTemplateLayout>
```

## 8. Production Environment Log Collection and Monitoring Integration

### ELK Stack Integration

For **Elasticsearch, Logstash, Kibana** stack integration, generate logs in JSON format with structured information. Use **JsonTemplateLayout** to output logs in ECS (Elastic Common Schema) compatible format.

```
<!-- JSON logs for ELK Stack -->
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

**ECS Compatible JSON Template**:

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

### Datadog APM Integration

For **Datadog APM** integration, extract trace IDs and span IDs from MDC and include them in logs. This connects distributed tracing and logs for complete observability.

```
<JsonTemplateLayout>
    <EventTemplateAdditionalField key="dd.trace_id" value="${mdc:dd.trace_id}"/>
    <EventTemplateAdditionalField key="dd.span_id" value="${mdc:dd.span_id}"/>
    <EventTemplateAdditionalField key="service" value="${env:DD_SERVICE}"/>
    <EventTemplateAdditionalField key="env" value="${env:DD_ENV}"/>
</JsonTemplateLayout>
```

### Kubernetes Environment Log Collection

Use the **sidecar pattern** to store logs in shared volumes, with a separate log collection container forwarding them to centralized logging systems.

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

## 9. Sensitive Data Masking for Security

### PII Data Masking Implementation

Protect **personally identifiable information** (PII) by implementing custom pattern converters to automatically mask emails, phone numbers, credit card numbers, etc.

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

### Policy-Based Filtering for Security

Use **RewritePolicy** to remove or mask specific fields in JSON structures. Implement comprehensive data protection strategies for GDPR and privacy law compliance.

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

### Security Best Practices

**JsonTemplateLayout** usage is recommended, guaranteeing safer output format than **PatternLayout**. When logging user-controlled input, use the **%encode** converter to prevent log injection attacks.

```
<!-- Use safe patterns -->
<PatternLayout pattern="%d [%t] %-5level %logger - %encode{%msg}{CRLF}%n"/>
```

## 10. Real-World Examples and Complete Configuration

### Complete Production Configuration

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN" monitorInterval="300">
    <Properties>
        <Property name="LOG_PATTERN">%d{yyyy-MM-dd HH:mm:ss.SSS} [%t] %-5level %logger{1} - %msg%n</Property>
        <Property name="LOG_DIR">${sys:log.dir:-logs}</Property>
    </Properties>

    <Appenders>
        <!-- Console - Only errors -->
        <Console name="Console" target="SYSTEM_OUT" direct="true">
            <PatternLayout pattern="${LOG_PATTERN}"/>
            <ThresholdFilter level="ERROR" onMatch="ACCEPT" onMismatch="DENY"/>
        </Console>

        <!-- High-performance application logs -->
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

        <!-- Error-only logs -->
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

        <!-- Performance monitoring logs -->
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
        <!-- Performance-critical async logger -->
        <AsyncLogger name="com.company.performance" level="INFO" includeLocation="false">
            <AppenderRef ref="PerfLog"/>
        </AsyncLogger>

        <!-- Application logger -->
        <AsyncLogger name="com.company" level="DEBUG" includeLocation="false">
            <AppenderRef ref="AppLog"/>
        </AsyncLogger>

        <!-- Framework loggers -->
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

### Application Code Implementation

```
@RestController
@Slf4j
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUser(@PathVariable Long id) {
        // Request tracing with MDC
        MDC.put("operation", "getUser");
        MDC.put("userId", id.toString());

        try {
            log.info("Starting user information lookup: {}", id);

            User user = userService.findById(id);
            log.debug("User lookup successful: {}", user.getName());

            return ResponseEntity.ok(user);
        } catch (UserNotFoundException e) {
            log.error("User not found: {}", id, e);
            return ResponseEntity.notFound().build();
        } catch (Exception e) {
            log.error("Unexpected error during user lookup", e);
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
        log.info("Creating new user: {}", userDto.getEmail());

        // Performance logging
        long startTime = System.currentTimeMillis();

        try {
            User user = userRepository.save(new User(userDto));

            long duration = System.currentTimeMillis() - startTime;
            log.info("User creation completed - ID: {}, Duration: {}ms", user.getId(), duration);

            return user;
        } catch (Exception e) {
            log.error("User creation failed: {}", userDto.getEmail(), e);
            throw new UserCreationException("Error during user creation", e);
        }
    }
}
```

### JVM Tuning Parameters

```
# JVM settings for optimal performance
-DLog4jContextSelector=org.apache.logging.log4j.core.async.AsyncLoggerContextSelector
-Dlog4j2.asyncLoggerRingBufferSize=1048576
-Dlog4j2.asyncLoggerWaitStrategy=Yield
-Dlog4j2.formatMsgAsync=true
-Dlog4j2.enableThreadLocals=true
-Dlog4j2.enableDirectEncoders=true

# GC optimization
-XX:+UseG1GC
-XX:MaxGCPauseMillis=200
-XX:+DisableExplicitGC
-XX:G1HeapRegionSize=16m
```

This comprehensive guide covers all core features of Log4j2 in Spring Boot, supporting optimized logging system construction at every stage from development to production. Simultaneously achieve **10-100x performance improvement through async logging**, **efficient monitoring through structured logging**, and **enhanced security through personal information protection**.

Core recommendations are as follows: Use AsyncLogger and JsonTemplateLayout in production, include detailed debugging information in development, leverage MDC for distributed tracing, and conduct regular security audits and performance monitoring.
