---
title: "Backend Development Standard Guide - Spring Boot 3, MySQL, MyBatis-Based"
date: 2025-04-23T18:23:51+09:00
slug: "562-Backend개발-표준-가이드-Spring-Boot-3-MySQL-MyBatis-기반"
original_url: "https://memoryhub.tistory.com/562"
tistory_id: 562
draft: false
categories: ["Dev Framework"]
tags: ["Spring"]
---

# I. Introduction

## A. Purpose and Scope

This document aims to define standards for backend application development using Spring Boot 3, MySQL, MyBatis technology stack, and Lombok library. These standard guidelines will enhance code consistency, readability, maintainability, and scalability, increase collaboration efficiency among team members, and minimize potential errors.

The scope covers all aspects of backend development including project structure, naming conventions, coding style, API design, database schema management, MyBatis usage, exception handling, and logging strategies. This standard is established based on official documentation for each technology stack, community best practices, and validated industry standards.

## B. Importance of Standards Compliance

Adhering to development standards goes beyond aesthetically improving code - it's an essential element for long-term project success. Consistent standards provide the following benefits:

1. **Improved Readability**: Unified style and naming conventions reduce time needed to understand code.
2. **Enhanced Maintainability**: Standardized structure and coding methods make maintenance tasks like bug fixes and feature additions easier.
3. **Increased Collaboration Efficiency**: When all team members follow the same rules, friction in code review and integration processes decreases, and productivity increases.
4. **Reduced Errors**: Verified best practices and clear guidelines help prevent potential design errors or implementation mistakes.
5. **Easier Adaptation of New Team Members**: Well-defined standards help new members quickly grasp project structure and codebase and contribute.

Therefore, it's very important that all team members understand and actively follow the standards defined in this document for project success.

# II. Project Structure and Naming Conventions

## A. Standard Directory Structure

Project structure should clearly show code organization and relationships between modules. It's good to follow the standard directory structure provided by build systems like Maven or Gradle. This helps new developers easily understand the structure when joining a project.

The basic directory structure is as follows:

```
src
├── main
│   ├── java                # Java source code root
│   │   └── com
│   │       └── example
│   │           └── projectname  # Top-level package
│   │               ├── ProjectnameApplication.java  # Spring Boot main application class
│   │               ├── config        # Configuration-related classes
│   │               ├── controller    # API request handling
│   │               ├── service       # Business logic implementation
│   │               ├── repository    # Data access
│   │               ├── domain        # Domain objects
│   │               ├── dto           # Data transfer objects
│   │               └── util          # Common utility classes
│   └── resources           # Resource file root
│       ├── static          # Static resources
│       ├── templates       # Template engine files
│       ├── mybatis         # MyBatis mapper XML files
│       │   └── mapper
│       ├── application.yml # Main configuration file
│       └── application-{profile}.yml # Profile-specific configuration files
└── test
    ├── java                # Test source code root
    │   └── com
    │       └── example
    │           └── projectname
    └── resources           # Test resource file root
        └── application-test.yml # Test configuration file
```

- **src/main/java**: Application's Java source code
- **src/main/resources**: Configuration files, static resources, MyBatis mapper XML files, etc. It's good to separate configuration files by environment (application-{profile}.yml).
- **src/test/java**: Unit and integration test code. Follows the same package structure as src/main/java.
- **src/test/resources**: Resource files needed for test execution

## B. Module Separation Criteria

For large projects, it's effective to separate modules based on functionality or domain. Each module should have an independent build unit with clearly defined dependencies. Spring Boot supports modularization and is particularly useful when multiple teams develop complex applications. Even when separating modules, consistently apply standard directory structure and package naming conventions within each module.

## C. Package Naming Conventions

Package name is an important element representing project structure. Clear and consistent package naming conventions help with code exploration and understanding.

- **Top-level Package**: Use company's reverse domain name (e.g., com.example.projectname). All classes should be located in this top-level package or its subpackages.
- **Package Name**: Use only lowercase letters and numbers, separated by dots (.). Don't use underscores (_) or uppercase letters.

### Package Composition Strategy

Package composition is divided into two main approaches:

#### 1. Package-by-Layer

Organize packages based on technical layers of the application. Suitable for small projects or microservices.

```
com.example.projectname
├── config
├── controller
├── service
├── repository
├── domain
└── dto
```

