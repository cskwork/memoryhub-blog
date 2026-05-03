---
title: "? NanoClaw, 500줄로 만든 개인 AI 비서가 OpenClaw의 대안이 된 이유"
date: 2026-02-07T08:20:53+09:00
slug: "1011-NanoClaw-500줄로-만든-개인-AI-비서가-OpenClaw의-대안이-된-이유"
original_url: "https://memoryhub.tistory.com/1011"
tistory_id: 1011
draft: false
---

![](/images/1011-NanoClaw-500줄로-만든-개인-AI-비서가-OpenClaw의-대안이-된-이유/img.png)

OpenClaw(구 Clawdbot/Moltbot)가 GitHub 스타 14만 개를 넘기며 "개인 AI 비서" 열풍을 일으키고 있습니다. 그런데 한 개발자는 이렇게 말했습니다. "내 삶에 접근하는 소프트웨어를 이해하지 못한 채 잠들 수 없다."

52개 모듈, 45개 이상의 의존성, 15개 채널 추상화 레이어로 이루어진 OpenClaw 대신, **TypeScript 500줄짜리 경량 대안 NanoClaw가 등장했습니다.**

이 글에서는 NanoClaw가 어떤 철학으로 설계되었고, 왜 "작을수록 안전하다"는 주장이 설득력을 갖는지 파헤칩니다.

**한줄요약:** NanoClaw는 Apple Container 기반의 OS 수준 격리를 적용한 경량 Claude 비서로, 코드베이스 전체를 8분 만에 이해할 수 있도록 설계된 OpenClaw의 미니멀리스트 대안입니다.

---

## 배경: 왜 또 다른 AI 비서가 필요했나

2025년 말부터 시작된 "개인 AI 비서" 트렌드의 중심에는 OpenClaw가 있습니다. Peter Steinberger가 만든 이 오픈소스 프로젝트는 WhatsApp, Telegram, Discord 등 메시징 플랫폼을 통해 Claude나 GPT 같은 LLM과 대화하며, 이메일 관리부터 코드 리뷰까지 자동화할 수 있는 도구입니다.

문제는 **복잡성**이었습니다. OpenClaw는 현재 52개 이상의 모듈, 8개의 설정 관리 파일, 45개 이상의 의존성을 가지고 있으며, 보안은 애플리케이션 수준의 허용 목록과 페어링 코드에 의존합니다. 모든 것이 하나의 Node.js 프로세스에서 공유 메모리로 동작합니다.

> NanoClaw의 핵심 전제: "이해할 수 없는 소프트웨어에 내 삶을 맡기지 않는다."

NanoClaw 제작자 gavrielc는 이 전제에서 출발했습니다. 같은 핵심 기능을 제공하되,

**코드베이스 전체를 8분 안에 읽고 이해할 수 있는 크기**로 만들겠다는 목표였습니다.

---

## NanoClaw가 다른 점: 세 가지 핵심 설계 원칙

### 1. 극단적 단순함 - "파일 몇 개가 전부"

NanoClaw의 전체 아키텍처는 한 줄로 설명됩니다.

```
WhatsApp (baileys) → SQLite → Polling loop → Container (Claude Agent SDK) → Response
```

핵심 소스 파일은 단 네 개입니다.

- `src/index.ts` : 메인 앱. WhatsApp 연결, 메시지 라우팅, IPC 처리
- `src/container-runner.ts` : 에이전트 컨테이너 생성 및 관리
- `src/task-scheduler.ts` : 예약 작업 실행
- `src/db.ts` : SQLite 데이터베이스 연산

마이크로서비스도 없고, 메시지 큐도 없고, 추상화 레이어도 없습니다.

비유하자면, OpenClaw가 백화점이라면 NanoClaw는 단골 동네 가게입니다. 필요한 물건만 정확히 갖춰놓은 구조입니다.

### 2. OS 수준 격리 - "컨테이너 안에서만 움직인다"

대부분의 AI 비서 도구는 애플리케이션 레벨에서 보안을 처리합니다. "이 파일에 접근해도 될까?"를 코드 로직으로 판단하는 방식입니다. NanoClaw는 이 접근 자체를 거부합니다.

각 에이전트는 Apple Container(또는 Docker)로 격리된 Linux 컨테이너 안에서 실행됩니다.

에이전트가 볼 수 있는 것은 명시적으로 마운트된 디렉토리뿐입니다.

이것의 실질적 의미를 풀어보면 이렇습니다. 일반적인 AI 비서에서 bash 명령어를 실행하면 호스트 시스템 전체가 노출될 위험이 있습니다. NanoClaw에서는 bash 명령어가 컨테이너 내부에서만 실행되므로, 호스트 Mac에는 전혀 영향을 주지 않습니다.

NanoClaw의 보안 경계를 단순화하면 다음과 같습니다.

```
[비신뢰 영역: WhatsApp 메시지]
         ↓ 트리거 확인, 입력 이스케이핑
[호스트 프로세스: 메시지 라우팅, 마운트 검증, 컨테이너 생명주기]
         ↓ 명시적 마운트만 허용
[컨테이너(격리됨): 에이전트 실행, bash, 파일 조작]
```

