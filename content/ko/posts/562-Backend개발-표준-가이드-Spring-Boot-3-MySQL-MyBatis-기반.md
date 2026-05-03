---
title: "Backend개발 표준 가이드 - Spring Boot 3, MySQL, MyBatis 기반"
date: 2025-04-23T18:23:51+09:00
slug: "562-Backend개발-표준-가이드-Spring-Boot-3-MySQL-MyBatis-기반"
original_url: "https://memoryhub.tistory.com/562"
tistory_id: 562
draft: false
---

# I. 서론

## A. 목적 및 범위

본 문서는 Spring Boot 3, MySQL, MyBatis 기술 스택 및 Lombok 라이브러리를 활용하는 백엔드 애플리케이션 개발의 표준을 정의하는 것을 목적으로 한다. 이 표준 가이드라인은 코드의 일관성, 가독성, 유지보수성 및 확장성을 향상시키고, 팀원 간의 협업 효율성을 증대시키며, 잠재적 오류를 최소화하는 데 기여할 것이다.

적용 범위는 프로젝트 구조, 명명 규칙, 코딩 스타일, API 설계, 데이터베이스 스키마 관리, MyBatis 활용법, 예외 처리 및 로깅 전략을 포함한 백엔드 개발의 전반적인 측면을 포괄한다. 본 표준은 기술 스택별 공식 문서, 커뮤니티 모범 사례, 그리고 검증된 업계 표준을 기반으로 수립되었다.

## B. 표준 준수의 중요성

개발 표준을 준수하는 것은 단순히 코드를 심미적으로 개선하는 것을 넘어, 프로젝트의 장기적인 성공에 필수적인 요소이다. 일관된 표준은 다음과 같은 이점을 제공한다:

1. **가독성 향상**: 통일된 스타일과 명명 규칙은 코드를 이해하는 데 필요한 시간을 단축시킨다.
2. **유지보수성 증대**: 표준화된 구조와 코딩 방식은 버그 수정, 기능 추가 등 유지보수 작업을 용이하게 한다.
3. **협업 효율 증진**: 팀원 모두가 동일한 규칙을 따름으로써 코드 리뷰 및 통합 과정에서의 마찰을 줄이고 생산성을 높인다.
4. **오류 감소**: 검증된 모범 사례와 명확한 가이드라인은 잠재적인 설계 오류나 구현 실수를 예방하는 데 도움이 된다.
5. **신규 팀원 적응 용이**: 잘 정의된 표준은 새로운 팀원이 프로젝트 구조와 코드베이스를 빠르게 파악하고 기여할 수 있도록 돕는다.

따라서, 본 문서에 정의된 표준을 모든 팀원이 숙지하고 적극적으로 준수하는 것이 프로젝트의 성공을 위해 매우 중요하다.

# II. 프로젝트 구조 및 명명 규칙

## A. 표준 디렉토리 구조

프로젝트의 구조는 코드의 구성과 모듈 간의 관계를 명확하게 보여주어야 한다. Maven 또는 Gradle과 같은 빌드 시스템에서 제공하는 표준 디렉토리 구조를 따르는 것이 좋다. 이는 새로운 개발자가 프로젝트에 합류했을 때 구조를 쉽게 파악하는 데 도움이 된다.

기본적인 디렉토리 구조는 다음과 같다:

```
src
├── main
│   ├── java                # 자바 소스 코드 루트
│   │   └── com
│   │       └── example
│   │           └── projectname  # 최상위 패키지
│   │               ├── ProjectnameApplication.java  # Spring Boot 메인 애플리케이션 클래스
│   │               ├── config        # 설정 관련 클래스
│   │               ├── controller    # API 요청 처리
│   │               ├── service       # 비즈니스 로직 구현
│   │               ├── repository    # 데이터 접근
│   │               ├── domain        # 도메인 객체
│   │               ├── dto           # 데이터 전송 객체
│   │               └── util          # 공통 유틸리티 클래스
│   └── resources           # 리소스 파일 루트
│       ├── static          # 정적 리소스
│       ├── templates       # 템플릿 엔진 파일
│       ├── mybatis         # MyBatis 매퍼 XML 파일
│       │   └── mapper
│       ├── application.yml # 메인 설정 파일
│       └── application-{profile}.yml # 프로파일별 설정 파일
└── test
    ├── java                # 테스트 소스 코드 루트
    │   └── com
    │       └── example
    │           └── projectname
    └── resources           # 테스트 리소스 파일 루트
        └── application-test.yml # 테스트용 설정 파일
```

- **src/main/java**: 애플리케이션의 자바 소스 코드
- **src/main/resources**: 설정 파일, 정적 리소스, MyBatis 매퍼 XML 파일 등. 설정 파일은 환경별로 분리하는 것이 좋다 (application-{profile}.yml).
- **src/test/java**: 단위 테스트 및 통합 테스트 코드. src/main/java와 동일한 패키지 구조를 따른다.
- **src/test/resources**: 테스트 실행에 필요한 리소스 파일

## B. 모듈 분리 기준

대규모 프로젝트의 경우, 기능 또는 도메인을 기준으로 모듈을 분리하는 것이 효과적이다. 각 모듈은 독립적인 빌드 단위를 가지며, 명확한 의존 관계를 정의해야 한다. Spring Boot는 모듈화를 지원하며, 복잡한 애플리케이션을 여러 팀이 개발할 때 특히 유용하다. 모듈 분리 시에도 각 모듈 내에서 표준 디렉토리 구조와 패키지 명명 규칙을 일관되게 적용한다.

## C. 패키지 명명 규칙

패키지 이름은 프로젝트의 구조를 나타내는 중요한 요소이다. 명확하고 일관된 패키지 명명 규칙은 코드의 탐색과 이해를 돕는다.

- **최상위 패키지**: 회사의 역 도메인 이름을 사용한다 (예: com.example.projectname). 모든 클래스는 이 최상위 패키지 또는 그 하위 패키지에 위치해야 한다.
- **패키지 이름**: 소문자 알파벳과 숫자만 사용하며, 단어 사이는 점(.)으로 구분한다. 밑줄(\_)이나 대문자는 사용하지 않는다.

### 패키지 구성 전략

패키지 구성 방식은 크게 두 가지로 나뉜다:

#### 1. 계층별 패키징(Package-by-Layer)

애플리케이션의 기술적 계층을 기준으로 패키지를 구성한다. 소규모 프로젝트나 마이크로서비스에 적합하다.

```
com.example.projectname
├── config
├── controller
├── service
├── repository
├── domain
└── dto
```

#### 2. 기능별 패키징(Package-by-Feature)

애플리케이션의 주요 기능 또는 도메인을 기준으로 패키지를 구성한다. 각 기능 패키지 내부에 필요한 계층 구성요소를 포함한다. 기능 간의 응집도를 높이고 결합도를 낮추며, 대규모 애플리케이션에 권장된다.

```
com.example.projectname
├── common          # 공통 유틸리티, 기반 클래스 등
├── user            # 사용자 관리 기능
│   ├── controller
│   ├── service
│   ├── repository
│   ├── domain
│   └── dto
├── order           # 주문 관리 기능
│   ├── controller
│   ├── service
│   ├── repository
│   ├── domain
│   └── dto
└── product         # 상품 관리 기능
    ├── controller
    ├── service
    ├── repository
    ├── domain
    └── dto
```

기능별 패키징을 사용하면:

- 각 기능이 독립적인 단위로 관리되어 코드 변경 시 다른 기능에 미치는 영향이 최소화된다
- 특정 기능을 삭제해야 할 경우 해당 패키지만 제거하면 되므로 유지보수가 용이하다
- 공통 요소는 별도의 common 패키지에 둔다

### 선택 가이드

프로젝트의 규모와 복잡성, 팀의 선호도를 고려하여 계층별 또는 기능별 패키징 전략 중 하나를 선택하고, 프로젝트 전체에 걸쳐 일관되게 적용하는 것이 중요하다.

## III. Java 코드 컨벤션

### A. 네이밍 컨벤션

의미 있고 일관된 네이밍은 코드 가독성을 크게 향상시킵니다. Google Java Style Guide와 Spring Framework Code Style을 기반으로 합니다.

### 클래스 (Class)

- **UpperCamelCase** 사용 (예: `Customer`, `OrderService`)
- 명사 또는 명사구 사용
- Spring 컴포넌트는 역할에 맞는 접미사 사용 (`Controller`, `Service`, `Repository`, `Config`)
- 테스트 클래스는 대상 클래스 이름 뒤에 `Test` 또는 `Tests` 붙임

### 인터페이스 (Interface)

- **UpperCamelCase** 사용
- 명사/명사구 또는 형용사/형용사구 사용 (예: `Runnable`, `Comparable`)
- 접두사 `I`는 권장하지 않음 (예: `IOrderService` 대신 `OrderService`)

### 메소드 (Method)

- **lowerCamelCase** 사용
- 동사 또는 동사구 사용 (예: `getUserById`, `processOrder`)
- Getter/Setter는 `getFieldName`/`setFieldName` 형식
- 테스트 메소드는 밑줄(\_)로 논리적 구성 요소 구분 가능 (예: `createUser_withValidData_shouldReturnCreatedUser`)

### 변수 (Variable)

- **lowerCamelCase** 사용
- 명확한 의미 전달 (예: `customerName`, `orderList`)
- 약어 사용 지양, 임시 변수 외 한 글자 이름 피함
- Boolean 변수는 `is`, `has` 접두사 권장 (예: `isValid`, `hasPermission`)

### 상수 (Constant)

- **UPPER\_SNAKE\_CASE** 사용
- `static final`로 선언
- 예: `MAX_CONNECTIONS`, `DEFAULT_TIMEOUT_SECONDS`

## Lombok 사용 가이드라인

Lombok은 반복적인 코드를 줄여주는 유용한 라이브러리지만, 신중하게 사용해야 합니다.

### 권장 어노테이션

