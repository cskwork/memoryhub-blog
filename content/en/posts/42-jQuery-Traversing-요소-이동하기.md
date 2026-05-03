---
title: "jQuery Traversing (Element Navigation)"
date: 2020-11-25T09:12:50+09:00
slug: "42-jQuery-Traversing-요소-이동하기"
original_url: "https://memoryhub.tistory.com/42"
tistory_id: 42
draft: false
categories: ["Dev Library"]
tags: ["jQuery"]
cover:
  image: "images/42-jQuery-Traversing-%EC%9A%94%EC%86%8C-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0/5.png"
  relative: false
  hidden: false
---

**Traversing** means "move through" or navigate, i.e., find HTML elements (tags).

: HTML has a DOM tree structure, so you need to find tags within the context of their relationships with other elements.

![](/images/42-jQuery-Traversing-%EC%9A%94%EC%86%8C-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0/5.png)

1 div : parent of ul, ancestor of all tags below

2 ul : parent of left and right li tags and child of div tag

3 left li : parent of span tag, child of ul tag, descendant of div tag

4 span tag is child of li tag, descendant of ul and div tags

5 li tags are siblings of each other (have same parent)

6 b tag is child of right li tag, descendant of ul and div tags

**parent()**

Definition: Return the parent of the selected element. (children() returns all children of the selected element)

Example:

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

Result:

![](/images/42-jQuery-Traversing-%EC%9A%94%EC%86%8C-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0/11.PNG)

---

**find()**

  Definition: Return all descendants of the selected element.

  Example:

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

  Result:

![](/images/42-jQuery-Traversing-%EC%9A%94%EC%86%8C-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0/111.PNG)

---

**filter()**

Definition: Return only elements that match the specified condition

Example:

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

Result:

![](/images/42-jQuery-Traversing-%EC%9A%94%EC%86%8C-%EC%9D%B4%EB%8F%99%ED%95%98%EA%B8%B0/22.PNG)
