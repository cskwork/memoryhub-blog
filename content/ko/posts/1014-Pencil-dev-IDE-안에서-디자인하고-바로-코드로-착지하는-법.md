---
title: "? Pencil.dev, IDE 안에서 디자인하고 바로 코드로 착지하는 법"
date: 2026-02-08T08:43:54+09:00
slug: "1014-Pencil-dev-IDE-안에서-디자인하고-바로-코드로-착지하는-법"
original_url: "https://memoryhub.tistory.com/1014"
tistory_id: 1014
draft: false
  hidden: false
cover:
  image: "/images/1014-Pencil-dev-IDE-안에서-디자인하고-바로-코드로-착지하는-법/img.png"
  relative: false
  hidden: false
---

![](/images/1014-Pencil-dev-IDE-안에서-디자인하고-바로-코드로-착지하는-법/img.png)

디자이너가 Figma에서 완성한 시안을 개발자에게 넘기면 무슨 일이 벌어지는가. 스타일 불일치, 에셋 추출 삽질, 끝없는 확인 메시지. McKinsey의 2024년 소프트웨어 개발 효율성 연구에 따르면,

이 "디자인 핸드오프" 과정이 중간 규모 팀 전체 프로젝트 타임라인의 15~20%를 잡아먹는다.

Pencil.dev는 이 문제를 근본부터 뒤집는다.

디자인 파일을 Figma가 아닌 **코드 레포지토리 안에 두고, IDE에서 직접 디자인하며, AI 에이전트가 캔버스를 읽고 쓰게 만든다.**

**한줄요약:** 결론부터 말하면, Pencil.dev는 MCP 기반의 벡터 디자인 캔버스를 IDE 안에 통합해서 디자인 핸드오프 자체를 제거하는 차세대 개발 도구다.

## 배경

소프트웨어 개발에서 "디자인-개발 핸드오프"는 오래된 병목이다. 디자이너는 Figma에서 작업하고, 개발자는 VS Code에서 작업한다. 둘 사이에는 항상 "번역 비용"이 존재한다.

> 디자인 핸드오프란, 디자이너가 완성한 시안을   
> 개발자가 해석 가능한 형태(스펙 문서, 에셋 파일 등)로 전달하는 과정을 말한다.

이 과정에서 발생하는 문제는 단순한 불편이 아니다. 색상값 하나가 달라지고, 간격이 4px 어긋나고, "이 버튼은 원래 이런 의도가 아니었는데"라는 대화가 반복된다. 핵심은 디자인 도구와 개발 도구가 **서로 다른 세계에 존재한다**는 구조적 문제에 있다.

Figma의 디자인 파일은 Figma 서버에 살고, 코드는 Git 레포에 산다.

두 세계를 연결하는 공식 통로가 없으니, 사람이 수동으로 "번역"하는 수밖에 없었다.

2025년 9월, 이 구조를 정면으로 겨냥한 도구가 등장했다. Tom Krcha가 만든 Pencil.dev다.

Krcha는 Adobe XD 개발에 참여했고, 화상회의 도구 Around(Miro에 인수)을 만들었으며, Alter avatars(Google에 인수)를 공동 창업한 인물이다.

14년 이상 디자인과 엔지니어링의 교차점에서 일해온 사람이 내놓은 답이 "디자인 파일을 코드 레포 안에 넣자"였다.

현재 Pencil.dev는 얼리 액세스 단계로 **무료**로 사용할 수 있다.

다만 AI 기능 구동을 위해서는 Claude Code 구독(월 $20부터)이 필요하다.

Pencil 자체는 UI 엔진이고, 실제 AI 생성은 Anthropic의 모델이 수행하는 구조다.

## Pencil.dev의 핵심 개념

Pencil.dev를 이해하려면 세 가지 축을 알아야 한다.

**첫째, .pen 파일 형식이다.** Pencil의 디자인 파일은 .pen이라는 확장자를 가진다. 내부는 JSON 기반 텍스트 데이터다. 이것이 의미하는 바가 크다. 텍스트 파일이기 때문에 Git으로 버전 관리가 가능하다. 코드와 같은 레포에 들어가니, 코드를 롤백하면 디자인도 함께 롤백된다. Figma에서 "Version History"를 뒤지며 "그때 그 버전이 뭐였지?"를 찾던 경험이 있다면, 이것이 얼마나 큰 차이인지 체감할 수 있다.

