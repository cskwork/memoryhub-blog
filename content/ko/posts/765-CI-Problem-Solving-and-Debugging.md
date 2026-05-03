---
title: "CI - Problem Solving and Debugging"
date: 2025-08-26T22:55:26+09:00
slug: "765-CI-Problem-Solving-and-Debugging"
original_url: "https://memoryhub.tistory.com/765"
tistory_id: 765
draft: false
---

## Top 10 Laws of Problem-Solving

|  |  |  |
| --- | --- | --- |
| **1. Define First Law** | Clearly understand the problem before attempting solutions | Spend 50% of time defining the problem accurately |
| **2. Root Cause Law** | Address causes, not symptoms | Ask "why" 5 times to reach the true source |
| **3. Simple Solutions Law** | The simplest solution is often the best  (Occam's Razor) | Choose the path with fewest assumptions |
| **4. Break Down Law** | Divide complex problems into smaller,  manageable parts | Tackle one piece at a time systematically |
| **5. Multiple Perspectives Law** | View problems from different angles and  stakeholders | Involve diverse viewpoints before deciding |
| **6. Data Before Opinions Law** | Base decisions on facts, not assumptions | Gather evidence before forming conclusions |
| **7. Test and Learn Law** | Try small experiments before large commitments | Prototype, test, iterate, then scale |
| **8. Time Boxing Law** | Set deadlines to prevent analysis paralysis | Limit research/planning time, then act |
| **9. Alternative Options Law** | Always have Plan B (and C) | Generate multiple solutions before choosing |
| **10. Learning Loop Law** | Document what worked and what didn't | Turn every problem into future wisdom |

- **Creative Problem-Solving**: Use brainstorming, mind mapping, or lateral thinking techniques
- **Systematic Methods**: Apply frameworks like PDCA cycle, Six Sigma, or design thinking

**The master problem-solver follows one golden rule: Think twice, act once, but never stop learning.**

---

## Top 10 Laws of Debugging Programming Environments

|  |  |  |
| --- | --- | --- |
| **1. Reproduce First Law** | If you can't reproduce it, you can't fix it | Create minimal reproducible examples with exact  steps |
| **2. Read the Error Law** | Error messages contain 80% of the  solution | Parse stack traces, error codes, and log messages  carefully |
| **3. Binary Search Law** | Isolate the problem by eliminating half  the code | Comment out sections, use git bisect, narrow scope  systematically |
| **4. Assumption Killer Law** | Your assumptions are usually wrong | Verify variables, check data types, validate input/ output |
| **5. Tooling First Law** | Use debuggers before print  statements | Step through with IDE debuggers, use breakpoints  strategically |
| **6. Minimal Case Law** | Reduce to the smallest failing example | Strip away complexity until only the bug remains |
| **7. Environment Isolation Law** | "It works on my machine" is not a  solution | Test across different OS, browsers, versions,  configurations |
| **8. State Inspection Law** | Check the state at every critical point | Log variables, inspect memory, monitor database  state |
| **9. Version Control Safety Law** | Always have a way back to working  code | Commit working states, use feature branches, tag releases |
| **10. Rubber Duck Law** | Explain the problem out loud to find the  solution | Walk through code line-by-line with  team/documentation |

- **Systematic Debugging**: Use formal debugging methodologies like scientific method approach
- **Collaborative Debugging**: Pair programming, code reviews, and team troubleshooting sessions

**Every expert debugger lives by this truth: The bug is always exactly where you didn't look, until you look there systematically.**
