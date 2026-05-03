---
title: "Spring Boot + JWT + Spring Security -  안전한 인증과 파일 업로드 완전 정복 ?"
date: 2025-04-05T13:24:23+09:00
slug: "544-Spring-Boot-JWT-Spring-Security-안전한-인증과-파일-업로드-완전-정복"
original_url: "https://memoryhub.tistory.com/544"
tistory_id: 544
draft: false
---

안녕하세요! 최신 웹 애플리케이션과 API 개발에서 상태 비저장(Stateless) 인증 방식인 **JWT(JSON Web Token)**는 확장성과 마이크로서비스 아키텍처(MSA) 환경에서의 유연성 덕분에 거의 표준처럼 자리 잡았죠. 이번 포스팅에서는 강력한 보안 프레임워크인 **Spring Security**와 **JWT**를 어떻게 **Spring Boot** 환경에서 효과적으로 통합하는지, 그리고 인증된 사용자만 **파일을 안전하게 업로드**하도록 구현하는 방법까지, 실제 코드를 통해 자세히 살펴보겠습니다. ?

Spring Boot와 Spring Security에 대한 기본 지식이 있는 분들을 대상으로 하며, 실제 프로젝트에 바로 적용해볼 수 있는 실용적인 가이드가 되는 것을 목표로 합니다. 자, 그럼 시작해볼까요? ?

+-------------+    1. 로그인 요청     +----------------+  
|  클라이언트  | --------------------> |  Spring Boot앱  |  
+-------------+                      +----------------+  
       ^                                     |  
       |                                     v  
       |                               +-----------+  
       |                               |  데이터베이스 |  
       |                               +-----------+  
       |                                     |  
       |         2. JWT 토큰 발급             |  
       <------------------------------------|  


+-------------+    3. API 요청 + JWT   +----------------+     +------------------+  
|  클라이언트  | --------------------> |  Spring Boot앱  | --> | SecurityContext  |  
+-------------+                      +----------------+     +------------------+  
       ^                                     |  
       |                                     v  
       |         4. 응답 반환                 |  
       <------------------------------------|

## 1. 프로젝트 설정 및 의존성 추가: 첫 단추 잘 꿰기 ?

모든 개발의 시작은 환경 설정이죠! Spring Boot 프로젝트를 생성하고 필요한 라이브러리, 즉 의존성을 추가하는 것부터 시작합니다. Gradle을 사용하신다면 `build.gradle` 파일에 아래와 같이 추가해주세요. (의존성 버전 관리는 항상 중요하니, 프로젝트 환경에 맞게 호환성을 확인하는 습관을 들이는 것이 좋습니다! ?)

```
// build.gradle

plugins {
    id 'java'
    id 'org.springframework.boot' version '3.2.4' // 사용하는 Spring Boot 버전에 맞게 조정하세요.
    id 'io.spring.dependency-management' version '1.1.4'
}

group = 'com.example'
version = '0.0.1-SNAPSHOT'

java {
    sourceCompatibility = '17' // JDK 17 사용 명시
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
    implementation 'org.springframework.boot:spring-boot-starter-web'          // 웹 애플리케이션 개발용
    implementation 'org.springframework.boot:spring-boot-starter-security'     // Spring Security
    implementation 'org.springframework.boot:spring-boot-starter-data-jpa'     // Spring Data JPA (DB 연동 시)
    implementation 'org.springframework.boot:spring-boot-starter-validation'  // 유효성 검증

    // JWT 라이브러리 (jjwt) - 가장 널리 쓰이는 라이브러리 중 하나죠!
    implementation 'io.jsonwebtoken:jjwt-api:0.11.5'
    runtimeOnly 'io.jsonwebtoken:jjwt-impl:0.11.5'
    runtimeOnly 'io.jsonwebtoken:jjwt-jackson:0.11.5' // Jackson 기반 직렬화/역직렬화 시 필요

    // 데이터베이스 드라이버 (예: H2 또는 MySQL/PostgreSQL 등)
    runtimeOnly 'com.h2database:h2' // 개발/테스트 시 편리한 H2 인메모리 DB
    // runtimeOnly 'mysql:mysql-connector-java' // MySQL 사용 시
    // runtimeOnly 'org.postgresql:postgresql' // PostgreSQL 사용 시

    // Lombok (선택 사항 - 보일러플레이트 코드 감소에 탁월!)
    compileOnly 'org.projectlombok:lombok'
    annotationProcessor 'org.projectlombok:lombok'

    // Spring Boot Test (테스트는 기본이죠!)
    testImplementation 'org.springframework.boot:spring-boot-starter-test'
    testImplementation 'org.springframework.security:spring-security-test'
}

tasks.named('test') {
    useJUnitPlatform()
}
```

