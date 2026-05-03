---
title: "pi-autoresearch: AI Tunes Your Code Overnight Automatically?"
date: 2026-04-17T01:38:25+09:00
slug: "1053-pi-autoresearch-AI가-밤새-내-코드를-스스로-튜닝한다고요"
original_url: "https://memoryhub.tistory.com/1053"
tistory_id: 1053
draft: false
---

```
┌──────────────────────────────┐
│     [ 1. Idea Generation ]   │
│              ↓               │
│    [ 2. Code Change·Commit ]  │
│              ↓               │
│    [ 3. Run Benchmark ]       │
│              ↓               │
│    Improvement?  Yes  ->  keep     │
│           No   ->  revert    │
│              ↺               │
│      Repeat & Accumulate     │
└──────────────────────────────┘
         pi-autoresearch
```

## Introduction — Manual Benchmarking, Stop

Ever meticulously measured how much bundle size shrank every time you changed one line of code? Developers have all experienced the grueling cycle of "measure → modify → remeasure" dozens of times hoping for even a 1-second test speedup. pi-autoresearch is an open-source extension that lets an AI agent run this repetitive loop for you. After reading this article, you'll understand both how automatic optimization loops work for "any metric" and how to install and run it yourself.

## TL;DR

> pi-autoresearch is an MIT-licensed open-source extension that attaches an autonomous experiment loop of "try → measure → adopt or discard → repeat" to the pi AI coding agent, automatically optimizing any metric overnight without being fooled by noise.

## Why This Tool Is Getting Attention

The autoresearch pattern released by Karpathy was originally an ML-only technique for tuning LLM training loops.

pi-autoresearch generalized this idea to "all measurable software metrics," greatly expanding its applicability.

Actually, Shopify CEO Tobi Lutke directly announced "open-sourcing the autoresearch plugin for pi," drawing attention,

and it currently exceeds 4.7k stars.

| Term | Explanation |
| --- | --- |
| pi | Terminal-based AI coding agent (extension host) |
| autoresearch loop | try-measure-keep-discard-repeat autonomous optimization cycle |
| MAD | Median Absolute Deviation, confidence metric based on measurement noise |
| metric | Optimization target (test speed, bundle size, Lighthouse score, etc.) |

## Core Architecture

> pi-autoresearch is a pi extension that automatically experiments and validates whether your specified metric actually improves,  
> and even organizes results into reviewable independent branches.
>
> It runs loops using three tools: init_experiment, run_experiment, log_experiment,  
> filters noise with MAD confidence scores,  
> and autoresearch-finalize cuts verified changes into clean branches.

The files the extension provides are simple. A benchmark itself needs just one shell script line.

```
# autoresearch.sh (Bash 5.x example — output test time as metric)
pnpm test 2>&1 | tail -n 1 \
  | awk '{print "METRIC name=test_time value="$NF}'
```

The agent parses the `METRIC name=... value=...` output line from this script and append-only records it in `autoresearch.jsonl`. A major advantage is that even if interrupted, the next session can read the same jsonl and continue.

## Hands-On Practice

### ① Installation

One line in terminal:

```
pi install https://github.com/davebcn87/pi-autoresearch
```

For manual installation, copy the `extensions/` and `skills/` directories from the repository to `~/.pi/agent/extensions/` and `~/.pi/agent/skills/` respectively, then run `/reload` in a pi session.

### ② Session Initialization

Calling `/skill:autoresearch-create` in the pi chat window has the agent sequentially ask for objective, execution command, metric, and modification scope files. For example, you'd say something like "reduce Jest test execution time by 10%, but all existing tests must pass."

### ③ Running Loops & Checking Results

Afterwards, the agent automatically repeats code modification → git commit → run `autoresearch.sh` → parse metric → record jsonl.

Once 3+ experiments accumulate, MAD-based confidence appears. Example output looks like:

```
run #7  metric=test_time  value=18.42s  best_delta=-1.80s
         MAD=0.42s  confidence=4.3x   [green]
```

The formula is `confidence = |best_improvement| / MAD`, and the interpretation guidelines are:

- 2.0× or higher (green): improvement likely real
- 1.0–2.0× (yellow): larger than noise but be cautious
- Below 1.0× (red): essentially noise, re-run recommended

### ④ Finalization

Running `/skill:autoresearch-finalize` selects only experiments marked "keep" in jsonl,

groups them in units without overlapping files, and generates independent branches each starting from merge-base.

Each branch can be safely reviewed and merged as a separate PR.

### ⑤ Optional Configuration

Placing `autoresearch.config.json` in the session directory limits execution scope.

```
{
  "workingDir": "/path/to/project",
  "maxIterations": 50
}
```

`maxIterations` is the most reliable mechanism for enforcing LLM call cost ceiling, so setting it is highly recommended.

## Comparison with Similar Approaches

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| pi-autoresearch (autonomous loop + MAD) | Noise-based confidence auto-removes "false improvements," can pause and resume, finalize produces independent branches | Requires pi runtime and LLM API key; without maxIterations can cause cost explosion |
| karpathy/autoresearch original | Reference implementation validated in ML training loop optimization | Domain locked to ML, difficult applying directly to general SW metrics |
| Manual benchmark scripts | Zero external dependencies, complete manual control | People handle all iteration, comparison, rollback, subjective judgment in noise assessment |

## Conclusion

pi-autoresearch is a generalized experiment loop infrastructure that can automatically run "any measurable metric."

Thanks to MAD-based confidence scoring, you don't get fooled by measurement noise, and the finalize stage produces reviewable independent branches—both very practical for real work. If you have repetitive optimization work, even just running it for a day and comparing results is a good choice.

## References

- [pi-autoresearch GitHub Repository](https://github.com/davebcn87/pi-autoresearch)
- [pi-autoresearch Extension Directory Source](https://github.com/davebcn87/pi-autoresearch/tree/main/extensions/pi-autoresearch)
- [Ry Walker — pi-autoresearch Research Notes](https://rywalker.com/research/pi-autoresearch)
- [Tobi Lutke X(Twitter) Open Source Announcement](https://x.com/tobi/status/2032212536716578932)
