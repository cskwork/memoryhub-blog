---
title: "Flask Basic Board (MongoDB Integration, AWS Usage, Web Scraping)"
date: 2020-11-23T13:07:25+09:00
slug: "38-Flask-기본-게시판-mongodb-연동-AWS-사용-Web-Scraping"
original_url: "https://memoryhub.tistory.com/38"
tistory_id: 38
draft: false
categories: ["Dev Util"]
tags: ["Flask Todo List"]
cover:
  image: "/images/38-Flask-기본-게시판-mongodb-연동-AWS-사용-Web-Scraping/img.png"
  relative: false
  hidden: false
---

Tools Used

: Pycharm, MongoDB, AWS, Gabia, Ubuntu

**A Setup**

1 Basic Project Setup

: static - stores image files, js, css

: templates - stores html files

: app.py - stores backend logic

![](/images/38-Flask-기본-게시판-mongodb-연동-AWS-사용-Web-Scraping/img.png)

2 Required Packages

```
from flask import Flask, render_template, jsonify, request
app = Flask(__name__) # Flask Web Container
import requests # Handle requests
from bs4 import BeautifulSoup # WebScrap Tool
from pymongo import MongoClient # MongoDB DataBaseConnectivity
```

3 Rendering HTML file from Backend (Frontend)

```
## Part that serves HTML
@app.route('/') #when entering the path specified by flask
def home():
   return render_template('index.html')
```

---

**B CRUD (Create Read Update Delete)**

**1 Data Request** (C**R**UD)
