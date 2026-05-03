---
title: "클로드 코드(Claude Code) - 터미널에서 일하는 AI 동료 개발자 ?"
date: 2025-06-07T13:48:05+09:00
slug: "664-클로드-코드-Claude-Code-터미널에서-일하는-AI-동료-개발자"
original_url: "https://memoryhub.tistory.com/664"
tistory_id: 664
draft: false
categories: ["데브 언어"]
tags: ["Vibe Coding"]
---

혹시 코딩할 때마다 IDE, 터미널, 브라우저를 정신없이 오가며 지친 경험 없으신가요? 마치 내 프로젝트 전체를 이해하고 궂은일을 척척 해주는 주니어 개발자 동료가 있다면 어떨까 상상해보셨을 겁니다. 오늘 소개해 드릴 앤스로픽(Anthropic)의 '클로드 코드(Claude Code)'가 바로 그런 역할을 하는 도구입니다[2].

클로드 코드는 여러분의 터미널에 상주하는 AI 코딩 에이전트입니다[2][9]. 자연어 명령만으로 복잡한 코딩 작업을 위임할 수 있죠[4]. 이제부터 클로드 코드의 모든 것을 쉽고 자세하게 알려드리겠습니다.

## 등장 배경

과거의 AI 코딩 도우미는 대부분 별도의 채팅 창 형태였습니다. 개발자는 현재 작업 중인 코드 일부를 복사해서 붙여넣고, 맥락을 일일이 설명해야만 도움을 받을 수 있었죠. 이는 개발 흐름을 끊고, 전체 프로젝트 구조를 이해시키기 어려웠습니다.

하지만 클로드 코드는 개발 환경의 핵심인 '터미널'에 직접 통합됩니다[2][3]. 덕분에 개발자가 파일을 일일이 지정하지 않아도, '에이전트 검색(agentic search)'이라는 기술로 스스로 프로젝트 전체 구조와 의존성을 파악합니다[5]. 단순히 질문에 답하는 챗봇을 넘어, 실제 파일을 수정하고, 테스트를 실행하며, 커밋까지 하는 진짜 '동료'처럼 느껴지는 이유입니다[2].

## 클로드 코드의 핵심 기능: 이런 문제를 해결해요!

1. **복잡한 코드베이스도 한눈에 파악**: 새로운 프로젝트에 투입되거나 오픈 소스에 기여할 때, 방대한 코드를 파악하는 데만 며칠이 걸리곤 합니다[3]. 클로드 코드는 단 몇 초 만에 전체 코드베이스의 지도를 그리고 핵심 로직을 설명해줍니다[5]. 코드 아키텍처에 대해 질문하며 빠르게 적응할 수 있습니다[2][3].
2. **이슈 해결부터 PR까지 한 번에**: GitHub, GitLab 이슈를 읽고 문제 해결에 필요한 코드를 여러 파일에 걸쳐 작성합니다[5]. 이후 테스트를 실행하고, 실패하면 스스로 수정하며, 최종적으로 변경 사항을 커밋하고 PR(Pull Request)까지 생성할 수 있습니다[2][5]. 개발자는 커피 한잔하며 전체 과정을 감독하기만 하면 됩니다[5].
3. **리팩토링, 문서화, 버그 수정 자동화**: 코드 가독성을 높이기 위한 리팩토링, 빠진 주석이나 문서를 채워 넣는 작업, 원인 모를 버그 수정 등 지루하고 반복적인 작업을 자동화합니다[3]. 특히 오류 메시지를 분석해 근본 원인을 찾고 해결책을 제안하는 능력은 디버깅 시간을 획기적으로 줄여줍니다[3].

## 핵심 원리 및 활용법

클로드 코드는 정해진 워크플로우를 강요하지 않는 유연한 도구입니다[1]. 그중 가장 효과적이고 보편적인 활용법은 **'탐색 → 계획 → 구현 → 커밋'** 워크플로우입니다[1].

```
# 1. 탐색 (Explore) - 먼저 코드를 읽고 상황을 파악해!
# "logging.py 파일과 관련된 로직들을 분석해줘. 아직 코드는 작성하지 마."
claude "read the file that handles logging, but don't write any code yet."

# 2. 계획 (Plan) - 어떻게 해결할지 '생각'해봐.
# 'think', 'think hard' 키워드로 더 깊은 고민을 유도할 수 있습니다[1].
claude "think hard and make a plan to improve the logging logic."

# 3. 구현 (Code) - 이제 계획대로 코드를 작성해줘.
claude "implement the solution according to your plan. verify as you go."

# 4. 커밋 (Commit) - 끝났으면 커밋하고 PR까지!
claude "commit the result and create a pull request. update the README too."
```

이 외에도 클로드 코드는 다양한 고급 기능을 제공합니다.

