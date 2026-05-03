---
title: "Spring Boot + JWT + Spring Security - Complete Mastery of Secure Authentication and File Upload"
date: 2025-04-05T13:24:23+09:00
slug: "544-Spring-Boot-JWT-Spring-Security-안전한-인증과-파일-업로드-완전-정복"
original_url: "https://memoryhub.tistory.com/544"
tistory_id: 544
draft: false
---

Hello! In modern web applications and API development, **JWT (JSON Web Token)**, a stateless authentication method, has become almost a standard due to its scalability and flexibility in microservices architecture (MSA) environments. In this post, I'll show you in detail through actual code how to effectively integrate the powerful security framework **Spring Security** with **JWT** in a **Spring Boot** environment, and how to implement secure file uploads for authenticated users only.

This guide targets those with basic knowledge of Spring Boot and Spring Security, aiming to be a practical guide that can be applied directly to actual projects. So, let's get started!

```
+-------------+    1. Login Request     +----------------+  
|   Client    | --------------------> |   Spring Boot   |  
+-------------+                      |   Application   |  
       ^                                |    +----------------+  
       |                                     |  
       |                                     v  
       |                               +-----------+  
       |                               | Database  |  
       |                               +-----------+  
       |                                     |  
       |         2. JWT Token Issued         |  
       <------------------------------------|  


+-------------+    3. API + JWT         +----------------+     +------------------+  
|   Client    | --------------------> |   Spring Boot   | --> | SecurityContext  |  
+-------------+                      |   Application   |     +------------------+  
       ^                                |    +----------------+  |  
       |                                     |  
       |         4. Response                 |  
       <------------------------------------|
```

## 1. Project Setup and Adding Dependencies: Getting Off on the Right Foot

Every development begins with configuration! Create a Spring Boot project and add the necessary libraries, or dependencies. If you're using Gradle, add the following to your `build.gradle` file. (Dependency version management is always important, so get in the habit of checking compatibility for your project environment!)

```
// build.gradle

plugins {
    id 'java'
    id 'org.springframework.boot' version '3.2.4'
    id 'io.spring.dependency-management' version '1.1.4'
}

group = 'com.example'
version = '0.0.1-SNAPSHOT'

java {
    sourceCompatibility = '17'
}

configurations {
    compileOnly {
        extendsFrom annotationProcessor
    }
}

repositories {
    mavenCentral()
}

dependencies {
    // Spring Boot Starters
    implementation 'org.springframework.boot:spring-boot-starter-web'
    implementation 'org.springframework.boot:spring-boot-starter-security'
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
    implementation 'org.springframework.boot:spring-boot-starter-validation'

    // JWT Library (jjwt)
    implementation 'io.jsonwebtoken:jjwt-api:0.11.5'
    runtimeOnly 'io.jsonwebtoken:jjwt-impl:0.11.5'
    runtimeOnly 'io.jsonwebtoken:jjwt-jackson:0.11.5'

    // Database Driver
    runtimeOnly 'com.h2database:h2'

    // Lombok
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'

    // Spring Boot Test
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    testImplementation 'org.springframework.security:spring-security-test'
}

tasks.named('test') {
    useJUnitPlatform()
}
```

The core dependencies are `spring-boot-starter-web`, `spring-boot-starter-security`, `spring-boot-starter-data-jpa`, and the `jjwt` library for JWT processing.

## 2. JWT and Application Configuration: Setting Up the Environment

Manage JWT token generation and validation core elements like secret keys and expiration times in a configuration file (`application.yml` or `application.properties`).

```
# src/main/resources/application.yml

spring:
  datasource:
    url: jdbc:h2:mem:testdb
    driverClassName: org.h2.Driver
    username: sa
    password:
  jpa:
    database-platform: org.hibernate.dialect.H2Dialect
    hibernate:
      ddl-auto: update
    show-sql: true

# JWT Configuration
app:
  jwt:
    # CRITICAL: Never hardcode this value in actual production!
    # Use environment variables, external config files, Vault, AWS Secrets Manager, etc.
    secret-key: VmVyeVNlY3JldEtleUZvckpXVEF1dGhlbnRpY2F0aW9uYW5kQXV0aG9yaXphdGlvblNlcnZpY2U=
    expiration-ms: 3600000 # Token expiration (milliseconds, e.g., 1 hour)
```

**Emphasizing again: `app.jwt.secret-key` is very sensitive information.** If leaked, token tampering becomes possible, so it must be managed securely. Always use environment variables or cloud provider secret management services. Configure the expiration time (`expiration-ms`) appropriately considering your service's security policy and user convenience.

## 3. User Information Modeling: Who Is Who?

Define an entity class to hold user information so Spring Security can recognize users and manage authorities. This class must implement Spring Security's `UserDetails` interface.

