---
title: "Universal Commerce Protocol: Essential Infrastructure for the Era When AI Handles Payments"
date: 2026-01-13T21:03:19+09:00
slug: "965-Universal-Commerce-Protocol-AI가-결제까지-해주는-시대의-필수-인프라"
original_url: "https://memoryhub.tistory.com/965"
tistory_id: 965
draft: false
categories: ["Dev Library"]
tags: ["Claude"]
---

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     ┌─────────┐    UCP    ┌─────────┐    UCP    ┌─────────┐  ║
║     │   AI    │◄────────►│ PAYMENT │◄────────►│  SHOP   │  ║
║     │  Agent  │           │Provider │           │ Backend │  ║
║     └─────────┘           └─────────┘           └─────────┘  ║
║          │                     │                     │        ║
║          └─────────────────────┴─────────────────────┘        ║
║                    Universal Commerce Protocol                ║
║                                                               ║
║      "The common language of an era when AI shops for you"   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

"AI, recommend wireless earbuds under $100." We're already used to this. But what if when you say "buy the recommended product right now," the AI actually completes the payment? The problem is there are millions of online shops, each using different systems.

**Universal Commerce Protocol (UCP) is the 'common language' that lets AI agents talk to any online shop in this chaos.**

Bottom line: UCP is an open-source standard jointly developed by Google and Shopify and supported by 20+ global companies, defining the commerce infrastructure for the era of AI agents.

## Background

The term "Agentic Commerce" has been spreading rapidly since 2025. Beyond simple product recommendations, it means AI agents handle the entire process—from product search to adding to cart to checkout—on behalf of users.

But here's a fundamental problem: Shopify-based shops, custom-built sites, and large marketplaces all use different APIs and payment systems. If an AI agent needs separate integration for each shop, you end up needing N×M custom integrations between N agents and M shops.

> UCP is a standardized communication protocol between AI agents, online shops, and payment services, guaranteeing interoperability without custom integrations—an open-source protocol.

Just as TCP/IP connected disparate networks into one, UCP unifies a fragmented commerce ecosystem under one language. Google officially announced it in January 2025, with Shopify, Etsy, Wayfair, Target, and Walmart participating in co-development. Major payment companies—Visa, Mastercard, PayPal, Stripe, American Express—have already declared support.

## Core Architecture: Layered Design

As Shopify's engineering team puts it, "monolithic protocols crumble under complexity." UCP was inspired by TCP/IP's layered structure, designed to separate concerns and scale independently.

UCP's layered structure breaks into three levels. The base layer, **Shopping Service**, defines core transaction primitives like checkout sessions, line items, totals, and status. Above it sits **Capabilities**, which independently versions major functional areas like Checkout, Orders, and Identity Linking. Finally, **Extensions** compose domain-specific schemas like discounts, shipping, and subscriptions.

This design matters because each layer can evolve independently. For example, if you need a new shipping option, you just add an Extension without touching the core protocol.

## Four Key Participants

The UCP ecosystem has four types of participants, each with clear roles.

**Platform** is an AI agent or app that shops on behalf of the user—services like Google's AI Mode, Gemini, and ChatGPT fit here. The Platform explores the shop's Capabilities, initiates checkout sessions, and provides UI to the user.

**Business** is the online shop selling products or services. In UCP, Business acts as "Merchant of Record," maintaining legal responsibility and customer relationships. Importantly, using UCP doesn't mean shops lose control of customer data.

**Payment Service Provider (PSP)** is a payment processor like Stripe, PayPal, or Adyen. Through UCP's modular payment architecture, multiple PSPs integrate as plugins.

**Credential Provider** is a service like Google Pay or Apple Pay that securely manages and tokenizes the user's payment methods.

## Initial Launch Features: Three Core Capabilities

UCP's initial version focuses on three core capabilities.

**Checkout** handles payment sessions including cart management, dynamic pricing, and tax calculation. It supports both flows requiring human intervention and fully automated flows. For example, if a furniture shop requires shipping date selection, UCP tells the agent in a standardized way "this information is needed."

**Identity Linking** is an OAuth 2.0-based mechanism for the Platform to obtain authority to act on behalf of the user. Essential for personalized shopping experiences like membership benefits and loyalty points.

**Order Management** delivers order lifecycle events (shipped, arrived, returned, etc.) webhook-style. Lets the AI agent answer "where is my order?"

## Payment Architecture: Trust-by-Design

UCP's payment design solves the "N-to-N complexity problem" by separating Payment Instrument (what to accept) from Payment Handler (how to process it).

The core philosophy is "Trust-by-Design." There's existing legal/technical trust between Business and PSP, but the Platform as intermediary doesn't access raw financial information. All authentication is backed by **encrypted user consent evidence**, and non-repudiation is possible through Agent Payments Protocol (AP2)'s Mandate Extension.

Dynamic negotiation is another key feature. Available payment methods vary by cart contents, buyer location, and transaction amount. UCP negotiates both the shop's and user's preferences for each transaction.

## Relationship to Existing Protocols

UCP isn't a standalone standard but designed for compatibility with the existing agent ecosystem.

| Protocol | Role | Relationship to UCP |
| --- | --- | --- |
| MCP (Model Context Protocol) | AI models communicate with external tools/data | One transport layer option in UCP |
| A2A (Agent2Agent) | Standard for agent-to-agent communication | Supported via UCP service bindings |
| AP2 (Agent Payments Protocol) | Agent payment security | Integrated into UCP payment architecture |

Transport is flexible too. REST API is the default, but MCP or A2A can work, letting you choose based on your infrastructure.

## Real Application: Shopping in Google AI Mode

UCP's first real application is Google's AI Mode and Gemini app. When users search for a product in AI Mode, UCP checks the shop's Capabilities and can proceed through checkout.

Payment uses information stored in Google Wallet or PayPal, and the shop remains the Merchant of Record. Starting in the US initially with global expansion planned, features like multi-item carts, loyalty program integration, and shipping tracking are on the roadmap.

## Integration Options for Developers

UCP offers two integration approaches.

**Native Integration** directly integrates checkout logic with Google AI Mode/Gemini. You can leverage UCP's full agentic capabilities and is recommended for most shops.

**Embedded Integration** is an iframe-based solution for select approved shops needing highly customized branding or complex checkout flows.

SDK was first provided as a Python reference implementation, with various language bindings to follow. It's open-source on GitHub so you can directly review the spec and contribute.

## Conclusion

- UCP is the standard protocol between AI agents and online shops—essential infrastructure for the agentic commerce era
- An open-source standard with 20+ global participants like Google, Shopify, Walmart, Visa—not vendor-locked
- Practical tip: If you run a commerce business, register on the waitlist at ucp.dev. If you're a developer, check the spec and sample implementations on GitHub.

## References

- Universal Commerce Protocol Official Documentation (<https://ucp.dev/>)
- Google Developers Blog - Under the Hood: UCP (<https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/>)
- Google for Developers - UCP Guide (<https://developers.google.com/merchant/ucp>)
- Shopify Engineering - Building the Universal Commerce Protocol (<https://shopify.engineering/UCP>)
- GitHub - UCP Specification (<https://github.com/Universal-Commerce-Protocol/ucp>)
- Google Blog - Agentic Commerce AI Tools (<https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/>)
