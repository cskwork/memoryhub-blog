---
title: "? Claude Code Auto Memory, CLAUDE.md만으로는 부족한 이유"
date: 2026-02-27T06:29:36+09:00
slug: "1044-Claude-Code-Auto-Memory-CLAUDE-md만으로는-부족한-이유"
original_url: "https://memoryhub.tistory.com/1044"
tistory_id: 1044
draft: false
---

```
  ╔══════════════════════════════════════════════╗
  ║                                              ║
  ║    ~/.claude/projects/my-app/memory/          ║
  ║    ├── MEMORY.md    ← Claude가 직접 작성     ║
  ║    ├── debugging.md                          ║
  ║    ├── api-conventions.md                    ║
  ║    └── ...                                   ║
  ║                                              ║
  ║    "세션이 끝나도, 기억은 남는다"              ║
  ║                                              ║
  ╚══════════════════════════════════════════════╝
```

매일 아침 출근할 때마다 동료에게 프로젝트 히스토리를 처음부터 다시 설명해야 한다면 어떨까. Claude Code를 쓰면서 비슷한 경험을 한 적이 있을 것이다. 어제 분명히 "우리 프로젝트는 pnpm을 쓴다"고 말했는데, 오늘 새 세션을 열면 또 npm install을 시도하는 Claude. CLAUDE.md에 규칙을 적어두면 되지 않냐고? 그건 내가 직접 써야 하는 "지시서"다.

**Auto Memory는 Claude가 작업하면서 스스로 학습 노트를 작성하고, 다음 세션에서 자동으로 불러오는 시스템이다.**

**한줄요약:** 결론부터 말하면, Claude Code의 Auto Memory는 CLAUDE.md와 별개로 Claude가 프로젝트 패턴과 학습 내용을 자동 기록하는 메모리 시스템이며, 이를 이해하고 관리하면 세션 간 맥락 유지 효율이 크게 달라진다.

---

## 배경

LLM은 본질적으로 상태를 갖지 않는(stateless) 시스템이다. 세션이 끝나면 컨텍스트 윈도우에 있던 모든 정보가 사라진다.

Claude Code 사용자 대부분은 이 문제를 CLAUDE.md 파일로 해결해왔다.

프로젝트 루트에 마크다운 파일을 두면 매 세션 시작 시 자동으로 로드되니까.

그런데 여기에 한 가지 근본적인 한계가 있다. CLAUDE.md는 내가 미리 알고 있는 것만 적을 수 있다. 작업하다 발견한 디버깅 패턴이나, 코드베이스의 숨겨진 규칙같은 것들은 그때그때 수동으로 기록해야 한다. 대부분의 개발자는 이걸 잊어버린다.

> Auto Memory는 Claude가 작업 중 발견한 학습 내용, 패턴, 인사이트를 자동으로 기록하는 영속 디렉토리다.

Anthropic은 이 문제를 해결하기 위해 Auto Memory 기능을 도입했다. 기본적으로 활성화되어 있으며, Claude Code 2.1.32 버전부터 본격적으로 적용되었다. CLAUDE.md가 "개발자가 Claude에게 쓴 지시서"라면,

Auto Memory는 "Claude가 자기 자신을 위해 쓴 학습 노트"에 해당한다.

---

## CLAUDE.md vs Auto Memory(MEMORY.md) 핵심 차이

이 둘을 혼동하는 경우가 많다. 역할이 완전히 다르다.

| 구분 | CLAUDE.md | Auto Memory (MEMORY.md) |
| --- | --- | --- |
| 작성 주체 | 개발자가 직접 작성 | Claude가 자동 작성 |
| 저장 위치 | 프로젝트 루트 또는 홈 디렉토리 | `~/.claude/projects/<project>/memory/` |
| 내용 | 코딩 규칙, 컨벤션, 지시사항 | 프로젝트 패턴, 디버깅 인사이트, 선호도 |
| 로딩 방식 | 전체 내용 자동 로드 | MEMORY.md 첫 200줄만 자동 로드 |
| 버전 관리 | Git에 커밋 가능 | .gitignore에 추가 권장 |
| 팀 공유 | 팀 전체 공유용 | 개인 로컬 전용 |

비유하자면, CLAUDE.md는 회사 위키에 적어둔 "팀 개발 가이드"고,

Auto Memory는 개인 노트에 적어둔 "이 프로젝트에서 내가 발견한 것들"이다.

---

## Auto Memory 동작 원리

### 디렉토리 구조

Auto Memory는 프로젝트별로 독립된 디렉토리를 생성한다. 경로는 Git 저장소 루트를 기준으로 결정된다.

```
~/.claude/projects/<project>/memory/
├── MEMORY.md           # 핵심 인덱스 (매 세션 자동 로드)
├── debugging.md        # 디버깅 패턴 상세 노트
├── api-conventions.md  # API 설계 결정사항
└── ...
```

Git 저장소가 없는 경우, 현재 작업 디렉토리가 기준이 된다. 같은 저장소의 하위 디렉토리들은 하나의 Auto Memory 디렉토리를 공유한다. **Git worktree는 별도의 메모리 디렉토리를 갖는다는 점**에 주의해야 한다.

### 200줄 제한 규칙

MEMORY.md에는 중요한 제약이 있다. 매 세션 시작 시 **첫 200줄만 시스템 프롬프트에 주입**된다.

200줄을 초과하면 Claude가 다음과 같은 경고를 보여준다.

```
WARNING: MEMORY.md is N lines (limit: 200). 
Only the first 200 lines were loaded. 
Move detailed content into separate topic files 
and keep MEMORY.md as a concise index.
```

