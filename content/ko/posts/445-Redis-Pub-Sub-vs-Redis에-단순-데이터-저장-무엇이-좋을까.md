---
title: "Redis Pub/Sub vs. Redis에 단순 데이터 저장, 무엇이 좋을까?"
date: 2025-02-09T10:44:05+09:00
slug: "445-Redis-Pub-Sub-vs-Redis에-단순-데이터-저장-무엇이-좋을까"
original_url: "https://memoryhub.tistory.com/445"
tistory_id: 445
draft: false
categories: ["데브 데이터베이스"]
tags: ["Redis"]
---

오늘은 **Redis의 Pub/Sub(Channel/Topic) 기능**과, 단순히 **Redis 자료구조(SET, LIST 등)로 로깅**하는 방법 중 어떤 것을 선택해야 할지, 특히 **채팅 에러(에러 로그) 관리**를 예시로 이야기를 나눠보겠습니다.

---

## **1. Redis Pub/Sub과 로깅용 자료구조(SET 등)란? ?**

먼저, 간단히 개념부터 살펴보겠습니다.

### ? Redis Pub/Sub(Channel/Topic)이란?

- **Pub/Sub(Publish/Subscribe)** 모델은 메시지를 발행(Publish)하고, 이를 구독(Subscribe)하는 방식을 통해 **실시간 통신**이 가능하도록 해주는 Redis의 기능입니다.
- 메시지를 보내는 쪽(Publisher)과 이를 받는 쪽(Subscriber)이 직접 연결되는 것이 아니라, **중간에 ‘Channel(Topic)’**을 두고 이 채널을 통해 메시지가 오가게 됩니다.
- 예를 들어, 채팅 애플리케이션에서 **"새로운 채팅 메시지 알림"** 등을 실시간으로 전달해야 할 때, Redis Pub/Sub을 사용해 메인 서버에서 메시지를 Publish하면 구독 중인 다른 서버나 클라이언트에서 바로 메시지를 수신할 수 있습니다.

### ? Redis에 자료구조(SET 등)를 활용해 로깅하는 방법

- Redis는 다양한 자료구조(String, List, Set, Hash, Sorted Set 등)를 제공합니다.
- **오류 로그**와 같은 정보를 `List`나 `Set`에 쌓아두는 방식은, 데이터 조회와 분석을 위해 **“상태값을 저장”**하는 데 유용합니다.
- 예: `SADD chat_errors "ChatID:123 Error:ConnectionLost"` 처럼, 에러가 발생하면 Redis의 Set에 저장해두고, 필요할 때 조회/분석을 합니다.

결국, **Pub/Sub**은 **실시간 메시지 전달**에 특화된 기능이고, **SET, LIST 등 자료구조**를 활용하는 것은 **데이터를 저장하고 검색**하는 데 더 특화된 방식이라고 볼 수 있습니다.

---

## **2. 어떻게 동작하나요? ?**

### 1) Redis Pub/Sub의 기본 개념

```
# Redis CLI에서 예시
# 1) Subcriber(구독자) 측
SUBSCRIBE my_error_channel

# 2) Publisher(발행자) 측
PUBLISH my_error_channel "User XYZ Chat Connection Error"
```

- `SUBSCRIBE my_error_channel` 명령을 통해 특정 채널을 구독합니다.
- 누군가가 `PUBLISH my_error_channel "메시지"`를 하면, 이 채널을 구독하는 모든 클라이언트는 즉시 해당 메시지를 수신합니다.
- **실시간성**이 필요한 시스템에서 매우 유용합니다.

### 2) Redis SET(로깅용) 활용 예시

```
# Redis CLI에서 예시
# 에러 로그를 세트에 저장
SADD chat_error_logs "User XYZ Chat Connection Error"
SADD chat_error_logs "User ABC Chat Timeout Error"

# 세트 안에 있는 에러 로그 확인
SMEMBERS chat_error_logs
```

