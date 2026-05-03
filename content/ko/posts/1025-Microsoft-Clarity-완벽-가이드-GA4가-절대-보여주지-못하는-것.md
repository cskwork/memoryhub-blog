---
title: "? Microsoft Clarity 완벽 가이드 — GA4가 절대 보여주지 못하는 것"
date: 2026-02-14T14:46:38+09:00
slug: "1025-Microsoft-Clarity-완벽-가이드-GA4가-절대-보여주지-못하는-것"
original_url: "https://memoryhub.tistory.com/1025"
tistory_id: 1025
draft: false
---

```
  ╔══════════════════════════════════════════╗
  ║                                          ║
  ║    [  CLARITY  ]     ◉ Click             ║
  ║    ┌──────────────┐  ◉ Scroll            ║
  ║    │ ████░░░░░░░░ │  ◉ Rage Click        ║
  ║    │ ██████░░░░░░ │                       ║
  ║    │ ████████████ │  ► Session Replay     ║
  ║    │ ██░░░░░░░░░░ │  ► Heatmap           ║
  ║    └──────────────┘  ► AI Copilot         ║
  ║                                          ║
  ║    Microsoft Clarity  ──  FREE Forever   ║
  ║                                          ║
  ╚══════════════════════════════════════════╝
```

Google Analytics 대시보드를 열면 이탈률 75%라는 숫자가 보입니다. 그런데 정작 궁금한 건 "왜?"입니다. 사용자가 어디서 헤매고, 어떤 버튼을 클릭했는데 반응이 없어서 떠났는지, 숫자만으로는 절대 알 수 없습니다. **Microsoft Clarity는 GA4가 "무엇이 일어났는지" 보여준다면, "왜 일어났는지"를 눈으로 보여주는 도구입니다.** 그것도 완전 무료로.

**한줄요약:** 결론부터 말하면, Microsoft Clarity는 히트맵과 세션 리플레이를 무제한 무료로 제공하는 행동 분석 도구로, GA4와 함께 쓰면 웹사이트 UX 문제를 데이터가 아닌 "눈"으로 진단할 수 있습니다.

---

## 배경

웹 분석 도구 시장은 오랫동안 Google Analytics가 지배해왔습니다. 트래픽 수, 유입 경로, 전환율 같은 정량적 데이터를 보는 데는 탁월하지만, 한 가지 치명적인 한계가 있습니다.

사용자가 실제로 화면에서 무엇을 했는지 보여주지 못한다는 점입니다.

이 문제를 해결하기 위해 Hotjar, Crazy Egg 같은 행동 분석 도구가 등장했지만, 대부분 유료입니다.

Hotjar의 유료 플랜은 월 39달러부터 시작하고, 트래픽이 늘면 비용이 급격히 올라갑니다.

2020년 말, Microsoft가 Clarity를 출시하면서 판도가 바뀌었습니다. 핵심 차별점은 단 하나.

**완전 무료이면서 트래픽 제한이 없다**는 것입니다.

> Microsoft Clarity는 사용자가 웹사이트와 어떻게 상호작용하는지를 시각적으로 보여주는 무료 행동 분석 도구입니다. 히트맵, 세션 녹화, AI 기반 인사이트를 제공합니다.

2025년 12월 기준, Clarity는 출시 5주년을 맞았습니다. 단순한 히트맵 도구에서 AI 기반 인사이트 플랫폼으로 진화했으며, 매일 10,000개 이상의 모바일 앱이 Clarity SDK를 사용하고 있습니다.

Capterra에서 4.8/5.0 평점을 받을 만큼, "무료라서 쓰는 도구"가 아니라 "무료인데 이래도 되나 싶은 도구"로 자리 잡았습니다.

---

## Clarity의 핵심 기능

### 세션 리플레이: 사용자의 눈으로 사이트를 본다

세션 리플레이는 실제 사용자의 방문 과정을 영상처럼 재생하는 기능입니다. 마우스 움직임, 클릭, 스크롤, 페이지 이동까지 그대로 볼 수 있습니다.

단순히 "녹화"하는 수준을 넘어, Clarity는 세션 내 이벤트 타임라인을 제공합니다. 2025년 업데이트로 이벤트 유형별 필터링이 가능해져서, 긴 녹화 영상에서 Rage Click이 발생한 순간만 골라서 볼 수 있습니다. 탭 간 전환도 정확한 순서대로 표시됩니다.

가장 주목할 점은 **Clarity Copilot**입니다. 최대 250개의 세션 녹화를 AI가 한꺼번에 분석해 공통 행동 패턴, 불편 요소, 트렌드를 자연어로 요약해줍니다. 녹화를 하나하나 시청하는 것이 아니라,

AI가 "사용자의 43%가 가격 페이지에서 이탈했으며, 주로 비교 표가 로딩되기 전에 떠났습니다"처럼 핵심을 짚어줍니다.

### 히트맵: 데이터를 색으로 읽는다

