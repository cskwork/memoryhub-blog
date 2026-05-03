---
title: "Claude Code: 에이전트 코딩을 위한 모범 사례"
date: 2025-06-04T18:14:55+09:00
slug: "648-Claude-Code_-에이전트-코딩을-위한-모범-사례"
original_url: "https://memoryhub.tistory.com/648"
tistory_id: 648
draft: false
categories: ["데브 언어"]
tags: ["Vibe Coding"]
---

Anthropic이 개발한 Claude Code는 커맨드 라인(CLI) 기반의 에이전트 코딩 도구입니다[1]. 개발자는 이 도구를 통해 자연어 명령으로 코드를 작성, 편집, 디버깅하고, Git과 같은 개발 도구와 연동하여 워크플로우를 자동화할 수 있습니다[4][8][14]. Claude Code는 특정 워크플로를 강요하지 않는 유연한 로우레벨(low-level) 설계를 채택하여, 사용자가 자신의 환경에 맞게 자유롭게 커스터마이징할 수 있는 강력하고 안전한 코딩 환경을 제공합니다[1][10]. 다만 이러한 유연성으로 인해 처음 사용하는 개발자에게는 다소 학습이 필요할 수 있습니다[1].

이 글에서는 다양한 코드베이스와 언어, 환경에서 Claude Code를 효과적으로 사용하기 위한 팁과 모범 사례를 소개합니다.

### 1. 설정 사용자 정의

Claude Code는 프롬프트에 컨텍스트를 자동으로 가져오는 방식으로 작동합니다. 이 과정은 시간과 토큰을 소모할 수 있으므로, 환경을 최적화하여 효율을 높이는 것이 중요합니다.

**CLAUDE.md 파일 생성**  
`CLAUDE.md`는 대화 시작 시 Claude가 자동으로 컨텍스트에 포함하는 특수 파일입니다. 이 파일에 다음과 같은 정보를 문서화하면 유용합니다.

- 자주 사용하는 bash 명령어
- 핵심 파일 및 유틸리티 함수
- 코드 스타일 가이드라인 및 테스트 지침
- 저장소 규칙 (예: 브랜치 명명 규칙)
- 개발 환경 설정 정보
- 프로젝트 관련 특이사항이나 경고
- 그 외 Claude가 기억해야 할 정보

`CLAUDE.md` 파일은 특별한 형식 없이 간결하고 읽기 쉽게 작성하면 됩니다. 이 파일은 여러 위치에 둘 수 있습니다.

- **저장소 루트**: 가장 일반적인 사용법으로, `CLAUDE.md`로 저장하여 팀과 공유하거나, `.gitignore`에 추가 후 `CLAUDE.local.md`로 개인 설정을 관리할 수 있습니다.
- **상위 및 하위 디렉토리**: 모노레포(monorepo) 구조에서 여러 `CLAUDE.md` 파일을 계층적으로 로드하여 사용할 수 있습니다.
- **홈 폴더 (`~/.claude/CLAUDE.md`)**: 모든 Claude 세션에 전역적으로 적용됩니다.
- `/init` 명령을 실행하면 Claude가 자동으로 `CLAUDE.md` 파일을 생성해 줍니다.

**CLAUDE.md 파일 조정**  
`CLAUDE.md` 파일은 프롬프트의 일부가 되므로, 지속적인 개선이 필요합니다. 내용을 무작정 추가하기보다, 모델의 반응을 테스트하며 지침 준수율을 높이는 방향으로 수정하는 것이 좋습니다. `#` 키를 사용하여 Claude에게 지시하면 해당 내용이 `CLAUDE.md` 파일에 자동으로 통합되므로, 코딩 중 실시간으로 문서를 보강할 수 있습니다.

**허용 도구 목록 관리**  
기본적으로 Claude Code는 파일 쓰기나 특정 bash 명령어처럼 시스템을 수정할 수 있는 작업에 대해 사용자 권한을 요청합니다[5]. 이는 안전을 위한 보수적인 접근 방식으로, 허용 목록을 수정하여 자주 사용하는 안전한 도구(예: 파일 편집, git commit)에 대한 권한 요청을 생략할 수 있습니다.

