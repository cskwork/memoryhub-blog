---
title: "? Ralph Wiggum Loop: 5줄 bash로 AI가 밤새 코딩하게 만드는 법"
date: 2026-01-17T17:57:07+09:00
slug: "977-Ralph-Wiggum-Loop-5줄-bash로-AI가-밤새-코딩하게-만드는-법"
original_url: "https://memoryhub.tistory.com/977"
tistory_id: 977
draft: false
---

```
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║     while :; do                                  ║
    ║       cat PROMPT.md | claude-code                ║
    ║     done                                         ║
    ║                                                  ║
    ║         ? → ? → ? → ✅                        ║
    ║                                                  ║
    ║     "I'm in danger!" - Ralph Wiggum             ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
```

AI 코딩 도구를 써봤다면 이런 경험이 있을 것입니다. Claude에게 작업을 시키고, 에러가 나면 다시 지시하고, 또 에러가 나면 또 지시하고. 이 반복을 밤새 자동으로 돌릴 수 있다면 어떨까요?

호주의 한 개발자가 5줄짜리 bash 스크립트로 이 문제를 해결했고,

그 기법은 심슨 캐릭터 이름을 따 'Ralph Wiggum'이라 불립니다.

**완벽한 한 번의 응답보다, 끈질기게 반복하며 스스로 수정하는 AI가 더 강력하다는 것이 핵심입니다.**

**한줄요약:** 결론부터 말하면, Ralph Wiggum은 AI 코딩 에이전트를 무한 루프에 넣어 작업 완료까지 자동 반복시키는 기법으로, $50,000 계약을 $297 API 비용으로 완료한 사례까지 나왔습니다.

## 배경

2025년 5월, 호주에서 염소를 키우며 오픈소스 개발을 하던 Geoffrey Huntley는 AI 코딩의 근본적 한계에 부딪혔습니다. Claude Code 같은 에이전트형 코딩 도구가 아무리 똑똒해도, 결국 사람이 매번 결과를 검토하고 다시 지시해야 한다는 점이었습니다. 이른바 'human-in-the-loop' 병목 현상입니다.

그의 해결책은 놀라울 정도로 단순했습니다.

```
while :; do cat PROMPT.md | claude-code ; done
```

이게 전부입니다. Claude에게 작업을 주고, Claude가 끝내려 하면 같은 프롬프트를 다시 넣습니다. Claude가 수정한 파일은 그대로 남아 있으니 다음 반복에서 이전 작업을 이어갈 수 있습니다.

> Ralph Wiggum Loop는 AI가 실패하더라도 예측 가능하게 실패하고, 그 실패를 학습해 다음 반복에서 개선하도록 하는 '자기 참조적 피드백 루프'입니다.

이름의 유래가 재미있습니다. 심슨 가족에서 불타는 방 안에 앉아 "나 위험해!"라고 태평하게 말하는 Ralph Wiggum 캐릭터처럼, AI가 새벽 2시에 코드베이스를 자율적으로 수정하는 모습이 꼭 그렇다는 것입니다.

멍청해 보이지만 포기하지 않는 끈기가 핵심입니다.

## 작동 원리

Ralph Wiggum의 철학을 한 마디로 요약하면 이렇습니다.

**"예측 불가능하게 성공하는 것보다, 예측 가능하게 실패하는 게 낫다."**

전통적인 AI 코딩 워크플로우는 완벽한 프롬프트를 작성해서 한 번에 깔끔한 코드를 받아내는 데 집중합니다. Ralph Wiggum은 이를 완전히 뒤집습니다. 완벽함 대신 반복을, 영리한 프롬프트 대신 명확한 완료 조건을 추구합니다.

Anthropic은 2025년 여름 이 기법을 공식 Claude Code 플러그인으로 만들었습니다.

플러그인은 Stop Hook이라는 기능을 사용합니다.

```
/ralph-loop "작업 설명" --completion-promise "DONE" --max-iterations 20
```

작동 흐름은 다음과 같습니다.

① 사용자가 작업과 완료 조건을 정의합니다

② Claude가 작업을 수행합니다

③ Claude가 종료하려 합니다

④ Stop Hook이 종료를 가로채고, 완료 조건이 충족되지 않으면 같은 프롬프트를 다시 주입합니다

⑤ Claude는 이전 반복에서 수정한 파일과 git 히스토리를 확인하고 이어서 작업합니다

⑥ 완료 조건 충족 또는 최대 반복 횟수 도달까지 반복합니다

핵심은 각 반복이 이전 반복의 결과를 그대로 본다는 점입니다. Claude가 새로 시작하는 게 아니라, 자신이 만든 코드를 검토하고 개선합니다.

## 실제 성과 사례

Ralph Wiggum이 단순한 장난이 아니라는 건 실제 결과가 증명합니다.

**$50,000 계약을 $297로 완료:** Geoffrey Huntley가 공유한 iMessage 스크린샷에 따르면,

한 개발자가 Ralph를 활용해 MVP를 테스트와 리뷰까지 완료한 비용이 $297였습니다.

원래 계약 금액은 $50,000이었습니다.

**Y Combinator 해커톤 결과:** 한 팀이 Ralph를 사용해 하룻밤 만에 6개 이상의 리포지토리를 배포했고,

API 비용은 $297였습니다.