**둘째, MCP(Model Context Protocol) 통합이다.** MCP는 AI 에이전트가 외부 도구와 표준화된 방식으로 소통하는 프로토콜이다. 비유하자면, AI와 디자인 캔버스 사이의 "공용어"라고 할 수 있다. Pencil은 MCP를 통해 읽기뿐 아니라 **쓰기 권한까지** AI에게 부여한다. 즉 Claude Code나 Cursor의 AI 에이전트가 캔버스 위의 요소를 직접 배치하고, 스타일을 수정하고, 컴포넌트를 생성할 수 있다.

**셋째, 양방향 워크플로다.** 디자인에서 코드로(Design → Code)만 가능한 게 아니다. 코드에서 디자인으로(Code → Design)도 된다. 기존 코드베이스의 컴포넌트를 캔버스에 시각적으로 재현하거나, 캔버스에서 수정한 디자인 토큰이 CSS 변수로 자동 반영되는 식이다.

이 세 가지가 합쳐지면 기존 워크플로와 근본적으로 다른 경험이 만들어진다. "디자인 도구를 연다"는 행위 자체가 사라지고, 코드를 쓰는 연장선에서 UI가 만들어진다.

## 실습: Pencil.dev 시작하기

### ① 설치

Pencil.dev는 세 가지 방식으로 사용할 수 있다. 독립 데스크톱 앱, Cursor 확장 프로그램, 그리고 VS Code 확장 프로그램이다. macOS에서는 세 가지 모두 지원하고, Windows는 현재 확장 프로그램만 지원한다. Linux는 데스크톱 앱과 확장 프로그램 모두 가능하나 Wayland 환경에서 일부 UI 이슈가 보고되어 있다.

Cursor를 사용한다면 확장 프로그램 메뉴에서 "Pencil"을 검색해 설치하면 된다. 핵심 엔진 역할을 하는 Claude Code CLI가 시스템에 설치되어 있어야 하며, `claude` 명령어를 통해 인증이 완료된 상태여야 한다.

### ② MCP 연결 확인

설치 후 가장 중요한 단계다. Cursor를 사용한다면 Settings > Tools & MCP 탭에서 `extension-pencil`이 enable 상태인지 확인한다. Claude Code를 직접 사용한다면 터미널에서 `/mcp` 명령어를 입력했을 때 `pencil ✔ connected`가 표시되어야 한다. 이 연결이 되어야 AI가 캔버스를 인식하고 조작할 수 있다.

### ③ 첫 번째 디자인 파일 생성

프로젝트 디렉토리에서 `.pen` 확장자의 파일을 생성한다.

```
mkdir my-app && cd my-app
touch design.pen
```

이 파일을 IDE에서 열면 무한 캔버스가 나타난다. 여기서 직접 벡터 요소를 그릴 수도 있고, AI에게 자연어로 지시할 수도 있다.

예를 들어 "파란 그라디언트 배경에 흰색 텍스트로 Get Started 버튼을 만들어줘"라고 프롬프트하면 캔버스에 바로 반영된다.

### ④ Figma 자산 가져오기

기존 Figma 디자인이 있다면 처음부터 다시 그릴 필요가 없다. Figma에서 요소를 복사(Ctrl+C)한 뒤 Pencil 캔버스에 붙여넣기(Ctrl+V)하면 벡터, 텍스트, 스타일이 그대로 보존된다. 브랜드 킷이나 컴포넌트 라이브러리를 이식할 때 유용하다.

### ⑤ 디자인에서 코드 생성

캔버스에서 프레임을 선택한 뒤 AI에게 "이 디자인으로 React 컴포넌트를 생성해줘" 또는 "Next.js 페이지 컴포넌트로 내보내줘"라고 지시하면 코드가 같은 프로젝트 디렉토리 안에 생성된다. 생성된 코드는 즉시 실행 가능한 상태다.

