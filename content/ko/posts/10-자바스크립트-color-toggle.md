---
title: "자바스크립트 color toggle"
date: 2019-01-15T11:01:30+09:00
slug: "10-자바스크립트-color-toggle"
original_url: "https://memoryhub.tistory.com/10"
tistory_id: 10
draft: false
categories: ["데브 유틸"]
tags: ["자바스크립트 놀기"]
  hidden: false
cover:
  image: "/images/10-자바스크립트-color-toggle/colortoggle.jpg"
  relative: false
  hidden: false
---

> 백그라운드 색깔 변경하기--> 나중에 더 이미지 또는 css 배경 바꾸는데 응용할 수 있다.

![](/images/10-자바스크립트-color-toggle/colortoggle.jpg)

**color\_toggle.html**

<!DOCTYPE html>  
<html>  
<head>  
    <title></title>  

<style type="text/css">  
    .purple{  
        background: purple;  
    }  

</style>  
</head>  
<body>  


<button>CLICK TO CHANGE COLOR</button>  

<script type="text/javascript" src="**toggle**.js">  
</script>  

</body>  
</html>

**toggle**.js

var button=document.querySelector("button");  
var isPurple=false;  

button.addEventListener("click", function(){  

//방법 1 클래스 html에 등록하게 || 지우기  
    document.body.classList.toggle("purple");  


 /\*

**방법 2**

if(isPurple){  
        document.body.style.background="red";  
     } else{  
         document.body.style.background="purple";  
     }  
     isPurple=!isPurple;

\*/  
 });