이 설계는 의도적이다. MEMORY.md는 간결한 인덱스로 유지하고, 상세한 내용은 별도의 토픽 파일로 분리하라는 구조다.

토픽 파일(debugging.md, api-conventions.md 등)은 시작 시 자동 로드되지 않는다.

Claude가 해당 정보가 필요할 때 파일 도구를 사용해 on-demand로 읽는다.

### Claude가 기록하는 내용

Auto Memory에 Claude가 자동으로 기록하는 정보는 대체로 다음과 같다.

- 프로젝트에서 반복 사용되는 명령어(빌드, 테스트, 배포 스크립트)
- 코드베이스의 아키텍처 패턴과 설계 결정
- 디버깅 과정에서 발견한 문제 해결 방법
- 사용자가 선호하는 작업 방식과 도구

작업 중 "writing memory" 또는 "reading memory"라는 메시지가 나타나면,

Claude가 Auto Memory를 갱신하거나 참조하고 있는 것이다.

---

## 실습

### 1. Auto Memory 상태 확인

Claude Code 터미널에서 `/memory` 명령을 실행한다.

현재 프로젝트에 연결된 모든 메모리 파일(CLAUDE.md + Auto Memory)이 표시된다.

Auto Memory 토글 스위치도 이 화면에서 확인할 수 있다.

이미 `~/.claude/projects/` 하위에 memory 디렉토리가 존재한다면, Auto Memory가 활성 상태인 것이다.

### 2. Claude에게 직접 기억 요청하기

자연어로 명시적 저장을 요청할 수 있다.

```
"remember that we use pnpm, not npm"
"save to memory that the API tests require a local Redis instance"
"이 프로젝트에서는 항상 vitest를 사용한다고 기억해"
```

Claude는 이 내용을 MEMORY.md에 기록하고, 이후 세션에서 자동으로 참조한다.

### 3. MEMORY.md 직접 편집

Auto Memory 파일은 일반 마크다운이므로 언제든 직접 편집할 수 있다. `/memory` 명령으로 파일 선택기를 열거나,

경로를 직접 접근하면 된다.

```
# 현재 프로젝트의 Auto Memory 확인
cat ~/.claude/projects/<프로젝트경로>/memory/MEMORY.md

# 불필요한 항목 정리
code ~/.claude/projects/<프로젝트경로>/memory/MEMORY.md
```

### 4. Auto Memory 비활성화

프로젝트별로 또는 전역으로 비활성화할 수 있다.

**방법 1: /memory 토글**

`/memory` 실행 후 auto-memory 토글을 끄면 된다.

**방법 2: settings.json**

```
// ~/.claude/settings.json
{
  "autoMemoryEnabled": false
}
```

**방법 3: 환경 변수 (CI/관리 환경용)**

```
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1  # 강제 비활성화
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=0  # 강제 활성화
```

환경 변수는 `/memory` 토글과 settings.json보다 우선순위가 높다. CI 파이프라인이나 관리형 환경에서 일관된 동작을 보장하려면 이 방법이 적합하다.

---

## 모범사례/패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| MEMORY.md를 인덱스로, 토픽 파일로 분리 | 200줄 제한 극복, 체계적 관리 | 토픽 파일은 자동 로드 안 됨 |
| "remember that..." 자연어 저장 | 작업 흐름 끊김 없이 즉시 저장 | Claude가 판단해서 저장하므로 표현이 달라질 수 있음 |
| 주기적 MEMORY.md 리뷰/정리 | 오래된 정보 제거, 토큰 절약 | 월 1회 이상 수동 점검 필요 |
| Auto Memory + CLAUDE.md 병행 | 지시사항과 학습 내용 분리 | 둘 사이 규칙 충돌 가능성 있음 |
| CI에서 환경 변수로 비활성화 | 재현 가능한 빌드 환경 유지 | 개발 환경에서는 활성화 유지 권장 |

---

## 메모리 계층 전체 구조

Claude Code의 메모리 시스템은 4개 계층으로 구성된다. 충돌 시 더 구체적인(하위) 파일이 우선한다.

```
1. 사용자 전역    ~/.claude/CLAUDE.md           (모든 프로젝트 공통)
2. 프로젝트       ./CLAUDE.md                   (팀 공유, Git 커밋)
3. 모듈 규칙      .claude/rules/*.md            (경로별 조건부 적용)
4. Auto Memory    ~/.claude/projects/.../memory/ (Claude 자동 기록, 개인용)
```

이 구조를 이해하면 "어디에 무엇을 넣을지"가 명확해진다. 모든 프로젝트에 적용할 개인 스타일은 전역 파일에, 팀 컨벤션은 프로젝트 CLAUDE.md에, 특정 디렉토리 규칙은 모듈 규칙에, 나머지는 Auto Memory가 알아서 처리하도록 두면 된다.

---

## 마치며

- Claude Code의 Auto Memory는 CLAUDE.md와 별개로, Claude가 작업 중 발견한 패턴과 인사이트를 자동 기록하는 시스템이다.
- MEMORY.md의 첫 200줄만 자동 로드되므로, 간결한 인덱스 + 토픽 파일 분리 구조가 핵심이다.
- 실전 팁: 오늘 당장 `/memory` 명령으로 현재 프로젝트의 Auto Memory 상태를 확인하고, 불필요한 항목이 있다면 정리해보자.

---

## 참고자료

- Manage Claude's memory - Claude Code Docs (<https://code.claude.com/docs/en/memory>)
- Memory tool - Claude API Docs (<https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool>)
- Claude Code's Experimental Memory System (<https://giuseppegurgone.com/claude-memory>)
- Claude Code Best Practices: Memory Management (<https://cuong.io/blog/2025/06/15-claude-code-best-practices-memory-management>)
