---
title: "Basic AJAX Syntax"
date: 2019-01-16T12:33:00+09:00
slug: "16-기본-AJAX-문법"
original_url: "https://memoryhub.tistory.com/16"
tistory_id: 16
draft: false
categories: ["Dev Util"]
tags: ["JavaScript Play"]
---

> Basic AJAX syntax summary and examples

**1. Basic Syntax**

- GET and POST methods using jQuery

1. User input event listener function

2. URL to call, function, and data type to receive data

3. Data received from server

4. Parsing received data

5. Selector to place data

| | | |
| --- | --- | --- |
| 12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879 | //Method to run different files in current file jQuery//Implement dictionary here $(document).ready(function() {  $('#load').click(function() {    $('#dictionary').load("load.html");    return false;  });});//Using jQuery and AJAX /*Short version*///get function$.get ( URL , DATA , CALLBACK);//post function$.post ( URL , DATA , CALLBACK);/*Full version*/ $(webDocument).ready(function(){    $('#selector requesting data').Event(function(){        $.ajax({            url:'request.URL',            type:'request Method',            dataType:'request dataType',            success: function(data received from server){ //Callback function                $('#selector to place data').empty(); //Clear                $.each($(data received from server).find('entry'), function(){                var $entry=$(this);                var html ='<div class="entry">';                    html +='<h3 class="term">'+ $entry.attr('term'); +'</h3>';                    html +='<div class="part">'+ $entry.attr('part'); +'</div>';                    html +='<div class="definition">'+  $entry.text()+'</div>';                    html +='</div>';                    $('#selector to place data').append(html);                }); //end each            }//end        });//end ajax        return false;    });});//getJSON implementation//Short version$.getJSON( URL , DATA , CALLBACK);/* *Explanation:*First parameter URL is where you input the URL address to send the request to, second parameter DATA is the DATA received from the server through the client request, and third parameter is where you define the callback function that will be executed when communication is successful. What exactly is a callback function?-callback() is a function that is called when a client requests an action from a server and the client receives the result! -In other words, you specify the name of the function that will be called after the AJAX request is complete *///dictionary.js implementation$(document).ready(function() {    $('#json').click(function() {        $.getJSON('json.json',function(data){             $('#dictionary').empty();            $.each(data,function(index,entry){                var html ='<div class="entry">';                html +='<h3 class="term">'+entry.term +'</h3>';                html +='<div class="part">'+entry.part +'</div>';                html +='<div class="definition">'+ entry.definition+'</div>';                html +='</div>';                $('#dictionary').append(html);            });// end each        });// end json        return false;    });// end click});//JAVASCRIPT methodtest.html<span id="selectorForOutput"></span></p><input type="button"/><script>document.querySelector('data input selector').addEventListener('event').function(event){    var xhr=new XMLHttpRequest();    xhr.open('method(GET/POST)','request URL');    xhr.onreadystatechange=function(){    //Communication complete && Communication successful         if(xhr.readyState===4 && xhr.status===200){            document.querySelector('data output selector').innerHTML=xhr.responseText;        }    }    xhr.send();});</script>Reference: http://www.nextree.co.kr/p11205/  [Colored by Color Scripter](http://colorscripter.com/info#e) | [cs](http://colorscripter.com/info#e) |

**2. Calling AJAX as a method using common.js file**

| | | |
| --- | --- | --- |
| 123456789101112131415161718192021222324252627282930313233343536373839404142434445464748 | var gfv\_ajaxCallback = "";function ComAjax(opt\_formId){  //Use the method below to put url, formId, param, callBack into $.ajax    this.url = "";         this.formId = gfn\_isNull(opt\_formId) == true ? "commonForm" : opt\_formId;    this.param = "";         if(this.formId == "commonForm"){        var frm = $("#commonForm");        if(frm.length > 0){            frm.remove();        }        var str = "<form id='commonForm' name='commonForm'></form>";        $('body').append(str);    }         this.setUrl = function setUrl(url){        this.url = url;    };        this.setCallback = function setCallback(callBack){        fv\_ajaxCallback = callBack;    };     this.addParam = function addParam(key,value){        this.param = this.param + "&" + key + "=" + value;    };         this.ajax = function ajax(){        if(this.formId != "commonForm"){            this.param += "&" + $("#" + this.formId).serialize();        }        $.ajax({            url : this.url,               type : "POST",              data : this.param,            async : false,            success : function(data, status) {                if(typeof(fv\_ajaxCallback) == "function"){                    fv\_ajaxCallback(data);                }                else {                    eval(fv\_ajaxCallback + "(data);");                }            }        });    };} Source: http://addio3305.tistory.com/91?category=772645 [Common Developer Development Note] | [cs](http://colorscripter.com/info#e) |

| | | |
| --- | --- | --- |
| 1234567891011 | //Call and use the one you created like this function fn\_selectBoardList(pageNo){            var comAjax = new ComAjax();            comAjax.setUrl("<c:url value='/sample/selectBoardList.do' />");            comAjax.setCallback("fn\_selectBoardListCallback");            comAjax.addParam("PAGE\_INDEX",pageNo);            comAjax.addParam("PAGE\_ROW", 15);            comAjax.ajax();        } [Colored by Color Scripter](http://colorscripter.com/info#e) | [cs](http://colorscripter.com/info#e) |
