---
title: "? 한 줄의 코드가 인터넷을 무너뜨린 날: CrowdStrike 대참사 완벽 분석"
date: 2025-06-17T05:30:08+09:00
slug: "699-한-줄의-코드가-인터넷을-무너뜨린-날-CrowdStrike-대참사-완벽-분석"
original_url: "https://memoryhub.tistory.com/699"
tistory_id: 699
draft: false
categories: ["생활"]
tags: ["트렌드"]
---

```
    ┌────────────────────────────────────────┐
    │                                        │
    │    ? WORLD                           │
    │         ╱╲                            │
    │        ╱?╲  <-- CrowdStrike Update   │
    │       ╱────╲                          │
    │      ╱???╲                        │
    │     ╱????╲ <-- 8.5M Systems      │
    │    ────────────                        │
    │    Blue Screen of Death                │
    │                                        │
    └────────────────────────────────────────┘
```

"2024년 7월 19일 오후 1시 9분, 제 노트북이 갑자기 블루스크린이 떴습니다. 재부팅해도 계속 같은 화면... 알고 보니 전 세계가 마비된 거였죠."

850만 대의 Windows 시스템이 동시에 다운되고, 항공기가 지연되고, 병원이 마비되고, 은행 업무가 중단된 그날. **단 한 줄의 잘못된 코드**가 어떻게 역사상 최악의 IT 재난을 일으켰을까요?

⚡ **TL;DR**

- CrowdStrike의 보안 소프트웨어 업데이트에서 발생한 메모리 오류가 전 세계 시스템을 마비시킴
- 초기엔 Null Pointer Dereference로 추정했으나, 실제로는 Array Out-of-Bounds Read가 원인

## 목차

1. 배경 - 그날 무슨 일이 일어났나?
2. 핵심 개념 정리 - Null Pointer와 Array Out-of-Bounds
3. 실습 - 위험한 코드 패턴 이해하기
4. 모범 사례·베스트 프랙티스
5. 마치며 & 참고자료

---

## 1. 배경 - 그날 무슨 일이 일어났나?

2024년 7월 19일 04:09 UTC(한국시간 13:09)에 지속적인 운영 일환으로 CrowdStrike는 Windows 시스템에 대한 센서 구성 업데이트를 제공했습니다. 이 업데이트는 평범한 보안 패치처럼 보였지만, 치명적인 버그를 품고 있었습니다.

### ? 피해 규모

| 영향 범위 | 피해 내용 |
| --- | --- |
| **850만 대** | 영향받은 Windows 시스템 |
| **전 세계** | 항공, 금융, 의료, 제조업 등 |
| **78분** | 문제 업데이트 배포 시간 |
| **수십억 달러** | 추정 피해액 |

### ? 용어 정리

✅ **CrowdStrike Falcon**: 엔드포인트 보안 솔루션 (EDR)  
✅ **커널 드라이버**: Windows 핵심 시스템에서 작동하는 프로그램  
✅ **BSOD**: Blue Screen of Death (블루스크린)

## 2. 핵심 개념 - 처음엔 Null Pointer, 실제론 Array 문제

> **초기 추정: Null Pointer Dereference**  
> A null pointer does neither point to an object nor to valid memory, and as a consequence dereferencing or accessing the memory pointed by such a pointer is undefined behavior

### Null Pointer Dereference란?

```
// 초기에 의심받았던 패턴
void* get_data() {
    if (data_available) {
        return data_ptr;  // 이게 NULL일 수 있음!
    } else {
        return NULL;      // NULL 반환
    }
}

int process_data(void* data) {
    // NULL 체크 없이 사용하면... ?
    return *data;  // 시스템 크래시!
}
```

### 실제 원인: Array Out-of-Bounds Read

Update 07AUG2024: CrowdStrike released a technical root cause analysis that confirms that an array out-of-bounds read, very similar to our example, caused the issue.

```
// 실제로 일어난 문제 (추정)
int process_array(int* arr, int size) {
    // 배열 크기를 초과한 인덱스 접근
    for (int i = 0; i <= size; i++) {  // <= 주의! 
        // i == size일 때 범위 초과
        int value = arr[i];  // ? 메모리 접근 오류
    }
}
```