- **@Getter / @Setter**

  - 불변성이 필요한 필드는 `@Setter` 사용 자제
  - 필요 시 접근 수준 제어: `@Setter(AccessLevel.PROTECTED)
- **생성자 관련**

  - **@NoArgsConstructor**: 기본 생성자 (JPA Entity 등 필요 시)
  - **@AllArgsConstructor**: 모든 필드 포함 생성자
  - **@RequiredArgsConstructor**: `final`/`@NonNull` 필드만 포함 (생성자 주입에 권장)
- **@ToString**

  - 민감 정보/지연 로딩 필드 제외: `@ToString(exclude = {"password"})
- **@EqualsAndHashCode**

  - JPA Entity에 사용 금지 (ID 기반 비교 문제 발생)
  - DTO/Value Object에 사용 시 비교 필드 명시: `@EqualsAndHashCode(of = {"field1", "field2"})
- **@Data**

  - DTO 등 단순 데이터 객체에만 사용
  - JPA Entity에 절대 사용 금지
- **@Builder**

  - 파라미터가 많거나 선택적인 객체 생성에 유용
  - DTO/설정 객체에 권장
- **@Slf4j**

  - 로깅 객체 자동 생성
  - 로깅 구현 시 적극 사용
- **@NonNull**

  - Null 검사 자동 추가
  - `@RequiredArgsConstructor`와 함께 활용

### 사용 시 고려사항

- **가독성**: 어떤 메소드가 생성되는지 명확히 인지
- **Delombok**: 생성 코드 확인 및 의존성 제거 시 활용
- **IDE 설정**: Lombok 플러그인 설치 및 어노테이션 프로세싱 활성화
- **lombok.config**: 동작 커스터마이징 (팀 내 합의 필요)

가장 권장되는 패턴: `@RequiredArgsConstructor`를 통한 생성자 주입, `@Slf4j`를 통한 로거 생성

## IV. 데이터베이스 스키마 표준

### A. 테이블 명명 규칙

데이터베이스 객체의 명명 규칙은 일관성과 명확성을 유지하는 데 필수적이다.

- **케이스**: 테이블 이름은 소문자 snake\_case를 사용한다. (예: `customer_orders`, `product_categories`). MySQL은 운영체제에 따라 테이블 이름의 대소문자를 구분할 수 있으므로, 혼동을 피하기 위해 소문자로 통일한다.
- **단/복수**: 테이블 이름은 복수형(plural) 명사를 사용한다. 이는 테이블이 여러 레코드(리소스 모음)를 저장한다는 의미를 내포한다. (예: `users`, `orders`, `products`). 단, 팀 내에서 단수형(singular)으로 합의했다면 일관성 있게 단수형을 사용해도 무방하다. 중요한 것은 일관성이다.
- **접두사/접미사**: 일반적으로 테이블 이름에 불필요한 접두사(`tbl_`)나 접미사(`_table`)는 사용하지 않는다. 다만, 기능이나 모듈별로 테이블을 그룹화하기 위해 의미 있는 접두사를 사용할 수 있다 (예: `sales_orders`, `inventory_products`).
- **예약어**: MySQL 예약어(예: `order`, `select`, `group`)는 테이블 이름으로 사용하지 않는다. 사용해야 할 경우 백틱(`)으로 감싸야 하지만, 가급적 피한다.
- **길이**: 테이블 이름은 의미를 명확하게 전달하면서도 너무 길지 않게 작성한다. MySQL의 테이블 이름 길이 제한(64자)을 염두에 둔다. SAS 등 특정 도구와의 호환성을 위해 32자 이내로 제한해야 할 수도 있다.
- **연결 테이블**: 다대다 관계를 위한 연결 테이블의 이름은 연결되는 두 테이블의 이름을 조합하여 짓는다. 일반적으로 `table1_table2` 형식을 사용한다 (예: `users_roles`, `products_categories`).

### B. 컬럼 명명 규칙

- **케이스**: 컬럼 이름은 소문자 snake\_case를 사용한다 (예: `first_name`, `order_date`, `product_id`).
- **의미**: 컬럼 이름은 저장하는 데이터의 의미를 명확하게 나타내야 한다. 모호하거나 지나치게 축약된 이름(예: `nm`, `od`)은 피한다.
- **접두사/접미사**: 일반적으로 컬럼 이름에 테이블 이름을 접두사로 붙이지 않는다 (예: `users` 테이블에 `user_name` 대신 `name` 사용). 단, 외래 키(Foreign Key)의 경우 아래 규칙을 따른다.
- **예약어**: 테이블 이름과 마찬가지로 MySQL 예약어를 컬럼 이름으로 사용하지 않는다.
- **기본 키(Primary Key)**:

  - 단일 컬럼 기본 키의 이름은 `id`로 통일하는 것을 권장한다.
  - 또는 `<table_name>_id` 형식을 사용할 수도 있다 (예: `customer_id`, `order_id`). 이 방식은 여러 테이블 조인 시 컬럼 이름 충돌을 피하고 명확성을 높일 수 있다. 팀 내에서 일관된 방식을 선택한다.
- **외래 키(Foreign Key)**:

  - 참조하는 테이블의 기본 키 컬럼 이름과 동일하게 짓는 것을 권장한다. 만약 기본 키가 `id`라면, 외래 키 이름은 `<referenced_table_name>_id` 형식을 사용한다 (예: `orders` 테이블에서 `users` 테이블을 참조하는 외래 키는 `user_id`). 이는 어떤 테이블을 참조하는지 명확하게 보여준다.
  - 또는 `fk_` 접두사를 사용하여 `fk_<referenced_table_name>_id` 형식으로 명명할 수도 있다. 팀 내에서 일관된 방식을 선택한다.
- **Boolean 타입**: Boolean 값을 저장하는 컬럼은 `is_` 또는 `has_` 접두사를 사용한다 (예: `is_active`, `has_email_verified`).

# C. 인덱스 및 제약 조건 명명 규칙

- **형식**: `<type>_<table_name>_<column_names>` 형식을 사용한다.
- **`<type>`**: 인덱스 또는 제약 조건의 유형을 나타내는 약어

  - pk (Primary Key)
  - uk (Unique Key)
  - fk (Foreign Key)
  - idx (Index)
  - ck (Check)
- **`<table_name>`**: 해당 객체가 속한 테이블 이름
- **`<column_names>`**: 인덱스 또는 제약 조건에 포함된 컬럼 이름. 여러 컬럼인 경우 언더스코어(\_)로 연결
- **예시**:

  - `pk_users_id`: users 테이블의 id 컬럼에 대한 기본 키
  - `uk_users_email`: users 테이블의 email 컬럼에 대한 고유 키
  - `fk_orders_user_id`: orders 테이블의 user\_id 컬럼에 대한 외래 키
  - `idx_products_name_price`: products 테이블의 name과 price 컬럼에 대한 인덱스
- **일관성**: 프로젝트 내에서 일관된 명명 규칙을 적용하여 유지보수성과 가독성을 높인다.

# D. 데이터 타입 표준 (MySQL 기준)

데이터 타입을 효율적으로 선택하는 것은 저장 공간을 절약하고 성능을 향상시키는 데 중요하다.

## 정수형 (Integer Types)

- 데이터의 범위에 맞는 가장 작은 데이터 타입을 선택한다.

  - **TINYINT**: -128 ~ 127 (SIGNED), 0 ~ 255 (UNSIGNED). 상태 값, 플래그 등에 적합.
  - **SMALLINT**: -32,768 ~ 32,767 (SIGNED), 0 ~ 65,535 (UNSIGNED).
  - **MEDIUMINT**: -8,388,608 ~ 8,388,607 (SIGNED), 0 ~ 16,777,215 (UNSIGNED).
  - **INT**: -2,147,483,648 ~ 2,147,483,647 (SIGNED), 0 ~ 4,294,967,295 (UNSIGNED). 일반적인 ID, 카운터 등에 사용.
  - **BIGINT**: 매우 큰 범위의 정수. INT 범위를 초과할 경우 사용.
- 음수 값이 필요 없는 ID나 카운터 등에는 UNSIGNED 옵션을 사용하는 것이 좋다. 저장 공간은 동일하지만 양수 표현 범위가 2배로 늘어난다.

## 고정 소수점 (Fixed-Point)

- **DECIMAL(M, D)**: 금액과 같이 정확한 소수점 연산이 필요한 경우 반드시 사용한다. M은 총 자릿수, D는 소수점 이하 자릿수이다. FLOAT나 DOUBLE은 근사값을 저장하므로 금융 계산에 부적합하다.

## 부동 소수점 (Floating-Point)

- **FLOAT, DOUBLE**: 근사값을 저장하며, 과학 계산 등 정밀도가 중요하지 않은 경우 사용한다.
- FLOAT: 약 7자리 유효 숫자
- DOUBLE: 약 16자리 유효 숫자
- 금액 계산에는 절대 사용하지 않는다.
- FLOAT(M, D)나 DOUBLE(M, D) 형태는 사용하지 않는 것이 좋다.

## 문자열 (String Types)

- **VARCHAR(L)**: 가변 길이 문자열에 사용한다. 실제 저장된 데이터 길이만큼만 공간을 차지하므로 효율적이다. L은 최대 길이를 나타내며, 예상되는 최대 길이에 맞춰 적절한 크기를 지정한다. 무조건 VARCHAR(255)를 사용하는 것을 지양한다.
- **CHAR(L)**: 고정 길이 문자열에 사용한다. 항상 L 길이만큼 공간을 차지하며, 짧은 데이터가 저장되면 공백으로 채워진다. 국가 코드(CHAR(2)), 성별 코드(CHAR(1)) 등 길이가 항상 고정된 경우에만 제한적으로 사용한다.
- **TEXT** (및 TINYTEXT, MEDIUMTEXT, LONGTEXT): VARCHAR의 최대 길이(일반적으로 65,535 바이트)를 초과하는 긴 텍스트 데이터(게시글 내용, 로그 등)에 사용한다.
- **문자 집합 (Character Set)**: 다국어 지원이 필요하면 utf8mb4를 사용한다. 영문, 숫자, 기본 기호만 저장하는 컬럼(예: 코드 값, UUID)에는 ascii나 latin1을 사용하여 저장 공간을 절약할 수 있다.

