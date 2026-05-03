---
title: "? OpenClaw 리뷰: 3주 만에 '보안 쓰레기장'이 된 10만 스타 AI 비서"
date: 2026-02-04T02:26:18+09:00
slug: "1001-OpenClaw-리뷰-3주-만에-보안-쓰레기장-이-된-10만-스타-AI-비서"
original_url: "https://memoryhub.tistory.com/1001"
tistory_id: 1001
draft: false
---

```
  ╔═══════════════════════════════════════════════════════════╗
  ║                                                           ║
  ║     ██████╗ ██████╗ ███████╗███╗   ██╗ ██████╗██╗       ║
  ║    ██╔═══██╗██╔══██╗██╔════╝████╗  ██║██╔════╝██║       ║
  ║    ██║   ██║██████╔╝█████╗  ██╔██╗ ██║██║     ██║       ║
  ║    ██║   ██║██╔═══╝ ██╔══╝  ██║╚██╗██║██║     ██║       ║
  ║    ╚██████╔╝██║     ███████╗██║ ╚████║╚██████╗███████╗  ║
  ║     ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═══╝ ╚═════╝╚══════╝  ║
  ║                     A W                                  ║
  ║               ? AI Assistant ?                         ║
  ║                                                           ║
  ║        [ The Good, The Bad, and The Malware ]            ║
  ║                                                           ║
  ╚═══════════════════════════════════════════════════════════╝
```

"24시간 일하는 무료 AI 비서를 갖고 싶다"는 생각, 한 번쯤 해보셨을 겁니다. OpenClaw는 바로 그 꿈을 현실로 만들어 줄 것처럼 보였습니다. 텔레그램으로 명령하면 컴퓨터가 알아서 일하고, 내가 잠든 사이 이메일을 정리해주는 AI 비서.

그런데 왜 구글 클라우드 보안 부사장은 **"절대 설치하지 말라"**고 경고했을까요?

**한줄요약:** 결론부터 말하면, OpenClaw는 개인 AI 비서의 미래를 보여주지만,

월 30~75만원의 API 비용과 심각한 보안 취약점으로 인해 현재 일반 사용자에게는 권장하기 어렵습니다.

## 배경

2025년 11월, iOS 개발자 피터 스타인버거(Peter Steinberger)가 주말 프로젝트로 시작한 Clawdbot이 2026년 초 기술 업계를 뒤흔들었습니다. GitHub 스타 10만 개를 3주 만에 돌파했고, 맥 미니가 품절되는 현상까지 일어났습니다.

하지만 폭발적인 인기만큼이나 빠르게 문제점이 드러났습니다.

> OpenClaw는 사용자 컴퓨터에서 실행되며 메시징 앱을 통해 제어하는 오픈소스 자율 AI 에이전트입니다.

영화 아이언맨의 자비스를 떠올리면 이해하기 쉽습니다. "자비스, 오늘 일정 정리해줘"라고 말하면 AI가 알아서 처리하는 것처럼, OpenClaw는 텔레그램이나 왓츠앱으로 명령을 내리면 실제로 컴퓨터를 조작해 작업을 수행합니다.

기존 ChatGPT나 Claude가 "대화만" 하는 것과 달리,

OpenClaw는 "직접 행동"합니다. 파일 정리, 이메일 발송, 코드 실행까지 가능합니다.

문제는 이 강력한 권한이 양날의 검이라는 점입니다.

## 이름이 세 번 바뀐 이유

OpenClaw의 이름 변천사 자체가 이 프로젝트의 혼란스러운 상황을 보여줍니다.

| 시기 | 이름 | 변경 이유 |
| --- | --- | --- |
| 2025년 11월 | Clawdbot | 최초 출시 |
| 2026년 1월 중순 | Moltbot | Anthropic의 상표권 요청(Claude와 혼동) |
| 2026년 1월 말 | OpenClaw | 발음 불편 및 브랜드 정리 |

"Clawd"가 "Claude"와 너무 비슷하다는 이유로 Anthropic에서 이의를 제기했고, 급하게 Moltbot으로 변경했습니다.

