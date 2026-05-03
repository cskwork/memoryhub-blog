---
title: "Bootstrap 소개"
date: 2024-05-26T10:47:18+09:00
slug: "91-Bootstrap-소개"
original_url: "https://memoryhub.tistory.com/91"
tistory_id: 91
draft: false
categories: ["데브 프레임워크"]
tags: ["Bootstrap"]
---

*Bootstrap은 반응형 및 모바일 우선 웹사이트를 쉽게 개발할 수 있도록 도와주는 강력한 프론트엔드 프레임워크로, 미리 설계된 사용자 도구와 맞춤화 가능한 도구로 집을 짓는 것과 비슷합니다.*

### 전체 그림

집을 짓는다고 상상해 보세요. 적절한 도구 없이 모든 도구와 구성 요소를 처음부터 만들어야 한다면 매우 힘든 작업이 될 것입니다. Bootstrap은 미리 설계되고 맞춤화할 수 있는 도구를 제공하는 잘 갖추어진 공구 상자와 같아서 웹사이트를 만드는 과정을 훨씬 더 쉽고 빠르게 만들어 줍니다. 이것은 HTML, CSS, JavaScript 구성 요소를 포함하는 인기 있는 프론트엔드 프레임워크입니다.

### 핵심 개념

1. **반응형 디자인**: 모든 장치(데스크탑, 태블릿, 휴대폰)에서 웹사이트가 잘 보이도록 보장합니다.
2. **그리드 시스템**: 다양한 화면 크기에 맞는 레이아웃을 만드는 데 도움이 되는 유연한 그리드 레이아웃 시스템입니다.
3. **구성 요소**: 버튼, 폼, 내비게이션 바, 모달 등 쉽게 통합할 수 있는 미리 스타일링된 요소들입니다.
4. **유틸리티**: 간격, 정렬, 가시성 등을 제어할 수 있는 클래스입니다.

### 세부 설명

1. **반응형 디자인**:

   - Bootstrap은 모바일 우선 접근 방식을 사용하여, 모바일 장치용으로 먼저 설계한 다음 더 큰 화면으로 확장합니다.
   - CSS의 미디어 쿼리를 사용하여 화면 크기에 따라 레이아웃을 조정합니다.
2. **그리드 시스템**:

   - 그리드 시스템은 12열 레이아웃을 기반으로 하여 복잡한 레이아웃도 쉽게 만들 수 있습니다.
   - `.row`, `.col-sm-4`, `.col-md-6` 등의 클래스를 사용하여 페이지를 행과 열로 나눌 수 있습니다.
   - 예시:

     ```
     <div class="container">
       <div class="row">
         <div class="col-sm-4">컬럼 1</div>
         <div class="col-sm-4">컬럼 2</div>
         <div class="col-sm-4">컬럼 3</div>
       </div>
     </div>
     ```
3. **구성 요소**:

   - Bootstrap은 버튼, 카드, 모달, 내비게이션 바 등 다양한 구성 요소를 제공합니다.
   - 이러한 구성 요소는 기본 스타일이 있으며, 이를 맞춤화할 수 있습니다.
   - 예시:

     ```
     <button type="button" class="btn btn-primary">기본 버튼</button>
     ```
4. **유틸리티**:

   - 유틸리티 클래스는 간격, 패딩, 색상, 정렬 등을 빠르게 스타일링하는 데 도움이 됩니다.
   - 예시:

     ```
     <div class="text-center">가운데 정렬 텍스트</div>
     <div class="mt-3">상단 간격 3</div>
     ```

### 예시를 통한 이해

Bootstrap을 사용하여 간단한 반응형 웹페이지를 만들어 봅시다.

```
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
  <title>Bootstrap 예제</title>
</head>
<body>
  <div class="container">
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">내비게이션 바</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">홈 <span class="sr-only">(현재)</span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">기능</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">가격</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="row mt-4">
      <div class="col-md-8">
        <h1>Bootstrap에 오신 것을 환영합니다</h1>
        <p>Bootstrap의 기능을 시연하는 간단한 예제입니다.</p>
      </div>
      <div class="col-md-4">
        <button type="button" class="btn btn-success">클릭하세요</button>
      </div>
    </div>
  </div>
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

### 결론 및 요약

Bootstrap은 웹 개발을 위한 종합 도구 상자와 같아서 반응형, 모바일 우선 웹사이트를 만드는 데 필요한 모든 것을 제공합니다. 레이아웃을 위한 그리드 시스템, 일반적인 UI 요소를 위한 미리 스타일링된 구성 요소, 빠른 스타일링을 위한 유틸리티 클래스를 포함하고 있어 웹 개발 프로세스를 크게 간소화할 수 있습니다.

### 이해도 테스트

1. Bootstrap의 그리드 시스템의 목적은 무엇인가요?
2. Bootstrap을 사용하여 반응형 내비게이션 바를 어떻게 만들 수 있나요?
3. Bootstrap의 유틸리티 클래스를 사용하여 간격을 관리하는 방법을 설명해 보세요.

### 참고 자료

추가 학습을 위해 공식 [Bootstrap 문서](https://getbootstrap.com/docs/4.5/getting-started/introduction/)를 참조하십시오.