## 날짜 및 시간 (Date and Time Types)

- **DATE**: 날짜만 저장 (YYYY-MM-DD). 생년월일 등에 적합.
- **DATETIME**: 날짜와 시간을 함께 저장 (YYYY-MM-DD HH:MM:SS). 특정 시점 기록에 사용. 타임존 정보는 포함하지 않는다.
- **TIMESTAMP**: 날짜와 시간을 함께 저장하며, 타임존 정보를 고려하여 UTC로 변환되어 저장된다. 조회 시 서버 또는 클라이언트의 타임존에 맞춰 변환된다. 생성/수정 시각 등 전 세계적으로 동일한 시점을 기록해야 할 때 유용하다. 일반적으로 TIMESTAMP 또는 타임존 정보가 포함된 DATETIME (MySQL 8.0 이상) 사용이 권장된다.
- **TIME**: 시간만 저장 (HH:MM:SS).
- **형식**: 날짜/시간 값을 문자열로 저장하지 말고, 반드시 해당 데이터 타입 컬럼에 저장한다. ISO 8601 형식 (YYYY-MM-DD HH:MM:SS)을 사용하는 것이 좋다.

## 기타

- **ENUM**: 미리 정의된 문자열 값 중 하나만 저장할 때 사용. 저장 공간이 작다(1 또는 2바이트). 값 목록이 적고 거의 변경되지 않는 경우에 유용하다. NULL 허용 대신 'UNKNOWN' 등의 기본값을 첫 번째 옵션으로 두는 것이 좋다.
- **BOOLEAN** (또는 BOOL): 내부적으로 TINYINT(1)로 처리된다. true/false 값을 저장하는 데 사용.

데이터 타입 선택 시 저장 공간 효율성과 쿼리 성능을 함께 고려해야 한다. 작은 데이터 타입과 적절한 인덱싱은 대규모 데이터 처리 시 성능에 큰 영향을 미친다.

# V. API 설계 표준

## A. RESTful API 설계 원칙

REST(Representational State Transfer)는 웹 서비스를 설계하기 위한 아키텍처 스타일로, 다음 원칙을 준수해야 한다[^1]:

- **자원(Resource)**: 모든 개념은 명사 형태의 자원으로 식별되고 URI(Uniform Resource Identifier)를 통해 표현된다[^2].
- **표현(Representation)**: 클라이언트는 자원의 상태를 특정 형식(주로 JSON)으로 주고받는다[^3].
- **메시지(Messages)**: 클라이언트와 서버는 메시지를 통해 통신하며, 메시지는 자원을 어떻게 처리할지에 대한 충분한 정보를 담고 있어야 한다(HTTP 메소드, 헤더 등).
- **상태 없음(Stateless)**: 서버는 클라이언트의 상태를 저장하지 않는다. 각 요청은 서버가 처리하는 데 필요한 모든 정보를 포함해야 한다[^1].
- **캐시 가능(Cacheable)**: 클라이언트는 서버 응답을 캐시할 수 있어야 한다. 서버는 응답의 캐시 가능 여부를 명시해야 한다[^1].
- **균일 인터페이스(Uniform Interface)**: 자원 식별(URI), 표현을 통한 자원 조작(HTTP 메소드 + Body), 자기 서술적 메시지, HATEOAS(Hypermedia As The Engine Of Application State) 원칙을 따른다[^1].
- **계층화 시스템(Layered System)**: 클라이언트는 최종 서버에 직접 연결되었는지, 중간 서버를 통해 연결되었는지 알 수 없다.

## B. 엔드포인트 URI 설계 규칙

URI는 API의 자원을 명확하고 일관되게 식별해야 한다.

- **명사 사용**: URI 경로에는 자원을 나타내는 명사를 사용하고, 동사(행위)는 사용하지 않는다. 행위는 HTTP 메소드로 표현한다[^2].

  - 좋은 예: `/users`, `/orders/{orderId}`
  - 나쁜 예: `/getUsers`, `/createOrder
- **복수 명사 사용**: 컬렉션(자원의 목록)을 나타내는 URI에는 복수 명사를 사용한다[^2].

  - 좋은 예: `/users`, `/products`
  - 나쁜 예: `/user`, `/product
- **계층 구조**: 자원 간의 관계는 경로 계층으로 표현할 수 있다. 단, 너무 깊은 계층(2단계 초과)은 피한다[^2].

  - 좋은 예: `/users/{userId}/orders` (특정 사용자의 주문 목록)
  - 허용 가능: `/users/{userId}/orders/{orderId}` (특정 사용자의 특정 주문)
  - 지양: `/users/{userId}/orders/{orderId}/products/{productId}` (관계는 응답 내 링크(HATEOAS)로 표현하는 것이 더 유연함)
