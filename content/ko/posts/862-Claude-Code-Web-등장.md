---
title: "Claude Code Web 등장"
date: 2025-10-21T08:48:49+09:00
slug: "862-Claude-Code-Web-등장"
original_url: "https://memoryhub.tistory.com/862"
tistory_id: 862
draft: false
cover:
  image: "/images/862-Claude-Code-Web-등장/img.png"
  relative: false
  hidden: false
---

![](/images/862-Claude-Code-Web-등장/img.png)

웹 기반 Claude Code를 사용하면 터미널을 열지 않고도 코딩 세션을 시작할 수 있습니다. GitHub 저장소를 연결하고 필요한 작업을 설명하면 Claude가 구현을 처리합니다.

각 세션은 실시간 진행 상황 추적과 함께 독립된 환경에서 실행되며, 작업 진행 중에도 Claude의 방향을 조정할 수 있습니다.

Claude Code가 클라우드에서 실행되므로 이제 단일 인터페이스에서 여러 저장소의 작업을 동시에 병렬로 실행할 수 있으며, 자동 PR 생성과 명확한 변경 사항 요약으로 더 빠르게 배포할 수 있습니다.

### 모든 워크플로에 유연하게 대응

웹 인터페이스는 기존 Claude Code 워크플로를 보완합니다. 클라우드에서 작업을 실행하는 것은 특히 다음과 같은 경우에 효과적입니다:

- 프로젝트 작동 방식과 저장소 매핑에 대한 질문 답변
- 버그 수정 및 일상적이고 명확히 정의된 작업
- 백엔드 변경 작업 - Claude Code가 테스트 주도 개발을 사용하여 변경 사항을 검증할 수 있는 경우

모바일에서도 Claude Code를 사용할 수 있습니다. 이번 연구 프리뷰의 일환으로 iOS 앱에서 Claude Code를 제공하여 개발자들이 이동 중에도 Claude와 코딩을 경험할 수 있도록 했습니다. 아직 초기 프리뷰 단계이며, 여러분의 피드백을 바탕으로 모바일 경험을 빠르게 개선할 계획입니다.

### 보안 우선 클라우드 실행

모든 Claude Code 작업은 네트워크 및 파일 시스템 제한이 적용된 격리된 샌드박스 환경에서 실행됩니다. Git 상호작용은 Claude가 승인된 저장소에만 접근할 수 있도록 보장하는 보안 프록시 서비스를 통해 처리되어 전체 워크플로 동안 코드와 자격 증명을 안전하게 보호합니다.

또한 사용자 정의 네트워크 구성을 추가하여 Claude Code가 샌드박스에서 연결할 수 있는 도메인을 선택할 수 있습니다. 예를 들어 Claude가 인터넷을 통해 npm 패키지를 다운로드하여 테스트를 실행하고 변경 사항을 검증할 수 있도록 허용할 수 있습니다.

<https://www.anthropic.com/news/claude-code-on-the-web>