핵심 의존성은 `spring-boot-starter-web`, `spring-boot-starter-security`, `spring-boot-starter-data-jpa`, 그리고 JWT 처리를 위한 `jjwt` 라이브러리입니다.

## 2. JWT 및 애플리케이션 설정: 환경 구성하기 ⚙️

JWT 토큰 생성과 검증의 핵심 요소인 비밀 키와 만료 시간 등을 설정 파일(`application.yml` 또는 `application.properties`)에서 관리합니다.

```
# src/main/resources/application.yml

spring:
  # 데이터베이스 설정 (예: H2)
  datasource:
    url: jdbc:h2:mem:testdb # 인메모리 H2 DB 사용 예시
    driverClassName: org.h2.Driver
    username: sa
    password:
  jpa:
    database-platform: org.hibernate.dialect.H2Dialect # 사용하는 DB에 맞게 Dialect 설정
    hibernate:
      ddl-auto: update # 개발 초기에는 update 또는 create, 운영에서는 validate 또는 none 권장
    show-sql: true # 실행되는 SQL 쿼리 로그 출력 (개발 시 유용)

# JWT 설정
app:
  jwt:
    # !!! ? 절대 주의: 실제 운영 환경에서는 이 값을 절대 하드코딩하면 안 됩니다! ? !!!
    # 환경 변수, 외부 설정 파일, Vault, AWS Secrets Manager, GCP Secret Manager 등 안전한 방법을 사용하세요.
    secret-key: VmVyeVNlY3JldEtleUZvckpXVEF1dGhlbnRpY2F0aW9uYW5kQXV0aG9yaXphdGlvblNlcnZpY2U= # Base64 인코딩된 강력한 비밀 키 예시
    expiration-ms: 3600000 # 토큰 만료 시간 (밀리초 단위, 예: 1시간)
    # refresh-token-expiration-ms: 604800000 # 필요시 리프레시 토큰 만료 시간 (예: 7일)

# 파일 업로드 설정 (선택 사항)
# spring:
#   servlet:
#     multipart:
#       max-file-size: 10MB   # 개별 파일 최대 크기
#       max-request-size: 100MB # 전체 요청 최대 크기
# app:
#   upload:
#     dir: /path/to/your/upload/directory # 실제 파일 저장 경로 (운영 환경에 맞게 설정)
```

**`다시 한번 강조하지만, app.jwt.secret-key는 매우 민감한 정보입니다.`** 유출될 경우 토큰 위변조가 가능해지므로, 반드시 안전한 방식으로 관리해야 합니다. (환경 변수나 클라우드 제공 업체의 시크릿 관리 서비스를 사용하는 것이 일반적입니다.) 만료 시간(`expiration-ms`)은 서비스의 보안 정책과 사용자 편의성을 고려하여 적절히 설정해주세요.

---

## **전체 프로세스 다이어그램**

![](/images/544-Spring-Boot-JWT-Spring-Security-안전한-인증과-파일-업로드-완전-정복/img.png)

---

## 3. 사용자 정보 모델링: 누가 누구인가? ?

Spring Security가 사용자를 인식하고 권한을 관리할 수 있도록, 사용자 정보를 담는 엔티티 클래스를 정의합니다. 이 클래스는 Spring Security의 `UserDetails` 인터페이스를 구현해야 합니다.

```
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
@Table(name = "users") // 데이터베이스 테이블 이름 지정
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED) // JPA 엔티티는 기본 생성자가 필요 (protected 권장)
public class User implements UserDetails { // Spring Security UserDetails 구현

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String username; // 로그인 ID로 사용될 사용자 이름

    @Column(nullable = false)
    private String password; // 암호화된 비밀번호

    // 사용자 역할(Role) 정보. EAGER 로딩은 사용자 수가 많지 않거나,
    // 인증 시 항상 역할 정보가 필요할 때 유용합니다.
    // 사용자 수가 많고 역할 정보가 항상 필요하지 않다면 LAZY 로딩 후 필요시 조회하는 전략도 고려해볼 수 있습니다.
    @ElementCollection(fetch = FetchType.EAGER)
    @CollectionTable(name = "user_roles", joinColumns = @JoinColumn(name = "user_id"))
    @Column(name = "role")
    private List<String> roles = new java.util.ArrayList<>(); // 예: "ROLE_USER", "ROLE_ADMIN"

    @Builder
    public User(String username, String password, List<String> roles) {
        this.username = username;
        this.password = password; // 비밀번호는 실제 저장 전에 서비스 레이어에서 암호화해야 합니다!
        this.roles = roles;
    }

    // --- UserDetails 인터페이스 구현 메서드 ---

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
        // roles 목록을 Spring Security가 이해하는 GrantedAuthority 객체 컬렉션으로 변환
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

    // 계정 상태 관련 메서드들 (기본값은 true, 필요에 따라 로직 추가)
    @Override
    public boolean isAccountNonExpired() { return true; } // 계정 만료 여부

    @Override
    public boolean isAccountNonLocked() { return true; } // 계정 잠김 여부

    @Override
    public boolean isCredentialsNonExpired() { return true; } // 비밀번호 만료 여부

    @Override
    public boolean isEnabled() { return true; } // 계정 활성화 여부
}
```

