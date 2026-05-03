---
title: "Impressions After Using Claude Code"
date: 2025-06-15T01:04:12+09:00
slug: "686-Claude-Code-사용-후기"
original_url: "https://memoryhub.tistory.com/686"
tistory_id: 686
draft: false
---

1. **Understand the Nature of the Tool**
   - Claude is a generator that concatenates text probabilistically.
   - Results vary slightly each time, even with the same prompt.

2. **Difference from Formal Software Synthesis**
   - Synthesis tools produce bug-free code if specifications are met, but Claude's predictions based on training data can contain bugs.

3. **Test-Driven Development (TDD) is Essential**
   - First define desired behavior as unit tests, then have Claude generate and refine code to pass those tests.

4. **Prompt = Specification**
   - Vague instructions like "make a cool program" lead to hallucinations.
   - You must clearly specify functionality, constraints, and performance requirements.

5. **Break Down Tasks and Attempt Multiple Times**
   - Rather than one large task, split it into subtasks (writing tests, implementing specific functions) and request separately.
   - Regenerate as many times as needed and adopt the best result.

6. **Use Claude as 'Support Staff'**
   - Useful for auxiliary work like comparing algorithm candidates, code review, and documentation.
   - Accuracy increases as you provide more specific criteria and examples.

7. **Verify Results Directly**
   - Even if Claude says "tests passed," you must actually run the code to verify.

> **Summary:** Claude Code is powerful but an unreliable text generator. Safe and clean code can only be obtained with clear specifications, rigorous testing, and continuous human validation.