- **소문자 사용**: URI 경로는 모두 소문자로 작성한다[^2].
- **단어 구분**: 경로 내 단어 구분에는 하이픈(-)(kebab-case)을 사용한다. 밑줄(\_)이나 CamelCase는 사용하지 않는다[^2].

  - 좋은 예: `/product-categories`
  - 나쁜 예: `/product_categories`, `/productCategories
- **파일 확장자 미포함**: URI 경로에 .json, .xml 등 파일 확장자를 포함하지 않는다. 응답 형식은 Accept 요청 헤더와 Content-Type 응답 헤더를 통해 결정한다(Content Negotiation)[^2].
- **쿼리 파라미터**: 컬렉션 자원의 필터링, 정렬, 페이징 등에는 쿼리 파라미터를 사용한다[^1].

  - 예: `/users?status=active&sort=name&page=1&size=20`
  - 쿼리 파라미터 이름은 lowerCamelCase 또는 snake\_case를 일관되게 사용한다[^2].

## C. HTTP 메소드 활용 기준

HTTP 메소드는 URI로 식별된 자원에 대한 행위를 정의한다. CRUD(Create, Read, Update, Delete) 작업에 맞춰 표준 메소드를 사용한다[^3].

- **GET**: 자원을 조회(Read)한다. 본문(body)을 가지지 않으며, 멱등성(idempotent)과 안전성(safe)을 가진다.

  - `/users`: 모든 사용자 목록 조회
  - `/users/{userId}`: 특정 사용자 정보 조회
- **POST**: 새로운 자원을 생성(Create)하거나, 하위 자원을 생성하거나, 특정 처리를 요청(멱등성 보장 안 됨)한다. 요청 본문을 포함한다.

  - `/users`: 새로운 사용자 생성
  - `/orders/{orderId}/cancel`: 특정 주문 취소 요청 (동사형 URI가 불가피한 경우 제한적 사용)
- **PUT**: 기존 자원을 전체적으로 수정(Update/Replace)한다. 요청 본문에 자원의 전체 표현을 포함하며, 멱등성을 가진다.

  - `/users/{userId}`: 특정 사용자의 전체 정보 수정
- **PATCH**: 기존 자원을 부분적으로 수정(Update)한다. 요청 본문에 변경할 필드만 포함하며, 멱등성을 보장하지 않을 수 있다. PUT보다 효율적일 수 있지만, 구현이 더 복잡할 수 있다.

  - `/users/{userId}`: 특정 사용자의 일부 정보(예: 이메일 주소)만 수정
- **DELETE**: 기존 자원을 삭제(Delete)한다. 멱등성을 가진다.

  - `/users/{userId}`: 특정 사용자 삭제

## D. 요청/응답 데이터 형식 표준화

- **JSON 사용**: 요청 본문과 응답 본문에는 JSON(JavaScript Object Notation) 형식을 표준으로 사용한다[^3]. JSON은 가볍고 가독성이 높으며, 대부분의 클라이언트 환경에서 쉽게 파싱할 수 있다[^4].
- **Content-Type 헤더**:

  - 요청 시: 클라이언트는 요청 본문이 JSON임을 명시하기 위해 `Content-Type: application/json` 헤더를 포함해야 한다[^3].
  - 응답 시: 서버는 응답 본문이 JSON임을 명시하기 위해 `Content-Type: application/json` 헤더를 포함해야 한다[^3]. Spring Boot는 일반적으로 이를 자동으로 처리한다.
- **JSON 필드 네이밍**: JSON 객체의 키(필드 이름)는 lowerCamelCase를 사용한다. 이는 자바스크립트 및 다수 클라이언트 라이브러리의 일반적인 관례와 일치한다[^2]. snake\_case도 가능하지만, 프로젝트 내에서 일관성을 유지해야 한다.
- **날짜 형식**: JSON 내 날짜 및 시간 정보는 ISO 8601 형식의 문자열(예: `"2024-03-15T10:30:55.123Z"` 또는 `"2024-03-15T19:30:55.123+09:00"`)로 표현한다[^4].
- **DTO 사용**: API 요청 및 응답에는 반드시 DTO(Data Transfer Object)를 사용한다. 도메인 객체(Entity)를 직접 노출하지 않는다. 이는 API 스펙과 내부 데이터 모델을 분리하고, 필요한 데이터만 선택적으로 노출하며, 유효성 검증 로직을 적용하는 데 유리하다[^3].
- **응답 압축**: 대규모 페이로드의 경우, 서버 설정(예: `server.compression.enabled=true` in application.yml)을 통해 응답을 gzip 등으로 압축하여 네트워크 대역폭을 절약하고 응답 시간을 개선하는 것을 고려한다[^1].

# E. API 버전 관리 전략

API는 시간이 지남에 따라 변경될 수 있습니다. 기존 클라이언트의 호환성을 유지하면서 API를 발전시키기 위해 명확한 버전 관리 전략이 필요합니다.

## 버전 명시 위치

**URI 경로(URL Path Versioning)**가 가장 일반적이고 권장되는 방법입니다.

- 예시: `/api/v1/users`, `/api/v2/products`
- 장점: 브라우저 테스트 용이, 버전이 명확하게 드러남, 캐싱 용이
- 단점: URI가 길어지고, 메이저 버전 변경 시 코드베이스 분기 필요 가능성

## 대안적 방법 (덜 권장됨)

1. **쿼리 파라미터**: `/api/users?version=1`

   - 구현은 간단하나 URI가 복잡해지고 라우팅이 어려울 수 있음
2. **커스텀 헤더**: `Accepts-version: 1.0` 또는 `Api-Version: 1`

   - URI는 깔끔하게 유지되나, 요청 생성 및 테스트가 번거로워질 수 있음
3. **Accept 헤더(Media Type Versioning)**: `Accept: application/vnd.example.v1+json`

   - RESTful 원칙에 가장 부합하지만, 구현 및 사용이 복잡함

## 버전 형식

- 메이저 버전 번호(예: v1, v2)를 사용하는 것이 일반적
- 마이너 변경(기능 추가 등 하위 호환성 유지)은 버전을 변경하지 않음
- 브레이킹 체인지(기존 기능 변경/삭제 등 하위 호환성 깨짐)가 발생할 경우에만 메이저 버전을 올림
- Semantic Versioning(MAJOR.MINOR.PATCH)을 내부적으로 사용하더라도, URI에는 일반적으로 MAJOR 버전만 표시

## 권장 전략

- \*\*URI 경로를 통한 메이저 버전 관리(/v1, /v2 등)를 기본 전략으로 채택
- **하위 호환성**: 가능하면 하위 호환성을 유지하도록 노력
  - 새로운 필드 추가는 허용
  - 기존 필드 삭제나 타입 변경은 브레이킹 체인지
  - 확장성을 고려한 설계로 브레이킹 체인지 최소화

# F. 오류 응답 표준 (RFC 7807)

API 오류 발생 시, 클라이언트가 문제를 이해하고 적절히 대응할 수 있도록 일관되고 상세한 오류 정보를 제공해야 합니다. 이를 위해 RFC 7807(Problem Details for HTTP APIs) 표준을 따르는 것을 권장합니다. Spring Boot 3는 ProblemDetail 객체를 통해 RFC 7807을 기본적으로 지원합니다.

## 기본 구성

- **Content-Type**: 오류 응답의 Content-Type 헤더는 `application/problem+json`으로 설정

## 표준 필드

RFC 7807 응답 본문(JSON)은 다음 표준 필드를 포함할 수 있습니다:

- **type** (string, URI): 문제 유형을 식별하는 URI. 문제에 대한 문서 링크 등을 제공할 수 있음. 기본값은 `about:blank` (필수 아님)
- **title** (string): 문제 유형에 대한 짧고 사람이 읽을 수 있는 요약. HTTP 상태 코드의 이유 구문과 같아서는 안 됨 (필수 아님)
- **status** (number): 해당 문제에 대한 HTTP 상태 코드 (필수 아님)
- **detail** (string): 문제 발생에 대한 사람이 읽을 수 있는 구체적인 설명 (필수 아님)
- **instance** (string, URI): 문제의 특정 발생을 식별하는 URI (필수 아님)

## 확장 필드(Extensions)

표준 필드 외에 추가적인 문제 관련 정보를 제공하기 위해 사용자 정의 필드를 포함할 수 있습니다. 예를 들어, 유효성 검사 오류 시 어떤 필드에서 오류가 발생했는지 상세 정보를 담을 수 있습니다.

## HTTP 상태 코드

오류 유형에 맞는 적절한 HTTP 상태 코드를 사용해야 합니다:

- **400 Bad Request**: 클라이언트 요청 오류 (예: 잘못된 파라미터, 유효성 검사 실패)
- **401 Unauthorized**: 인증 실패 (로그인 필요)
- **403 Forbidden**: 인가 실패 (권한 없음)
- **404 Not Found**: 요청한 리소스를 찾을 수 없음
- **405 Method Not Allowed**: 허용되지 않은 HTTP 메소드 사용
- **409 Conflict**: 리소스 상태 충돌 (예: 중복 생성 시도)
- **415 Unsupported Media Type**: 지원하지 않는 요청 본문 형식
- **429 Too Many Requests**: 요청 속도 제한 초과
- **500 Internal Server Error**: 서버 내부 오류 (예상치 못한 예외 발생)
- **502 Bad Gateway**: 게이트웨이 또는 프록시 오류
- **503 Service Unavailable**: 서버 과부하 또는 유지보수로 인한 일시적 서비스 불가

## 구현

Spring Boot에서는 `@ControllerAdvice`와 `@ExceptionHandler`를 사용하여 예외를 처리하고, 핸들러 메소드에서 `ProblemDetail` 객체를 생성하여 반환함으로써 RFC 7807 형식의 오류 응답을 쉽게 구현할 수 있습니다. (자세한 내용은 VII. 예외 처리 전략 참조)

RFC 7807을 사용하면 다양한 API에서 발생하는 오류를 일관된 방식으로 표현할 수 있어, 클라이언트 개발자가 오류 처리 로직을 표준화하고 자동화하는 데 큰 도움이 됩니다.

# VI. MyBatis 사용 표준

## A. Mapper 인터페이스 및 XML 작성 규칙

MyBatis는 SQL 쿼리를 별도의 XML 파일 또는 어노테이션에 작성하여 자바 코드와 분리함으로써 유지보수성을 높입니다.

### Mapper 인터페이스

- 데이터 접근 로직을 정의하는 자바 인터페이스는 repository 패키지 하위에 위치시킵니다.
- 인터페이스 이름은 `<Domain>Mapper` 형식을 따릅니다 (예: `UserMapper`, `OrderMapper`).
- 메소드 이름은 수행하는 SQL 작업을 명확히 나타내야 합니다 (예: `findById`, `insertUser`, `updateOrderStatus`).
- Spring Boot 환경에서는 `@Mapper` 어노테이션을 인터페이스에 추가하거나, 메인 애플리케이션 클래스 또는 설정 클래스에 `@MapperScan` 어노테이션을 사용합니다.

### XML 매퍼 파일

- 복잡한 SQL이나 동적 SQL을 사용할 경우 XML 매퍼 파일을 사용합니다.
- XML 파일은 `src/main/resources/mybatis/mapper/` 또는 `src/main/resources/com/example/projectname/repository/` 등 일관된 위치에 저장합니다. `application.yml`에서 `mybatis.mapper-locations` 속성으로 위치를 지정할 수 있습니다.
- XML 파일 이름은 해당 Mapper 인터페이스 이름과 동일하게 합니다 (예: `UserMapper.xml`, `OrderMapper.xml`).
- XML 파일의 `<mapper>` 태그의 namespace 속성 값은 해당 Mapper 인터페이스의 FQCN과 일치해야 합니다 (예: `com.example.projectname.repository.UserMapper`).
- `<select>`, `<insert>`, `<update>`, `<delete>` 태그의 id 속성 값은 Mapper 인터페이스의 메소드 이름과 일치해야 합니다.
- `parameterType` 속성은 전달되는 파라미터의 타입을 명시합니다 (선택 사항이지만 명시 권장).
- 조회 결과 매핑은 다음과 같이 처리합니다:
  - `resultType`: 간단한 매핑에 사용하며, `mybatis.configuration.map-underscore-to-camel-case=true` 설정으로 자동 변환을 활성화합니다.
  - `<resultMap>`: 복잡한 매핑(컬럼명과 필드명 불일치, 연관 관계 매핑 등)에 사용합니다.

### 어노테이션 vs XML

- 간단한 CRUD 쿼리는 `@Select`, `@Insert`, `@Update`, `@Delete` 어노테이션을 사용할 수 있습니다.
- 복잡한 쿼리, 동적 SQL, 재사용 가능한 SQL 조각(`<sql>`)은 XML 매퍼 파일이 더 유리합니다.
- 본 표준에서는 XML 매퍼 파일 사용을 기본으로 권장하되, 매우 간단한 쿼리에 한해 어노테이션 사용을 허용합니다.

## B. SQL 쿼리 스타일 가이드라인

XML 매퍼 파일 내 SQL 쿼리는 가독성과 일관성을 위해 다음 스타일을 따릅니다:

### 일반 규칙

- SQL 키워드(SELECT, FROM, WHERE 등)는 대문자로 작성합니다.
- 가독성을 위해 적절한 들여쓰기와 줄바꿈을 사용합니다:
  - SELECT 절의 각 컬럼은 새로운 줄에서 시작하고 들여씁니다.
  - FROM 절 다음에 테이블 이름을 명시합니다.
  - JOIN 절은 새로운 줄에서 시작하고, ON 조건은 들여씁니다.
  - WHERE 절 다음 첫 조건은 같은 줄에 쓰고, 이후 AND/OR 조건은 새로운 줄에서 시작합니다.
  - GROUP BY, ORDER BY 절도 새로운 줄에서 시작합니다.

### 별칭 및 바인딩

- 테이블 별칭은 의미 있는 이름(예: `users u`, `orders o`)을 사용하고, AS 키워드를 명시적으로 사용합니다.
- 컬럼 별칭도 필요 시 AS 키워드로 명확하게 지정합니다.
- 파라미터 바인딩은 `#{propertyName}` 구문을 사용합니다.
- `${propertyName}` 구문은 SQL Injection 취약점을 유발하므로 사용을 제한합니다.
- `SELECT *` 사용을 금지하고 조회할 컬럼을 명시적으로 나열합니다.
- 복잡한 로직에는 SQL 주석(`--` 또는 `/*... */`)을 사용합니다.

### 예시

```
<select id="findUsersByCriteria" parameterType="map" resultMap="userResultMap">
    SELECT
        u.id            AS userId,
        u.username      AS userName,
        u.email         AS userEmail,
        u.created_at    AS createdAt,
        r.role_name     AS roleName
    FROM
        users u
    LEFT JOIN
        user_roles ur ON u.id = ur.user_id
    LEFT JOIN
        roles r ON ur.role_id = r.id
    <where>
        <if test="username != null and username != ''">
            AND u.username LIKE CONCAT('%', #{username}, '%')
        </if>
        <if test="email != null and email != ''">
            AND u.email = #{email}
        </if>
        <if test="roleId != null">
            AND r.id = #{roleId}
        </if>
        AND u.is_active = true
    </where>
    ORDER BY
        u.created_at DESC
    <if test="limit != null and offset != null">
        LIMIT #{limit} OFFSET #{offset}
    </if>
</select>
```