#### 2. Package-by-Feature

Organize packages based on main functionality or domain of the application. Each function package includes necessary layer components internally. Increases cohesion within functions and decreases coupling between functions, recommended for large-scale applications.

```
com.example.projectname
├── common          # Common utilities, base classes, etc.
├── user            # User management functionality
│   ├── controller
│   ├── service
│   ├── repository
│   ├── domain
│   └── dto
├── order           # Order management functionality
│   ├── controller
│   ├── service
│   ├── repository
│   ├── domain
│   └── dto
└── product         # Product management functionality
    ├── controller
    ├── service
    ├── repository
    ├── domain
    └── dto
```

Using package-by-feature:

- Each function is managed as an independent unit, minimizing impact of code changes on other functions
- If a specific function needs to be deleted, you only need to remove that package for easy maintenance
- Common elements are kept in a separate common package

### Selection Guide

It's important to choose either package-by-layer or package-by-feature strategy considering project size, complexity, and team preferences, and apply it consistently throughout the project.

## III. Java Code Conventions

### A. Naming Conventions

Meaningful and consistent naming greatly improves code readability. Based on Google Java Style Guide and Spring Framework Code Style.

### Classes

- **Use UpperCamelCase** (e.g., `Customer`, `OrderService`)
- Use nouns or noun phrases
- Spring components use appropriate suffixes for their role (`Controller`, `Service`, `Repository`, `Config`)
- Test classes have `Test` or `Tests` appended to target class name

### Interfaces

- **Use UpperCamelCase**
- Use nouns/noun phrases or adjectives/adjective phrases (e.g., `Runnable`, `Comparable`)
- Don't recommend `I` prefix (e.g., use `OrderService` instead of `IOrderService`)

### Methods

- **Use lowerCamelCase**
- Use verbs or verb phrases (e.g., `getUserById`, `processOrder`)
- Getter/Setter use `getFieldName`/`setFieldName` format
- Test methods can be distinguished with underscore (_) (e.g., `createUser_withValidData_shouldReturnCreatedUser`)

### Variables

- **Use lowerCamelCase**
- Communicate clear meaning (e.g., `customerName`, `orderList`)
- Avoid abbreviations, avoid single-letter names except for temporary variables
- Boolean variables recommended with `is`, `has` prefix (e.g., `isValid`, `hasPermission`)

### Constants

- **Use UPPER_SNAKE_CASE**
- Declare with `static final`
- Example: `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT_SECONDS`

## Lombok Usage Guidelines

Lombok is a useful library for reducing repetitive code, but should be used carefully.

### Recommended Annotations

- **@Getter / @Setter**

  - Avoid using `@Setter` for fields requiring immutability
  - Control access level if needed: `@Setter(AccessLevel.PROTECTED)`
- **Constructor-related**

  - **@NoArgsConstructor**: Default constructor (when needed for JPA Entity, etc.)
  - **@AllArgsConstructor**: Constructor including all fields
  - **@RequiredArgsConstructor**: Only includes `final`/`@NonNull` fields (recommended for constructor injection)
- **@ToString**

  - Exclude sensitive information/lazy-loaded fields: `@ToString(exclude = {"password"})`
- **@EqualsAndHashCode**

  - Don't use for JPA Entity (causes ID-based comparison issues)
  - When using for DTO/Value Object, specify comparison fields: `@EqualsAndHashCode(of = {"field1", "field2"})`

### Cautions

- **Avoid @Data**: While convenient, it automatically generates all annotations, making behavior unpredictable. Explicitly use only necessary annotations.
- **Immutability first**: Prefer final fields with @RequiredArgsConstructor for entity initialization rather than @Setter

## IV. API Design Standards

### A. RESTful API Principles

- **Resource-Centric**: Design endpoints around resources, not actions
- **Use Standard HTTP Methods**: GET (retrieve), POST (create), PUT (update), DELETE (delete)
- **Appropriate Status Codes**: Use meaningful HTTP status codes (200, 201, 400, 404, 500, etc.)
- **Consistent Naming**: Use plural nouns for collections (e.g., `/users`, `/orders`)

### B. API Response Format

Maintain a consistent response format for all APIs:

```java
{
  "success": true,
  "data": {
    "id": 1,
    "name": "John Doe"
  },
  "message": null,
  "timestamp": "2025-04-23T18:23:51Z"
}
```