```java
// src/main/java/com/example/demo/user/User.java
package com.example.demo.user;

import jakarta.persistence.*;
import lombok.AccessLevel;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;

@Entity
@Table(name = "users")
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class User implements UserDetails {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String username;

    @Column(nullable = false)
    private String password;

    @ElementCollection(fetch = FetchType.EAGER)
    @CollectionTable(name = "user_roles", joinColumns = @JoinColumn(name = "user_id"))
    @Column(name = "role")
    private List<String> roles = new java.util.ArrayList<>();

    @Builder
    public User(String username, String password, List<String> roles) {
        this.username = username;
        this.password = password;
        this.roles = roles;
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        return this.roles.stream()
                .map(SimpleGrantedAuthority::new)
                .collect(Collectors.toList());
    }

    @Override
    public String getPassword() {
        return this.password;
    }

    @Override
    public String getUsername() {
        return this.username;
    }

    @Override
    public boolean isAccountNonExpired() { return true; }

    @Override
    public boolean isAccountNonLocked() { return true; }

    @Override
    public boolean isCredentialsNonExpired() { return true; }

    @Override
    public boolean isEnabled() { return true; }
}
```

User entity interactions with the database occur through Spring Data JPA repository interfaces:

```java
// src/main/java/com/example/demo/user/UserRepository.java
package com.example.demo.user;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByUsername(String username);
}
```

## 4. User Information Loading Service: The Starting Point of Authentication

When Spring Security handles login requests, a `UserDetailsService` implementation is needed to tell it where and how to retrieve actual user information.

```java
// src/main/java/com/example/demo/security/UserDetailsServiceImpl.java
package com.example.demo.security;

import com.example.demo.user.User;
import com.example.demo.user.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class UserDetailsServiceImpl implements UserDetailsService {

    private final UserRepository userRepository;

    @Override
    @Transactional(readOnly = true)
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new UsernameNotFoundException("User not found: " + username));

        return user;
    }
}
```

## 5. JWT Token Processing Utility: Token Wizard

Gather and manage all core logic related to tokens - token generation, validation, and information extraction:

```java
// src/main/java/com/example/demo/security/JwtTokenProvider.java
package com.example.demo.security;

import io.jsonwebtoken.*;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import io.jsonwebtoken.security.SecurityException;
import jakarta.annotation.PostConstruct;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.util.Date;
import java.util.stream.Collectors;

@Component
@Slf4j
public class JwtTokenProvider {

    @Value("${app.jwt.secret-key}")
    private String secretKeyValue;

    @Value("${app.jwt.expiration-ms}")
    private long jwtExpirationInMs;

    private SecretKey secretKey;

    private static final String AUTHORITIES_KEY = "auth";

    @PostConstruct
    public void init() {
        byte[] keyBytes = Decoders.BASE64.decode(secretKeyValue);
        this.secretKey = Keys.hmacShaKeyFor(keyBytes);
    }

    public String generateToken(Authentication authentication) {
        String authorities = authentication.getAuthorities().stream()
                .map(GrantedAuthority::getAuthority)
                .collect(Collectors.joining(","));

        long now = (new Date()).getTime();
        Date validity = new Date(now + this.jwtExpirationInMs);

        return Jwts.builder()
                .setSubject(authentication.getName())
                .claim(AUTHORITIES_KEY, authorities)
                .setIssuedAt(new Date())
                .setExpiration(validity)
                .signWith(secretKey, SignatureAlgorithm.HS512)
                .compact();
    }

    public Authentication getAuthentication(String token) {
        Claims claims = Jwts.parserBuilder()
                .setSigningKey(secretKey)
                .build()
                .parseClaimsJws(token)
                .getBody();

        String username = claims.getSubject();
        String[] authorities = claims.get(AUTHORITIES_KEY, String.class).split(",");

        UserDetails userDetails = org.springframework.security.core.userdetails.User.builder()
                .username(username)
                .password("")
                .authorities(authorities)
                .build();

        return new UsernamePasswordAuthenticationToken(userDetails, token, userDetails.getAuthorities());
    }

    public boolean validateToken(String token) {
        try {
            Jwts.parserBuilder().setSigningKey(secretKey).build().parseClaimsJws(token);
            return true;
        } catch (SecurityException | MalformedJwtException e) {
            log.info("Invalid JWT signature.");
        } catch (ExpiredJwtException e) {
            log.info("Expired JWT token.");
        } catch (UnsupportedJwtException e) {
            log.info("Unsupported JWT token.");
        } catch (IllegalArgumentException e) {
            log.info("Invalid JWT token.");
        }
        return false;
    }

    public String getUsernameFromToken(String token) {
        Claims claims = Jwts.parserBuilder()
                .setSigningKey(secretKey)
                .build()
                .parseClaimsJws(token)
                .getBody();
        return claims.getSubject();
    }
}
```

