---
title: "Network Protocols: Role of ARP, ICMP, IGMP"
date: 2024-05-25T14:38:18+09:00
slug: "53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할"
original_url: "https://memoryhub.tistory.com/53"
tistory_id: 53
draft: false
categories: ["Dev Concepts"]
tags: ["Info Processing Cert"]
cover:
  image: "/images/53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할/img.png"
  relative: false
  hidden: false
---

- ARP (Address Resolution Protocol)
  - Hardware address connection protocol
  - Protocol used to map IP addresses to physical network addresses
  - Operation principle:
    1. Used when two IP devices on the same network segment communicate
    2. Uses lower layer protocols and addressing methods defined according to the specific medium used by the network

  ![](/images/53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할/img.png)

  Example
  - Communication in Ethernet environment:
    1. When IP system communicates, the local device first confirms the hardware address of other devices connected to the network it belongs to
    2. ARP provides service to convert IP addresses to corresponding hardware (MAC) addresses

![](/images/53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할/img_1.png)

![](/images/53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할/img_2.png)

## ICMP

- Overview
  - IP does not guarantee reliability
  - Protocol to handle errors from network failures or relay routers
  - Main functions:
  - Detects error information and transmits message to sender
  - Network problem diagnosis and reporting
  - Usage example: ping
  - Transmits ICMP Echo Request message
  - Destination system responds with ICMP Echo Reply message
  - Measures response time to check network connection status

![](/images/53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할/img_3.png)

![](/images/53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할/img_4.png)

The ping tool transmits ICMP Echo Request messages and measures the time to receive ICMP Echo Reply messages from the destination system to check network connection.

```
ping www.yahoo.co.kr
tracert 59.5.67.254
```

ICMP Message Format

![](/images/53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할/img_5.png)

## IGMP

- Overview
  - Protocol for multicast group management
  - Communication method comparison:
    1. Unicast: One-to-one communication
    2. Broadcast: One-to-all-hosts communication
    3. Multicast: One-to-specific-group communication
  - IGMP characteristics:
  - Transmits packets using group addresses
  - Only hosts in the designated group receive data, other network devices ignore it
  - Enables efficient group communication avoiding broadcast limitations
  - Useful for applications that need to send data simultaneously from one host to multiple destinations

![](/images/53-네트워크-프로토콜_-ARP-ICMP-IGMP-역할/img_6.png)

## Source

<https://spider-web.tistory.com/12>
