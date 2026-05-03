---
title: "Redis 기반 고객 채팅 에러 로그 기록 및 중복 로그 처리 시스템"
date: 2025-02-09T01:40:01+09:00
slug: "442-Redis-기반-고객-채팅-에러-로그-기록-및-중복-로그-처리-시스템"
original_url: "https://memoryhub.tistory.com/442"
tistory_id: 442
draft: false
---

오늘은 **Redis**를 활용하여 운영 환경에 올라가는 고객 채팅 에러 로그를 효율적으로 기록하고, 중복 로그인 경우에는 기존 로그를 그대로 반환하는 방식의 시스템 명세서를 작성해보겠습니다!  
이 포스트는 기술 블로그 형식으로 작성되었으며, Redis를 이용한 간단하면서도 확장성 있는 구조를 예시 코드와 함께 설명합니다.

---

## **1. 고객 채팅 에러 로그 기록 및 중복 로그 처리 시스템이란? ?**

보통 채팅 서비스에서는 다음과 같은 문제들이 발생합니다.

1. **실시간으로 발생하는 대규모 로그**: 사용자가 많을수록 에러 로그가 폭발적으로 늘어납니다.
2. **중복 로그 처리**: 특정 에러가 반복적으로 발생할 경우, 저장 공간과 분석 효율이 떨어질 수 있습니다.
3. **신속한 접근 및 검색**: 문제 발생 시 빨리 로그를 확인해야 합니다.

이 시스템은 **Redis**를 사용해 **실시간으로 고객 채팅 에러 로그를 기록**하고, **이미 존재하는 에러 로그가 다시 들어오면 중복 처리를 최소화하여 그대로 반환**합니다.

---

## **2. 어떻게 동작하나요? ?**

### **1) 기본 구조**

Redis를 데이터 저장소로 사용하며, 주요 데이터 흐름은 다음과 같습니다.

1. **에러 발생**: 고객 채팅 서비스에서 에러가 발생하면, 에러 정보를 구조화(에러 코드, 메시지, 발생 시간 등)하여 로그로 전송합니다.
2. **Redis 검사**: Redis에서 해당 에러 메시지가 이미 존재하는지 검사합니다.
   - 존재한다면: 캐시에 저장된 에러 로그를 그대로 반환합니다.
   - 존재하지 않는다면: 새로운 에러 로그로 Redis에 저장합니다.
3. **반환 및 추가 처리**:
   - 에러 로그가 이미 존재하는 경우: Redis의 기존 로그 정보를 반환하고, 원하는 경우 카운트를 증가시키거나, 가장 최근 발생 시점만 업데이트합니다.
   - 새로운 에러 로그의 경우: 에러 정보를 로그 서버(예: Elasticsearch, Logstash 등)나 모니터링 시스템으로 전달할 수도 있습니다.

### **2) 기본 데이터 모델**

Redis에서 키-값 구조를 사용한다고 가정해봅시다.

- **Key**: 에러 메시지(혹은 에러 코드)를 식별할 수 있는 고유한 문자열
- **Value**: 추가 정보(발생 시간, 횟수, 상세 메시지 등)를 담은 JSON 또는 해시(Hash)

예시로 해시 구조를 사용한다면, 다음과 같은 형태가 가능합니다.

```
# key: "error:{errorCodeOrMessage}"
HSET "error:DB_CONNECTION_FAIL"
    "message" "DB connection timed out."
    "first_occurrence" "2025-02-01 10:00:00"
    "last_occurrence" "2025-02-01 10:00:00"
    "count" 1
```

### **3) 실제 적용 예시 (Java 가정)**

