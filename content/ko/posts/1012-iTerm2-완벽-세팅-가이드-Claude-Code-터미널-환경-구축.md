---
title: "? iTerm2 완벽 세팅 가이드: Claude Code 터미널 환경 구축"
date: 2026-02-07T13:46:00+09:00
slug: "1012-iTerm2-완벽-세팅-가이드-Claude-Code-터미널-환경-구축"
original_url: "https://memoryhub.tistory.com/1012"
tistory_id: 1012
draft: false
---

```
  ╔═══════════════════════════════════════════════════════════╗
  ║                                                           ║
  ║    ┌──────────────────────────────────────────────┐       ║
  ║    │  $ claude                                    │       ║
  ║    │  ╭──────────────────────────────────────╮    │       ║
  ║    │  │ > Plan mode (Shift+Tab)              │    │       ║
  ║    │  │ > Analyzing codebase...              │    │       ║
  ║    │  │ > 5 sessions running in parallel     │    │       ║
  ║    │  ╰──────────────────────────────────────╯    │       ║
  ║    │                                              │       ║
  ║    │  [Tab1:claude] [Tab2:claude] [Tab3:dev]      │       ║
  ║    │   ██ Backend    ██ Frontend   ██ Testing      │       ║
  ║    │                                              │       ║
  ║    │  iTerm2 + Oh My Zsh + Claude Code            │       ║
  ║    └──────────────────────────────────────────────┘       ║
  ║                                                           ║
  ║     AI 코딩 시대, 터미널이 가장 중요한 이유              ║
  ╚═══════════════════════════════════════════════════════════╝
```

터미널은 그냥 검은 화면에 글자나 치는 곳이라고 생각하시나요? Claude Code 개발자 Boris Cherny는 iTerm2에서 탭 5개를 열고, 각 탭마다 Claude를 동시에 돌립니다. 한쪽에서 백엔드를 짜는 동안, 다른 탭에서는 프론트엔드 코드가 자동으로 완성되고 있죠.

이 워크플로우의 출발점은 화려한 AI가 아니라, 제대로 세팅된 터미널 환경입니다.

**AI 코딩 도구의 성능은 터미널 설정이 80%를 결정합니다.**

**한줄요약:** 결론부터 말하면, iTerm2에 Oh My Zsh, Powerlevel10k, 핵심 플러그인을 세팅하고 Claude Code 전용 설정까지 마치면,

AI 코딩 생산성이 체감상 2배 이상 올라간다.

---

## 배경

macOS에는 기본 터미널 앱(Terminal.app)이 있습니다. 간단한 명령어를 실행하기엔 충분하지만, AI 코딩 도구를 본격적으로 사용하려면 한계가 분명합니다.

> iTerm2는 macOS의 기본 Terminal.app을 대체하는 오픈소스 터미널 에뮬레이터로, 화면 분할, 핫키 윈도우, Shell Integration, AI Chat 등 개발자에게 필수적인 기능을 제공한다.

기본 터미널의 문제는 세 가지입니다.

**첫째**, Claude Code가 작업을 완료했을 때 알림을 받을 수 없습니다. 탭을 왔다 갔다 하며 완료 여부를 확인해야 하죠.

**둘째**, 화면 분할이 불편하거나 아예 불가능합니다. AI 에이전트를 병렬로 돌리려면 여러 터미널 창을 따로 열어야 합니다.

**셋째**, 긴 출력을 스크롤하거나 과거 명령어를 검색하는 기능이 빈약합니다.

iTerm2는 이 문제를 모두 해결합니다. 2025년 9월에 출시된 최신 버전 3.6은 AI Chat 기능까지 내장했습니다.

LLM이 터미널 내용을 읽고 명령어를 설명해주거나, 직접 실행까지 할 수 있는 수준입니다.

하지만 이 글에서는 "있어 보이는 기능"보다 **실제로 AI 코딩 생산성에 직결되는 설정**에 집중합니다.

