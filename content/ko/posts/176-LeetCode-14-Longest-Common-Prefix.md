---
title: "LeetCode - 14. Longest Common Prefix"
date: 2024-06-02T14:37:53+09:00
slug: "176-LeetCode-14-Longest-Common-Prefix"
original_url: "https://memoryhub.tistory.com/176"
tistory_id: 176
draft: false
---

*To solve the problem of finding the longest common prefix string amongst an array of strings, we'll use a method that iterates over the characters of the strings, checking for the common prefix.*

### The Big Picture

Imagine you have a group of people and you want to find the longest sequence of actions they all perform in the same order. This is like finding the longest common prefix in a group of strings: you look at each action (or character) one by one until you find a difference.

### Core Concepts

1. **Prefix:** A prefix of a string is a substring that starts at the beginning and includes some or all characters up to a certain point.
2. **Iterating Over Characters:** We'll compare characters at the same position across all strings.
3. **Early Termination:** If at any point the characters don't match, we stop and return the prefix found so far.

### Detailed Walkthrough

1. **Check for Edge Cases:** If the input list is empty, return an empty string immediately.
2. **Find the Shortest String:** The longest possible common prefix can't be longer than the shortest string in the list.
3. **Compare Characters:** Iterate character by character across all strings, stopping when characters don't match.

Here is the Python function to solve this problem:

```
def longestCommonPrefix(strs):
    if not strs:
        return ""

    # Find the shortest string in the list
    shortest_str = min(strs, key=len)

    for i in range(len(shortest_str)):
        # Get the current character from the shortest string
        current_char = shortest_str[i]

        # Compare this character with the same position character in all strings
        for string in strs:
            if string[i] != current_char:
                return shortest_str[:i]

    return shortest_str

# Example Usage:
strs1 = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(longestCommonPrefix(strs2))  # Output: ""
```

### Understanding Through an Example

For `strs = ["flower", "flow", "flight"]`:

1. Find the shortest string, which is `"flow"`.
2. Compare characters of `"flow"` with `"flower"` and `"flight"`:
   - At index 0: All strings have 'f'.
   - At index 1: All strings have 'l'.
   - At index 2: All strings have 'o'.
   - At index 3: `"flow"` has 'w', `"flower"` has 'w', but `"flight"` has 'i'. We stop here and return `"fl"`.

For `strs = ["dog", "racecar", "car"]`:

1. The shortest string is `"dog"`.
2. Compare characters of `"dog"` with `"racecar"` and `"car"`:
   - At index 0: `"dog"` has 'd', `"racecar"` has 'r', and `"car"` has 'c'. No match at the first character, so we return an empty string.

### Conclusion and Summary

We compared characters of each string at the same position until we found a mismatch. The process stops at the first mismatch, and we return the prefix found so far. This approach ensures efficient comparison and early termination when necessary.

### Test Your Understanding

1. What will be the output of the function for the input `["interview", "internet", "internal"]`?
2. How does the function handle an empty list?
3. Why is finding the shortest string important in this solution?

### Reference

- [LeetCode: Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)
