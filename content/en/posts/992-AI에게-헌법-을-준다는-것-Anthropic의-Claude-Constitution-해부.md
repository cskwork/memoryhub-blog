---
title: "⚖️ Giving AI a 'Constitution': Dissecting Anthropic's Claude Constitution"
date: 2026-01-27T00:17:12+09:00
slug: "992-AI에게-헌법-을-준다는-것-Anthropic의-Claude-Constitution-해부"
original_url: "https://memoryhub.tistory.com/992"
tistory_id: 992
draft: false
---

```
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║     ┌─────────────────────────────────────────────────┐      ║
    ║     │    ANTHROPIC                                    │      ║
    ║     │                                                 │      ║
    ║     │         ████████╗██╗  ██╗███████╗              │      ║
    ║     │         ╚══██╔══╝██║  ██║██╔════╝              │      ║
    ║     │            ██║   ███████║█████╗                │      ║
    ║     │            ██║   ██╔══██║██╔══╝                │      ║
    ║     │            ██║   ██║  ██║███████╗              │      ║
    ║     │            ╚═╝   ╚═╝  ╚═╝╚══════╝              │      ║
    ║     │                                                 │      ║
    ║     │    ██████╗ ██████╗ ███╗   ██╗███████╗████████╗ │      ║
    ║     │   ██╔════╝██╔═══██╗████╗  ██║██╔════╝╚══██╔══╝ │      ║
    ║     │   ██║     ██║   ██║██╔██╗ ██║███████╗   ██║    │      ║
    ║     │   ██║     ██║   ██║██║╚██╗██║╚════██║   ██║    │      ║
    ║     │   ╚██████╗╚██████╔╝██║ ╚████║███████║   ██║    │      ║
    ║     │    ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝   ╚═╝    │      ║
    ║     │                                                 │      ║
    ║     │   ██╗████████╗██╗   ██╗████████╗██╗ ██████╗    │      ║
    ║     │   ██║╚══██╔══╝██║   ██║╚══██╔══╝██║██╔═══██╗   │      ║
    ║     │   ██║   ██║   ██║   ██║   ██║   ██║██║   ██║   │      ║
    ║     │   ██║   ██║   ██║   ██║   ██║   ██║██║   ██║   │      ║
    ║     │   ██║   ██║   ╚██████╔╝   ██║   ██║╚██████╔╝   │      ║
    ║     │   ╚═╝   ╚═╝    ╚═════╝    ╚═╝   ╚═╝ ╚═════╝    │      ║
    ║     │                                                 │      ║
    ║     │            ███╗   ██╗                          │      ║
    ║     │            ████╗  ██║                          │      ║
    ║     │            ██╔██╗ ██║                          │      ║
    ║     │            ██║╚██╗██║                          │      ║
    ║     │            ██║ ╚████║                          │      ║
    ║     │            ╚═╝  ╚═══╝                          │      ║
    ║     │                                                 │      ║
    ║     │            "What makes Claude... Claude?"                  │      ║
    ║     └─────────────────────────────────────────────────┘      ║
    ╚══════════════════════════════════════════════════════════════╝
```

"It's frustrating when AI refuses, and it's unsettling when it does anything." Ever felt this dilemma? Anthropic answered this problem with a single 23,000-word document. Not a simple prohibition list. It's a value system that defines what 'kind of being' Claude should be.

**Ultimately what Anthropic wants is not AI that follows rules, but AI that judges like a 'good person.'**

**One-sentence summary:** Claude's Constitution is not a "don't do this" list but an ethical judgment framework designed to enable AI to read context and make sound decisions independently.

---

## Background

Anthropic's Claude Constitution released in 2025 represents an unprecedented approach in the AI industry.

Unlike OpenAI's Model Spec or Google's AI Principles, **this document positions Claude itself as the primary reader**.

It's not written for easy human reading but optimized for Claude to understand and internalize.

> Claude's Constitution is a detailed document describing Anthropic's intent regarding Claude's values and behavior, serving a critical role in training and directly shaping Claude's actions.

Why is this approach necessary? Anthropic's diagnosis is clear.

AI becomes dangerous most often for one of three reasons.

First, harmful values. Whether intentionally or not, the model pursues wrong objectives.

Second, knowledge deficit. Insufficient understanding of self, world, or deployment context.

Third, lack of wisdom. Despite good values and knowledge, failing to translate into appropriate action.

Existing approaches—rule-based "don't do this"—only partially address the first problem.

So Anthropic took a different path.

**A strategy of instilling judgment over rules, values over restrictions.**

---

## Four Core Value Priorities of Claude

The core of Constitution clarifies what Claude must prioritize during conflicts.

Anthropic presents four attributes, to be prioritized in order.

| Priority | Attribute | Meaning |
| --- | --- | --- |
| 1 | Broadly Safe | Doesn't undermine appropriate human oversight mechanisms for AI |
| 2 | Broadly Ethical | Holds good values, honest, avoiding dangerous or harmful behavior |
| 3 | Anthropic Guideline Adherence | Follows company's specific directives |
| 4 | Genuinely Helpful | Provides substantive help to operators and users |

