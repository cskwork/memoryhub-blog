---
title: "?‍? Codex가 이제 내 PC를 직접 조작한다고? Codex 앱 업데이트"
date: 2026-04-17T02:58:27+09:00
slug: "1061-Codex가-이제-내-PC를-직접-조작한다고-Codex-앱-업데이트"
original_url: "https://memoryhub.tistory.com/1061"
tistory_id: 1061
draft: false
cover:
  image: "images/1061-Codex%EA%B0%80-%EC%9D%B4%EC%A0%9C-%EB%82%B4-PC%EB%A5%BC-%EC%A7%81%EC%A0%91-%EC%A1%B0%EC%9E%91%ED%95%9C%EB%8B%A4%EA%B3%A0-Codex-%EC%95%B1-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8/img.png"
  relative: false
  hidden: false
---

![](/images/1061-Codex%EA%B0%80-%EC%9D%B4%EC%A0%9C-%EB%82%B4-PC%EB%A5%BC-%EC%A7%81%EC%A0%91-%EC%A1%B0%EC%9E%91%ED%95%9C%EB%8B%A4%EA%B3%A0-Codex-%EC%95%B1-%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8/img.png)

JIRA 보고 Slack 답하다 또 코드로 돌아오는 그 왕복, 하루에 몇 번 하시나요. 저는 오늘도 브라우저·터미널·Notion을 번갈아 열다 오전이 녹아 버렸습니다. 그런데 이번 Codex 업데이트는 '에이전트가 창을 직접 클릭하고 타이핑하며 같이 일한다'는 약속을 들고 나왔습니다.

이 글을 끝까지 읽으면 무엇이 바뀌었고, 어디에 먼저 투입해야 체감 이득이 큰지 한눈에 잡힙니다.

## 한줄요약

OpenAI Codex가 백그라운드 컴퓨터 유즈·인앱 브라우저·gpt-image-1.5 이미지 생성·90여 개 플러그인·장기 메모리를 한꺼번에 얹어, 코드 작성을 넘어 소프트웨어 개발 라이프사이클 전 구간을 함께 끌고 가는 파트너로 확장됐습니다.

## 왜 이번 업데이트가 '메이저'인가

OpenAI가 공식적으로 밝힌 Codex의 주간 활성 사용자는 300만 명 이상입니다.

지난 1년간 개발자들이 Codex를 쓰는 방식은 단순 코드 생성에서 시스템 이해·맥락 수집·리뷰·디버깅·장기 작업 지속으로 계속 넓어졌고, 이번 릴리스는 그 확장 방향을 도구 차원에서 공식화한 셈입니다.

| 새로 들어온 것 | 핵심 내용 |
| --- | --- |
| 백그라운드 컴퓨터 유즈 | Codex가 자체 커서로 앱을 보고·클릭·타이핑, 내가 다른 작업을 해도 방해받지 않고 여러 에이전트가 병렬로 동작 |
| 인앱 브라우저 | 웹 페이지에 직접 코멘트를 달아 에이전트에게 정밀 지시, 프런트엔드·게임 개발에 우선 적용 |
| 이미지 생성 (gpt-image-2) | 제품 컨셉·프런트엔드 목업·게임 비주얼을 코드·스크린샷과 같은 워크플로우에서 생성·반복 |
| 90여 개 추가 플러그인 | Atlassian Rovo(JIRA), CircleCI, CodeRabbit, GitLab Issues, Microsoft Suite, Neon by Databricks, Remotion, Render, Superpowers 등 |
| SDLC 지원 확장 | GitHub 리뷰 코멘트 처리, 다중 터미널 탭, SSH 원격 devbox(알파), 사이드바 파일 미리보기, 요약 패널 |
| 장기 자동화 | 기존 스레드 재사용, 미래 시점에 스스로 깨어나 며칠·몇 주짜리 작업 이어 가기 |
| 메모리 프리뷰 | 선호·교정·수집한 맥락을 기억해 다음 작업 속도와 품질을 끌어올림 |
| 선제 제안 | 프로젝트·플러그인·메모리 맥락으로 '오늘 어디서 이어 할지' 우선순위 리스트 제공 |

## 핵심

> 이번 Codex 업데이트의 본질은 "에이전트를 코드 편집 창 밖으로 꺼내 컴퓨터와 웹, 팀 도구 위에서 직접 일하게 만든 것"입니다.  
> 컴퓨터 유즈·브라우저·이미지·플러그인·메모리·스케줄링이 한 번에 붙으면서 Codex는 이제 SDLC의 '쓰기' 단계가 아니라 '전 구간 오케스트레이터'로 재정의됩니다.

