---
title: "IntelliJ Community Edition에서 application.yml 인식 문제 해결"
date: 2025-03-25T18:10:32+09:00
slug: "525-IntelliJ-Community-Edition에서-application-yml-인식-문제-해결"
original_url: "https://memoryhub.tistory.com/525"
tistory_id: 525
draft: false
categories: ["데브 컨셉"]
tags: ["Tech News"]
cover:
  image: "이미지 예시"
  alt: "Run Configuration 메뉴"
  relative: false
  hidden: false
---

## 문제

IntelliJ Community Edition에서 Gradle bootRun 실행 시 application.yml 파일을 읽지 못하는 문제

## 해결 방법

### 1. 환경 변수 설정하기

1. 메인 클래스를 선택하고 오른쪽 클릭
2. **Edit Configurations...** 선택

![Run Configuration 메뉴](%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%98%88%EC%8B%9C)

### 2. 환경 변수 추가

1. **Run/Debug Configurations** 창에서 **Environment variables** 필드 찾기
2. 다음 값 입력: `SPRING_PROFILES_ACTIVE=dev`
3. **Apply** 및 **OK** 클릭

![환경 변수 설정](%EC%9D%B4%EB%AF%B8%EC%A7%80%20%EC%98%88%EC%8B%9C)

### 3. 애플리케이션 실행

1. 일반적인 방법으로 애플리케이션 실행 (Run 또는 Debug)
2. 로그를 확인하여 application.yml이 올바르게 로드되는지 확인

## 대체 방법 (필요시)

**VM 옵션으로 설정:**

1. **Edit Configurations** → **VM options** 필드에 입력:  
   `-Dspring.profiles.active=dev`

**프로그램 인수로 설정:**

1. **Edit Configurations** → **Program arguments** 필드에 입력:  
   `--spring.profiles.active=dev`

---

※ 참고: 이 설정은 새로운 실행 구성에서 매번 설정해야 합니다.
