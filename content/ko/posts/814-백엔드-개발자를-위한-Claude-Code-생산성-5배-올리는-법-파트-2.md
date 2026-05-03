---
title: "⚡ 백엔드 개발자를 위한 Claude Code 생산성 5배 올리는 법 파트 2"
date: 2025-10-01T23:18:43+09:00
slug: "814-백엔드-개발자를-위한-Claude-Code-생산성-5배-올리는-법-파트-2"
original_url: "https://memoryhub.tistory.com/814"
tistory_id: 814
draft: false
---

### ⑥ MCP로 실제 데이터베이스와 대화하기

**문제상황**

API 개발 중 실제 데이터 구조를 확인하거나 쿼리 결과를 검증하려면 별도 도구를 오가야 합니다.

**해결방법**

Model Context Protocol(MCP)은 AI와 외부 데이터 소스를 연결하는 개방형 표준입니다. Postgres, GitHub, Slack, JIRA 등 수백 개의 도구에 Claude가 직접 접근할 수 있습니다.

```
# Postgres MCP 서버 추가
claude mcp add postgres \
  -e DATABASE_URL=postgresql://user:pass@localhost:5432/mydb \
  -- npx @modelcontextprotocol/server-postgres

# 이제 Claude에게 직접 요청
프롬프트:
"Postgres를 조회해서 최근 7일간 가입한 사용자 중 
아직 주문을 하지 않은 사용자 리스트를 가져와.
그리고 이들에게 보낼 마케팅 이메일 템플릿을 작성해줘."
```

Claude Code는 JIRA 이슈를 읽고 기능을 구현한 뒤 GitHub PR을 생성하고, Sentry로 모니터링 데이터를 분석하는 등 워크플로우 자동화가 가능합니다.

**백엔드 개발자를 위한 필수 MCP**

MCP 서버 용도 설정 예시

|  |  |  |
| --- | --- | --- |
| **Postgres** | DB 스키마 분석, 쿼리 최적화 | 공식 MCP 서버 저장소 제공 |
| **GitHub** | PR 생성, 이슈 관리, 코드 리뷰 | Personal Access Token 필요 |
| **Context7** | 최신 라이브러리 문서 자동 검색 | 무료, 회원가입 필요 |
| **Claude Context** | 전체 코드베이스를 시맨틱 검색으로 색인화 | Vector DB 연결 |

---

### ⑦ 스크린샷으로 API 문서 직접 전달

**문제상황**

복잡한 API 스펙이나 아키텍처 다이어그램을 텍스트로 설명하면 오해가 생깁니다.

**해결방법**

Claude는 이미지와 다이어그램 처리에 뛰어나며, 스크린샷을 붙여넣거나 드래그 앤 드롭할 수 있습니다.

```
# macOS 단축키: Cmd+Ctrl+Shift+4 (클립보드로 스크린샷)
# 터미널에서 Ctrl+V로 붙여넣기 (Cmd+V 아님!)

프롬프트:
"이 Swagger 문서 스크린샷을 보고 
Node.js + Express로 동일한 API 엔드포인트를 구현해줘.
validation, error handling, OpenAPI 주석까지 포함."
```

**활용 예시**

- Postman 응답 화면 → 에러 디버깅
- ERD 다이어그램 → 데이터베이스 스키마 생성
- 디자인 목업 → Admin 패널 UI 구현
- 성능 모니터링 그래프 → 최적화 방향 분석

디자인 목업을 참조해 UI를 개발하거나, 차트를 분석해 디버깅하는 데 특히 효과적입니다.

---

### ⑧ URL 페이스트로 최신 프레임워크 문서 참조

**문제상황**

Next.js 15, Prisma 6 등 빠르게 업데이트되는 프레임워크의 최신 API를 Claude가 모를 수 있습니다.

**해결방법**

프롬프트에 URL을 직접 붙여넣으면 Claude가 해당 페이지를 읽어옴니다.

```
프롬프트:
"https://nextjs.org/docs/app/api-reference/functions/cookies
이 공식 문서를 참고해서 Next.js 15에서 
쿠키를 읽고 설정하는 API 미들웨어를 작성해줘."
```

**생산성 팁**

/permissions 명령으로 자주 쓰는 도메인을 허용 목록에 추가하면 권한 프롬프트 없이 자동으로 접근합니다.

```
claude
/permissions

# 허용할 도메인 추가
docs.nestjs.com
docs.spring.io
prisma.io/docs
```

이제 NestJS나 Prisma 문서 URL을 붙여넣으면 즉시 최신 정보를 기반으로 코드를 생성합니다.

---

### ⑨ 체크리스트 방식으로 대규모 마이그레이션

**문제상황**

수백 개 파일의 import 경로 변경, 레거시 API 제거, 린트 에러 수정 같은 대규모 작업은 Claude가 중간에 멈추거나 놓치는 경우가 있습니다.

**해결방법**

Markdown 파일이나 GitHub 이슈를 체크리스트 작업 공간으로 활용합니다.