히트맵은 사용자의 클릭, 스크롤, 관심 영역을 색상으로 시각화합니다. Clarity는 일반적인 클릭/스크롤 맵 외에도 다양한 유형을 제공합니다.

| 히트맵 유형 | 보여주는 것 | 활용 포인트 |
| --- | --- | --- |
| Click Map | 클릭이 집중된 영역 | CTA 버튼 위치 최적화 |
| Scroll Map | 사용자가 어디까지 스크롤했는지 | 핵심 콘텐츠 배치 전략 |
| Area Map | 특정 영역의 클릭 합계 | 네비게이션 효과 측정 |
| Attention Map | 사용자가 오래 머문 구간 | 콘텐츠 관심도 파악 |
| Dead Click Map | 클릭했지만 반응이 없던 곳 | UI 버그 발견 |
| Rage Click Map | 분노의 연속 클릭 발생 지점 | 핵심 UX 문제 즉시 파악 |

특히 **Dead Click과 Rage Click 감지**는 Clarity의 가장 실용적인 기능입니다.

Dead Click은 사용자가 클릭했지만 아무 반응이 없는 요소를 찾아냅니다. Rage Click은 사용자가 같은 지점을 빠르게 반복 클릭한 것으로, 심각한 불만의 신호입니다.

실제 사례를 보면, 한 SaaS 기업은 Clarity에서 "무료 체험 시작" 버튼에 Rage Click이 집중되는 것을 발견했습니다.

세션 리플레이로 확인해보니 버튼 클릭 후 시각적 피드백이 나타나기까지 1.5초의 지연이 있었습니다.

로딩 메시지를 추가하자 Rage Click이 사라지고 체험 전환율이 개선되었습니다.

### 2025년 주요 업데이트

Clarity는 2025년 한 해 동안 공격적으로 기능을 확장했습니다. 주요 변화를 정리하면 다음과 같습니다.

**AI 트래픽 채널 추적**: ChatGPT, Claude, Gemini 같은 AI 플랫폼에서 유입된 방문자를 별도 채널로 분류합니다. AI 유입 사용자는 홈페이지를 건너뛰고 사이트 깊은 곳으로 바로 도착하며, 전환율이 더 높은 경향이 있습니다. AI Platform과 Paid AI Platform 채널이 신설되었습니다.

**Clarity Notes**: 세션 녹화의 특정 시점에 팀원들과 코멘트를 남길 수 있습니다. 스크린샷을 찍어서 이메일로 보내는 번거로운 워크플로가 사라지고, 모든 논의가 녹화 안에서 이루어집니다.

**Trends 기능**: 기존에 정적 데이터 포인트로만 제공되던 분석 결과를 장기 추세로 시각화합니다. 사용자 참여도의 급증이나 갑작스러운 이탈을 시간축에서 파악할 수 있습니다.

**Flutter SDK 지원**: 기존 iOS/Android 네이티브 SDK에 이어, Flutter 앱에서도 Clarity를 사용할 수 있게 되었습니다.

**EEA/UK 동의 모드 강제**: 2025년 10월 31일부터 유럽 경제 지역, 영국, 스위스 방문자에 대해 쿠키 동의 신호가 필수가 되었습니다. Google Consent Mode와 연동됩니다.

---

## 실습: Clarity 설치부터 GA4 연동까지

### 1단계: 프로젝트 생성

clarity.microsoft.com에 접속해 Microsoft, Google, 또는 Facebook 계정으로 로그인합니다. "New project"를 클릭하고, 사이트 이름과 URL을 입력합니다. 카테고리를 선택하면 프로젝트가 생성됩니다.

### 2단계: 추적 코드 설치

프로젝트 생성 후 Settings > Setup으로 이동합니다. 세 가지 설치 방법이 있습니다.

**직접 설치**: "Get tracking code"를 클릭하면 JavaScript 스니펫이 나타납니다. 이 코드를 웹사이트의 `<head>` 태그 안에 붙여넣습니다.

```
<!-- HTML의 <head> 섹션에 삽입 -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        // Clarity 추적 코드
        // 프로젝트별 고유 ID가 포함됨
    })(window, document, "clarity", "script", "YOUR_PROJECT_ID");
</script>
```

**플랫폼 연동**: WordPress, Shopify, Wix, Squarespace 등은 전용 플러그인이나 앱을 통해 코드 수정 없이 설치할 수 있습니다. WordPress의 경우 공식 Microsoft Clarity 플러그인을 설치하고 인증하면 끝입니다.

**GTM(Google Tag Manager) 연동**: GTM 컨테이너에서 새 태그를 생성하고,

Custom HTML로 Clarity 스크립트를 붙여넣습니다. 트리거는 All Pages로 설정합니다.

### 3단계: 설치 확인

코드 설치 후 사이트에 접속하여 브라우저 개발자 도구(F12)의 Network 탭에서 `clarity.ms/collect`로 POST 요청이 발생하는지 확인합니다. 요청이 보이면 정상 설치된 것입니다. 데이터는 수분 내로 대시보드에 나타나기 시작합니다.

