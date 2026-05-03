---
title: "논문 \"Attention Is All You Need\""
date: 2025-07-29T23:06:52+09:00
slug: "734-논문-_Attention-Is-All-You-Need_"
original_url: "https://memoryhub.tistory.com/734"
tistory_id: 734
draft: false
---

이 글은 구글 브레인 팀이 발표한 2017년 논문 "Attention Is All You Need"[[1]](https://arxiv.org/html/1706.03762v7#:~:text=The%20dominant%20sequence%20transduction%20models,large%20and%20limited%20training%20data)를 이해할 수 있도록 쉽게 설명한 것이다. 이 논문에서는 번역 등 길이가 다른 두 개의 문장을 처리하는 **시퀀스** **변환** 문제를 푸는 새로운 방법을 제안한다.

기존에는 문장의 단어들을 순서대로 처리하는 **순환** **신경망(RNN)** 이 주로 사용되었지만, 논문 저자들은 **어텐션(attention)** 메커니즘을 이용해 전혀 다른 구조를 설계하였다.

이 구조를 **트랜스포머(Transformer)** 라고 부른다.

## 1.시퀀스 변환과 기존 방법

·       **시퀀스** **변환**은 영어 문장을 독일어로 바꾸는 번역과 같이 입력 문자의 순서와 길이가 다른 출력을 만들어내는 문제이다. 이를 위해 신경망은 입력을 압축하는 **인코더(encoder)** 와 출력을 만들어내는 **디코더(decoder)** 로 구성된다[[2]](https://arxiv.org/html/1706.03762v7#:~:text=Most%20competitive%20neural%20sequence%20transduction,input%20when%20generating%20the%20next).

·       기존에는 **RNN**(특히 LSTM)과 **컨볼루션** **신경망**이 사용되었는데, 이들 모델은 입력 위치에 맞춰 한 단계씩 순차적으로 계산해야 한다[[3]](https://arxiv.org/html/1706.03762v7#:~:text=Recurrent%20models%20typically%20factor%20computation,The%20fundamental). 이런 **순차적** **계산** 때문에 길이가 긴 문장은 병렬처리가 어렵고 학습 시간이 길다.

·       어텐션은 입력의 특정 부분에 "집중"할 수 있게 해주는 장치다. 이전 모델들은 RNN과 함께 어텐션을 사용했지만, 이 논문은 **어텐션만으로도** **충분하다**고 주장한다[[4]](https://arxiv.org/html/1706.03762v7#:~:text=In%20this%20work%20we%20propose,hours%20on%20eight%20P100%20GPUs).

## 2.어텐션이란?

·       **어텐션**은 질문(query)과 키(key), 값(value)을 받아서 각 값에 얼마나 집중해야 하는지 가중치를 계산하는 함수이다[[5]](https://arxiv.org/html/1706.03762v7#:~:text=An%20attention%20function%20can%20be,query%20with%20the%20corresponding%20key). 여러 값들이 있을 때 어떤 값이 더 중요한지 **소프트맥스(softmax)** 함수를 통해 결정한다.

·       논문에서는 빠르고 메모리 효율적인 **점곱** **어텐션**을 사용하며, 값이 너무 커져 소프트맥스의 기울기가 사라지는 문제를 막기 위해

![](/images/734-논문-_Attention-Is-All-You-Need_/img.png)

 로 나누어 스케일링한다[[6]](https://arxiv.org/html/1706.03762v7#:~:text=We%20call%20our%20particular%20attention,the%20weights%20on%20the%20values).

·       **셀프** **어텐션(self‑attention)**은 한 문장 안의 단어들이 서로를 참고하도록 하는 것이다. 단어 **하나**가 아니라 **모든** **위치**를 서로 비교해 어떤 단어가 다른 단어와 얼마나 관련 있는지 알아낸다[[7]](https://arxiv.org/html/1706.03762v7#:~:text=Self,40%2C%2028%20%2C%20%2047).

### 2.1멀티-헤드 어텐션

하나의 어텐션만 사용하면 여러 관계를 동시에 표현하기 어렵다. 그래서 저자들은 **멀티-****헤드** **어텐션**을 사용한다. Queries, keys, values를 여러 번 다른 선형 변환으로 투사한 뒤 여러 개의 어텐션을 병렬로 수행하고 결과를 이어 붙인다[[8]](https://arxiv.org/html/1706.03762v7#:~:text=Instead%20of%20performing%20a%20single,values%2C%20as%20depicted%20in%20Figure%C2%A02). 멀티-헤드 어텐션을 쓰면 모델이 서로 다른 의미 영역(예: 문법 구조, 의미 관계 등)에 동시에 주의를 기울일 수 있다[[9]](https://arxiv.org/html/1706.03762v7#:~:text=Multi,attention%20head%2C%20averaging%20inhibits%20this).

## 3.트랜스포머 구조

트랜스포머는 인코더와 디코더 모두 **여러** **층(stack)** 으로 쌓여 있다[[10]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,produce%20outputs%20of%20dimension). 각 층의 주요 구성 요소는 다음과 같다.

### 3.1인코더 층

·       각 인코더 층에는 **두** **개의** **서브층**이 있다. 첫 번째는 멀티-헤드 **셀프** **어텐션**이고, 두 번째는 위치별로 동일하게 적용되는 작은 **피드포워드** **신경망**이다[[11]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,To%20facilitate%20these%20residual).

·       각 서브층 뒤에는 **잔차** **연결(residual connection)**과 **레이어** **정규화**가 있어 학습을 안정시킨다[[12]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,is%20%2C%20where%20is%20the).

### 3.2디코더 층

·       디코더 층도 구조는 비슷하지만, 인코더와 달리 **세** **개의** **서브층**으로 구성된다. 첫 번째는 이전에 생성된 출력에 대한 셀프 어텐션이고, 두 번째는 인코더의 출력(입력 문장 정보)에 대한 어텐션, 세 번째는 피드포워드 신경망이다[[13]](https://arxiv.org/html/1706.03762v7#:~:text=The%20decoder%20is%20also%20composed,at%20positions%20less%20than).

·       디코더의 셀프 어텐션에서는 **미래** **단어를** **보지** **않도록** **마스크(masking)**를 적용해, 모델이 이미 생성된 부분만 참고하게 한다【480715253073321†L234-L369】.

### 3.3위치 부호(Positional Encoding)

트랜스포머에는 RNN이나 CNN처럼 순서 정보를 처리하는 구조가 없다. 따라서 단어 위치 정보를 주입하기 위해 **사인과** **코사인** **파형으로** **구성된** **위치** **부호**를 입력 임베딩에 더한다[[14]](https://arxiv.org/html/1706.03762v7#:~:text=Since%20our%20model%20contains%20no,9). 이런 방식은 모델이 문장 길이를 넘어선 위치 관계를 일반화하는 데 도움을 준다[[15]](https://arxiv.org/html/1706.03762v7#:~:text=We%20also%20experimented%20with%20using,the%20ones%20encountered%20during%20training).

### 3.4왜 셀프 어텐션인가?

·       셀프 어텐션은 RNN과 CNN에 비해 한 층에서 **모든** **위치** **간의** **의존성을** **한** **번에** **계산**하므로 병렬화가 쉽다[[16]](https://arxiv.org/html/1706.03762v7#:~:text=4%20Why%20Self). RNN은 순차적으로 계산하기 때문에 긴 문장에서 병렬화가 어렵다[[3]](https://arxiv.org/html/1706.03762v7#:~:text=Recurrent%20models%20typically%20factor%20computation,The%20fundamental).

·       논문에서 비교한 표에 따르면 셀프 어텐션 층의 순차 연산 수는 **상수**이고, RNN은 시퀀스 길이에 비례하여 늘어난다[[17]](https://arxiv.org/html/1706.03762v7#:~:text=Table%201%3A%20%20Maximum%20path,Report%20issue%20for%20preceding%20element).

·       셀프 어텐션은 긴 문장에서도 정보가 오가는 **경로** **길이(path length)**가 짧아, 멀리 떨어진 단어 간 관계를 학습하기 쉽다[[18]](https://arxiv.org/html/1706.03762v7#:~:text=The%20third%20is%20the%20path,networks%20composed%20of%20the%20different).

## 4.학습과 성능

### 4.1학습 데이터

모델은 **영어→****독일어** 번역을 위해 약 450만 문장, **영어→****프랑스어** 번역을 위해 3,600만 문장으로 학습되었다[[19]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20on%20the%20standard,a%20set%20of%20sentence%20pairs). 입력과 출력은 **바이트-****쌍** **인코딩**이라는 방법으로 문장 단위를 세분화하여 3만여 개의 단위로 표현했다[[19]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20on%20the%20standard,a%20set%20of%20sentence%20pairs).

### 4.2결과 비교

논문은 트랜스포머를 기존 모델과 비교하면서 **BLEU** **점수**(번역 품질 측정 지표)와 학습 비용을 보고하였다. 아래 표는 영어→독일어(newstest2014) 결과를 간단히 정리한 것이다[[20]](https://arxiv.org/html/1706.03762v7#:~:text=Report%20issue%20for%20preceding%20element,8).

|  |  |  |
| --- | --- | --- |
| 모델 | BLEU 점수 | 특징 |
|  |  |  |
| --- | --- | --- |
| ByteNet | 23.75 | CNN 기반 시퀀스 모델 |
| GNMT + RL | 26.30 | 구글의 RNN 기반 모델, 보상학습 사용 |
| ConvS2S | 25.16 | CNN 기반 seq2seq 모델 |
| **Transformer (base)** | **27.3** | 멀티-헤드 어텐션 8개, 작은 파라미터 수 |
| **Transformer (big)** | **28.4** | 더 큰 차원과 헤드 수 사용, 최고 성능 |

트랜스포머의 **big** **모델**은 영어→독일어 번역에서 기존 최고 모델보다 **2 BLEU** 이상 높았으며, 영어→프랑스어에서도 단일 모델 기준 최고 성능을 기록했다[[21]](https://arxiv.org/html/1706.03762v7#:~:text=On%20the%20WMT%202014%20English,any%20of%20the%20competitive%20models). 또한 트랜스포머는 **훈련** **속도**가 매우 빨라 base 모델은 8개의 GPU로 **12****시간** 만에, big 모델은 **3.5****일** 만에 훈련되었다[[22]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20our%20models%20on,5%20days).

### 4.3다른 작업으로의 확장

트랜스포머는 문장 구조를 분석하는 **구문** **분석(parsing)** 작업에도 적용되어, 기존 RNN 모델들과 경쟁할 수 있는 성능을 보였다[[23]](https://arxiv.org/html/1706.03762v7#:~:text=6). 심지어 데이터가 적은 경우에도 다른 모델보다 좋은 성능을 보였고, 추가 학습 없이도 구조가 다른 작업에 잘 적응했다[[24]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20a%204,supervised%20setting).

## 5.결론 및 의의

·       **혁신적** **구조**: 트랜스포머는 RNN과 CNN을 완전히 배제하고, 오직 **어텐션** **메커니즘**만으로 입력과 출력을 연결한다[[25]](https://arxiv.org/html/1706.03762v7#:~:text=7%20Conclusion). 이는 시퀀스 모델링에서 큰 전환점이 되었다.

·       **병렬화와** **속도**: 셀프 어텐션의 병렬 처리 덕분에 훈련 속도가 빠르고, 긴 문장에서도 정보를 효율적으로 전달할 수 있다[[16]](https://arxiv.org/html/1706.03762v7#:~:text=4%20Why%20Self).

·       **성능** **향상**: 번역 작업에서 기존 최고 모델을 뛰어넘는 성능을 보여주었고[[21]](https://arxiv.org/html/1706.03762v7#:~:text=On%20the%20WMT%202014%20English,any%20of%20the%20competitive%20models), 구문 분석 같은 다른 언어 작업에도 확장 가능성을 보였다[[24]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20a%204,supervised%20setting).

·       **미래** **연구** **방향**: 논문에서는 트랜스포머를 **이미지,** **음성** 같은 다른 유형의 데이터에도 적용해보고, 긴 시퀀스에서 부분 어텐션을 연구하는 등 여러 확장 계획을 제시하였다[[26]](https://arxiv.org/html/1706.03762v7#:~:text=We%20are%20excited%20about%20the,inputs%20and%20outputs%20such%20as).

## 6.쉽게 이해하기 위한 비유

트랜스포머를 공부할 때는 다음과 같은 비유를 떠올려보자:

·       **어텐션은** **하이라이트** **펜**: 긴 문장을 읽을 때 중요한 단어에 형광펜으로 줄을 긋는 것처럼, 어텐션은 입력 문장에서 번역할 때 중요한 부분에 더 큰 가중치를 준다.

·       **멀티-****헤드** **어텐션은** **여러** **색의** **펜**: 하나의 형광펜만 사용하면 다양한 종류의 중요도를 표현하기 어렵다. 여러 색의 형광펜을 사용하면 문법, 의미, 위치 등 각기 다른 정보를 동시에 강조할 수 있다[[27]](https://arxiv.org/html/1706.03762v7#:~:text=Instead%20of%20performing%20a%20single,values%2C%20as%20depicted%20in%20Figure%C2%A02).

·       **잔차** **연결은** **메모지** **겹치기**: 두 가지 정보를 합칠 때, 이전 정보를 그대로 넘기고 새로운 정보를 위에 덧붙이는 것과 같다. 덕분에 학습이 안정되고 정보가 유실되지 않는다[[11]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,To%20facilitate%20these%20residual).

이상으로 트랜스포머 논문의 주요 아이디어를 쉽고 간단히 살펴보았다. 트랜스포머는 오늘날 자연어 처리 분야에서 가장 널리 사용되는 구조이며, 챗봇이나 번역 앱 등 여러 AI 서비스의 핵심을 이루고 있다.

---

[[1]](https://arxiv.org/html/1706.03762v7#:~:text=The%20dominant%20sequence%20transduction%20models,large%20and%20limited%20training%20data) [[2]](https://arxiv.org/html/1706.03762v7#:~:text=Most%20competitive%20neural%20sequence%20transduction,input%20when%20generating%20the%20next) [[3]](https://arxiv.org/html/1706.03762v7#:~:text=Recurrent%20models%20typically%20factor%20computation,The%20fundamental) [[4]](https://arxiv.org/html/1706.03762v7#:~:text=In%20this%20work%20we%20propose,hours%20on%20eight%20P100%20GPUs) [[5]](https://arxiv.org/html/1706.03762v7#:~:text=An%20attention%20function%20can%20be,query%20with%20the%20corresponding%20key) [[6]](https://arxiv.org/html/1706.03762v7#:~:text=We%20call%20our%20particular%20attention,the%20weights%20on%20the%20values) [[7]](https://arxiv.org/html/1706.03762v7#:~:text=Self,40%2C%2028%20%2C%20%2047) [[8]](https://arxiv.org/html/1706.03762v7#:~:text=Instead%20of%20performing%20a%20single,values%2C%20as%20depicted%20in%20Figure%C2%A02) [[9]](https://arxiv.org/html/1706.03762v7#:~:text=Multi,attention%20head%2C%20averaging%20inhibits%20this) [[10]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,produce%20outputs%20of%20dimension) [[11]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,To%20facilitate%20these%20residual) [[12]](https://arxiv.org/html/1706.03762v7#:~:text=The%20encoder%20is%20composed%20of,is%20%2C%20where%20is%20the) [[13]](https://arxiv.org/html/1706.03762v7#:~:text=The%20decoder%20is%20also%20composed,at%20positions%20less%20than) [[14]](https://arxiv.org/html/1706.03762v7#:~:text=Since%20our%20model%20contains%20no,9) [[15]](https://arxiv.org/html/1706.03762v7#:~:text=We%20also%20experimented%20with%20using,the%20ones%20encountered%20during%20training) [[16]](https://arxiv.org/html/1706.03762v7#:~:text=4%20Why%20Self) [[17]](https://arxiv.org/html/1706.03762v7#:~:text=Table%201%3A%20%20Maximum%20path,Report%20issue%20for%20preceding%20element) [[18]](https://arxiv.org/html/1706.03762v7#:~:text=The%20third%20is%20the%20path,networks%20composed%20of%20the%20different) [[19]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20on%20the%20standard,a%20set%20of%20sentence%20pairs) [[20]](https://arxiv.org/html/1706.03762v7#:~:text=Report%20issue%20for%20preceding%20element,8) [[21]](https://arxiv.org/html/1706.03762v7#:~:text=On%20the%20WMT%202014%20English,any%20of%20the%20competitive%20models) [[22]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20our%20models%20on,5%20days) [[23]](https://arxiv.org/html/1706.03762v7#:~:text=6) [[24]](https://arxiv.org/html/1706.03762v7#:~:text=We%20trained%20a%204,supervised%20setting) [[25]](https://arxiv.org/html/1706.03762v7#:~:text=7%20Conclusion) [[26]](https://arxiv.org/html/1706.03762v7#:~:text=We%20are%20excited%20about%20the,inputs%20and%20outputs%20such%20as) [[27]](https://arxiv.org/html/1706.03762v7#:~:text=Instead%20of%20performing%20a%20single,values%2C%20as%20depicted%20in%20Figure%C2%A02) Attention Is All You Need

<https://arxiv.org/html/1706.03762v7>

[Attention Is All You Need

Provided proper attribution is provided, Google hereby grants permission to reproduce the tables and figures in this paper solely for use in journalistic or scholarly works. Attention Is All You Need \ANDAshish Vaswani Google Brain avaswani@google.com &Noa

arxiv.org](https://arxiv.org/html/1706.03762v7)

[Attention is all You Need.pptx2.13MB](./file/Attention is all You Need.pptx)
