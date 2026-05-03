---
title: "?️ 리버스 프록시(Reverse Proxy), 왜 모든 서비스 앞에 서있을까요?"
date: 2024-11-17T09:00:05+09:00
slug: "386-리버스-프록시-Reverse-Proxy-왜-모든-서비스-앞에-서있을까요"
original_url: "https://memoryhub.tistory.com/386"
tistory_id: 386
draft: false
---

```
          +------------+      +-------------------+      +-----------------+
          |            |      |                   |      |                 |
User   |  Internet  |   |   Reverse Proxy   |  |  Backend Server |
          |            |      | (e.g., NGINX)     |      |  (e.g., Node.js)|
          +------------+      +-------------------+      +-----------------+
```

프로젝트를 개발하고 `localhost:3000`으로 서버를 띄웠을 때, "이제 이걸 어떻게 외부 사용자들이 안전하고 빠르게 쓰게 하지?" 라는 고민을 해보신 적 있나요? 서버 IP와 포트를 그대로 노출하자니 보안이 걱정되고, 사용자가 몰리면 서버가 버틸 수 있을지 막막합니다. 바로 이때 우리를 구해줄 든든한 문지기가 등장합니다.

이 글에서는 웹 서비스의 안정성과 보안, 성능을 모두 잡는 핵심 기술, 리버스 프록시(Reverse Proxy)에 대해 알아봅니다.

⚡ **TL;DR**

- 리버스 프록시는 클라이언트의 요청을 대신 받아 백엔드 서버에 전달하는 '중개 서버'입니다[3].
- 이를 통해 서버 부하 분산, 보안 강화, 성능 향상이라는 세 마리 토끼를 잡을 수 있습니다[2][5].

---

### 목차

1. **배경: 프록시가 뭔가요?**
2. **핵심 개념: 리버스 프록시의 작동 원리**
3. **실습: NGINX로 리버스 프록시 구축하기**
4. **베스트 프랙티스: 리버스 프록시 200% 활용법**
5. **마치며 & 참고자료**

---

### 1. 배경: 프록시가 뭔가요?

리버스 프록시를 이해하려면 먼저 '프록시(Proxy)'의 개념을 알아야 합니다. 프록시는 우리말로 '대리'를 의미하며, 클라이언트나 서버를 대신해 네트워크 통신을 처리하는 중개자 역할을 합니다[3][10]. 프록시는 역할에 따라 정방향 프록시와 리버스 프록시로 나뉩니다.

- ✅ **정방향 프록시 (Forward Proxy)**: **클라이언트**를 위한 대리인입니다. 내부 네트워크의 클라이언트가 인터넷에 접속할 때 거치는 서버로, 클라이언트의 신원을 숨기거나 접근을 제어하는 역할을 합니다[1][6]. 서버는 프록시 서버와 통신하므로 실제 클라이언트가 누구인지 알지 못합니다.
- ✅ **리버스 프록시 (Reverse Proxy)**: **서버**를 위한 대리인입니다. 인터넷의 클라이언트들이 웹 서버에 요청을 보낼 때 그 요청을 대신 받는 서버입니다[1]. 클라이언트는 리버스 프록시를 실제 서버라고 생각하며 통신하고, 실제 백엔드 서버의 존재는 외부로부터 숨겨집니다[4][6].

### 2. 핵심 개념: 리버스 프록시의 작동 원리

> **리버스 프록시는 클라이언트와 하나 이상의 웹 서버 사이에 위치하여 모든 클라이언트 요청을 가로채 백엔드 서버로 전달하는 중개 서버입니다[1][5][6].**

작동 흐름은 간단합니다.

1. **요청 수신**: 클라이언트(사용자)가 웹 서비스에 요청을 보내면, 이 요청은 백엔드 서버가 아닌 리버스 프록시 서버에 먼저 도착합니다[5].
2. **요청 평가 및 전달**: 리버스 프록시는 요청을 분석합니다. 캐시된 데이터가 있다면 즉시 응답하고, 없다면 미리 정해진 규칙(라우팅, 로드 밸런싱)에 따라 가장 적절한 백엔드 서버로 요청을 전달합니다[5].
3. **응답 수신 및 전달**: 백엔드 서버는 요청을 처리한 후 응답을 리버스 프록시에게 보냅니다[5].
4. **최종 응답**: 리버스 프록시는 백엔드 서버로부터 받은 응답을 클라이언트에게 최종적으로 전달합니다. 이 과정에서 응답 데이터를 캐싱하거나 압축할 수도 있습니다[2][5].

이 구조 덕분에 클라이언트는 수많은 백엔드 서버의 복잡한 구조를 알 필요 없이 단일 진입점(리버스 프록시)과 통신하게 됩니다[4].

### 3. 실습: NGINX로 리버스 프록시 구축하기

가장 인기 있는 오픈 소스 리버스 프록시인 NGINX를 사용하여 직접 리버스 프록시를 설정해보겠습니다[2]. NGINX는 높은 성능과 낮은 메모리 사용량으로 유명합니다[2].

**① 기본 리버스 프록시 설정**

내 로컬 환경에서 3000번 포트로 실행 중인 Node.js 애플리케이션을 80번 포트로 접속할 수 있도록 설정하는 예제입니다.

