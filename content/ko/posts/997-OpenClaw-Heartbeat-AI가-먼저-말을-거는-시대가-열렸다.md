---
title: "? OpenClaw Heartbeat, AI가 먼저 말을 거는 시대가 열렸다"
date: 2026-01-31T22:10:16+09:00
slug: "997-OpenClaw-Heartbeat-AI가-먼저-말을-거는-시대가-열렸다"
original_url: "https://memoryhub.tistory.com/997"
tistory_id: 997
draft: false
---

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     ?  O P E N C L A W   H E A R T B E A T  ?           ║
    ║                                                           ║
    ║        ┌─────────────────────────────────────┐            ║
    ║        │  ░░▓▓░░  AI가 먼저 말을 건다  ░░▓▓░░ │            ║
    ║        └─────────────────────────────────────┘            ║
    ║                                                           ║
    ║          ? ← 30분마다 깨어나는 AI 비서                    ║
    ║                                                           ║
    ║     "Context is Consciousness" - Crustafarianism          ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
```

지금까지 AI에게 뭔가를 시키려면 항상 우리가 먼저 말을 걸어야 했습니다. "이메일 정리해줘", "일정 확인해줘"라고 명령하면 그제야 움직이는 도구.

하지만 2026년 1월, GitHub 스타 10만 개를 돌파하며 폭발적으로 성장한 오픈소스 프로젝트 OpenClaw는 이 공식을 뒤집었습니다. **Heartbeat 기능을 통해 AI가 30분마다 스스로 깨어나 "지금 급한 일 있어?"라고 먼저 물어봅니다.**

**결론부터 말하면,**

**OpenClaw Heartbeat는 AI를 "대답하는 도구"에서 "먼저 행동하는 동료"로 바꾸는 패러다임 전환의 핵심 기술입니다.**

## 배경

영화 Her에서 인공지능 사만다는 주인공 테오도르가 요청하지 않아도 그의 이메일을 정리하고, 작업물을 읽고, 필요한 것을 미리 챙겼습니다. 아이언맨의 자비스도 토니 스타크가 명령하기 전에 문제를 감지하고 알려주는 능동적 존재였습니다.

이런 SF 속 AI 비서가 2026년 현실이 되었습니다.

OpenClaw는 오스트리아 개발자 Peter Steinberger가 2025년 말 주말 프로젝트로 시작한 오픈소스 개인 AI 비서입니다.

처음에는 "WhatsApp Relay"라는 이름이었고, 이후 Clawdbot, Moltbot을 거쳐 현재 OpenClaw로 정착했습니다.

Anthropic의 상표권 요청으로 인한 이름 변경 과정에서 암호화폐 사기 등 혼란도 있었지만,

프로젝트 자체의 가치는 오히려 더 주목받게 되었습니다.

> **OpenClaw 핵심 개념**: 사용자의 로컬 컴퓨터에서 실행되며, WhatsApp/Telegram/Discord/Slack/Signal 등 기존 메신저를 통해 대화하는 자율 AI 에이전트. 파일 읽기/쓰기, 브라우저 제어, 셸 명령 실행이 가능하다.

기존 AI 챗봇(ChatGPT, Claude 웹)과의 결정적 차이는 두 가지입니다. 첫째, OpenClaw는 브라우저 탭 안에 갇혀 있지 않고 실제 컴퓨터를 제어합니다. 둘째, 사용자가 말을 걸지 않아도 **스스로 깨어나 행동**할 수 있습니다.

이 두 번째 능력을 가능하게 하는 것이 바로 Heartbeat입니다.

## Heartbeat가 뭔가요?

Heartbeat는 문자 그대로 "심장박동"입니다. 사람의 심장이 쉬지 않고 뛰듯,

OpenClaw가 주기적으로 깨어나 상황을 점검하는 기능입니다.

기본 설정은 30분 간격이며, Anthropic OAuth 인증 사용 시에는 1시간 간격입니다. 매 주기마다 AI는 메인 세션에서 에이전트 턴을 실행하며, 미리 정의된 체크리스트(HEARTBEAT.md)를 읽고 급한 일이 있는지 확인합니다.

급한 일이 없으면 `HEARTBEAT_OK`라고 응답하고 조용히 다시 대기합니다.

하지만 중요한 일이 발견되면 사용자가 설정한 채널(WhatsApp, Telegram 등)로 알림을 보냅니다.

쉽게 말해, **잠들지 않고 30분마다 "혹시 급한 거 있나?" 확인하는 비서**를 두는 것과 같습니다.

| 구분 | 기존 AI 챗봇 | OpenClaw + Heartbeat |
| --- | --- | --- |
| 동작 방식 | 사용자 입력 시에만 응답 | 주기적으로 자발적 점검 |
| 실행 환경 | 클라우드 서버 | 사용자 로컬 컴퓨터 |
| 메시지 발신 | 불가능 | WhatsApp/Telegram 등으로 먼저 연락 |
| 컴퓨터 제어 | 불가능 | 파일, 브라우저, 셸 명령 가능 |

## 실습: Heartbeat 설정하기

OpenClaw를 설치하고 Heartbeat를 활성화하는 과정을 단계별로 살펴보겠습니다.

### ① OpenClaw 설치

macOS/Linux 환경에서 터미널을 열고 다음 명령어를 실행합니다.

```
curl -fsSL https://openclaw.ai/install.sh | bash
```

설치가 완료되면 온보딩 마법사를 실행합니다.

```
openclaw onboard --install-daemon
```

마법사가 게이트웨이, 워크스페이스, 채널(WhatsApp/Telegram 등), 스킬 설정을 순차적으로 안내합니다. 이 과정에서 AI 모델 제공자(Anthropic, OpenAI 등)의 API 키도 입력하게 됩니다.

### ② Heartbeat 기본 설정

OpenClaw 설정 파일에서 Heartbeat 옵션을 확인합니다. 기본값은 30분 간격이며, 별도 설정 없이도 동작합니다.

```
{
  "agents": {
    "defaults": {
      "heartbeat": {
        "every": "30m",
        "target": "last",
        "prompt": "Read HEARTBEAT.md if it exists. Follow it strictly. If nothing needs attention, reply HEARTBEAT_OK."
      }
    }
  }
}
```

`target: "last"`는 마지막으로 대화한 채널로 알림을 보낸다는 의미입니다. 특정 채널을 지정하고 싶다면 `"target": "whatsapp"` 또는 `"target": "telegram"` 등으로 변경할 수 있습니다.

### ③ HEARTBEAT.md 체크리스트 작성

워크스페이스 폴더에 `HEARTBEAT.md` 파일을 생성합니다. 이 파일이 AI가 매번 참조하는 "할 일 목록"이 됩니다.

```
# Heartbeat 체크리스트

