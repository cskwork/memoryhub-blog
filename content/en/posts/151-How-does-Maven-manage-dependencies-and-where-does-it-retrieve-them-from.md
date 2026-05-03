---
title: "How does Maven manage dependencies, and where does it retrieve them from?"
date: 2024-05-29T07:50:54+09:00
slug: "151-How-does-Maven-manage-dependencies-and-where-does-it-retrieve-them-from"
original_url: "https://memoryhub.tistory.com/151"
tistory_id: 151
draft: false
categories: ["Dev Ops"]
tags: ["Maven"]
---

*Maven manages dependencies by defining them in the POM file and retrieving them from repositories, which can be local or remote.*

### How Maven Manages Dependencies

1. **Defining Dependencies in the POM File**:

   - Dependencies are specified in the `<dependencies>` section of the `pom.xml` file. Each dependency is identified by its group ID, artifact ID, version, and optional scope.

     ```
     <dependencies>
         <dependency>
             <groupId>org.springframework</groupId>
             <artifactId>spring-core</artifactId>
             <version>5.2.0.RELEASE</version>
         </dependency>
         <dependency>
             <groupId>junit</groupId>
             <artifactId>junit</artifactId>
             <version>4.13.1</version>
             <scope>test</scope>
         </dependency>
     </dependencies>
     ```
2. **Dependency Scope**:

   - Scopes control the classpath of the various build tasks (e.g., compiling and testing). Common scopes include:
     - `compile`: Default scope, available in all classpaths.
     - `provided`: Needed for compilation but provided by the runtime environment.
     - `runtime`: Not needed for compilation, but required for execution.
     - `test`: Used only for testing.
3. **Transitive Dependencies**:

   - Maven automatically resolves transitive dependencies, which are dependencies of your dependencies. For example, if your project depends on Library A, which in turn depends on Library B, Maven will include both A and B in your project.

### Where Maven Retrieves Dependencies From

1. **Local Repository**:

   - The local repository is a directory on your machine where Maven stores all the downloaded dependencies. By default, this is located in the `.m2/repository` directory in your home directory.
   - If a dependency is already in the local repository, Maven will use it directly, saving the need to download it again.
2. **Remote Repositories**:

   - Maven retrieves dependencies from remote repositories when they are not available in the local repository.
   - The central repository (<https://repo.maven.apache.org/maven2>) is the default remote repository Maven uses.
   - Additional remote repositories can be configured in the `pom.xml` file or in the `settings.xml` file. For example:

     ```
     <repositories>
         <repository>
             <id>central</id>
             <url>https://repo.maven.apache.org/maven2</url>
         </repository>
         <repository>
             <id>my-custom-repo</id>
             <url>https://my.custom.repo/repository</url>
         </repository>
     </repositories>
     ```

### Summary

Maven simplifies dependency management by allowing developers to declare dependencies in the POM file. It retrieves these dependencies from the local repository, and if not found, it fetches them from remote repositories. This system ensures that all required libraries are available for the project and handles transitive dependencies automatically.

### Test Your Understanding

1. What is the default location of the local repository in Maven?
2. How does Maven handle transitive dependencies?
3. Can you add custom remote repositories to Maven? How?

### Reference

For further details, you can check out the [Maven Dependency Mechanism Documentation](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html).
