---
title: "Firewalld에서 포트 구성 방법"
date: 2024-06-12T08:43:43+09:00
slug: "282-Firewalld에서-포트-구성-방법"
original_url: "https://memoryhub.tistory.com/282"
tistory_id: 282
draft: false
categories: ["데브 옵스"]
tags: ["Firewalld"]
---

### **포트 열기**

- **명령어**: **`firewalld`**에서 포트를 열려면 다음 명령어를 사용합니다:
  - ```
    sudo firewall-cmd --add-port={포트번호}/tcp --permanent # --permanent 옵션은 방화벽 규칙을 영구적으로 적용합니다.
    ```
- **예시**: 여러 응용 프로그램에서 일반적으로 사용되는 여러 포트를 열기:
  - ```
    sudo firewall-cmd --add-port=8080/tcp --permanent # 일반적인 대체 HTTP 포트
    sudo firewall-cmd --add-port=3306/tcp --permanent # MySQL/MariaDB
    sudo firewall-cmd --add-port=1521/tcp --permanent # Oracle
    # 기타 포트들을 계속 열기
    sudo firewall-cmd --add-port={8080/tcp,3306/tcp,1521/tcp} --permanent # 여러 포트를 한 번에 추가
    sudo firewall-cmd --reload # 변경 사항을 적용하고, firewalld를 재시작하지 않고 새 규칙을 활성화합니다.
    ```
- **검증**: 포트가 열렸는지 확인하기 위해:
  - ```
    firewall-cmd --list-ports
    ```

### **일반적인 포트와 그 용도**

- **HTTP 및 대체 포트**: 80, 8080 포트는 HTTP 서비스용입니다.
- **데이터베이스 서비스**:
  - 3306/tcp: MySQL 또는 MariaDB 데이터베이스 서버
  - 1521/tcp: Oracle 데이터베이스 서버
  - 6379/tcp: Redis 키-값 저장소 서비스
- **기타 응용 프로그램**:
  - 5555: 다양한 네트워크 서비스에 사용됩니다.
  - 4444: 웹 응용 프로그램이나 개발 환경에서 자주 사용됩니다.

### **실제 애플리케이션 테스트**

### **연결 테스트를 위한 예시 URL 및 IP**

- **보안 주의**: 테스트 URL과 IP는 인터넷에 노출되지 않도록 관리하세요. 테스트가 완료된 후에는 적절히 방화벽 규칙을 재설정하거나 수정하세요.
  - **DB 테스트**: **`http://127.0.0.1:8082/app`**
  - **App 테스트**: **`http://127.0.0.1:13120/app2`**
  - **Oracle 연결**: Oracle과 같은 데이터베이스에 연결할 때 **`sys dba`**로 주의해서 접속해야 합니다.

### **주요 참고자료**

- [유용한 10가지 firewall-cmd 명령어](https://www.linuxcloudvps.com/blog/10-useful-firewall-cmd-commands-in-linux/)
- [Firewalld 공식 문서](https://firewalld.org/documentation/)
- [Red Hat Enterprise Linux에서 Firewalld 사용법](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-using_firewalls)
