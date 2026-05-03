---
title: "컴퓨터-CPU(프로세서)-작업-프로세스"
date: 2024-05-25T14:53:35+09:00
slug: "68-컴퓨터-CPU-프로세서-작업-프로세스"
original_url: "https://memoryhub.tistory.com/68"
tistory_id: 68
draft: false
categories: ["데브 컨셉"]
tags: ["정보처리기사"]
cover:
  image: "images/68-%EC%BB%B4%ED%93%A8%ED%84%B0-CPU-%ED%94%84%EB%A1%9C%EC%84%B8%EC%84%9C-%EC%9E%91%EC%97%85-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4/img.png"
  relative: false
  hidden: false
---

## 컴퓨터-CPU(프로세서)-작업-프로세스

프로세서(처리기,CPU)에서 처리하는 프로그램.  
작업 또는 타스크라고도 한다.

### 프로세스 상태 전이

프로세스가 시스템 내에 있는 동안 상태가 변하는 것.

### PCB(Process Control Block)

- HAS address, state, time, id

![](/images/68-%EC%BB%B4%ED%93%A8%ED%84%B0-CPU-%ED%94%84%EB%A1%9C%EC%84%B8%EC%84%9C-%EC%9E%91%EC%97%85-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4/img.png)

### 프로세스 상태 전이

![](/images/68-%EC%BB%B4%ED%93%A8%ED%84%B0-CPU-%ED%94%84%EB%A1%9C%EC%84%B8%EC%84%9C-%EC%9E%91%EC%97%85-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4/img_1.png)

- 제출 : 작업이 시스템에 제출된 상태
- 접수 : 제출된 작업이 디스크에 저장된 상태
- 준비 : 프로세스가 프로세서를 할당받기 전에 대기중인 상태. 잡스케줄러가 접수에서 준비 상태로 전이함.
- 실행 : 프로세스가 프로세서를 할당받아 실행되는 상태.
- 대기 : 프로세스에 입 출력이 필요하면 현재 실행 중인 프로세스가 중단되고, 입 출력이 끝날 때까지 대기하고 있는다.
- 종료 : 프로세스의 실행이 끝나고 프로세스 할당이 해제된 상태.

#### Windows

- 작업 관리자로 관리하고, 우선순위 지정 가능

#### Linux

- ps 명령어로 확인하고 proc 디렉터리(RAM에 저장된 데이터를 확인할 수 있는 가상 디렉터리)에 PID에 해당하는 디렉터리로 이동해서 확인할 수 있다.
- top 명령어로 현재 시스템 CPU, RAM 사용률 모니터링 가능.
- kill 명령어로 프로세스 종료 가능.

### 참고

- 2020 시나공 정보처리기사 실기 기본서
