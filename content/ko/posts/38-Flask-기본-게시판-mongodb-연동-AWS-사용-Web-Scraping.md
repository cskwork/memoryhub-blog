---
title: "Flask 기본 게시판 (mongodb 연동, AWS 사용, Web Scraping)"
date: 2020-11-23T13:07:25+09:00
slug: "38-Flask-기본-게시판-mongodb-연동-AWS-사용-Web-Scraping"
original_url: "https://memoryhub.tistory.com/38"
tistory_id: 38
draft: false
categories: ["데브 유틸"]
tags: ["Flask활용한 todo리스트 구현"]
cover:
  image: "images/38-Flask-%EA%B8%B0%EB%B3%B8-%EA%B2%8C%EC%8B%9C%ED%8C%90-mongodb-%EC%97%B0%EB%8F%99-AWS-%EC%82%AC%EC%9A%A9-Web-Scraping/img.png"
  relative: false
  hidden: false
---

사용툴

: Pycharm, MongoDB, AWS, Gabia, Ubuntu

**A 세팅**

1 기본 프로젝트 세팅

: static - 이미지 파일 , js, css 보관

: templates - html 파일 보관

: app.py - 백앤드 로직 보관

![](/images/38-Flask-%EA%B8%B0%EB%B3%B8-%EA%B2%8C%EC%8B%9C%ED%8C%90-mongodb-%EC%97%B0%EB%8F%99-AWS-%EC%82%AC%EC%9A%A9-Web-Scraping/img.png)

2 필요한 패키지

```
from flask import Flask, render_template, jsonify, request
app = Flask(__name__) # Flask Web Container
import requests # Handle requests
from bs4 import BeautifulSoup # WebScrap Tool
from pymongo import MongoClient # MongoDB DataBaseConnectivity
```

3 백앤드에서 (프론트) html 파일 렌더링

```
## HTML을 주는 부분
@app.route('/') #flask에서 지정해주는 경로로 진입할 때
def home():
   return render_template('index.html')
```

---

**B CRUD (Create Read Update Delete)**

**1 데이터 요청** (C**R**UD)

html -> js -> app.py 데이터 요청

index.html

```
 <script>
   $(document).ready(function () {
     $("#cards-box").html("");
     showArticles();
   });
</script>
<script type="text/javascript" src="{{url_for('static',filename='memo/js/memo.js')}}"></script>
```

memo.js

```
 function showArticles() {
   $.ajax({
     type: "GET",
     url: "/listAllMemo",
     data: {},
     error : function(error){
       alert('오류가 발생했습니다. 관리자에게 문의해주세요.');
       console.log(error);
       window.location.reload();
 	 },
     success: function (response) {
       let articles = response["articles"];
       console.log(articles);
       for (let i = 0; i < articles.length; i++) {
          makeCard(articles[i]["image"], articles[i]["url"], articles[i]["title"], articles[i]["desc"], articles[i]["comment"]);
       }
     }
   })
}
```

app.py

```
@app.route('/listAllMemo', methods=['GET'])
def read_articles():
    # 1. mongoDB에서 _id 값을 제외한 모든 데이터 조회해오기 (Read) 1=허용
    result = list(db.articles.find({}, {'_id': 0}))  #list(db.articles.find({}, {'_id': 0}))
    # 2. articles라는 키 값으로 article 정보 보내주기
    return jsonify({'result': 'success', 'articles': result})
```

**2 데이터 삽입**(**C**RUD)

-웹 스크랩으로 데이터 넣기 

index.html

```
  <button type="button" class="btn btn-primary" onclick="postArticle()">기사저장</button>
```

memo.js

```
            function postArticle() {
                //멀티 포스팅 방지 , 20201106, by cskuk
                if(posted) return;
                posted=true;

                let url = $("#post-url").val();
                let comment = $("#post-comment").val();
                if(url == ''){
                    alert('입력된 URL이 없습니다');
                    return;
                }

                // 2. memo에 POST 방식으로 메모 생성 요청하기
                $.ajax({
                    type: "POST", // POST 방식으로 요청하겠다.
                    url: "/insertOneMemo", // /memo라는 url에 요청하겠다.
                    data: {url_give: url, comment_give: comment}, // 데이터를 주는 방법
                    error : function(error){
                        alert('오류가 발생했습니다. 관리자에게 문의해주세요.');
                        console.log(error);
                        window.location.reload();
                    },
                    success: function (response) { // 성공하면
                        if (response["result"] == "success") {
                            alert("포스팅 성공!");
                            posted=false;//멀티 포스팅 방지 , 20201106, by cskuk
                            // 3. 성공 시 페이지 새로고침하기
                            window.location.reload();
                        } else {
                            alert("서버 오류!")
                        }
                    }
                });
            }
```

app.py

```
@app.route('/insertOneMemo', methods=['POST'])
def post_article():
    # 1. 클라이언트로부터 데이터를 받기
    url_receive = request.form['url_give']  # 클라이언트로부터 url을 받는 부분
    comment_receive = request.form['comment_give']  # 클라이언트로부터 comment를 받는 부분

    # 2. meta tag를 스크래핑하기
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    og_image = soup.select_one('meta[property="og:image"]')
    og_title = soup.select_one('meta[property="og:title"]')
    og_description = soup.select_one('meta[property="og:description"]')

    url_title = og_title['content']
    url_description = og_description['content']
    url_image = og_image['content']

    article = {'url': url_receive, 'title': url_title, 'desc': url_description, 'image': url_image,
               'comment': comment_receive}

    # 3. mongoDB에 데이터를 넣기
    db.articles.insert_one(article)

    return jsonify({'result': 'success'})
```

**3 데이터 삭제**(CRU**D**)

index.html

```
 <button onclick="delMemo('${url}')" class="btn btn-outline-danger">삭제</button>
```

memo.js

```
function delMemo(url){
                $.ajax({
                    type: "POST",
                    url: "/delOneMemo",
                    data: {del_url : url},
                    error : function(error){
                        alert('오류가 발생했습니다. 관리자에게 문의해주세요.');
                        console.log(error);
                        window.location.reload();
                    },
                    success: function (response) {
                        window.location.reload()
                    }
                })
            }
```

app.py

```
@app.route('/delOneMemo', methods=['POST'])
def delete_memo():
    # 1. 삭제할 url 받기 
    del_url = request.form['del_url']
    # 2. db 아티클 테이블에서 해당 url 레코드 삭제 
    db.articles.delete_one({'url': del_url})
    # 3. 성공하면 success 메시지를 반환.
    return jsonify({'result': 'success'})
```

4 **데이터 수정**(CR**U**D)