**3개월간 프로그래밍 언어 개발:** Huntley 본인은 Ralph를 3개월 연속 실행해 'Cursed'라는 완전한 프로그래밍 언어를 만들었습니다. Gen Z 슬랭을 키워드로 사용하는 난해한 언어로, LLVM 컴파일러와 표준 라이브러리까지 갖췄습니다.

slay가 함수 선언, sus가 변수, based가 true입니다.

**Cursor의 브라우저 개발:** Cursor 공동창업자 Michael Truell은 GPT-5.2를 1주일간 중단 없이 실행해 300만 줄 이상의 브라우저를 개발했다고 발표했습니다. Rust로 작성된 커스텀 렌더링 엔진, HTML 파싱, CSS, 레이아웃, JavaScript VM까지 포함됩니다. 해당 트윗은 450만 뷰를 기록했습니다.

## 실습

### 1. 플러그인 설치

Claude Code에서 공식 Ralph Wiggum 플러그인을 설치합니다.

```
claude /install-plugin @anthropics/claude-code-ralph-wiggum
```

설치 후 `/help`를 실행하면 상세 사용법을 확인할 수 있습니다.

### 2. 기본 사용법

단순한 리팩토링 작업으로 시작해봅니다. max-iterations는 반드시 설정해야 무한 루프를 방지할 수 있습니다.

```
/ralph-loop "모든 Jest 테스트를 Vitest로 마이그레이션하라. 
완료되면 <promise>COMPLETE</promise>를 출력하라." 
--max-iterations 30 
--completion-promise "COMPLETE"
```

각 반복에서 Claude는 이전에 수정한 파일과 git 커밋 내역을 확인하고 작업을 이어갑니다.

### 3. 야간 자동화 스크립트

여러 프로젝트를 밤새 작업시키려면 배치 스크립트를 작성합니다.

```
#!/bin/bash
# overnight-work.sh

cd /path/to/project1
claude -p "/ralph-loop '데이터베이스 스키마 구현. 
완료 시 <promise>PHASE1_DONE</promise>' --max-iterations 20"

cd /path/to/project2  
claude -p "/ralph-loop 'API 엔드포인트 구축.
완료 시 <promise>PHASE2_DONE</promise>' --max-iterations 25"
```

실행 전 API 대시보드에서 비용 알림을 설정하는 것을 권장합니다.

50회 반복 루프가 대규모 코드베이스에서 돌면 $50-100 이상의 API 비용이 발생할 수 있습니다.

### 4. 효과적인 프롬프트 작성법

Ralph의 성공은 모델 성능이 아니라 프롬프트 품질에 달려 있습니다. Matt Pocock의 권장 사항을 참고합니다.

**명확한 완료 조건을 포함합니다:**

```
REST API 구축:
- 모든 CRUD 엔드포인트 작동
- 입력 검증 구현
- 테스트 통과 (커버리지 80% 이상)
- README에 API 문서 작성
완료 시 <promise>COMPLETE</promise> 출력
```

**막혔을 때의 행동을 정의합니다:**

```
15회 반복 후에도 미완료 시:
- 진행을 막는 요소 문서화
- 시도한 방법 나열
- 대안 제시
```

**단일 기능에 집중합니다.** 한 번에 여러 기능을 요청하면 루프가 수렴하지 않습니다.

## 모범사례/패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| 공식 플러그인 (/ralph-loop) | 설치 간편, Stop Hook 내장, 세션 내 실행 | 권한 설정 필요, 일부 환경에서 불안정 보고 |
| bash 루프 (원본 방식) | 완전한 제어권, 커스터마이징 자유 | 수동 설정 필요, 안전장치 직접 구현 |
| ralph-claude-code (3,300+ stars) | 308개 테스트, 이중 종료 조건, Rate limiting | 별도 설치, 학습 곡선 존재 |
| Ralphy (병렬 실행) | 다중 AI 엔진 지원, git worktree 격리 | 초기 단계, 문서 부족 |

## 마치며

- Ralph Wiggum Loop는 AI 코딩의 패러다임을 '완벽한 한 번'에서 '끈질긴 반복'으로 전환시킨 기법입니다
- 핵심은 Stop Hook을 통한 자기 참조적 피드백 루프로, AI가 자신의 작업을 검토하고 개선하도록 합니다
- $50k 계약을 $297로 완료하거나 3개월 만에 프로그래밍 언어를 개발한 사례가 실제로 존재합니다

**실전 팁:** 오늘 당장 간단한 작업(타입 어노테이션 추가,

콜백을 Promise로 변환 등)으로 max-iterations 10 설정 후 Ralph를 테스트해보세요.

## 참고자료

- Geoffrey Huntley's Ralph Wiggum 공식 페이지 (<https://ghuntley.com/ralph>)
- Claude Code 공식 Ralph Wiggum 플러그인 (<https://github.com/anthropics/claude-code/tree/main/plugins/ralph-wiggum>)
- ralph-claude-code by Frank Bria (<https://github.com/frankbria/ralph-claude-code>)
- Matt Pocock's 11 Tips For AI Coding With Ralph Wiggum (<https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum>)
- VentureBeat: How Ralph Wiggum went from 'The Simpsons' to the biggest name in AI (<https://venturebeat.com/technology/how-ralph-wiggum-went-from-the-simpsons-to-the-biggest-name-in-ai-right-now>)
