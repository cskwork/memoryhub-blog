---
title: "Nginx의 모든 것: 가볍고 강력한 웹 서버 ☕️"
date: 2024-11-17T08:57:39+09:00
slug: "384-Nginx의-모든-것_-가볍고-강력한-웹-서버"
original_url: "https://memoryhub.tistory.com/384"
tistory_id: 384
draft: false
---

안녕하세요! 오늘은 현대 웹 서비스에서 빠질 수 없는 핵심 도구인 **Nginx**에 대해 자세히 알아보겠습니다.  
Nginx를 이해하기 쉽게 커피숍에 비유해 봅시다.

- **손님(클라이언트)**: 웹 브라우저나 모바일 앱 등에서 요청을 보내는 주체
- **직원(Nginx)**: 요청을 받아 적절히 분배하고 처리 흐름을 제어
- **주방(백엔드 서버)**: 실제로 요청을 처리하고 응답을 생성

커피숍 직원인 Nginx는 주문이 몰리는 ‘피크 타임’에도 여러 손님을 효율적으로 대응합니다. 필요한 경우, 다른 직원(서버)에게 업무를 분산시켜 빠르고 안정적으로 서비스를 제공하죠.

---

## 1. Nginx의 핵심 개념 ?

Nginx는 웹 서버이자 **리버스 프록시(Reverse Proxy)**로 동작할 수 있는 고성능 서버 소프트웨어입니다.  
**“웹 서버”**로서 정적인 파일(HTML, CSS, JS, 이미지 등)을 빠르게 서빙하고,  
**“리버스 프록시”**로서 백엔드 서버로의 요청을 중개하고 로드 밸런싱을 수행하여 서버 부하를 효율적으로 분산합니다.

### 어떤 문제를 해결하나요?

- **고성능 처리:** 다수의 동시 요청을 효율적으로 처리해 서버 과부하를 방지
- **로드 밸런싱:** 여러 서버에 요청을 분산해 특정 서버가 과도하게 부하되지 않도록 제어
- **보안 & SSL 종료:** HTTPS 연결을 위한 인증서 관리 및 SSL/TLS 종단 역할 수행
- **유연한 라우팅:** URL 매핑, 리다이렉션, API 게이트웨이 등 다양한 라우팅 시나리오 지원

---

## 2. 어떻게 동작하나요? ?

Nginx의 동작 방식을 조금 더 깊이 파헤쳐 보겠습니다.

### 1) 이벤트 기반 아키텍처

전통적인 서버(예: Apache의 프리포크 방식)는 **‘요청 1개당 프로세스(또는 스레드) 1개’**를 할당합니다. 하지만 많은 요청이 몰리면 프로세스나 스레드가 기하급수적으로 늘어나 시스템에 큰 부담이 됩니다.

반면, **Nginx는 이벤트 기반(비동기) 아키텍처**를 채택합니다.

- **한 명의 직원**(워커 프로세스)이 **이벤트(연결/요청)들을 논블로킹 I/O로 처리**하기 때문에, 동시에 많은 요청을 처리할 수 있습니다.
- 내부적으로 **Master-Worker 프로세스 구조**를 사용하여, Master 프로세스는 설정 파일 로드 및 워커 프로세스 관리를 담당하고, 실제 요청 처리는 여러 개의 워커 프로세스가 맡습니다.

```
# 예시
events {
    worker_connections 1024; # 한 워커 프로세스가 동시에 처리할 수 있는 최대 연결 수
}
```

### 2) 비동기 처리와 논블로킹 I/O

Nginx는 이벤트 루프를 통해 네트워크 소켓에서 발생하는 **읽기/쓰기 이벤트**를 감지하고, 이를 워커 프로세스가 처리합니다. 요청 입출력 시 **블로킹 없이(Non-blocking)** 데이터 처리를 수행하여 높은 동시성을 확보할 수 있죠.

### 3) 내부 모듈 구조

- **HTTP 모듈**: HTTP 요청 처리, 정적 파일 서빙, 압축(Gzip), 캐싱 등
- **Stream 모듈**: TCP/UDP 트래픽의 프록시, 로드 밸런싱
- **Mail 모듈**: 이메일 프로토콜(SMTP, IMAP, POP3) 프록시

구성 요소마다 플러그인처럼 독립적인 모듈을 추가하거나 제거할 수 있어, **가볍고 유연한 구조**를 유지합니다.

---

## 3. 주요 특징 ⭐

1. **이벤트 기반 아키텍처**
   - 적은 리소스로도 높은 동시 접속 처리 가능
   - 논블로킹 I/O 활용으로 CPU 사용 효율 극대화
2. **비동기 처리**
   - 워커 프로세스가 다수의 요청을 효율적으로 처리
   - 고성능, 고확장성 확보
3. **가벼운 리소스 사용**
   - 전통적인 웹 서버(Apache 등)에 비해 메모리와 CPU 사용량이 낮음
   - 높은 성능 대비 비용 절감 효과가 큼

---

## 4. 주요 기능 ?

### 1) 정적 파일 서빙

정적인 콘텐츠(HTML, CSS, JS, 이미지 등)를 빠르게 제공할 때 Nginx가 특히 강점을 발휘합니다.  
아래 설정은 `/images/` 경로로 들어오는 요청을 `/var/www/static` 경로에서 가져오고, 30일 동안 브라우저 캐싱을 유지합니다.

```
location /images/ {
    root /var/www/static;
    expires 30d; # 브라우저 캐싱 30일
}
```

### 2) 로드 밸런싱 (Upstream)

여러 대의 백엔드 서버를 운영할 때 Nginx를 로드 밸런서로 활용하면 특정 서버에 부하가 집중되지 않도록 막을 수 있습니다. 다음 예시는 `backend`라는 업스트림 그룹에 3개의 서버를 등록하고 있습니다.

