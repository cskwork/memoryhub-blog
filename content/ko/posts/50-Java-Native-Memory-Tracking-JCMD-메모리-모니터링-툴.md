---
title: "Java Native Memory Tracking(JCMD) 메모리 모니터링 툴"
date: 2024-05-25T14:01:34+09:00
slug: "50-Java-Native-Memory-Tracking-JCMD-메모리-모니터링-툴"
original_url: "https://memoryhub.tistory.com/50"
tistory_id: 50
draft: false
categories: ["데브 언어"]
tags: ["Java"]
---

오늘은 **JCMD** 툴을 활용하여 JVM 환경을 보다 효율적으로 모니터링하는 방법을 알아보겠습니다. JCMD는 Oracle Java 7 버전부터 제공되는 강력한 명령줄 도구로, JVM 애플리케이션의 프로세스 정보, 힙 덤프, 스레드 덤프, VM 시스템 정보, GC 통계 등을 손쉽게 확인하고 관리할 수 있습니다.

## **1. JCMD란? ?**

JCMD는 한마디로 **“JVM 모니터링을 위한 스위스 군용 칼”** 같은 도구입니다. Java 프로세스를 식별하고, 힙 덤프를 생성하거나 스레드 상태를 확인하는 등 다양한 분석 정보를 얻을 수 있습니다.

- **개념 요약**:
  - JVM 프로세스 ID, 힙 덤프, 스레드 덤프, VM 시스템 정보, GC 통계 등을 커맨드라인에서 간편하게 확인
  - Oracle Java 7 버전부터 사용 가능
  - Java 애플리케이션 성능 튜닝과 문제 해결에 유용
- **실생활 예시**:
  - 운영 중인 Tomcat 서버에서 갑자기 메모리가 부족해지거나 CPU 사용률이 치솟는 문제가 발생했을 때, 바로 jcmd 명령어를 통해 어느 프로세스에서 문제가 있는지 식별하고, 힙이나 스레드 관련 정보를 즉시 덤프 받아 원인을 분석할 수 있습니다.
- **어떤 문제를 해결하는가?**
  - 프로세스 식별부터 메모리 누수, 스레드 교착 상태(Deadlock), GC 비정상 동작 등 JVM과 관련된 다양한 성능 문제를 빠르게 파악할 수 있게 해줍니다.

## **2. 어떻게 동작하나요? ?**

### 1) 기본 개념

JCMD가 하는 일은 크게 다음과 같이 요약됩니다:

- **프로세스 식별**: 현재 실행 중인 Java 프로세스 목록 확인
- **명령어 실행**: 특정 프로세스에 대해 VM.native\_memory, GC.heap\_dump, Thread.print 등의 다양한 명령어를 실행
- **분석 결과 제공**: 명령어 결과를 실시간으로 확인하여 문제 진단 및 모니터링 수행

```
# Java 프로세스 식별
$ jcmd
1234 org.apache.catalina.startup.Bootstrap
5678 com.example.MyApplication

# Java 프로세스 목록 자세히 확인
$ jcmd -l
1234 org.apache.catalina.startup.Bootstrap /usr/local/tomcat/...
5678 com.example.MyApplication /usr/local/app/...
```

### 2) 실제 적용 예시

#### 예: Tomcat 서버 모니터링

1. **Tomcat 서버 구동**
   - Tomcat이 정상적으로 실행 중이라고 가정합니다. (예: PID=1234)
2. **프로세스 정보 확인**

   ```
   $ jcmd -l
   1234 org.apache.catalina.startup.Bootstrap /usr/local/tomcat/bin/bootstrap.jar
   ```
3. **스레드 덤프 등 필요한 정보 확인**

   ```
   $ jcmd 1234 Thread.print
   # 스레드 스택 트레이스 출력
   ```
4. **GC 힙 덤프 생성**

   ```
   $ jcmd 1234 GC.heap_dump /path/to/dump.hprof
   # JVM 힙 덤프 파일 생성
   ```

### ? 동작 원리

1. **명령어 발행 단계**: jcmd <pid> <command> 형태로 JVM 프로세스에 특정 명령을 전달합니다.
2. **JVM 내부 처리**: 해당 프로세스의 JVM이 명령을 해석하여 필요에 따라 힙이나 스레드 덤프, GC 통계를 수집합니다.
3. **결과 반환**: 수집된 정보를 콘솔에 출력하거나 파일 형태(예: 힙 덤프)로 저장합니다.

## **3. 주요 장점 ?**

1. **광범위한 기능 제공**: 프로세스 식별, 스레드 덤프, 힙 덤프, GC 정보, 네이티브 메모리 추적 등 다양한 명령을 한 도구에서 제공합니다.
2. **간편한 명령어 사용**: 명령 형식이 직관적이어서, JVM 관련 문제를 빠르게 진단하고 모니터링할 수 있습니다.
3. **Native Memory Tracking(NMT) 지원**: 네이티브 메모리 영역까지 추적할 수 있어, 메모리 누수 등 복잡한 문제도 파악이 가능합니다.

## **4. 주의할 점 ⚠️**

