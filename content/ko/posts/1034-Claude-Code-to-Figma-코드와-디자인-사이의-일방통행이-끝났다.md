---
title: "? Claude Code to Figma, 코드와 디자인 사이의 일방통행이 끝났다"
date: 2026-02-18T10:45:43+09:00
slug: "1034-Claude-Code-to-Figma-코드와-디자인-사이의-일방통행이-끝났다"
original_url: "https://memoryhub.tistory.com/1034"
tistory_id: 1034
draft: false
---

![](/images/1034-Claude-Code-to-Figma-코드와-디자인-사이의-일방통행이-끝났다/img.png)

AI로 UI를 만드는 건 이제 누구나 할 수 있습니다. Claude Code에 "대시보드 만들어줘"라고 프롬프트 하나만 던지면 몇 분 안에 작동하는 인터페이스가 나옵니다. 그런데 그다음이 문제입니다. 이걸 팀원들과 어떻게 함께 다듬고, 비교하고, 방향을 정할 수 있을까요?

스크린샷을 찍어서 슬랙에 올리는 게 최선이었습니다.

**Figma와 Anthropic이 이 문제를 해결하는 "Code to Canvas"를 2026년 2월 17일 공식 발표했습니다.**

**한줄요약:** 결론부터 말하면, Claude Code로 만든 UI를 Figma 캔버스에 편집 가능한 디자인 프레임으로 바로 가져올 수 있게 되었고,

반대로 Figma 디자인을 Claude Code에서 코드로 구현하는 양방향 워크플로우가 열렸습니다.

---

## 배경

지금까지 디자인과 개발의 흐름은 한 방향이었습니다. 디자이너가 Figma에서 시안을 만들고, 개발자가 그걸 보고 코드로 옮깁니다. 그 과정에서 의도가 유실되고, "이거 디자인이랑 다른데요?"라는 대화가 반복됩니다.

AI 코딩 도구의 등장으로 이 흐름에 새로운 변수가 생겼습니다.

Claude Code, Cursor, Windsurf 같은 도구로 개발자가 프롬프트만으로 작동하는 UI를 만들 수 있게 된 것입니다.

문제는 이렇게 만든 결과물이 개발자의 로컬 환경에 갇혀 있다는 점입니다.

팀원이 결과를 보려면 직접 빌드를 돌리거나, 스크린샷을 받거나, 화면 녹화를 봐야 합니다.

> 한Code to Canvas는 AI 코딩 도구로 만든 작동하는 UI를 Figma 캔버스에 편집 가능한   
> 디자인 프레임으로 변환하는 기능입니다.

Figma와 Anthropic의 파트너십으로 탄생한 "Code to Canvas"는 이 단방향 흐름을 양방향으로 바꿉니다.

코드에서 캔버스로, 캔버스에서 코드로. 이것이 왜 중요한지 비유를 들어보겠습니다.

코드 작업은 **수렴(converging)**에 강합니다. 빌드를 실행하고, 경로를 클릭하고, 한 번에 하나의 상태에 도달합니다.

반면 캔버스 작업은 **발산(diverging)**에 강합니다. 전체 경험을 한눈에 펼치고, 분기를 살펴보고, 방향을 함께 잡아갑니다.

두 세계가 연결되면 팀은 좁혀야 할 때 좁히고, 넓혀야 할 때 넓힐 수 있습니다.

---

## Code to Canvas가 바꾸는 것

### 스크린샷이 아니라 편집 가능한 디자인 프레임

가장 핵심적인 차이점입니다. Claude Code로 만든 UI를 캡처하면 평면 이미지가 아니라 Figma에서 편집할 수 있는 실제 프레임으로 변환됩니다. 복제, 재배치, 수정이 모두 가능합니다.

디자이너, PM, 개발자가 동일한 산출물 위에서 같은 맥락으로 의사결정을 내릴 수 있습니다.

### 멀티 스크린 캡처로 흐름 전체를 한눈에