## 6. Spring Security Configuration: Setting the Security Framework

Now write the core configuration class (`SecurityConfig`) that defines how Spring Security operates. Configure HTTP request handling rules, session management, CORS, JWT filter integration, and more here:

```java
// src/main/java/com/example/demo/config/SecurityConfig.java
package com.example.demo.config;

import com.example.demo.security.JwtAuthenticationFilter;
import com.example.demo.security.JwtTokenProvider;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;

import java.util.Arrays;
import java.util.List;

@Configuration
@EnableWebSecurity
@EnableMethodSecurity(securedEnabled = true, prePostEnabled = true)
@RequiredArgsConstructor
public class SecurityConfig {

    private final JwtTokenProvider jwtTokenProvider;

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration) throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }

    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration configuration = new CorsConfiguration();
        configuration.setAllowedOrigins(List.of("http://localhost:8081", "http://your-frontend-domain.com"));
        configuration.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"));
        configuration.setAllowedHeaders(Arrays.asList("Authorization", "Cache-Control", "Content-Type"));
        configuration.setAllowCredentials(true);
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", configuration);
        return source;
    }

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                .csrf(AbstractHttpConfigurer::disable)
                .cors(cors -> cors.configurationSource(corsConfigurationSource()))
                .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
                .authorizeHttpRequests(authz -> authz
                        .requestMatchers("/api/auth/**").permitAll()
                        .requestMatchers("/api/files/upload").authenticated()
                        .anyRequest().authenticated()
                )
                .addFilterBefore(new JwtAuthenticationFilter(jwtTokenProvider), UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }
}
```

## 7. JWT Authentication Filter: Request Checkpoint

Every HTTP request passes through this gateway before reaching the controller. It finds JWT in the request header, validates it, and if valid, sets authentication information in the Security Context so that subsequent logic can access authenticated user information through `@AuthenticationPrincipal`:

```java
// src/main/java/com/example/demo/security/JwtAuthenticationFilter.java
package com.example.demo.security;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.util.StringUtils;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;

@RequiredArgsConstructor
@Slf4j
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    private final JwtTokenProvider jwtTokenProvider;
    public static final String AUTHORIZATION_HEADER = "Authorization";
    public static final String BEARER_PREFIX = "Bearer ";

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

        String jwt = resolveToken(request);
        String requestURI = request.getRequestURI();

        if (StringUtils.hasText(jwt) && jwtTokenProvider.validateToken(jwt)) {
            Authentication authentication = jwtTokenProvider.getAuthentication(jwt);
            SecurityContextHolder.getContext().setAuthentication(authentication);
            log.debug("Successfully set authentication in Security Context for '{}', uri: {}", authentication.getName(), requestURI);
        } else {
            log.debug("No valid JWT token found, uri: {}", requestURI);
        }

        filterChain.doFilter(request, response);
    }

    private String resolveToken(HttpServletRequest request) {
        String bearerToken = request.getHeader(AUTHORIZATION_HEADER);
        if (StringUtils.hasText(bearerToken) && bearerToken.startsWith(BEARER_PREFIX)) {
            return bearerToken.substring(BEARER_PREFIX.length());
        }
        return null;
    }
}
```

## 8. Authentication Endpoint Controller: Login & Token Issuance

This is the API endpoint where users attempt to log in with username and password, and on success, a JWT is issued:

```java
// src/main/java/com/example/demo/auth/AuthController.java
package com.example.demo.auth;

import com.example.demo.security.JwtAuthenticationFilter;
import com.example.demo.security.JwtTokenProvider;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {

    private final AuthenticationManager authenticationManager;
    private final JwtTokenProvider jwtTokenProvider;

    @PostMapping("/login")
    public ResponseEntity<JwtAuthenticationResponse> authenticateUser(@Valid @RequestBody LoginRequest loginRequest) {

        UsernamePasswordAuthenticationToken authenticationToken =
                new UsernamePasswordAuthenticationToken(loginRequest.getUsername(), loginRequest.getPassword());

        Authentication authentication = authenticationManager.authenticate(authenticationToken);

        SecurityContextHolder.getContext().setAuthentication(authentication);

        String jwt = jwtTokenProvider.generateToken(authentication);

        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.add(JwtAuthenticationFilter.AUTHORIZATION_HEADER, JwtAuthenticationFilter.BEARER_PREFIX + jwt);

        return new ResponseEntity<>(new JwtAuthenticationResponse(jwt), httpHeaders, HttpStatus.OK);
    }

    @lombok.Data
    public static class LoginRequest {
        @jakarta.validation.constraints.NotBlank(message = "Username is required.")
        private String username;

        @jakarta.validation.constraints.NotBlank(message = "Password is required.")
        private String password;
    }

    @lombok.Getter
    @lombok.RequiredArgsConstructor
    public static class JwtAuthenticationResponse {
        private final String accessToken;
        private final String tokenType = "Bearer";
    }
}
```