```
# /etc/nginx/sites-available/default 또는 nginx.conf

server {
    # 80번 포트로 들어오는 요청을 수신합니다.
    listen 80;

    location / {
        # 모든 요청을 http://127.0.0.1:3000 으로 전달합니다.
        # 실제 애플리케이션이 실행 중인 주소입니다.
        proxy_pass http://127.0.0.1:3000;

        # 클라이언트의 실제 IP, 프로토콜 등의 헤더 정보를 백엔드 서버로 전달합니다.
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**② 로드 밸런싱 적용**

트래픽이 많아져서 서버를 여러 대로 증설했다고 가정해봅시다. `upstream` 지시어를 사용하면 들어오는 요청을 여러 서버에 분산시킬 수 있습니다[2].

```
http {
    # 'backend_servers'라는 이름으로 서버 그룹을 정의합니다.
    upstream backend_servers {
        # 요청을 분산시킬 서버 목록
        # 기본 전략은 round-robin 방식입니다.
        server 127.0.0.1:3001;
        server 127.0.0.1:3002;
        server 127.0.0.1:3003;
    }

    server {
        listen 80;

        location / {
            # 요청을 'backend_servers' 그룹으로 전달합니다.
            proxy_pass http://backend_servers;
        }
    }
}
```

이제 NGINX는 3001, 3002, 3003 포트로 들어오는 요청을 공평하게 나누어 전달하여 서버 한 대에 부하가 몰리는 것을 막아줍니다[2].

### 4. 베스트 프랙티스: 리버스 프록시 200% 활용법

리버스 프록시는 단순한 요청 전달 외에도 다양한 고급 기능을 제공하여 서비스 품질을 크게 향상시킬 수 있습니다[2][6].

| 기능 | 장점 | 주요 NGINX 설정 |
| --- | --- | --- |
| **로드 밸런싱** | 여러 서버로 트래픽을 분산하여 부하를 줄이고 특정 서버 장애 시에도 서비스 중단을 방지합니다[2][5]. | `upstream` 블록 정의 및 `proxy_pass` 지시어 |
| **보안 강화** | 백엔드 서버의 IP와 구조를 숨기고, 악성 요청을 필터링합니다. 외부에는 리버스 프록시만 노출됩니다[2][4][6]. | `allow`, `deny` 지시어로 특정 IP 접근 제어[2] |
| **SSL/TLS 암호화** | SSL 인증서를 리버스 프록시에만 설정하여 관리를 일원화하고 백엔드 서버의 암/복호화 부담을 줄입니다(SSL Termination)[4][7]. | `listen 443 ssl;` `ssl_certificate` 등 설정 |
| **캐싱** | 이미지, CSS 등 정적 콘텐츠를 캐싱하여 응답 속도를 높이고 백엔드 서버의 부하를 크게 줄입니다[2][4][8]. | `proxy_cache_path`, `proxy_cache` 지시어 |
| **API 게이트웨이** | 마이크로서비스 아키텍처에서 여러 API의 단일 진입점 역할을 하며, 라우팅, 인증 등을 중앙에서 처리합니다[2][4]. | `location` 블록을 경로별로 다르게 설정하여 각기 다른 백엔드로 전달 |

### 5. 마치며

리버스 프록시는 이제 현대 웹 아키텍처에서 선택이 아닌 필수 요소로 자리 잡았습니다.

- 리버스 프록시는 클라이언트와 서버 사이의 필수적인 '문지기' 역할을 합니다.
- 단순한 요청 전달을 넘어 로드 밸런싱, 보안, 캐싱 등 서비스의 안정성과 성능을 높이는 핵심 기능을 제공합니다[2].
- NGINX와 같은 강력한 도구를 사용하면 복잡한 설정 없이도 견고한 리버스 프록시 환경을 구축할 수 있습니다[2][3].

**실제 프로젝트 적용 팁**: 실제 운영 환경에서는 리버스 프록시 서버 자체의 고가용성(High Availability)을 구성하여, 리버스 프록시가 다운되더라도 서비스가 중단되지 않도록 대비하는 것이 중요합니다.

❤️ 글이 유용하셨다면 하트와 댓글 부탁드립니다! 여러분의 피드백이 더 좋은 글을 쓰는 데 큰 힘이 됩니다.

---

**참고자료**

- NGINX Reverse Proxy 공식 문서 [11]
- 리버스 프록시(Reverse Proxy) 쉽게 이해하기 (aday7.tistory.com) [2]
- 리버스 프록시란? (Cloudflare) [1]

[1] <https://www.cloudflare.com/ko-kr/learning/cdn/glossary/reverse-proxy/>  
[2] <https://aday7.tistory.com/entry/%EB%A6%AC%EB%B2%84%EC%8A%A4-%ED%94%84%EB%A1%9D%EC%8B%9CReverse-Proxy-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-%EA%B0%9C%EB%85%90%EB%B6%80%ED%84%B0-%ED%95%84%EC%9A%94%EC%84%B1-%EC%98%A4%ED%94%88-%EC%86%8C%EC%8A%A4-%EC%86%94%EB%A3%A8%EC%85%98%EA%B9%8C%EC%A7%80>  
[3] <https://narup.tistory.com/238>  
[4] <https://api7.ai/ko/learning-center/api-gateway-guide/api-gateway-vs-reverse-proxy-vs-load-balancer>  
[5] <https://brightdata.com/blog/proxy-101/reverse-proxy-defined>  
[6] <https://en.wikipedia.org/wiki/Reverse_proxy>  
[7] <https://velog.io/@jmjmjmz732002/Infra-Reverse-Proxy..-%EA%B3%BC%EC%97%B0-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C%EC%9A%94>  
[8] <https://www.f5.com/ko_kr/glossary/reverse-proxy>  
[9] <https://with-cloud.tistory.com/59>  
[10] <https://losskatsu.github.io/it-infra/reverse-proxy/>  
[11] <https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/>  
[12] <https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html>  
[13] <https://www.howtogeek.com/devops/what-is-a-reverse-proxy-and-how-does-it-work/>  
[14] <https://de.wikipedia.org/wiki/Reverse_Proxy>  
[15] <https://www.youtube.com/watch?v=Vfe4F6jlbfc>  
[16] <https://www.youtube.com/watch?v=MYubx9GmK1Q>