Error response:

```java
{
  "success": false,
  "data": null,
  "message": "User not found",
  "timestamp": "2025-04-23T18:23:51Z"
}
```

### C. Pagination

Use consistent pagination parameters:

```
GET /api/users?page=1&size=10&sort=name,desc
```

Response should include pagination metadata:

```java
{
  "success": true,
  "data": [...],
  "pagination": {
    "page": 1,
    "size": 10,
    "totalElements": 100,
    "totalPages": 10
  }
}
```

## V. Database Schema Management

### A. Naming Conventions

- **Table Names**: Use snake_case, lowercase (e.g., `user_info`, `order_item`)
- **Column Names**: Use snake_case, lowercase (e.g., `user_id`, `created_at`)
- **Primary Key**: Always name as `id` or `<table>_id`
- **Foreign Key**: Name as `<referenced_table>_id`

### B. Essential Columns

Every table should have these columns:

```sql
CREATE TABLE user_info (
  id BIGINT PRIMARY KEY AUTO_INCREMENT,
  ...
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  deleted_at TIMESTAMP NULL DEFAULT NULL
);
```

- `id`: Primary key
- `created_at`: Record creation time
- `updated_at`: Last modification time
- `deleted_at`: Soft delete timestamp (NULL if not deleted)

### C. Indexing Strategy

- Create index on frequently searched columns
- Create index on foreign key columns
- Avoid excessive indexes that slow down write operations
- Regularly review and optimize indexes

## VI. MyBatis Usage Guide

### A. Mapper Configuration

- Keep SQL separate from Java code
- One mapper interface per entity/table
- Use parameterized queries to prevent SQL injection

Example mapper:

```java
@Mapper
public interface UserMapper {
  @Select("SELECT * FROM user_info WHERE id = #{id}")
  UserInfo findById(Long id);
  
  @Insert("INSERT INTO user_info (name, email) VALUES (#{name}, #{email})")
  @Options(useGeneratedKeys = true, keyProperty = "id")
  int insert(UserInfo userInfo);
  
  @Update("UPDATE user_info SET name = #{name} WHERE id = #{id}")
  int update(UserInfo userInfo);
  
  @Delete("DELETE FROM user_info WHERE id = #{id}")
  int deleteById(Long id);
}
```

### B. Dynamic SQL

Use MyBatis dynamic SQL for conditional queries:

```xml
<select id="findUsers" resultType="com.example.UserInfo">
  SELECT * FROM user_info
  <where>
    <if test="name != null">
      AND name LIKE CONCAT('%', #{name}, '%')
    </if>
    <if test="email != null">
      AND email = #{email}
    </if>
  </where>
  <if test="sort != null">
    ORDER BY ${sort}
  </if>
</select>
```

### C. Result Mapping

Map query results to objects:

```java
@Results({
  @Result(property = "id", column = "id"),
  @Result(property = "userName", column = "user_name"),
  @Result(property = "createdAt", column = "created_at")
})
@Select("SELECT * FROM user_info WHERE id = #{id}")
UserInfo findById(Long id);
```

## VII. Exception Handling

### A. Custom Exceptions

Create domain-specific exceptions:

```java
public class UserNotFoundException extends RuntimeException {
  public UserNotFoundException(String message) {
    super(message);
  }
  
  public UserNotFoundException(String message, Throwable cause) {
    super(message, cause);
  }
}
```

### B. Global Exception Handler

Use @ControllerAdvice for centralized exception handling:

```java
@ControllerAdvice
public class GlobalExceptionHandler {
  
  @ExceptionHandler(UserNotFoundException.class)
  public ResponseEntity<ApiResponse<Void>> handleUserNotFound(UserNotFoundException e) {
    ApiResponse<Void> response = new ApiResponse<>(
      false,
      null,
      e.getMessage(),
      LocalDateTime.now()
    );
    return ResponseEntity.status(HttpStatus.NOT_FOUND).body(response);
  }
  
  @ExceptionHandler(Exception.class)
  public ResponseEntity<ApiResponse<Void>> handleGenericException(Exception e) {
    ApiResponse<Void> response = new ApiResponse<>(
      false,
      null,
      "An error occurred",
      LocalDateTime.now()
    );
    return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).body(response);
  }
}
```

## VIII. Logging Strategy

### A. Logging Levels