```
프롬프트:
"1단계: 린트를 실행하고 모든 에러를 파일명과 라인 번호를 포함해서 
LINT_ERRORS.md에 체크리스트로 작성해줘.

2단계: 체크리스트의 각 항목을 하나씩 수정하고, 
수정 완료하면 체크박스를 체크해줘.

3단계: 각 수정 후 린트를 다시 실행해서 에러가 사라졌는지 확인.

4단계: 모든 체크박스가 완료될 때까지 반복."
```

**LINT\_ERRORS.md 예시**

```
# 린트 에러 수정 체크리스트

## 타입 에러
- [ ] src/api/users.ts:45 - 'User' 타입에 'email' 속성 없음
- [ ] src/api/orders.ts:128 - 'Promise<void>' 타입을 'number'에 할당 불가
- [x] src/utils/date.ts:12 - 'Date' 타입 파라미터 누락 ✅

## 사용하지 않는 import
- [ ] src/services/auth.ts:3 - 'bcrypt' import 미사용
...
```

코드 마이그레이션, 빌드 스크립트 실행, 수많은 린트 에러 수정 같은 복잡한 다단계 작업에서 성능이 향상됩니다.

---

### ⑩ 커밋 메시지와 PR 설명 자동 생성

**문제상황**

코드 작성에 집중하다 보면 커밋 메시지와 PR 설명이 부실해집니다.

**해결방법**

Claude는 명확한 PR 설명과 의미 있는 커밋 메시지 작성에 탁월하며, 완벽한 기억력 덕분에 놓치는 내용이 없음니다.

```
# 작업 완료 후
프롬프트:
"지금까지 구현한 결제 시스템 관련 변경사항을 
의미 있는 단위로 나눠서 커밋해줘.

각 커밋 메시지는 Conventional Commits 형식으로:
- feat: 새 기능
- fix: 버그 수정
- refactor: 리팩토링
- test: 테스트 추가

그리고 GitHub PR 설명도 작성해줘. 포함할 내용:
- 변경 내용 요약
- 기술적 구현 세부사항
- 테스트 방법
- 관련 JIRA 티켓 번호"
```

**생성 예시**

```
# Claude가 자동으로 실행하는 git 명령들

git add src/payment/tosspayments.service.ts
git commit -m "feat: 토스페이먼츠 API 연동 서비스 구현

- 결제 요청/승인/취소 메서드 추가
- 웹훅 서명 검증 로직 구현
- Retry 로직 포함 (최대 3회)"

git add src/payment/payment.entity.ts src/payment/dto/
git commit -m "feat: Payment 엔티티 및 DTO 정의

- Prisma 스키마에 Payment 테이블 추가
- 결제 상태 enum (PENDING/COMPLETED/FAILED)
- 환불 관련 필드 포함"

git add tests/payment/tosspayments.spec.ts
git commit -m "test: 토스페이먼츠 서비스 통합 테스트 작성

- 정상 결제 시나리오
- 결제 실패 처리
- 웹훅 검증 테스트"
```

사람보다 더 나은 커밋 메시지를 작성하는 경우가 많으며, 협업 커뮤니케이션이 매끄러워짐니다.

---

## 보너스: 아키텍처 수준 질문

Claude는 단순 검색을 넘어 아키텍처 수준의 질의를 이해합니다.

```
프롬프트 예시:
"사용자 인증이 앱 전체에서 어떻게 흐르는지 보여줘"
"UserContext에 의존하는 모든 컴포넌트를 찾아줘"
"제품 데이터가 API 호출부터 UI 렌더링까지 어떻게 흐르는지 추적"
"모듈 구조에서 순환 의존성을 찾아줘"
```

이런 고수준 질문은 레거시 코드 이해나 복잡한 시스템 리팩토링에서 시간을 크게 절약해줍니다.

---

## 마치며

**추가로 배운 점 5줄**

- MCP로 데이터베이스, GitHub, JIRA를 직접 연결하면 컨텍스트 스위칭 제거
- 스크린샷과 URL 페이스트로 최신 정보를 Claude에게 실시간 주입
- 체크리스트 방식은 대규모 마이그레이션을 안정적으로 완수
- 커밋/PR 자동화로 코드 이력 품질이 팀 전체에 향상
- 아키텍처 질문 능력은 Claude를 시니어 컨설턴트처럼 활용 가능

**최종 실전 팁**  
Claude Code Max 플랜(월 100달러)은 월 2시간만 절약해도 본전이며, 토큰 걱정 없는 무제한 사용이 생산성의 핵심입니다. 백엔드 개발자라면 MCP + 멀티 인스턴스 + TDD 조합이 가장 강력합니다.

---

## 참고자료 (업데이트)

- [Anthropic - MCP 공식 소개](https://www.anthropic.com/news/model-context-protocol)
- [Claude Code MCP 연동 가이드](https://docs.claude.com/en/docs/claude-code/mcp)
- [MCP 서버 저장소 (Postgres, GitHub 등)](https://github.com/modelcontextprotocol/servers)
- [Context7 MCP - 최신 문서 자동 검색](https://context7.com/)