한 번의 세션에서 여러 화면을 캡처할 수 있습니다. 온보딩, 결제, 설정 등 전체 플로우를 순서와 맥락을 보존한 채 캔버스에 펼칠 수 있습니다. 복잡한 멀티스텝 흐름에서 패턴, 간극, 불일치를 파악하기가 훨씬 쉬워집니다.

### 코드 변경 없이 대안 탐색

캔버스 위에서 프레임을 복제하고, 단계를 재배치하고, 구조적 변화를 실험할 수 있습니다.

아이디어를 시도하기 위해 코드를 다시 작성할 필요가 없습니다. 기각된 아이디어도 캔버스에 남아 있어 나중에 다시 참고할 수 있습니다.

### Figma에서 코드로 돌아가기 (Roundtrip)

Code to Canvas의 진짜 힘은 단방향이 아니라는 점입니다. Figma MCP 서버를 통해 Figma 디자인을 Claude Code 프롬프트에서 참조할 수 있습니다. 프레임 링크를 붙여넣으면 Claude Code가 해당 디자인의 컨텍스트를 이해하고 코드를 생성합니다.

**디자인에서 코드로, 코드에서 디자인으로 맥락을 잃지 않고 왕복하는 워크플로우**가 완성됩니다.

---

## 작동 원리: MCP가 핵심이다

Code to Canvas는 MCP(Model Context Protocol) 서버 위에서 동작합니다. MCP는 AI 도구가 외부 데이터 소스 및 애플리케이션과 상호작용할 수 있도록 하는 개방형 표준입니다. 쉽게 말해 Claude Code와 Figma 사이를 연결하는 **범용 어댑터**라고 생각하면 됩니다.

작동 흐름은 다음과 같습니다.

① Claude Code로 UI를 만들거나 수정합니다. 로컬 개발 서버, 스테이징, 프로덕션 등 브라우저에서 실행되는 모든 환경이 대상입니다.

② 화면을 캡처합니다. 통합 기능이 라이브 브라우저 상태를 가져와 Figma 호환 프레임으로 변환합니다.

③ Figma에 붙여넣기합니다. 캡처된 화면이 편집 가능한 디자인 프레임으로 캔버스에 올라갑니다.

④ 팀이 협업합니다. 주석, 복제, 재배치, 비교 작업을 캔버스 위에서 직접 수행합니다.

---

## 실습: Figma MCP 서버 설정하기

Figma MCP 서버는 두 가지 방식으로 사용할 수 있습니다. 리모트 서버(Figma 호스팅)와 로컬 데스크톱 서버입니다.

### 방법 1: 리모트 MCP 서버 (권장)

브라우저 기반 Figma 사용자에게 적합한 방식입니다. 별도 활성화가 필요 없이 바로 사용할 수 있습니다.

**1. Claude Code에 Figma MCP 추가**

```
claude mcp add --transport http figma-remote-mcp https://mcp.figma.com/mcp
```

모든 프로젝트에서 사용하려면 `--scope user` 플래그를 추가합니다.

```
claude mcp add --scope user --transport http figma-remote-mcp https://mcp.figma.com/mcp
```

**2. Claude Code 재시작 후 인증**

Claude Code에서 `/mcp` 명령어를 입력하고, `figma-remote-mcp`를 선택한 뒤 Authenticate를 진행합니다. Figma 계정 접근을 허용하면 연결이 완료됩니다.

**3. 연결 확인**

```
/mcp
```

`figma-remote-mcp` 상태가 connected로 표시되면 준비 완료입니다.

### 방법 2: 데스크톱 MCP 서버

Figma 데스크톱 앱 사용자를 위한 방식입니다.

**1. Figma 데스크톱 앱에서 MCP 서버 활성화**

Figma 데스크톱 앱 최신 버전을 열고, 하단 툴바에서 Dev Mode로 전환합니다(단축키: Shift+D). Inspect 패널의 MCP server 섹션에서 "Enable desktop MCP server"를 클릭합니다. 서버가 `http://127.0.0.1:3845/mcp`에서 실행됩니다.

**2. Claude Code에 로컬 서버 연결**

```
claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp
```

**3. 프롬프팅 시작**

