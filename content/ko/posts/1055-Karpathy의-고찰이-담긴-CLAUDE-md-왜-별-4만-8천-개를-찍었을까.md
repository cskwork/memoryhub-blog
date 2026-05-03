---
title: "? Karpathy의 고찰이 담긴 CLAUDE.md, 왜 별 4만 8천 개를 찍었을까?"
date: 2026-04-17T01:53:46+09:00
slug: "1055-Karpathy의-고찰이-담긴-CLAUDE-md-왜-별-4만-8천-개를-찍었을까"
original_url: "https://memoryhub.tistory.com/1055"
tistory_id: 1055
draft: false
cover:
  image: "/images/1055-Karpathy의-고찰이-담긴-CLAUDE-md-왜-별-4만-8천-개를-찍었을까/ChatGPT Image 2026년 4월 26일 오후 01_54_04.png"
  relative: false
  hidden: false
---

# 

![](/images/1055-Karpathy의-고찰이-담긴-CLAUDE-md-왜-별-4만-8천-개를-찍었을까/ChatGPT Image 2026년 4월 26일 오후 01_54_04.png)

Claude Code에게 "함수 하나만 고쳐줘"라고 했는데 파일 다섯 개가 통째로 갈려 나온 경험, 다들 한 번쯤 해보셨을 겁니다.

Andrej Karpathy도 트위터에서 똑같은 불만을 터뜨렸고, 한 개발자가 그 관찰을 단 70줄짜리 `CLAUDE.md` 한 장으로 정리해 올렸더니 단 몇 주 만에 스타가 4만 8천 개 넘게 붙었습니다.

이 글 하나로 그 파일이 무엇인지, 어떤 원칙이 들어있는지, 내 프로젝트에 어떻게 붙이는지까지 정리해 드립니다.

## 한줄요약

Karpathy의 LLM 코딩 관찰을 70줄로 압축한 `CLAUDE.md`를 붙이면 Claude Code의 과잉 수정·근거 없는 가정·범위 이탈을 눈에 띄게 줄일 수 있습니다.

## 왜 지금 뜨는가

Andrej Karpathy는 2026년 1월 26일 X(옛 트위터)에서 LLM 코딩 도구의 고질병 세 가지를 짚었습니다.

- 근거 없는 가정 — 확인 없이 맥락을 지어냅니다
- 과잉 엔지니어링 — 요청에 없던 추상화와 옵션을 덧붙입니다
- 범위 이탈 — 건드리지 말아야 할 코드까지 "개선"합니다

다음 날 개발자 Forrest Chang이 이를 `CLAUDE.md`라는 한 장짜리 행동 지침으로 옮겨 공개했고, 2026년 4월 기준 저장소 스타는 48,309개에 달합니다. 파일 한 개짜리 저장소가 기여자 수천 명의 인기 오픈소스를 제친 보기 드문 사례입니다.

| 용어 | 의미 |
| --- | --- |
| CLAUDE.md | Claude Code가 세션 시작 시 자동으로 읽는 프로젝트 규칙 파일 |
| Claude Code | Anthropic이 공식 배포하는 CLI 코딩 어시스턴트 |
| Plugin marketplace | Claude Code에서 규칙·에이전트 묶음을 공유하는 배포 채널 |

## 4원칙의 핵심

> 한 줄 정의: 네 개의 원칙으로 LLM이 개발자처럼 "멈추고, 줄이고, 좁히고, 검증"하도록 만드는 시스템 프롬프트입니다.  
> 핵심은 새 기능이 아니라 "제약"을 심어주는 데 있습니다.

- **Think Before Coding** — 가정을 드러내고, 모호하면 일단 멈춰서 묻습니다 ("Don't assume. Don't hide confusion.").
- **Simplicity First** — 요청 외 기능·추상화·방어 코드 금지입니다. 200줄짜리를 50줄로 줄일 수 있으면 다시 씁니다.
- **Surgical Changes** — 바꿔야 할 줄만 바꾸고, 내 변경 때문에 쓰이지 않게 된 임포트만 정리합니다.
- **Goal-Driven Execution** — "기능 추가" 같은 모호한 지시를 "테스트 통과"처럼 검증 가능한 목표로 바꿉니다.

