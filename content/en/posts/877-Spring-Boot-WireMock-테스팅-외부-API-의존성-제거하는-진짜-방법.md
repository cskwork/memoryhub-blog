---
title: "Spring Boot WireMock Testing: The Real Way to Remove External API Dependencies"
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

Have you ever struggled writing test code that calls external APIs with issues like "the server is down," "response time is too slow," or "charges are being incurred"? Tests that depend on actual external APIs are unreliable, slow, and costly.

WireMock provides a mock HTTP server that perfectly replaces external APIs, creating fast and stable integration test environments. This article covers the practical method of using the WireMock Spring Boot integration officially released in December 2024 to eliminate external API dependencies and build independent test environments.

> WireMock Spring Boot integration is an official library that allows you to replace external HTTP APIs with mock servers, enabling you to build fast, stable, and independent integration test environments.

## Background

When testing Spring Boot applications that call external APIs, using real APIs introduces multiple issues. Tests become unstable depending on external server status, response times are slow making overall test execution lengthy, and API usage incurs costs. WireMock solves these problems by providing an HTTP mock server library.

On December 6, 2024, WireMock officially adopted Spring Boot integration developed by Maciej Walkowiak, significantly improving usability in Spring Boot environments.

### Problem

Existing approaches to testing external APIs have the following limitations:

1. **Calling Real Beta APIs:** This puts load on the system and tests may fail depending on API status. Additionally, it's difficult to intentionally create timeout or failure situations.
2. **Postman Mock:** Has API call number limitations.
3. **Mockito (@MockBean):** Mocks the API client itself like FeignClient. This prevents validating API call-related logic such as client timeout settings or 404 error handling.

### Solution

We introduce **WireMock** to configure a mock server that simulates actual HTTP calls in the test environment.

- **How it works:** Operates as an embedded server only when JUnit tests run.
- **Configuration:**
  - Add the spring-cloud-contract-wiremock dependency.
  - In test application.yml, set the API call URL to http://localhost:${wiremock.server.port}.
  - Define **stubs** as JSON files in the src/testFixtures/resources/mappings path.
- **Stub (JSON):** A file predefined with what response (status code, body, delay, etc.) to return when a certain request (method, URL, headers, etc.) arrives.

### Validation

WireMock enables testing of various scenarios that were previously difficult:

- **Timeout testing:** Set fixedDelayMilliseconds in the response to validate that FeignClient's Read Timeout works correctly.
- **Default response setting:** Set low priority and use urlPathPattern (regex) so all requests except specific cases return a default response.
- **Resolving path conflicts:** When different APIs use identical URL paths, add a specific **header** only during tests, and configure WireMock to distinguish the header and return the appropriate response.

**Key Term Definitions**

| Term | Definition | Purpose |
| --- | --- | --- |
| WireMock | Open-source library for mocking HTTP APIs | Simulate external API calls |
| Stub | Predefined response settings for requests | Return fixed response for specific requests |
| Mock Server | Fake HTTP server behaving like a real server | Replace external API in test environment |
| @EnableWireMock | Annotation automatically starting WireMock server | Convenient configuration in Spring Boot tests |

## Core Concept

The core features of WireMock Spring Boot integration are as follows:

**Dynamic Port Auto-Assignment**

Each test execution assigns WireMock server an available port automatically, preventing port conflicts. The assigned port is exposed as a Spring Context property and can be injected into application configuration.

**Annotation-Based Declarative Configuration**

Simply using the @EnableWireMock annotation automatically starts and manages the WireMock server. You can construct mock servers concisely without complex boilerplate code.

**Multiple Mock Server Instance Support**

When a single test calls multiple external APIs, create independent WireMock instances for each API, preventing URL scheme conflicts and establishing clear test environments.

**Complete Spring Boot 3 Compatibility**

Perfectly compatible with the latest Spring Boot 3.x versions and Jakarta EE transition, running stably on Jetty 12 basis.

## Practice

### 1. Add Dependencies

Add WireMock Spring Boot dependencies to your Spring Boot project's build.gradle or pom.xml.

**Gradle (build.gradle.kts)**

```groovy
dependencies {
    // For Spring Boot 3.x
    testImplementation("org.wiremock.integrations:wiremock-spring-boot:3.9.0")

    // Or for Spring Boot 3.x using Jetty 12 directly
    testImplementation("org.wiremock:wiremock-jetty12:3.10.0")
}
```

**Maven (pom.xml)**

```xml
<dependency>
    <groupId>org.wiremock.integrations</groupId>
    <artifactId>wiremock-spring-boot</artifactId>
    <version>3.9.0</version>
    <scope>test</scope>
</dependency>
```

**Version Selection Guide**

For Spring Boot 2.x, use com.github.tomakehurst:wiremock:2.27.2. For Spring Boot 3.x, use the latest version above. Spring Boot 3 has transitioned to Jakarta EE, so older WireMock versions based on javax packages will cause NoClassDefFoundError.

