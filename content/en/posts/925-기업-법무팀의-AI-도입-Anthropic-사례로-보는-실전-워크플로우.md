---
title: "Corporate Legal Team's AI Adoption, Real-World Workflow Through Anthropic Case Study"
date: 2025-12-09T23:13:30+09:00
slug: "925-기업-법무팀의-AI-도입-Anthropic-사례로-보는-실전-워크플로우"
original_url: "https://memoryhub.tistory.com/925"
tistory_id: 925
draft: false
---

```
    ╔═══════════════════════════════════════════╗
    ║                                           ║
    ║      LEGAL  +  AI                        ║
    ║                                           ║
    ║    ┌─────────────────────────────────┐    ║
    ║    │  CONTRACT REVIEW      [AUTO]   │    ║
    ║    │  COMPLIANCE CHECK     [AUTO]   │    ║
    ║    │  RISK ANALYSIS        [AUTO]   │    ║
    ║    │  DRAFT DOCUMENTS      [AUTO]   │    ║
    ║    └─────────────────────────────────┘    ║
    ║                                           ║
    ║         Human-in-the-Loop Review          ║
    ║              ┌─────────┐                  ║
    ║              │  ✓ OK   │                  ║
    ║              └─────────┘                  ║
    ╚═══════════════════════════════════════════╝
```

"The legal team? They're the most conservative, so AI adoption is difficult there." You've probably heard this before. Yet Anthropic, the company that creates AI, already uses Claude to build and run an automated legal workflow directly. And they have no coding experience. **The key to legal AI adoption is not technical prowess but answering the question: "What repetitive tasks will we automate?"**

**Summary:** In short, legal team AI adoption hinges on process analysis ability rather than coding skills, and the success strategy is automating the most tedious repetitive work first.

## Background

The legal tech market is exploding. According to Grand View Research, the global legal AI market is projected to grow at a compound annual growth rate of 17.3%, from $1.45 billion in 2024 to $3.9 billion by 2030. In 2024 alone, $4.98 billion (approximately 7.3 trillion won) was invested in legal tech companies worldwide.

Korea is no exception. At the "Korea Legal Tech Forum 2025" held in Seoul in June 2025, major companies and law firms like SK C&C, Doosan, and Kim & Chang shared AI adoption cases. Bang Young-sun, CEO of Thomson Reuters Korea, diagnosed: "In 2023, expectations about AI were the focus; in 2024, actual utilization began in earnest; now in 2025, there's a growing awareness that not adopting AI could put you behind."

Yet many legal teams hesitate to adopt AI for clear reasons: fear of technical barriers, lack of trustworthy content, and existing system integration problems. Thomson Reuters' Asia regional survey confirms these three are the biggest adoption obstacles.

## Core Concepts

> One-line definition: A legal AI workflow is a Human-in-the-Loop system where AI handles the first pass of repetitive legal review work, and legal professionals perform final validation.

The Anthropic legal team's case demonstrates this concept concretely. The law department's professionals describe themselves as "non-technical" and say "you can build workflows through natural language conversation alone with Claude Code, even without coding knowledge."

**Implemented Workflow: Automating Legal Review of Marketing Materials**

The old process worked like this: When marketing finishes a blog post or launch materials, they send a legal review request. The legal professional reads the material from beginning to end and identifies legal risk factors. Most requests arrive the day before launch, and staff spend considerable time performing repetitive checklist reviews.

The automated process is different. Marketing staff open a review tool linked to Slack and paste content. When they click 'Analyze Content,' Claude analyzes the content according to pre-defined legal frameworks. The output presents an identified issues list (accuracy, security claims, third-party content rights, partnership considerations, etc.) and risk levels (Low/Medium/High). A Slack message to share with the legal team is also auto-generated.

**The critical part is Human-in-the-Loop.** AI handles first-pass screening and issue classification, but the legal team's final review and judgment must come from humans. The professional even clarifies: "The AI system can still hallucinate. I'm still reviewing the work."

This approach works because it fundamentally changes the work nature. Instead of legal professionals spending all day on repetitive first-pass screening, they can focus on high-value expert judgment about issues AI pre-classified.

## Implementation Methods

① **Identify the Most Tedious Work**

AI adoption starts with work analysis, not technology. Anthropic's legal counsel agrees: "When people ask where to start, I tell them to think about their most routine work. Just open Claude and try. You don't know what AI can do until you try it yourself."

Common repetitive tasks in legal teams include: contract draft review, checking standard clause conformance, legal risk screening for marketing materials, conflict of interest policy review, and external business activity request assessment.

② **Define a Review Framework**

Telling AI "review this contract" doesn't yield consistent results. Instead, provide specific checklists. Anthropic's marketing materials review tool provides Claude with a "what I care about" framework and designs analysis accordingly.

For example, the marketing materials review framework includes fact accuracy verification, confirmation of security claim evidence, third-party content usage rights review, and partnership disclosure appropriateness.

③ **Integrate with Workflows**

Tools integrated into existing workflows actually get used over standalone ones. In the Anthropic example, the review tool link is pinned in a Slack channel for easy marketing team access. The flow also implements generating Slack messages directly from analysis results and connecting to legal team tickets.

④ **Maintain Human-in-the-Loop**

Using AI output directly as final results is risky. According to the 2025 Legal Industry Report, legal workflows must "include review by qualified attorneys before finalizing AI output." Only humans can judge missed context, latest legal changes, and company-specific circumstances.

## Adoption Pattern Comparison

| Pattern | Advantages | Considerations |
| --- | --- | --- |
| Marketing/PR Material Pre-Review | Early risk discovery before launch, reduced legal workload | Must clearly define AI risk classification criteria |
| Contract Clause Conformance Review | Auto-identify changes vs. standard, reduce review time | Exception judgment based on context must be human |
| Conflict of Interest/External Activity Review | Automate first-pass classification by policy | Privacy required for sensitive information handling |
| Contract Data Analysis | Derive insights on company-wide contract status, discover risk patterns | Data quality determines analysis result quality |

Korea's legal AI platform "Alibi" is used by companies like CJ CheilJedang, Hanwha Solutions, and Aekyung Chemical, reporting 67% contract review time reduction.

## Final Thoughts

- The key to legal team AI adoption is **what repetitive work will be automated**, not coding ability
- AI doesn't replace legal professionals—it handles first-pass screening so **experts focus on high-value judgment**
- Practical tip: Pick one legal task that consumes the most time while being repetitive, explain review criteria to Claude right now, and test it

## References

- Grand View Research, Legal AI Market Report (https://www.grandviewresearch.com/industry-analysis/legal-ai-market-report)
- 2025 Legal Industry Report, American Bar Association (https://www.americanbar.org/groups/law_practice/resources/law-technology-today/2025/the-legal-industry-report-2025/)
- Korea Legal Tech Forum 2025 Coverage - Tech42 (https://www.tech42.co.kr/)
- 2025 LTAS Legal Tech AI Special Exhibition (https://ltas.co.kr/)