"Molt"는 바닷가재가 껍질을 벗는다는 의미였지만, 발음이 어색했습니다. 결국 OpenClaw로 최종 결정되었습니다.

**여기서 보안 문제가 시작됩니다.** 이름이 바뀌는 혼란 속에서 스캐머들이 등록되지 않은 도메인과 소셜 미디어 계정을 선점했고,

가짜 악성 확장 프로그램이 등장했습니다.

## 장점: 왜 개발자들이 열광했는가

OpenClaw가 주목받은 이유는 명확합니다.

첫째, 완전한 오픈소스입니다. MIT 라이선스로 누구나 자유롭게 수정하고 배포할 수 있습니다. 월 구독료 없이 직접 운영할 수 있다는 점이 매력적입니다.

둘째, 메시징 플랫폼 통합입니다. 별도 앱 설치 없이 텔레그램, 왓츠앱, 디스코드, 슬랙, 심지어 카카오톡까지 기존에 사용하던 메신저로 AI를 제어할 수 있습니다.

셋째, 진짜 자동화가 가능합니다. "캘린더 확인하고 다음 주 치과 예약해줘"라고 메시지를 보내면, 실제로 캘린더를 확인하고 예약까지 시도합니다. 여러 앱을 오가며 작업하던 것을 하나의 대화로 처리할 수 있습니다.

GeekNews의 한 사용자는 이렇게 평가했습니다.

> "동적으로 스킬을 생성할 수 있고, 반복/단발성 작업을 예약할 수 있으며, 원격 메시징이 가능한 지속형 에이전트라 진짜 비서처럼 느껴집니다."

## 단점 1: API 비용 폭탄

OpenClaw 자체는 무료입니다. 하지만 이를 구동하는 AI 모델은 유료입니다.

MacStories의 Federico Viticci는 첫 달에 1억 8천만 토큰을 소비했습니다. Claude Sonnet 요금 기준 약 480만원입니다. 또 다른 사용자는 자동화 루프가 폭주하면서 **하루에 200달러(약 27만원)**를 써버렸습니다.

문제의 핵심은 OpenClaw의 작동 방식에 있습니다.

작업을 완료할 때까지 시도-실패-수정-재시도를 반복하는데, 매 시도마다 토큰이 소비됩니다.

The Register에 따르면 한 개발자는 단순히 시간을 확인하는 "heartbeat" 작업이 30분마다 12만 토큰을 소비해 하룻밤에 20달러가 청구됐습니다.

## 단점 2: 보안 악몽

2026년 1월 27일, 보안 연구 기업 Aikido가 VS Code 마켓플레이스에서 "ClawdBot Agent"라는 악성 확장 프로그램을 발견했습니다.

이 가짜 확장 프로그램은 VS Code 시작 시 자동 실행되어 악성 코드를 다운로드했습니다.

결과적으로 공격자가 개발자 컴퓨터에 원격 접속할 수 있게 만들었습니다.

**핵심은 OpenClaw에 공식 VS Code 확장 프로그램이 존재하지 않는다는 점입니다.** 공격자들은 단순히 프로젝트의 인기와 공식 도구의 부재를 악용했습니다.

그리고 이것은 시작에 불과했습니다.

2026년 2월 3일 기준 The Register가 정리한 보안 이슈 목록입니다.

| 취약점 | 심각도 | 상태 |
| --- | --- | --- |
| CVE-2026-25253: 원클릭 원격 코드 실행 | CVSS 8.8 (높음) | 패치 완료 |
| ClawHub 악성 스킬 341개 발견 | 높음 | 대부분 미제거 |
| 커맨드 인젝션 취약점 2건 | 높음 | 패치 완료 |
| Moltbook 데이터베이스 노출 | 중간 | 조치 중 |

보안 연구원 Mav Levin이 발견한 원클릭 RCE 취약점은 특히 심각했습니다.

피해자가 악성 웹페이지를 단 한 번 방문하면 "밀리초" 단위로 공격이 완료됩니다.

WebSocket 연결의 origin 헤더를 검증하지 않아 발생한 문제였습니다.