## C. 동적 SQL 작성법

MyBatis의 동적 SQL 기능은 조건에 따라 SQL 구문을 동적으로 변경할 때 유용합니다.

### 주요 요소

- `<if test="...">`: 조건이 true일 경우 내부 SQL 구문을 포함시킵니다.
- `<choose>`, `<when>`, `<otherwise>`: 여러 조건 중 하나만 만족하는 SQL 구문을 생성합니다.
- `<where>`: WHERE 절을 동적으로 생성하며, 불필요한 AND/OR를 자동으로 처리합니다.
- `<set>`: UPDATE 문에서 SET 절을 동적으로 생성하며, 불필요한 콤마(,)를 자동으로 처리합니다.
- `<foreach>`: 컬렉션 요소를 반복 처리하며, 주로 IN 절 생성에 사용됩니다.
  - `collection`: 반복할 대상 파라미터 이름
  - `item`: 각 반복 요소에 접근하기 위한 변수 이름
  - `index`: 반복 인덱스에 접근하기 위한 변수 이름
  - `open`: 반복 결과의 시작 문자열 (예: `(`)
  - `close`: 반복 결과의 종료 문자열 (예: `)`)
  - `separator`: 각 반복 요소 사이의 구분자 (예: `,`)
- `<trim>`: 생성된 SQL 구문의 앞/뒤에 문자열을 추가하거나 제거합니다.
- `<sql>`, `<include>`: 재사용 가능한 SQL 조각을 정의하고 참조합니다.

### 추가 고려사항

- 동적 SQL 로직이 복잡해지면 `@SelectProvider`, `@InsertProvider` 등을 사용한 자바 코드 기반 SQL 생성을 고려합니다.
- 다양한 파라미터 조합에 대해 동적 SQL을 철저히 테스트합니다.

## D. 트랜잭션 관리 정책

데이터의 일관성과 무결성을 보장하기 위해 트랜잭션 관리는 필수적입니다.

### 기본 원칙

- **선언적 트랜잭션 관리**: Spring의 `@Transactional` 어노테이션을 표준으로 채택합니다. 이는 비즈니스 로직과 트랜잭션 관리 코드를 분리하여 코드 침투성을 최소화하고 가독성을 높입니다.
- **프로그래밍 방식 트랜잭션 관리**(TransactionTemplate 등)는 특별한 경우가 아니면 사용하지 않습니다.

### 설정 가이드라인

- Spring Boot는 `spring-boot-starter-jdbc` 또는 `spring-boot-starter-data-jpa` 의존성과 DataSource 빈이 존재하면 자동으로 DataSourceTransactionManager를 설정합니다. MyBatis 사용 시 이 자동 설정을 활용하세요.
- 트랜잭션 관리자의 DataSource는 SqlSessionFactoryBean이 사용하는 DataSource와 반드시 동일해야 합니다.
- JTA를 사용하는 환경(예: 분산 트랜잭션)에서는 JtaTransactionManager를 설정해야 합니다.

### @Transactional 사용 지침

#### 위치 및 범위

- **클래스 레벨**: Service 계층의 클래스에 선언하여 모든 public 메소드가 트랜잭션 내에서 실행되도록 합니다.
- **메소드 레벨**: 특정 메소드에 다른 트랜잭션 속성이 필요한 경우 메소드에 별도로 선언하여 오버라이드합니다.

#### 주요 속성 설정

- **전파(Propagation)**: 기본값은 `REQUIRED`(기존 트랜잭션에 참여하거나 새로 시작). 다른 전파 수준은 명확한 요구사항이 있을 때만 신중하게 사용합니다.
- **격리 수준(Isolation)**: 일반적으로 데이터베이스의 기본 격리 수준을 사용하나, 필요시 명시적으로 지정(`@Transactional(isolation = Isolation.READ_COMMITTED)`)할 수 있습니다.
- **읽기 전용(Read-Only)**: 조회 메소드에는 `@Transactional(readOnly = true)`를 지정하여 성능 최적화합니다.

#### 롤백 규칙

- **기본 동작**: Unchecked Exception 발생 시 롤백, Checked Exception 발생 시 커밋
- **중요**: 의도치 않은 커밋을 방지하기 위해 비즈니스 예외에 대한 롤백 정책을 명확히 정의해야 합니다.
- **표준 정책**: 롤백이 필요한 Checked Exception에는 반드시 `@Transactional(rollbackFor = {SpecificCheckedException.class})` 또는 `@Transactional(rollbackFor = Exception.class)`를 지정하세요.

#### 프록시 동작 주의사항

- `@Transactional`은 Spring AOP 프록시를 통해 동작하므로 적용 메소드는 반드시 public이어야 합니다.
- 동일 클래스 내 내부 호출(`this.method()`)에는 트랜잭션이 적용되지 않으므로 항상 Service 빈을 주입받아 호출해야 합니다.

## VII. 예외 처리 전략

### A. Checked vs. Unchecked Exceptions 구분

#### Checked Exceptions

- **특징**: Exception 클래스를 상속하되 RuntimeException 계열이 아닌 예외
- **처리 요구사항**: 컴파일 시점에 확인되어 반드시 throws 선언 또는 try-catch로 처리해야 함
- **적용 상황**:
  - 외부 요인(네트워크, 파일 시스템) 관련 문제
  - 예측 가능하고 복구 가능한 비즈니스 규칙 위반(잔고 부족, 중복 ID 등)

#### Unchecked Exceptions

- **특징**: RuntimeException 또는 Error 클래스를 상속하는 예외
- **처리 요구사항**: 컴파일 시점에 확인되지 않으며, 명시적 처리 의무 없음
- **적용 상황**:
  - 프로그래밍 오류(null 참조, 잘못된 인자, 배열 범위 초과 등)
  - 시스템 레벨의 심각한 오류(메모리 부족 등)

#### 사용 가이드라인

- **복구 가능성 기준**: 호출자가 예외 상황을 인지하고 대응할 수 있는 경우 Checked Exception 사용
- **프로그래밍 오류**: 개발자의 실수로 인한 예외는 Unchecked Exception 사용
- **구체적 예외 처리**: `catch (Exception e)`와 같은 포괄적 처리 대신 구체적인 예외 타입을 처리
- **예외 전파**: 예외를 다시 던질 때는 원본 예외를 cause로 설정하여 스택 트레이스 보존

### B. 사용자 정의 예외 설계

#### 목적

- 구체적이고 의미 있는 오류 정보 전달
- 문제 파악 및 디버깅 용이성 향상

#### 설계 원칙

- **계층 구조**: 공통 기반 예외 클래스 정의 후 구체적 예외 클래스가 상속
- **명명 규칙**: 예외 이름은 문제 상황을 명확히 표현(예: `ResourceNotFoundException`)
- **컨텍스트 정보**: 오류 메시지 외에도 문제 해결에 도움되는 정보(ID, 필드명 등) 포함

#### 예시 구현

```
// 리소스를 찾지 못한 경우 (Unchecked)
public class ResourceNotFoundException extends RuntimeException {
    private final String resourceType;
    private final Object resourceId;

    public ResourceNotFoundException(String resourceType, Object resourceId) {
        super(String.format("%s not found with id %s", resourceType, resourceId));
        this.resourceType = resourceType;
        this.resourceId = resourceId;
    }
    // Getters...
}

// 입력 데이터 유효성 검증 실패 (Unchecked)
public class InvalidInputDataException extends RuntimeException {
    private final List<FieldError> errors;

    public InvalidInputDataException(String message, List<FieldError> errors) {
        super(message);
        this.errors = errors;
    }
    // Getter...
}

// 비즈니스 규칙 위반 - 재고 부족 (Checked)
public class InsufficientStockException extends Exception {
    private final String productId;
    private final int requestedQuantity;
    private final int availableQuantity;

    public InsufficientStockException(String productId, int requestedQuantity, int availableQuantity) {
        super(String.format("Insufficient stock for product %s. Requested: %d, Available: %d",
                productId, requestedQuantity, availableQuantity));
        this.productId = productId;
        this.requestedQuantity = requestedQuantity;
        this.availableQuantity = availableQuantity;
    }
    // Getters...
}
```

## E. 전역 예외 처리 방식 개선안

### @ControllerAdvice와 @ExceptionHandler를 활용한 예외 처리 표준화

Spring MVC/WebFlux 기반의 REST API에서 발생하는 예외를 일관되게 처리하고 표준화된 오류 응답을 반환하기 위해 @ControllerAdvice와 @ExceptionHandler를 사용한 전역 예외 처리 방식을 도입합니다.

### 핵심 개념

- **@ControllerAdvice**: 애플리케이션 전역에서 발생하는 예외를 처리하는 컴포넌트를 정의합니다. 여러 컨트롤러에 걸쳐 예외 처리 로직을 중앙화할 수 있습니다.
- **@ExceptionHandler**: 특정 예외 타입(또는 하위 타입)을 처리할 메소드를 지정합니다.

  - 예: `@ExceptionHandler(ResourceNotFoundException.class)`
  - 다중 예외 처리: `@ExceptionHandler({Type1Exception.class, Type2Exception.class})`
  - 구체적인 예외 핸들러가 우선 선택되므로, 일반적인 `Exception.class` 핸들러는 마지막에 배치하세요.

### 핸들러 메소드 설계

- **파라미터**: 예외 객체, WebRequest/HttpServletRequest 등을 받을 수 있음
- **반환 타입**: RFC 7807 준수를 위해 `ResponseEntity<ProblemDetail>` 권장
- **상태 코드**: 각 예외 유형에 적합한 HTTP 상태 코드 사용

### RFC 7807 (ProblemDetail) 구현 방법