- **DEBUG**: Detailed information for debugging
- **INFO**: General informational messages
- **WARN**: Warning messages for potentially problematic situations
- **ERROR**: Error messages for error events
- **FATAL**: Critical errors requiring immediate attention

### B. Logging Best Practices

```java
@Slf4j
@Service
public class UserService {
  
  public UserInfo getUserById(Long id) {
    log.debug("Fetching user with id: {}", id);
    
    Optional<UserInfo> user = userRepository.findById(id);
    if (user.isEmpty()) {
      log.warn("User not found with id: {}", id);
      throw new UserNotFoundException("User not found");
    }
    
    log.info("Successfully retrieved user: {}", user.get().getName());
    return user.get();
  }
}
```

### C. Performance Logging

Monitor performance-critical operations:

```java
@Aspect
@Component
public class PerformanceAspect {
  
  @Around("@annotation(com.example.annotation.Timed)")
  public Object logExecutionTime(ProceedingJoinPoint joinPoint) throws Throwable {
    long start = System.currentTimeMillis();
    Object proceed = joinPoint.proceed();
    long duration = System.currentTimeMillis() - start;
    
    log.info("Method {} took {} ms", joinPoint.getSignature(), duration);
    return proceed;
  }
}
```

## IX. Testing Standards

### A. Unit Testing

Test individual methods in isolation:

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
  
  @Mock
  UserRepository userRepository;
  
  @InjectMocks
  UserService userService;
  
  @Test
  void testGetUserById() {
    Long userId = 1L;
    UserInfo userInfo = new UserInfo(userId, "John Doe", "john@example.com");
    
    when(userRepository.findById(userId)).thenReturn(Optional.of(userInfo));
    
    UserInfo result = userService.getUserById(userId);
    
    assertThat(result).isNotNull();
    assertThat(result.getName()).isEqualTo("John Doe");
    verify(userRepository).findById(userId);
  }
}
```

### B. Integration Testing

Test interactions between components:

```java
@SpringBootTest
class UserControllerIntegrationTest {
  
  @Autowired
  MockMvc mockMvc;
  
  @Test
  void testGetUser() throws Exception {
    mockMvc.perform(get("/api/users/1"))
      .andExpect(status().isOk())
      .andExpect(jsonPath("$.success").value(true));
  }
}
```

## X. Security Best Practices

### A. Authentication and Authorization

- Use Spring Security for authentication
- Implement proper authorization checks
- Use method-level security with @PreAuthorize

```java
@Service
public class UserService {
  
  @PreAuthorize("hasRole('ADMIN')")
  public void deleteUser(Long id) {
    userRepository.deleteById(id);
  }
}
```

### B. Password Management

- Never store passwords in plain text
- Use BCryptPasswordEncoder for password hashing
- Implement password complexity requirements

### C. Input Validation

Always validate user input:

```java
@PostMapping("/users")
public ResponseEntity<ApiResponse<UserInfo>> createUser(
  @Valid @RequestBody CreateUserRequest request) {
  // Process request
}
```

## XI. Performance Optimization

### A. Query Optimization

- Use appropriate indexes
- Implement pagination for large result sets
- Use eager loading for related entities when needed
- Avoid N+1 query problems

### B. Caching

Implement caching for frequently accessed data:

```java
@Service
public class UserService {
  
  @Cacheable(value = "users", key = "#id")
  public UserInfo getUserById(Long id) {
    return userRepository.findById(id)
      .orElseThrow(UserNotFoundException::new);
  }
  
  @CacheEvict(value = "users", key = "#id")
  public void updateUser(Long id, UserInfo userInfo) {
    userRepository.save(userInfo);
  }
}
```

### C. Database Connection Pool

Configure appropriate connection pool settings:

```yml
spring:
  datasource:
    hikari:
      maximum-pool-size: 20
      minimum-idle: 5
      connection-timeout: 30000
      idle-timeout: 600000
      max-lifetime: 1800000
```

## XII. Conclusion

This standard guide provides comprehensive guidelines for backend development using Spring Boot 3, MySQL, and MyBatis. Adherence to these standards ensures code quality, maintainability, and team productivity. These guidelines should be reviewed and updated periodically to reflect new best practices and technologies.

The key to successful implementation is consistent application of these standards across all team members. Regular code reviews and discussions will help maintain and improve these standards over time.