| 비교 항목 | Terminal.app | iTerm2 |
| --- | --- | --- |
| 화면 분할 | 불가 | 수직/수평 자유 분할 |
| 시스템 알림 | 미지원 | 작업 완료 알림 지원 |
| Shift+Enter | 수동 설정 필요 | 기본 지원 |
| 핫키 윈도우 | 없음 | 전역 단축키로 즉시 호출 |
| 스크롤백 | 제한적 | 무제한 설정 가능 |
| tmux 통합 | 기본 | 네이티브 창/탭으로 변환 |
| Shell Integration | 없음 | 명령어 추적, 디렉토리 기록 |

---

## 실습

### 1. iTerm2 설치

Homebrew가 설치되어 있다면 한 줄이면 끝납니다. Homebrew가 없다면 먼저 설치해야 합니다.

```
# Homebrew 설치 (이미 있다면 건너뛰기)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# iTerm2 설치
brew install --cask iterm2
```

설치 후 iTerm2를 처음 실행하면 "인터넷에서 다운로드한 앱"이라는 경고가 뜹니다. "열기"를 눌러 진행합니다.

이 시점에서는 기본 터미널과 큰 차이를 느끼기 어렵습니다. 차이는 설정에서 나옵니다.

### 2. Oh My Zsh 설치

macOS는 Catalina(10.15)부터 기본 셸이 Zsh입니다. Oh My Zsh는 이 Zsh의 설정을 쉽게 관리해주는 프레임워크로, 200개 이상의 플러그인과 140개 이상의 테마를 제공합니다.

```
# 현재 셸 확인
echo $SHELL
# /bin/zsh가 출력되면 정상

# Oh My Zsh 설치
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

설치가 완료되면 홈 디렉토리에 `.zshrc` 파일이 생성됩니다. 이 파일이 앞으로 모든 셸 설정의 중심이 됩니다.

### 3. Powerlevel10k 테마 설치

Oh My Zsh의 기본 테마(robbyrussell)는 심플하지만 정보가 부족합니다. Powerlevel10k는 Git 브랜치, 실행 시간, 에러 코드 등을 프롬프트에 실시간으로 표시해줍니다. AI 코딩 도구를 쓸 때 현재 브랜치와 작업 상태를 한눈에 파악하는 것은 중요합니다.

```
# Powerlevel10k 설치
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git \
  ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

설치 후 `.zshrc` 파일에서 테마를 변경합니다.

```
# .zshrc 편집 (vi, nano, 또는 VS Code 중 편한 것 사용)
code ~/.zshrc   # VS Code
# 또는
nano ~/.zshrc   # 터미널 내장 편집기
```

아래 줄을 찾아 수정합니다.

```
# 변경 전
ZSH_THEME="robbyrussell"

# 변경 후
ZSH_THEME="powerlevel10k/powerlevel10k"
```

저장 후 iTerm2를 재시작하면 Powerlevel10k 설정 마법사가 자동으로 실행됩니다.

마법사에서 **Meslo Nerd Font 설치 여부를 물으면 반드시 "y"를 선택**합니다. 이 폰트가 없으면 아이콘이 물음표로 깨져 보입니다.

설정 마법사에서 선택하는 항목들은 순전히 취향입니다.

나중에 `p10k configure` 명령어로 언제든 다시 설정할 수 있으니 부담 없이 진행하면 됩니다.

### 4. 필수 플러그인 3종 설치

Oh My Zsh의 진짜 가치는 플러그인에 있습니다.

수백 개 중에서 AI 코딩 워크플로우에 실질적으로 도움이 되는 3개만 설치합니다.

**zsh-autosuggestions** - 과거 입력 기반 자동완성

```
git clone https://github.com/zsh-users/zsh-autosuggestions \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

이전에 입력한 명령어를 흐린 글씨로 제안해줍니다. `git commit`, `docker compose up` 같은 반복 명령어를 매번 타이핑할 필요가 없어집니다. 오른쪽 화살표 키로 수락합니다.

**zsh-syntax-highlighting** - 실시간 문법 하이라이팅

```
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git \
  ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