```
upstream backend {
    server backend1.example.com:8080;
    server backend2.example.com:8080;
    server backend3.example.com:8080;
}

server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://backend;
    }
}
```

**로드 밸런싱 알고리즘**을 `least_conn`, `ip_hash`, `weighted round robin` 등으로 설정할 수도 있어, 트래픽 특성에 맞춰 최적의 방식을 선택할 수 있습니다.

### 3) SSL/TLS 터미네이션

HTTPS 프로토콜 사용 시, 인증서 관리와 SSL/TLS 연결을 Nginx가 맡아서 해주면 **백엔드 서버는 SSL 처리 부담**을 덜 수 있습니다.

```
server {
    listen 443 ssl;
    server_name secure.example.com;

    ssl_certificate     /etc/nginx/ssl/server.crt;
    ssl_certificate_key /etc/nginx/ssl/server.key;

    location / {
        proxy_pass http://backend;
    }
}
```

### 4) URL 리라이팅

구버전 URL이나 특정 패턴을 가진 요청을 새로운 경로로 보낼 때 유용합니다.

```
location /old-page {
    rewrite ^/old-page(.*)$ /new-page$1 permanent;
}
```

---

## 5. 실전 설정 예시 ?

### 1) 기본 웹 서버 설정

```
http {
    server {
        listen       80;
        server_name  example.com;

        location / {
            root   /var/www/html;
            index  index.html;
        }

        # Gzip 압축 활성화
        gzip on;
        gzip_types text/plain text/css application/json application/javascript;

        # 에러 페이지 설정
        error_page 404 /404.html;
    }
}
```

- **root**: 정적 파일을 제공할 루트 디렉터리
- **index**: 기본 문서
- **gzip on**: 전송 효율을 높여 페이지 로드 시간을 단축
- **error\_page 404**: 사용자 친화적인 에러 페이지 제공

### 2) API 리버스 프록시 설정

```
location /api/ {
    proxy_pass http://backend;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```

- **proxy\_pass**: `/api/`로 들어오는 요청을 백엔드 서버(backend)로 전달
- **proxy\_set\_header**: 실제 호스트 정보와 클라이언트 IP 등을 백엔드에 전달

---

## 6. 성능 최적화 팁 ?

### 1) 워커 프로세스와 파일 디스크립터 한도

```
worker_processes auto;
worker_rlimit_nofile 65535;
```

- **worker\_processes auto**: CPU 코어 수에 맞춰 적절히 워커 프로세스를 할당
- **worker\_rlimit\_nofile**: Nginx가 열 수 있는 파일(소켓) 최대 개수를 늘려 대규모 트래픽에 대비

### 2) 버퍼 및 요청 크기 설정

```
client_body_buffer_size 10K;
client_max_body_size 8m;
```

- **client\_body\_buffer\_size**: 요청 본문을 임시로 저장할 버퍼 크기
- **client\_max\_body\_size**: 업로드 가능한 요청(파일) 크기를 제한

### 3) 캐싱 설정

```
proxy_cache_path /path/to/cache levels=1:2 keys_zone=my_cache:10m;
location / {
    proxy_cache my_cache;
    proxy_cache_valid 200 1m;
    proxy_cache_valid any 10s;
    proxy_pass http://backend;
}
```

- **proxy\_cache\_path**: 캐싱할 위치, 디렉터리 구조, 키 영역 등을 정의
- **proxy\_cache\_valid**: 응답 코드별로 캐싱 유효 기간을 지정

---

## 7. 주의사항 ⚠️

1. **설정 파일 문법 확인**
   - 세미콜론(`;`) 누락, 중괄호(`{}`) 짝이 안 맞는 실수가 자주 발생
   - 설정 변경 후에는 `nginx -t` 명령으로 문법 오류를 검사하는 습관을 들이기
2. **보안 설정**
   - **버전 정보 숨기기**: `server_tokens off;`
   - 불필요한 HTTP 메서드(`TRACE`, `TRACK` 등) 차단
   - WAF(Web Application Firewall)나 추가 보안 모듈 연동 고려
3. **로그 관리**
   - 로그를 적절히 로테이션하여 디스크 용량을 관리
   - `access_log`, `error_log` 레벨을 사용 사례에 맞게 조정
4. **업스트림 헬스 체크**
   - 로드 밸런싱 시 백엔드 서버의 상태를 주기적으로 확인해 장애 감지
   - `health_check` 모듈을 활용하거나, 별도 솔루션과 연동 가능

---

## 8. 마치며 ?

이상으로 **Nginx**의 핵심 개념부터 주요 기능, 설정 방법, 그리고 성능 최적화 팁까지 살펴보았습니다.

- 동시성 처리와 이벤트 기반 구조 덕분에 **고성능**과 **안정성**을 확보할 수 있으며,
- 로드 밸런싱, SSL/TLS 처리, 정적 파일 서빙 등 다양한 기능을 한 번에 제공하여 **유연한 인프라 구축**이 가능합니다.

만약 높은 트래픽과 빠른 응답 시간이 필요한 서비스를 운영 중이거나, 여러 백엔드 서버를 효율적으로 관리하고 싶다면, **Nginx를 적극적으로 검토해 보시길 추천**드립니다!

---

### 참고자료 및 출처

- **Nginx 공식 문서**: <https://nginx.org/en/docs/>
- **Nginx Blog**: <https://www.nginx.com/blog/>
- **DigitalOcean Nginx 가이드**: <https://www.digitalocean.com/community/tutorials?q=nginx>

**Nginx**를 잘 활용하면, 적은 리소스로도 놀라운 퍼포먼스를 낼 수 있다는 점 꼭 기억해두세요!
