---
title: "? Google Gen AI Toolbox + MCP, 왜 개발자들이 열광하나요?"
date: 2025-07-18T03:01:08+09:00
slug: "726-Google-Gen-AI-Toolbox-MCP-왜-개발자들이-열광하나요"
original_url: "https://memoryhub.tistory.com/726"
tistory_id: 726
draft: false
categories: ["데브 라이브러리"]
tags: ["MCP"]
---

```
        ┌─────────────────────────────────────────┐
        │      ?‍? 개발자가 직접 정의            │
        │   ┌─────────────────────────────────┐   │
        │   │ tools.yaml                      │   │
        │   │ ├─ search-hotels-by-name        │   │
        │   │ │  └─ statement: SELECT * FROM..│   │
        │   │ ├─ book-hotel                   │   │
        │   │ │  └─ statement: UPDATE hotels..│   │
        │   └─────────────────────────────────┘   │
        └─────────────────────┬───────────────────┘
                              │
        ┌─────────────────────▼───────────────────┐
        │     ? AI 에이전트 도구 실행            │
        │   Claude가 정의된 도구들 중에서 선택    │
        └─────────────────────────────────────────┘
```

Google Gen AI Toolbox Tools는 에이전트가 취할 수 있는 액션을 정의합니다. 자연어를 SQL로 자동 변환하는 것이 아니라, **개발자가 직접 SQL 쿼리를 정의하고 AI가 그 도구들을 선택해서 실행**하는 방식입니다.

tools.yaml 파일의 tools 섹션에서 에이전트가 취할 수 있는 액션을 정의: 어떤 종류의 도구인지, 어떤 소스에 영향을 주는지, 어떤 파라미터를 사용하는지 등을 명시적으로 지정하죠.

⚡ **TL;DR**: Google Gen AI Toolbox는 개발자가 SQL 쿼리를 직접 정의한 '도구들'을 만들고, AI 에이전트가 상황에 맞는 도구를 선택해서 실행하는 시스템입니다. 자동 SQL 생성이 아닌 **미리 정의된 안전한 도구들의 조합**이 핵심입니다.

## 목차

1. 배경 - Tools 중심 접근법이 왜 중요한가?
2. 핵심 개념 정리 - Tools와 수동 쿼리 정의
3. 실습 - tools.yaml로 도구 만들기
4. 모범 사례와 베스트 프랙티스
5. 마치며 & 참고자료

---

## 1. 배경

### 기존 접근법의 문제점들

대부분의 AI-데이터베이스 연동은 자연어를 SQL로 자동 변환하려고 시도합니다. 하지만 LLM을 SQL 데이터베이스에 직접 연결하면 안전하지 않은 쿼리 생성, 연결 생명주기 관리 부실, 민감한 자격 증명 노출 등의 운영 및 보안 문제가 발생합니다.

### Tools 중심 접근법의 장점

데이터베이스 스키마를 내성으로 파악하고 LLM이나 에이전트가 사용할 수 있게 만들어 안전하고 스키마 검증된 쿼리를 가능하게 합니다. **개발자가 미리 정의한 안전한 쿼리 템플릿들**을 AI가 선택하여 실행하는 방식입니다.

### 용어 정의

| 용어 | 설명 |
| --- | --- |
| **Tool** | SQL 문 실행과 같이 에이전트가 취할 수 있는 액션 |
| **Statement** | 도구에서 실행할 실제 SQL 쿼리 ($1, $2로 파라미터 받음) |
| **Parameters** | SQL의 플레이스홀더에 전달될 입력값들 |
| **Template Parameters** | 테이블명, 컬럼명 등을 동적으로 교체할 수 있는 파라미터 |

## 2. 핵심 개념

> **Tools는 개발자가 직접 정의하는 SQL 도구 모음**  
> 개발자가 tools.yaml 파일의 tools 섹션에서 맵으로 도구들을 정의할 수 있습니다. 일반적으로 도구는 작업할 소스가 필요합니다.

### 핵심 아키텍처: 수동 쿼리 정의

tools.yaml에서 각 도구는 kind, source, statement, parameters를 명시적으로 정의합니다:

```
tools:
  search-hotels-by-name:
    kind: postgres-sql
    source: my-pg-source  
    statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%'
    description: Search for hotels based on name.
    parameters:
      - name: name
        type: string
        description: The name of the hotel.
```

**중요한 점**: AI가 SQL을 생성하는 것이 아니라, **개발자가 미리 작성한 쿼리들 중에서 AI가 적절한 도구를 선택**하는 방식입니다.

## 3. 실습

### ① 완전한 tools.yaml 작성

실제 호텔 예약 시스템을 위한 도구들을 정의해보겠습니다:

