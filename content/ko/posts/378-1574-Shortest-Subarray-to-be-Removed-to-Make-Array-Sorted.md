---
title: "1574. Shortest Subarray to be Removed to Make Array Sorted"
date: 2024-11-15T22:41:52+09:00
slug: "378-1574-Shortest-Subarray-to-be-Removed-to-Make-Array-Sorted"
original_url: "https://memoryhub.tistory.com/378"
tistory_id: 378
draft: false
categories: ["데브 컨셉"]
tags: ["Leetcode"]
---

1. **요구사항 명확화**:

```
- 정수 배열에서 부분 배열을 제거하여 남은 요소들이 비감소 순서가 되도록 해야 함
- 제거해야 할 가장 짧은 부분 배열의 길이를 반환
- 부분 배열은 연속된 요소들의 시퀀스여야 함
```

1. **핵심 솔루션 설계**:

```
- 양쪽 끝에서부터 비감소 수열을 찾아 확장
- 왼쪽과 오른쪽 부분이 겹치는 경우를 고려하여 최소 길이 계산
```

1. **구현 상세**:

```
public class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        int n = arr.length;
        int left = 0;

        // 왼쪽에서 비감소 수열의 끝 찾기
        while (left + 1 < n && arr[left] <= arr[left + 1]) {
            left++;
        }

        // 이미 정렬되어 있는 경우
        if (left == n - 1) {
            return 0;
        }

        // 오른쪽에서 비감소 수열의 시작 찾기
        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) {
            right--;
        }

        // 최소 제거 길이 초기화
        int result = Math.min(n - left - 1, right);

        // 양쪽 비감소 수열을 합치는 경우 고려
        int i = 0;
        int j = right;
        while (i <= left && j < n) {
            if (arr[i] <= arr[j]) {
                result = Math.min(result, j - i - 1);
                i++;
            } else {
                j++;
            }
        }

        return result;
    }
}
```

1. **주요 설계 결정**:

```
- Two Pointer 접근 방식 사용
- 양쪽에서 비감소 수열을 찾아 확장하는 방식 선택
- 메모리 사용을 최소화하기 위해 추가 배열 사용하지 않음
```

1. **검증 결과**:

```
시간 복잡도: O(n) - 배열을 최대 두 번 순회
공간 복잡도: O(1) - 상수 공간만 사용
주요 테스트 케이스:
- [1,2,3,10,4,2,3,5] => 3
- [5,4,3,2,1] => 4
- [1,2,3] => 0
```

---

### 쉬운 설명

**1. 기본 아이디어:**

```
public class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        int n = arr.length;

        // 1단계: 왼쪽에서 증가하는 부분 찾기
        int left = 0;
        while (left + 1 < n && arr[left] <= arr[left + 1]) {
            left++;
        }

        // 만약 전체가 이미 정렬되어 있다면
        if (left == n - 1) {
            return 0;  // 제거할 필요 없음
        }

        // 2단계: 오른쪽에서 증가하는 부분 찾기
        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) {
            right--;
        }

        // 3단계: 최소 제거 길이 찾기
        int result = Math.min(n - left - 1, right);

        // 4단계: 왼쪽과 오른쪽을 연결할 수 있는지 확인
        int i = 0;
        int j = right;
        while (i <= left && j < n) {
            if (arr[i] <= arr[j]) {
                result = Math.min(result, j - i - 1);
                i++;
            } else {
                j++;
            }
        }

        return result;
    }
}
```

**2. 코드를 단계별로 설명:**

```
// 1단계: 왼쪽에서 증가하는 부분 찾기
while (left + 1 < n && arr[left] <= arr[left + 1]) {
    left++;
}
```

```
예: [1,2,3,10,4,2,3,5]
    ↑→→→
    left는 3까지 증가
```

```
// 2단계: 오른쪽에서 증가하는 부분 찾기
while (right > 0 && arr[right - 1] <= arr[right]) {
    right--;
}
```

```
예: [1,2,3,10,4,2,3,5]
               ←←←↑
    right는 2부터 시작
```

```
// 3단계: 기본적인 최소 제거 길이 계산
result = Math.min(n - left - 1, right);
```

```
두 가지 경우 중 작은 것 선택:
1. 왼쪽 부분만 남기고 나머지 제거
2. 오른쪽 부분만 남기고 나머지 제거
```

```
// 4단계: 더 나은 방법 찾기
while (i <= left && j < n) {
    if (arr[i] <= arr[j]) {
        result = Math.min(result, j - i - 1);
        i++;
    } else {
        j++;
    }
}
```

```
왼쪽과 오른쪽을 연결할 수 있는 모든 경우를 확인:
- arr[i]가 arr[j]보다 작거나 같으면 연결 가능
- 연결 가능할 때마다 제거해야 할 길이 업데이트
```

**3. 작동 예시:**

```
입력: [1,2,3,10,4,2,3,5]

1단계: left = 3 ([1,2,3,10]까지)
2단계: right = 5 ([2,3,5]부터)
3단계: 여러 경우 확인
결과: 3 (가장 짧게 제거 가능한 길이)
```