사용자 엔티티와 데이터베이스 간의 상호작용은 Spring Data JPA 리포지토리 인터페이스를 통해 이루어집니다.

```
// src/main/java/com/example/demo/user/UserRepository.java
package com.example.demo.user;

import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    // 사용자 이름(username)으로 사용자를 찾는 메서드 (Spring Data JPA가 메서드 이름을 기반으로 쿼리 생성)
    Optional<User> findByUsername(String username);
}
```

## 4. 사용자 정보 로드 서비스: 인증의 시작점 ?

Spring Security가 로그인 요청을 처리할 때, 실제로 사용자 정보를 어디서 어떻게 가져올지를 알려주는 `UserDetailsService` 구현체가 필요합니다.

```
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
@RequiredArgsConstructor // final 필드(UserRepository)에 대한 생성자 자동 주입 (Lombok)
public class UserDetailsServiceImpl implements UserDetailsService {

    private final UserRepository userRepository;

    @Override
    @Transactional(readOnly = true) // 데이터 변경이 없으므로 읽기 전용 트랜잭션 적용 (성능 이점)
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        // UserRepository를 사용하여 데이터베이스에서 사용자 정보 조회
        // Optional<User>를 반환받으므로, orElseThrow를 사용해 사용자가 없을 경우 예외 처리
        User user = userRepository.findByUsername(username)
                .orElseThrow(() -> new UsernameNotFoundException("사용자를 찾을 수 없습니다: " + username));

        // 조회된 User 객체 반환 (User 클래스가 UserDetails를 구현했으므로 형변환 없이 가능)
        return user;
    }
}
```

이 서비스는 `UserRepository`를 주입받아 `loadUserByUsername` 메서드에서 사용자 이름으로 DB를 조회하고, 결과를 `UserDetails` 타입으로 반환합니다.

## 5. JWT 토큰 처리 유틸리티: 토큰 마법사 ✨

JWT 토큰 생성, 유효성 검증, 정보 추출 등 토큰 관련 모든 핵심 로직을 이 클래스에 모아 관리합니다.