- `SADD` 명령을 통해 에러 문자열을 삽입합니다.
- `SMEMBERS`를 통해 전체 에러 로그를 조회할 수 있습니다.
- 이처럼 **데이터를 누적**해 관리하고 필요할 때 특정 기준으로 가져와서 분석할 수 있습니다.

---

### ? 동작 원리

1. **Redis Pub/Sub**

   - **실시간** 메시지 전달용으로, 연결된 Subscriber는 발행(Publish)되는 순간 **즉시 알림**을 받습니다.
   - 메시지 자체를 Redis 메모리에 **영구 저장**하지는 않기 때문에, 한 번 놓친 메시지는 다시 가져오기 어려울 수 있습니다.
2. **Redis 자료구조(SET 등)**

   - 에러 로그 등을 **저장**해두는 용도로 사용합니다.
   - 이렇게 저장된 데이터는 **원할 때 다시 검색**해 볼 수 있으며, **분석**하거나 **집계**할 수 있습니다.
   - 한 번 입력된 로그는 Redis가 관리하는 메모리에 남아 있으므로, 추후에도 쉽게 조회 가능합니다.
3. **채팅 에러 로깅 시**

   - **Pub/Sub**을 사용하면, 다른 마이크로서비스나 모니터링 툴에서 해당 채널을 **실시간**으로 구독해 바로 에러 알림을 받을 수 있습니다.
   - **자료구조(SET 등)**를 사용하면, 에러 발생 시 로그를 축적해두고, 추후 DevOps팀이나 모니터링 서비스가 이 데이터를 조회해 **지연 분석**을 수행하기 좋습니다.

---

## **3. 주요 장점 ?**

### 1) Redis Pub/Sub(Channel/Topic) 활용 시 장점

1. **실시간성**: 메시지가 발생하면 구독자는 바로 전달받을 수 있습니다.
2. **비동기 통신**: 발행자와 구독자가 직접 연결되지 않아도, 채널만 알고 있으면 비동기로 통신이 가능합니다.
3. **간편한 스케일 아웃**: 여러 Subscriber가 동시에 채널을 구독할 수 있어, 확장성(스케일 아웃)에 유리합니다.

### 2) Redis SET(단순 로깅) 활용 시 장점

1. **데이터 영속성(실시간이 아니더라도)**: Redis는 인메모리 DB이지만, RDB(AOF) 설정 등에 따라 영속성을 확보할 수 있습니다.
2. **간단한 조회/분석**: 한 번 쌓아둔 데이터는 원하는 시점에 언제든지 조회·분석 가능.
3. **구현 난이도 낮음**: 단순히 `SADD`만으로 에러를 저장할 수 있으므로 로깅 구현이 간편합니다.

---

## **4. 주의할 점 ⚠️**

### 1) Pub/Sub 사용 시 주의사항

1. **데이터 유실 위험**: Pub/Sub은 특정 시점에 구독 중이 아닌 경우, 이미 발행된 메시지는 놓칠 수 있습니다.
2. **추후 분석 어려움**: 메시지가 Redis에 **“영구 저장”**되지 않으므로, 나중에 메시지를 복원하기 위해서는 별도의 로깅이 필요합니다.
3. **모니터링**: 실시간 메시지 큐의 특성상, 성능과 트래픽 모니터링을 꼼꼼히 해야 합니다.

### 2) SET(로깅) 사용 시 주의사항

1. **실시간 알림 불가**: 데이터는 쌓이지만, 자동으로 알려주는 기능은 없으므로 **Polling** 또는 다른 방식을 함께 써야 실시간 알림이 가능합니다.
2. **메모리 및 저장공간 이슈**: 로그가 매우 많아지면 Redis 메모리를 많이 차지할 수 있습니다.
3. **집계/분석 부담**: 실시간으로 처리가 필요하다면, 추가적인 작업(워크플로우)이 필요할 수 있습니다.