`.ssh`, `.aws`, `.env`, `private_key` 등 민감한 경로는 기본적으로 차단 목록에 포함되어 있으며,

각 그룹은 서로의 대화 기록이나 파일 시스템을 볼 수 없도록 완전히 격리됩니다.

### 3. AI 네이티브 - "설치 마법사 대신 Claude Code"

NanoClaw는 설치 과정부터 독특합니다.

```
git clone https://github.com/gavrielc/nanoclaw.git
cd nanoclaw
claude
```

이후 `/setup`을 실행하면 Claude Code가 의존성 설치, 인증, 컨테이너 설정, 서비스 구성을 모두 처리합니다. 모니터링 대시보드도 없습니다. 상태가 궁금하면 Claude에게 물어보면 됩니다. 버그가 발생하면 `/debug`를 실행합니다. 설정 파일도 없습니다.

동작을 바꾸고 싶으면 코드를 직접 수정합니다. 코드베이스가 충분히 작기 때문에 이것이 안전합니다.

---

## Apple Container: NanoClaw의 보안 기반 기술

NanoClaw를 이해하려면 Apple Container를 알아야 합니다. 2025년 WWDC에서 발표된 이 기술은 macOS에서 Linux 컨테이너를 실행하는 Apple의 오픈소스 프레임워크입니다.

> Apple Container: macOS에서 각 컨테이너를 독립된 경량 VM으로 실행하는 Swift 기반 오픈소스 컨테이너 런타임

Docker와의 결정적 차이는 **격리 방식**에 있습니다. Docker는 하나의 큰 Linux VM 안에서 여러 컨테이너가 커널을 공유합니다. Apple Container는 각 컨테이너마다 별도의 경량 VM을 생성합니다. 비유하자면, Docker가 하나의 건물에서 여러 식당이 부엌을 공유하는 방식이라면, Apple Container는 각 식당마다 독립된 건물을 제공하는 방식입니다.

| 항목 | Docker on Mac | Apple Container |
| --- | --- | --- |
| 격리 방식 | 공유 VM + 커널 공유 | 컨테이너별 독립 VM |
| 보안 수준 | 컨테이너 간 커널 취약점 공유 가능 | 완전한 프로세스 격리 |
| 시작 시간 | 수 초 | 1초 미만 |
| 네트워킹 | 포트 포워딩 필요 | 컨테이너별 전용 IP |
| 최적화 대상 | 범용 | Apple Silicon 특화 |
| 요구 환경 | macOS 전 버전 | macOS Tahoe(26) 권장 |

NanoClaw가 Apple Container를 선택한 이유는 분명합니다.

각 WhatsApp 그룹의 AI 에이전트가 독립된 VM에서 실행되므로, 한 그룹의 에이전트가 침해되더라도 다른 그룹이나 호스트 시스템에 영향을 줄 수 없습니다.

---

## OpenClaw vs NanoClaw: 어떤 상황에서 무엇을 선택할까

두 프로젝트는 같은 문제를 정반대 방식으로 풀고 있습니다.

| 비교 항목 | OpenClaw | NanoClaw |
| --- | --- | --- |
| GitHub 스타 | 149K+ | 1.5K+ |
| 코드 규모 | 52+ 모듈, 45+ 의존성 | 소스 파일 4개, ~500줄 |
| 지원 채널 | WhatsApp, Telegram, Discord, Slack, Signal, iMessage | WhatsApp (기본), Skill로 확장 가능 |
| LLM 지원 | Claude, GPT, DeepSeek, Ollama 등 다수 | Claude Agent SDK 전용 |
| 보안 모델 | 애플리케이션 수준 (허용 목록, 페어링 코드) | OS 수준 컨테이너 격리 |
| 설정 방식 | 온보딩 위저드, 설정 파일 | 코드 직접 수정 (설정 파일 없음) |
| 확장 방식 | 스킬 레지스트리 (3,000+개) | Claude Code 스킬 (기여 권장) |
| 실행 환경 | macOS, Linux, Windows(WSL2) | macOS Tahoe 26+ (권장) |
| 적합한 사용자 | 다양한 플랫폼과 모델을 활용하려는 사용자 | 코드를 직접 이해하고 통제하려는 개발자 |

**OpenClaw을 선택해야 할 때:** 여러 메시징 플랫폼을 동시에 사용하거나, Claude 외의 다른 LLM도 활용하고 싶거나, 풍부한 커뮤니티 스킬 생태계가 필요한 경우입니다.

**NanoClaw를 선택해야 할 때:** 실행 중인 코드 전체를 직접 이해하고 싶거나, OS 수준의 강력한 보안 격리가 필요하거나, 가볍고 예측 가능한 시스템을 선호하는 경우입니다.

---

## 실습: NanoClaw 시작하기

### ① 요구 사항 확인

