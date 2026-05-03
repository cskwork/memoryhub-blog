---
title: "? Hermes Agent, 왜 다들 주목할까? 학습하는 에이전트 핵심 정리"
date: 2026-04-07T07:41:31+09:00
slug: "1051-Hermes-Agent-왜-다들-주목할까-학습하는-에이전트-핵심-정리"
original_url: "https://memoryhub.tistory.com/1051"
tistory_id: 1051
draft: false
---

```
 ┌──────────────────────────────────────┐
 │          HERMES AGENT                │
 │                                      │
 │  Chat  →  Tool Use  →  Memory        │
 │    │         │           │           │
 │    └────→  Skills  ←─────┘           │
 │                │                     │
 │      CLI / Telegram / Slack / ACP    │
 │                │                     │
 │        Docker / SSH / Modal / VPS    │
 └──────────────────────────────────────┘
```

## 인트로

요즘 오픈소스 에이전트 저장소를 보면 “툴 호출 된다”, “채팅 된다” 수준의 설명은 정말 많습니다.  
그런데 실제로 오래 쓰려면 기억이 남는지, 채널을 바꿔도 이어지는지, 운영할 때 안전한지가 더 중요하더라고요.  
Hermes Agent는 바로 그 지점을 전면에 내세운 프로젝트라서 한 번 보면 왜 화제가 되는지 구조가 바로 보입니다.  
이 글에서는 README를 길게 읽지 않아도, Hermes Agent를 왜 사용해 봐야 하는지와

어떻게 시작하면 되는지 한 번에 정리해보겠습니다.

## 한줄요약

Hermes Agent는 단순한 채팅형 LLM 래퍼보다, 기억·스킬·멀티채널·실행 격리까지 묶어