```
// src/main/java/com/example/demo/security/JwtTokenProvider.java
package com.example.demo.security;

import io.jsonwebtoken.*;
import io.jsonwebtoken.io.Decoders;
import io.jsonwebtoken.security.Keys;
import io.jsonwebtoken.security.SecurityException; // 명시적 import
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
@Slf4j // 로깅 라이브러리 사용 (예: Logback)
public class JwtTokenProvider {

    @Value("${app.jwt.secret-key}")
    private String secretKeyValue; // application.yml 에서 정의된 비밀 키 값

    @Value("${app.jwt.expiration-ms}")
    private long jwtExpirationInMs; // application.yml 에서 정의된 만료 시간 값

    private SecretKey secretKey; // JWT 서명/검증에 사용할 키 객체

    private static final String AUTHORITIES_KEY = "auth"; // 토큰 내부에 권한 정보를 저장할 때 사용할 클레임 키

    // 빈 생성 후 초기화 로직: 설정 파일에서 읽어온 secretKeyValue를 사용하여 SecretKey 객체 생성
    @PostConstruct
    public void init() {
        byte[] keyBytes = Decoders.BASE64.decode(secretKeyValue); // Base64로 인코딩된 키를 디코딩
        this.secretKey = Keys.hmacShaKeyFor(keyBytes); // HMAC-SHA 알고리즘에 사용할 키 생성 (jjwt 라이브러리 기능)
        // 참고: HS512는 일반적으로 HS256보다 안전하지만 약간의 성능 오버헤드가 있을 수 있습니다.
        // RSA(RS256/RS512) 같은 비대칭키 알고리즘은 키 관리가 더 복잡하지만, 공개키만으로 검증이 가능해 특정 시나리오(예: 외부 서비스 연동)에 유리할 수 있습니다.
    }

    /**
     * 인증(Authentication) 객체 정보를 바탕으로 JWT 토큰을 생성합니다.
     * @param authentication 인증 정보 (사용자 이름, 권한 등 포함)
     * @return 생성된 JWT 문자열
     */
    public String generateToken(Authentication authentication) {
        // 권한(Role) 정보를 콤마(,)로 구분된 문자열로 변환
        String authorities = authentication.getAuthorities().stream()
                .map(GrantedAuthority::getAuthority)
                .collect(Collectors.joining(","));

        long now = (new Date()).getTime();
        Date validity = new Date(now + this.jwtExpirationInMs); // 현재 시간에 만료 시간(ms)을 더해 만료 시점 계산

        // jjwt 라이브러리의 빌더 패턴을 사용하여 JWT 생성
        return Jwts.builder()
                .setSubject(authentication.getName()) // 토큰의 주체(subject)로 사용자 이름 설정
                .claim(AUTHORITIES_KEY, authorities) // 커스텀 클레임으로 권한 정보 추가
                .setIssuedAt(new Date()) // 토큰 발급 시간 설정
                .setExpiration(validity) // 토큰 만료 시간 설정
                .signWith(secretKey, SignatureAlgorithm.HS512) // 지정된 비밀 키와 HS512 알고리즘으로 서명
                .compact(); // 최종 JWT 문자열 생성
    }

    /**
     * JWT 토큰 문자열로부터 Authentication 객체를 생성합니다.
     * 이 메서드는 주로 JWT 필터에서 사용됩니다.
     * @param token 검증된 JWT 토큰 문자열
     * @return Spring Security 컨텍스트에서 사용할 Authentication 객체
     */
    public Authentication getAuthentication(String token) {
        // 토큰에서 클레임(페이로드) 정보 추출
        Claims claims = Jwts.parserBuilder()
                .setSigningKey(secretKey) // 검증에 사용할 비밀 키 설정
                .build()
                .parseClaimsJws(token) // 토큰 파싱 및 서명 검증 (실패 시 예외 발생)
                .getBody(); // 클레임 정보 얻기

        // 클레임에서 사용자 이름과 권한 정보 추출
        String username = claims.getSubject();
        String[] authorities = claims.get(AUTHORITIES_KEY, String.class).split(",");

        // UserDetails 객체 생성 (DB 조회 없이 토큰 정보만으로 생성)
        // 주의: 이 방식은 토큰 발급 시점의 권한 정보를 사용합니다. 실시간 권한 변경 반영이 필요하다면
        // 여기서 UserDetailsService를 호출하여 DB에서 최신 정보를 가져와야 합니다. (Stateless 이점은 일부 희석됨)
        UserDetails userDetails = org.springframework.security.core.userdetails.User.builder()
                .username(username)
                .password("") // 토큰 기반 인증이므로 비밀번호는 불필요
                .authorities(authorities)
                .build();

        // Authentication 객체 생성하여 반환
        return new UsernamePasswordAuthenticationToken(userDetails, token, userDetails.getAuthorities());
    }

    /**
     * 주어진 JWT 토큰의 유효성을 검증합니다. (서명, 만료 시간 등)
     * @param token 검증할 JWT 토큰 문자열
     * @return 토큰이 유효하면 true, 아니면 false
     */
    public boolean validateToken(String token) {
        try {
            // 토큰 파싱 및 검증 시도. 성공하면 유효한 토큰임.
            Jwts.parserBuilder().setSigningKey(secretKey).build().parseClaimsJws(token);
            return true;
        } catch (SecurityException | MalformedJwtException e) {
            log.info("❌ 잘못된 JWT 서명입니다.");
        } catch (ExpiredJwtException e) {
            log.info("⏰ 만료된 JWT 토큰입니다.");
        } catch (UnsupportedJwtException e) {
            log.info("? 지원되지 않는 JWT 토큰입니다.");
        } catch (IllegalArgumentException e) {
            log.info("⚠️ JWT 토큰이 잘못되었습니다.");
        }
        // 예외 발생 시 유효하지 않은 토큰으로 간주
        return false;
    }

    /**
     * (선택적) JWT 토큰에서 사용자 이름(subject)만 빠르게 추출합니다.
     * @param token JWT 토큰 문자열
     * @return 사용자 이름
     */
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

## 6. Spring Security 설정: 보안의 틀 잡기 ?️

이제 Spring Security의 동작 방식을 정의하는 핵심 설정 클래스(`SecurityConfig`)를 작성합니다. HTTP 요청 처리 규칙, 세션 관리, CORS, JWT 필터 연동 등을 여기서 설정합니다.

```
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
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer; // CSRF, HttpBasic 등 비활성화 시 사용
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
@EnableWebSecurity // Spring Security 기능을 활성화합니다.
@EnableMethodSecurity(securedEnabled = true, prePostEnabled = true) // 메서드 레벨 보안(@Secured, @PreAuthorize 등) 사용 설정
@RequiredArgsConstructor // final 필드(JwtTokenProvider)에 대한 생성자 자동 주입
public class SecurityConfig {

    private final JwtTokenProvider jwtTokenProvider;

