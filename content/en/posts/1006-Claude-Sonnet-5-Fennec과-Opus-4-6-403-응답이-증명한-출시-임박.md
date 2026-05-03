---
title: "🔐 Claude Sonnet 5 Fennec and Opus 4.6: 403 Response Proves Launch is Imminent"
date: 2026-02-05T21:49:57+09:00
slug: "1006-Claude-Sonnet-5-Fennec과-Opus-4-6-403-응답이-증명한-출시-임박"
original_url: "https://memoryhub.tistory.com/1006"
tistory_id: 1006
draft: false
---

```
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║     VERTEX AI MODEL GARDEN - ENDPOINT SCAN RESULTS             ║
    ║     ══════════════════════════════════════════════════         ║
    ║                                                                ║
    ║     ┌────────────────────────────────────────────────┐         ║
    ║     │  MODEL ID                    │  HTTP RESPONSE  │         ║
    ║     ├────────────────────────────────────────────────┤         ║
    ║     │  claude-sonnet-99 (fake)     │  404 NOT FOUND  │         ║
    ║     │  claude-opus-99 (fake)       │  404 NOT FOUND  │         ║
    ║     ├────────────────────────────────────────────────┤         ║
    ║     │  claude-sonnet-5             │  403 FORBIDDEN  │  ←      ║
    ║     │  claude-opus-4-6             │  403 FORBIDDEN  │  ←      ║
    ║     └────────────────────────────────────────────────┘         ║
    ║                                                                ║
    ║     403 = EXISTS but ACCESS DENIED (permission-gated)          ║
    ║     404 = DOES NOT EXIST                                       ║
    ║                                                                ║
    ║          ┌─────────┐        ┌─────────┐                        ║
    ║         /  FENNEC   \      /  OPUS    \                        ║
    ║        │   (o   o)   │    │   4.6     │                        ║
    ║         \   \_/    /      │    ???    │                        ║
    ║          \_______/        └─────────┘                          ║
    ║                                                                ║
    ║              SONNET 5          OPUS 4.6                        ║
    ║            "Value monster"      "New peak?"                    ║
    ╚════════════════════════════════════════════════════════════════╝
```

"404 means the model doesn't exist, 403 means it exists but access is denied." This simple HTTP response rule became the technical evidence of the largest leak in the AI industry.

When developer Ben Taleb Jr. scanned Google Vertex AI endpoints, both `claude-sonnet-5` and `claude-opus-4-6` returned 403 Forbidden. Fake model IDs returned 404.

**This is technical evidence that both models are already deployed on Google infrastructure and are just waiting for the public switch to be flipped.**

**TL;DR:** In short, both Claude Sonnet 5 and Opus 4.6 have been confirmed to exist on Vertex AI, and

Anthropic's "dual-track" strategy is becoming a reality.

## Background

Anthropic's model lineup had a clear hierarchy: Haiku for speed, Sonnet for balance, Opus for maximum performance. But this leak creates a crack in that structure.

> One-line definition: 403 Forbidden means in a RESTful API that "the resource exists but access is denied." Unlike 404 Not Found, it indicates the server recognizes the resource.

In early February 2026, a post by developer Ben Taleb Jr.(@macintoch) on X shook the AI community.

He ran a scan script against Google Cloud Vertex AI's Model Garden endpoint, and the results were clear.

Fake model IDs that don't exist (claude-sonnet-99) returned 404,

while leaked model IDs (claude-sonnet-5, claude-opus-4-6) returned 403.

This discovery was independently verified.

Multiple developers, including DeepakNess, created their own Vertex AI projects and performed the same tests.

The results were consistently identical: actually existing models (like Opus 4.5) returned 200 OK, leaked models returned 403, and fake models returned 404.

## Core of the Leak: Two Models Discovered Simultaneously

What's notable is that **Sonnet 5 and Opus 4.6 were discovered together.** This suggests that Anthropic is preparing two models with different purposes simultaneously.

**Claude Sonnet 5 "Fennec" - Leaked Information**