- 세션 중 "항상 허용" 선택
- `/permissions` 명령어로 허용 목록 관리
- `.claude/settings.json` 또는 `~/.claude.json` 파일 직접 편집
- `--allowedTools` CLI 플래그를 사용하여 세션별 권한 설정

**GitHub 사용 시 gh CLI 설치**  
GitHub CLI(`gh`)가 설치되어 있으면, Claude는 이를 활용해 이슈 생성, 풀 리퀘스트(PR) 열기 등 GitHub 관련 작업을 더 원활하게 수행할 수 있습니다[4].

### 2. Claude에 더 많은 도구 제공

Claude는 셸 환경에 접근할 수 있으며, MCP(Model Context Protocol) 및 REST API를 통해 더 복잡한 도구도 활용할 수 있습니다[3][6].

- **bash 도구**: Claude는 `gh`와 같은 일반적인 유틸리티는 알고 있지만, 사용자 정의 도구는 별도의 설명이 필요합니다. 도구의 이름과 사용 예시를 알려주거나, `--help` 명령을 실행하도록 지시하여 스스로 학습하게 할 수 있습니다. 자주 쓰는 도구는 `CLAUDE.md`에 문서화하는 것이 좋습니다[6].
- **MCP와 함께 사용**: Claude Code는 MCP 서버와 클라이언트로 모두 작동합니다. `.mcp.json` 파일을 통해 Puppeteer나 Sentry 같은 서버를 프로젝트에 추가하면, 저장소에서 작업하는 모든 팀원이 해당 도구를 즉시 사용할 수 있습니다[6].
- **사용자 정의 슬래시 명령어**: 디버깅이나 로그 분석처럼 반복적인 작업은 `.claude/commands` 폴더에 프롬프트 템플릿을 저장하여 자신만의 슬래시 명령어로 만들 수 있습니다. 예를 들어, GitHub 이슈를 자동으로 수정하는 `/project:fix-github-issue` 같은 명령어를 만들 수 있습니다.

### 3. 일반적인 워크플로

Claude Code는 특정 워크플로를 강요하지 않지만, 커뮤니티에서 효과가 입증된 몇 가지 패턴이 있습니다[1].

- **탐색, 계획, 코딩, 커밋**: 복잡한 문제 해결에 적합한 범용 워크플로입니다. Claude에게 관련 파일을 읽고 계획을 세우게 한 뒤, 계획이 합리적이라고 판단되면 코딩을 지시하고 마지막으로 커밋과 PR 생성을 요청하는 방식입니다[6]. "think"와 같은 키워드를 사용하면 Claude가 더 깊이 생각하도록 유도할 수 있습니다.
- **테스트 주도 개발(TDD)**: 먼저 Claude에게 테스트 케이스를 작성하게 하고, 테스트가 실패하는 것을 확인한 후 커밋합니다. 그다음, 테스트를 통과하는 코드를 작성하도록 지시합니다. 이 과정에서 Claude는 코드 작성, 테스트 실행, 수정을 반복하며 결과물을 완성합니다.
- **시각적 목표 기반 개발**: Puppeteer와 같은 도구를 사용해 UI 스크린샷을 찍게 하거나, 디자인 목업(mockup) 이미지를 제공하여 시각적 목표를 제시합니다. Claude는 결과물이 목표와 일치할 때까지 코드를 수정하고 스크린샷을 찍는 과정을 반복합니다.
- **안전한 YOLO 모드**: `--dangerously-skip-permissions` 플래그를 사용하면 모든 권한 확인을 건너뛰고 Claude가 중단 없이 작업을 수행하게 할 수 있습니다. 린트 오류 수정처럼 예측 가능한 작업에 유용하지만, 데이터 손실 등의 위험이 있으므로 인터넷이 차단된 Docker 컨테이너 같은 격리된 환경에서 사용하는 것을 권장합니다.
- **코드베이스 Q&A**: 새로운 코드베이스에 적응할 때 유용합니다. "로깅은 어떻게 작동하나요?"와 같이 동료에게 물어볼 법한 질문을 하면, Claude가 코드베이스를 탐색하여 답변을 찾아줍니다[4][5].
- **Git 및 GitHub 연동**: Claude는 커밋 메시지 작성, git 히스토리 검색, 병합 충돌 해결 등 대부분의 Git 작업을 처리할 수 있습니다[4][11]. 또한 PR 생성, 코드 리뷰 의견 반영, 실패한 빌드 수정 등 GitHub 관련 작업도 자동화할 수 있습니다[4].
- **Jupyter 노트북 작업**: Jupyter 노트북을 읽고 쓰며, 이미지 출력을 해석하여 데이터 탐색 및 시각화 작업을 돕습니다. "미학적으로 보기 좋게" 만들어 달라고 요청하면 결과물의 시각적 품질을 높일 수 있습니다.