운영형으로 설계된 오픈소스 AI 에이전트에 가깝습니다. ([GitHub](https://github.com/nousresearch/hermes-agent "GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub"))

## 배경

Hermes Agent를 볼 때 먼저 기억할 포인트는 “기능 몇 개가 많은 프로젝트”가 아니라, 에이전트를 실제로 계속 굴리기 위한 런타임에 가깝다는 점입니다. 공식 저장소는 이 프로젝트를 self-improving AI agent로 소개하고,

2026년 4월 7일 기준 공개 저장소에서 약 27.9k stars와 3.7k forks를 기록하고 있습니다.

또 패키지 메타데이터 기준 Python 3.11 이상을 요구하고 MIT 라이선스를 사용합니다. ([GitHub](https://github.com/nousresearch/hermes-agent "GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub"))

- **학습 루프를 전면에 둔 구조**: 공식 README는 경험에서 스킬을 만들고, 사용 중 개선하고, 과거 대화를 검색하며, 세션을 넘어 사용자 모델을 깊게 만든다고 설명합니다. 여기서 핵심은 “한 번 답하고 끝나는 봇”이 아니라 “쓸수록 맥락이 누적되는 구조”라는 점입니다. ([GitHub](https://github.com/nousresearch/hermes-agent "GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub"))
- **모델 종속성이 낮은 구성**: Quickstart 문서에는 Nous Portal, OpenAI, Anthropic, OpenRouter, Hugging Face, GitHub Copilot, Custom Endpoint 등 다양한 공급자를 선택할 수 있다고 나옵니다. 즉 특정 모델 하나에 묶이는 느낌보다, 에이전트 런타임 자체를 중심에 두고 공급자를 갈아끼우는 방향입니다. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart "Quickstart | Hermes Agent"))
- **채널 확장성이 큼**: README와 아키텍처 문서 기준으로 CLI와 메시징 게이트웨이를 모두 지원하고, 아키텍처 쪽에서는 telegram, discord, slack, whatsapp, signal, matrix, mattermost, email, sms, dingtalk, feishu, wecom, homeassistant, webhook까지 14개 어댑터가 보입니다. ([GitHub](https://github.com/nousresearch/hermes-agent "GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub"))
- **보안과 격리를 꽤 진지하게 다룸**: 승인 모드, 위험 명령 감지, Docker 격리, 환경 변수 패스스루 제한 같은 운영 문서가 별도로 정리되어 있습니다. 생산 환경에서는 Docker, Modal, Daytona 같은 격리형 백엔드를 권장한다는 점도 눈에 띕니다. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/security "Security | Hermes Agent"))
- **업데이트 속도가 빠름**: 최근 릴리스만 봐도 2026년 3월 28일 v0.5.0, 3월 30일 v0.6.0, 4월 3일 v0.7.0이 연달아 나왔습니다. 최근 버전에서는 Hugging Face 공급자, 멀티 프로필, MCP server mode, Docker 컨테이너, 플러그형 메모리 provider 같은 기능이 빠르게 추가됐습니다. ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.5.0.md "hermes-agent/RELEASE_v0.5.0.md at main · NousResearch/hermes-agent · GitHub"))

## 핵심

> Hermes Agent는 대화형 LLM 인터페이스 위에 도구 실행, 장기 기억, 스킬 시스템, 메시징 게이트웨이, 실행 환경 격리를 한 번에 얹은 오픈소스 에이전트 런타임입니다.

> 잘 답변하는 챗봇을 만드는 프로젝트라기보다, 여러 채널에서 계속 일하고 사용자 맥락을 축적하는 “운영 가능한 에이전트”를 만드는 프로젝트에 더 가깝습니다.

Hermes Agent가 흥미로운 이유는 메모리와 스킬을 별도 옵션이 아니라 중심축으로 둔다는 점입니다.

README는 과거 대화 검색, 메모리 유지, 스킬 생성과 개선을 핵심 특성으로 설명하고 있고,

문서에서도 Skills System, Memory, Context Files, Cron Scheduling이 나란히 큰 축으로 배치되어 있습니다.

그래서 이 프로젝트는 “웹 검색도 되는 챗봇”보다 “작업 습관을 점점 구조화하는 비서” 쪽에 더 가깝습니다. ([GitHub](https://github.com/nousresearch/hermes-agent "GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub"))

구조도도 꽤 명확합니다. 아키텍처 문서에서는 CLI, Gateway, ACP, Batch Runner, API Server, Python Library 같은 여러 진입점을 하나의 `AIAgent` 중심으로 묶고 있습니다. 또 프롬프트 조립 시 personality, memory, skills, context files가 함께 반영되며, 프로필마다 config, memory, sessions, gateway PID가 분리됩니다.

이 설계 덕분에 개인용 실험부터 팀 단위 분리 운영까지 자연스럽게 이어집니다. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture "Architecture | Hermes Agent"))

운영 관점에서 특히 눈에 띄는 부분은 보안입니다. 승인 시스템은 `manual`, `smart`, `off` 모드를 두고 위험 명령을 별도로 감지합니다. 반대로 Docker 백엔드에서는 컨테이너 자체를 경계로 삼아 보안을 강화하고,

프로덕션 게이트웨이에서는 host 대신 격리형 백엔드를 권장합니다.

또 FAQ 문서 기준으로 대화·메모리·스킬은 기본적으로 로컬 `~/.hermes/` 아래에 저장되고,

텔레메트리를 수집하지 않는다고 안내합니다. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/security "Security | Hermes Agent"))

## 실습

### 설치부터 시작하기