- macOS Tahoe(26) 이상 (Mac Mini에서 잘 동작함)
- Node.js 20+
- Claude Code (<https://claude.ai/download>)
- Apple Container (<https://github.com/apple/container>)

### ② 클론 및 설정

```
git clone https://github.com/gavrielc/nanoclaw.git
cd nanoclaw
claude
```

Claude Code가 실행되면 `/setup`을 입력합니다. Claude Code가 npm 의존성 설치, WhatsApp 인증(QR 코드 스캔), 컨테이너 빌드, launchd 서비스 등록까지 자동으로 처리합니다.

### ③ 사용하기

WhatsApp에서 트리거 단어(기본값: `@Andy`)를 사용합니다.

```
@Andy 매주 월요일 아침 9시에 Hacker News와 TechCrunch의 AI 뉴스를 정리해서 보내줘
@Andy 지난주 git 히스토리를 검토하고 README에 변경사항이 있으면 업데이트해줘
@Andy 매일 저녁 6시에 영업 파이프라인 현황을 요약해줘
```

메인 채널(자기 자신과의 채팅)에서는 관리 명령이 가능합니다.

```
@Andy 모든 예약 작업 목록을 보여줘
@Andy 월요일 브리핑 작업을 일시 중지해줘
```

### ④ 커스터마이징

NanoClaw의 핵심 철학은 **설정 파일이 아닌 코드 수정**입니다. Claude Code에게 자연어로 요청하면 됩니다.

```
"트리거 단어를 @Bob으로 바꿔줘"
"응답을 더 짧고 직접적으로 만들어줘"
"매주 대화 요약을 저장하도록 해줘"
```

코드베이스가 작기 때문에 Claude Code가 안전하게 수정할 수 있습니다.

---

## "Skills over Features" - NanoClaw의 기여 모델

NanoClaw의 독특한 점 중 하나는 **기능 추가를 거부하는 기여 정책**입니다. Telegram 지원을 추가하고 싶다면, 코드에 Telegram 모듈을 넣는 PR을 보내는 대신 `.claude/skills/add-telegram/SKILL.md` 파일을 기여합니다.

이 스킬 파일은 Claude Code에게 "이 NanoClaw 설치에 Telegram을 추가하는 방법"을 가르칩니다.

사용자는 자신의 포크에서 `/add-telegram`을 실행하면 됩니다.

결과적으로 자신에게 필요한 기능만 정확히 포함된 깔끔한 코드를 얻게 됩니다.

현재 요청 중인 스킬(RFS)은 다음과 같습니다.

- `/add-telegram` : Telegram 채널 추가
- `/add-slack` : Slack 채널 추가
- `/add-discord` : Discord 채널 추가
- `/setup-windows` : WSL2 + Docker를 통한 Windows 지원
- `/add-clear` : 대화 컴팩션 명령어 추가

이 모델의 핵심은 **기본 코드베이스를 작고 감사 가능한 상태로 유지**하면서도, 각 사용자가 자신만의 맞춤형 비서를 구축할 수 있게 하는 것입니다.

---

## 주의할 점

NanoClaw는 분명한 트레이드오프가 있습니다. macOS Tahoe(26)와 Apple Silicon이 필요하다는 플랫폼 종속성이 가장 큰 제약입니다. Claude Agent SDK에만 의존하므로 다른 LLM을 사용할 수 없습니다.

기본 채널이 WhatsApp뿐이라 다른 메신저를 쓰려면 직접 스킬을 만들거나 기다려야 합니다.

보안 문서에도 명시된 한 가지 알려진 리스크가 있습니다. Anthropic 인증 정보가 에이전트 컨테이너에 마운트되는데,

에이전트가 bash나 파일 작업을 통해 이 인증 정보를 발견할 수 있다는 점입니다. 이것은 현재 아키텍처의 한계로 인식되고 있습니다.

---

## 마치며

- NanoClaw는 "이해할 수 있는 크기"라는 설계 철학으로, AI 비서의 보안과 투명성 문제에 대한 하나의 답을 제시합니다.
- Apple Container의 VM-per-container 격리 모델과 결합하여, 애플리케이션 수준이 아닌 OS 수준의 보안을 달성합니다.
- 실전 팁: Mac을 쓰는 개발자라면 `git clone` 후 `claude`를 실행해서 NanoClaw의 코드를 직접 읽어보세요. 8분이면 전체 구조를 파악할 수 있고, 그 자체로 좋은 아키텍처 학습이 됩니다.

---

## 참고자료

- NanoClaw GitHub (<https://github.com/gavrielc/nanoclaw>)
- NanoClaw 보안 모델 문서 (<https://github.com/gavrielc/nanoclaw/blob/main/docs/SECURITY.md>)
- Apple Container GitHub (<https://github.com/apple/container>)
- Apple Containerization 프레임워크 기술 분석 - The New Stack (<https://thenewstack.io/apple-containers-on-macos-a-technical-comparison-with-docker/>)
- OpenClaw GitHub (<https://github.com/openclaw/openclaw>)
- OpenClaw Wikipedia (<https://en.wikipedia.org/wiki/OpenClaw>)
