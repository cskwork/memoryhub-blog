---
title: "Can you add custom remote repositories to Maven? How?"
date: 2024-05-29T07:52:22+09:00
slug: "152-Can-you-add-custom-remote-repositories-to-Maven-How"
original_url: "https://memoryhub.tistory.com/152"
tistory_id: 152
draft: false
---

*Yes, you can add custom remote repositories to Maven by configuring the `pom.xml` file or the `settings.xml` file.*

### Adding Custom Remote Repositories to Maven

#### 1. Configuring the POM File

You can specify custom remote repositories directly in your project's `pom.xml` file. This allows Maven to search these repositories for dependencies needed by your project.

Here’s how you can add custom repositories in the `pom.xml` file:

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0-SNAPSHOT</version>

    <repositories>
        <repository>
            <id>central</id>
            <url>https://repo.maven.apache.org/maven2</url>
        </repository>
        <repository>
            <id>custom-repo</id>
            <url>https://my.custom.repo/repository</url>
            <snapshots>
                <enabled>true</enabled>
            </snapshots>
            <releases>
                <enabled>true</enabled>
            </releases>
        </repository>
    </repositories>
</project>
```

- `<repositories>`: The section where custom repositories are defined.
- `<repository>`: Each custom repository is defined within this tag.
- `<id>`: A unique identifier for the repository.
- `<url>`: The URL where the repository is hosted.
- `<snapshots>` and `<releases>`: These sections specify whether the repository should be used for snapshot versions and release versions of artifacts, respectively.

#### 2. Configuring the Settings File

Alternatively, you can add custom repositories in the global or user-specific `settings.xml` file, which is found in the Maven `conf` directory or the `.m2` directory, respectively. This approach applies the repository settings to all Maven projects on your system.

Here’s how you can add custom repositories in the `settings.xml` file:

```
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0 
          http://maven.apache.org/xsd/settings-1.0.0.xsd">

    <profiles>
        <profile>
            <id>custom-repo-profile</id>
            <repositories>
                <repository>
                    <id>central</id>
                    <url>https://repo.maven.apache.org/maven2</url>
                </repository>
                <repository>
                    <id>custom-repo</id>
                    <url>https://my.custom.repo/repository</url>
                    <snapshots>
                        <enabled>true</enabled>
                    </snapshots>
                    <releases>
                        <enabled>true</enabled>
                    </releases>
                </repository>
            </repositories>
        </profile>
    </profiles>

    <activeProfiles>
        <activeProfile>custom-repo-profile</activeProfile>
    </activeProfiles>
</settings>
```

- `<profiles>`: Defines different profiles for various configurations.
- `<profile>`: Each profile can have its own repository settings.
- `<activeProfiles>`: Specifies which profiles are active by default.

### Summary

You can add custom remote repositories to Maven either by configuring the `pom.xml` file for project-specific settings or the `settings.xml` file for global settings. This allows Maven to fetch dependencies from additional sources beyond the default central repository.

### Test Your Understanding

1. What is the purpose of adding custom repositories in Maven?
2. What is the difference between configuring repositories in the `pom.xml` file and the `settings.xml` file?
3. How do you enable snapshot and release repositories in the repository configuration?

### Reference

For more details, refer to the [Apache Maven Project Documentation on Repositories](https://maven.apache.org/guides/mini/guide-multiple-repositories.html).