The model ID is `claude-sonnet-5@20260203`, which matches Anthropic's existing naming convention (`claude-opus-4-5@20251101`). The internal codename "Fennec" refers to a desert fox with large ears, which is interpreted as symbolizing the expanded context window of 1 million tokens. According to leaked benchmarks, the SWE-Bench Verified score is estimated between 82.1% and 83.3%,

which exceeds the current Opus 4.5's 80.9%. The price is known to be the same as Sonnet 4.5: $3/$15 (input/output per 1M tokens).

**Claude Opus 4.6 - Existence Only Confirmed**

Detailed specs for Opus 4.6 were not leaked. All that's confirmed is that the `claude-opus-4-6` endpoint returns a 403 response. This means the model exists and is deployed, but hasn't been publicly released yet.

Pankaj Kumar analyzed on X that there were four service disruptions on February 3rd, which could be evidence of failed deployments and rollbacks.

## Technical Evidence Analysis

| Test Target | HTTP Response | Meaning |
| --- | --- | --- |
| claude-sonnet-99 (fake) | 404 Not Found | Resource doesn't exist |
| claude-opus-99 (fake) | 404 Not Found | Resource doesn't exist |
| claude-opus-4-5 (current) | 200 OK | Normal access possible |
| **claude-sonnet-5** | **403 Forbidden** | **Exists but inaccessible** |
| **claude-opus-4-6** | **403 Forbidden** | **Exists but inaccessible** |

The key point is that multiple independent validators obtained identical results.

This is reproducible technical evidence, not just screenshots or rumors.

## Inferred Positioning of the Two Models

Based on leaked information, Anthropic's strategy can be inferred as follows:

**Sonnet 5: Value Revolution**

Offers Opus 4.5-level performance at 20% of Opus pricing.

A 1-million-token context enables processing entire codebases at once. Through "Dev Team Mode," autonomous sub-agent creation is possible. Primary targets are high-volume API calls, agent workflows, and cost-sensitive projects.

**Opus 4.6: New Peak?**

Specific specs remain unconfirmed. However, based on Anthropic's pattern, the Opus line always aims for "maximum performance."

If Sonnet 5 exceeds Opus 4.5, Opus 4.6 would target an even higher level.

Anticipated targets are research requiring extreme reasoning capability and mission-critical enterprise work.

## Best Practices/Response Strategy Comparison

| Situation | Recommended Strategy | Rationale |
| --- | --- | --- |
| Currently using Opus 4.5 | Maintain, A/B test when Sonnet 5 launches | Sonnet 5 may offer equal or better performance at lower cost |
| High-cost reasoning tasks | Wait for Opus 4.6 launch | New flagship needed for maximum performance requirements |
| Operating many agents | Prepare immediate switch to Sonnet 5 | Potential 80% cost savings |
| Can't depend on unconfirmed info | Continue with current models | All info unverified until official announcement |

## Conclusion

- Google Vertex AI scan results confirmed existence of both Claude Sonnet 5 and Opus 4.6 with 403 Forbidden status.
- Sonnet 5 "Fennec" may offer Opus 4.5 performance at 20% of the price, while Opus 4.6 is estimated to be the new top-tier model.
- Anthropic has made no official announcement, so all specs and launch dates remain unverified.
- Practical tip: Monitor the Anthropic official blog (anthropic.com/news) and have your code ready to test with just a `model` parameter change upon launch.

## References

- Claude Sonnet 5 & Opus 4.6 Leak: The 403 Forbidden Proof - Marco Patzelt (https://www.marc0.dev/en/blog/claude-sonnet-5-fennec-leak-what-the-vertex-ai-logs-actually-show-1770048662320)
- Claude Opus 4.6 launching soon - DeepakNess (https://deepakness.com/raw/opus-4-6-soon/)
- Anthropic Fennec Leak Signals Imminent Launch - Dataconomy (https://dataconomy.com/2026/02/04/anthropic-fennec-leak-signals-imminent-claude-sonnet-5-launch/)
- Pankaj Kumar X Post on Double Drop (https://x.com/pankajkumar_dev/status/2019055211164381649)
- Anthropic official news page (https://www.anthropic.com/news)
