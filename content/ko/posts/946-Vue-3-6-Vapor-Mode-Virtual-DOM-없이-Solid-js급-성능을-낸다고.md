---
title: "⚡ Vue 3.6 Vapor Mode, Virtual DOM 없이 Solid.js급 성능을 낸다고?"
date: 2025-12-26T22:14:11+09:00
slug: "946-Vue-3-6-Vapor-Mode-Virtual-DOM-없이-Solid-js급-성능을-낸다고"
original_url: "https://memoryhub.tistory.com/946"
tistory_id: 946
draft: false
categories: ["데브 프레임워크"]
tags: ["VueJS"]
---

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     ██╗   ██╗██╗   ██╗███████╗    ██████╗    ██████╗          ║
║     ██║   ██║██║   ██║██╔════╝    ╚════██╗  ██╔════╝          ║
║     ██║   ██║██║   ██║█████╗       █████╔╝  ███████╗          ║
║     ╚██╗ ██╔╝██║   ██║██╔══╝       ╚═══██╗  ██╔═══██╗         ║
║      ╚████╔╝ ╚██████╔╝███████╗    ██████╔╝  ╚██████╔╝         ║
║       ╚═══╝   ╚═════╝ ╚══════╝    ╚═════╝    ╚═════╝          ║
║                                                               ║
║              VAPOR MODE + ALIEN SIGNALS                       ║
║           ─────────────────────────────────                   ║
║             No Virtual DOM. Pure Speed.                       ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

"Vue는 편하지만 React나 Solid보다 느리다"라는 말을 들어본 적 있을 것이다. 많은 개발자들이 성능이 중요한 프로젝트에서 Vue를 선택할 때 한 번쯤 고민하게 되는 지점이다. 그런데 Vue 3.6이 이 공식을 완전히 뒤집어 버렸다. Vapor Mode라는 새로운 컴파일 전략을 통해 **Virtual DOM을 완전히 제거하고, Solid.js와 Svelte 5 수준의 렌더링 성능을 달성**했기 때문이다.

**결론부터 말하면, Vue 3.6의 Vapor Mode는 기존 Vue 문법을 그대로 쓰면서 번들 크기 10KB 미만, 10만 컴포넌트 100ms 마운트라는 놀라운 성능을 제공한다.**

## 배경

Vue.js는 오랫동안 "적당히 빠르고, 매우 편한 프레임워크"로 자리 잡았다. 하지만 Solid.js나 Svelte처럼 컴파일 타임에 최적화를 수행하는 프레임워크들이 등장하면서, Vue의 Virtual DOM 기반 렌더링이 성능 병목으로 지적받기 시작했다.

> Virtual DOM이란 실제 DOM의 가상 복사본을 메모리에 만들어두고, 상태가 변경될 때마다 새 Virtual DOM을 생성해 이전 것과 비교(diffing)한 뒤, 차이점만 실제 DOM에 반영하는 방식이다.

이 방식은 개발자가 DOM을 직접 조작하지 않아도 되는 편리함을 제공하지만, 근본적인 오버헤드가 존재한다. 상태가 바뀔 때마다 새로운 Virtual DOM 트리를 생성하고, 전체 트리를 순회하며 비교해야 하기 때문이다. 컴포넌트가 수백, 수천 개로 늘어나면 이 비용이 무시할 수 없는 수준이 된다.

Vue의 창시자 Evan You는 2025년 1월 Vue.js Nation 컨퍼런스에서 이 문제에 대한 해답을 발표했다. 바로 Vapor Mode와 Alien Signals다.

## Vapor Mode의 핵심 원리

Vapor Mode를 이해하려면 먼저 기존 방식과의 차이를 알아야 한다.

**기존 Virtual DOM 방식**을 비유하자면, 외국어를 쓰는 친구와 대화할 때 매번 통역사를 거치는 것과 같다. 내가 한 말을 통역사가 듣고, 외국어로 번역해서 전달한다. 빠르긴 하지만 직접 대화하는 것보다는 느릴 수밖에 없다.

**Vapor Mode**는 통역사 없이 직접 대화하는 것과 같다. 컴파일 시점에 "이 상태가 바뀌면 정확히 이 DOM 요소를 업데이트하라"는 코드를 미리 생성해둔다. 런타임에 Virtual DOM을 만들고 비교하는 과정 자체가 사라지는 것이다.

| 구분 | Virtual DOM 방식 | Vapor Mode |
| --- | --- | --- |
| 렌더링 방식 | 가상 DOM 생성 후 비교 | 직접 DOM 조작 코드 생성 |
| 상태 변경 시 | 전체 컴포넌트 재계산 | 변경된 부분만 정확히 업데이트 |
| 번들 크기 | 런타임 코드 포함 | 10KB 미만 |
| 성능 수준 | 일반적인 프레임워크 | Solid.js, Svelte 5급 |

Vue 공식 벤치마크에서 Vapor Mode는 **10만 개의 컴포넌트를 단 100ms에 마운트**하는 결과를 보여줬다. 이는 기존 방식 대비 수 배에서 수십 배 빠른 수치다.

## Alien Signals: 반응성 시스템의 재설계

Vue 3.6의 또 다른 핵심 변화는 반응성 시스템 자체의 리팩토링이다. Johnson Chu가 개발한 Alien Signals 라이브러리를 Vue의 @vue/reactivity 패키지에 통합했다.

> Signal은 값이 변경되면 구독자에게 자동으로 알림을 보내는 반응형 데이터 단위다. Vue의 ref나 reactive도 내부적으로 이 패턴을 따른다.