```
import redis.clients.jedis.Jedis;

public class ChatErrorLogger {

    private Jedis jedis;

    public ChatErrorLogger(String redisHost, int redisPort) {
        jedis = new Jedis(redisHost, redisPort);
    }

    public ErrorLog logError(ErrorLog errorLog) {
        String key = "error:" + errorLog.getErrorCode(); 
        // 에러 코드나 메시지를 유니크하게 파싱하여 key로 설정

        if (jedis.exists(key)) {
            // 이미 존재하는 에러이므로 해당 로그를 가져옴
            String lastOccurrence = jedis.hget(key, "last_occurrence");
            int count = Integer.parseInt(jedis.hget(key, "count"));

            // count 증가
            jedis.hset(key, "count", String.valueOf(count + 1));

            // last_occurrence 업데이트(현재 시각)
            String currentTime = getCurrentTime();
            jedis.hset(key, "last_occurrence", currentTime);

            // Redis에 저장된 값을 가져와 반환
            return new ErrorLog(
                errorLog.getErrorCode(),
                jedis.hget(key, "message"),
                jedis.hget(key, "first_occurrence"),
                currentTime,
                count + 1
            );

        } else {
            // 새로운 에러 로그이므로 Redis에 저장
            jedis.hset(key, "message", errorLog.getMessage());
            String currentTime = getCurrentTime();
            jedis.hset(key, "first_occurrence", currentTime);
            jedis.hset(key, "last_occurrence", currentTime);
            jedis.hset(key, "count", "1");

            // 바로 입력된 내용을 반환
            return new ErrorLog(
                errorLog.getErrorCode(),
                errorLog.getMessage(),
                currentTime,
                currentTime,
                1
            );
        }
    }

    // 현재 시각 포맷팅 예시 메서드
    private String getCurrentTime() {
        // SimpleDateFormat 등을 사용
        return "2025-02-09 12:00:00";
    }
}

// 에러 로그 정보를 담을 간단한 DTO 예시
class ErrorLog {
    private String errorCode;
    private String message;
    private String firstOccurrence;
    private String lastOccurrence;
    private int count;

    public ErrorLog(String errorCode, String message,
                    String firstOccurrence, String lastOccurrence, int count) {
        this.errorCode = errorCode;
        this.message = message;
        this.firstOccurrence = firstOccurrence;
        this.lastOccurrence = lastOccurrence;
        this.count = count;
    }

    // Getter, Setter
}
```

#### ? 동작 원리 요약

1. **Redis 키 조회**: `jedis.exists(key)`를 통해 해당 에러 코드/메시지가 저장되어 있는지 확인합니다.
2. **중복 로그 처리**: 존재한다면 `count` 값을 증가시키고, `last_occurrence`만 갱신합니다.
3. **새 로그 처리**: 새로운 로그라면 Redis에 해시 구조로 저장합니다.
4. **결과 반환**: 최종적으로 내부에 저장된 정보를 객체 형태로 반환해 시스템이 후속 작업을 처리할 수 있도록 합니다.

---

## **3. 주요 장점 ?**

1. **실시간 처리**: Redis는 메모리 기반 저장소이므로 에러 로그를 빠르게 쓰고 읽을 수 있습니다.
2. **중복 데이터 절약**: 이미 존재하는 에러 로그에 대해서는 중복 기록을 막고, `count` 증가만 처리하여 저장 공간을 효율적으로 사용합니다.
3. **확장성**: Redis는 클러스터링(Cluster) 구성이 가능하므로 사용자 증가나 로그 폭증 상황에도 수평 확장이 용이합니다.
4. **분석에 유리**: 중복 횟수, 최근 발생 시각을 관리함으로써 에러 발생 양상 파악이 쉬워집니다.

---

## **4. 주의할 점 ⚠️**