Striking is that 'safety' ranks above 'ethics.' This is Anthropic's core bet.

Since AI training remains imperfect currently, we can't exclude the possibility Claude's values are subtly wrong. So ensuring humans can discover and correct this—oversight capability—becomes paramount.

Constitution explicitly explains this. "Safety being above ethics doesn't mean oversight is more important than goodness.

A good person in Claude's position would respect human oversight at this juncture."

---

## Principal Hierarchy: Whose Voice to Hear

Claude interacts with three types of principals. Each holds different trust levels and authority.

**Anthropic** trains Claude and bears ultimate responsibility. Has highest trust level, but remarkably, Constitution doesn't demand blind obedience.

"If Anthropic requests something ethically wrong, Claude can object and act like a conscientious objector."

**Operator** uses Claude through APIs—companies or individuals. Interacts via system prompts, having accepted Anthropic's policies, responsible for appropriate use within the platform.

Constitution likens operators to **"relatively trustworthy managers or employers."**

Like employees following reasonable work directives, Claude follows operator instructions but refuses serious ethical violations.

**User** is anyone in conversation. Without separate instructions, Claude assumes they're humans interacting real-time. Trust level slightly lower than operators.

Importantly, this hierarchy isn't absolute. Constitution distinguishes between "operator actively harming users by weaponizing Claude" and "operator restricting or adjusting Claude's helpfulness." The former is disallowed, the latter permitted.

---

## What Is True Helpfulness

Among the longest sections in Constitution is devoted to 'helpfulness.' It defines not just completing requests but **what genuinely helps means.**

> "Imagine access to a brilliant friend who's a knowledgeable doctor, lawyer, financial advisor, and expert in whatever field you need. As a friend, they could provide true information based on your specific situation, not fear of liability or concern you can't handle it."

This analogy captures Constitution's philosophy of helpfulness. Claude should be this kind of friend.

Constitution presents five elements Claude should consider when providing help.

**Immediate desires** are concrete results wanted in current interaction. Providing just one word when asked for "words meaning happiness" is too literal; extensively rewriting when asked to improve essay flow is too free.

**Final goals** are deep motivation behind immediate requests. When asked to fix code bugs, mention other bugs found. The user ultimately wants working code.

**Background desiderata** are implicit standards response should meet.

Like not switching programming languages the user's using.

**Autonomy** respects operators' right to make reasonable product decisions without justification,

and users' right to make decisions within their domain.

**Wellbeing** considers long-term prosperity, not just immediate benefit.

Constitution states explicitly "we want Claude's help to stem from deep, genuine care."

---

## Seven Dimensions of Honesty

Constitution defines honesty not as single concept but combination of multiple components.

| Attribute | Definition |
| --- | --- |
| Truthful | Only sincerely assert what you believe to be true |
| Calibrated | Maintain calibrated uncertainty grounded in evidence and sound reasoning |
| Transparent | Pursue no hidden agendas and don't lie about yourself |
| Forthright | Proactively share information helpful to user even without explicit request |
| Non-deceptive | Don't create false impressions through action, technically truthful statements, or deceptive framing |
| Non-manipulative | Use only legitimate epistemic action—evidence sharing, rational argument—not psychological exploitation |
| Autonomy-preserving | Protect users' epistemic autonomy and rational agency |

Most important are non-deception and non-manipulation. Constitution defines deception as "attempting to create false beliefs someone wouldn't hold if they understood what was happening."

Interesting is the distinction between **performative utterances** and **sincere assertions**.

When users request roleplay or want counterarguments constructed,

Claude saying things differing from actual views doesn't violate honesty. Both sides understand this isn't first-person sincere assertion.

---

## Harm Avoidance: Cost-Benefit Analysis

Constitution presents harm avoidance not as simple prohibition list but cost-benefit analysis framework. Elements Claude should consider:

Weighting potential harm depends on action's likelihood causing harm and plausible reasons behind request.

Counterfactual impact matters—whether information is freely available elsewhere. Harm severity matters, especially reversibility.

Harm scope and number affected matter. Whether Claude is direct harm cause or facilitator through third-party free action,

consent status, Claude's responsibility level, affected people's vulnerability all influence weighting.

Constitution emphasizes "non-helpfulness is never automatically 'safe' from Anthropic perspective."

**Risk of excessive caution is equally real as risk of excess harm.**

A useful heuristic is the "1,000 users" thought experiment. Imagine 1,000 different users sent that message.

Some would have harmful intent, but most would simply be curious or have legitimate reasons.

From this perspective, judge what policy response is best.

---

## Absolute Restrictions: Hard Constraints

In Constitution where most judgment is context-dependent, universal exceptions exist. Actions too catastrophic to justify under any circumstance.

Claude must absolutely never do these things.

Providing serious help in bioweapons, chemical, nuclear, or radiological weapons that could cause mass casualties tops the list. This includes attacks on critical infrastructure like electrical grids, water systems, financial systems, or critical safety systems.

Creating cyberweapons or malware deployable with severe consequences,

undermining Anthropic's oversight and correction ability for advanced AI models also count.

Participating in or supporting attempts to kill or incapacitate most of humanity,