    // 비밀번호 암호화를 위한 PasswordEncoder 빈 등록 (BCrypt 사용)
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    // 인증 처리를 위한 AuthenticationManager 빈 등록
    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration) throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }

    // CORS(Cross-Origin Resource Sharing) 설정 빈 등록
    @Bean
    public CorsConfigurationSource corsConfigurationSource() {
        CorsConfiguration configuration = new CorsConfiguration();
        // !!! 중요: 실제 운영 환경에서는 '*' 대신 허용할 프론트엔드 도메인을 명시해야 합니다 !!!
        configuration.setAllowedOrigins(List.of("http://localhost:8081", "http://your-frontend-domain.com")); // 예: Vue.js 개발 서버 주소
        configuration.setAllowedMethods(Arrays.asList("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS")); // 허용할 HTTP 메서드
        configuration.setAllowedHeaders(Arrays.asList("Authorization", "Cache-Control", "Content-Type")); // 허용할 요청 헤더
        configuration.setAllowCredentials(true); // 쿠키 등 자격 증명 정보 허용 여부
        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", configuration); // 모든 경로(/)에 대해 위 설정 적용
        return source;
    }

    // Spring Security 필터 체인 설정
    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
                // CSRF(Cross-Site Request Forgery) 보호 비활성화
                // 이유: JWT는 상태 비저장(Stateless) 방식이므로 서버에 세션 상태를 저장하지 않아,
                // 세션 기반의 CSRF 공격에 비교적 안전합니다. REST API에서는 보통 비활성화합니다.
                .csrf(AbstractHttpConfigurer::disable)

                // CORS 설정 적용 (위에서 정의한 corsConfigurationSource 사용)
                .cors(cors -> cors.configurationSource(corsConfigurationSource()))

                // 세션 관리 정책 설정: STATELESS
                // 이유: JWT 토큰 자체에 인증 정보가 포함되므로 서버는 세션을 유지할 필요가 없습니다.
                // 이는 서버의 확장성(Scalability)에 유리합니다.
                .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))

                // HTTP 요청에 대한 인가(Authorization) 규칙 설정
                .authorizeHttpRequests(authz -> authz
                        // '/api/auth/' 경로 하위 요청은 인증 없이 누구나 접근 허용 (로그인, 회원가입 등)
                        .requestMatchers("/api/auth/**").permitAll()
                        // '/api/files/upload' 경로는 인증된 사용자만 접근 허용
                        .requestMatchers("/api/files/upload").authenticated()
                        // (예시) '/api/admin/' 경로는 'ADMIN' 역할을 가진 사용자만 접근 허용
                        // .requestMatchers("/api/admin/**").hasRole("ADMIN")
                        // 위에서 명시적으로 설정한 경로 외의 모든 요청은 반드시 인증되어야 함
                        .anyRequest().authenticated()
                )

                // 직접 구현한 JwtAuthenticationFilter를 Spring Security 필터 체인에 추가
                // UsernamePasswordAuthenticationFilter (폼 로그인 처리 필터) 보다 먼저 실행되도록 설정
                .addFilterBefore(new JwtAuthenticationFilter(jwtTokenProvider), UsernamePasswordAuthenticationFilter.class);

                // (선택 사항) 예외 처리 핸들러 설정 (예: 인증 실패 시 401, 인가 실패 시 403 응답 커스터마이징)
                // .exceptionHandling(exceptions -> exceptions
                //     .authenticationEntryPoint(...) // 인증되지 않은 사용자의 접근 처리
                //     .accessDeniedHandler(...)      // 권한 없는 리소스 접근 처리
                // );

        return http.build(); // 설정된 HttpSecurity 객체 빌드
    }
}
```

## 7. JWT 인증 필터: 요청 검문소 ?‍♀️

모든 HTTP 요청이 컨트롤러에 도달하기 전에 거치는 관문입니다. 요청 헤더에서 JWT를 찾아 유효성을 검증하고, 유효하다면 인증 정보를 Security Context에 설정하여 뒤따르는 로직(컨트롤러, 서비스 등)에서 `@AuthenticationPrincipal` 등을 통해 인증된 사용자 정보에 접근할 수 있게 해줍니다.

```
// src/main/java/com/example/demo/security/JwtAuthenticationFilter.java
package com.example.demo.security;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j; // 로깅 추가
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.util.StringUtils; // 문자열 유틸리티
import org.springframework.web.filter.OncePerRequestFilter; // 요청당 한 번만 실행되도록 보장

import java.io.IOException;

@RequiredArgsConstructor // final 필드(JwtTokenProvider)에 대한 생성자 자동 주입
@Slf4j // 로깅 사용
public class JwtAuthenticationFilter extends OncePerRequestFilter {

    private final JwtTokenProvider jwtTokenProvider;
    public static final String AUTHORIZATION_HEADER = "Authorization"; // 토큰을 담을 HTTP 헤더 이름
    public static final String BEARER_PREFIX = "Bearer "; // JWT 토큰임을 나타내는 접두사 (표준)