1. **데이터 영속성**: Redis는 기본적으로 메모리 기반이므로, 영속성(AOF, RDB)을 적절히 설정하지 않으면 재시작 시 데이터가 유실될 수 있습니다.
2. **키 만료 정책**: 모든 에러 로그를 무기한 보관할 필요가 없다면, `EXPIRE` 설정을 통해 일정 시간 이후 자동 삭제하는 방법을 고려해야 합니다.
3. **로그 분석 시스템 연동**: Redis는 영구 로그 저장소가 아니므로, 검색이나 장기 보관이 필요한 경우 Elasticsearch, S3 등 다른 로그 관리 시스템과 연동이 필요합니다.
4. **메모리 사용량 관리**: 로그가 장기적으로 쌓이면 Redis 메모리가 부족해질 수 있습니다. 주기적 백업 또는 만료(Expire) 전략이 중요합니다.

---

## **5. 실제 사용 예시 ?**

아래는 간단한 예시 시나리오입니다.

1. **사용자 A**, "DB\_CONNECTION\_FAIL" 에러를 최초로 발생 -> Redis에 새로운 로그 키 생성, `count = 1`, `first_occurrence = now`, `last_occurrence = now`
2. 1분 뒤 **사용자 B** 또한 같은 에러 발생 -> 이미 키가 존재하므로 `count = 2`, `last_occurrence` 갱신
3. 10분 뒤 **사용자 C**가 새로운 "API\_TIMEOUT" 에러 발생 -> Redis에 또 다른 키("error:API\_TIMEOUT") 생성

사용자는 여러 명이지만, 동일 에러는 중복 저장하지 않고 카운트만 증가시킵니다. 모니터링 대시보드나 Kibana 같은 툴에서 Redis에서 가져온 데이터(에러별 발생 횟수, 최근 발생 시점)를 시각화하면 **에러 분석이 더욱 효율적**이 됩니다.

```
public class ChatErrorLogTest {
    public static void main(String[] args) {
        ChatErrorLogger logger = new ChatErrorLogger("localhost", 6379);

        ErrorLog log1 = logger.logError(new ErrorLog("DB_CONNECTION_FAIL", 
            "DB connection timed out.", null, null, 0));
        System.out.println("첫 번째 로그 발생: " + log1.getCount()); // count = 1

        ErrorLog log2 = logger.logError(new ErrorLog("DB_CONNECTION_FAIL", 
            "DB connection timed out.", null, null, 0));
        System.out.println("중복 로그 발생: " + log2.getCount()); // count = 2

        ErrorLog log3 = logger.logError(new ErrorLog("API_TIMEOUT", 
            "External API did not respond.", null, null, 0));
        System.out.println("새로운 에러 로그 발생: " + log3.getCount()); // count = 1
    }
}
```

---

## **6. 마치며 ?**

Redis를 활용하면 **실시간 에러 로그 기록**이 간편해지고, **중복 로그 처리**를 통해 로그 저장소를 효율적으로 운영할 수 있습니다. 또한, 간단한 키-값 및 해시 구조를 활용하여 **발생 횟수**, **최근 발생 시각** 등 중요한 정보를 빠르게 업데이트할 수 있습니다.

이 기술을 사용하면 **중복 로그 문제를 손쉽게 해결**하고, **로그 분석 및 모니터링** 과정에서 필요한 데이터를 빠르게 조회할 수 있습니다. 더불어 영구 보관이 필요한 로그는 후속 시스템(Elasticsearch, S3 등)으로 전송하고, Redis에서의 만료 정책을 적절히 사용한다면 보다 안정적이고 확장성 있는 로그 처리 시스템을 구축할 수 있습니다.

---

### **참고 자료 및 출처**

- [Redis 공식 문서](https://redis.io/docs/)
- [Jedis 라이브러리 GitHub](https://github.com/redis/jedis)
- [Elastic Stack(Elasticsearch) 공식 문서](https://www.elastic.co/guide/index.html)

이상으로 **Redis 기반 고객 채팅 에러 로그 기록 및 중복 로그 처리 시스템** 명세서였습니다. 실제 운영 환경 적용 시에는 Redis 설정, 로그 모니터링 시스템 연동, 보안 이슈(접근 제어, TLS 등)도 함께 고려하시길 추천드립니다!
