---
title: "AJAX로 JSON 데이터 가져오기"
date: 2019-01-15T11:37:07+09:00
slug: "12-AJAX로-JSON-데이터-가져오기"
original_url: "https://memoryhub.tistory.com/12"
tistory_id: 12
draft: false
categories: ["데브 유틸"]
tags: ["자바스크립트 놀기"]
cover:
  image: "images/12-AJAX%EB%A1%9C-JSON-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0/JsonAjax.jpg"
  relative: false
  hidden: false
---

> AJAX 사용해서 JSON 데이터 가져오는 소스

![](/images/12-AJAX%EB%A1%9C-JSON-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0/JsonAjax.jpg)

**AJAX.js (백앤드-논리처리)**

1 id btn click 이벤트 리스너 함수 생성

2 AJAX 객체 생성 

2 불러올 데이터 호출 (URL GET 호출)

3 응답 상태 및 응답 받은 데이터 담고 파싱하기

|  |  |  |
| --- | --- | --- |
| 123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566 | //https://learnwebcode.github.io/json-example/animals-1.json var pageCounter = 1;var animalContainer = document.getElementById("animal-info");var btn = document.getElementById("btn"); btn.addEventListener("click", function() {    //AJAX 사용 메소드 for ajax request  var ourRequest = new XMLHttpRequest();      //요청 URL request url  ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-' + pageCounter + '.json');      //요청 상태 request status   ourRequest.onload = function() { //익명 함수     if (ourRequest.status >= 200 && ourRequest.status < 400) {      //요청한 정보 담는 컨테이너 JSON.parse() JSON형태로 해석하기       var ourData = JSON.parse(ourRequest.responseText);      //console.log(ourData[0]);      renderHTML(ourData);    } else {        //에러 창      console.log("We connected to the server, but it returned an error.");    }      };   ourRequest.onerror = function() {    console.log("Connection error");  };   ourRequest.send();  pageCounter++;  if (pageCounter > 3) {    btn.classList.add("hide-me");  }}); function renderHTML(data) {  var htmlString = "";   for (i = 0; i < data.length; i++) {    htmlString += "<p>" + data[i].name + " is a " + data[i].species + " that likes to eat ";        for (ii = 0; ii < data[i].foods.likes.length; ii++) {      if (ii == 0) {        htmlString += data[i].foods.likes[ii];      } else {        htmlString += " and " + data[i].foods.likes[ii];      }    }     htmlString += ' and dislikes ';     for (ii = 0; ii < data[i].foods.dislikes.length; ii++) {      if (ii == 0) {        htmlString += data[i].foods.dislikes[ii];      } else {        htmlString += " and " + data[i].foods.dislikes[ii];      }    }     htmlString += '.</p>';   }   animalContainer.insertAdjacentHTML('beforeend', htmlString);}[Colored by Color Scripter](http://colorscripter.com/info#e) | [cs](http://colorscripter.com/info#e) |

**AJAX\_AND\_JSON.html**

-프론트앤드 화면

-버튼 생성

|  |  |  |
| --- | --- | --- |
| 123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263646566676869 | <!DOCTYPE html><html><head><style type="text/css">    html, body {  padding: 0;  margin: 0;}.hide-me {  visibility: hidden;  opacity: 0;  transform: scale(.75);}h1 {  margin-top: 0;  font-size: 2.4em;  font-weight: normal;  display: inline-block;}body {  font-family: Helvetica, sans-serif;  padding: 50px 10%;}button {  background-color: #046380;  color: #FFF;  border: none;  padding: 10px 15px;  font-size: 15px;  border-radius: 4px;  cursor: pointer;  outline: none;  box-shadow: 2px 2px 0 #034154;  margin-bottom: 10px;  margin-left: 18px;  transition: opacity .4s ease-out, transform .4s ease-out, visibility .4s ease-out;  position: relative;  top: -10px;}button:hover {  background-color: #034F66;}button:active {  background-color: #034154;  box-shadow: none;  position: relative;  top: -8px;  left: 2px;}p {  padding: 4px 0 2px 8px;  line-height: 1.7;  border-bottom: 1px dotted #DDD;  list-style: none;  margin: 0;}</style>    <title>Json and ajax</title></head><body>    <header>          <h1>JSON and AJAX</h1>          <button id="btn">동물 정보 3개 가져오기</button>    </header>    <div id="animal-info"></div><script type="text/javascript" src="ajax.js"></script></body></html>[Colored by Color Scripter](http://colorscripter.com/info#e) | [cs](http://colorscripter.com/info#e) |
