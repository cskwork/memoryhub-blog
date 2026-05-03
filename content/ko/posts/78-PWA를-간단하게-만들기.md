---
title: "PWA를 간단하게 만들기"
date: 2024-05-25T17:52:42+09:00
slug: "78-PWA를-간단하게-만들기"
original_url: "https://memoryhub.tistory.com/78"
tistory_id: 78
draft: false
categories: ["데브 유틸"]
cover:
  image: "/images/78-PWA를-간단하게-만들기/img.png"
  relative: false
  hidden: false
---

### ? PWA? 그게 뭔데?

웹과 앱을 결함이 있는 경험. 브라우저를 통해서 처음 방문한 사용자에게 유용하고 설치가 필요 없다. 느린 네트워크에서도 빠르게 로딩되고, 푸시 알림도 전송한다. 모바일 앱처럼 전체 화면이 로드되고 홈 화면에 아이콘이 있다. by Google I/O 2016

PWA가 필요한 이유

- 모바일 사용자 대부분은 웹보다 네이티브 앱에서 훨씬 더 많은 시간을 보낸다.!
- 2017년 기준 50% 이상의 사용자는 앱을 전혀 다운로드하지 않는다.
- 네이티브 앱 설치는 사용자의 시간과 에너지가 들지만, 웹은 설치가 빠르고 URL로 간단하게 접근할 수 있다.
- 네이티브 앱 개발은 많은 시간과 노력이 필요하다 PWA는 비교적 훨씬 쉽고 플랫폼 종속적이지 않다! (iOS 기능 한계는 아직 있음)

### ?‍? 필수 요소

- manifest.json  
  (PWA 정보, 아이콘 정보, 시발점 등 모음)
- sw.js  
  (serviceworker를 활성화하는 스크립트. 서비스 워커는 웹페이지와는 별도로 백그라운드에서 실행되는데. 잘만 쓰면 푸시도 받을 수 있다 - 안드로이드만)
- main.js/sw.js 등록 스크립트  
  (웹 브라우저 로딩 시 sw.js를 로딩하는 스크립트를 포함한다.)

테스트해 보려면 github pages로 올리면 된다. (sw는 https에서만 작동!)

### ? 실습

- index.html

```
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <title> HELLO PWA  </title>
  <link rel="manifest" crossorigin="use-credentials" href="./manifest.json">
  <style>
   .hidden {
       display: none !important;
   }
  </style>
</head>
<body>
  <h1>HELLO PWA</h1>

   <div id="installContainer" class="hidden" >
      <button id="butInstall" type="button">
        앱으로 설치
      </button>
    </div>

</body>

 <script src="js/main.js"></script>
 <script>

window.addEventListener('beforeinstallprompt', (event) => {
  console.log('?', 'beforeinstallprompt', event);
  // 나중에 이벤트를 활성화하려고 보관한다.
  window.deferredPrompt = event;
  // 설치 버튼에 담긴 hidden 클래스를 제거한다. 
  divInstall.classList.toggle('hidden', false);
});

butInstall.addEventListener('click', async () => {
  console.log('?', 'butInstall-clicked');
  const promptEvent = window.deferredPrompt;
  if (!promptEvent) {
    // The deferred prompt isn't available.
    return;
  }
  // 설치 prompt 호출!
  promptEvent.prompt();
  // 결과물 로깅 및 사용자 선택 저장
  const result = await promptEvent.userChoice;
  console.log('?', 'userChoice', result);
  // 이벤트 초기화. prompt()는 한번만 호출할 수 있다.
  window.deferredPrompt = null;
  // 설치 버튼 다시 숨기기
  divInstall.classList.toggle('hidden', true);

});

window.addEventListener('appinstalled', (event) => {
  console.log('?', 'appinstalled', event);
  // 이벤트 초기화 (리소스 가비지 처리) 
  window.deferredPrompt = null;
});
  </script>
</html>
```

- manifest.json  
  (이미지는 해당 경로에 따로 추가해줘야 한다)

```
{
  "name": "hello-pwa",
  "short_name": "pwa",
  "icons": [{
    "src": "images/hello-icon-128.png",
      "sizes": "128x128",
      "type": "image/png"
    }, {
      "src": "images/hello-icon-144.png",
      "sizes": "144x144",
      "type": "image/png"
    }, {
      "src": "images/hello-icon-152.png",
      "sizes": "152x152",
      "type": "image/png"
    }, {
      "src": "images/hello-icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    }, {
      "src": "images/hello-icon-256.png",
      "sizes": "256x256",
      "type": "image/png"
    }, {
      "src": "images/hello-icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }],
  "lang": "ko-KR",
  "start_url": "./index.html",
  "display": "standalone",
  "background_color": "white",
  "theme_color": "white"
}
```

- sw.js  
  (여기서 주의할 건 경로! 경로가 잘못되면 sw가 시작조차 안할 수 있다)

```
var cacheName = 'pwacache';
var filesToCache = [
  './',
  './index.html',
  './css/style.css', // css style있으면 추가! 
  './js/main.js'
];

/* 서비스 워커를 시작하고 앱 컨텐츠를 캐싱한다 - offline 작동 */
self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(cacheName).then(function(cache) {
      return cache.addAll(filesToCache);
    })
  );
  self.skipWaiting();
});

/* 오프라인시 리소스 fetch해서 앱이 작동하게끔 한다 */
self.addEventListener('fetch', function(e) {
  e.respondWith(
    caches.match(e.request).then(function(response) {
      return response || fetch(e.request);
    })
  );
});
```

- main.js

```
window.onload = () => {
  'use strict';

  if ('serviceWorker' in navigator) {
    navigator.serviceWorker
             .register('./sw.js');
  }
}
```

### ? 서비스 워커 작동 단계

![](/images/78-PWA를-간단하게-만들기/img.png)

### 참고

<https://developers.google.com/web/fundamentals/primers/service-workers?hl=ko>  
<https://altenull.github.io/2018/02/25/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%A0%88%EC%8B%9C%EB%B8%8C-%EC%9B%B9-%EC%95%B1-Progressive-Web-Apps-%EB%9E%80/>  
<https://web.dev/progressive-web-apps/>