---

## **5. 실제 사용 예시 ?**

아래 예시는 **스프링 부트(Spring Boot)** 환경에서 Redis를 활용해 채팅 에러를 처리할 때의 가상의 코드 예시입니다.

### 1) Pub/Sub으로 에러 메시지 발행하기 (Publisher)

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.RedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class ChatErrorPublisher {

    @Autowired
    private RedisTemplate<String, Object> redisTemplate;

    public void publishError(String errorMessage) {
        redisTemplate.convertAndSend("chatErrorChannel", errorMessage);
    }
}
```

- `convertAndSend(channel, message)` 메서드를 통해 `chatErrorChannel`이라는 채널에 에러 메시지를 발행합니다.

### 2) Pub/Sub으로 에러 메시지 구독하기 (Subscriber)

```
import org.springframework.stereotype.Component;
import org.springframework.data.redis.connection.Message;
import org.springframework.data.redis.connection.MessageListener;
import org.springframework.data.redis.serializer.RedisSerializer;

@Component
public class ChatErrorSubscriber implements MessageListener {

    @Override
    public void onMessage(Message message, byte[] pattern) {
        String channel = new String(pattern);
        String errorMessage = (String) RedisSerializer.string().deserialize(message.getBody());
        System.out.println("Received error on channel: " + channel + " Error: " + errorMessage);

        // 추가로 에러를 DB 혹은 Redis의 SET으로 저장할 수도 있음
    }
}
```

- 해당 클래스는 `MessageListener`를 구현해, 특정 채널에서 들어온 메시지를 실시간으로 수신합니다.

### 3) 간단히 Redis SET에 로깅하기

```
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;

@Service
public class ChatErrorLogger {

    private static final String ERROR_SET_KEY = "chat_error_logs";

    @Autowired
    private StringRedisTemplate stringRedisTemplate;

    public void logError(String errorMessage) {
        stringRedisTemplate.opsForSet().add(ERROR_SET_KEY, errorMessage);
        System.out.println("Error logged: " + errorMessage);
    }

    public Set<String> getAllErrors() {
        return stringRedisTemplate.opsForSet().members(ERROR_SET_KEY);
    }
}
```

- 에러 메시지를 `chat_error_logs` 라는 Set에 저장하고, 필요 시 조회할 수 있습니다.

---

## **6. 마치며 ?**

정리해보면, **Redis Pub/Sub**은 **실시간**으로 에러나 메시지를 받아서 바로 처리해야 하는 시나리오에 적합합니다. 반면, 단순히 로그를 **“누적”**하고 싶다면, Redis의 **SET이나 LIST** 등의 자료구조를 사용해 저장하는 방식을 택할 수 있습니다.

- **실시간 처리가 중요**한 경우: **Pub/Sub**
- **장기 로깅과 분석**이 중요한 경우: **SET/LIST 등 자료구조**

두 방식을 **결합**해서 실시간 알림이 필요한 부분은 Pub/Sub으로 처리하고, 별도로 에러 로그는 Set이나 Database에 저장해둔 뒤 사후 분석을 수행하는 **하이브리드** 방식도 많이 활용합니다. 이 방식을 사용하면 **실시간 모니터링과 사후 분석** 두 마리 토끼를 잡을 수 있습니다.

---

### 참고 자료 및 출처

1. [Redis 공식 문서 - Pub/Sub](https://redis.io/docs/manual/pubsub/)
2. [Redis 공식 문서 - Data Types (SET, LIST 등)](https://redis.io/docs/data-types/)
3. [Spring Data Redis Reference](https://docs.spring.io/spring-data/redis/docs/current/reference/html/)

이처럼 **Redis**의 기능을 상황에 맞추어 잘 활용한다면, 채팅 에러 로깅이나 실시간 알림 시스템을 **더욱 견고하고 유연**하게 구성할 수 있습니다!
