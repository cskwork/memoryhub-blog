---
title: "? Docker 컨테이너에서 로컬 Ollama 연결, 왜 host.docker.internal이 답일까?"
date: 2025-09-16T09:01:13+09:00
slug: "779-Docker-컨테이너에서-로컬-Ollama-연결-왜-host-docker-internal이-답일까"
original_url: "https://memoryhub.tistory.com/779"
tistory_id: 779
draft: false
---

```
    ┌─────────────────────────────────────┐
    │         Host Machine                │
    │  ┌─────────────────────────────┐    │
    │  │       Ollama                │    │
    │  │    localhost:11434          │    │
    │  └─────────────────────────────┘    │
    │              ▲                      │
    │              │                      │
    │   host.docker.internal:11434        │
    │              │                      │
    │  ┌─────────────────────────────┐    │
    │  │    Docker Container         │    │
    │  │   ┌─────────────────────┐   │    │
    │  │   │   Your App          │   │    │
    │  │   │                     │   │    │
    │  │   └─────────────────────┘   │    │
    │  └─────────────────────────────┘    │
    └─────────────────────────────────────┘
```

Docker 컨테이너에서 애플리케이션을 실행하다가 로컬에 설치된 Ollama에 연결하려고 localhost:11434를 사용했는데 연결이 안 된 경험 있으신가요? 저도 처음엔 당황했지만, 해답은 생각보다 간단했습니다.

이 글을 읽으면 Docker의 네트워크 구조를 이해하고, host.docker.internal을 활용해 컨테이너에서 호스트의 Ollama에 완벽하게 연결하는 방법을 터득하게 됩니다.

## 목차

1. 배경
2. 핵심 개념 정리
3. 실습
4. 모범 사례·베스트 프랙티스
5. 마치며 & 참고자료

---

## 1. 배경

Docker 컨테이너에서 로컬 호스트의 Ollama(포트 11434)에 연결하려고 할 때 흔히 발생하는 문제가 바로 네트워크 연결 실패입니다. 많은 개발자들이 localhost:11434를 사용했다가 "Connection refused" 오류를 마주하게 됩니다.

**문제의 핵심 원인들:**

- Docker 컨테이너는 격리된 네트워크 환경을 가짐
- 컨테이너 내부에서 localhost는 컨테이너 자신을 가리키므로 호스트의 서비스에 접근할 수 없음
- 기존 포트 포워딩 방식으로는 해결되지 않는 역방향 연결 문제

**관련 용어 정리:**

용어 정의

|  |  |
| --- | --- |
| **Ollama** | 로컬에서 LLM을 실행할 수 있는 도구, 기본 포트 11434 사용 |
| **host.docker.internal** | Docker 컨테이너에서 호스트(로컬 머신)로 접근할 수 있도록 제공되는 특수한 호스트명 |
| **Docker Bridge Network** | 하나의 호스트 컴퓨터 내에서 여러 컨테이너이 서로 소통할 수 있도록 해주는 기본 네트워크 |

## 2. 핵심 개념

> **한 줄 정의**  
> **host.docker.internal은 Docker 컨테이너가 호스트 시스템의 localhost를 대신해 사용하는 특수 도메인입니다.**

Docker 컨테이너는 독립된 네트워크 환경을 가지므로, 컨테이너 내부에서 호스트의 네트워크 자원에 접근하려면 특정한 방법이 필요합니다. Mac이나 Windows의 경우에는 기본적으로 DNS 이름 host.docker.internal으로 컨테이너 내부에서 Host에 접근이 가능합니다.

```
# docker-compose.yml 예제
version: '3.8'
services:
  my-app:
    image: my-app
    environment:
      - OLLAMA_BASE_URL=http://host.docker.internal:11434
```

## 3. 실습

### ① 환경 확인 및 준비

먼저 로컬에 Ollama가 정상적으로 실행되고 있는지 확인하세요:

```
# Ollama 서비스 상태 확인
curl http://localhost:11434/api/version

# 정상 응답 예시
{"version":"0.1.26"}
```

### ② Windows/Mac에서 기본 설정

Windows 11에서는 <http://host.docker.internal:11434를> Base URL로 사용하면 됩니다.

```
# Docker 컨테이너 실행 예제
docker run -d \
  -e OLLAMA_API_BASE_URL=http://host.docker.internal:11434 \
  -p 8080:8080 \
  your-app:latest
```

### ③ Linux에서 추가 설정

Linux에서는 host.docker.internal이 기본적으로 지원되지 않으므로, 별도로 설정이 필요합니다.

```
# Linux에서 host.docker.internal 활성화
docker run -d \
  --add-host=host.docker.internal:host-gateway \
  -e OLLAMA_API_BASE_URL=http://host.docker.internal:11434 \
  -p 8080:8080 \
  your-app:latest
```

### ④ Docker Compose 설정

```
# docker-compose.yml
version: '3.8'
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    ports:
      - "8080:8080"
    extra_hosts:
      - "host.docker.internal:host-gateway"  # Linux 지원
    environment:
      - OLLAMA_BASE_URL=http://host.docker.internal:11434
    volumes:
      - open-webui:/app/backend/data
    restart: always

volumes:
  open-webui:
```

### ⑤ 연결 테스트

```
# 컨테이너 내부에서 연결 테스트
docker exec -it your-container-name curl http://host.docker.internal:11434/api/tags

# 성공 시 Ollama 모델 목록이 반환됩니다
```

## 4. 모범 사례

패턴 장점 주의점

|  |  |  |
| --- | --- | --- |
| **host.docker.internal 사용** | 크로스 플랫폼 호환성, 간단한 설정 | 개발용이며 프로덕션 환경에서는 작동하지 않음 |
| **네트워크 브릿지 모드** | 성능 최적화, 더 나은 격리 | 복잡한 설정 필요 |
| **컨테이너 내부 Ollama 설치** | 완전한 격리, 배포 단순화 | 리소스 중복, 이미지 크기 증가 |

**환경별 권장사항:**

- **개발 환경**: host.docker.internal 사용으로 빠른 개발
- **스테이징**: 네트워크 브릿지 또는 별도 Ollama 컨테이너
- **프로덕션**: 완전히 분리된 Ollama 서비스 또는 컨테이너 내부 설치

**트러블슈팅 체크리스트:**

1. Ollama 서비스가 0.0.0.0:11434에서 리스닝하는지 확인
2. 방화벽에서 11434 포트가 열려있는지 확인
3. Linux 환경에서는 --add-host=host.docker.internal:host-gateway 옵션 추가
4. 컨테이너 로그에서 정확한 오류 메시지 확인

## 5. 마치며

Docker 컨테이너에서 로컬 Ollama에 연결하는 핵심은 host.docker.internal을 활용하는 것입니다. 이는 컨테이너의 격리된 네트워크 환경에서 호스트 시스템에 접근할 수 있는 Docker의 표준 메커니즘입니다. Linux 환경에서는 추가 설정이 필요하지만, 한 번 설정하면 안정적으로 동작합니다.

**실제 프로젝트 적용 팁**: 환경변수를 활용해 개발/프로덕션 환경을 분리하고, Docker Compose의 extra\_hosts 설정으로 크로스 플랫폼 호환성을 확보하세요.

⸻

**참고자료**

- Ollama 공식 Docker 이미지 가이드
- Stack Overflow: Docker 컨테이너에서 Ollama 연결 문제 해결
- Docker 네트워크 및 host.docker.internal 상세 가이드
