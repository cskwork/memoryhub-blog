---
title: "JS TO-DO LIST ❄️"
date: 2020-11-25T09:52:06+09:00
slug: "44-JS-TO-DO-LIST"
original_url: "https://memoryhub.tistory.com/44"
tistory_id: 44
draft: false
categories: ["데브 유틸"]
tags: ["자바스크립트 놀기"]
  hidden: false
cover:
  image: "/images/44-JS-TO-DO-LIST/img.jpg"
  relative: false
  hidden: false
---

> JS 간단한 to-do List

**화면:**

![](/images/44-JS-TO-DO-LIST/img.jpg)

**기능 설명:**

1 css- 목록 및 버튼 간격 띄우고, 버튼 생상 정하고, 백그라운드 색깔 입힘.

2 html- 간단한 항목 추가 공간 ol 과 버튼 기능 추가

3 js- 동적으로 목록 및 삭제 버튼 구현되었고. 삭제 기능을 클릭하면 removeChild 즉 제거함.

**소스코드:**

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>버킷 리스트</title>
    <style>
      li {
        margin-bottom: 10px;
      }
      li button {
        font-size: 12px;
        margin-left: 40px;
        color: red;
   }
      body{
        background: cyan; 
      }
    </style>
  </head>
  <body>

    <h1>내 버킷 리스트</h1>

    <div>
      <label for="item">버킷 리스트 추가하기:</label>
      <input type="text" name="item" id="item">
      <button>추가</button>
    </div>

    <ol>

    </ol>

    <script>
      //선택자
      var list = document.querySelector('ol');
      var input = document.querySelector('input');
      var button = document.querySelector('button');

      //버튼 이벤트 실행
      button.onclick = function() {
        var myItem = input.value;
        input.value = '';
        var listItem = document.createElement('li');
        var listText = document.createElement('span');
        var listBtn = document.createElement('button');

        //유저가 입력한 값 추가
        listItem.appendChild(listText);
        listText.textContent = myItem;

        //삭제 버튼 추가
        listItem.appendChild(listBtn);
        listBtn.textContent = '삭제';

        list.appendChild(listItem);

       //삭제 버튼 이벤트 실행
        listBtn.onclick = function(e) {
          list.removeChild(listItem);
        }
        //이벤트 실행 후 입력창으로 돌아가기
        input.focus();
      }
    </script>
  </body>
</html>
```
