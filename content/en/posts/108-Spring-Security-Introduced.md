---
title: "Spring Security Introduced"
date: 2024-05-29T12:20:18+09:00
slug: "108-Spring-Security-Introduced"
original_url: "https://memoryhub.tistory.com/108"
tistory_id: 108
draft: false
categories: ["Dev Framework"]
tags: ["Spring"]
---

*Spring Security is like a security guard for your web applications, ensuring that only authorized users can access certain parts and protecting against various threats.*

### The Big Picture

Imagine your web application is like a museum. You want to allow visitors to explore certain sections freely, but some areas should be restricted to staff only. Additionally, you need to protect valuable exhibits from being tampered with. Spring Security acts as the guard and the surveillance system, ensuring that visitors have the right tickets (authentication) and only access areas they are allowed to (authorization), while also protecting against various threats (like CSRF attacks).

### Core Concepts

1. **Authentication**: Verifying the identity of a user (like checking a visitor's ticket).
2. **Authorization**: Determining whether a user has permission to access a specific resource (like allowing only staff to enter restricted areas).
3. **CSRF Protection**: Preventing cross-site request forgery attacks, which can be thought of as protecting against unauthorized actions performed on behalf of authenticated users.
4. **Security Filters**: A series of checks and rules that requests go through to ensure they are safe and authorized.
5. **User Details Service**: A component that retrieves user information (like a staff directory).

### Detailed Walkthrough

Let's dive deeper into these concepts:

#### Authentication

Authentication in Spring Security is about verifying who a user is. This can be done using various methods like username and password, OAuth tokens, or other credentials.

- **Example**: When a user logs in with their username and password, Spring Security checks these credentials against a database or another user store. If the credentials match, the user is authenticated.

#### Authorization

Once authenticated, Spring Security needs to determine what the user is allowed to do.

- **Example**: After logging in, an authenticated user might be allowed to view their profile but not access the admin dashboard. Spring Security uses roles and permissions to manage this.

#### CSRF Protection

Cross-Site Request Forgery (CSRF) is an attack where unauthorized commands are transmitted from a user that the web application trusts. Spring Security provides mechanisms to protect against these attacks.

- **Example**: When submitting a form, Spring Security can ensure that the request includes a unique token that verifies the request came from the authenticated user.

#### Security Filters

Security filters are the backbone of Spring Security. Each filter performs a specific task, like checking credentials or enforcing access rules.

- **Example**: When a request is made to the server, it passes through a chain of filters. One filter might check if the user is authenticated, another might check if they have the right role, and so on.

#### User Details Service

The UserDetailsService is a core interface in Spring Security that loads user-specific data. It is used throughout the framework as a way to find the user based on their username.

- **Example**: When a user logs in, Spring Security uses the UserDetailsService to fetch user information (like username, password, and roles) from a database.

### Understanding Through an Example

Consider a simple web application where users can view public content, log in to see private content, and administrators can manage all content.

1. **Public Content**: No authentication or authorization needed.
2. **Private Content**: Requires authentication (username/password).
3. **Admin Dashboard**: Requires both authentication and specific authorization (admin role).

Here’s a simplified code example of how Spring Security might be configured for this application:

```
@Configuration
@EnableWebSecurity
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
            .authorizeRequests()
                .antMatchers("/public/**").permitAll() // Public pages
                .antMatchers("/private/**").authenticated() // Requires authentication
                .antMatchers("/admin/**").hasRole("ADMIN") // Requires admin role
                .and()
            .formLogin()
                .loginPage("/login") // Custom login page
                .permitAll()
                .and()
            .logout()
                .permitAll()
                .and()
            .csrf().disable(); // Disable CSRF for simplicity in this example
    }

    @Bean
    @Override
    public UserDetailsService userDetailsService() {
        UserDetails user = 
             User.withDefaultPasswordEncoder()
                .username("user")
                .password("password")
                .roles("USER")
                .build();

        UserDetails admin = 
             User.withDefaultPasswordEncoder()
                .username("admin")
                .password("admin")
                .roles("ADMIN")
                .build();

        return new InMemoryUserDetailsManager(user, admin);
    }
}
```

### Conclusion and Summary

Spring Security is a powerful and flexible framework for securing web applications. It handles authentication (verifying user identity) and authorization (checking user permissions), and protects against threats like CSRF. By using a series of security filters and services, it ensures that only authorized users can access certain parts of an application.

### Test Your Understanding

1. What is the difference between authentication and authorization?
2. How does Spring Security protect against CSRF attacks?
3. What role does the UserDetailsService play in Spring Security?

### Reference

For further learning, you can refer to the official Spring Security documentation: [Spring Security Reference](https://docs.spring.io/spring-security/site/docs/current/reference/html5/).