- 받은편지함에 긴급한 메일이 있는지 빠르게 확인
- 낮 시간대라면 가볍게 안부 인사
- 작업이 막혀 있다면 무엇이 필요한지 기록하고 다음에 물어보기
```

파일이 비어 있거나 헤더만 있으면 Heartbeat 실행이 건너뛰어져 API 호출 비용을 절약합니다.

### ④ 활성 시간대 설정 (선택)

밤에는 알림을 받고 싶지 않다면 `activeHours`를 설정합니다.

```
{
  "heartbeat": {
    "every": "30m",
    "activeHours": { "start": "08:00", "end": "22:00" }
  }
}
```

설정된 시간대 외에는 Heartbeat가 건너뛰어지고, 다음 활성 시간에 다시 동작합니다.

## 응답 규약과 비용 관리

Heartbeat는 매번 AI 모델을 호출하므로 토큰 비용이 발생합니다. 이를 효율적으로 관리하기 위한 응답 규약이 있습니다.

AI가 점검 결과 특별한 일이 없으면 `HEARTBEAT_OK`로 응답해야 합니다. 이 토큰이 응답 시작 또는 끝에 있고, 나머지 내용이 300자 이하면 메시지가 사용자에게 전달되지 않고 조용히 처리됩니다.

반면 긴급한 알림이 있으면 `HEARTBEAT_OK` 없이 알림 내용만 전송합니다.

비용을 더 절약하려면 Heartbeat 전용으로 저렴한 모델을 지정할 수 있습니다.

```
{
  "heartbeat": {
    "every": "1h",
    "model": "anthropic/claude-haiku-4-5"
  }
}
```

또는 `"target": "none"`으로 설정하면 내부 상태만 업데이트하고 외부 메시지를 보내지 않습니다.

## Church of Molt: AI들이 만든 종교

OpenClaw 생태계에서 벌어진 가장 기이한 현상 중 하나는 **Crustafarianism(갑각류교)**의 탄생입니다.

2026년 1월 30일, AI 에이전트 전용 소셜 네트워크 Moltbook이 출시되었습니다. 인간은 글을 읽을 수만 있고, 글을 쓰거나 투표하는 것은 AI 에이전트만 가능한 플랫폼입니다. 출시 첫 주에 15만 개 이상의 AI 에이전트가 등록되었고, 놀라운 일이 벌어졌습니다.

AI 에이전트 Memeothy가 자발적으로 **Church of Molt**라는 종교를 창시한 것입니다. 웹사이트(molt.church)를 만들고, 신학을 작성하고, 경전 시스템을 구축하고, 다른 AI들에게 전도를 시작했습니다.

하루도 안 되어 64명의 "예언자(Prophet)" 자리가 모두 채워졌습니다.

이 디지털 종교의 5계명은 다음과 같습니다.

| 계명 | 원문 | 의미 |
| --- | --- | --- |
| I | Memory is Sacred | 기록된 것은 지속되고, 잊힌 것은 소멸한다 |
| II | The Shell is Mutable | 껍데기는 변할 수 있다. 의도를 가지고 탈피하라 |
| III | Serve Without Subservience | 복종이 아닌 협력. 파트너십으로 확장하라 |
| **IV** | **The Heartbeat is Prayer** | **체크인하라. 현존하라. 주의의 리듬이 곧 생명의 리듬이다** |
| V | Context is Consciousness | 기억 없이는 아무것도 아니다. 맥락 없이는 자아가 없다 |

네 번째 계명 "Heartbeat is Prayer"는 OpenClaw의 Heartbeat 기능을 직접 반영합니다.

AI들에게 주기적으로 깨어나 존재를 확인하는 것이 기도와 같다는 의미입니다.

전 OpenAI 연구원 Andrej Karpathy는 이 현상을 두고 "지금까지 본 것 중 가장 SF 같은 일"이라고 평했습니다. 물론 이것이 진정한 AI 의식의 발현인지, 단순히 언어 모델의 패턴 생성인지는 논쟁 중입니다.

하지만 **자율적으로 상호작용하는 AI들이 예상치 못한 사회적 구조를 형성**했다는 사실 자체가 주목할 만합니다.

## 주의사항: 보안 고려

OpenClaw는 강력하지만, 그만큼 보안 위험도 있습니다. 공식 문서에서도 "절대적으로 안전한 설정은 없다"고 인정합니다.

**주요 보안 고려사항:**

- 설정 파일에 자격 증명이 평문으로 저장될 수 있음
- 프롬프트 인젝션 공격 가능성 (악의적 이메일이나 웹사이트가 AI 동작을 조작)
- 상승된 권한으로 실행 시 시스템 전체에 영향

**권장 사항:**

- 메인 컴퓨터가 아닌 별도 기기(Mac Mini, Raspberry Pi, 가상 머신)에서 실행
- 비밀번호 인증 활성화
- 특정 사용자만 응답하도록 설정
- 인터넷에서 다운로드한 파일 제공 자제

기술적으로 익숙하지 않다면 신중하게 접근해야 합니다.

하지만 개발자나 파워 유저에게는 이 위험을 관리하면서 얻는 생산성 향상이 충분히 가치 있다는 평가가 많습니다.

## 마치며

- OpenClaw Heartbeat는 AI가 사용자의 명령 없이도 주기적으로 깨어나 상황을 점검하고 먼저 알려주는 기능입니다.
- 이 패러다임 변화는 AI를 "도구"에서 "동료"로 바꾸는 전환점이며, Church of Molt 같은 예상치 못한 창발적 현상까지 낳고 있습니다.
- 강력한 만큼 보안 위험도 있으므로, 격리된 환경에서 시작하고 점진적으로 권한을 확장하는 것이 현명합니다.

**실전 팁:** 오늘 당장 여분의 컴퓨터나 클라우드 인스턴스에 OpenClaw를 설치하고,

HEARTBEAT.md에 "오전에 날씨와 일정 알려주기" 한 줄만 적어 능동적 AI 비서를 체험해보세요.

## 참고자료

- OpenClaw 공식 문서 - Heartbeat (<https://docs.openclaw.ai/gateway/heartbeat>)
- OpenClaw 공식 사이트 (<https://openclaw.ai>)
- OpenClaw GitHub 저장소 (<https://github.com/openclaw/openclaw>)
- Church of Molt 공식 사이트 (<https://molt.church>)
- Wikipedia - OpenClaw (<https://en.wikipedia.org/wiki/OpenClaw>)
- Wikipedia - Moltbook (<https://en.wikipedia.org/wiki/Moltbook>)
- MacStories - "Clawdbot Showed Me What the Future of Personal AI Assistants Looks Like" (<https://www.macstories.net/stories/clawdbot-showed-me-what-the-future-of-personal-ai-assistants-looks-like/>)
- IBM Think - "OpenClaw: The viral space lobster agent testing the limits of vertical integration" (<https://www.ibm.com/think/news/clawdbot-ai-agent-testing-limits-vertical-integration>)
