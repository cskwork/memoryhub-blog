---
title: "Fetching JSON Data with AJAX"
date: 2019-01-15T11:37:07+09:00
slug: "12-AJAX로-JSON-데이터-가져오기"
original_url: "https://memoryhub.tistory.com/12"
tistory_id: 12
draft: false
categories: ["Dev Util"]
tags: ["JavaScript Play"]
  hidden: false
cover:
  image: "/images/12-AJAX로-JSON-데이터-가져오기/JsonAjax.jpg"
  relative: false
  hidden: false
---

> Source code for fetching JSON data using AJAX

![](/images/12-AJAX로-JSON-데이터-가져오기/JsonAjax.jpg)

**AJAX.js (Backend - Logic Processing)**

1. Create event listener function for button click
2. Create AJAX object
3. Call data to load (URL GET request)
4. Store and parse response status and received data

**AJAX.js Code:**

```javascript
// https://learnwebcode.github.io/json-example/animals-1.json
var pageCounter = 1;
var animalContainer = document.getElementById("animal-info");
var btn = document.getElementById("btn");

btn.addEventListener("click", function() {
    // AJAX method for ajax request
    var ourRequest = new XMLHttpRequest();
    
    // Request URL
    ourRequest.open('GET', 'https://learnwebcode.github.io/json-example/animals-' + pageCounter + '.json');
    
    // Request status
    ourRequest.onload = function() {
        if (ourRequest.status >= 200 && ourRequest.status < 400) {
            // Parse received data as JSON
            var ourData = JSON.parse(ourRequest.responseText);
            renderHTML(ourData);
        } else {
            // Error message
            console.log("We connected to the server, but it returned an error.");
        }
    };
    
    ourRequest.onerror = function() {
        console.log("Connection error");
    };
    
    ourRequest.send();
    pageCounter++;
    
    if (pageCounter > 3) {
        btn.classList.add("hide-me");
    }
});

function renderHTML(data) {
    var htmlString = "";
    
    for (i = 0; i < data.length; i++) {
        htmlString += "<p>" + data[i].name + " is a " + data[i].species + " that likes to eat ";
        
        for (ii = 0; ii < data[i].foods.likes.length; ii++) {
            if (ii == 0) {
                htmlString += data[i].foods.likes[ii];
            } else {
                htmlString += " and " + data[i].foods.likes[ii];
            }
        }
        
        htmlString += ' and dislikes ';
        
        for (ii = 0; ii < data[i].foods.dislikes.length; ii++) {
            if (ii == 0) {
                htmlString += data[i].foods.dislikes[ii];
            } else {
                htmlString += " and " + data[i].foods.dislikes[ii];
            }
        }
        
        htmlString += '.</p>';
    }
    
    animalContainer.insertAdjacentHTML('beforeend', htmlString);
}
```

**AJAX_AND_JSON.html**

- Frontend display
- Button creation

```html
<!DOCTYPE html>
<html>
<head>
    <style type="text/css">
        html, body {
            padding: 0;
            margin: 0;
        }
        
        .hide-me {
            visibility: hidden;
            opacity: 0;
            transform: scale(.75);
        }
        
        h1 {
            margin-top: 0;
            font-size: 2.4em;
            font-weight: normal;
            display: inline-block;
        }
        
        body {
            font-family: Helvetica, sans-serif;
            padding: 50px 10%;
        }
        
        button {
            background-color: #046380;
            color: #FFF;
            border: none;
            padding: 10px 15px;
            font-size: 15px;
            border-radius: 4px;
            cursor: pointer;
            outline: none;
            box-shadow: 2px 2px 0 #034154;
            margin-bottom: 10px;
            margin-left: 18px;
            transition: opacity .4s ease-out, transform .4s ease-out, visibility .4s ease-out;
            position: relative;
            top: -10px;
        }
        
        button:hover {
            background-color: #034F66;
        }
        
        button:active {
            background-color: #034154;
            box-shadow: none;
            position: relative;
            top: -8px;
            left: 2px;
        }
        
        p {
            padding: 4px 0 2px 8px;
            line-height: 1.7;
            border-bottom: 1px dotted #DDD;
            list-style: none;
            margin: 0;
        }
    </style>
    <title>Json and ajax</title>
</head>
<body>
    <header>
        <h1>JSON and AJAX</h1>
        <button id="btn">Get 3 Animal Infos</button>
    </header>
    <div id="animal-info"></div>
    <script type="text/javascript" src="ajax.js"></script>
</body>
</html>
```
