---
title: "Creating a Simple PWA"
date: 2024-05-25T17:52:42+09:00
slug: "78-PWA를-간단하게-만들기"
original_url: "https://memoryhub.tistory.com/78"
tistory_id: 78
draft: false
categories: ["Dev Util"]
  hidden: false
cover:
  image: "/images/78-PWA를-간단하게-만들기/img.png"
  relative: false
  hidden: false
---

### 📱 What's a PWA?

A seamless blend of web and app experiences. Useful for first-time visitors through a browser without requiring installation. Loads quickly even on slow networks and sends push notifications. Displays full screen like a mobile app with an icon on the home screen. by Google I/O 2016

Why PWA is Needed

- Most mobile users spend significantly more time on native apps than the web
- As of 2017, more than 50% of users never download any apps
- Native app installation requires user time and energy, but web is fast and simply accessible via URL
- Native app development requires significant time and effort, but PWA is relatively much easier and not platform-dependent! (though iOS functionality is still limited)

### 👨‍💻 Essential Components

- manifest.json  
  (Collection of PWA information, icon information, starting point, etc.)
- sw.js  
  (Script that activates the service worker. Service workers run in the background separate from the web page. Used correctly, they can receive push notifications - Android only)
- main.js/sw.js registration script  
  (Includes scripts that load sw.js when the web browser loads)

To test, upload to GitHub Pages. (SW only works on HTTPS!)

### 🚀 Practice

- index.html

```
<!doctype html>
<html lang="en">
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
        Install as App
      </button>
    </div>

</body>

 <script src="js/main.js"></script>
 <script>

window.addEventListener('beforeinstallprompt', (event) => {
  console.log('👍', 'beforeinstallprompt', event);
  // Store the event for later activation.
  window.deferredPrompt = event;
  // Remove the hidden class from the install button container.
  divInstall.classList.toggle('hidden', false);
});

butInstall.addEventListener('click', async () => {
  console.log('👍', 'butInstall-clicked');
  const promptEvent = window.deferredPrompt;
  if (!promptEvent) {
    // The deferred prompt isn't available.
    return;
  }
  // Show the install prompt!
  promptEvent.prompt();
  // Log the result and save user choice
  const result = await promptEvent.userChoice;
  console.log('👍', 'userChoice', result);
  // Reset event. prompt() can only be called once.
  window.deferredPrompt = null;
  // Hide install button again
  divInstall.classList.toggle('hidden', true);

});

window.addEventListener('appinstalled', (event) => {
  console.log('👍', 'appinstalled', event);
  // Reset event (garbage collection for resources)
  window.deferredPrompt = null;
});
  </script>
</html>
```

- manifest.json  
  (Images must be added separately in the specified path)

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
  "lang": "en-US",
  "start_url": "./index.html",
  "display": "standalone",
  "background_color": "white",
  "theme_color": "white"
}
```

- sw.js  
  (Note the path! Wrong paths may prevent the SW from starting)

```
var cacheName = 'pwacache';
var filesToCache = [
  './',
  './index.html',
  './css/style.css', // Add if you have CSS styles!
  './js/main.js'
];

/* Start service worker and cache app content - for offline operation */
self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open(cacheName).then(function(cache) {
      return cache.addAll(filesToCache);
    })
  );
  self.skipWaiting();
});

/* Fetch resources when offline so app continues to work */
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

### 🔄 Service Worker Operation Stages

![](/images/78-PWA를-간단하게-만들기/img.png)

### References

<https://developers.google.com/web/fundamentals/primers/service-workers>  
<https://altenull.github.io/2018/02/25/Progressive-Web-Apps-란/>  
<https://web.dev/progressive-web-apps/>