### 4단계: GA4 연동

Clarity의 진가는 GA4와 함께 사용할 때 드러납니다. Settings > Setup에서 Google Analytics Integration의 "Get Started"를 클릭합니다. Google 계정으로 로그인한 뒤 연동할 GA4 속성을 선택하고 Save를 누릅니다.

연동이 완료되면 Clarity 대시보드에 Google Analytics 탭이 나타납니다. GA4의 인기 페이지, 유입 경로, 국가별 세션 데이터가 Clarity 안에서 보이고, 각 데이터 포인트에서 바로 관련 히트맵이나 세션 녹화로 이동할 수 있습니다.

GA4 측에서도 Clarity의 세션 녹화 재생 URL이 커스텀 디멘션으로 전달되어, GA4 탐색 보고서에서 특정 세션의 녹화를 바로 재생할 수 있습니다.

---

## Clarity vs Hotjar: 어떤 상황에서 무엇을 쓸까

가장 많이 비교되는 두 도구의 차이를 실질적인 기준으로 정리합니다.

| 비교 항목 | Microsoft Clarity | Hotjar |
| --- | --- | --- |
| 가격 | 완전 무료, 트래픽 제한 없음 | 무료 플랜(일 35세션), 유료 월 $39~ |
| 세션 녹화 | 무제한 | 무료 플랜 제한, 유료는 샘플링 |
| 히트맵 | 클릭, 스크롤, 영역, Dead/Rage Click | 클릭, 스크롤, 이동, Rage, Engagement Zone |
| AI 요약 | Copilot(250개 세션 동시 분석) | AI 기반 요약(제한적) |
| 설문/피드백 | 미지원 | 설문, 피드백 위젯, 인터뷰 도구 |
| 퍼널 분석 | 기본 수준 | 전환 퍼널 분석 제공 |
| 모바일 앱 | iOS, Android, Flutter SDK | 웹 전용 |
| 데이터 프라이버시 | MS가 익명화된 데이터를 ML/광고에 활용 | 프라이버시 우선 정책 |
| 통합 | GA4, MS Ads, Shopify | Slack, Jira, Mixpanel 등 다수 |

정리하면 이렇습니다. 예산이 제한적이고 히트맵/세션 녹화가 핵심 필요라면 Clarity가 압도적입니다.

반면 사용자 설문, 피드백 수집, 팀 협업 워크플로가 중요하다면 Hotjar가 적합합니다. 실무에서는 Clarity로 시각적 행동 데이터를, GA4로 정량 데이터를 보는 조합이 가장 효율적입니다.

다만 한 가지 알아둘 점이 있습니다. Clarity의 무료 모델에는 대가가 따릅니다. Microsoft는 Clarity를 통해 수집된 익명화 데이터를 머신러닝 모델 개선과 광고 서비스에 활용할 수 있습니다. 의료, 금융, 정부 관련 웹사이트에서는 사용이 제한되며, GDPR 관련 개별 사용자 데이터 삭제 요청 처리에 제약이 있습니다.

프라이버시에 민감한 서비스라면 이 점을 반드시 고려해야 합니다.

---

## 마치며

- Microsoft Clarity는 히트맵, 세션 리플레이, AI 기반 인사이트를 완전 무료로 무제한 제공하는 행동 분석 도구입니다. GA4가 "무엇이" 일어났는지 보여준다면, Clarity는 "왜" 일어났는지를 사용자의 시점에서 시각적으로 보여줍니다.
- 2025년 AI 트래픽 추적, Copilot 250세션 분석, Notes 기능 등이 추가되며, 단순 분석 도구에서 팀 협업 가능한 인사이트 플랫폼으로 진화하고 있습니다.
- 실전 팁: 오늘 당장 clarity.microsoft.com에서 프로젝트를 만들고, GA4와 연동한 뒤 Rage Click 필터로 세션 녹화를 확인해보세요. 5분이면 설치가 끝나고, 숫자로는 보이지 않던 UX 문제가 눈앞에 펼쳐집니다.

---

## 참고자료

- Microsoft Clarity 공식 사이트 (<https://clarity.microsoft.com/>)
- Clarity Turns 5: Celebrating Five Years of Insights and Innovation (<https://clarity.microsoft.com/blog/clarity-turns-five/>)
- Clarity 공식 블로그 - August 2025 Recap (<https://clarity.microsoft.com/blog/august-2025-recap/>)
- Clarity 공식 블로그 - July 2025 Recap (<https://clarity.microsoft.com/blog/july-2025-recap/>)
- Microsoft Learn - Clarity Overview (<https://learn.microsoft.com/en-us/clarity/setup-and-installation/about-clarity>)
- Microsoft Learn - GA4 Integration (<https://learn.microsoft.com/en-us/clarity/ga-integration/ga4-integration>)
- Microsoft Learn - Clarity Setup (<https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-setup>)
