---
title: "Cursor, Codex, Claude Code: 파일 읽기/쓰기 권한 제한, 한 번에 끝내는 실전 가이드 (2025)"
date: 2025-09-23T09:01:41+09:00
slug: "786-Cursor-Codex-Claude-Code-파일-읽기-쓰기-권한-제한-한-번에-끝내는-실전-가이드-2025"
original_url: "https://memoryhub.tistory.com/786"
tistory_id: 786
draft: false
---

개발용 AI 에이전트가 점점 “에디터+터미널+브라우저”까지 건드리다 보니, **어떤 파일을 읽거나 수정해도 되는지**를 선명하게 통제하는 게 안전과 생산성 모두에서 핵심이 됐죠.

이 글은 **Cursor, Codex, Claude Code**에서 “특정 파일/폴더의 **읽기·쓰기 제한**”을 실제로 어떻게 거는지, **설정 예시와 주의점까지** 한 번에 정리합니다.

---

## 한눈 비교 (요약)

도구 읽기 차단 방식 쓰기(수정) 제어 포인트/주의

|  |  |  |  |
| --- | --- | --- | --- |
| **Cursor** | .cursorignore로 **AI 기능 전반의 파일 접근 차단** (인덱싱·탭·채팅·@심볼) | 기본적으로 파일 수정은 쉽게 되지만 **명령/위험 작업은 승인 필요** | 터미널/MCP 같은 **외부 도구 호출은 .cursorignore로 완전 차단 불가** → 비밀파일은 **워크스페이스 밖/OS 권한으로** 보호 권장. ([Cursor Documentation](https://docs.cursor.com/ja/context/ignore-files)) |
| **Codex** | **샌드박스 모드**로 전역 제어: Read-only / Auto / Full Access | **승인(approval) 모드**로 명령/수정 허용 범위 조절 | 기본값은 **워크스페이스 내 읽기/쓰기 허용·외부는 승인 요구**, 세분화된 ignore 파일은 **아직(요청 이슈 존재)**. ([OpenAI 개발자](https://developers.openai.com/codex/security/?utm_source=chatgpt.com)) |
| **Claude Code** | .claude/settings.json에 **권한 규칙**: deny/allow/ask + 글롭 패턴 | /permissions, **allowlist**, **hooks**, canUseTool로 촘촘히 | 규칙 예: Read(./.env) **deny**, Write(./production/\*\*) **ask** — SDK에서도 동일 규칙 사용. ([Claude Docs](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-permissions)) |

---

# 1) Cursor: **.cursorignore**로 “읽기” 자체를 막고, 위험 작업은 승인

### 핵심 설정

- 프로젝트 루트에 \*\*.cursorignore\*\*를 두면 Cursor가 그 파일/폴더를 **인덱싱·탭·채팅·@심볼 컨텍스트에서 통째로 못 보게** 합니다. Gitignore 문법을 그대로 씁니다. 예:또한 필요하면 인덱싱만 제외하는 \*\*.cursorindexingignore\*\*도 제공됩니다. ([Cursor Documentation](https://docs.cursor.com/ja/context/ignore-files))
- # 민감정보 .env secrets/\*\* \*.pem # 대용량/불필요 dist/ \*.log
- **계층적(ignore 상위 폴더 탐색)** 기능을 켜면 상위 디렉터리의 .cursorignore도 적용됩니다. (Settings → Features → Editor → Hierarchical Cursor Ignore) ([Cursor Documentation](https://docs.cursor.com/ja/context/ignore-files))

### 쓰기(수정)와 명령 실행

- **읽기**는 기본적으로 승인 없이 가능(단, .cursorignore로 막으면 접근 불가).  
  **명령 실행·네트워크 등 민감 작업은 기본 승인 필요**하며, 일부는 allowlist가 있지만 **보안 통제 수단으로는 권장되지 않습니다**. ([Cursor Documentation](https://docs.cursor.com/en/account/agent-security))

### 실무 주의점

- .cursorignore는 **에디터·인덱서·대화 컨텍스트**에 강력하지만, **터미널/MCP 같은 “외부 도구 호출”까지 OS 레벨에서 막아주진 않습니다.** 승인해 주면 cat secrets.env 같은 쉘로 읽을 수 있죠.  
  → **비밀파일은 워크스페이스 밖**으로 빼거나 \*\*OS 권한(ACL/권한비트)\*\*로 추가 보호하세요. ([Cursor Documentation](https://docs.cursor.com/ja/context/ignore-files))

---

# 2) Codex: **샌드박스 & 승인(approvals) 모드**로 읽기/쓰기를 단계별 제한

### 핵심 개념

- Codex(2025)의 CLI/IDE 확장엔 **샌드박스**와 **승인(approval) 모드**가 있습니다.
  - 기본값(**Auto/기본 모드**): **워크스페이스 안**에서는 파일 읽기·수정·명령이 자연스럽게 진행되며, **바깥/네트워크 등 위험 작업은 승인 요청**.
  - **Read-only**: **읽기만 가능**(수정/명령 금지).
  - **Full Access**: 경고 수준. 승인 프롬프트 최소화(실험용 권장). ([OpenAI 개발자](https://developers.openai.com/codex/security/?utm_source=chatgpt.com))

### 실전 레시피

- **읽기만 허용(완전 안전 모드)**
- codex --sandbox read-only --ask-for-approval never # 워크스페이스 읽기만, 어떤 승인도 묻지 않음
- **기본(작업 편의) 모드**: 워크스페이스 내 수정·명령은 자연스럽게, 위험 작업만 승인.  
  필요 시 /approvals 커맨드로 모드 전환. ([OpenAI 개발자](https://developers.openai.com/codex/security/?utm_source=chatgpt.com))

### 현재 한계 & 팁

- .codexignore 같은 **세밀한 파일 수준 denylist는 공식 제공 X(요청 이슈 진행 중)**. 민감 파일은 **프로젝트 밖**으로 빼거나 **OS 권한**으로 보호하세요. ([GitHub](https://github.com/openai/codex/issues/1397?utm_source=chatgpt.com))

---

# 3) Claude Code: **settings.json 권한 규칙** + **hooks/canUseTool**로 촘촘 제어

### 가장 쉬운 방법: .claude/settings.json

아래처럼 “허용/거부/질문” 규칙을 **글롭 패턴**으로 선언합니다.

```
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./secrets/**)",
      "WebFetch"
    ],
    "ask": [
      "Write(./production/**)",
      "Bash(git push:*)"
    ],
    "allow": [
      "Bash(npm run test:*)",
      "Read(~/.zshrc)"
    ]
  }
}
```

- 규칙은 deny → allow → ask → (그 외) canUseTool 순서로 평가됩니다.
- 파일 규칙은 **글롭**(./secrets/\*\*), Bash 규칙은 **접두사 매칭**(Bash(npm:\*)). ([Claude Docs](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-permissions))

### 더 촘촘히

- **/permissions 커맨드**나 **allowlist**로 세션별 도구 허용을 관리.
- **canUseTool 콜백**: 런타임에 “허용/거부”를 코드로 결정.
- **Hooks(PreToolUse/PostToolUse)**: 실행 전후 가로채 로깅·검증·차단. ([Anthropic](https://www.anthropic.com/engineering/claude-code-best-practices))

> 참고: 일부 버전에서 설정 무시 이슈 리포트가 있었으니(업데이트로 해결될 수 있음) 최신 버전 동작을 꼭 확인하세요. ([GitHub](https://github.com/anthropics/claude-code/issues/3501?utm_source=chatgpt.com))

---

## 바로 가져다 쓰는 **권한 레시피**

### Cursor

```
# .cursorignore (루트)
.env
secrets/**
**/*.pem
dist/
*.log
```

- 상위 폴더의 규칙도 적용하려면 **Hierarchical Cursor Ignore**를 켜세요.
- 인덱싱만 제외하려면 .cursorindexingignore를 사용. ([Cursor Documentation](https://docs.cursor.com/ja/context/ignore-files))

### Codex

```
# 읽기 전용 세션 시작
codex --sandbox read-only --ask-for-approval never

# 기본 모드(워크스페이스 내부는 자연스럽게 작업, 위험 작업은 승인)
codex            # 세션 내 /approvals 로 모드 전환 가능
```

- 민감파일은 **워크스페이스 밖** 또는 \*\*OS 권한(읽기 전용/소유자만)\*\*으로 보호. ([OpenAI 개발자](https://developers.openai.com/codex/security/?utm_source=chatgpt.com))

### Claude Code

```
// .claude/settings.json
{
  "permissions": {
    "deny":  ["Read(./.env)", "Read(./secrets/**)"],
    "ask":   ["Write(./production/**)", "Bash(git push:*)"],
    "allow": ["Bash(npm run test:*)"]
  }
}
```

- 필요하면 **hooks**로 추가 감시·차단 로직을 붙이세요. ([Claude Docs](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-permissions))

---

## 안전을 완성하는 **미니 체크리스트**

- **비밀파일은 저장소 밖**(혹은 배포 시스템의 시크릿 매니저)
- 에이전트는 **브랜치/깃 관리 하에서**만 작업
- Cursor는 \*\*.cursorignore\*\*로 읽기 자체를 차단
- Codex는 **Read-only/Auto 모드**를 적절히 전환
- Claude Code는 \*\*.claude/settings.json\*\*으로 deny/ask/allow 선언
- 승인(approvals)은 **기본값 유지** + 필요한 항목만 점진적 완화

---

## 참고문서

- Cursor: **Ignore files**, **Agent Security**, **Codebase Indexing**. ([Cursor Documentation](https://docs.cursor.com/ja/context/ignore-files))
- Codex: **Security & Sandbox/Approval 모드**(공식 가이드), **모드 정리 글**, **ignore 파일 기능 요청 이슈**. ([OpenAI 개발자](https://developers.openai.com/codex/security/?utm_source=chatgpt.com))
- Claude Code: **Permissions(설정/규칙/훅/SDK)**, **Best Practices(allowlist·/permissions)**. ([Claude Docs](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-permissions))

---

### 한 줄 결론

**읽기는 .cursorignore / 쓰기는 승인·규칙(Approvals/Rules)** — 이 조합만 탄탄히 잡아도 **대부분의 사고는 미리 막을 수 있습니다.**