Alien Signals가 가져온 개선점은 다음과 같다.

**의존성 추적 오버헤드 감소**: 기존에는 반응형 데이터의 의존성을 추적하기 위해 상당한 메모리와 CPU를 사용했다. Alien Signals는 이 과정을 최적화해 더 적은 리소스로 더 많은 반응형 데이터를 처리한다.

**메모리 사용량 절감**: 대규모 애플리케이션에서 반응형 객체가 수천 개에 달할 때, 메모리 효율이 체감될 정도로 개선된다.

**크로스 프레임워크 호환성**: Alien Signals는 TC39에서 논의 중인 Signals 표준 제안과 호환되도록 설계됐다. 장기적으로 프레임워크 간 상호 운용성이 높아질 가능성이 있다.

## 실습: Vapor Mode 적용하기

현재 Vue 3.6은 alpha 단계이며, 2025년 12월 기준 v3.6.0-alpha.6까지 릴리스됐다. 안정 버전은 아니지만 실험적으로 적용해볼 수 있다.

### 1. Vapor Mode 기본 사용법

기존 SFC(Single File Component)에 `vapor` 속성 하나만 추가하면 된다.

```
<!-- 기존 방식 -->
<script setup>
import { ref } from 'vue'
const count = ref(0)
</script>

<!-- Vapor Mode 적용 -->
<script setup vapor>
import { ref } from 'vue'
const count = ref(0)
</script>

<template>
  <button @click="count++">
    Count: {{ count }}
  </button>
</template>
```

`<script setup>`에 `vapor` 속성을 추가하는 것만으로 해당 컴포넌트는 Virtual DOM 없이 컴파일된다. 기존 코드를 거의 수정하지 않아도 된다는 점이 핵심이다.

### 2. Vapor 전용 앱 생성

새 프로젝트를 Vapor Mode로 시작하려면 `createVaporApp`을 사용한다.

```
// main.js
import { createVaporApp } from 'vue'
import App from './App.vue'

createVaporApp(App).mount('#app')
```

이 방식으로 생성된 앱은 Virtual DOM 런타임 코드를 아예 포함하지 않아 **번들 크기가 10KB 미만**으로 줄어든다.

### 3. 기존 VDOM 앱에 Vapor 컴포넌트 혼용

기존 프로젝트에 점진적으로 적용하려면 `vaporInteropPlugin`을 사용한다.

```
// main.js
import { createApp, vaporInteropPlugin } from 'vue'
import App from './App.vue'

createApp(App)
  .use(vaporInteropPlugin)  // Vapor 상호운용 플러그인 활성화
  .mount('#app')
```

이후 성능이 중요한 특정 컴포넌트에만 `vapor` 속성을 추가하면 된다. 나머지 컴포넌트는 기존 VDOM 방식으로 동작한다.

## Vapor Mode 지원 기능과 제한사항

Vapor Mode는 Vue의 모든 기능을 지원하지는 않는다. 의도적으로 일부 기능을 제외해 단순성과 성능을 확보했다.

| 지원되는 기능 | 지원되지 않는 기능 |
| --- | --- |
| Composition API 전체 | Options API |
| `<script setup>` | Render Functions |
| v-if, v-for, v-show | Suspense (단독 사용 시) |
| 컴포넌트, Props, Events | $attrs, $slots 런타임 접근 |
| Slots (정적/동적) | 일부 고급 Directive API |
| Teleport, Transition | - |

주목할 점은 **Suspense의 경우 Vapor 전용 앱에서는 지원되지 않지만, VDOM 앱 내부의 Suspense 안에서 Vapor 컴포넌트를 렌더링하는 것은 가능**하다는 것이다.

## 언제 Vapor Mode를 써야 할까

Vue 팀에서 현재 권장하는 사용 시나리오는 다음과 같다.

**권장되는 경우**

- 성능이 민감한 특정 페이지나 컴포넌트에 부분 적용
- 소규모 새 프로젝트를 Vapor Mode로 전체 구축
- 대시보드, 실시간 데이터 시각화 등 업데이트가 잦은 UI

**아직 권장되지 않는 경우**

- 기존 대규모 프로젝트의 전체 마이그레이션
- 복잡한 VDOM 기반 UI 라이브러리(Vuetify, Element Plus 등)와의 혼용
- Options API를 주로 사용하는 레거시 코드

## 마치며

- Vue 3.6의 Vapor Mode는 Virtual DOM을 제거해 Solid.js급 렌더링 성능을 달성했다
- Alien Signals 통합으로 반응성 시스템의 메모리 효율과 속도가 크게 개선됐다
- 기존 Vue 문법과 100% 호환되므로 `vapor` 속성 하나로 점진적 적용이 가능하다

**실전 팁**: 현재 Vue 3.5를 사용 중이라면, 프로젝트 내 가장 무거운 리스트 렌더링 컴포넌트 하나를 골라 Vapor Mode로 실험해보자. 성능 차이를 직접 체감할 수 있을 것이다.

## 참고자료

- Vue 3.6.0-beta.1 Release Notes (<https://github.com/vuejs/core/releases/tag/v3.6.0-beta.1>)
- Preview of Vue 3.6 & Vapor Mode - Vue School (<https://vueschool.io/articles/news/vn-talk-evan-you-preview-of-vue-3-6-vapor-mode/>)
- Vue.js 2025 In Review - Vue School (<https://vueschool.io/articles/news/vue-js-2025-in-review-and-a-peek-into-2026/>)
- vuejs/core GitHub Releases (<https://github.com/vuejs/core/releases>)