### 4. 워크플로 최적화

모든 워크플로에 적용할 수 있는 몇 가지 최적화 제안입니다[14].

- **구체적인 지침**: "foo.py에 테스트 추가"보다 "foo.py에 로그아웃된 사용자의 엣지 케이스를 다루는 테스트를 추가해 줘. 모의(mock)는 사용하지 마"와 같이 지침을 구체적으로 제공하면 성공률이 높아집니다.
- **이미지 활용**: 스크린샷을 붙여넣거나 파일 경로를 제공하여 Claude에게 시각적 컨텍스트를 제공하면 UI 개발이나 디버깅에 특히 유용합니다.
- **파일 및 URL 참조**: 탭(Tab) 완성을 사용해 파일이나 폴더를 빠르게 참조하고, URL을 직접 제공하여 Claude가 필요한 정보를 가져오게 할 수 있습니다.
- **조기 경로 수정**: 코딩 전 계획을 검토하고, `Esc` 키를 눌러 작업을 중단하거나 이전 프롬프트를 수정하여 Claude의 작업 방향을 조기에 수정하면 더 나은 결과를 더 빨리 얻을 수 있습니다.
- **컨텍스트 관리**: `/clear` 명령으로 컨텍스트 창을 주기적으로 초기화하여 관련 없는 정보가 성능에 영향을 미치는 것을 방지합니다.
- **체크리스트 활용**: 복잡한 작업 시 마크다운 파일이나 GitHub 이슈를 체크리스트로 사용하게 하면 Claude가 작업을 체계적으로 처리하여 성능을 높일 수 있습니다.
- **데이터 전달**: 프롬프트에 직접 붙여넣거나, 파이프(`|`)를 사용해 입력하거나, 파일을 읽게 하는 등 다양한 방식으로 데이터를 전달할 수 있습니다.

### 5. 헤드리스 모드를 사용한 인프라 자동화

Claude Code는 CI/CD나 Git 프리커밋 훅(pre-commit hook) 같은 비대화형 환경을 위한 헤드리스 모드를 지원합니다[1]. `-p` 플래그로 프롬프트를 전달하여 이 모드를 활성화할 수 있으며, GitHub 이슈 분류나 주관적인 코드 리뷰를 수행하는 린터(linter) 등으로 활용 가능합니다[14].

### 6. 다중 Claude 워크플로

여러 Claude 인스턴스를 병렬로 실행하면 더 복잡한 작업을 효율적으로 처리할 수 있습니다[1].

- **역할 분담**: 한 Claude가 코드를 작성하면 다른 Claude가 리뷰하거나 테스트를 작성하게 하여 결과물의 품질을 높일 수 있습니다.
- **여러 체크아웃 활용**: 여러 폴더에 Git 저장소를 체크아웃한 뒤, 각 폴더에서 다른 작업을 동시에 실행시켜 대기 시간을 줄일 수 있습니다.
- **git worktree 사용**: `git worktree`를 사용하면 동일한 저장소에서 여러 브랜치를 동시에 작업할 수 있어, 각기 다른 독립적인 작업을 병렬로 처리할 때 유용합니다.
- **사용자 정의 하네스**: 헤드리스 모드를 스크립트와 결합하여 대규모 코드 마이그레이션(팬아웃)이나 기존 데이터 파이프라인에 Claude를 통합(파이프라이닝)하는 고도로 자동화된 워크플로를 구축할 수 있습니다[14].

