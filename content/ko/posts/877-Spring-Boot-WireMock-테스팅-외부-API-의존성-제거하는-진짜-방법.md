---
title: "Spring Boot WireMock 테스팅, 외부 API 의존성 제거하는 진짜 방법"
date: 2025-10-28T11:36:33+09:00
slug: "877-Spring-Boot-WireMock-테스팅-외부-API-의존성-제거하는-진짜-방법"
original_url: "https://memoryhub.tistory.com/877"
tistory_id: 877
draft: false
---

```
    ╔════════════════════════════════════╗
    ║   ? API → ? → ? → ✅ Test      ║
    ║                                    ║
    ║   External API (Not Available)    ║
    ║          ↓                         ║
    ║   WireMock Mock Server            ║
    ║          ↓                         ║
    ║   Your Spring Boot App            ║
    ║          ↓                         ║
    ║   ✅ Test Success                 ║
    ╚════════════════════════════════════╝
```

외부 API 호출하는 테스트 코드를 작성하다가 "서버 다운됐어요", "응답 시간 너무 오래 걸려요", "비용 청구돼요" 같은 문제로 고민해본 적 있으신가요? 실제 외부 API에 의존하는 테스트는 불안정하고 느리고 비용이 발생합니다.

WireMock은 이런 외부 API를 완벽하게 대체하는 Mock HTTP 서버를 제공하여 빠르고 안정적인 통합 테스트 환경을 만들어줍니다. 이 글에서는 2024년 12월에 공식 출시된 WireMock Spring Boot 통합을 활용하여 외부 API 의존성을 제거하고 독립적인 테스트 환경을 구축하는 실전 방법을 다룹니다.

> WireMock Spring Boot 통합은 외부 HTTP API를 Mock 서버로 대체하여 빠르고 안정적이며 독립적인 통합 테스트 환경을 구축할 수 있게 해주는 공식 라이브러리입니다.

## 배경

외부 API에 의존하는 Spring Boot 애플리케이션을 테스트할 때 실제 API를 호출하면 여러 문제가 발생합니다. 테스트가 외부 서버 상태에 종속되어 불안정하고, 응답 시간이 느려 전체 테스트 수행 시간이 길어지며, API 사용량에 따른 비용이 발생합니다. WireMock은 이런 문제를 해결하기 위해 HTTP Mock 서버를 제공하는 라이브러리입니다.

2024년 12월 6일, WireMock은 Maciej Walkowiak이 개발한 Spring Boot 통합을 공식 채택하여 Spring Boot 환경에서의 사용성을 대폭 개선했습니다.

### 문제 (Problem)

외부 API를 테스트하는 기존 방식들은 다음과 같은 한계가 있었습니다.

1. **실제 베타 API 호출:** 시스템에 부하를 주며, API 상태에 따라 테스트가 실패할 수 있습니다. 또한 타임아웃이나 장애 상황을 의도적으로 만들기 어렵습니다.
2. **Postman Mock:** API 호출 횟수 제한이 있습니다.
3. **Mockito (@MockBean):** FeignClient 같은 API 클라이언트 자체를 모킹(mocking)합니다. 이로 인해 클라이언트의 타임아웃 설정이나 404 에러 처리 등, API 호출과 관련된 로직을 검증할 수 없습니다.

### 해결 (Solution)

**WireMock**을 도입하여 실제 HTTP 호출을 흉내 내는 Mock 서버를 테스트 환경에 구성했습니다.

- **동작 방식:** JUnit 테스트가 실행될 때만 내장 서버로 동작합니다.
- **설정:**
  - spring-cloud-contract-wiremock 의존성을 추가합니다.
  - 테스트용 application.yml에서 API 호출 URL을 http://localhost:${wiremock.server.port}로 설정합니다.
  - src/testFixtures/resources/mappings 경로에 JSON 파일로 **stub**을 정의합니다.
- **Stub (JSON):** 어떤 request(메서드, URL, 헤더 등)가 오면 어떤 response(상태 코드, 바디, 딜레이 등)를 반환할지 미리 정의한 파일입니다.

### 활용 (Validation)

WireMock을 통해 기존에 어려웠던 다양한 시나리오를 테스트할 수 있습니다.

- **타임아웃 테스트:** 응답(response)에 fixedDelayMilliseconds를 설정하여, FeignClient의 Read Timeout이 정상 동작하는지 검증합니다.
- **기본 응답 설정:** priority (우선순위)를 낮게 설정하고 urlPathPattern (정규식)을 사용해, 특정 케이스 외의 모든 요청에 대해 기본 응답을 반환하도록 설정할 수 있습니다.
- **경로 충돌 해결:** 서로 다른 API가 동일한 URL 경로를 사용할 경우, 테스트 시에만 특정 \*\*헤더(header)\*\*를 추가하도록 설정하고, WireMock이 이 헤더를 구분하여 알맞은 응답을 주도록 설정합니다.

**주요 용어 정의**

