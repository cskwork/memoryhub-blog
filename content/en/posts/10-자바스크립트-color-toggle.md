---
title: "JavaScript color toggle"
date: 2019-01-15T11:01:30+09:00
slug: "10-자바스크립트-color-toggle"
original_url: "https://memoryhub.tistory.com/10"
tistory_id: 10
draft: false
categories: ["Dev Util"]
tags: ["JavaScript Play"]
  hidden: false
cover:
  image: "/images/10-자바스크립트-color-toggle/colortoggle.jpg"
  relative: false
  hidden: false
---

> Changing background color --> Later this can be applied to changing images or CSS backgrounds.

![](/images/10-자바스크립트-color-toggle/colortoggle.jpg)

**color_toggle.html**

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

<script type="text/javascript" src="toggle.js">  
</script>  

</body>  
</html>

**toggle.js**

var button=document.querySelector("button");  
var isPurple=false;  

button.addEventListener("click", function(){  

//Method 1: Add class to html or remove it  
    document.body.classList.toggle("purple");  


 /*

**Method 2**

if(isPurple){  
        document.body.style.background="red";  
     } else{  
         document.body.style.background="purple";  
     }  
     isPurple=!isPurple;

*/  
 });
