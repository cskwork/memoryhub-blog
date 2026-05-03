---
title: "Mac OS에서 Coolify 설치 오류 해결 방법"
date: 2025-03-26T21:50:27+09:00
slug: "532-Mac-OS에서-Coolify-설치-오류-해결-방법"
original_url: "https://memoryhub.tistory.com/532"
tistory_id: 532
draft: false
---

Mac OS에서 Coolify 설치 시 발생하는 `/etc/os-release: No such file or directory` 오류는 Mac OS가 리눅스 배포판이 아니기 때문에 발생합니다. Coolify는 주로 리눅스 환경을 지원하며, Mac OS에서는 Docker Desktop을 통해 설치해야 합니다.

## 해결 방법

Mac OS에서 Coolify를 설치하려면 다음 두 가지 방법이 있습니다:

1. **Docker Desktop을 사용한 설치 (권장)**:

   - Docker Desktop 설치
   - Coolify Docker 이미지 실행
2. **Docker Compose를 사용한 설치**:

   - docker-compose.yml 파일 생성
   - Docker Compose 명령으로 실행

먼저 Docker Desktop을 사용한 방법을 살펴보겠습니다.

## Docker Desktop을 사용한 설치 방법

```
# 1. Docker Desktop이 설치되어 있는지 확인
docker --version

# 2. 설치되어 있지 않다면 설치
# https://www.docker.com/products/docker-desktop/ 에서 다운로드

# 3. Coolify 이미지 실행
docker run -d \
  --name coolify \
  -p 8000:8000 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v coolify-db:/app/db \
  -v coolify-backup:/app/backup \
  coollabsio/coolify:latest
```

설치가 완료되면 브라우저에서 `http://localhost:8000`으로 접속하여 Coolify 대시보드에 액세스할 수 있습니다.

이 방법으로도 문제가 계속되면 다음과 같이 Docker Compose를 사용하실 수 있습니다:

## Docker Compose를 사용한 설치 방법

1. `docker-compose.yml` 파일 생성:

```
version: '3'
services:
  coolify:
    image: coollabsio/coolify:latest
    container_name: coolify
    restart: unless-stopped
    ports:
      - "8000:8000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - coolify-db:/app/db
      - coolify-backup:/app/backup

volumes:
  coolify-db:
  coolify-backup:
```

2. Docker Compose로 실행:

```
docker-compose up -d
```

## 결론

Mac OS에서는 Coolify 설치 스크립트가 직접 작동하지 않으므로, Docker Desktop을 통해 설치하는 것이 가장 적합합니다. 이 방법은 Coolify 공식 문서에서도 권장하는 Mac OS 환경에서의 설치 방법입니다.

## 출처

1. Coolify 공식 문서, "Installation Guide", <https://coolify.io/docs/installation/>
2. Docker Desktop 다운로드, <https://www.docker.com/products/docker-desktop/>