```
sources:
  my-pg-source:
    kind: postgres
    host: 127.0.0.1
    port: 5432
    database: toolbox_db
    user: ${USER_NAME}
    password: ${PASSWORD}

tools:
  search-hotels-by-name:
    kind: postgres-sql
    source: my-pg-source
    description: Search for hotels based on name.
    statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%'
    parameters:
      - name: name
        type: string
        description: The name of the hotel.

  book-hotel:
    kind: postgres-sql  
    source: my-pg-source
    description: Book a hotel by its ID.
    statement: UPDATE hotels SET booked = B'1' WHERE id = $1
    parameters:
      - name: hotel_id
        type: string
        description: The ID of the hotel to book.

  cancel-hotel:
    kind: postgres-sql
    source: my-pg-source  
    description: Cancel a hotel by its ID.
    statement: UPDATE hotels SET booked = B'0' WHERE id = $1
    parameters:
      - name: hotel_id
        type: string
        description: The ID of the hotel to cancel.

toolsets:
  hotel-management:
    - search-hotels-by-name
    - book-hotel
    - cancel-hotel
```

### ② 템플릿 파라미터 활용

템플릿 파라미터를 사용하면 테이블명과 컬럼명을 동적으로 교체할 수 있지만, SQL 인젝션에 취약하므로 기본 파라미터가 성능과 안전성 면에서 권장됩니다:

```
select-columns-from-table:
  kind: postgres-sql
  source: my-pg-instance
  statement: SELECT {{array .columnNames}} FROM {{.tableName}}
  templateParameters:
    - name: tableName
      type: string
    - name: columnNames  
      type: array
      items:
        name: column
        type: string
```

### ③ 서버 실행 및 테스트

```
./toolbox --tools-file "tools.yaml"
```

## 4. 모범 사례

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **기본 파라미터 사용** | 성능과 안전성 면에서 선호됨 | 유연성 제한 |
| **인증 필수 도구** | authRequired 필드로 인증 체크 | 설정 복잡도 증가 |
| **자동 인증 파라미터** | ID 토큰에서 사용자 정보 자동 추출 | 토큰 설정 필요 |

### 보안 고려사항

**인증된 파라미터 사용:**

```
search-flights-by-user-id:
  kind: postgres-sql
  statement: SELECT * FROM flights WHERE user_id = $1
  parameters:
    - name: user_id
      type: string
      authServices:
        - name: my-google-auth
          field: sub  # OIDC의 사용자 ID 클레임
```

### 실제 활용 사례

실시간으로 관계형 데이터베이스에서 사용자 정보를 검색하는 고객 서비스 에이전트, 분석 데이터베이스를 쿼리하여 비즈니스 메트릭 질문에 답하는 BI 어시스턴트, 데이터베이스 상태를 모니터링하고 이상을 보고하는 DevOps 봇 등에 활용됩니다.

## 5. 마치며

**배운 점들:**

- Google Gen AI Toolbox는 SQL 자동 생성이 아닌 **미리 정의된 도구들의 체계적 관리**가 핵심입니다
- 개발자가 tools.yaml에서 직접 정의한 SQL 도구들을 AI가 상황에 맞게 선택하여 실행합니다
- 이 방식은 보안성과 안정성을 크게 향상시키면서도 개발자에게 완전한 제어권을 제공합니다

**실제 프로젝트 적용 팁:** YAML 파일에서 "영화 검색"이나 "고객 대여 조회" 같은 도구들을 정의하고 LLM이 사용자 쿼리에 따라 도구를 선택하고 실행하도록 설계하세요.

⸻

## 참고자료

**공식 문서**

- [Tools 정의 가이드](https://googleapis.github.io/genai-toolbox/resources/tools/)
- [Python 퀵스타트](https://googleapis.github.io/genai-toolbox/getting-started/local_quickstart/)

**샘플 레포**

- [googleapis/genai-toolbox](https://github.com/googleapis/genai-toolbox)

**추가 읽을거리**

- [Google Cloud의 Gen AI Toolbox 발표](https://cloud.google.com/blog/products/ai-machine-learning/announcing-gen-ai-toolbox-for-databases-get-started-today)
- [DVD 대여 챗봇 실습 가이드](https://medium.com/google-cloud/building-a-dvd-rental-chatbot-using-llamaindex-agentworkflow-google-genai-toolbox-postgresql-5d6e806d5891)
- [AlloyDB와 MCP Toolbox 연동](https://codelabs.developers.google.com/genai-toolbox-for-alloydb)

---

### ? 용어 사전 (어린이도 이해할 수 있게)

**Tools (도구)**: AI가 사용할 수 있는 미리 만들어진 작업들 (레고 블록 같은 것)  
**Statement (구문)**: 데이터베이스에게 "이것을 찾아줘"라고 말하는 특별한 언어  
**Parameters (매개변수)**: 도구에게 전달하는 구체적인 정보 (예: "홀리데이 인"이라는 호텔 이름)  
**Template Parameters (템플릿 매개변수)**: 도구의 모양 자체를 바꿀 수 있는 특별한 설정  
**Toolsets (도구 세트)**: 관련된 도구들을 묶어놓은 상자