- `ProblemDetail.forStatusAndDetail(HttpStatus, String)` 활용
- 추가 정보 설정: `setTitle()`, `setType()`, `setInstance()`, `setProperty()` 등
- Content-Type: `application/problem+json` 자동 적용

## 구현 예시

```
import org.springframework.http.HttpStatus;
import org.springframework.http.ProblemDetail;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.context.request.WebRequest;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.URI;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@ControllerAdvice
public class GlobalExceptionHandler {

    private static final Logger log = LoggerFactory.getLogger(GlobalExceptionHandler.class);

    // 리소스 찾을 수 없음 예외 (404)
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ProblemDetail> handleResourceNotFoundException(ResourceNotFoundException ex, WebRequest request) {
        ProblemDetail problemDetail = ProblemDetail.forStatusAndDetail(HttpStatus.NOT_FOUND, ex.getMessage());
        problemDetail.setTitle("Resource Not Found");
        problemDetail.setType(URI.create("/errors/resource-not-found"));
        problemDetail.setInstance(URI.create(request.getDescription(false)));
        log.warn("Resource not found: {}", ex.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(problemDetail);
    }

    // 잘못된 입력 데이터 예외 (400)
    @ExceptionHandler(InvalidInputDataException.class)
    public ResponseEntity<ProblemDetail> handleInvalidInputDataException(InvalidInputDataException ex, WebRequest request) {
        ProblemDetail problemDetail = ProblemDetail.forStatusAndDetail(HttpStatus.BAD_REQUEST, ex.getMessage());
        problemDetail.setTitle("Invalid Input Data");
        problemDetail.setType(URI.create("/errors/invalid-input"));
        problemDetail.setInstance(URI.create(request.getDescription(false)));

        // 상세 오류 정보 추가
        if (ex.getErrors() != null && !ex.getErrors().isEmpty()) {
            problemDetail.setProperty("invalidFields", ex.getErrors());
        }

        log.warn("Invalid input data: {}", ex.getMessage());
        return ResponseEntity.badRequest().body(problemDetail);
    }

    // Bean Validation 예외 처리 (@Valid)
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ResponseEntity<ProblemDetail> handleValidationExceptions(MethodArgumentNotValidException ex, WebRequest request) {
        ProblemDetail problemDetail = ProblemDetail.forStatus(HttpStatus.BAD_REQUEST);
        problemDetail.setTitle("Validation Failed");
        problemDetail.setType(URI.create("/errors/validation-error"));
        problemDetail.setInstance(URI.create(request.getDescription(false)));

        List<Map<String, String>> errors = ex.getBindingResult().getFieldErrors().stream()
              .map(fieldError -> Map.of(
                    "field", fieldError.getField(),
                    "message", fieldError.getDefaultMessage() != null ? fieldError.getDefaultMessage() : "Invalid value"
                ))
              .collect(Collectors.toList());

        problemDetail.setProperty("errors", errors);
        problemDetail.setDetail("Input validation failed for one or more fields.");
        log.warn("Validation failed: {}", errors);
        return ResponseEntity.badRequest().body(problemDetail);
    }

    // 비즈니스 로직 예외 (409 Conflict)
    @ExceptionHandler(InsufficientStockException.class)
    public ResponseEntity<ProblemDetail> handleInsufficientStockException(InsufficientStockException ex, WebRequest request) {
        ProblemDetail problemDetail = ProblemDetail.forStatusAndDetail(HttpStatus.CONFLICT, ex.getMessage());
        problemDetail.setTitle("Insufficient Stock");
        problemDetail.setType(URI.create("/errors/insufficient-stock"));
        problemDetail.setInstance(URI.create(request.getDescription(false)));

        // 비즈니스 관련 정보 추가
        problemDetail.setProperty("productId", ex.getProductId());
        problemDetail.setProperty("requestedQuantity", ex.getRequestedQuantity());
        problemDetail.setProperty("availableQuantity", ex.getAvailableQuantity());

        log.warn("Insufficient stock: {}", ex.getMessage());
        return ResponseEntity.status(HttpStatus.CONFLICT).body(problemDetail);
    }

    // 기타 모든 예외 처리 (500)
    @ExceptionHandler(Exception.class)
    public ResponseEntity<ProblemDetail> handleGenericException(Exception ex, WebRequest request) {
        ProblemDetail problemDetail = ProblemDetail.forStatusAndDetail(
            HttpStatus.INTERNAL_SERVER_ERROR, 
            "An unexpected internal server error occurred."
        );
        problemDetail.setTitle("Internal Server Error");
        problemDetail.setType(URI.create("/errors/internal-server-error"));
        problemDetail.setInstance(URI.create(request.getDescription(false)));

        // 보안을 위해 클라이언트에게 상세 오류 정보 노출 제한
        log.error("Unhandled exception occurred: {}", request.getDescription(false), ex);
        return ResponseEntity.internalServerError().body(problemDetail);
    }
}
```

## 발전 방향 및 고려사항

1. **예외 계층 구조**: 비즈니스 예외들을 위한 BaseException을 정의하여 예외 처리 일관성 확보
2. **다국어 지원**: 오류 메시지를 다국어로 제공하기 위한 MessageSource 활용
3. **환경별 오류 응답 차별화**: 개발 환경에서는 디버깅을 위한 상세 정보 제공, 운영 환경에서는 최소화
4. **모니터링 연계**: 특정 예외 발생 시 알림 트리거나 모니터링 시스템과 연동

이러한 전역 예외 처리 방식은 컨트롤러 로직을 깔끔하게 유지하고, API 전체에 걸쳐 일관된 오류 응답 형식을 보장하며, 유지보수를 용이하게 합니다. RFC 7807 표준을 준수함으로써 API 클라이언트와의 상호 운용성도 크게 향상됩니다.

# VIII. 로깅 표준

## A. 로깅 프레임워크 및 설정

효과적인 로깅은 애플리케이션의 동작을 추적하고, 문제를 진단하며, 성능을 모니터링하는 데 필수적이다.

- **프레임워크**: SLF4j (Simple Logging Facade for Java)를 로깅 퍼사드(Facade)로 사용하고, Logback 또는 log4j2을 실제 로깅 구현체(Implementation)로 사용한다. Spring Boot는 spring-boot-starter-logging(대부분의 starter에 포함됨)을 통해 이 조합을 기본으로 제공하며, 다른 로깅 프레임워크(JUL, Commons Logging, Log4j)를 사용하는 라이브러리의 로그도 SLF4j를 통해 라우팅한다. Lombok의 `@Slf4j` 어노테이션을 사용하여 로거 인스턴스를 간편하게 생성하는 것을 권장한다.
- **설정**:

  - **기본 설정**: `application.yml` 또는 `application.properties` 파일의 `logging.*` 속성을 통해 기본적인 로깅 레벨, 로그 파일 경로 등을 설정할 수 있다.
  - **고급 설정**: 더 세부적인 설정(Appender 구성, 패턴 변경, 프로파일별 설정 등)을 위해서는 `src/main/resources` 디렉토리에 `logback-spring.xml` 파일을 생성하여 Logback 설정을 직접 구성하는 것을 권장한다. `logback.xml`도 사용 가능하지만, `logback-spring.xml`은 Spring Boot 환경에 더 특화된 기능(예: Spring 프로파일 연동)을 지원한다.
  - **Spring 프로파일 연동**: `logback-spring.xml` 내에서 `<springProfile name="...">` 태그를 사용하여 개발(dev), 테스트(test), 운영(prod) 등 환경별로 다른 로깅 설정을 적용할 수 있다. 예를 들어, 개발 환경에서는 DEBUG 레벨로 더 상세한 로그를 남기고, 운영 환경에서는 INFO 레벨 이상만 기록하도록 설정할 수 있다.

## B. 로그 레벨 활용 기준

로그 레벨은 로그 메시지의 중요도를 나타내며, 설정된 레벨 이상의 로그만 기록된다. 적절한 로그 레벨을 사용하는 것이 중요하다.

- **레벨 (심각도 순)**: ERROR > WARN > INFO > DEBUG > TRACE (Logback은 SLF4j의 FATAL 레벨을 ERROR로 매핑한다).
- **사용 지침**:

  - **ERROR**: 심각한 오류 발생으로 인해 애플리케이션의 정상적인 기능 수행이 불가능하거나 중요한 작업이 실패한 경우 사용한다. 즉각적인 조치가 필요한 상황이다. 예외 발생 시 스택 트레이스와 함께 기록한다.
  - **WARN**: 당장 에러는 아니지만 잠재적인 문제(예: deprecated API 사용, 설정 오류 가능성)나 예상치 못한 상황이 발생했으나 애플리케이션 동작은 계속되는 경우 사용한다. 주의가 필요한 상황이다.
  - **INFO**: 애플리케이션의 주요 진행 상황이나 상태 변경을 나타내는 정보성 메시지에 사용한다. 사용자의 주요 액션, 서비스 시작/종료, 주요 작업 완료 등을 기록한다. 운영 환경의 기본 로그 레벨로 권장된다.
  - **DEBUG**: 개발 및 문제 해결 과정에서 시스템 내부 동작을 상세히 추적하기 위해 사용한다. 특정 로직의 변수 값, 메소드 호출 흐름 등을 기록한다. 운영 환경에서는 기본적으로 비활성화하고, 필요 시 특정 모듈에 대해서만 일시적으로 활성화한다.
  - **TRACE**: DEBUG보다 더 상세한 정보를 기록한다. 메소드 호출의 시작과 끝, 매우 세밀한 단계별 진행 상황 등을 기록한다. 극히 예외적인 디버깅 상황에서만 사용하며, 운영 환경에서는 거의 사용하지 않는다.
- **레벨 설정**: `application.yml` 또는 `logback-spring.xml`에서 전역 레벨(`logging.level.root`)과 패키지/클래스별 레벨(`logging.level.<package_or_class_name>`)을 설정한다. 운영 환경에서는 root 레벨을 INFO로 설정하고, 문제 발생 시 필요한 부분만 DEBUG로 조정하는 방식을 권장한다.

