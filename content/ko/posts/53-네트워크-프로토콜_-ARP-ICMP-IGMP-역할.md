---
title: "네트워크 프로토콜: ARP, ICMP, IGMP 역할"
date: 2024-05-25T14:38:18+09:00
slug: "53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할"
original_url: "https://memoryhub.tistory.com/53"
tistory_id: 53
draft: false
categories: ["데브 컨셉"]
tags: ["정보처리기사"]
cover:
  image: "images/53-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_-ARP-ICMP-IGMP-%EC%97%AD%ED%95%A0/img.png"
  relative: false
  hidden: false
---

- ARP (Address Resolution Protocol)
  - 하드웨어 주소 연결 규약
  - IP 주소를 물리적 네트워크 주소로 대응(bind)시키기 위해 사용되는 프로토콜동작 원리
  1. 같은 네트워크 세그먼트에 있는 두 IP 장비가 통신할 때 사용
  2. 네트워크에서 이용하는 특정 매체에 맞게 정의된 하위 계층 프로토콜과 주소 지정 방식 사용

  ![](/images/53-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_-ARP-ICMP-IGMP-%EC%97%AD%ED%95%A0/img.png)

  예시
  - 이더넷 환경에서의 통신:
    1. IP 시스템 통신 시 먼저 로컬 장비가 속한 네트워크에 연결된 다른 장비의 하드웨어 주소 확인
    2. ARP가 IP 주소를 해당 하드웨어(MAC) 주소로 변환하는 서비스 제공

![](/images/53-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_-ARP-ICMP-IGMP-%EC%97%AD%ED%95%A0/img_1.png)

![](/images/53-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_-ARP-ICMP-IGMP-%EC%97%AD%ED%95%A0/img_2.png)

## ICMP

- 개요
  - IP는 신뢰성을 보장하지 않음
  - 네트워크 장애나 중계 라우터 등의 에러에 대처하기 위한 프로토콜주요 기능
  - 오류 정보를 발견하여 송신측에 메시지 전달
  - 네트워크 문제 진단 및 보고활용 예: ping
  - ICMP Echo Request 메시지 전송
  - 목적지 시스템에서 ICMP Echo Reply 메시지로 응답
  - 응답 시간을 측정하여 네트워크 연결 상태 검사

![](/images/53-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_-ARP-ICMP-IGMP-%EC%97%AD%ED%95%A0/img_3.png)

![](/images/53-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_-ARP-ICMP-IGMP-%EC%97%AD%ED%95%A0/img_4.png)

ping 도구는 ICMP Echo Request 메시지를 전송해 목적지 시스템에서 ICMP Echop Reply 메시지로 응답 받는 시간을 측정해 네트워크 연결을 검사한다.

```
ping www.yahoo.co.kr
tracert 59.5.67.254
```

ICMP 메시지 포맷

![](/images/53-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_-ARP-ICMP-IGMP-%EC%97%AD%ED%95%A0/img_5.png)

## IGMP

- 개요
  - 멀티캐스트 그룹 관리를 위한 프로토콜통신 방식 비교
  1. Unicast: 1대1 통신
  2. Broadcast: 1대 모든 호스트 통신
  3. Multicast: 1대 특정 그룹 통신IGMP의 특징
  - 그룹 주소를 사용하여 패킷 전송
  - 지정된 그룹의 호스트만 데이터 수신, 다른 네트워크 장비는 무시
  - Broadcast의 제한을 피해 효율적인 그룹 통신 가능활용
  - 한 호스트에서 여러 개의 목적지로 동시에 데이터를 보내야 하는 응용 프로그램에 유용

![](/images/53-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%ED%94%84%EB%A1%9C%ED%86%A0%EC%BD%9C_-ARP-ICMP-IGMP-%EC%97%AD%ED%95%A0/img_6.png)

## 출처

<https://spider-web.tistory.com/12>
