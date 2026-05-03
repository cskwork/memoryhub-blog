---
title: "Javascript Promise"
date: 2024-05-25T14:48:44+09:00
slug: "64-Javascript-Promise"
original_url: "https://memoryhub.tistory.com/64"
tistory_id: 64
draft: false
categories: ["데브 언어"]
tags: ["Javascript"]
cover:
  image: "/images/64-Javascript-Promise/img.png"
  relative: false
  hidden: false
---

![](/images/64-Javascript-Promise/img.png)

## Promise 등장 배경 : 콜백 지옥!

JavaScript를 작성할 때 종종 다른 작업에 의존하는(순차적인) 작업을 처리해야 해!

**이미지 조회 후 저장하기 예제**

이미지를 가져 와서 압축하고 필터를 적용하고 저장?하는 작업이 필요하다고 가정해보면.

![](/images/64-Javascript-Promise/img_1.png)

- 1 먼저 getImage 함수가 편집하려는 이미를 얻고! 해당 이미지가 성공적으로 조회 된 후에만 해당 값을
- 2 resizeImage 함수에 전달하고
- 3 이미지 크기가 성공적으로 조정되면 applyFilter 함수로 이미지에 필터를 적용해.
- 4 이미지가 압축되고 필터를 추가한 후 이미지를 저장하고 (saveImage) 사용자에게 모든 것이 올바르게 작동했다는 걸 알려줘 (console.log)

근데 이 방식은 너무 지저분하지 않아? 이전 콜백 함수에 의존하는 너무 많은 중첩 콜백 함수가 생겨. 이건 콜백 지옥으로도 부르는데, 코드 읽기가 어렵고 유지보수할 때 엄청 오래걸릴 수 있어

그래서 똑똑한 개발자들이 이 문제를 해결할 수 있는 Promise 라는 걸 만들었어

## Promise 문법 : 상태값과 결과값

ES6 규정에 첨 소개된 **Promise** 의 정의

"promise는 미래의 어느 시점에 해결되거나 거부될 수 있는 가치에 대한 자리 표시자."

무슨 말이야…? ? 어쨋든 미래에 뭔가 처리해주는 것 같긴한데… promise는 약속이란 거잖아. 그래서 미래의 어떤 약속을 지킨다는 얘기인가. 약속을 안지키면 어떻게 되는거야?

실습을 통해 설명해야 겠어. 콘솔로 같이 한번 따라해봐!

```
new Promise(() => {})
```

![](/images/64-Javascript-Promise/img_2.png)

**Promise 는** 상태([[**Promise 상태(status)**]]) 및 값([[**Promise 값(Result/Value)**]])을 포함하는 개체야.

위의 예에서 [[PromiseStatus]]의 값이 "보류 중/pending"이고 Promise 값이 정의되지 않지?

일단은 이렇게 두 가지 속성 값이 있다는 것만 알고! - (어차피 이 개체와 상호 작용할 필요 없고 [[PromiseStatus]] 및 [[PromiseValue]] 속성에 직접 접근할 수도 없어!)

그치만 이 속성 값은 Promise에서 정말 중요해!

PromiseStatus / Promise 상태 값은 다음 세 가지 값 중 하나야.

✅ 성취됨/fulfilled: Promise가 해결되었습니다. (약속을 지켰다!) 모든 것이 잘되었고 Promise ? 내에서 오류가 발생하지 않았습니다.  
❌ 거부됨/rejected : Promise 가 거부되었습니다. 뭔가 잘못되었습니다 ..  
⏳ 보류 중/pending: Promise 가 해결되거나 거부되지 않았으며 아직 Promise가 보류 중입니다.  
좋아, 그럼 Promise 상태가 "보류 중", "이행 됨"또는 "거부 됨"은 언제인가요? 그리고 이 상태값은 왜 중요합니까?

위의 예에서 간단한 콜백 함수 **() => {}**를 Promise 생성자에 전달했어. 근데 이 콜백 함수는 실제로는 **두 개의 인수를 받아**. **첫 번째 인수값은** 종종 **resolve(해결)** 또는 res라고 하고 Promise가 해결되어야 할 때 호출되는 메서드야. **두 번째 인수값은** 종종 **reject(거부)** 또는 rej라고 불리는 Promise가 거부해야 할 때 호출되는 값 메서드야.

![](/images/64-Javascript-Promise/img_3.png)

한번 해볼까?

```
new Promise((res, rej) => res("야호! 안녕"));
new Promise((res, rej) => rej("아냐! 바이"));
```

![](/images/64-Javascript-Promise/img_4.png)

잘했어!

우리가 첨에 인수 값이 돌렸던 new Promise 에서 PromiseState 보류 중 (pending) 상태하고 PromiseResult 정의되지 않은(undefined) 값을 제거하는 방법을 알게됐어!

resolve 메서드를 호출한 경우 Promise 상태는 "이행/fulfilled"되고, 거부된 메서드를 호출한 경우 Promise 상태는 "거부됨/rejected" 가 발생해.

Promise의 값, [[PromiseValue]]의 값은 해결되거나 거부된 메서드에 인수로 전달하는 값이야.

이미지 조회 후 저장하기 예제 이미지 최초 조회 (getImage) 만 Promise 방식으로 전환해 보자

```
// 1  new Promise 객체 사용 함수
function getImage(file){
  return new Promise((res, rej) => {
    try {
      const data = readFile(file);
      resolve(data);
    } catch (error) {
      reject(new Error(err))
    }
  })
}
```

음 근데 Promise객체를 굳이 매번 만들 필요 없고 데이터만 가져오면 되는데 더 간단한 방법은 없을까?

Promise의 3 가지 방법

- 1 **.then()** : **Promise resolved(해결된)** 후에 호출.
- 2 **.catch()**: **Promise rejected(거부된)** 후에 호출.
- 3 **.finally ()** : Promise가 해결되었는지 거부되었는지에 관계없이 **항상** 호출.

```
getImage("./image.png") 
  .then(res=> console.log(res)) // resolve PromiseValue
  .catch(error => console.log(error)) // reject PromiseValue
  .finally( ()=> console.log("끝!"))
```

그럼 우리가 아까 작업했던 **이미지 조회 후 저장하기 예제**를 최종적으로 다시 만들어볼까?

```
getImage("./image.png") 
  .then(image => compressImage(image))
  .then(compressImage => applyFilter(compressImage))
  .then(filteredImage => saveImage(filteredImage))
  .then(res => console.log("Successfully saved Image!"))
  .catch(err => {throw new Error(err)})
```

그리고 이런 것도 가능해!

![](/images/64-Javascript-Promise/img_5.png)

다음 시간엔 Promise하고 event loop가 어떻게 연결되는지 알아볼거야. (엄청 쉬움)

**티저** :

![](/images/64-Javascript-Promise/img.gif)

## 참고

[⭐️? JavaScript Visualized: Promises & Async/Await - DEV Community](https://dev.to/lydiahallie/javascript-visualized-promises-async-await-5gke)

[Promise icons created by manshagraphics - Flaticon](https://www.flaticon.com/free-icons/promise)