## C. 로그 포맷 표준 (JSON)

로그는 사람이 읽기 쉬울 뿐만 아니라, 기계(로그 분석 시스템)가 파싱하고 분석하기 쉬워야 한다. 이를 위해 구조화된 로깅(Structured Logging), 특히 JSON 형식을 표준 로그 포맷으로 채택한다.

- **장점**: JSON 형식은 키-값 쌍으로 데이터를 명확하게 표현하여 로그 분석 도구(ELK Stack, Splunk, Graylog 등)에서 필터링, 검색, 집계, 시각화가 용이하다.
- **설정**: `logback-spring.xml`에서 LogstashEncoder (Logstash용 JSON 인코더)나 JsonEncoder 등을 사용하여 JSON 포맷으로 로그를 출력하도록 설정한다.
- **표준 필드**: 모든 JSON 로그 항목에 다음 필드를 포함하는 것을 권장한다. 일관된 스키마를 유지하는 것이 중요하다.

  - **timestamp**: 로그 발생 시각. ISO 8601 형식 (YYYY-MM-DDTHH:mm:ss.SSSZ 또는 타임존 포함)을 사용한다.
  - **level**: 로그 레벨 (예: "INFO", "ERROR").
  - **thread\_name**: 로그를 기록한 스레드 이름.
  - **logger\_name**: 로거 이름 (일반적으로 FQCN).
  - **message**: 실제 로그 메시지.
  - **app\_name**: 애플리케이션 이름 (spring.application.name 값).
  - **exception** (선택 사항): 예외 발생 시 예외 클래스 이름, 메시지, 스택 트레이스 정보.
- **컨텍스트 필드 (MDC)**: SLF4j의 MDC(Mapped Diagnostic Context)를 사용하여 추가적인 컨텍스트 정보를 포함시킨다. 이는 분산 환경에서 요청 추적이나 사용자별 문제 분석에 매우 중요하다.

  - **trace\_id**: 분산 트레이싱 시스템의 추적 ID.
  - **span\_id**: 분산 트레이싱 시스템의 스팬 ID.
  - **user\_id** (선택 사항): 요청을 발생시킨 사용자 ID (민감 정보 처리 주의).
  - **request\_id** (선택 사항): 특정 요청을 식별하는 고유 ID.

- **JSON 로그 예시**:

| 필드명 | 예시 값 | 설명 |
| --- | --- | --- |
| timestamp | "2024-03-15T10:30:55.123Z" | ISO 8601 형식의 로그 발생 시각 |
| level | "INFO" | 로그 레벨 |
| thread\_name | "http-nio-8080-exec-1" | 스레드 이름 |
| logger\_name | "com.example.projectname.service.OrderService" | 로거 이름 (클래스 FQCN) |
| message | "Order ORD-12345 processed successfully" | 로그 메시지 |
| app\_name | "order-service" | 애플리케이션 이름 |
| trace\_id | "a1b2c3d4e5f6a7b8" | 분산 추적 ID (MDC) |
| user\_id | "user\_abc" | 사용자 ID (MDC, 선택 사항) |
| exception | { "class": "...", "message": "...", "stacktrace": "..." } | 예외 정보 (발생 시) |
| custom\_field | "value" | 기타 필요한 컨텍스트 정보 (MDC 등) |

## D. 로깅 Best Practice

효과적이고 효율적인 로깅을 위한 추가적인 모범 사례는 다음과 같다.

- **플레이스홀더 사용**: 문자열 연결(+) 대신 SLF4j의 파라미터화된 로깅({})을 사용한다. 로그 레벨이 비활성화된 경우 불필요한 문자열 객체 생성 및 연결 비용을 피할 수 있어 성능에 유리하다.

  - Good: `log.info("Processing order {} for user {}", orderId, userId);`
  - Bad: `log.info("Processing order " + orderId + " for user " + userId);
- **예외 로깅**: 예외 발생 시, 예외 객체를 로깅 메소드의 마지막 인자로 전달하여 스택 트레이스가 자동으로 기록되도록 한다. e.getMessage()만 기록하면 원인 파악에 필요한 정보가 누락된다.

  - Good: `log.error("Failed to process order {}", orderId, e);`
  - Bad: `log.error("Failed to process order {}: {}", orderId, e.getMessage());
- **민감 정보 로깅 금지**: 비밀번호, API 키, 개인 식별 정보(주민등록번호, 전체 신용카드 번호 등)와 같은 민감 정보는 절대 로그에 기록하지 않는다. 필요한 경우 마스킹 또는 익명화 처리를 한다.
- **컨텍스트 정보 활용 (MDC)**: 웹 요청 처리 시, 요청 시작 시점에 MDC에 traceId, requestId, userId 등의 컨텍스트 정보를 설정하고 요청 종료 시점에 제거한다. 이렇게 하면 해당 요청 처리 중 발생하는 모든 로그에 컨텍스트 정보가 자동으로 포함되어, 특정 요청의 흐름을 추적하거나 사용자별 문제를 분석하는 데 매우 유용하다. Spring Cloud Sleuth와 같은 분산 트레이싱 라이브러리는 traceId, spanId를 MDC에 자동으로 설정해준다.
- **성능 고려**: 반복문 내부나 초당 수백/수천 번 호출되는 성능에 민감한 코드 경로에서는 로깅 호출을 최소화한다. 특히 INFO 레벨 이상의 로그는 신중하게 사용한다. 메소드 진입/종료 로그는 DEBUG 또는 TRACE 레벨로 기록한다.
- **로그 메시지 명확성**: 로그 메시지는 모호하지 않고, 어떤 상황에서 왜 기록되었는지 명확하게 전달해야 한다. "Error occurred"와 같은 메시지보다는 "User login failed due to incorrect password for user ID: 123"와 같이 구체적인 정보를 포함한다.
- **로그 파일 관리**: `logback-spring.xml`에서 로그 파일 로테이션(크기 기반, 시간 기반) 및 보존 정책을 설정하여 디스크 공간을 효율적으로 관리한다.
- **중앙 집중식 로깅**: 마이크로서비스 환경에서는 로그를 파일에 쓰는 것 외에도 Fluentd, Logstash 등을 사용하여 중앙 로그 수집 시스템(예: ELK Stack, Graylog)으로 전송하는 것을 고려한다. 이를 통해 여러 서비스의 로그를 통합적으로 검색하고 분석할 수 있다.

구조화된 JSON 로깅과 MDC를 활용한 컨텍스트 정보 기록은 현대적인 분산 시스템 환경에서 필수적인 로깅 관행이다. 이를 통해 문제 해결 시간을 단축하고 시스템 가시성을 확보할 수 있다.

#### 참고 자료

