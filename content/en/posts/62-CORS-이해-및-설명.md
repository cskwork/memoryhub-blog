---
title: "CORS Understanding and Explanation"
date: 2024-05-25T14:46:18+09:00
slug: "62-CORS-이해-및-설명"
original_url: "https://memoryhub.tistory.com/62"
tistory_id: 62
draft: false
---

## CORS Definition

CORS is an abbreviation for Cross Origin Resource Sharing, which is a **security feature implemented in web browsers**.

Using this feature, a web application running on one domain can access resources from a different domain.

The **main purpose of CORS** is to **restrict access to resources from different domains to prevent malicious scripts from secretly stealing important data from other domains**.

CORS is implemented by setting several HTTP headers in the server response that the browser checks before providing resources.

These headers include Access-Control-Allow-Origin, Access-Control-Allow-Methods, Access-Control-Allow-Headers, and others.

To use CORS in a web application, you need to configure your server to send the appropriate headers in the response for each request that requires cross-origin access.

Once configured, client-side code can use technologies such as AJAX, Fetch API, or WebSockets to access restricted resources from different domains.

## CORS Headers Definition

1. Access-Control-Allow-Origin - **Specifies the source domain that can access the resource**. You can set the value to "*" to allow all origins or set it to a specific domain.
2. Access-Control-Allow-Methods - **Header that specifies the HTTP methods (e.g., GET, POST, etc.) that can access the resource**. This prevents unauthorized methods from being used to access the resource.
3. Access-Control-Allow-Headers - **Specifies the HTTP headers that can be sent in the request** (e.g., content type, authorization, etc.). This prevents unauthorized headers from being used to access the resource.
4. Access-Control-Max-Age - This header **specifies the time in seconds that the preflight request result can be cached**. This can reduce the need for repeated preflight requests.
5. Access-Control-Expose-Headers - This header **lists the HTTP headers that can be exposed to the browser**. This allows the browser to access certain headers that are hidden, such as custom headers used for authentication or caching.
6. Access-Control-Allow-Credentials - This header **indicates whether requests can be made using credentials such as cookies or authorization headers**. If set to true, the server must also include the Access-Control-Allow-Origin header with the specific origin making the request.

The headers work together to ensure that only authorized domains, methods, and headers can access the resource, preventing unauthorized access and data theft.

## How to Test CORS Allowed Without Extensions

- Adding a Parameter

One way to temporarily bypass **CORS** issues is to run Chrome with the **"--disable-web-security" flag**, which disables the same-origin policy and allows cross-origin requests.

To do this on Windows:

1. Close all instances of Chrome.
2. Right-click on the **Chrome shortcut** and select "Properties".
3. In the "Target" field, add "--disable-web-security" after the Chrome executable path at the end of the command. For example, the target field should look like: "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --disable-web-security
4. Click "Apply" and then "OK" to save the changes.
5. Run Chrome using the modified shortcut.

This method is not recommended for general browsing and should only be used for development and testing purposes.

## Source: ChatGPT