존재하는 명령어는 초록색, 잘못된 명령어는 빨간색으로 표시됩니다. Enter를 누르기 전에 오타를 잡을 수 있어서 특히 긴 파이프라인 명령어를 작성할 때 유용합니다.

**autojump** - 디렉토리 빠른 이동

```
brew install autojump
```

`cd ~/Projects/my-app/src/components` 대신 `j components`만 입력하면 됩니다.

방문 빈도를 학습해서 가장 자주 가는 디렉토리로 점프합니다.

세 플러그인을 모두 설치했으면 `.zshrc`의 plugins 항목을 수정합니다.

```
# .zshrc에서 plugins 줄을 찾아 수정
plugins=(
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  autojump
)
```

변경사항을 적용합니다.

```
source ~/.zshrc
```

### 5. iTerm2 핵심 설정 5가지

설치만으로는 부족합니다.

AI 코딩 도구와 함께 쓸 때 체감 차이를 만드는 설정 5가지를 적용합니다.

**① 무제한 스크롤백 설정**

Claude Code는 대량의 코드를 출력하는 경우가 많습니다. 기본 스크롤백 버퍼로는 이전 출력이 잘려나갑니다.

설정 경로: Settings > Profiles > Terminal > Scrollback Buffer  
"Unlimited scrollback"을 체크합니다.

**② 시스템 알림 설정**

Claude Code가 긴 작업을 끝냈을 때 macOS 알림을 받을 수 있습니다. 이 설정이 없으면 작업 완료를 확인하려고 계속 탭을 전환해야 합니다.

설정 경로: Settings > Profiles > Terminal  
"Silence bell"을 체크하고, Filter Alerts에서 "Send escape sequence-generated alerts"를 활성화합니다.

추가로 macOS 시스템 설정 > 알림 > iTerm2에서 알림을 허용해야 합니다.

**③ Option 키 설정**

Claude Code에서 `Option+Enter`로 줄바꿈을 사용하려면 이 설정이 필요합니다.

설정 경로: Settings > Profiles > Keys > General  
Left Option key를 "Esc+"로 변경합니다.

**④ 핫키 윈도우 등록**

어떤 앱을 쓰고 있든 단축키 하나로 터미널을 즉시 불러올 수 있습니다. 코드를 읽다가 바로 Claude Code에 질문하고 싶을 때 유용합니다.

설정 경로: Settings > Keys > Hotkey > "Show/hide all windows with a system-wide hotkey"  
원하는 단축키를 등록합니다. 흔히 `Option+Space`를 사용합니다.

**⑤ 상태 바 활성화**

현재 CPU, 메모리 사용량, 배터리 상태를 터미널 하단에 표시할 수 있습니다. Claude Code가 무거운 작업을 돌릴 때 시스템 리소스를 모니터링하기 좋습니다.

설정 경로: Settings > Profiles > Session > "Status bar enabled" 체크  
"Configure Status Bar"에서 원하는 컴포넌트를 드래그하여 추가합니다.

### 6. Claude Code 전용 설정

iTerm2 기본 설정을 마쳤으니 Claude Code에 최적화된 설정을 추가합니다.

**Shift+Enter 줄바꿈**

iTerm2에서는 Shift+Enter가 기본 지원됩니다. 별도 설정 없이 Claude Code에서 여러 줄 입력이 가능합니다. Warp나 Alacritty 같은 다른 터미널에서는 Claude Code 내에서 `/terminal-setup` 명령어를 실행해야 하지만,

iTerm2 사용자는 이 과정이 필요 없습니다.

**알림 훅 설정**

기본 시스템 알림보다 더 정교한 알림이 필요하다면 Claude Code의 훅 시스템을 활용할 수 있습니다.

예를 들어, 작업 완료 시 macOS 알림 대화상자를 띄우려면 프로젝트의 `.claude/settings.json`에 아래 내용을 추가합니다.

```
{
  "hooks": [
    {
      "matcher": "Notification",
      "hooks": [{
        "type": "command",
        "command": "osascript -e 'display notification \"Task complete\" with title \"Claude Code\"'"
      }]
    }
  ]
}
```

