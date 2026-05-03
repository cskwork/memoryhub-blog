---
title: "JS TO-DO LIST"
date: 2020-11-25T09:52:06+09:00
slug: "44-JS-TO-DO-LIST"
original_url: "https://memoryhub.tistory.com/44"
tistory_id: 44
draft: false
---

> Simple JavaScript to-do List

**Display:**

![](/images/44-JS-TO-DO-LIST/img.jpg)

**Feature Description:**

1. CSS - Space out list items and buttons, set button colors, and apply background color.

2. HTML - Simple item addition area with ol and button functionality.

3. JavaScript - Dynamically implement list and delete buttons. When the delete button is clicked, removeChild is used to remove the item.

**Source Code:**

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>My Bucket List</title>
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

    <h1>My Bucket List</h1>

    <div>
      <label for="item">Add to bucket list:</label>
      <input type="text" name="item" id="item">
      <button>Add</button>
    </div>

    <ol>

    </ol>

    <script>
      //Selectors
      var list = document.querySelector('ol');
      var input = document.querySelector('input');
      var button = document.querySelector('button');

      //Execute button event
      button.onclick = function() {
        var myItem = input.value;
        input.value = '';
        var listItem = document.createElement('li');
        var listText = document.createElement('span');
        var listBtn = document.createElement('button');

        //Add user input value
        listItem.appendChild(listText);
        listText.textContent = myItem;

        //Add delete button
        listItem.appendChild(listBtn);
        listBtn.textContent = 'Delete';

        list.appendChild(listItem);

       //Execute delete button event
        listBtn.onclick = function(e) {
          list.removeChild(listItem);
        }
        //Return to input field after event execution
        input.focus();
      }
    </script>
  </body>
</html>
```
