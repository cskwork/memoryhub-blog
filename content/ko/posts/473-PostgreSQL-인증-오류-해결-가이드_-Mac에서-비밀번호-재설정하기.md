---
title: "PostgreSQL 인증 오류 해결 가이드: Mac에서 비밀번호 재설정하기"
date: 2025-03-15T15:13:42+09:00
slug: "473-PostgreSQL-인증-오류-해결-가이드_-Mac에서-비밀번호-재설정하기"
original_url: "https://memoryhub.tistory.com/473"
tistory_id: 473
draft: false
categories: ["데브 데이터베이스"]
tags: ["PostgreSQL"]
---

## 문제 소개

맥(Mac)에서 PostgreSQL을 사용할 때 다음과 같은 오류 메시지를 마주친 적이 있으신가요?

```
connection failed: connection to server at "127.0.0.1", port 5432 failed: FATAL: password authentication failed for user "postgres"
```

올바른 비밀번호를 입력했음에도 불구하고 이러한 오류가 발생하는 경우가 있습니다. 특히 pgAdmin과 같은 GUI 도구를 사용할 때 자주 발생합니다. 이번 글에서는 이 문제의 원인과 해결 방법을 단계별로 알아보겠습니다.

## 오류의 원인

PostgreSQL 인증 오류가 발생하는 주요 원인은 다음과 같습니다:

1. 비밀번호를 잊어버렸거나 초기 설정이 올바르지 않은 경우
2. PostgreSQL의 인증 방식(scram-sha-256, md5 등)과 클라이언트 설정이 맞지 않는 경우
3. pg\_hba.conf 파일에 인증 설정이 잘못 구성된 경우
4. 다중 PostgreSQL 인스턴스가 설치되어 혼란을 주는 경우

## 환경 확인하기

먼저 어떤 버전의 PostgreSQL이 어디에 설치되어 있는지 확인해야 합니다:

```
which postgres
postgres --version
```

위 명령어는 PostgreSQL 실행 파일의 위치와 버전을 보여줍니다. 예를 들어:

```
/Library/PostgreSQL/17/bin/postgres
postgres (PostgreSQL) 17.4
```

## PostgreSQL 프로세스 확인

PostgreSQL이 실행 중인지 확인합니다:

```
ps aux | grep postgres
```

실행 중이라면 다음과 같이 여러 프로세스가 표시됩니다:

```
postgres   13208   0.0  0.1 411076016  21456   ??  Ss    2:55PM   0:00.07 /Library/PostgreSQL/17/bin/postgres -D /Library/PostgreSQL/17/data
postgres   13209   0.0  0.0 410929280   2448   ??  Ss    2:55PM   0:00.00 postgres: logger
...
```

## 해결 방법: PostgreSQL 비밀번호 재설정하기

### 1단계: pg\_hba.conf 파일 수정하기

PostgreSQL의 인증 설정을 변경하여 임시로 비밀번호 없이 접속할 수 있도록 합니다:

```
sudo nano /Library/PostgreSQL/17/data/pg_hba.conf
```

파일에서 다음과 같은 설정을 찾아:

```
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
```

임시로 'trust' 인증 방식으로 변경합니다:

```
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust
```

### 2단계: PostgreSQL 설정 다시 로드하기

설정 변경 사항을 적용합니다:

```
sudo -u postgres /Library/PostgreSQL/17/bin/pg_ctl reload -D /Library/PostgreSQL/17/data
```

### 3단계: 비밀번호 없이 접속하여 새 비밀번호 설정하기

이제 비밀번호 없이 접속할 수 있습니다:

```
/Library/PostgreSQL/17/bin/psql -U postgres -h 127.0.0.1
```

접속 후 비밀번호를 변경합니다:

```
ALTER USER postgres WITH PASSWORD '새로운_비밀번호';
\q
```

### 4단계: 보안 설정 복원하기

pg\_hba.conf 파일을 다시 열고 인증 방식을 'scram-sha-256'으로 되돌립니다:

```
sudo nano /Library/PostgreSQL/17/data/pg_hba.conf
```

다음과 같이 수정:

```
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
```

### 5단계: 설정 다시 로드하고 확인하기

```
sudo -u postgres /Library/PostgreSQL/17/bin/pg_ctl reload -D /Library/PostgreSQL/17/data
```

새 비밀번호로 접속이 되는지 확인합니다:

```
/Library/PostgreSQL/17/bin/psql -U postgres -h 127.0.0.1
```

## 대체 방법: postgres 유저로 직접 접근하기

만약 위 방법이 실패한다면, postgres 시스템 유저로 전환하여 시도할 수 있습니다:

```
sudo su - postgres
/Library/PostgreSQL/17/bin/pg_ctl stop -D /Library/PostgreSQL/17/data
/Library/PostgreSQL/17/bin/postgres --single -D /Library/PostgreSQL/17/data postgres
```

프롬프트에서 비밀번호를 변경합니다:

```
ALTER USER postgres WITH PASSWORD '새로운_비밀번호';
```

Ctrl+D로 종료한 후 서버를 재시작합니다:

```
/Library/PostgreSQL/17/bin/pg_ctl start -D /Library/PostgreSQL/17/data
```

## 알아두면 좋은 점

1. **보안 주의사항**: 'trust' 인증 방식은 임시로만 사용하세요. 비밀번호 재설정 후 즉시 원래 인증 방식으로 돌아가야 합니다.
2. **PostgreSQL 17의 기본 인증 방식**: PostgreSQL 17은 scram-sha-256 인증을 기본으로 사용합니다. 이는 더 안전하지만 일부 오래된 클라이언트와 호환성 문제가 있을 수 있습니다.
3. **pgAdmin 연결 설정**: pgAdmin에서 연결할 때 정확한 호스트명(127.0.0.1 또는 localhost), 포트(5432), 그리고 사용자 이름(postgres)을 사용하세요.
4. **여러 PostgreSQL 인스턴스**: 시스템에 여러 버전의 PostgreSQL이 설치된 경우, 원하는 인스턴스에 연결하고 있는지 확인하세요.
5. **로그 확인**: 문제가 지속되면 `/Library/PostgreSQL/17/data/log/` 디렉토리에서 로그 파일을 확인하여 자세한 오류 내용을 파악하세요.

## 결론

PostgreSQL의 비밀번호 인증 오류는 흔히 발생하지만, 적절한 단계를 따르면 쉽게 해결할 수 있습니다. 이 가이드가 여러분의 PostgreSQL 연결 문제 해결에 도움이 되길 바랍니다. 추가 질문이나 피드백이 있으시면 댓글로 남겨주세요!

---

참고 자료:

- [PostgreSQL 공식 문서: Client Authentication](https://www.postgresql.org/docs/current/client-authentication.html)
- [PostgreSQL 17 릴리스 노트](https://www.postgresql.org/docs/17/release-17.html)
