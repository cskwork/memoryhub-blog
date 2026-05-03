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
