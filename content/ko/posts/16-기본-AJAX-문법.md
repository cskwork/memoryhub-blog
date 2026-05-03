---
title: "기본 AJAX 문법"
date: 2019-01-16T12:33:00+09:00
slug: "16-기본-AJAX-문법"
original_url: "https://memoryhub.tistory.com/16"
tistory_id: 16
draft: false
categories: ["데브 유틸"]
tags: ["자바스크립트 놀기"]
---

> 기본 AJAX 문법 정리 및 예제

**1 기본 문법**

-jQuery를 사용한 get, post 방식

1 사용자 입력 이벤트 리스너 함수

2 데이터를 받을 호출할 URL, 함수, 데이터 타입

3 서버에서 받은 데이터

4 받은 데이터 파싱

5 데이터 넣을 선택자

|  |  |  |
| --- | --- | --- |
| 12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879 | //다른 파일을 현재 파일에 구동하는 방식 jQuery//여기선 dictionary를 구현 $(document).ready(function() {  $('#load').click(function() {    $('#dictionary').load("load.html");    return false;  });});//jQuery와 AJAX 사용 /\*약식\*///get함수$.get ( URL , DATA , CALLBACK);//post함수$.post ( URL , DATA , CALLBACK);/\*전체\*/ $(webDocument).ready(function(){    $('#데이터 요청한 선택자').Event(function(){        $.ajax({            url:'요청.URL',            type:'요청 Method',            dataType:'요청 dataType',            success: function(서버로 부터 응답 받은 data){ //콜백 함수                $('#데이터 넣을 선택자').empty(); //비워주기                $.each($(서버로 부터 응답 받은 data).find('entry'), function(){                var $entry=$(this);                var html ='<div class="entry">';                    html +='<h3 class="term">'+ $entry.attr('term'); +'</h3>';                    html +='<div class="part">'+ $entry.attr('part'); +'</div>';                    html +='<div class="definition">'+  $entry.text()+'</div>';                    html +='</div>';                    $('#데이터 넣을 선택자').append(html);                }); //end each            }//end        });//end ajax        return false;    });});//getJSON 구현//약식$.getJSON( URL , DATA , CALLBACK);/\* \*설명:\*첫번째 매개 변수 URL로는 요청을 보낼 URL주소를 입력하게되며, 두번째 매개 변수 DATA로는 클라이언트의 요청을 통해 서버로 부터 받은 DATA를  세번째 매개변수로는 통신 성공시 구현하게될 콜백 함수를 정의해 주게 된다. 콜백 함수란 그럼 무엇인가?-callback()는 클라이언트가 서버에 동작을 요청하고 클라이언트가 그 결과를 받을 때 호출되는 함수! -즉 다시 말하자면 AJAX 요청이 완료된 후에 호출될 함수의 이름을 지정하는 것 \*///dictionary.js 구현$(document).ready(function() {    $('#json').click(function() {        $.getJSON('json.json',function(data){             $('#dictionary').empty();            $.each(data,function(index,entry){                var html ='<div class="entry">';                html +='<h3 class="term">'+entry.term +'</h3>';                html +='<div class="part">'+entry.part +'</div>';                html +='<div class="definition">'+ entry.definition+'</div>';                html +='</div>';                $('#dictionary').append(html);            });// end each        });// end json        return false;    });// end click});//JAVASCRIPT 방식test.html<span id="selectorForOutput"></span></p><input type="button"/><script>document.querySelector('데이터 입력 선택자').addEventListener('event').function(event){    var xhr=new XMLHttpRequest();    xhr.open('방식(GET/POST)','요청 URL');    xhr.onreadystatechange=function(){    //통신 완료 && 통신 성공         if(xhr.readyState===4 && xhr.status===200){            document.querySelector('데이터 출력 선택자').innerHTML=xhr.responseText;        }    }    xhr.send();});</script>참고 http://www.nextree.co.kr/p11205/  [Colored by Color Scripter](http://colorscripter.com/info#e) | [cs](http://colorscripter.com/info#e) |

**2 common.js 파일을 활용해서 메소드로 ajax 호출**

|  |  |  |
| --- | --- | --- |
| 123456789101112131415161718192021222324252627282930313233343536373839404142434445464748 | var gfv\_ajaxCallback = "";function ComAjax(opt\_formId){  //아래 메소드를 사용해서 url,formId,param,callBack 을 $.ajax에 집어넣는다    this.url = "";         this.formId = gfn\_isNull(opt\_formId) == true ? "commonForm" : opt\_formId;    this.param = "";         if(this.formId == "commonForm"){        var frm = $("#commonForm");        if(frm.length > 0){            frm.remove();        }        var str = "<form id='commonForm' name='commonForm'></form>";        $('body').append(str);    }         this.setUrl = function setUrl(url){        this.url = url;    };        this.setCallback = function setCallback(callBack){        fv\_ajaxCallback = callBack;    };     this.addParam = function addParam(key,value){        this.param = this.param + "&" + key + "=" + value;    };         this.ajax = function ajax(){        if(this.formId != "commonForm"){            this.param += "&" + $("#" + this.formId).serialize();        }        $.ajax({            url : this.url,               type : "POST",              data : this.param,            async : false,            success : function(data, status) {                if(typeof(fv\_ajaxCallback) == "function"){                    fv\_ajaxCallback(data);                }                else {                    eval(fv\_ajaxCallback + "(data);");                }            }        });    };} 출처: http://addio3305.tistory.com/91?category=772645 [흔한 개발자의 개발 노트] | [cs](http://colorscripter.com/info#e) |

|  |  |  |
| --- | --- | --- |
| 1234567891011 | //위에서 만든 걸 이런식으로 불러와서 쓰면 된다 function fn\_selectBoardList(pageNo){            var comAjax = new ComAjax();            comAjax.setUrl("<c:url value='/sample/selectBoardList.do' />");            comAjax.setCallback("fn\_selectBoardListCallback");            comAjax.addParam("PAGE\_INDEX",pageNo);            comAjax.addParam("PAGE\_ROW", 15);            comAjax.ajax();        } [Colored by Color Scripter](http://colorscripter.com/info#e) | [cs](http://colorscripter.com/info#e) |
