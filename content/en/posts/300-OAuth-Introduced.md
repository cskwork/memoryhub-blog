---
title: "OAuth Introduced"
date: 2024-06-17T17:25:02+09:00
slug: "300-OAuth-Introduced"
original_url: "https://memoryhub.tistory.com/300"
tistory_id: 300
draft: false
categories: ["Dev Framework"]
tags: ["Spring Security"]
---

*OAuth is a protocol that allows secure authorization in a simple and standardized way from web, mobile, and desktop applications.*

### The Big Picture

Imagine you want to give your friend access to a specific photo album in your locked drawer, but you don't want to give them the key to your entire house. OAuth works in a similar way for online services. It allows one application (the client) to access resources (like photos, emails, or profile information) from another application (the service provider) on behalf of a user, without sharing the user's credentials.

### Core Concepts

1. **Resource Owner**: The user who authorizes an application to access their account.
2. **Client**: The application requesting access to the user's account.
3. **Resource Server**: The server hosting the protected resources (e.g., user photos).
4. **Authorization Server**: The server that authenticates the user and issues access tokens.
5. **Access Token**: A token that the client uses to make authenticated requests on behalf of the user.

### Detailed Walkthrough

#### 1. Authorization Flow

OAuth typically involves the following steps:

1. **Authorization Request**: The client requests authorization from the resource owner (the user).
2. **Authorization Grant**: The resource owner approves the request.
3. **Token Request**: The client requests an access token from the authorization server.
4. **Token Response**: The authorization server issues an access token.
5. **Resource Request**: The client uses the access token to request resources from the resource server.

#### 2. Creating OAuth in Java

To implement OAuth in Java, you'll often use libraries like Spring Security OAuth, which simplifies the process. Here's a step-by-step guide to creating an OAuth 2.0 client in Java using Spring Boot:

##### Step 1: Setup Your Project

Create a new Spring Boot project. You can use [Spring Initializr](https://start.spring.io/) to generate a basic project with the necessary dependencies:

- Spring Web
- Spring Security
- OAuth2 Client

##### Step 2: Configure OAuth2 Client

In your `application.yml` or `application.properties` file, configure the OAuth2 client details:

```
spring:
  security:
    oauth2:
      client:
        registration:
          google:
            client-id: YOUR_CLIENT_ID
            client-secret: YOUR_CLIENT_SECRET
            scope: profile, email
            redirect-uri: "{baseUrl}/login/oauth2/code/google"
            authorization-grant-type: authorization_code
            client-name: Google
        provider:
          google:
            authorization-uri: https://accounts.google.com/o/oauth2/auth
            token-uri: https://oauth2.googleapis.com/token
            user-info-uri: https://www.googleapis.com/oauth2/v3/userinfo
            user-name-attribute: sub
```

Replace `YOUR_CLIENT_ID` and `YOUR_CLIENT_SECRET` with the credentials you get from the OAuth provider (e.g., Google).

##### Step 3: Create Security Configuration

Create a security configuration class to enable OAuth2 login:

```
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/").permitAll()
                .anyRequest().authenticated()
                .and()
            .oauth2Login();
    }
}
```

##### Step 4: Handle OAuth2 Login Success

Create a controller to handle the login success and retrieve user information:

```
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.oauth2.core.user.OAuth2User;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class LoginController {

    @GetMapping("/loginSuccess")
    public String loginSuccess(@AuthenticationPrincipal OAuth2User oauth2User, Model model) {
        model.addAttribute("name", oauth2User.getAttribute("name"));
        return "loginSuccess";
    }
}
```

##### Step 5: Create a View

Create an HTML view (`loginSuccess.html`) to display the user information:

```
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <title>Login Success</title>
</head>
<body>
    <h1>Welcome, <span th:text="${name}">User</span>!</h1>
</body>
</html>
```

### Understanding Through an Example

Let's consider a real-world example: logging in to a website using Google. Here's a simplified sequence of events:

1. **User tries to log in to the website**: The client (website) redirects the user to the Google OAuth2 authorization page.
2. **User grants permission**: The user logs in to Google and grants permission to the website to access their profile information.
3. **Website receives authorization code**: Google redirects the user back to the website with an authorization code.
4. **Website requests access token**: The website exchanges the authorization code for an access token from Google's token endpoint.
5. **Website accesses user data**: The website uses the access token to request the user's profile information from Google's resource server.

### Conclusion and Summary

OAuth is a powerful protocol that enables secure authorization between applications. By following the steps above, you can set up an OAuth2 client in a Java application using Spring Boot. The key components include configuring the OAuth2 client, setting up security configurations, and handling the login success to retrieve user information.

### Test Your Understanding

1. What are the main roles in the OAuth2 framework?
2. How does an authorization code flow differ from an implicit flow in OAuth2?
3. What is the purpose of the access token?

### Reference

For more detailed information on OAuth2, you can refer to the official documentation of [Spring Security OAuth](https://docs.spring.io/spring-security-oauth2-boot/docs/current/reference/html5/).
