---
title: "SKT Call Center AWS Bedrock Claude Use Case"
date: 2025-09-30T09:01:30+09:00
slug: "802-SKT-콜센터-AWS-Bedrock-Claude-사용-사례"
original_url: "https://memoryhub.tistory.com/802"
tistory_id: 802
draft: false
---

SK Telecom has maintained the top position in Korea's National Customer Satisfaction Index (NCSI) for 27 years and is further enhancing its renowned customer service operations by leveraging Claude from Amazon Bedrock.

# Claude Implementation Results

- In-call assistant support: Human representatives evaluated LLM response quality improved by 34%
- Telecommunications-specific fine-tuned model: Low-quality response rate decreased by 68% compared to baseline
- Post-call processing response quality: Achieved approximately 89% of human representative level

## Meeting Korea's Unique Customer Service Demands

Korea's fast-paced culture creates unique customer service expectations beyond standard support. Eric Davis, SK Telecom's AI Technology Collaboration Group leader, said: "Korea is a very impatient society. If you're one minute late, you might as well be ten minutes late."

SK Telecom, which has maintained first place in domestic customer service for 27 consecutive years, built its reputation through regional call centers reflecting local dialects and cultural nuances, providing rapid responses and personalized support. However, traditional call centers operate only weekday 9am–6pm, and while older customers prefer phone calls, younger customers prefer chat—creating gaps that must be bridged while maintaining excellence. Davis noted: "When you call, you can speak to someone in minutes, but that's very different from waiting 30 minutes on hold," explaining that as expectations continue rising, innovation is necessary to maintain this service level.

## Why SK Telecom Chose Claude

After evaluating multiple LLMs, SK Telecom chose Claude based on three criteria essential for market leadership. First was brand safety. Davis said: "Brand safety is decisive for us. We cannot tolerate anything that damages our brand. Anthropic's heavy focus on safety was particularly notable."

Second, Claude's natural communication ability differentiated it from competitors. Davis explained: "Claude is more empathetic and creative." In Korean customer service, cultural nuance and empathy are especially important. While other models generated formal and stiff responses, Claude demonstrated the cultural sensitivity needed for natural conversations including local dialects. 

The final breakthrough came from Amazon Bedrock integration. Davis stated: "We put significant effort into Bedrock to ensure performance," adding that "performance goes beyond just accuracy—throughput and latency also had to meet our standards."

Amazon Bedrock smoothly served SK Telecom's custom models, rapidly scaled resources, and enabled stable launches of large-scale LLM services. AWS and Anthropic's close collaboration also resolved issues quickly and enabled efficient deployment.

SK Telecom combined its proprietary RAG model with Claude to implement end-to-end Retrieval-Augmented Generation (RAG), which Davis calls a "killer combination." This integration significantly improved service capabilities, with telecommunications LLM performance improving from 3.3 to 4.3 or higher—a meaningful achievement in the highly efficient Korean market with very high customer service standards.

## Intelligent Customer Support Implemented by Claude

SK Telecom deployed two key solutions.

In-Call Assist

- Provides real-time document search and answers to representatives
- Reduces cognitive load of overwhelmed representatives
- Automatically delivers relevant information

Post-Call Processing

- Automates routine post-call tasks like summarization, topic classification, to-do generation, and sentiment analysis
- Maintains human review of results
- Simplifies workflows while guaranteeing quality

## Changes in Representative and Customer Experience

Claude-based solutions transformed representative well-being and service quality at SK Telecom. Claude-based solutions greatly improved representative evaluation scores, increasing from 3.3 to mid-4-range, meeting SK Telecom's strict service deployment standards. Davis said: "We realized our customer service representatives were stressed and overloaded. We wanted human-in-the-loop (HITL) technology that could make their lives better."

SK Telecom's approach is "Intelligence Augmentation (IA)," focusing on enhancing rather than replacing human capability. Davis emphasized: "This isn't about replacing jobs, it's about augmenting experience." Thanks to this philosophy, SK Telecom maintained the human touch of its regional support network that responds in local dialects preferred by regional customers while solidifying its 27-year customer service leadership.

## Building the Future of Human-Centered AI Support

SK Telecom is developing more sophisticated AI solutions supporting a human-centered vision. Davis stated: "We'll build models that are much more multilingual and much more sophisticated." While automation levels will increase due to workforce structure changes, SK Telecom maintains its principle of using technology to enhance irreplaceable human connections that distinguish exceptional customer service.

Through its partnership with Anthropic, SK Telecom aims to provide a blueprint for how global companies can harness AI's power while preserving the irreplaceable human element of customer care.

### References

<https://claude.com/customers/skt>
