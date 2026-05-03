---
title: "ngrok으로 localhost를 공개 URL로! 5분 만에 터널링 마스터하기"
date: 2025-10-12T23:23:39+09:00
slug: "849-ngrok으로-localhost를-공개-URL로-5분-만에-터널링-마스터하기"
original_url: "https://memoryhub.tistory.com/849"
tistory_id: 849
draft: false
---

```
    ╔══════════════════════════════════════╗
    ║                                      ║
    ║   [Localhost] ←→ [ngrok] ←→ [?]    ║
    ║                                      ║
    ║   로컬 서버를 순식간에 공개하는      ║
    ║          마법의 터널링 도구          ║
    ║                                      ║
    ╚══════════════════════════════════════╝
```

웹훅 테스트하려다 막막했던 경험, 있으신가요? 프론트 개발자에게 API 결과를 빨리 공유해야 하는데 배포는 너무 번거롭고... 바로 이럴 때 필요한 게 ngrok입니다. 로컬 환경의 포트 하나만 열어두면, 전 세계 어디서든 접속 가능한 HTTPS URL이 생성됩니다. 이 글을 읽으면 ngrok 설치부터 실전 활용까지 단 5분 만에 터널링 전문가가 될 수 있습니다.

**로컬 서버를 방화벽 너머 공개 인터넷에 안전하게 노출시키는 가장 빠른 방법**

## 배경

ngrok을 선택하는 이유

ngrok은 로컬호스트를 공개적으로 접근 가능한 URL로 변환해주는 역방향 프록시 터널링 소프트웨어입니다. 개발 환경에서 외부 접근이 필요한 다양한 상황에서 포트 포워딩이나 서버 배포 없이 즉시 사용할 수 있습니다.

### 주요 활용 시나리오

| 상황 | ngrok 활용 |
| --- | --- |
| 웹훅 테스트 | 외부 API에서 로컬 서버로 콜백 수신 |
| 모바일 앱 개발 | 실제 디바이스에서 로컬 백엔드 테스트 |
| 클라이언트 데모 | 배포 없이 로컬 작업물 즉시 공유 |
| 소셜 로그인 개발 | OAuth 리다이렉트 URL에 공개 도메인 필요 |
| API 통합 테스트 | 외부 서비스와 로컬 환경 연동 |

### 핵심 용어 정리

**터널링**: 네트워크 방화벽을 통과해 외부에서 내부 네트워크로 접근할 수 있게 만드는 기술

**리버스 프록시**: 외부 요청을 받아 내부 서버로 전달하는 중개 서버

**포트 포워딩**: 라우터 설정을 통해 특정 포트를 외부에 개방하는 방식 (ngrok은 이 과정 불필요)

## 핵심

> ngrok은 NAT와 방화벽 뒤의 로컬 서버를 안전한 터널을 통해 공개 인터넷에 즉시 노출시키는 도구

ngrok은 HTTP 터널을 생성해 로컬호스트를 즉시 인터넷에 노출시키므로 웹훅 테스트, API 개발, 지역별 개발 환경 구축에 필수적입니다.

**주요 기능**