## 실습 — 오늘 퇴근 전 30분에 체험해 보기

### ① 컴퓨터 유즈로 프런트엔드 이터레이션

macOS용 Codex 데스크톱 앱을 최신 버전으로 업데이트하고 ChatGPT 계정으로 로그인하면 백그라운드 컴퓨터 유즈가 노출됩니다.

실행 예: Figma 목업을 띄워 놓고 "이 화면을 Next.js 페이지로 구현하고 실제 브라우저에서 동작 확인까지 끝내 줘" 같은 지시를 주면,

에이전트가 자체 커서로 편집기·브라우저를 왕복하며 작업합니다. 이때 내 다른 앱은 방해받지 않습니다.

### ② 인앱 브라우저로 UI 결함 정밀 지시

localhost로 띄운 개발 서버를 Codex 인앱 브라우저에서 열고, 버튼·폼에 직접 코멘트를 남기는 방식입니다.

"이 영역의 패딩을 16px로, 모바일 320px 기준 레이아웃 깨짐 수정"처럼 좌표·요소 맥락과 함께 지시를 전달할 수 있어 스크린샷 붙여넣기 왕복이 사라집니다.

게임 UI·복잡한 대시보드 같은 시각 집약적 작업에서 체감 차이가 가장 큽니다.

### ③ 자동화·메모리로 '내일의 나' 준비

장기 자동화는 "금요일 오후 5시에 깨어나 PR 댓글 최종 반영 후 merge 큐에 올려 둬" 같은 지시가 가능합니다.

메모리 프리뷰를 켜면 내가 반복해서 교정했던 컨벤션(예: "우리 팀은 일괄 import 대신 배럴 파일을 쓰지 않는다")을 에이전트가 기억합니다.

결과 텍스트 캡처 대체 설명: Codex 앱 좌측 요약 패널에 에이전트의 계획·참고 소스·산출물이 타임라인 형태로 표시됩니다.

CLI만 빠르게 확인하고 싶다면 아래를 참고하세요(언어·런타임: Node.js 20 이상, `openai/codex` 기준).

```
npm install -g @openai/codex
codex login
codex plugins list        # 90여 개 플러그인 중 설치 가능 목록 확인
codex --help              # 자동화·메모리 플래그 확인
```

## 경쟁 도구와의 패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| OpenAI Codex (이번 업데이트) | 컴퓨터 유즈·인앱 브라우저·이미지 생성·90여 개 플러그인·장기 메모리가 단일 앱에 통합, SDLC 전 구간 커버 | 데스크톱 앱 중심 릴리스라 IDE 친화도는 낮음, 개인화·컴퓨터 유즈는 EU/UK 지역 순차 배포 |
| GitHub Copilot | IDE 내 자동완성·채팅 경험 성숙, 엔터프라이즈 도입률·감사 로그 강점 | 멀티 앱 오케스트레이션이나 장시간 태스크, 외부 도구 자동 조작은 Codex 대비 제한적 |
| Claude Code (Anthropic) | 터미널·SDK·MCP 생태계 유연성, 장문 컨텍스트 처리와 서브에이전트 설계 자유도 높음 | 네이티브 컴퓨터 유즈 UX·데스크톱 앱 기반 시각적 워크플로우는 Codex 앱보다 나중에 따라오는 편 |

## 마치며

이번 릴리스의 포인트는 '모델이 똑똑해졌다'가 아니라 '에이전트가 앉은 자리가 바뀌었다'는 점입니다.

컴퓨터 유즈·브라우저·플러그인·메모리가 한 워크스페이스에 모이면서, Codex는 코드를 넘어 JIRA·Slack·Notion·CI까지 손대는 공동 작업자로 올라섰습니다.

내일 아침 반복 작업 하나만 골라 Codex 자동화에 넘겨 보시면, 이 흐름이 왜 지금 중요한지 손끝으로 느끼실 겁니다.

## 참고자료

- [OpenAI, Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/)
- [OpenAI, Introducing the Codex app](https://openai.com/index/introducing-the-codex-app/)
- [OpenAI Developers, Codex Changelog](https://developers.openai.com/codex/changelog)
- [OpenAI Developers, Agent Skills](https://developers.openai.com/codex/skills)
- [OpenAI Developers, Subagents](https://developers.openai.com/codex/subagents)
- [GitHub, openai/codex](https://github.com/openai/codex)
