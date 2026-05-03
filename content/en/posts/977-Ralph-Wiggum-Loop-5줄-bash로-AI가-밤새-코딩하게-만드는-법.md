---
title: "Ralph Wiggum Loop: Making AI Code All Night with 5 Lines of Bash"
date: 2026-01-17T17:57:07+09:00
slug: "977-Ralph-Wiggum-Loop-5줄-bash로-AI가-밤새-코딩하게-만드는-법"
original_url: "https://memoryhub.tistory.com/977"
tistory_id: 977
draft: false
---

```
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║     while :; do                                  ║
    ║       cat PROMPT.md | claude-code                ║
    ║     done                                         ║
    ║                                                  ║
    ║         ? → ? → ? → ✅                        ║
    ║                                                  ║
    ║     "I'm in danger!" - Ralph Wiggum             ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
```

If you've used AI coding tools, you've probably had this experience: you give Claude a task, it errors, you instruct again, it errors again, and you instruct once more. What if you could run this iteration automatically all night?

An Australian developer solved this with a 5-line bash script,

and the technique is named after a Simpsons character: 'Ralph Wiggum.'

**The core insight is that an AI that persistently iterates and self-corrects is more powerful than one perfect response.**

**One-line summary:** In short, Ralph Wiggum is a technique that puts AI coding agents in an infinite loop for automatic iteration until task completion, with real cases like completing a $50,000 contract for just $297 in API costs.

## Background

In May 2025, Geoffrey Huntley, an Australian developer who raises goats and contributes to open source, hit a fundamental limitation of AI coding. No matter how smart agentic coding tools like Claude Code are, you still end up having to review results and give new instructions each time. The so-called 'human-in-the-loop' bottleneck.

His solution was surprisingly simple:

```
while :; do cat PROMPT.md | claude-code ; done
```

That's it. Give Claude a task, and when Claude tries to finish, feed the same prompt back in. The files Claude modified stay there, so the next iteration can pick up where the previous one left off.

> Ralph Wiggum Loop is a 'self-referential feedback loop' where AI fails predictably even if it fails, learns from that failure, and improves in the next iteration.

The name is amusing. Just like Ralph Wiggum from The Simpsons, sitting calmly in a burning room saying "I'm in danger!", the AI autonomously modifying the codebase at 2 AM looks exactly like that.

Seeming dumb but persisting is the key.

## How It Works

Ralph Wiggum's philosophy in one sentence:

**"Failing predictably is better than succeeding unpredictably."**

Traditional AI coding workflows focus on writing perfect prompts to get clean code in one shot. Ralph Wiggum flips this completely. Instead of perfection, it pursues iteration; instead of clever prompts, it seeks clear completion conditions.

Anthropic made this technique an official Claude Code plugin in summer 2025.

The plugin uses a Stop Hook feature:

```
/ralph-loop "task description" --completion-promise "DONE" --max-iterations 20
```

The workflow is as follows:

① User defines the task and completion condition

② Claude performs the task

③ Claude tries to exit

④ Stop Hook intercepts the exit, and if the completion condition isn't met, injects the same prompt again

⑤ Claude checks the files it modified and git history from the previous iteration and continues working

⑥ Repeats until completion condition is met or max iterations reached

The key is that each iteration sees the exact results of the previous iteration. Claude doesn't start fresh—it reviews and improves code it created.

## Real Success Stories

That Ralph Wiggum isn't just a prank is proven by actual results.

**$50,000 contract for $297:** According to iMessage screenshots shared by Geoffrey Huntley,

one developer used Ralph to complete an MVP including testing and review at a cost of $297.

The original contract value was $50,000.

**Y Combinator Hackathon results:** One team used Ralph to deploy 6+ repositories in a single overnight session,

with API costs of $297.

**3-month programming language development:** Huntley himself ran Ralph for 3 months straight to create 'Cursed,' a complete programming language. An esoteric language using Gen Z slang as keywords, complete with LLVM compiler and standard library.

'slay' declares functions, 'sus' creates variables, 'based' is true.

**Cursor's browser development:** Cursor co-founder Michael Truell announced that he ran GPT-5.2 uninterrupted for a week to develop 3+ million lines of browser code. Includes a custom rendering engine in Rust, HTML parsing, CSS, layout, and JavaScript VM. That tweet reached 4.5 million views.

## Practical Guide

### 1. Install Plugin

Install the official Ralph Wiggum plugin from Claude Code.

```
claude /install-plugin @anthropics/claude-code-ralph-wiggum
```

After installation, run `/help` to see detailed usage instructions.

### 2. Basic Usage

Start with a simple refactoring task. Make sure to set max-iterations to prevent infinite loops.

```
/ralph-loop "Migrate all Jest tests to Vitest. 
When complete, output <promise>COMPLETE</promise>." 
--max-iterations 30 
--completion-promise "COMPLETE"
```

In each iteration, Claude checks previously modified files and git commit history before continuing.

### 3. Overnight Automation Script

To have multiple projects work overnight, write a batch script.

```
#!/bin/bash
# overnight-work.sh

cd /path/to/project1
claude -p "/ralph-loop 'Implement database schema. 
Output <promise>PHASE1_DONE</promise> when complete' --max-iterations 20"

cd /path/to/project2  
claude -p "/ralph-loop 'Build API endpoints.
Output <promise>PHASE2_DONE</promise> when complete' --max-iterations 25"
```

It's recommended to set cost alerts in your API dashboard before running.

A 50-iteration loop on a large codebase can incur $50-100+ in API costs.

### 4. Effective Prompt Writing

Ralph's success depends not on model performance but on prompt quality. Reference Matt Pocock's recommendations.

**Include clear completion conditions:**

```
Build REST API:
- All CRUD endpoints working
- Input validation implemented
- Tests pass (80%+ coverage)
- API documentation written in README
Output <promise>COMPLETE</promise> when done
```

**Define behavior when stuck:**

```
If incomplete after 15 iterations:
- Document blocking issues
- List attempted approaches
- Suggest alternatives
```

**Focus on single features.** Requesting multiple features at once prevents loop convergence.

## Best Practices/Pattern Comparison

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| Official plugin (/ralph-loop) | Easy installation, Stop Hook built-in, runs in session | Requires permissions setup, instability reported in some environments |
| bash loop (original method) | Complete control, full customization | Manual setup needed, implement safety mechanisms yourself |
| ralph-claude-code (3,300+ stars) | 308 tests, dual exit conditions, rate limiting | Separate installation, learning curve |
| Ralphy (parallel execution) | Multi-AI engine support, git worktree isolation | Early stage, documentation sparse |

## Conclusion

- Ralph Wiggum Loop transforms AI coding paradigm from 'perfect once' to 'persistent iteration'
- The core is self-referential feedback loop via Stop Hook, enabling AI to review and improve its own work
- Real cases exist: completing $50k contracts for $297 or developing programming languages in 3 months

**Practical tip:** Try Ralph today on a simple task (add type annotations, convert callbacks to promises, etc.) with max-iterations set to 10.

## References

- Geoffrey Huntley's Ralph Wiggum Official Page (<https://ghuntley.com/ralph>)
- Claude Code Official Ralph Wiggum Plugin (<https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum>)
- ralph-claude-code by Frank Bria (<https://github.com/frankbria/ralph-claude-code>)
- Matt Pocock's 11 Tips For AI Coding With Ralph Wiggum (<https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum>)
- VentureBeat: How Ralph Wiggum went from 'The Simpsons' to the biggest name in AI (<https://venturebeat.com/technology/how-ralph-wiggum-went-from-the-simpsons-to-the-biggest-name-in-ai-right-now>)