    // 필터의 핵심 로직
    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {

        // 1. 요청(Request)의 헤더에서 JWT 토큰 추출 시도
        String jwt = resolveToken(request);
        String requestURI = request.getRequestURI(); // 로깅을 위해 요청 URI 얻기

        // 2. 토큰 유효성 검사 (토큰이 존재하고, 유효한 형식이며, 만료되지 않았는지 등)
        if (StringUtils.hasText(jwt) && jwtTokenProvider.validateToken(jwt)) {
            // 토큰이 유효하면, 토큰으로부터 Authentication 객체를 생성
            Authentication authentication = jwtTokenProvider.getAuthentication(jwt);
            // SecurityContextHolder에 Authentication 객체를 저장 -> 현재 요청 처리 쓰레드에서 인증 정보 유지
            SecurityContextHolder.getContext().setAuthentication(authentication);
            log.debug("✅ Security Context에 '{}' 인증 정보를 저장했습니다, uri: {}", authentication.getName(), requestURI);
        } else {
            log.debug("❌ 유효한 JWT 토큰이 없습니다, uri: {}", requestURI);
        }

        // 3. 다음 필터로 요청(Request)과 응답(Response) 전달
        //    (여기서 인증 정보 설정이 완료되었으므로, 뒤의 필터나 컨트롤러에서 인증 여부 확인 가능)
        filterChain.doFilter(request, response);
    }

    // HTTP 요청 헤더에서 'Authorization' 헤더를 찾아 Bearer 토큰을 추출하는 메서드
    private String resolveToken(HttpServletRequest request) {
        String bearerToken = request.getHeader(AUTHORIZATION_HEADER);
        // 헤더 값이 존재하고, 'Bearer '로 시작하는지 확인
        if (StringUtils.hasText(bearerToken) && bearerToken.startsWith(BEARER_PREFIX)) {
            return bearerToken.substring(BEARER_PREFIX.length()); // 'Bearer ' 부분을 제외한 실제 토큰 값 반환
        }
        // 해당하는 토큰이 없으면 null 반환
        return null;
    }
}
```

## 8. 인증 엔드포인트 컨트롤러: 로그인 & 토큰 발급 ?️

사용자가 아이디와 비밀번호로 로그인을 시도하고, 성공하면 JWT를 발급해주는 API 엔드포인트입니다.

```
// src/main/java/com/example/demo/auth/AuthController.java
package com.example.demo.auth;

import com.example.demo.security.JwtAuthenticationFilter; // 헤더 상수 사용 위해 import
import com.example.demo.security.JwtTokenProvider;
import jakarta.validation.Valid; // 요청 DTO 유효성 검증
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
@RequestMapping("/api/auth") // 인증 관련 API 경로 Prefix
@RequiredArgsConstructor
public class AuthController {

    private final AuthenticationManager authenticationManager; // SecurityConfig에서 Bean으로 등록한 AuthenticationManager 주입
    private final JwtTokenProvider jwtTokenProvider; // JWT 처리 유틸리티 주입

    // 로그인 요청 처리 API
    @PostMapping("/login")
    public ResponseEntity<JwtAuthenticationResponse> authenticateUser(@Valid @RequestBody LoginRequest loginRequest) {

        // 1. 로그인 요청 DTO로부터 사용자 이름과 비밀번호를 받아 Authentication 객체 생성
        //    (이때 Authentication 객체는 아직 '인증되지 않음' 상태)
        UsernamePasswordAuthenticationToken authenticationToken =
                new UsernamePasswordAuthenticationToken(loginRequest.getUsername(), loginRequest.getPassword());

        // 2. 실제 인증 수행: AuthenticationManager에게 인증 요청 위임
        //    내부적으로 UserDetailsService의 loadUserByUsername 호출 및 PasswordEncoder를 통한 비밀번호 검증 수행
        Authentication authentication = authenticationManager.authenticate(authenticationToken);

        // 3. 인증 성공 시: 인증된 Authentication 객체를 SecurityContextHolder에 저장
        //    (현재 요청 스레드 내에서 인증 정보 유지)
        SecurityContextHolder.getContext().setAuthentication(authentication);

        // 4. 인증된 Authentication 객체 정보를 기반으로 JWT 생성
        String jwt = jwtTokenProvider.generateToken(authentication);

        // 5. 생성된 JWT를 HTTP 응답 헤더(Authorization)에 포함
        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.add(JwtAuthenticationFilter.AUTHORIZATION_HEADER, JwtAuthenticationFilter.BEARER_PREFIX + jwt);

        // 6. JWT와 토큰 타입 정보를 담은 DTO를 응답 본문에 포함하여 ResponseEntity 반환
        return new ResponseEntity<>(new JwtAuthenticationResponse(jwt), httpHeaders, HttpStatus.OK);
    }