| 용어 | 정의 | 사용 목적 |
| --- | --- | --- |
| WireMock | HTTP API를 Mocking하는 오픈소스 라이브러리 | 외부 API 호출을 시뮬레이션 |
| Stub | 미리 정의된 요청에 대한 응답 설정 | 특정 요청에 대한 고정 응답 반환 |
| Mock Server | 실제 서버처럼 동작하는 가짜 HTTP 서버 | 테스트 환경에서 외부 API 대체 |
| @EnableWireMock | WireMock 서버를 자동으로 시작하는 어노테이션 | Spring Boot 테스트에서 간편한 설정 |

## 핵심

WireMock Spring Boot 통합의 핵심 기능은 다음과 같습니다.

**동적 포트 자동 할당**

테스트 실행 시마다 WireMock 서버가 사용 가능한 포트를 자동으로 할당받아 포트 충돌 문제를 원천 차단합니다. 할당된 포트는 Spring Context의 프로퍼티로 노출되어 애플리케이션 설정에 주입할 수 있습니다.

**어노테이션 기반 선언적 설정**

@EnableWireMock 어노테이션만으로 WireMock 서버를 자동으로 시작하고 관리할 수 있습니다. 복잡한 보일러플레이트 코드 없이 간결하게 Mock 서버를 구성할 수 있습니다.

**여러 Mock 서버 인스턴스 지원**

하나의 테스트에서 여러 외부 API를 호출하는 경우, 각 API마다 독립된 WireMock 인스턴스를 생성하여 URL 스킴 충돌을 방지하고 명확한 테스트 환경을 구축할 수 있습니다.

**Spring Boot 3 완벽 호환**

최신 Spring Boot 3.x 버전과 Jakarta EE 전환에 완벽하게 대응하며, Jetty 12 기반으로 안정적으로 동작합니다.

## 실습

### 1. 의존성 추가

Spring Boot 프로젝트의 build.gradle 또는 pom.xml에 WireMock Spring Boot 의존성을 추가합니다.

**Gradle (build.gradle.kts)**

```
dependencies {
    // Spring Boot 3.x 사용 시
    testImplementation("org.wiremock.integrations:wiremock-spring-boot:3.9.0")

    // 또는 Spring Boot 3.x에서 Jetty 12 직접 사용
    testImplementation("org.wiremock:wiremock-jetty12:3.10.0")
}
```

**Maven (pom.xml)**

```
<dependency>
    <groupId>org.wiremock.integrations</groupId>
    <artifactId>wiremock-spring-boot</artifactId>
    <version>3.9.0</version>
    <scope>test</scope>
</dependency>
```

**버전 선택 가이드**

Spring Boot 2.x를 사용하는 경우 com.github.tomakehurst:wiremock:2.27.2를 사용하고, Spring Boot 3.x를 사용하는 경우 위의 최신 버전을 사용해야 합니다. Spring Boot 3는 Jakarta EE로 전환되었기 때문에 기존 javax 패키지 기반 WireMock 구버전은 NoClassDefFoundError를 발생시킵니다.

### 2. 기본 테스트 작성

가장 간단한 WireMock 테스트를 작성합니다.

```
@SpringBootTest(
    webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT,
    classes = MyApplication.class
)
@EnableWireMock
class SimpleWireMockTest {

    @Value("${wiremock.server.baseUrl}")
    private String wireMockBaseUrl;

    @Autowired
    private TestRestTemplate restTemplate;

    @Test
    void testExternalApiCall() {
        // Stub 설정: GET /api/users 요청 시 JSON 응답 반환
        stubFor(get("/api/users")
            .willReturn(okJson("[{\"id\":1,\"name\":\"Alice\"}]")));

        // 테스트 실행
        String url = wireMockBaseUrl + "/api/users";
        ResponseEntity<String> response = restTemplate.getForEntity(url, String.class);

        // 검증
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertTrue(response.getBody().contains("Alice"));
    }
}
```

위 코드에서 @EnableWireMock 어노테이션이 WireMock 서버를 자동으로 시작하고, ${wiremock.server.baseUrl} 프로퍼티를 통해 동적으로 할당된 서버 URL을 주입받습니다.

### 3. 여러 Mock 서버 사용

실무에서는 여러 외부 API를 호출하는 경우가 많습니다. 각 API마다 독립된 WireMock 인스턴스를 생성합니다.

```
@SpringBootTest(
    webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT,
    classes = MyApplication.class
)
@EnableWireMock({
    @ConfigureWireMock(name = "user-service", port = 8081),
    @ConfigureWireMock(name = "payment-service", port = 8082)
})
class MultipleWireMockTest {

    @InjectWireMock("user-service")
    private WireMockServer userServiceMock;

    @InjectWireMock("payment-service")
    private WireMockServer paymentServiceMock;

    @Test
    void testMultipleServices() {
        // User Service Stub
        userServiceMock.stubFor(get("/users/1")
            .willReturn(okJson("{\"id\":1,\"name\":\"Alice\"}")));

        // Payment Service Stub
        paymentServiceMock.stubFor(post("/payments")
            .willReturn(okJson("{\"status\":\"success\"}")));

        // 테스트 로직...
    }
}
```

