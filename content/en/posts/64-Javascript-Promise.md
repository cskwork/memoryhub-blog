---
title: "Javascript Promise"
date: 2024-05-25T14:48:44+09:00
slug: "64-Javascript-Promise"
original_url: "https://memoryhub.tistory.com/64"
tistory_id: 64
draft: false
categories: ["Dev Language"]
tags: ["Javascript"]
cover:
  image: "/images/64-Javascript-Promise/img.png"
  relative: false
  hidden: false
---

![](/images/64-Javascript-Promise/img.png)

## Promise Background: Callback Hell!

When writing JavaScript, you often need to handle sequential tasks that depend on other tasks.

**Example: Getting and Saving an Image**

Suppose you need to fetch an image, compress it, apply filters, and save it.

![](/images/64-Javascript-Promise/img_1.png)

- 1 First, the getImage function fetches the image you want to edit! Only after that image is successfully retrieved
- 2 Pass that value to the resizeImage function
- 3 Once the image is successfully resized, apply filters to the image with the applyFilter function
- 4 After compressing the image and adding filters, save the image (saveImage) and let the user know that everything worked correctly (console.log)

But isn't this approach too messy? Too many nested callback functions depending on previous callbacks are created. This is also called callback hell, and it can be very difficult to read and time-consuming to maintain.

So smart developers created something called Promise to solve this problem.

## Promise Syntax: Status and Result

The definition of **Promise** first introduced in the ES6 specification:

"a promise is a placeholder for a value that can be resolved or rejected at some point in the future."

What does that mean? Anyway, it seems like something will be processed in the future. Promise means "promise" after all. So you're talking about keeping some promise in the future. What happens if you break the promise?

I should explain through practice. Try following along with the console!

```
new Promise(() => {})
```

![](/images/64-Javascript-Promise/img_2.png)

**Promise** is an object containing a status ([[**Promise Status**]]) and a value ([[**Promise Result/Value**]]).

In the example above, the value of [[PromiseStatus]] is "pending" and the Promise value is undefined, right?

For now, just know that there are these two property values! - (You don't need to interact with this object anyway, and you can't directly access the [[PromiseStatus]] and [[PromiseValue]] properties!)

But these property values are really important in Promise!

The PromiseStatus / Promise status value is one of three values:

✅ fulfilled: The Promise has been resolved. (You kept the promise!) Everything went well and no errors occurred within the Promise.
❌ rejected: The Promise was rejected. Something went wrong...
⏳ pending: The Promise has not been resolved or rejected yet and is still pending.

Okay, so when is the Promise status "pending", "fulfilled", or "rejected"? And why is this status value important?

In the example above, I passed a simple callback function **() => {}** to the Promise constructor. But this callback function actually receives **two arguments**. The **first argument** is often called **resolve** or res, and it's a method called when the Promise should be resolved. The **second argument** is often called **reject** or rej, a method value called when the Promise should be rejected.

![](/images/64-Javascript-Promise/img_3.png)

Want to try?

```
new Promise((res, rej) => res("Yay! Hello"));
new Promise((res, rej) => rej("Nope! Bye"));
```

![](/images/64-Javascript-Promise/img_4.png)

Good job!

We now know how to remove the pending state and undefined value from the new Promise we first tried with arguments!

When you call the resolve method, the Promise status becomes "fulfilled", and when you call the rejected method, the Promise status becomes "rejected".

The value of the Promise, [[PromiseValue]], is the value passed as an argument to the resolved or rejected method.

Let's convert just the initial image retrieval (getImage) from the "Get and Save Image Example" to Promise style.

```
// 1 Function using new Promise object
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

But I don't need to create a Promise object every time if I just need to fetch data. Isn't there a simpler way?

Promise's 3 Methods

- 1 **.then()**: Called after Promise is **resolved**.
- 2 **.catch()**: Called after Promise is **rejected**.
- 3 **.finally()**: Always called regardless of whether the Promise is resolved or rejected.

```
getImage("./image.png") 
  .then(res=> console.log(res)) // resolve PromiseValue
  .catch(error => console.log(error)) // reject PromiseValue
  .finally( ()=> console.log("Done!"))
```

So let's finally recreate the **Get and Save Image Example** we worked on earlier?

```
getImage("./image.png") 
  .then(image => compressImage(image))
  .then(compressImage => applyFilter(compressImage))
  .then(filteredImage => saveImage(filteredImage))
  .then(res => console.log("Successfully saved Image!"))
  .catch(err => {throw new Error(err)})
```

And this is also possible!

![](/images/64-Javascript-Promise/img_5.png)

Next time we'll explore how Promise and the event loop are connected. (It's very easy)

**Teaser**:

![](/images/64-Javascript-Promise/img.gif)

## References

[⭐️🔥 JavaScript Visualized: Promises & Async/Await - DEV Community](https://dev.to/lydiahallie/javascript-visualized-promises-async-await-5gke)

[Promise icons created by manshagraphics - Flaticon](https://www.flaticon.com/free-icons/promise)
