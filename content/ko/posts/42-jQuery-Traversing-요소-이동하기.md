---
title: "jQuery Traversing(요소 이동하기)"
date: 2020-11-25T09:12:50+09:00
slug: "42-jQuery-Traversing-요소-이동하기"
original_url: "https://memoryhub.tistory.com/42"
tistory_id: 42
draft: false
categories: ["데브 라이브러리"]
tags: ["jQuery"]
cover:
  image: "/images/42-jQuery-Traversing-요소-이동하기/5.png"
  relative: false
  hidden: false
---

**Traversing** 이란 "move through" 또는 이동하다 즉 HTML element(태그)를 찾는다.

 : HTML은 DOM tree 구조여서 다른 element와의 관계 속에서 태그를 찾아야 한다.

![](/images/42-jQuery-Traversing-요소-이동하기/5.png)

1 div : ul의 parent, 하위 모든 태그 ancestor

2 ul : 좌측, 우측 li 태그의 parent 및 div 태그 child

3 좌측 li : span 태그 parent, ul 태그 child, div 태그 descendant

4 span 태그는 li 태그 child, ul 및 div 태그 descendant

5 li 태그는 서로 sibling (동일한 부모 보유)

6 b 태그는 우측 li 태그 child, ul 및 div 태그 descendant

**parent()**

정의: 선택한 element의 parent를 리턴. (children() 은 선택한 element의 모든 child 리턴)

예제:

```
<!DOCTYPE html>
<html>
<head>
<style>
.ancestors * { 
  display: block;
  border: 2px solid lightgrey;
  color: lightgrey;
  padding: 5px;
  margin: 15px;
}
</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("span").parent().css({"color": "red", "border": "2px solid red"});
});
</script>
</head>
<body>

<div class="ancestors">
  <div style="width:500px;">div (great-grandparent)
    <ul>ul (grandparent)  
      <li>li (direct parent)
        <span>span</span>
      </li>
    </ul>   
  </div>

  <div style="width:500px;">div (grandparent)   
    <p>p (direct parent)
      <span>span</span>
    </p> 
  </div>
</div>

</body>
</html>
```

결과:

![](/images/42-jQuery-Traversing-요소-이동하기/11.PNG)

---

**find()**

  정의: 선택한 element의 decendant를 전부 리턴.

  예제:

```
<!DOCTYPE html>
<html>
<head>
<style>
.descendants * { 
  display: block;
  border: 2px solid lightgrey;
  color: lightgrey;
  padding: 5px;
  margin: 15px;
}
</style>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("div").find("span").css({"color": "red", "border": "2px solid red"});
});
</script>
</head>
<body>

<div class="descendants" style="width:500px;">div (current element) 
  <p>p (child)
    <span>span (grandchild)</span>   
  </p>
  <p>p (child)
    <span>span (grandchild)</span>
  </p> 
</div>

</body>
</html>
```

  결과:

![](/images/42-jQuery-Traversing-요소-이동하기/111.PNG)

---

**filter()**

정의: 지정된 조건의 element 만 리턴

예제:

```
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("p").filter(".intro").css("background-color", "yellow");
});
</script>
</head>
<body>

<h1>Welcome to My Homepage</h1>

<p>My name is Donald.</p>
<p class="intro">I live in Duckburg.</p>
<p class="intro">I love Duckburg.</p>
<p>My best friend is Mickey.</p>

</body>
</html>
```

결과:

![](/images/42-jQuery-Traversing-요소-이동하기/22.PNG)