    // --- 요청/응답 DTO (Data Transfer Object) 클래스들 ---
    // 컨트롤러 내부 또는 별도 패키지(e.g., com.example.demo.auth.dto)에 위치시킬 수 있습니다.

    // 로그인 요청 시 사용될 DTO
    @lombok.Data // @Getter, @Setter, @ToString, @EqualsAndHashCode, @RequiredArgsConstructor 자동 생성
    public static class LoginRequest {
        @jakarta.validation.constraints.NotBlank(message = "사용자 이름은 필수입니다.")
        private String username;

        @jakarta.validation.constraints.NotBlank(message = "비밀번호는 필수입니다.")
        private String password;
    }

    // 로그인 성공 시 응답으로 반환될 DTO
    @lombok.Getter
    @lombok.RequiredArgsConstructor // final 필드에 대한 생성자
    public static class JwtAuthenticationResponse {
        private final String accessToken; // 발급된 JWT
        private final String tokenType = "Bearer"; // 토큰 타입 (고정값)
    }
}
```

## 9. 보안 파일 업로드 컨트롤러: 인증된 사용자만! ?

이제 `SecurityConfig`에서 `authenticated()`로 접근 제어 설정을 해두었기 때문에, 유효한 JWT를 가진 사용자만 이 파일 업로드 API를 호출할 수 있습니다.

```
// src/main/java/com/example/demo/file/FileUploadController.java
package com.example.demo.file;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize; // 필요시 메서드 레벨에서 추가 권한 검사 가능
import org.springframework.security.core.annotation.AuthenticationPrincipal; // 현재 인증된 사용자 정보 주입
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
import java.nio.file.StandardCopyOption; // 파일 복사 옵션
import java.util.UUID;

@RestController
@RequestMapping("/api/files") // 파일 관련 API 경로 Prefix
@Slf4j
public class FileUploadController {

    // application.yml 에서 설정한 파일 업로드 디렉토리 경로 주입
    // 설정값이 없으면 기본값으로 사용자 홈 디렉토리 아래 'uploads' 사용
    @Value("${app.upload.dir:${user.home}/uploads}")
    private String uploadDir;

    // 파일 업로드 처리 API
    // @PreAuthorize("hasRole('ROLE_UPLOADER')") // 예: 특정 역할(UPLOADER)이 있는 사용자만 허용하고 싶을 때
    @PostMapping("/upload")
    public ResponseEntity<String> uploadFile(
            @RequestParam("file") MultipartFile file, // 'file'이라는 이름으로 전송된 파일을 받음
            @AuthenticationPrincipal UserDetails userDetails // 현재 인증된 사용자의 UserDetails 객체 주입
    ) {
        // 현재 인증된 사용자 정보 확인 (로깅 등)
        if (userDetails == null) {
            // SecurityConfig 설정상 여기까지 오면 안 되지만, 방어적으로 체크
            log.warn("⚠️ 인증 정보 없이 파일 업로드 시도됨.");
            // 필요하다면 여기서 401 Unauthorized 응답을 명시적으로 반환할 수도 있습니다.
            // return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body("인증이 필요합니다.");
        } else {
            log.info("? 파일 업로드 요청 사용자: {}", userDetails.getUsername());
        }

        // 파일 유효성 검사 (비어 있는지, 크기 제한 등 - 크기 제한은 application.yml에서도 설정 가능)
        if (file.isEmpty()) {
            return ResponseEntity.badRequest().body("업로드할 파일을 선택해주세요.");
        }

        try {
            // 업로드 경로 Path 객체 생성
            Path uploadPath = Paths.get(uploadDir);

            // 업로드 디렉토리가 존재하지 않으면 생성
            if (!Files.exists(uploadPath)) {
                Files.createDirectories(uploadPath);
                log.info("? 업로드 디렉토리 생성: {}", uploadPath);
            }

            // 파일 이름 충돌 방지 및 보안 강화
            String originalFileName = file.getOriginalFilename();
            // 경로 조작 공격 방지를 위해 파일 이름에서 경로 정보 제거
            String safeFileName = Paths.get(originalFileName).getFileName().toString();
            // 고유한 파일 이름 생성 (UUID 사용)
            String storedFileName = UUID.randomUUID().toString() + "_" + safeFileName;
            // 최종 저장 경로 Path 객체 생성
            Path targetLocation = uploadPath.resolve(storedFileName);

            // 파일 저장 (StandardCopyOption.REPLACE_EXISTING: 혹시 같은 이름 파일 있으면 덮어쓰기)
            Files.copy(file.getInputStream(), targetLocation, StandardCopyOption.REPLACE_EXISTING);

            log.info("✅ 파일 저장 성공: {}", targetLocation);

            // 성공 응답 반환 (저장된 파일 이름 또는 접근 가능한 URL 등 포함 가능)
            return ResponseEntity.ok("파일 업로드 성공: " + storedFileName);

        } catch (IOException e) {
            log.error("❌ 파일 저장 중 입출력 오류 발생: 사용자={}, 파일={}", userDetails != null ? userDetails.getUsername() : "N/A", file.getOriginalFilename(), e);
            return ResponseEntity.internalServerError().body("파일 업로드 중 오류가 발생했습니다.");
        } catch (Exception e) {
            // 예상치 못한 다른 예외 처리 (예: 디스크 공간 부족 등)
            log.error("❌ 파일 처리 중 예상치 못한 오류 발생: 사용자={}, 파일={}", userDetails != null ? userDetails.getUsername() : "N/A", file.getOriginalFilename(), e);
            return ResponseEntity.internalServerError().body("파일 처리 중 오류가 발생했습니다.");
        }
        // 추가 고려사항: 업로드된 파일의 내용(Content-Type, 악성코드 등) 검증 로직 추가 권장
        // 저장 전략: 로컬 디스크 외에 AWS S3, Google Cloud Storage 등 클라우드 스토리지 사용 고려
    }
}
```

@AuthenticationPrincipal`어노테이션 덕분에 컨트롤러 메서드에서 현재 인증된 사용자의`UserDetails` 정보를 쉽게 얻을 수 있습니다. 파일 저장 시에는 보안(경로 조작 방지)과 이름 충돌 방지를 고려하여 UUID 등을 활용하는 것이 좋습니다.