**병렬 세션 운영**

Claude Code 개발자 Boris Cherny의 워크플로우처럼 여러 Claude 세션을 동시에 운영하려면, iTerm2의 탭에 번호를 매기는 것이 효과적입니다. Settings > Appearance > Tab bar location에서 탭 바 위치를 조정하고,

각 탭의 이름을 "Backend", "Frontend", "Test"처럼 역할별로 지정합니다.

탭 이름 변경: 탭을 더블클릭하거나 `Cmd+Shift+I`로 세션 정보를 열어 Badge에 역할 이름을 입력합니다.

**CLAUDE.md 활용**

Claude Code는 프로젝트 루트의 `CLAUDE.md` 파일을 자동으로 읽어 프로젝트 컨텍스트를 파악합니다.

이 파일에 코딩 규칙, 프로젝트 구조, 자주 발생하는 실수 등을 기록해두면 AI의 코드 품질이 눈에 띄게 향상됩니다. 팀 전체가 하나의 `CLAUDE.md`를 git에 관리하며 지속적으로 업데이트하는 것이 모범 사례입니다.

### 7. 생산성 향상 보조 도구

터미널 경험을 한 단계 끌어올리는 CLI 도구 3가지입니다.

```
# bat: 문법 강조가 되는 cat 대체
brew install bat

# lsd: 아이콘이 포함된 ls 대체
brew install lsd

# fzf: 퍼지 검색 (Ctrl+R로 명령어 히스토리 검색)
brew install fzf
$(brew --prefix)/opt/fzf/install
```

bat은 Claude Code가 출력한 코드를 검토할 때 가독성을 높여줍니다. fzf는 `Ctrl+R`을 눌러 과거 명령어를 퍼지 검색할 수 있게 해주는데, 복잡한 Docker나 kubectl 명령어를 반복 실행할 때 특히 유용합니다.

---

## 모범사례/패턴 비교

| 패턴 | 장점 | 주의점 |
| --- | --- | --- |
| 탭별 Claude 세션 분리 | 백엔드/프론트엔드 병렬 개발 가능 | 시스템 리소스 소비 증가, 메모리 모니터링 필요 |
| 화면 분할(Split Panes) | 코드와 실행 결과를 동시에 확인 | 화면이 작으면 오히려 가독성 저하 |
| 핫키 윈도우 활용 | 앱 전환 없이 즉시 터미널 접근 | 다른 앱의 단축키와 충돌할 수 있음 |
| tmux 통합 사용 | SSH 끊김에도 세션 유지, 원격 작업에 적합 | 학습 곡선 존재, 로컬 작업에는 과할 수 있음 |
| 알림 훅 설정 | 긴 작업 완료를 놓치지 않음 | 과도한 알림은 오히려 집중력 방해 |

---

## 마치며

- iTerm2는 단순히 "예쁜 터미널"이 아니라, AI 코딩 도구의 성능을 극대화하는 인프라다
- Oh My Zsh + Powerlevel10k + 플러그인 3종(autosuggestions, syntax-highlighting, autojump)으로 기본 생산성을 확보하고, Claude Code 전용 알림과 병렬 세션 설정으로 AI 코딩 워크플로우를 완성할 수 있다
- 실전 팁: 오늘 당장 iTerm2를 설치하고, 이 글의 "실습" 섹션을 1번부터 7번까지 순서대로 따라해보세요. 30분이면 완료됩니다.

---

## 참고자료

- iTerm2 공식 사이트 (<https://iterm2.com/>)
- iTerm2 GitHub 저장소 (<https://github.com/gnachman/iTerm2>)
- Oh My Zsh 공식 사이트 (<https://ohmyz.sh/>)
- Powerlevel10k GitHub (<https://github.com/romkatv/powerlevel10k>)
- Claude Code 터미널 설정 공식 문서 (<https://code.claude.com/docs/en/terminal-config>)
- Boris Cherny의 Claude Code 워크플로우 (<https://twitter-thread.com/t/2007179832300581177>)
