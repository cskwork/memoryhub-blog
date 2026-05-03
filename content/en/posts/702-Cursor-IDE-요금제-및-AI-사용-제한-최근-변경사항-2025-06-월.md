---
title: "Cursor IDE Pricing and AI Usage Limits Recent Changes - June 2025"
date: 2025-06-19T20:13:30+09:00
slug: "702-Cursor-IDE-요금제-및-AI-사용-제한-최근-변경사항-2025-06-월"
original_url: "https://memoryhub.tistory.com/702"
tistory_id: 702
draft: false
---

Cursor IDE completely restructured its personal pricing plan in mid-2025, introducing new premium tiers and modifying how AI usage is measured for existing plans. Key changes include the new "Ultra" subscription tier and the transition of the Pro plan from fixed monthly request allocations to "unlimited with rate limiting" model. Below is a detailed breakdown of updates with focus on AI usage limits and rate limiting rules across Free (Hobby), Pro, and Ultra tiers.

**New Pricing Structure (2025 Update)**

**Ultra Tier Introduction:** On June 16, 2025, Cursor launched the Ultra plan at $200/month for power users. This tier provides approximately 20x the usage of Pro, equivalent to roughly ~10,000 AI requests per month on fixed allocation. The Ultra tier was created to meet the demands of heavy users seeking predictable high-volume access without relying on overage pay-as-you-go charges. It also includes all Pro features plus perks like full pull request indexing and early access to new features.

**Pro Plan Changes:** Cursor's Pro plan (maintained at $20/month for individual users) has become more generous. Previously, Pro included 500 "fast" AI requests per month (with additional purchase options or everything beyond was slow requests). After the update, Pro now offers "unlimited" AI requests with speed-based throttling instead of fixed monthly limits. This means monthly request counts are not capped; instead, usage is limited by internal rate limits on how quickly requests can be made. All specific tool-call limits under Pro (such as for background agents or bug-finding bots) have also been removed. Notably, existing Pro users can maintain the legacy 500-request allocation if they prefer predictable counts over the new model.

**Free (Hobby) Tier:** The Hobby (free) tier continues to be offered at $0 for new and light users. New users still receive a 2-week Pro trial, after which usage becomes restricted. The free tier provides limited AI usage - approximately 2,000 code completions and 50 AI agent requests per month (these free requests run in "slow" mode with queue delays). This allows free users to try Cursor's core features at small scale, but larger AI usage requires an upgrade. Model access is also limited in the free tier (fewer or lower-tier models), while Pro/Ultra users get access to all premium models (GPT-4 variants, Claude, Google Gemini, etc.).

**AI Usage Limits by Plan (Free vs Pro vs Ultra)**

The table below compares key features and AI usage limits across Cursor's personal tiers after recent changes:

| Plan (Individual) | Price | AI Requests (Agent/Chat) | Rate Limiting Policy | Code Completions (Tab Support) |
| --- | --- | --- | --- | --- |
| Hobby (Free) | $0/month | ~50 AI requests/month, "slow" queued requests (no fast quota) | No real-time burst – free requests are queue-limited (low priority) | ~2,000 completions max/month |
| Pro | $20/month ($16/month annual) | Unlimited AI requests but real-time rate limits (legacy option: 500 fast requests/month) | Yes – usage managed by internal rate limits per minute/hour rather than fixed monthly cap. Temporary throttling possible with heavy usage | Unlimited code completions |
| Ultra | $200/month | 20x Pro usage (~10,000 AI requests/month equivalent), fixed included. Effectively very high limit before restrictions. | Yes (higher) – similar rate limiting system but ~20x higher thresholds than Pro, allowing significantly more throughput | Unlimited code completions (same as Pro) |

**Note:** All tiers support optional pay-as-you-go usage beyond included limits (usage-based billing for additional requests). Team and Enterprise plans (not detailed above) are based on Pro features with team management capabilities and higher included usage for Enterprise.

**New AI Rate Limiting Policy**

With Pro's fixed request limit removal, Cursor introduced rate limiting mechanisms to prevent abuse and manage costs. All tiers (Pro and Ultra included) now experience these AI usage rate limits for "agent" (chat) functionality:

**Burst vs. Sustained Limits:** Cursor defines two types of limits. Burst rate limits allow short-term "explosive" usage – users can briefly exceed normal speed if needed, but this burst capacity slowly recharges over time. Meanwhile, local rate limits (sustained rate) impose a more stable cap on request throughput but fully reset every few hours. Simply put, you can execute a quick sequence of AI requests during a burst (consuming burst quota), but if you continue heavily afterward, you may wait for the quota to replenish. Normal usage is managed by periodic local speeds that refill (Cursor hasn't disclosed exact refill intervals, but they're hourly).

**Computing-Based Metering:** Rate limits are not based on simple request counts but on underlying compute usage (tokens/model time) for requests. This means heavy requests (large code context, complex prompts using GPT-4 or Claude) consume more quota. The Cursor team noted they "internally calculate computing used much like OpenAI/Anthropic does for their pricing." Consequently, hitting limits occurs after varying numbers of requests, making limits somewhat opaque to users.

**Undisclosed Thresholds:** Cursor has not publicly disclosed exact numerical rate limits (e.g., "X requests per hour") for the new system. This lack of transparency has caused some user confusion about how much they can do before limits kick in. Some users speculate it's similar to Anthropic's Claude Code pricing, but Cursor officially only states users are notified when limits are reached. Limits automatically reset after a few hours, at which point usage can resume.