| 기능 | 설명 | 사용 예시 |
| --- | --- | --- |
| **스크린샷 기반 개발** | 디자인 시안(이미지)을 보고 UI를 코드로 구현하고, 결과물을 스크린샷으로 찍어 비교하며 반복적으로 개선합니다[1]. | `claude "이 디자인 시안대로 웹페이지 만들어줘."` |
| **안전한 YOLO 모드** | `--dangerously-skip-permissions` 플래그로 권한 확인을 건너뛰어 린트 오류 수정이나 보일러플레이트 생성 같은 작업을 중단 없이 수행합니다. (컨테이너 환경 권장)[1] | `claude "모든 파일에 린트 규칙 적용해줘." --dangerously-skip-permissions` |
| **헤드리스 모드 (`-p`)** | `-p` 플래그를 사용하여 Claude Code를 다른 스크립트나 파이프라인에 통합합니다. 대규모 마이그레이션이나 데이터 처리 자동화에 유용합니다[1]. | `claude -p "foo.py를 React에서 Vue로 마이그레이션해줘."` |
| **외부 도구 연동** | 사용자의 bash 환경을 그대로 사용하며, MCP(Multi-Claude Protocol)나 REST API를 통해 Puppeteer 같은 복잡한 도구와도 연동할 수 있습니다[1]. | `claude "puppeteer로 현재 페이지 스크린샷 찍어줘."` |

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **YOLO 모드는 신중하게**: `--dangerously-skip-permissions` 옵션은 모든 권한 확인을 건너뛰므로 매우 편리하지만, 의도치 않은 데이터 손실이나 시스템 손상을 유발할 수 있습니다[1]. 린트 수정과 같이 위험도가 낮은 작업에 사용하되, 가급적 인터넷이 차단된 도커(Docker) 컨테이너 같은 격리된 환경에서 실행하는 것이 안전합니다[1].

? **꿀팁**

- **"Think" 키워드 활용**: 복잡한 문제를 맡길 때 프롬프트에 "think", "think hard", "think harder" 같은 단어를 포함시켜 보세요[1]. Claude가 대안을 더 신중하게 평가하고 깊이 생각할 시간을 갖게 되어 훨씬 질 좋은 계획을 세웁니다[1].
- **반복은 미덕**: AI가 만든 첫 결과물이 완벽하지 않을 수 있습니다. 특히 UI 코딩처럼 시각적인 결과물이 중요한 작업은, 스크린샷을 통해 피드백을 주며 2~3번 반복 수정하면 결과물의 완성도가 눈에 띄게 향상됩니다[1].
- **나만의 도구 알려주기**: Claude는 `git`, `gh` 같은 유명한 도구는 잘 알지만, 여러분이 직접 만든 커스텀 셸 스크립트나 도구는 모릅니다[1]. 도구의 이름과 사용 예시를 알려주거나, 프로젝트 내 `CLAUDE.md` 파일에 자주 쓰는 도구를 문서화해두면 Claude가 여러분의 도구를 똑똑하게 활용할 수 있습니다[1].

## 마치며

지금까지 터미널에서 일하는 AI 동료, 클로드 코드에 대해 알아보았습니다. 처음에는 생소하게 느껴질 수 있지만, 코드베이스 이해부터 PR 생성까지 개발의 전 과정을 돕는 강력한 파트너가 될 수 있습니다[5]. 이 글이 여러분의 개발 생산성을 한 단계 높이는 데 도움이 되었기를 바랍니다!

여러분은 Claude Code를 어떤 작업에 가장 먼저 사용해보고 싶으신가요? 댓글로 자유롭게 의견을 나눠주세요! ?‍♀️

## 참고 자료 ?

- [Claude Code 공식 문서](https://docs.anthropic.com/en/docs/claude-code/overview)
- [Claude Code 베스트 프랙티스](https://www.anthropic.com/engineering/claude-code-best-practices)
- [Claude Code GitHub 저장소](https://github.com/anthropics/claude-code)

---

#ClaudeCode #AI개발자 #코딩자동화 #개발생산성 #Anthropic

### 출처

[1] Claude Code: Best practices for agentic coding - Anthropic <https://www.anthropic.com/engineering/claude-code-best-practices>  
[2] Claude Code overview - Anthropic API <https://docs.anthropic.com/en/docs/claude-code/overview>  
[3] Claude Code: A Guide With Practical Examples - DataCamp <https://www.datacamp.com/tutorial/claude-code>  
[4] Using Claude Code with your Pro or Max Plan | Anthropic Help Center <https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan>  
[5] Claude Code: Deep Coding at Terminal Velocity \ Anthropic <https://www.anthropic.com/claude-code>  
[6] How I use Claude AI Projects on a Per-Feature basis to ... - Reddit <https://www.reddit.com/r/ClaudeAI/comments/1eei464/how_i_use_claude_ai_projects_on_a_perfeature/>  
[7] Mastering Claude Code in 30 minutes - YouTube <https://www.youtube.com/watch?v=6eBSHbLKuN0>  
[8] Using Claude Code and Supabase to Create a Hand-Tracking App <https://www.youtube.com/watch?v=TLKxx_-fdio>  
[9] anthropics/claude-code: Claude Code is an agentic coding ... - GitHub <https://github.com/anthropics/claude-code>  
[10] Programming programming.ai\_tools