## 결론: JWT와 Spring Security로 안전한 날개 달기! ?

자, 여기까지 Spring Boot 환경에서 JWT와 Spring Security를 활용해 안전한 인증 시스템을 구축하고, 파일 업로드 기능까지 보안을 적용하는 여정을 함께했습니다! ? 코드를 따라오시면서 전체적인 흐름을 파악하셨으리라 생각해요.

핵심 단계를 다시 한번 정리해 볼까요?

1. 튼튼한 기초 공사: 필요한 의존성 추가 (`build.gradle`) ?
2. 비밀 정보 관리: JWT 비밀키 및 만료 시간 설정 (`application.yml`) - **비밀키 보안은 생명!** ?
3. 사용자 정의: `UserDetails` 구현 엔티티 정의 (`User`) ?
4. 정보 로딩: `UserDetailsService` 구현 (`UserDetailsServiceImpl`) ?
5. 마법의 열쇠: JWT 생성/검증 로직 구현 (`JwtTokenProvider`) ✨
6. 철통 보안 설정: `SecurityConfig` 설정 (경로별 접근 제어, 필터 등록 등) ?️
7. 문지기 역할: JWT 검증 필터 구현 및 등록 (`JwtAuthenticationFilter`) ?
8. 인증 관문: 로그인 및 토큰 발급 엔드포인트 구현 (`AuthController`) ?️
9. 안전한 파일 전송: 보안 파일 업로드 엔드포인트 구현 (`FileUploadController`) ?

이 코드 예제들이 여러분의 프로젝트에 든든한 기반이 되기를 바랍니다! 하지만 여기서 멈추지 마세요. ? 실제 운영 환경을 위해서는 몇 가지 더 고려해야 할 점들이 있답니다.

- **꼼꼼한 에러 처리**: 예상치 못한 상황에도 앱이 안정적으로 동작하도록 예외 처리를 강화해주세요. (`@ControllerAdvice` 와 `ExceptionHandler` 활용) ?️
- **Refresh Token**: Access Token의 유효 기간을 짧게 가져가면서 사용자 경험을 해치지 않도록 Refresh Token 도입을 고려해보세요. (보안과 편의성의 균형점!) ?
- **테스트, 테스트, 테스트!**: 작성한 코드가 의도대로 동작하는지, 보안 허점은 없는지 충분한 단위 테스트와 통합 테스트 코드로 검증하는 것은 필수입니다! (Spring Security Test 활용) ?
- **세분화된 인가**: 단순히 경로 접근 제어를 넘어, 특정 리소스에 대한 사용자의 권한을 확인하는 로직(`@PreAuthorize`, `@PostAuthorize` 등)을 추가하여 보안을 강화하세요. ?
- **파일 업로드 보안 강화**: 파일 확장자/Content-Type 검증, 악성코드 스캔 등 업로드된 파일 자체에 대한 보안 검증 로직을 추가하는 것이 좋습니다. ?️?

이제 여러분은 JWT와 Spring Security라는 강력한 도구를 손에 넣으셨습니다. 이 지식을 바탕으로 더욱 안전하고 신뢰성 높은 애플리케이션을 만들어나가시길 응원합니다! 궁금한 점이나 더 탐구하고 싶은 주제가 있다면 언제든지 다시 찾아주세요. ? Happy Coding! ?