Figma에서 프레임을 선택한 뒤 Claude Code에 "현재 선택한 디자인을 구현해줘"라고 요청하거나, Figma 프레임 링크를 복사해서 Claude Code 프롬프트에 붙여넣으면 됩니다.

### Claude Code 플러그인 방식 (대안)

Figma 공식 Claude Code 플러그인을 설치하면 리모트/데스크톱 MCP 서버 설정과 Agent Skills가 한 번에 구성됩니다.

```
claude plugin install figma@claude-plugins-official
```

---

## 기존 방식과 Code to Canvas 비교

| 항목 | 기존 워크플로우 | Code to Canvas |
| --- | --- | --- |
| AI 결과물 공유 | 스크린샷, 화면 녹화, 로컬 빌드 실행 | Figma 프레임으로 직접 전환 |
| 편집 가능성 | 디자이너가 처음부터 재현해야 함 | 편집 가능한 프레임으로 즉시 수정 |
| 팀 협업 | 개발자 환경에 접근해야 피드백 가능 | Figma 캔버스에서 주석, 비교, 토론 |
| 대안 탐색 | 코드 수정 후 다시 빌드 | 프레임 복제로 코드 변경 없이 비교 |
| 양방향성 | 디자인→코드 단방향 | 코드→디자인→코드 왕복 가능 |
| 멀티스크린 | 화면별 개별 스크린샷 | 한 세션에서 전체 플로우 캡처 |

---

## 이 파트너십이 의미하는 것

"AI가 코드를 만들면 디자이너가 필요 없어지는 거 아닌가?"라는 질문이 자연스럽게 떠오릅니다. Figma와 Anthropic의 답은 그 반대입니다. AI 코딩 도구가 발전할수록 디자인 협업이 더 중요해진다는 것이 이 파트너십의 핵심 전제입니다.

AI가 인터페이스를 만들 수 있느냐는 더 이상 질문이 아닙니다.

진짜 질문은 **AI가 만든 것을 팀이 함께 평가하고 다듬을 수 있는 공유 공간이 있는가**입니다.

Code to Canvas는 바로 그 공간을 만들어줍니다.

다만 잠재적 리스크도 있습니다. CNBC 보도에 따르면, AI 도구가 계속 개선되면 팀이 디자인 다듬기 단계를 아예 건너뛸 수도 있다는 우려가 존재합니다. Figma가 더 이상 자신이 통제하지 못하는 고속도로의 진입 램프를 만들고 있는 것일 수도 있다는 시각입니다.

그러나 현재 시점에서 제품을 차별화하는 것은 기능의 유무가 아니라

**제품이 어떤 느낌을 주는지, 사용자를 어떻게 안내하는지, 가치를 얼마나 명확하게 전달하는지**입니다.

이 영역은 여전히 사람의 판단과 팀 협업이 필요한 곳입니다.

---

## 마치며

- Code to Canvas는 AI 코딩 도구로 만든 UI를 Figma 캔버스에서 편집 가능한 디자인 프레임으로 변환하는 기능이며, MCP 서버 기반으로 양방향 워크플로우를 지원합니다.
- 코드는 수렴에, 캔버스는 발산에 강합니다. 두 세계가 연결되면서 AI 시대 디자인-개발 협업의 새로운 기준이 만들어지고 있습니다.
- 실전 팁: 터미널에서 `claude mcp add --transport http figma-remote-mcp https://mcp.figma.com/mcp` 한 줄이면 오늘 바로 시작할 수 있습니다. Claude Code로 만든 화면을 Figma에 가져와서 팀원과 함께 살펴보세요.

---

## 참고자료

- From Claude Code to Figma: Turning Production Code into Editable Figma Designs (<https://www.figma.com/blog/introducing-claude-code-to-figma/>)
- Guide to the Figma MCP server (<https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server>)
- Figma MCP Remote Server Developer Docs (<https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/>)
- Figma MCP Server Guide - GitHub (<https://github.com/figma/mcp-server-guide>)
- Claude Code MCP 연결 가이드 (<https://code.claude.com/docs/en/mcp>)
