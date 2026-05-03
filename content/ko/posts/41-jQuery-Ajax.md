---
title: "jQuery Ajax"
date: 2020-11-25T08:55:49+09:00
slug: "41-jQuery-Ajax"
original_url: "https://memoryhub.tistory.com/41"
tistory_id: 41
draft: false
---

**목차**

****$.get()****

****$.post()****

****$().load()****

**$.get()** [jQuery AJAX get() and post() Methods (w3schools.com)](https://www.w3schools.com/jquery/jquery_ajax_get_post.asp)

  1 def: 서버에서 get방식(url)으로 데이터 요청

  2 syntax : $.get(*URL,callback*); //URL: 요청 URL(web address). callback(option): load 후 실행 함수. 

  3 example:

demo\_test.asp:

<%  
response.write("This is some text from an external ASP file.")  
%>

```
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("button").click(function(){
    $.get("demo_test.asp", function(data, status){
      alert("Data: " + data + "\nStatus: " + status);
    });
  });
});
</script>
</head>
<body>

<button>Send an HTTP GET request to a page and get the result back</button>

</body>
</html>
```

   4 result:

![](/images/41-jQuery-Ajax/2.PNG)

---

**$.post()** [jQuery AJAX get() and post() Methods (w3schools.com)](https://www.w3schools.com/jquery/jquery_ajax_get_post.asp)

  1 def: 서버에서 post방식(url)으로 데이터 요청

  2 syntax : $.post(*URL,data,callback*) //URL: 요청 URL(web address). data(option): 요청 파라미터. callback(option): load 후 실행 함수. 

  3 example:

demo\_test\_post.asp:

<%  
dim fname,city  
fname=Request.Form("name")  
city=Request.Form("city")  
Response.Write("Dear " & fname & ". ")  
Response.Write("Hope you live well in " & city & ".")  
%>

```
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("button").click(function(){
    $.post("demo_test_post.asp",
    {
      name: "Donald Duck",
      city: "Duckburg"
    },
    function(data,status){
      alert("Data: " + data + "\nStatus: " + status);
    });
  });
});
</script>
</head>
<body>

<button>Send an HTTP POST request to a page and get the result back</button>

</body>
</html>
```

   4 result:

![](/images/41-jQuery-Ajax/3.PNG)

---

**$().load()** [jQuery AJAX load() Method (w3schools.com)](https://www.w3schools.com/jquery/jquery_ajax_load.asp)

  1 서버에서 데이터 로딩해서 선택자로 데이터 리턴

  2 syntax : $(*selector*).load(*URL,data,callback*);  //URL: loading URL. data(option): 요청 파라미터. callback(option): load 후 실행 함수.

  3 example:

demo\_test.txt :

<h2>jQuery and AJAX is FUN!!!</h2>  
<p id="p1">This is some text in a paragraph.</p>

```
<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
  $("button").click(function(){
    $("#div1").load("demo_test.txt", function(responseTxt, statusTxt, xhr){
      if(statusTxt == "success")
        alert("External content loaded successfully!");
      if(statusTxt == "error")
        alert("Error: " + xhr.status + ": " + xhr.statusText);
    });
  });
});
</script>
</head>
<body>
<div id="div1"><h2>Let jQuery AJAX Change This Text</h2></div>

<button>Get External Content</button>

</body>
</html>
```

   3 result:

![](/images/41-jQuery-Ajax/4.PNG)