1. Spring Boot 3.3 best practices | OpenRewrite Docs, 4월 23, 2025에 액세스, <https://docs.openrewrite.org/recipes/java/spring/boot3/springboot33bestpractices>
2. Spring Boot 3.4 best practices | OpenRewrite Docs, 4월 23, 2025에 액세스, <https://docs.openrewrite.org/recipes/java/spring/boot3/springboot3bestpractices>
3. arsy786/springboot-best-practices: This repo serves as a ... - GitHub, 4월 23, 2025에 액세스, <https://github.com/arsy786/springboot-best-practices>
4. Spring Boot Reference Documentation, 4월 23, 2025에 액세스, <https://docs.spring.io/spring-boot/docs/3.0.x/reference/htmlsingle/>
5. Code Style · spring-projects/spring-framework Wiki · GitHub, 4월 23, 2025에 액세스, <https://github.com/spring-projects/spring-framework/wiki/Code-Style>
6. Google Java Style Guide, 4월 23, 2025에 액세스, <https://google.github.io/styleguide/javaguide.html>
7. Naming Conventions for Database Objects - MySQL :: Developer Zone, 4월 23, 2025에 액세스, <https://dev.mysql.com/doc/dev/mysql-server/9.1.0/PAGE_NAMING_CONVENTIONS.html>
8. java-families-docs/mybatis/mybatis-guidelines.md at main - GitHub, 4월 23, 2025에 액세스, <https://github.com/jovanliuc/java-families-docs/blob/main/mybatis/mybatis-guidelines.md>
9. Coding Standards - MyBatis Dynamic SQL, 4월 23, 2025에 액세스, <https://mybatis.org/mybatis-dynamic-sql/docs/codingStandards.html>
10. Mastering Lombok: The Ultimate Guide to Simplifying Java Development - Codesarray, 4월 23, 2025에 액세스, <https://codesarray.com/view/Mastering-Lombok:-The-Ultimate-Guide-to-Simplifying-Java-Development>
11. Google Style Guides | styleguide, 4월 23, 2025에 액세스, <https://google.github.io/styleguide/>
12. 9. Naming Conventions - Java - Oracle, 4월 23, 2025에 액세스, <https://www.oracle.com/java/technologies/javase/codeconventions-namingconventions.html>
13. Expert Tips on Database Naming Conventions - Claravine, 4월 23, 2025에 액세스, <https://www.claravine.com/database-naming-conventions/>
14. Best Practices for API Design in Java - Mezo Code, 4월 23, 2025에 액세스, <https://mezocode.com/best-practices-for-api-design-in-java/>
15. Error Details in Spring Boot with RFC 7807 - , 4월 23, 2025에 액세스, <https://schegge.de/2024/02/error-details-in-spring-boot-with-rfc-7807/>
16. Logging :: Spring Boot, 4월 23, 2025에 액세스, <https://docs.spring.io/spring-boot/reference/features/logging.html>
17. Using Java Naming Conventions - ThoughtCo, 4월 23, 2025에 액세스, <https://www.thoughtco.com/using-java-naming-conventions-2034199>
18. Spring Boot folder structure best practices - Symflower, 4월 23, 2025에 액세스, <https://symflower.com/en/company/blog/2024/spring-boot-folder-structure/>
19. Best Practices for Database Naming Conventions - Drygast.NET, 4월 23, 2025에 액세스, <https://drygast.net/blog/post/database_naming_conventions>
20. Understanding Spring Boot Project Structure | CodeSignal Learn, 4월 23, 2025에 액세스, <https://codesignal.com/learn/courses/introduction-to-spring-boot-and-spring-core-with-kotlin/lessons/understanding-spring-boot-project-structure>
21. codefinity.com, 4월 23, 2025에 액세스, <https://codefinity.com/courses/v2/87dc501e-89a6-4a4b-afd4-8b38c46a80c7/9a2cd386-7414-4da6-a5ba-c79732024d97/c5672c70-6af2-4164-ad97-b6205befa155#:~:text=In%20a%20Spring%20Boot%20project,rapid%20deployment%20of%20the%20application.>
22. Naming Conventions in Java - GeeksforGeeks, 4월 23, 2025에 액세스, <https://www.geeksforgeeks.org/java-naming-conventions/>
23. What strategy do you use for package naming in Java projects and ..., 4월 23, 2025에 액세스, <https://stackoverflow.com/questions/533102/what-strategy-do-you-use-for-package-naming-in-java-projects-and-why>
24. Package by Feature - Philipp Hauer's Blog, 4월 23, 2025에 액세스, <https://phauer.com/2020/package-by-feature/>
25. Where to put my framework classes using package-by-feature convention? - Stack Overflow, 4월 23, 2025에 액세스, <https://stackoverflow.com/questions/41160381/where-to-put-my-framework-classes-using-package-by-feature-convention>
26. Java Style Guide | Codecademy, 4월 23, 2025에 액세스, <https://www.codecademy.com/article/java-for-programmers-java-style-guide>
27. Lombok Made Simple: Improve Java with Getters, Setters & More - JigNect Technologies Pvt Ltd, 4월 23, 2025에 액세스, <https://jignect.tech/lombok-unleashed-elevating-java-efficiency-with-getters-setters-constructors-builders-and-more/>
28. Introduction to Project Lombok | Baeldung, 4월 23, 2025에 액세스, <https://www.baeldung.com/intro-to-project-lombok>
29. Project Lombok: Clean, Concise Java Code - Oracle, 4월 23, 2025에 액세스, <https://www.oracle.com/corporate/features/project-lombok.html>
30. 10 Rules for a Better SQL Schema | Sisense, 4월 23, 2025에 액세스, <https://www.sisense.com/blog/better-sql-schema/>
31. SAS Help Center: Naming Conventions for MySQL, 4월 23, 2025에 액세스, <https://documentation.sas.com/doc/ru/pgmsascdc/v_023/acreldb/n0rfg6x1shw0ppn1cwhco6yn09f7.htm>
32. Web API design best practices - Azure Architecture Center | Microsoft Learn, 4월 23, 2025에 액세스, <https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design>
33. Top REST API URL naming convention standards | TheServerSide, 4월 23, 2025에 액세스, <https://www.theserverside.com/video/Top-REST-API-URL-naming-convention-standards>
34. Naming Conventions - api.gov.au, 4월 23, 2025에 액세스, <https://api.gov.au/sections/naming-conventions.html>
35. API Design Basics: Resources & Collections - APIs You Won't Hate, 4월 23, 2025에 액세스, <https://apisyouwonthate.com/blog/understanding-resources-and-collections-in-restful-apis/>
36. Database schema: SQL schema examples and best practices - CockroachDB, 4월 23, 2025에 액세스, <https://www.cockroachlabs.com/blog/database-schema-beginners-guide/>
37. MySQL Data Types and Performance Optimization: Usage & Examples - DataCamp, 4월 23, 2025에 액세스, <https://www.datacamp.com/doc/mysql/mysql-data-types-and>
38. Best Practices for Datatypes in a MySQL Schema, 4월 23, 2025에 액세스, <https://mysql.rjweb.org/doc.php/schema_best_practices_mysql>
39. 22 MySQL best practices to follow as a developer in 2019 - wpDataTables - Tables and Charts WordPress Plugin, 4월 23, 2025에 액세스, <https://wpdatatables.com/mysql-best-practices/>
40. Choosing the Right Data Types in MySQL - Codeneur the best Bootcamp in the world, 4월 23, 2025에 액세스, <https://www.codeneur.com/choosing-the-right-data-types-in-mysql/>
41. Best practices for REST API design - The Stack Overflow Blog, 4월 23, 2025에 액세스, <https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/>
42. A Guide to Spring Boot Logging: Best Practices & Techniques - Last9, 4월 23, 2025에 액세스, <https://last9.io/blog/a-guide-to-spring-boot-logging/>
43. Best Practices while Making Rest APIs in Spring Boot Application - GeeksforGeeks, 4월 23, 2025에 액세스, <https://www.geeksforgeeks.org/best-practices-while-making-rest-apis-in-spring-boot-application/>
44. Log Formatting: 8 Best Practices for Better Readability - Sematext, 4월 23, 2025에 액세스, <https://sematext.com/blog/log-formatting-8-best-practices-for-better-readability/>
45. Understanding JSON Logging and Analysis - OpenObserve, 4월 23, 2025에 액세스, <https://openobserve.ai/blog/json-logging-guide-examples/>
46. Log Formats – a (Mostly) Complete Guide - Graylog, 4월 23, 2025에 액세스, <https://graylog.org/post/log-formats-a-complete-guide/>
47. What is API versioning? Benefits, types & best practices | Postmann, 4월 23, 2025에 액세스, <https://www.postman.com/api-platform/api-versioning/>
48. API Versioning: Strategies & Best Practices - xMatters, 4월 23, 2025에 액세스, <https://www.xmatters.com/blog/api-versioning-strategies>
49. API Versioning Strategies: Best Practices Guide - Daily.dev, 4월 23, 2025에 액세스, <https://daily.dev/blog/api-versioning-strategies-best-practices-guide>
50. API versioning: URL vs Header vs Media Type versioning - Lonti, 4월 23, 2025에 액세스, <https://www.lonti.com/blog/api-versioning-url-vs-header-vs-media-type-versioning>
51. RFC-7807 problem details with Spring Boot and JAX-RS - codecentric AG, 4월 23, 2025에 액세스, <https://www.codecentric.de/knowledge-hub/blog/rfc-7807-problem-details-with-spring-boot-and-jax-rs>
52. Returning Errors Using ProblemDetail in Spring Boot - GeeksforGeeks, 4월 23, 2025에 액세스, <https://www.geeksforgeeks.org/returning-errors-using-problemdetail-in-spring-boot/>
53. Best Practices for REST API Error Handling - Baeldung, 4월 23, 2025에 액세스, <https://www.baeldung.com/rest-api-error-handling-best-practices>
54. Common MyBatis Configuration Pitfalls and How to Avoid Them - Java Tech Blog, 4월 23, 2025에 액세스, <https://javanexus.com/blog/mybatis-configuration-pitfalls>
55. Quick Guide to MyBatis - Baeldung, 4월 23, 2025에 액세스, <https://www.baeldung.com/mybatis>
56. SQL Style guide - Reddit, 4월 23, 2025에 액세스, <https://www.reddit.com/r/SQL/comments/urkixb/sql_style_guide/>
57. MyBatis 3 | Dynamic SQL, 4월 23, 2025에 액세스, <https://mybatis.org/mybatis-3/dynamic-sql.html>
58. MyBatis Dynamic SQL - Tutorialspoint, 4월 23, 2025에 액세스, <https://www.tutorialspoint.com/mybatis/mybatis_dynamic_sql.htm>
59. WHERE Conditions - MyBatis Dynamic SQL, 4월 23, 2025에 액세스, <https://mybatis.org/mybatis-dynamic-sql/docs/conditions.html>
60. Declarative Transaction Management :: Spring Framework, 4월 23, 2025에 액세스, <https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative.html>
61. Transactions - mybatis-spring, 4월 23, 2025에 액세스, <https://mybatis.org/spring/transactions.html>
62. Chapter 7. Transaction management - Spring, 4월 23, 2025에 액세스, <https://docs.spring.io/spring-framework/docs/1.1.5/reference/transaction.html>
63. Spring Transaction Management not working with Spring Boot + MyBatis? - Stack Overflow, 4월 23, 2025에 액세스, <https://stackoverflow.com/questions/37310550/spring-transaction-management-not-working-with-spring-boot-mybatis>
64. Unchecked Exceptions — The Controversy (The Java™ Tutorials > Essential Java Classes > Exceptions), 4월 23, 2025에 액세스, <https://docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html>
65. Checked and Unchecked Exceptions in Java | Baeldung, 4월 23, 2025에 액세스, <https://www.baeldung.com/java-checked-unchecked-exceptions>
66. Java Checked vs Unchecked Exceptions - GeeksforGeeks, 4월 23, 2025에 액세스, <https://www.geeksforgeeks.org/checked-vs-unchecked-exceptions-in-java/>
67. Understanding Java Exceptions: A Deep Dive into Checked and Unchecked Exceptions, 4월 23, 2025에 액세스, <https://www.sparkcodehub.com/java/checked-and-unchecked-exceptions>
68. @ControllerAdvice and @ExceptionHandler Annotations Spring Boot - DEV Community, 4월 23, 2025에 액세스, <https://dev.to/realnamehidden1_61/controlleradvice-and-exceptionhandler-annotations-spring-boot-15l0>
69. Exception Handling in Spring Boot | GeeksforGeeks, 4월 23, 2025에 액세스, <https://www.geeksforgeeks.org/exception-handling-in-spring-boot/>
70. Spring MVC – @ControllerAdvice Annotation for Global Exception Handling, 4월 23, 2025에 액세스, <https://www.geeksforgeeks.org/spring-mvc-controlleradvice-annotation-for-global-exception-handling/>
71. Master Spring Boot Logging | Configuration, Log Levels, Best Practices - YouTube, 4월 23, 2025에 액세스, <https://www.youtube.com/watch?v=fEG57C1Xq0k>
72. Spring Framework Documentation, 4월 23, 2025에 액세스, <https://docs.spring.io/spring-framework/reference/index.html>