### 2. Write Basic Test

Write the simplest WireMock test:

```java
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
        // Stub setting: Return JSON when GET /api/users requested
        stubFor(get("/api/users")
            .willReturn(okJson("[{\"id\":1,\"name\":\"Alice\"}]")));

        // Execute test
        String url = wireMockBaseUrl + "/api/users";
        ResponseEntity<String> response = restTemplate.getForEntity(url, String.class);

        // Verify
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertTrue(response.getBody().contains("Alice"));
    }
}
```

The @EnableWireMock annotation automatically starts the WireMock server in the above code, and the dynamically assigned server URL is injected through the ${wiremock.server.baseUrl} property.

### 3. Use Multiple Mock Servers

In real-world scenarios, you often call multiple external APIs. Create independent WireMock instances for each API:

```java
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

        // Test logic...
    }
}
```

Assign unique names and ports to each mock server and inject them into fields via @InjectWireMock annotations to independently configure stubs for each.

### 4. Test Error Scenarios

Simulate external API failure situations to verify your application's error handling logic:

```java
@Test
void testApiTimeout() {
    // Set 5-second delayed response
    stubFor(get("/api/data")
        .willReturn(aResponse()
            .withFixedDelay(5000)
            .withStatus(200)));

    // Verify Timeout exception
    assertThrows(ResourceAccessException.class, () -> {
        restTemplate.getForEntity(wireMockBaseUrl + "/api/data", String.class);
    });
}

@Test
void testApiServerError() {
    // Set 500 error response
    stubFor(get("/api/data")
        .willReturn(aResponse()
            .withStatus(500)
            .withBody("Internal Server Error")));

    ResponseEntity<String> response = 
        restTemplate.getForEntity(wireMockBaseUrl + "/api/data", String.class);

    assertEquals(HttpStatus.INTERNAL_SERVER_ERROR, response.getStatusCode());
}
```

With WireMock, you can easily simulate timeout, server error, and network failure situations that are difficult to reproduce with real external APIs.

### 5. Request Verification

WireMock can verify that your application sends correct requests:

```java
@Test
void testRequestVerification() {
    stubFor(post("/api/users")
        .withHeader("Content-Type", equalTo("application/json"))
        .withRequestBody(containing("\"email\""))
        .willReturn(okJson("{\"id\":2,\"status\":\"created\"}")));

    // Execute application logic
    restTemplate.postForEntity(
        wireMockBaseUrl + "/api/users",
        new User("alice@example.com"),
        String.class
    );

    // Verify the request was called exactly once
    verify(exactly(1), postRequestedFor(urlEqualTo("/api/users"))
        .withHeader("Content-Type", equalTo("application/json")));
}
```

## Best Practices and Pattern Comparison

| Pattern | Advantages | Notes |
| --- | --- | --- |
| **Annotation-Based (@EnableWireMock)** | Clean configuration, automatic resource management, Spring Context integration | Available only in Spring Boot environment |
| **Plain Java (WireMockServer)** | Framework-independent, fine-grained control possible | Manual server start/stop management required, boilerplate code increases |
| **Testcontainers WireMock** | Docker-based isolated environment, similar to actual deployment | Docker runtime required, test execution time increases |
| **File-Based Stub (JSON)** | Reusable, version control friendly, easy team sharing | Complex initial setup, limited dynamic response handling |
| **Record & Playback** | Record real API responses then replay, guarantees accurate responses | Requires initial real API calls, careful handling of sensitive data |

**Recommendations**

In Spring Boot projects, prioritize the @EnableWireMock annotation-based pattern and leverage multiple instances for complex scenarios with multiple external APIs. Manage repeatedly used stub configurations as files to increase reusability while being careful not to include sensitive data.

## Conclusion

WireMock Spring Boot integration makes testing applications that call external APIs independent and stable. Dynamic port assignment solves port conflict issues, and annotation-based configuration enables concise test code writing. Leveraging multiple mock server instances allows you to test even complex external dependencies clearly.

In practice, you can directly experience improved test execution speed and reduced external API costs, and it operates reliably in CI/CD pipelines.

## References

- WireMock Now Has an Official Spring Boot Integration (<https://www.wiremock.io/post/wiremock-now-has-an-official-spring-boot-integration>)
- WireMock Spring Boot Integration Official Documentation (<https://wiremock.org/docs/spring-boot/>)
- Integrating WireMock with Spring Boot - Baeldung (<https://www.baeldung.com/spring-boot-wiremock>)
- GitHub - wiremock/wiremock-spring-boot (<https://github.com/wiremock/wiremock-spring-boot>)
- Testing REST API integrations using WireMock - Testcontainers (<https://testcontainers.com/guides/testing-rest-api-integrations-using-wiremock/>)
- <https://techblog.woowahan.com/17674/>
