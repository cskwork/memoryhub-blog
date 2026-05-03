---
title: "Universal Commerce Protocol, AI가 결제까지 해주는 시대의 필수 인프라"
date: 2026-01-13T21:03:19+09:00
slug: "965-Universal-Commerce-Protocol-AI가-결제까지-해주는-시대의-필수-인프라"
original_url: "https://memoryhub.tistory.com/965"
tistory_id: 965
draft: false
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
║         "AI가 쇼핑을 대신하는 시대의 공용어"                   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

"AI야, 10만원 이하 무선 이어폰 추천해줘." 여기까지는 이미 익숙합니다. 그런데 "추천받은 제품 바로 구매해줘"라고 했을 때, AI가 정말로 결제까지 완료한다면 어떨까요? 문제는 세상에 수백만 개의 쇼핑몰이 있고, 각자 다른 시스템을 쓴다는 점입니다.

**Universal Commerce Protocol(UCP)은 이 혼란 속에서 AI 에이전트가 어떤 쇼핑몰과도 대화할 수 있게 해주는 '공용어'입니다.**

결론부터 말하면, UCP는 Google과 Shopify가 공동 개발하고 20개 이상의 글로벌 기업이 지지하는 오픈소스 표준으로, AI 에이전트 시대의 커머스 인프라를 정의합니다.

## 배경

2025년 들어 "에이전틱 커머스(Agentic Commerce)"라는 용어가 빠르게 확산되고 있습니다. 단순히 제품을 추천하는 것을 넘어, AI 에이전트가 사용자를 대신해 상품 검색부터 장바구니 담기, 결제까지 전 과정을 처리하는 개념입니다.

하지만 여기서 근본적인 문제가 발생합니다. Shopify 기반 쇼핑몰, 자체 구축 사이트, 대형 마켓플레이스 모두 다른 API와 결제 시스템을 사용합니다. AI 에이전트가 각 쇼핑몰마다 별도 연동을 구축해야 한다면, N개의 에이전트와 M개의 쇼핑몰 사이에 N×M개의 커스텀 통합이 필요해집니다.

> UCP는 AI 에이전트, 쇼핑몰, 결제 서비스 사이의 표준화된 통신 규약으로, 커스텀 통합 없이 상호운용성을 보장하는 오픈소스 프로토콜입니다.

TCP/IP가 서로 다른 네트워크들을 하나로 연결했듯이, UCP는 파편화된 커머스 생태계를 하나의 언어로 통합합니다. 2025년 1월 Google이 공식 발표했으며, Shopify, Etsy, Wayfair, Target, Walmart이 공동 개발에 참여했습니다. Visa, Mastercard, PayPal, Stripe, American Express 등 주요 결제 기업들도 이미 지지를 선언한 상태입니다.

## 핵심 아키텍처: 계층화된 설계

Shopify 엔지니어링 팀의 표현을 빌리자면, "단일 구조의 프로토콜은 복잡성에 무너진다"고 합니다. UCP는 TCP/IP의 계층 구조에서 영감을 받아, 책임을 분리하고 독립적으로 확장 가능하게 설계되었습니다.

UCP의 계층 구조는 크게 세 단계로 나뉩니다. 가장 기본이 되는 **Shopping Service**는 체크아웃 세션, 라인 아이템, 총액, 상태 등 핵심 거래 원시(primitive)를 정의합니다. 그 위에 **Capabilities**가 위치하는데, 이는 Checkout, Orders, Identity Linking 등 주요 기능 영역을 독립적으로 버전 관리합니다. 마지막으로 **Extensions**는 할인, 배송, 구독 등 도메인별 스키마를 조합(composition) 방식으로 확장합니다.

이 설계가 중요한 이유는 각 층위가 독립적으로 진화할 수 있기 때문입니다. 예를 들어 새로운 배송 옵션이 필요하면 코어 프로토콜을 건드리지 않고 Extension만 추가하면 됩니다.

## 네 가지 핵심 참여자

UCP 생태계에는 네 종류의 참여자가 있으며, 각자 명확한 역할을 담당합니다.

**Platform**은 사용자를 대신해 쇼핑을 수행하는 AI 에이전트나 앱입니다. Google의 AI Mode, Gemini, ChatGPT 같은 서비스가 여기에 해당합니다. Platform은 쇼핑몰의 Capability를 탐색하고, 체크아웃 세션을 시작하며, 사용자에게 UI를 제공합니다.

**Business**는 상품이나 서비스를 판매하는 쇼핑몰입니다. UCP에서 Business는 "Merchant of Record"로서 거래에 대한 법적 책임과 고객 관계를 유지합니다. 중요한 점은 UCP를 사용해도 쇼핑몰이 고객 데이터 통제권을 잃지 않는다는 것입니다.

**Payment Service Provider(PSP)**는 Stripe, PayPal, Adyen 같은 결제 처리 업체입니다. UCP의 모듈식 결제 아키텍처를 통해 여러 PSP가 플러그인 방식으로 연동됩니다.

**Credential Provider**는 Google Pay, Apple Pay 같이 사용자의 결제 수단을 안전하게 관리하고 토큰화하는 서비스입니다.

## 초기 출시 기능: 세 가지 핵심 Capability

UCP의 초기 버전은 세 가지 핵심 기능에 집중합니다.

