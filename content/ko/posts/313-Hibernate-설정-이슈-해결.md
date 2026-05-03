---
title: "Hibernate 설정 이슈 해결"
date: 2024-06-24T15:15:34+09:00
slug: "313-Hibernate-설정-이슈-해결"
original_url: "https://memoryhub.tistory.com/313"
tistory_id: 313
draft: false
categories: ["데브 옵스"]
---

**PrefixPhysicalNamingStrategy**: Hibernate에서 사용하는 전략으로, 데이터베이스의 테이블이나 컬럼 이름을 자동으로 수정합니다. 주로 테이블 이름 앞에 특정 글자나 단어를 붙이는 데 사용됩니다.

**SpringImplicitNamingStrategy**: Spring에서 제공하는 전략으로, 개발자가 직접 이름을 지정하지 않았을 때 자동으로 이름을 만들어줍니다.

**PrefixQueryModifier**: Hibernate가 데이터베이스에 보내는 쿼리를 중간에 가로채서 수정할 수 있게 해주는 도구입니다.

**잠재적 충돌**:

- **이름 중복**: PrefixPhysicalNamingStrategy와 PrefixQueryModifier가 둘 다 테이블 이름 앞에 뭔가를 붙이려고 하면 문제가 생길 수 있습니다.
- **예상치 못한 결과**: 두 도구가 동시에 작동하면 테이블 이름이 이상하게 변할 수 있습니다.
- **작동 시점 차이**: PrefixPhysicalNamingStrategy는 데이터베이스 구조를 만들 때 작동하고, PrefixQueryModifier는 쿼리를 보낼 때 작동합니다. 이 차이 때문에 문제가 생길 수 있습니다.
- **호환성 문제**: PrefixQueryModifier를 사용하면 Hibernate의 다른 기능들과 잘 맞지 않을 수 있습니다.

**해결 방법**:

- **PrefixPhysicalNamingStrategy만 사용**하세요. 이게 가장 표준적인 방법입니다.
- **PrefixQueryModifier는 제거**하는 게 좋습니다. 꼭 필요한 경우가 아니라면 사용하지 않는 것이 안전합니다.
- **Hibernate 설정을 다음과 같이 변경**하세요:
  - PrefixPhysicalNamingStrategy를 사용하도록 설정
  - SpringImplicitNamingStrategy를 사용하도록 설정
  - PrefixQueryModifier 관련 설정은 제거

이렇게 하면 Hibernate를 더 안정적으로 사용할 수 있고, 나중에 문제가 생길 가능성도 줄일 수 있습니다. 만약 PrefixQueryModifier로 특별히 하고 싶은 작업이 있다면, 다른 안전한 방법을 찾아볼 수 있습니다.

**PrefixQueryModifier를 사용하는 경우**:

- **동적 테이블 접두사**: 실행 시간에 테이블 접두사를 동적으로 변경해야 할 때 사용합니다. 예를 들어, 멀티테넌트 시스템에서 테넌트별로 다른 접두사를 사용해야 하는 경우입니다.
- **복잡한 쿼리 수정**: 단순히 테이블 이름만 수정하는 게 아니라, 쿼리 전체를 더 복잡하게 수정해야 할 때 사용합니다.
- **레거시 시스템 통합**: 기존 시스템과 통합해야 하는데, 그 시스템의 테이블 명명 규칙이 특이한 경우 사용할 수 있습니다.
- **보안 강화**: 특정 조건에 따라 쿼리에 보안 관련 조건을 추가해야 할 때 사용할 수 있습니다.
- **성능 최적화**: 특정 상황에서 쿼리를 자동으로 최적화하고 싶을 때 사용할 수 있습니다.

하지만 이런 경우에도 **PrefixQueryModifier 대신 다른 표준적인 방법을 사용하는 것이 좋습니다**. 예를 들어, 동적 테이블 접두사는 Hibernate의 멀티테넌트 기능을, 복잡한 쿼리 수정은 JPA Criteria API나 QueryDSL을 사용할 수 있습니다. 이렇게 하면 Hibernate와의 호환성 문제를 피하고 코드 유지보수도 쉬워집니다.

**PrefixQueryModifier를 사용하는 예시**:

동적 테이블 접두사:

```
public class TenantPrefixInterceptor extends EmptyInterceptor {
    private String tenantId;

    public void setTenantId(String tenantId) {
        this.tenantId = tenantId;
    }

    @Override
    public String onPrepareStatement(String sql) {
        return sql.replaceAll("FROM (\\w+)", "FROM " + tenantId + "_$1");
    }
}
```

이 예시에서는 테넌트 ID에 따라 테이블 이름 앞에 접두사를 붙입니다.

보안 강화:

```
public class SecurityInterceptor extends EmptyInterceptor {
    @Override
    public String onPrepareStatement(String sql) {
        if (sql.toLowerCase().contains("from users")) {
            return sql + " WHERE deleted = false";
        }
        return sql;
    }
}
```

이 예시는 'users' 테이블에 대한 모든 쿼리에 자동으로 보안 조건을 추가합니다.

성능 최적화:

```
public class QueryOptimizer extends EmptyInterceptor {
    @Override
    public String onPrepareStatement(String sql) {
        if (sql.toLowerCase().contains("from large_table")) {
            return sql.replace("SELECT *", "SELECT id, name");
        }
        return sql;
    }
}
```

이 예시는 대용량 테이블에 대한 쿼리를 자동으로 최적화합니다.

레거시 시스템 통합:

```
public class LegacySystemAdapter extends EmptyInterceptor {
    @Override
    public String onPrepareStatement(String sql) {
        return sql.replaceAll("user_info", "USR_INF")
                  .replaceAll("order_details", "ORD_DTL");
    }
}
```

이 예시는 현재 시스템의 테이블 이름을 레거시 시스템의 이름으로 자동 변환합니다.

이러한 예시들은 PrefixQueryModifier의 사용 가능성을 보여주지만, 앞서 말씀드렸듯이 이런 방식은 Hibernate와의 호환성 문제를 일으킬 수 있습니다. 가능하다면 Hibernate나 JPA에서 제공하는 표준 기능을 사용하는 것이 좋습니다.