**출처**  
[1] Claude Code: 에이전트 코딩을 위한 모범 사례 - GeekNews <https://news.hada.io/topic?id=20430>  
[2] 클로드 코드 (Claude Code) 총정리 | AI 코딩 도구 설치 및 사용법 까지 <https://www.magicaiprompts.com/docs/claude/claude-code/>  
[3] Claude Code: 새로운 AI 코드 도우미의 가능성과 한계 <https://digitalbourgeois.tistory.com/951>  
[4] Claude Code - velog <https://velog.io/@yeonililiil/Claude-Code>  
[5] Claude Code overview - 루닥스 - 티스토리 <https://rudaks.tistory.com/entry/Claude-Code-%EB%B2%88%EC%97%AD-Claude-Code-%EA%B0%9C%EC%9A%94-Claude-Code-overview>  
[6] 개발자를 위한 궁극의 AI 어시스턴트, Claude Code 완전 정복 가이드 <https://digitalbourgeois.tistory.com/1308>  
[7] 코드 에디터의 종말? '클로드 코드(Claude Code)'의 등장 - 요즘IT <https://yozm.wishket.com/magazine/detail/3162/?data=UD5w1+U5rF0uSl5hLAJAuZMMHaM5MGOAlLF1nFAJQHk%3D>  
[8] Claude Code 개요 - Anthropic API <https://docs.anthropic.com/ko/docs/claude-code/overview>  
[9] 2025년 클로드 코드, AI 코딩 혁신 방법 - Apidog <https://apidog.com/kr/blog/claude-code-coding/>  
[10] [AI 코딩 에이전트 비교 번역] Claude Code vs. OpenAI Codex <https://rudaks.tistory.com/entry/AI-%EC%BD%94%EB%94%A9-%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8-%EB%B9%84%EA%B5%90-%EB%B2%88%EC%97%AD-Claude-Code-vs-OpenAI-Codex-2025%EB%85%84-AI-%EC%BD%94%EB%94%A9-%EB%B0%B0%ED%8B%80>  
[11] AI 코딩 도구의 진화, 앤트로픽 'Claude Code'의 실전 활용법. - Threads <https://www.threads.com/@choi.openai/post/DIvZ5SMvJX8/ai-%EC%BD%94%EB%94%A9-%EB%8F%84%EA%B5%AC%EC%9D%98-%EC%A7%84%ED%99%94-%EC%95%A4%ED%8A%B8%EB%A1%9C%ED%94%BD-claude-code%EC%9D%98-%EC%8B%A4%EC%A0%84-%ED%99%9C%EC%9A%A9%EB%B2%95%EC%95%A4%ED%8A%B8%EB%A1%9C%ED%94%BD%EC%9D%B4-%EC%B5%9C%EA%B7%BC-%EB%B0%9C%ED%91%9C%ED%95%9C-%EC%83%88%EB%A1%9C%EC%9A%B4-%EB%8F%84%EA%B5%AC-claude-code%EA%B0%80-%EA%B0%9C%EB%B0%9C%EC%9E%90%EB%93%A4%EC%97%90%EA%B2%8C-%EB%A7%8E%EC%9D%80->  
[12] Claude Code 사용 가이드 - 하이퍼리즘 기술 블로그 <https://tech.hyperithm.com/claude_code_guides>  
[13] GeekNews on X: "Claude Code: 에이전트 코딩을 위한 모범 사례 - X <https://x.com/GeekNewsHada/status/1913772292011921808>  
[14] 프로그래밍 programming.ai\_tools
