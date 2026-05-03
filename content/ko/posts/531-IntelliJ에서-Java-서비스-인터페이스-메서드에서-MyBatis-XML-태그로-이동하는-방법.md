---
title: "IntelliJ에서 Java 서비스 인터페이스 메서드에서 MyBatis XML 태그로 이동하는 방법"
date: 2025-03-26T16:00:21+09:00
slug: "531-IntelliJ에서-Java-서비스-인터페이스-메서드에서-MyBatis-XML-태그로-이동하는-방법"
original_url: "https://memoryhub.tistory.com/531"
tistory_id: 531
draft: false
categories: ["데브 유틸"]
tags: ["Intellij"]
---

IntelliJ IDEA에서 Java 서비스 인터페이스 메서드에서 매핑된 MyBatis XML 태그로 쉽게 이동할 수 있는 여러 방법이 있습니다. 가장 효과적인 방법은 MyBatis 플러그인 사용이며, 이를 통해 메서드와 XML 태그 간 양방향 탐색이 가능합니다.

## 주요 해결 방법

1. **MyBatis 플러그인 설치**
2. **Ctrl+Alt+B 또는 Ctrl+Shift+Alt+B 단축키 사용**
3. **인터페이스 메서드에서 우클릭 후 "Go to Declaration" 선택**
4. **매퍼 주석 기반 탐색**

## 상세 설명

### 1. MyBatis 플러그인 설치 및 활용

MyBatis 플러그인은 IntelliJ IDEA에서 Java 인터페이스와 MyBatis XML 매핑 간의 탐색을 제공하는 가장 효과적인 방법입니다.

```
File > Settings > Plugins > Marketplace > 'MyBatis' 검색 > 설치
```

설치할 수 있는 주요 플러그인:

- Free MyBatis Plugin
- MyBatisX

이러한 플러그인을 설치하면 다음과 같은 기능이 제공됩니다:

- 인터페이스 메서드와 해당 XML 태그 간 양방향 탐색
- 코드 완성 및 자동 생성
- 메서드 이름과 XML ID 간 일치 여부 검증

### 2. 단축키를 통한 탐색

MyBatis 플러그인 설치 후:

- 인터페이스 메서드에 커서를 놓고 `Ctrl+Alt+B` 또는 `Ctrl+Shift+Alt+B` 단축키를 누르세요.
- 매핑된 XML 태그로 직접 이동할 수 있는 옵션이 표시됩니다.

### 3. 컨텍스트 메뉴 활용

1. 인터페이스 메서드에 커서를 놓고 우클릭
2. "Go to Declaration" 또는 "Go to Implementation(s)" 선택
3. 인터페이스 메서드에 매핑된 MyBatis XML 태그로 이동

### 4. 매퍼 주석 기반 탐색

MyBatis 매퍼 주석을 사용하는 경우:

```
@Mapper
public interface UserMapper {
    @Select("SELECT * FROM users WHERE id = #{id}")
    User getUserById(Long id);
}
```

이 경우, 주석을 클릭하거나 `Ctrl+B`를 누르면 해당 SQL 쿼리로 직접 이동할 수 있습니다.

### 5. 구성 파일 설정

MyBatis 구성이 올바르게 설정되어 있는지 확인하세요:

- `mybatis-config.xml` 파일이 올바르게 구성되어 있는지 확인
- 매퍼 XML 파일이 올바른 경로에 있는지 확인
- 네임스페이스와 ID가 인터페이스 및 메서드와 정확히 일치하는지 확인

## 오류 발생 시 해결 방법

1. **플러그인 재설치**: 플러그인을 제거하고 다시 설치해보세요.
2. **캐시 삭제**: `File > Invalidate Caches / Restart` 선택
3. **프로젝트 재시작**: IntelliJ를 재시작하거나 프로젝트를 다시 로드하세요.
4. **매핑 확인**: 인터페이스 네임스페이스와 XML 파일의 네임스페이스가 일치하는지 확인하세요.

## 결론

IntelliJ IDEA에서 MyBatis 플러그인을 사용하면 Java 서비스 인터페이스 메서드에서 매핑된 XML 태그로 쉽게 이동할 수 있습니다. 이는 개발 생산성을 높이고 코드 탐색을 용이하게 합니다.