각 Mock 서버에 고유한 이름과 포트를 지정하고, @InjectWireMock 어노테이션으로 필드에 주입받아 독립적으로 Stub을 설정할 수 있습니다.

### 4. 에러 시나리오 테스트

외부 API 장애 상황을 시뮬레이션하여 애플리케이션의 에러 처리 로직을 검증합니다.

```
@Test
void testApiTimeout() {
    // 5초 지연 응답 설정
    stubFor(get("/api/data")
        .willReturn(aResponse()
            .withFixedDelay(5000)
            .withStatus(200)));

    // Timeout 예외 검증
    assertThrows(ResourceAccessException.class, () -> {
        restTemplate.getForEntity(wireMockBaseUrl + "/api/data", String.class);
    });
}

@Test
void testApiServerError() {
    // 500 에러 응답 설정
    stubFor(get("/api/data")
        .willReturn(aResponse()
            .withStatus(500)
            .withBody("Internal Server Error")));

    ResponseEntity<String> response = 
        restTemplate.getForEntity(wireMockBaseUrl + "/api/data", String.class);

    assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, response.getStatusCode());
}
```

실제 외부 API에서는 재현하기 어려운 타임아웃, 서버 에러, 네트워크 장애 등의 상황을 WireMock으로 손쉽게 시뮬레이션할 수 있습니다.

### 5. 요청 검증

WireMock은 애플리케이션이 올바른 요청을 보냈는지 검증할 수 있습니다.

```
@Test
void testRequestVerification() {
    stubFor(post("/api/users")
        .withHeader("Content-Type", equalTo("application/json"))
        .withRequestBody(containing("\"email\""))
        .willReturn(okJson("{\"id\":2,\"status\":\"created\"}")));

    // 애플리케이션 로직 실행
    restTemplate.postForEntity(
        wireMockBaseUrl + "/api/users",
        new User("alice@example.com"),
        String.class
    );

    // 요청이 정확히 1번 호출되었는지 검증
    verify(exactly(1), postRequestedFor(urlEqualTo("/api/users"))
        .withHeader("Content-Type", equalTo("application/json")));
}
```

## 모범사례 및 패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **어노테이션 기반 (@EnableWireMock)** | 간결한 설정, 자동 리소스 관리, Spring Context 통합 | Spring Boot 환경에서만 사용 가능 |
| **Plain Java (WireMockServer)** | 프레임워크 독립적, 세밀한 제어 가능 | 수동으로 서버 시작/종료 관리 필요, 보일러플레이트 코드 증가 |
| **Testcontainers WireMock** | Docker 기반 격리된 환경, 실제 배포 환경과 유사 | Docker 실행 환경 필요, 테스트 실행 시간 증가 |
| **파일 기반 Stub (JSON)** | 재사용 가능, 버전 관리 용이, 팀 간 공유 쉬움 | 초기 설정 복잡, 동적 응답 처리 제한적 |
| **Record & Playback** | 실제 API 응답 기록 후 재생, 정확한 응답 보장 | 초기 실제 API 호출 필요, 민감 데이터 처리 주의 |

**권장 사항**

Spring Boot 프로젝트에서는 @EnableWireMock 어노테이션 기반 패턴을 우선 사용하고, 복잡한 시나리오나 여러 외부 API를 동시에 테스트하는 경우 여러 인스턴스를 활용합니다. 반복적으로 사용되는 Stub 설정은 파일 기반으로 관리하여 재사용성을 높이고, 민감한 데이터가 포함되지 않도록 주의합니다.

## 마치며

WireMock Spring Boot 통합은 외부 API에 의존하는 애플리케이션의 테스트를 독립적이고 안정적으로 만들어줍니다. 동적 포트 할당으로 포트 충돌 문제를 해결하고, 어노테이션 기반 설정으로 간결한 테스트 코드를 작성할 수 있습니다. 여러 Mock 서버 인스턴스를 활용하면 복잡한 외부 의존성도 명확하게 테스트할 수 있습니다.

실전에서는 테스트 실행 속도 향상과 외부 API 비용 절감 효과를 직접 체감할 수 있으며, CI/CD 파이프라인에서도 안정적으로 동작합니다.

## 참고자료

- WireMock Now Has an Official Spring Boot Integration (<https://www.wiremock.io/post/wiremock-now-has-an-official-spring-boot-integration>)
- WireMock Spring Boot Integration 공식 문서 (<https://wiremock.org/docs/spring-boot/>)
- Integrating WireMock with Spring Boot - Baeldung (<https://www.baeldung.com/spring-boot-wiremock>)
- GitHub - wiremock/wiremock-spring-boot (<https://github.com/wiremock/wiremock-spring-boot>)
- Testing REST API integrations using WireMock - Testcontainers (<https://testcontainers.com/guides/testing-rest-api-integrations-using-wiremock/>)
- <https://techblog.woowahan.com/17674/>
