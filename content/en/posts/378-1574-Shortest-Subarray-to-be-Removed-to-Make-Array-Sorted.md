---
title: "1574. Shortest Subarray to be Removed to Make Array Sorted"
date: 2024-11-15T22:41:52+09:00
slug: "378-1574-Shortest-Subarray-to-be-Removed-to-Make-Array-Sorted"
original_url: "https://memoryhub.tistory.com/378"
tistory_id: 378
draft: false
categories: ["Dev Concepts"]
tags: ["Leetcode"]
---

1. **Clarifying Requirements**:

```
- Remove a subarray from an integer array so remaining elements are in non-decreasing order
- Return the length of the shortest subarray that needs to be removed
- The subarray must be a sequence of consecutive elements
```

1. **Core Solution Design**:

```
- Find non-decreasing sequences expanding from both ends
- Consider cases where left and right portions overlap to calculate minimum length
```

1. **Implementation Details**:

```
public class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        int n = arr.length;
        int left = 0;

        // Find the end of non-decreasing sequence from the left
        while (left + 1 < n && arr[left] <= arr[left + 1]) {
            left++;
        }

        // If already sorted
        if (left == n - 1) {
            return 0;
        }

        // Find the start of non-decreasing sequence from the right
        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) {
            right--;
        }

        // Initialize minimum removal length
        int result = Math.min(n - left - 1, right);

        // Consider combining left and right non-decreasing sequences
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

1. **Key Design Decisions**:

```
- Use Two Pointer approach
- Choose to find non-decreasing sequences from both ends and extend them
- Minimize memory usage by not using additional arrays
```

1. **Verification Results**:

```
Time Complexity: O(n) - traverse the array at most twice
Space Complexity: O(1) - constant space only
Key Test Cases:
- [1,2,3,10,4,2,3,5] => 3
- [5,4,3,2,1] => 4
- [1,2,3] => 0
```

---

### Easy Explanation

**1. Basic Idea:**

```
public class Solution {
    public int findLengthOfShortestSubarray(int[] arr) {
        int n = arr.length;

        // Step 1: Find increasing part from the left
        int left = 0;
        while (left + 1 < n && arr[left] <= arr[left + 1]) {
            left++;
        }

        // If the entire array is already sorted
        if (left == n - 1) {
            return 0;  // No need to remove anything
        }

        // Step 2: Find increasing part from the right
        int right = n - 1;
        while (right > 0 && arr[right - 1] <= arr[right]) {
            right--;
        }

        // Step 3: Find minimum removal length
        int result = Math.min(n - left - 1, right);

        // Step 4: Check if we can connect left and right
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

**2. Explaining the code step-by-step:**

```
// Step 1: Find increasing part from the left
while (left + 1 < n && arr[left] <= arr[left + 1]) {
    left++;
}
```

```
Example: [1,2,3,10,4,2,3,5]
    ↑→→→
    left increases to 3
```

```
// Step 2: Find increasing part from the right
while (right > 0 && arr[right - 1] <= arr[right]) {
    right--;
}
```

```
Example: [1,2,3,10,4,2,3,5]
               ←←←↑
    right starts from 5
```

```
// Step 3: Calculate basic minimum removal length
result = Math.min(n - left - 1, right);
```

```
Choose the smaller of two cases:
1. Keep only left part and remove the rest
2. Keep only right part and remove the rest
```

```
// Step 4: Find better solution
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
Check all cases where we can connect left and right:
- If arr[i] <= arr[j], we can connect them
- Update the removal length whenever we can connect
```

**3. Working Example:**

```
Input: [1,2,3,10,4,2,3,5]

Step 1: left = 3 (up to [1,2,3,10])
Step 2: right = 5 (from [2,3,5])
Step 3: Check multiple cases
Result: 3 (shortest removal length)
```