**Checkout**은 장바구니 관리, 동적 가격 책정, 세금 계산 등을 포함한 결제 세션을 처리합니다. 사람의 개입이 필요한 흐름과 완전 자동화된 흐름 모두 지원합니다. 예를 들어 가구 쇼핑몰에서 배송 날짜 선택이 필수라면, UCP는 에이전트에게 "이 정보가 필요하다"고 표준화된 방식으로 알려줍니다.

**Identity Linking**은 OAuth 2.0 기반으로 Platform이 사용자를 대신해 행동할 권한을 얻는 메커니즘입니다. 멤버십 혜택 적용, 로열티 포인트 연동 같은 개인화된 쇼핑 경험에 필수적입니다.

**Order Management**는 주문 생명주기 이벤트(배송됨, 도착함, 반품됨 등)를 웹훅 기반으로 전달합니다. AI 에이전트가 "내 주문 어디까지 왔어?"라는 질문에 답할 수 있게 해줍니다.

## 결제 아키텍처: Trust-by-Design

UCP의 결제 설계는 "N-to-N 복잡성 문제"를 해결하기 위해 Payment Instrument(무엇을 받을 것인가)와 Payment Handler(어떻게 처리할 것인가)를 분리합니다.

핵심 철학은 "Trust-by-Design"입니다. Business와 PSP 사이에는 기존의 법적/기술적 신뢰 관계가 있지만, Platform은 중개자로서 원시 금융 정보에 접근하지 않습니다. 모든 인증은 **암호화된 사용자 동의 증명**으로 뒷받침되며, Agent Payments Protocol(AP2)의 Mandate Extension을 통해 부인 방지(non-repudiation)가 가능합니다.

동적 협상도 중요한 특징입니다. 장바구니 내용, 구매자 지역, 거래 금액에 따라 사용 가능한 결제 수단이 달라질 수 있는데, UCP는 매 거래마다 쇼핑몰과 사용자 양측의 선호를 협상합니다.

## 기존 프로토콜과의 관계

UCP는 독자적인 표준이 아니라, 기존 에이전트 생태계와 호환되도록 설계되었습니다.

| 프로토콜 | 역할 | UCP와의 관계 |
| --- | --- | --- |
| MCP (Model Context Protocol) | AI 모델이 외부 도구/데이터와 통신 | UCP의 전송 계층 옵션 중 하나 |
| A2A (Agent2Agent) | AI 에이전트 간 통신 표준 | UCP 서비스 바인딩으로 지원 |
| AP2 (Agent Payments Protocol) | 에이전트 결제 보안 | UCP 결제 아키텍처에 통합 |

전송 방식도 유연합니다. REST API가 기본이지만, MCP나 A2A로도 통신할 수 있어 기존 인프라에 맞춰 선택이 가능합니다.

## 실제 적용: Google AI Mode에서의 쇼핑

UCP의 첫 번째 실제 적용 사례는 Google의 AI Mode와 Gemini 앱입니다. 사용자가 AI Mode에서 제품을 검색하면, UCP를 통해 해당 쇼핑몰의 Capability를 확인하고 체크아웃까지 진행할 수 있습니다.

결제는 Google Wallet에 저장된 정보나 PayPal을 사용하며, 쇼핑몰은 여전히 Merchant of Record로서 거래의 주체가 됩니다. 초기에는 미국에서 시작하여 글로벌로 확대될 예정이고, 멀티 아이템 카트, 로열티 프로그램 연동, 배송 추적 같은 기능이 로드맵에 포함되어 있습니다.

## 개발자를 위한 통합 옵션

UCP는 두 가지 통합 방식을 제공합니다.

**Native Integration**은 체크아웃 로직을 Google AI Mode/Gemini와 직접 통합하는 방식입니다. UCP의 전체 에이전틱 기능을 활용할 수 있으며, 대부분의 쇼핑몰에 권장됩니다.

**Embedded Integration**은 iframe 기반 솔루션으로, 고도로 맞춤화된 브랜딩이나 복잡한 체크아웃 흐름이 필요한 특정 승인 쇼핑몰을 위한 옵션입니다.

SDK는 Python 레퍼런스 구현이 먼저 제공되었으며, 다양한 언어 바인딩이 지원될 예정입니다. GitHub에서 오픈소스로 공개되어 있어 스펙을 직접 확인하고 기여할 수 있습니다.

## 마치며

- UCP는 AI 에이전트와 쇼핑몰 사이의 표준 프로토콜로, 에이전틱 커머스 시대의 필수 인프라입니다.
- Google, Shopify, Walmart, Visa 등 20개 이상 글로벌 기업이 참여하는 오픈소스 표준으로, 특정 벤더에 종속되지 않습니다.
- 실전 팁: 커머스 비즈니스를 운영한다면 ucp.dev에서 대기자 명단에 등록하고, 개발자라면 GitHub 레포지토리에서 스펙과 샘플 구현을 확인해보세요.

## 참고자료

- Universal Commerce Protocol 공식 문서 (<https://ucp.dev/>)
- Google Developers Blog - Under the Hood: UCP (<https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/>)
- Google for Developers - UCP Guide (<https://developers.google.com/merchant/ucp>)
- Shopify Engineering - Building the Universal Commerce Protocol (<https://shopify.engineering/UCP>)
- GitHub - UCP Specification (<https://github.com/Universal-Commerce-Protocol/ucp>)
- Google Blog - Agentic Commerce AI Tools (<https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/>)