언어/버전은 `Bash`, 그리고 패키지 요구사항은 `Python >= 3.11`입니다. 가장 빠른 시작 경로는 공식 원라인 설치 스크립트이며, Linux, macOS, WSL2를 기준으로 안내됩니다. Windows는 네이티브보다 WSL2 사용이 공식 문서 기준 경로입니다. ([GitHub](https://github.com/nousresearch/hermes-agent "GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub"))

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
```

### 모델과 도구 연결하기

설치 후 바로 중요한 명령은 아래 세 가지입니다. 공급자는 대화형으로 고를 수 있고, 도구 활성화 범위도 별도로 설정할 수 있습니다.

```
hermes model
hermes tools
hermes setup
```

### 첫 대화 열기

가장 기본 진입점은 CLI입니다. 공식 Quickstart는 `hermes` 실행 후 바로 대화를 시작하고, `/model`, `/tools`, `/help`, `/save` 같은 명령으로 확장하는 흐름을 안내합니다.

```
hermes
```

실행 결과 텍스트 대체 예시는 이런 느낌입니다.

```
[텍스트 대체 스냅샷]
- 상단 웰컴 배너 표시
- 현재 선택된 provider / model 표시
- 사용 가능한 tools / skills 표시
- 입력 프롬프트가 열리고 바로 대화 시작
```

### 메시징 채널로 넓히기

Hermes Agent의 재미는 여기부터입니다. CLI에서 끝내지 않고 게이트웨이를 열면 Telegram, Discord, Slack 등으로 같은 에이전트를 이어서 쓸 수 있습니다. README 기준 기본 흐름은 아래와 같습니다.

```
hermes gateway setup
hermes gateway start
```

### 운영 전 꼭 챙길 점

로컬 백엔드는 기본적으로 호스트 권한 위에서 실행되므로, 실제 운영이나 자동화는 Docker 같은 격리형 백엔드로 바꾸는 편이 안전합니다. Quickstart와 Security 문서도 Docker, SSH, Modal, Daytona 같은 분리 환경을 권장합니다. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart "Quickstart | Hermes Agent"))

```
hermes config set terminal.backend docker
```

## 모범사례/패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| 빠른 체험형: CLI 단독 사용 | 설치 후 바로 대화가 가능해 진입장벽이 낮습니다. | 로컬 백엔드는 호스트 환경을 그대로 쓰므로 실험 범위를 작게 잡는 편이 좋습니다. |
| 운영 분리형: Docker/원격 백엔드 | 명령 실행을 격리해 운영 안정성과 보안성이 좋아집니다. | 이미지, 자원 제한, 환경 변수 전달 정책을 함께 설계해야 합니다. |
| 멀티채널형: Gateway 연결 | Telegram·Discord·Slack 등으로 접점을 넓혀 실제 사용성이 올라갑니다. | 채널별 권한, 승인 흐름, 응답 정책을 먼저 정해야 관리가 편합니다. |
| 확장형: MCP/ACP/Profiles 활용 | 에디터 연동, 외부 MCP 도구 연결, 프로필 분리 운영까지 확장할 수 있습니다. | 기능이 많아질수록 프로필별 설정과 도구 노출 범위를 분리해야 합니다. |

위 비교는 공식 Quickstart, 아키텍처, 보안 문서와 최근 릴리스 노트를 바탕으로 정리했습니다. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart "Quickstart | Hermes Agent"))

## 마치며

Hermes Agent는 “요즘 뜨는 에이전트 저장소 하나”로 보기엔 구조가 꽤 완성형입니다.  
특히 기억, 스킬, 게이트웨이, 격리 실행까지 한 덩어리로 묶었다는 점이 이 프로젝트의 진짜 포인트입니다.  
가볍게 체험해도 재미있지만, 운영 관점에서 보면 더 진가가 보이는 저장소라고 정리할 수 있겠습니다.

**데모는 CLI로, 운영은 격리형 백엔드와 프로필 분리부터 시작하면 훨씬 깔끔합니다.**

## 참고자료

- GitHub 저장소 메인 페이지 및 README 요약 정보 ([GitHub](https://github.com/nousresearch/hermes-agent "GitHub - NousResearch/hermes-agent: The agent that grows with you · GitHub"))
- Hermes Agent Quickstart 문서 ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart "Quickstart | Hermes Agent"))
- Hermes Agent Architecture 문서 ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/developer-guide/architecture "Architecture | Hermes Agent"))
- Hermes Agent Security 문서 ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/security "Security | Hermes Agent"))
- Hermes Agent FAQ 문서 ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/reference/faq/?utm_source=chatgpt.com "FAQ & Troubleshooting | Hermes Agent"))
- Hermes Agent v0.5.0 릴리스 노트 ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.5.0.md "hermes-agent/RELEASE_v0.5.0.md at main · NousResearch/hermes-agent · GitHub"))
- Hermes Agent v0.6.0 릴리스 노트 ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.6.0.md "hermes-agent/RELEASE_v0.6.0.md at main · NousResearch/hermes-agent · GitHub"))
- Hermes Agent v0.7.0 릴리스 노트 ([GitHub](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.7.0.md "hermes-agent/RELEASE_v0.7.0.md at main · NousResearch/hermes-agent · GitHub"))