## 3. 실습 - 위험한 코드 패턴 직접 이해하기

### ① 문제 코드 패턴 분석

```
// 위험한 패턴 1: NULL 포인터
struct DataStruct {
    int value;
    char name[32];
};

void dangerous_null_pattern() {
    DataStruct* ptr = nullptr;

    // 잘못된 접근 - 0x9c(156) 바이트 오프셋
    // CrowdStrike 사건에서 발견된 패턴
    int bad_access = ptr->value;  // 크래시!
}
```

### ② 배열 범위 초과 패턴

```
// 위험한 패턴 2: 배열 범위 초과
#define MAX_RULES 256

void dangerous_array_pattern(int rule_index) {
    int security_rules[MAX_RULES];

    // 인덱스 검증 없이 접근
    if (security_rules[rule_index] > 0) {  // rule_index >= 256이면?
        // 메모리 오염 또는 크래시
    }
}
```

### ③ 커널 모드에서의 영향

```
// 커널 드라이버에서 이런 오류가 발생하면...
void kernel_driver_function() {
    // 일반 프로그램: 해당 프로그램만 종료
    // 커널 드라이버: 전체 시스템 크래시 (BSOD)

    // CrowdStrike Falcon은 부팅 시 필수 드라이버
    // = Windows가 아예 시작 불가능
}
```

## 4. 모범 사례·베스트 프랙티스

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| **현대적 C++ 사용** | std::optional로 NULL 방지 | 레거시 코드 호환성 |
| **정적 분석 도구** | 컴파일 시점 오류 검출 | 도구 설정 필요 |
| **단계적 배포** | 문제 조기 발견 | 배포 시간 증가 |
| **메모리 안전 언어** | Rust 등으로 근본 해결 | 학습 곡선 존재 |

### 안전한 코드 작성법

```
// ✅ 개선된 코드 - 현대적 C++
#include <optional>
#include <array>

std::optional<DataStruct> get_safe_data() {
    if (!data_available) {
        return std::nullopt;  // 명시적 빈 값
    }
    return DataStruct{...};
}

// ✅ 배열 안전성
template<size_t N>
void safe_array_access(std::array<int, N>& arr, size_t index) {
    if (index >= arr.size()) {
        // 오류 처리
        return;
    }
    // 안전한 접근
    int value = arr[index];
}
```

### 배포 전략 개선

```
# 단계적 롤아웃 전략
deployment:
  canary:
    - 0.1%   # 1시간 모니터링
    - 1%     # 6시간 모니터링  
    - 10%    # 24시간 모니터링
    - 50%    # 48시간 모니터링
    - 100%   # 전체 배포
```

## 5. 마치며

이번 CrowdStrike 사건은 세 가지 중요한 교훈을 남겼습니다:

1. **커널 수준 코드의 위험성** - 한 줄의 실수가 전체 시스템을 마비시킬 수 있음
2. **테스트의 중요성** - CrowdStrike admitted in its root cause analysis that a lack of proper testing was part of the cause of the outage.
3. **점진적 배포의 필요성** - 78분 동안 잘못된 업데이트가 전 세계로 퍼짐

실제 프로젝트에서는 **"빠른 배포보다 안전한 배포"**가 우선이어야 합니다. 특히 시스템 핵심 부분을 다룰 때는 더욱 그렇습니다.

**Y2K는 실패했지만, CrowdStrike는 성공했다**는 농담이 있을 정도로 큰 사건이었습니다. 우리 모두 이 사건을 교훈 삼아 더 안전한 코드를 작성합시다!

---

### 참고자료

- [CrowdStrike 공식 기술 분석](https://www.crowdstrike.com/technical-details-on-todays-outage-kr/)
- [Sonar: What Code Issues Caused the CrowdStrike Outage?](https://www.sonarsource.com/blog/what-code-issues-caused-the-crowdstrike-outage/)
- [Wikipedia: 2024 CrowdStrike IT outages](https://en.wikipedia.org/wiki/2024_CrowdStrike-related_IT_outages)