## 9. Secure File Upload Controller: Authenticated Users Only!

Now that `authenticated()` access control is set in `SecurityConfig`, only users with valid JWT can call this file upload API:

```java
// src/main/java/com/example/demo/file/FileUploadController.java
package com.example.demo.file;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.UUID;

@RestController
@RequestMapping("/api/files")
@Slf4j
public class FileUploadController {

    @Value("${app.upload.dir:${user.home}/uploads}")
    private String uploadDir;

    @PostMapping("/upload")
    public ResponseEntity<String> uploadFile(
            @RequestParam("file") MultipartFile file,
            @AuthenticationPrincipal UserDetails userDetails
    ) {
        if (userDetails == null) {
            log.warn("File upload attempt without authentication.");
        } else {
            log.info("File upload request from user: {}", userDetails.getUsername());
        }

        if (file.isEmpty()) {
            return ResponseEntity.badRequest().body("Please select a file to upload.");
        }

        try {
            Path uploadPath = Paths.get(uploadDir);

            if (!Files.exists(uploadPath)) {
                Files.createDirectories(uploadPath);
                log.info("Upload directory created: {}", uploadPath);
            }

            String originalFileName = file.getOriginalFilename();
            String safeFileName = Paths.get(originalFileName).getFileName().toString();
            String storedFileName = UUID.randomUUID().toString() + "_" + safeFileName;
            Path targetLocation = uploadPath.resolve(storedFileName);

            Files.copy(file.getInputStream(), targetLocation, StandardCopyOption.REPLACE_EXISTING);

            log.info("File saved successfully: {}", targetLocation);

            return ResponseEntity.ok("File upload successful: " + storedFileName);

        } catch (IOException e) {
            log.error("IO error during file save: user={}, file={}", userDetails != null ? userDetails.getUsername() : "N/A", file.getOriginalFilename(), e);
            return ResponseEntity.internalServerError().body("An error occurred during file upload.");
        } catch (Exception e) {
            log.error("Unexpected error during file processing: user={}, file={}", userDetails != null ? userDetails.getUsername() : "N/A", file.getOriginalFilename(), e);
            return ResponseEntity.internalServerError().body("An error occurred during file processing.");
        }
    }
}
```

Thanks to the `@AuthenticationPrincipal` annotation, you can easily access the `UserDetails` information of the currently authenticated user in controller methods. When saving files, consider security (path manipulation prevention) and name collision prevention by using UUID.

## Conclusion: Adding Secure Wings with JWT and Spring Security!

We've journeyed together through building a secure authentication system using JWT and Spring Security in a Spring Boot environment and applying security to file upload functionality! By following the code, I hope you've grasped the overall flow.

Let's summarize the core steps one more time:

1. Solid Foundation: Add necessary dependencies (`build.gradle`)
2. Secret Management: Configure JWT secret key and expiration time (`application.yml`) - **Secret key security is vital!**
3. User Definition: Implement `UserDetails` entity (`User`)
4. Information Loading: Implement `UserDetailsService` (`UserDetailsServiceImpl`)
5. The Magic Key: Implement JWT generation/validation logic (`JwtTokenProvider`)
6. Ironclad Security: Configure `SecurityConfig` (per-path access control, filter registration, etc.)
7. Gatekeeper Role: Implement and register JWT validation filter (`JwtAuthenticationFilter`)
8. Authentication Gateway: Implement login and token issuance endpoint (`AuthController`)
9. Secure File Transfer: Implement secure file upload endpoint (`FileUploadController`)

I hope these code examples serve as a solid foundation for your projects! But don't stop here. There are a few more things to consider for actual production environments:

- **Careful Error Handling**: Strengthen exception handling to ensure your app operates stably in unexpected situations. (Use `@ControllerAdvice` and `ExceptionHandler`)
- **Refresh Token**: Consider implementing Refresh Token to keep Access Token's validity period short without compromising user experience. (Balance security and convenience!)
- **Test, Test, Test!**: It's essential to verify that your code works as intended and has no security holes through sufficient unit and integration tests. (Use Spring Security Test)
- **Fine-grained Authorization**: Beyond simple path access control, add logic to check user permissions for specific resources using `@PreAuthorize`, `@PostAuthorize`, etc.
- **Enhanced File Upload Security**: Add security validation for the uploaded files themselves, such as file extension/Content-Type validation and malicious code scanning.

Now you have powerful tools: JWT and Spring Security. Based on this knowledge, I encourage you to build increasingly secure and reliable applications! If you have questions or want to explore further, feel free to visit again anytime. Happy Coding!