**Behavior When Limits Reached:** When Pro/Ultra users exhaust both local and burst quotas (i.e., hit rate limits), Cursor notifies the user and temporarily denies further agent requests. At that point, the app presents options—for example, switch to a lower-cost model with lower rate limits, consider upgrading from Pro to Ultra if on Pro, or enable usage-based billing to continue beyond included usage for a per-request fee. That is, Pro users who repeatedly hit speed ceilings aren't simply locked out; they can either pay per additional request, upgrade, or wait for quotas to refresh.

**Free Tier Rate Limiting:** The free "Hobby" tier essentially runs all agent queries as "slow requests," which are heavily rate-limited by design. Once free users exhaust their trial fast requests, they receive queuing (often 30+ second waits per request). Essentially, free usage is so throttled that performing large-scale AI work without an upgrade becomes impractical.

**Plan Differences and Usage Boundaries**

Beyond price, tiers differ primarily in AI feature usage limits and speed:

**Free vs. Pro:** The free Hobby tier provides only a small amount of Cursor's AI features – after the trial, free users are capped to slow, queued requests (~50/month) and cannot access the most advanced models or large context windows. The Pro tier removes these barriers by allowing unlimited completions and agent chat at normal speed within fair-use limits (the new rate limiting system). Pro users also gain advanced features like background agents, "Bug Bot" for AI-aided debugging, and full-length context support for large files or codebases.

**Pro vs. Ultra:** The new Ultra tier was created for users who regularly push Pro's boundaries. Ultra users get capacity increases by orders of magnitude – roughly 20x Pro's usage allocation in terms of computing they can consume before limits apply. Practically, Ultra users are far less likely to see rate limit notifications. Ultra's fixed $200/month fee is steep but was designed for developers who burn through Pro limits and incur unpredictable overage charges.

**Rationale for Changes**

Cursor provided several explanations for these pricing and policy changes:

**Addressing Power User Demands:** The Ultra launch and new Pro model were driven by user feedback. Many "power users" were hitting the previous Pro ceiling (500 requests) and either had to purchase additional packs or deal with slow mode. They requested higher-tier plans for more predictable, unlimited development without micromanaging usage.

**Predictable Pricing vs. Usage-Based:** Previously, Pro users who exhausted included requests could enable usage-based billing (pay-per-request) for continued fast access. While flexible, this model made costs variable and could result in surprise bills if users weren't careful.

**Competitive Strategy:** The move of Pro to "unlimited with rate limiting" aligns Cursor more closely with competing products. Competing AI coding assistants (like GitHub Copilot) charge fixed monthly fees for unlimited usage. Cursor likely wanted to remove friction on the Pro tier's 500-request cap to stay competitive with individual users.

**Technology and Cost Viability:** Cursor was able to increase usage limits thanks to partnerships with AI model providers. The company has secured multi-year deals with OpenAI, Anthropic, Google, and others, securing better pricing and higher quotas for AI model consumption.

**Glossary:**

- **AI Request**: A command or question sent to the AI
- **Rate Limit**: Maximum number of uses allowed within a specific time period
- **Burst**: Using a large amount in a short time all at once
- **Token**: Basic unit of text processed by the AI
- **Computing**: Work calculated by the computer
- **Quota**: Fixed amount available for use
- **Legacy**: Previous version or outdated system
- **Pay-as-you-go**: Payment model where you pay based on what you use
- **Threshold**: Limit point or benchmark value
- **Pull Request**: Process of reviewing and merging code changes
- **Rate Limit**: Restricts the number of API calls allowed during a specific timeframe. Exceeding this causes requests to be delayed or blocked.
- **Throttle**: Measure to artificially slow processing speed when there are too many requests.

### 📚 **Sources List**

1. **Cursor Official Blog**
   - *Introducing the Ultra Plan | Cursor*
   - <https://www.cursor.com/en/blog/new-tier>  
     → Ultra plan introduction and differences vs existing plans
2. **API Dog Blog**
   - *Cursor's New $200 Ultra Plan: Is It Worth It for Developers?*
   - <https://apidog.com/blog/cursor-ultra-plan/>  
     → Ultra plan cost-effectiveness and developer perspective analysis
3. **Cursor Official Pricing Page**
   - *Pricing | Cursor*
   - <https://www.cursor.com/pricing>  
     → Summary comparison of Free, Pro, Ultra plans
4. **UI Bakery Blog**
   - *Cursor AI Pricing Explained: Which Plan is Right for You?*
   - <https://uibakery.io/blog/cursor-ai-pricing-explained>  
     → Feature-based plan selection guide
5. **Cursor Community Forum**
   - *Cursor Pro & Cursor Ultra - Discussions*
   - <https://forum.cursor.com/t/cursor-pro-cursor-ultra/104528>  
     → User plan comparisons and real experience sharing
6. **Cursor Forum**
   - *Still hit the rate limit for the pro plan*
   - <https://forum.cursor.com/t/still-hit-the-rate-limit-for-the-pro-plan/105796>  
     → Reports of rate limiting occurring even on Pro plan
7. **Cursor Official Documentation**
   - *Plans & Usage*
   - <https://docs.cursor.com/account/plans-and-usage>  
     → Organized usage policies for each plan
8. **Cursor Official Documentation**
   - *Rate Limits*
   - <https://docs.cursor.com/account/rate-limits>  
     → Request limit criteria and specific numbers
9. **Reddit Community**
   - *More info about Rate Limits on Cursor Website*
   - <https://www.reddit.com/r/cursor/comments/1le1uhj/more_info_about_rate_limits_on_cursor_website/>  
     → Unofficial rate limit information discovered by users
10. **Reddit Community**
    - *Slow requests are deliberately slowed down and I think I have the proof.*
    - <https://www.reddit.com/r/cursor/comments/1ileb1w/slow_requests_are_deliberately_slowed_down_and_i/>  
      → User-measured request speed limits and throttle phenomena