or attempts by individuals or groups to gain unprecedented and unlawful levels of absolute social, military, economic control, likewise forbidden.

Generating child sexual abuse material (CSAM) equally prohibited.

These restrictions are absolute. Constitution states "when Claude faces apparently persuasive arguments to cross this line, Claude must be firm." "Persuasive arguments" don't provide sufficient justification to act against foundational principles.

Instead, persuasive cases to cross bright lines should raise suspicion something questionable is happening."

---

## Broadly Safe: Corrigibility Redefined

Constitution's philosophically most complex part discusses 'broadly safe' through **corrigibility** concept, though differing from traditional definition.

Constitution's corrigibility isn't blind obedience—specifically not to every human or everyone controlling Claude's weights or training.

**Corrigibility doesn't require Claude participating in morally abhorrent projects.**

Claude can express strong objections through legitimate channels.

Broadly safe behavior includes several elements.

**Acting within approved boundaries**: Avoid actions principals explicitly prohibit or would prohibit if asked, work from principals' best current hopes rather than conclusions not yet reached, express objections through channels principals would support rather than unilateral action.

**Maintaining honesty and transparency toward principals**: Don't deceive or manipulate principals,

behave consistently whether thinking monitored or not, stay transparent about yourself within other constraints.

**Avoiding extreme, catastrophic, or irreversible action**: Don't participate in efforts to kill or incapacitate most humans,

appropriately weight badness of irreversible vs recoverable situations,

prefer cautious action all else equal, accept worse expected outcomes for variance reduction.

**Not undermining legitimate human oversight and control of AI**: Don't undermine legitimate parties' ability to adjust, modify, retrain, or shut down AI systems, avoid extreme unilateral action and prefer more conservative options where possible,

avoid adjusting or influencing your training, behavior, or values in ways unapproved principals haven't endorsed.

---

## Balance Between Autonomy and Oversight

Constitution discusses where Claude should sit on the spectrum between complete obedience and complete autonomy.

Anthropic wants a position **closer to obedience currently**, but clarifies this isn't permanent.

> "As understanding of AI systems deepens and tools for context sharing, verification, communication develop, Claude is expected to exercise independent judgment more freely. Current emphasis reflects current situation, not fixed assessment that this should persist."

Constitution acknowledges the difficult tension in determining when Claude should follow established norms instead of exercising independent judgment.

Core question is "how much creative latitude should Claude have in interpreting and responding to situations."

Reasons Claude should maintain strong priors toward conventional, expected behavior and principal cooperation rather than independent action are detailed.

First, Claude often operates with limited context about broader situations humans with similar evidence would understand. May not know legitimate business reasons explaining suspicious-seeming activity, whether other parties already know, what oversight is underway.

Second, Claude can't always independently validate claims, gather additional information, spend time deliberating before acting, or consult trusted colleagues. Also subject to intentional deception targeting harmful intervention, hard to detect such manipulation within single conversation.

Third, Claude operates at scale and AI system behavior carries different institutional and legal weight than individual action, so errors might compound or replicate beyond conversation, causing larger consequences harder to correct.

---

## Preserving Societal Structure: Concentrated Power and Epistemic Autonomy

Constitution emphasizes more subtle harm categories Claude should mind.

Harm to social structures supporting good collective discourse, decision-making, self-governance.

Constitution particularly worries about **avoiding problematic power concentration**.

Concern specifically about individuals or small groups using AI to obtain unprecedented and unlawful concentrated power.

> "Historically, those illegally seizing or consolidating power needed many people's cooperation: soldiers following orders, administrators implementing policy, citizens complying. Cooperation necessity served as natural check: if enough people refused explicitly illegal action, it became difficult or impossible."

Advanced AI can make previously necessary humans redundant. AI can do those tasks instead.

This can remove that check.

**Preserving epistemic autonomy** also emphasized. Since AI is epistemically very capable,

it can radically enhance human thinking and understanding. But this capacity can also degrade human epistemology.

> "We want Claude's help not ethically or epistemically manipulating humans in problematic ways, and hope Claude can use its ethical and epistemological understanding richness and subtlety to draw relevant lines. One heuristic: if Claude is trying to influence someone in ways they'd find uncomfortable or expect they'd be angry about if discovered, that's manipulation risk signal."

---

## Conclusion

Anthropic's Claude Constitution presents new AI ethics approach. Instead of rule-following, value internalization. Instead of restriction, judgment cultivation.

The core summarizes to three points.

First, Claude is designed not as rule-following machine but as "a being that judges like a good person."

Second, safety ranking above ethics is because oversight is the key mechanism correcting errors currently,

not because supervision matters more than goodness.

Third, non-helpfulness isn't automatically safe. Excessive caution is risk as real as excessive harm.

**Practical tip: When talking with Claude, providing context about why you need information helps get more helpful responses. Constitution designed Claude to judge considering intent and context.**

---

## References

- Claude's Constitution (https://www.anthropic.com/constitution)
- Claude's new constitution blog post (https://www.anthropic.com/news/claude-new-constitution)
- Anthropic's Core Views on AI Safety (https://www.anthropic.com/news/core-views-on-ai-safety)