1. **프로덕션 환경 영향**: 스레드 덤프나 힙 덤프 등은 순간적으로 애플리케이션 성능에 영향을 줄 수 있으므로, 트래픽이 적은 시간대나 사전 공지를 한 후 사용하는 것이 좋습니다.
2. **보안 이슈**: 내부 구조나 메모리 정보를 상세히 볼 수 있기 때문에, 접근 권한 관리가 중요합니다.
3. **파일 경로 및 권한**: 힙 덤프를 파일로 내보낼 경우 해당 디렉터리에 JVM 프로세스가 접근할 권한이 있는지 확인해야 합니다.

## **5. Native Memory Tracking(NMT) 사용 예시 ?**

네이티브 메모리 트래킹(NMT)은 **JVM 내부에서 사용되는 네이티브 메모리를 추적**하여, Java Heap 외 영역에서 발생할 수 있는 메모리 누수를 진단하는 데에 도움을 줍니다.

### 1) 설정 방법

1. **JVM 옵션 추가**
   - -XX:NativeMemoryTracking=summary 또는 -XX:NativeMemoryTracking=detail 옵션으로 활성화
2. **Tomcat 예시**
   - CATALINA\_OPTS 혹은 JAVA\_OPTS에 아래와 같이 추가

   ```
   # Linux (setenv.sh)
   export CATALINA_OPTS="$CATALINA_OPTS -XX:NativeMemoryTracking=summary"
   ```

   - Windows(setenv.bat)에서는 아래와 비슷하게 설정

   ```
   set CATALINA_OPTS=%CATALINA_OPTS% -XX:NativeMemoryTracking=summary
   ```
3. **서버 재시작**
   - 설정 파일 수정 후 Tomcat 서버를 재시작해야 적용됩니다.

### 2) 베이스라인 설정 및 모니터링

#### (1) 초기 베이스라인 설정

개발/운영 환경에서 **초기 메모리 상태**를 측정해두면, 이후 변화가 발생했을 때 비교 분석이 수월합니다.

```
# Tomcat 프로세스 PID가 1234라고 가정
$ jcmd 1234 VM.native_memory baseline
```

#### (2) 메모리 변화 모니터링

시간이 지난 후 같은 프로세스에 대해 다음 명령을 실행하면, 베이스라인 대비 어떤 부분에서 메모리가 증가/감소했는지 확인할 수 있습니다.

```
$ jcmd 1234 VM.native_memory detail.diff
```

- **“+” 기호**는 메모리가 증가했음을 의미
- **“-” 기호**는 메모리가 감소했음을 의미

### 3) NMT 보고서 주요 항목

1. **전체 메모리(Reserved/Committed)**:
   - JVM이 운영체제로부터 예약(Reserved)하고 실제로 사용 중(Committed)인 메모리 양
2. **Java Heap**:
   - Java 객체들이 저장되는 힙 영역
3. **클래스(Class)**:
   - 클래스 로딩 및 메타데이터가 차지하는 메모리
4. **스레드(Thread)**:
   - 각 스레드별 네이티브 스택, 구조체 등이 사용하는 메모리
5. **코드(Code)**:
   - JIT 컴파일 등으로 생성된 기계어 코드가 차지하는 메모리

아래는 detail.diff 보고서 예시를 단순화한 예입니다:

```
Native Memory Tracking:

Total: reserved=1234KB, committed=567KB
                ...
Class: reserved=200KB (+20KB), committed=150KB (+10KB)
Thread: reserved=300KB (-10KB), committed=250KB (+5KB)
Code: reserved=180KB (+30KB), committed=120KB (+15KB)
```

- Class 항목에서 +20KB / +10KB 증가가 확인되며, 이는 클래스 로딩에 의한 메모리 증가 가능성을 시사합니다.
- Thread는 reserved 메모리는 줄었지만 committed는 소폭 증가함을 확인할 수 있습니다.

## **6. 마치며 ?**

JCMD는 JVM 프로세스의 상태를 진단하고 모니터링하기 위한 **매우 유용한 도구**입니다. 특히 **Native Memory Tracking(NMT)** 기능을 통해 Java Heap 영역이 아닌 네이티브 메모리 영역의 누수까지 추적할 수 있어, 복합적인 메모리 문제 해결에 큰 도움이 됩니다. 운영 환경에서 애플리케이션 성능 문제가 발생했을 때, JCMD와 NMT 보고서를 적극 활용해보세요! 이를 통해 **프로세스 메모리 사용량과 GC 현황을 빠르게 파악**하고, **메모리 누수, 스레드 이슈** 등을 손쉽게 해결할 수 있을 것입니다.

---

### **참고 자료 및 출처**

- [Oracle 공식 문서 - Java Native Memory Tracking](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/nmt-summary.html)
- [Oracle 공식 문서 - JCMD 사용 가이드](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jcmd.html)

위 자료들을 참고하시면 **JCMD와 NMT를 더욱 깊이 있게 학습**하고, 실제 운영 환경에서 효과적인 모니터링 및 문제 해결을 수행하실 수 있습니다.
