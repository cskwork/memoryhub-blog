---
title: "jQuery Ajax"
date: 2020-11-25T08:55:49+09:00
slug: "41-jQuery-Ajax"
original_url: "https://memoryhub.tistory.com/41"
tistory_id: 41
draft: false
categories: ["Dev Library"]
tags: ["jQuery"]
cover:
  image: "/images/41-jQuery-Ajax/2.PNG"
  relative: false
  hidden: false
---

**Table of Contents**

****$.get()****

****$.post()****

****$().load()****

**$.get()** [jQuery AJAX get() and post() Methods (w3schools.com)](https://www.w3schools.com/jquery/jquery_ajax_get_post.asp)

  1 def: Request data from server using get method (URL)

  2 syntax : $.get(*URL,callback*); //URL: request URL(web address). callback(optional): function to execute after load.

  3 example:

demo_test.asp:

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

  1 def: Request data from server using post method (URL)

  2 syntax : $.post(*URL,data,callback*) //URL: request URL(web address). data(optional): request parameters. callback(optional): function to execute after load.

  3 example:

demo_test_post.asp:

<%
dim fname,city
fname=Request.Form("name")
city=Request.Form("city")
Response.Write("Dear " & fname & ".")
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

  1 Load data from server and return data with selector

  2 syntax : $(*selector*).load(*URL,data,callback*);  //URL: loading URL. data(optional): request parameters. callback(optional): function to execute after load.

  3 example:

demo_test.txt :

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