Goal-Driven 원칙의 변환 방식을 Claude Code CLI v1.x 환경에서 보면 이렇게 생겼습니다.

```
# 모호한 지시 → 검증 가능한 목표
"입력 검증 추가" → "잘못된 입력용 테스트를 먼저 쓰고, 그 테스트를 통과시켜라"
"버그 수정"      → "버그를 재현하는 테스트를 쓴 뒤, 그 테스트를 통과시켜라"
"X 리팩터링"     → "리팩터 전후로 기존 테스트가 모두 통과하는지 확인하라"
```

## 내 프로젝트에 붙이는 3단계

#### ① 방식 선택

플러그인으로 받거나, 원문 파일을 직접 내려받는 두 가지 길이 있습니다. 여러 프로젝트에 공유하려면 플러그인이,

이 프로젝트에서만 쓰려면 파일 복사가 편합니다.

#### ② 플러그인 방식 (권장)

Claude Code CLI에서 아래 두 줄을 차례대로 입력합니다.

```
# Claude Code CLI v1.x
/plugin marketplace add forrestchang/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-skills
```

실행 결과(텍스트 대체): `Installed karpathy-skills plugin. CLAUDE.md rules are now active in this project.` 비슷한 메시지가 뜨면 성공입니다.

#### ③ 파일 직접 병합 방식

이미 프로젝트 루트에 `CLAUDE.md`가 있다면 원문을 내려받아 이어 붙이면 됩니다.

```
curl -fsSL https://raw.githubusercontent.com/forrestchang/andrej-karpathy-skills/main/CLAUDE.md \
  >> ./CLAUDE.md
```

적용 후 Claude Code 세션을 새로 열면 규칙이 자동으로 로드됩니다. 세션 상단에 `CLAUDE.md loaded` 비슷한 로그가 찍혔는지 꼭 확인하세요.

## 어떤 방식이 더 맞을까

| 적용 방식 | 장점 | 주의점 |
| --- | --- | --- |
| Plugin 설치 | 여러 프로젝트에 한 번에 적용, 업데이트 자동 반영 | 팀원 전원이 동일 마켓플레이스 권한 필요, 사내 정책과 충돌 가능 |
| 파일 직접 병합 | 프로젝트별 커스터마이징 자유, 오프라인 환경 OK | 원본 업데이트를 수동 추적해야 하고, 기존 규칙과 중복 여부 점검 필요 |
| 일부 원칙만 발췌 | 팀 컨벤션과의 충돌을 최소화 | Surgical Changes처럼 맞물리는 원칙은 부분 적용 시 효과 반감 |

## 마치며

4만 8천 개의 별이 증명한 교훈은 단순합니다. LLM 코딩 도구에 필요한 건 더 많은 기능이 아니라 더 명확한 제약이라는 점입니다.

오늘 저녁 프로젝트 루트에 한 번만 붙여 두면, 내일부터 Claude Code의 과잉 수정 피로도가 눈에 띄게 줄어들 겁니다.

## 참고자료

- forrestchang/andrej-karpathy-skills 저장소 — <https://github.com/forrestchang/andrej-karpathy-skills>
- CLAUDE.md 원문 — <https://github.com/forrestchang/andrej-karpathy-skills/blob/main/CLAUDE.md>
- antigravity.codes, "Karpathy's CLAUDE.md Skills File: The Complete Guide" — <https://antigravity.codes/blog/karpathy-claude-code-skills-guide>
- explainx.ai, "Karpathy-inspired Claude Code guidelines" — <https://explainx.ai/blog/karpathy-claude-code-guidelines-andrej-karpathy-skills>
- DEV Community, "Karpathy's CLAUDE.md Template: 5,800 Stars and What It Does" — <https://dev.to/max_quimby/karpathys-claudemd-template-5800-stars-and-what-it-does-4a09>
