---
title: "Resolving application.yml Recognition Issue in IntelliJ Community Edition"
date: 2025-03-25T18:10:32+09:00
slug: "525-IntelliJ-Community-Edition에서-application-yml-인식-문제-해결"
original_url: "https://memoryhub.tistory.com/525"
tistory_id: 525
draft: false
categories: ["Dev Concepts"]
tags: ["Tech News"]
cover:
  image: "image example"
  alt: "Run Configuration menu"
  relative: false
  hidden: false
---

## Problem

IntelliJ Community Edition fails to read the application.yml file when running Gradle bootRun

## Solution

### 1. Setting Environment Variables

1. Select your main class and right-click
2. Select **Edit Configurations...**

![Run Configuration menu](image example)

### 2. Add Environment Variables

1. In the **Run/Debug Configurations** window, find the **Environment variables** field
2. Enter the following value: `SPRING_PROFILES_ACTIVE=dev`
3. Click **Apply** and **OK**

![Environment variable configuration](image example)

### 3. Run Application

1. Run the application normally (Run or Debug)
2. Check the logs to confirm that application.yml is being loaded correctly

## Alternative Methods (if needed)

**Setting via VM options:**

1. **Edit Configurations** → Enter in **VM options** field:  
   `-Dspring.profiles.active=dev`

**Setting via Program arguments:**

1. **Edit Configurations** → Enter in **Program arguments** field:  
   `--spring.profiles.active=dev`

---

※ Note: This configuration must be set each time in a new run configuration.