실제 사용자 후기를 보면, 복잡한 3단 반응형 레이아웃에서 4~8px 정도의 정렬 오차가 발생하는 경우가 있다.

이때 캔버스에서 직접 위치를 미세 조정하면 변경 사항이 코드에 다시 반영된다. 이 **양방향 동기화**가 Pencil의 핵심 가치다.

## 기존 도구와 비교

| 비교 항목 | Figma + 수동 핸드오프 | Pencil.dev |
| --- | --- | --- |
| 디자인 환경 | 별도 브라우저 앱 | IDE 내장 캔버스 |
| 버전 관리 | Figma 자체 히스토리 | Git (코드와 통합) |
| AI 연동 | 플러그인 의존 (Layermate 등) | MCP 네이티브 (읽기+쓰기) |
| 코드 생성 | 수동 해석 또는 별도 도구 | 캔버스에서 직접 생성 |
| 협업 | 디자이너-개발자 분리 | 같은 레포, 같은 도구 |
| 수동 편집 품질 | Figma가 우위 | 세밀한 조정은 아직 Figma가 앞섬 |
| 가격 | Figma 유료 + 개발 도구 | Pencil 무료 (Claude Code 구독 별도) |

솔직하게 짚어야 할 부분이 있다. "사람이 손으로 UI를 세밀하게 다듬는" 경험에서는 현시점에서 여전히 Figma가 앞선다는 것이 다수 사용자의 공통 평가다.

Pencil의 강점은 정교한 수작업이 아니라, **AI 에이전트와 협업하며 빠르게 프로토타입하고 바로 코드로 전환하는 속도**에 있다.

## 어떤 팀에 적합한가

Pencil.dev가 가장 큰 가치를 발휘하는 시나리오는 명확하다.

프론트엔드 중심의 빠른 UI 이터레이션이 필요한 프로젝트, 랜딩 페이지나 SaaS 대시보드 프로토타입 같은 작업이 대표적이다.

Claude Code나 Cursor를 이미 주요 개발 도구로 사용하는 팀이라면 기존 워크플로에 자연스럽게 녹아든다.

반면 복잡한 상태 관리, API 통합, 데이터베이스 로직이 핵심인 백엔드 중심 프로젝트에서는 직접적인 효용이 제한적이다.

또한 현재 얼리 액세스 단계이므로, 장기적으로 의존하는 구조를 설계할 때는 향후 가격 정책 변화를 고려해야 한다.

Andreessen Horowitz(a16z)가 투자한 스타트업인 만큼 현재의 무료 모델은 사용자 확보 전략일 가능성이 높다.

## 마치며

- Pencil.dev는 .pen 파일을 Git 레포에 넣고 MCP로 AI 에이전트와 연결함으로써, 디자인 핸드오프라는 구조적 병목을 제거하는 도구다.
- "디자인 도구를 따로 연다"는 행위 자체를 없애고, IDE 안에서 디자인과 코드가 양방향으로 동기화되는 워크플로를 만든다.
- 실전 팁: Cursor나 VS Code에 Pencil 확장 프로그램을 설치하고, 진행 중인 프로젝트에 `design.pen` 파일 하나를 추가해보라. 기존 Figma 시안을 복사-붙여넣기하는 것만으로도 워크플로 차이를 체감할 수 있다.

## 참고자료

- Pencil 공식 문서 (<https://docs.pencil.dev/>)
- <https://www.youtube.com/watch?v=7IRFzZyrKOE>
- Pencil.dev 공식 사이트 (<https://www.pencil.dev/>)
- Pencil.dev: Bridging the Design-to-Code Gap in Modern Development - Medium (<https://medium.com/@tentenco/pencil-dev-bridging-the-design-to-code-gap-in-modern-development-fede236fa551>)
- Pencil.dev the Missing Link Between Design and Vibe Coding? - Abduzeedo (<https://abduzeedo.com/pencildev-missing-link-between-design-and-vibe-coding>)
- Pencil.dev Review: Features, Pricing, Alternatives - Banani (<https://www.banani.co/blog/pencil-dev-review>)
- Speedrun by a16z - Pencil.dev (<https://speedrun.a16z.com/companies/pencildev>)