- HTTP/HTTPS/TCP 프로토콜 지원으로 다양한 서버 타입에 대응
- 자동 HTTPS 인증서 생성으로 보안 연결 제공
- 웹 콘솔([http://127.0.0.1:4040)을](http://127.0.0.1:4040)%EC%9D%84) 통한 실시간 트래픽 모니터링 및 리플레이 기능
- 무료 플랜으로도 분당 120회 TCP 커넥션 지원

**작동 원리**

ngrok 클라이언트가 로컬 서버와 ngrok 클라우드 서버 간 보안 터널을 생성합니다. 외부 요청은 ngrok 서버를 거쳐 이 터널을 통해 로컬호스트로 전달됩니다.

## 실습

### 1단계: 설치하기

**Mac 환경 (Homebrew)**

```
brew install ngrok
```

**Windows 환경**

공식 홈페이지([https://ngrok.com/)에서](https://ngrok.com/)%EC%97%90%EC%84%9C) Windows용 압축 파일 다운로드 후 압축 해제

**Linux 환경**

```
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | \
sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && \
echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | \
sudo tee /etc/apt/sources.list.d/ngrok.list && \
sudo apt update && sudo apt install ngrok
```

### 2단계: 인증 토큰 등록

기본적으로 ngrok는 세션 유효기간이 존재하며, 세션 만료 시 URL이 변경됩니다. 안정적인 사용을 위해 회원가입 후 인증 토큰을 등록하세요.

1. <https://dashboard.ngrok.com/signup> 접속하여 회원가입
2. 대시보드에서 Auth Token 확인
3. 터미널에서 토큰 등록

```
ngrok authtoken [Your_Authtoken]
```

토큰 등록 확인:

```
ngrok config edit
```

### 3단계: 로컬 서버 터널 생성

로컬에서 서버를 실행한 상태에서 ngrok을 시작합니다.

**기본 사용법**

```
# HTTP 서버를 8080 포트에서 실행 중인 경우
ngrok http 8080
```

**실행 결과 화면**

터미널에 다음과 같은 정보가 표시됩니다:

```
Session Status         online
Account                Your Name (Plan: Free)
Version                3.3.1
Region                 Japan (jp)
Web Interface          http://127.0.0.1:4040
Forwarding             https://abc123.ngrok-free.app -> http://localhost:8080
```

Forwarding 줄에 표시된 URL(예: [https://abc123.ngrok-free.app)이](https://abc123.ngrok-free.app)%EC%9D%B4) 외부 접속 주소입니다.

### 4단계: 트래픽 모니터링

<http://127.0.0.1:4040> 주소로 접속하면 ngrok 웹 인터페이스에서 상태와 HTTP 요청 현황을 실시간으로 확인할 수 있습니다.

웹 인터페이스 주요 기능:

- 모든 HTTP 요청/응답 헤더 및 바디 확인
- 특정 요청을 다시 보내는 Replay 기능
- 연결 통계 및 성능 지표

### 5단계: 데이터베이스 포트 터널링

웹 서버뿐만 아니라 MySQL, PostgreSQL 같은 데이터베이스 포트도 터널링 가능합니다.

```
# MySQL
ngrok tcp 3306

# PostgreSQL
ngrok tcp 5432

# MongoDB
ngrok tcp 27017
```

## 모범사례/패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| 무료 플랜 활용 | 비용 없이 즉시 시작 가능, 분당 120 커넥션 제공 | 세션 종료 시 URL 변경, 고정 도메인 미제공 |
| 인증 토큰 등록 | 세션 시간 무제한, 무료 고정 도메인 1개 제공 | 회원가입 필요 |
| 웹 인터페이스 활용 | 실시간 디버깅, 요청 리플레이로 개발 효율 향상 | 로컬 4040 포트 사용 중이면 충돌 |
| TCP 터널링 | 데이터베이스 등 HTTP 외 프로토콜 지원 | 보안 설정 필수 (인증, IP 제한) |
| 유료 플랜 사용 | 커스텀 도메인, 여러 터널 동시 실행 가능 | 월 비용 발생 |

## 마치며

ngrok은 로컬 개발 환경을 외부에 즉시 공개할 수 있는 가장 간편한 솔루션입니다. 포트 포워딩 설정 없이 한 줄 명령어로 HTTPS 보안 터널이 생성되며, 웹훅 테스트부터 클라이언트 데모까지 다양한 시나리오에서 개발 생산성을 크게 향상시킵니다.

웹훅 기능 테스트나 외부 API 연동 디버깅이 필요할 때 ngrok은 필수 도구입니다.

## 참고자료

- ngrok 공식 홈페이지 (<https://ngrok.com/>)
- ngrok 공식 문서 (<https://ngrok.com/docs>)
- ngrok 대시보드 (<https://dashboard.ngrok.com/>)
- Outsider's Dev Story - ngrok으로 로컬 네트워크의 터널 열기 (<https://blog.outsider.ne.kr/1159>)
- Aliencube - 웹훅 기능을 테스트 하기 좋은 도구들 소개 (<https://blog.aliencube.org/ko/2017/06/02/tools-for-testing-webhooks/>)