구글 클라우드 보안 부사장 Heather Adkins는 공개적으로 경고했습니다.

> "OpenClaw를 실행하지 마세요. 이것은 AI 개인 비서로 위장한 정보 탈취 악성코드입니다."

또한 SecurityAffairs에 따르면 2026년 1월 27일부터 2월 2일 사이에 **400개 이상의 악성 스킬**이 ClawHub과 GitHub에 업로드되었습니다. 암호화폐 거래 자동화 도구로 위장했지만,

실제로는 Windows와 macOS에서 비밀번호와 암호화폐 키를 탈취하는 악성코드였습니다.

## 안전한 대안은 무엇인가

Reddit과 Hacker News 커뮤니티의 공통된 의견은 의외로 단순합니다.

**"더 간단한 도구가 99%의 사용 사례를 커버한다."**

| 대안 | 장점 | 적합한 사용자 |
| --- | --- | --- |
| Claude Code + 텔레그램 연동 | 복잡한 설정 불필요, 안정적 | 개발자, 실무자 |
| Kimi K2.5 (로컬 모델) | API 비용 제로, 데이터 로컬 유지 | 프라이버시 중시 사용자 |
| 기존 자동화 도구(Zapier, n8n) | 검증된 보안, 풍부한 연동 | 비개발자 |

## 지금 설치해도 될까?

현재 시점에서 대부분의 사용자에게 OpenClaw를 권장하기 어렵습니다.

기술적 비전은 인상적입니다. 메시징 앱으로 제어하는 개인 AI 비서라는 개념은 분명히 미래지향적입니다.

하지만 현재 위험이 이점을 압도합니다.

**만약 그래도 시도하고 싶다면** 다음 조건을 갖춰야 합니다.

1. 보안 관련 지식이 있고 위험을 이해하는 개발자
2. API 키에 하드 리밋을 설정할 수 있는 사람
3. 테스트용 별도 기기가 있는 경우(메인 PC 사용 금지)
4. 공식 GitHub 저장소에서만 설치하고, ClawHub 스킬은 철저히 검증

프로젝트 메인테이너들은 보안 문제를 인정하고 개선 작업 중입니다. 6개월 후에 다시 확인해 보는 것이 현명할 수 있습니다.

## 마치며

- OpenClaw는 "직접 행동하는 AI 비서"라는 혁신적 개념을 제시했지만, 3주 만에 보안 취약점과 악성코드 유포로 "보안 쓰레기장"이라는 평가를 받게 됐습니다.
- API 비용 월 40~100만원, 원클릭 RCE 취약점, 400개 이상의 악성 스킬 등 현재 위험 요소가 이점을 압도합니다.
- 실전 팁: OpenClaw 대신 Claude Code나 검증된 자동화 도구로 시작하고, 6개월 후 보안이 안정화되면 재평가해 보세요.

## 참고자료

- OpenClaw - Wikipedia (<https://en.wikipedia.org/wiki/OpenClaw>)
- OpenClaw Bug Enables One-Click Remote Code Execution via Malicious Link - The Hacker News (<https://thehackernews.com/2026/02/openclaw-bug-enables-one-click-remote.html>)
- DIY AI bot farm OpenClaw is a security 'dumpster fire' - The Register (<https://www.theregister.com/2026/02/03/openclaw_security_problems/>)
- MoltBot Skills exploited to distribute 400+ malware packages - SecurityAffairs (<https://securityaffairs.com/187562/malware/moltbot-skills-exploited-to-distribute-400-malware-packages-in-days.html>)
- From Clawdbot to OpenClaw: When Automation Becomes a Digital Backdoor - Vectra AI (<https://www.vectra.ai/blog/clawdbot-to-moltbot-to-openclaw-when-automation-becomes-a-digital-backdoor>)
- OpenClaw - 모든 OS와 플랫폼에서 작동하는 개인용 AI 비서 - GeekNews (<https://news.hada.io/topic?id=26122>)
- OpenClaw (Formerly Clawdbot): The Good, The Bad, and The Malware - Everyday AI (<https://everydayaiblog.com/openclaw-moltbot-ai-assistant-review/>)
