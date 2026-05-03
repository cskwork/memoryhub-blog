---
title: "Vue 3 컴포넌트 구조 - script 먼저 vs template 먼저"
date: 2025-04-22T18:27:04+09:00
slug: "557-Vue-3-컴포넌트-구조-script-먼저-vs-template-먼저"
original_url: "https://memoryhub.tistory.com/557"
tistory_id: 557
draft: false
categories: ["데브 프레임워크"]
tags: ["VueJS"]
---

Vue.js로 컴포넌트를 만들다 보면 `.vue` 파일 안에서 `<template>`, `<script>`, `<style>` 블록들의 순서가 궁금할 때가 있죠? ? 어떤 사람은 `<template>`을 먼저 쓰고, 다른 사람은 `<script>`를 먼저 쓰기도 하는데요. 과연 이 순서에 특별한 의미가 있을까요? 또, Vue 3에서는 어떤 순서를 더 권장할까요? 함께 알아보아요! ?

## 등장 배경: 과거와 현재의 만남

초기 Vue 버전(Vue 2)이나 Options API를 주로 사용하던 시절에는 `<template>` 블록을 가장 위에 두는 방식이 흔했어요. 마치 전통적인 HTML 문서처럼 시각적인 구조를 먼저 보여주고, 그 다음에 데이터를 다루는 스크립트, 마지막으로 스타일을 정의하는 식이었죠. ?️➡️?➡️?

```
<template>
  <div>{{ message }}</div>
</template>

<script>
export default {
  data() {
    return {
      message: '안녕하세요!'
    }
  }
}
</script>

<style scoped>
div {
  color: blue;
}
</style>
```

하지만 Vue 3와 함께 **Composition API** 와 **`<script setup>`** 이 등장하면서 상황이 조금 달라졌어요. `<script setup>`을 사용하면 `<script>` 블록 안에서 정의한 변수나 함수를 바로 `<template>`에서 사용할 수 있게 되면서, `<script>`의 역할이 훨씬 중요해졌죠. 이제 로직과 상태 정의가 컴포넌트의 핵심 시작점이 되는 경우가 많아졌습니다. ?

## 핵심 원리: 순서, 중요할까?

결론부터 말하면, Vue 컴파일러는 `<template>`, `<script>`, `<style>` 블록의 순서에 **상관없이** 컴포넌트를 올바르게 해석하고 빌드합니다. 즉, 기술적으로 어떤 순서로 작성하든 컴포넌트의 기능 자체에는 영향을 주지 않아요. ?

하지만 **가독성**과 **유지보수성** 측면에서는 이야기가 다릅니다. 어떤 순서를 따르느냐에 따라 개발자가 코드를 읽고 이해하는 방식이 달라질 수 있거든요.

**1. `<template>` 우선 방식 (`template` > `script` > `style`)**

- **장점:**
  - 컴포넌트의 최종적인 HTML 구조를 가장 먼저 파악할 수 있어요. ?
  - HTML 중심적인 사고방식에 익숙한 개발자에게 더 직관적일 수 있어요.
- **단점:**
  - `<script setup>`을 사용하는 경우, 템플릿에서 사용되는 변수나 함수의 정의를 보려면 아래로 스크롤해야 해요. ?
  - 컴포넌트의 로직이나 상태를 먼저 파악하기 어려울 수 있어요.

```
+---------------------+
|     <template>      |  <-- 시각적 구조 먼저!
+---------------------+
|      <script>       |
+---------------------+
|      <style>        |
+---------------------+
```

**2. `<script>` 우선 방식 (`script` > `template` > `style`)**

- **장점:**
  - 컴포넌트를 열자마자 어떤 상태(state)와 로직(logic), 외부 모듈(import)을 사용하는지 바로 알 수 있어요. ?
  - `<script setup>`과 함께 사용하면, 정의된 변수/함수가 바로 아래 `<template>`에서 어떻게 사용되는지 흐름을 따라가기 쉬워요. ✨
  - **Vue 3 공식 스타일 가이드에서 권장하는 방식**이에요! (특히 `<script setup>` 사용 시) ?
  - 린팅 도구(ESLint 등)에서 기본적으로 권장하거나 강제하는 경우가 많아요.
- **단점:**
  - 시각적인 구조보다 로직을 먼저 보게 되어, UI 결과물을 먼저 상상하기엔 조금 어색할 수 있어요.

```
+---------------------+
|      <script>       |  <-- 로직/상태 먼저!
+---------------------+
|     <template>      |
+---------------------+
|      <style>        |
+---------------------+
```

**Vue 공식 스타일 가이드의 권장 순서:**

Vue 팀은 일관성과 `<script setup>`의 이점을 살리기 위해 다음과 같은 순서를 **강력히 권장(Strongly Recommended)** 합니다.

1. `<script setup>` (Composition API 로직)
2. `<script>` (Options API 또는 추가 설정 필요시)
3. `<template>` (템플릿 마크업)
4. `<style>` (스타일)

## 주의사항 및 팁 ?

⚠️ **이것만은 주의하세요!**

1. **일관성이 중요해요!**
   - 기술적으로 순서가 중요하지 않다고 해서 프로젝트 내에서 여러 스타일을 혼용하는 것은 좋지 않아요. ? 코드를 읽는 동료(또는 미래의 나!)에게 혼란을 줄 수 있습니다.
   - 팀이나 프로젝트 단위로 하나의 컨벤션을 정하고 일관되게 따르는 것이 중요해요.

? **꿀팁**

- **린터(Linter)를 활용하세요!** ESLint와 `eslint-plugin-vue` 같은 도구를 사용하면 코드 스타일을 자동으로 검사하고 교정할 수 있어요. `vue/block-order` 규칙을 설정하여 팀이 정한 순서(가급적 공식 권장 순서)를 강제하면 일관성을 유지하는 데 큰 도움이 됩니다. ✨

## 마치며

지금까지 Vue 3 컴포넌트 내 블록 순서에 대해 알아보았습니다. 기능적으로는 차이가 없지만, 최신 Vue 개발 트렌드와 가독성을 고려했을 때 **`<script>` (특히 `<script setup>`) 블록을 가장 위에 두는 방식이 현재로서는 가장 권장되는 방법**이라고 할 수 있겠네요. ? 여러분의 프로젝트에서는 어떤 순서를 사용하고 계신가요? 댓글로 의견을 나눠주세요! ?‍♀️

## 참고 자료 ?

- Vue 3 공식 스타일 가이드 - 컴포넌트/인스턴스 순서 (Component/Instance Order): <https://vuejs.org/style-guide/rules-recommended>
- Vue 3 공식 스타일 가이드 - 요소 속성 순서 (Element Attribute Order): <https://vuejs.org/style-guide/rules-strongly-recommended.html#element-attribute-order> (컴포넌트 블록 순서와 직접 관련은 없지만, 일관된 순서의 중요성을 보여줍니다.)
- eslint-plugin-vue - `vue/vue/block-order` 규칙: <https://eslint.vuejs.org/rules/block-order.html>

---

#Vue3 #컴포넌트 #SFC #스크립트셋업 #코딩컨벤션 #Vue스타일가이드
