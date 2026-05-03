---
title: "Git Introduction and Guide"
date: 2024-05-26T10:57:15+09:00
slug: "95-Git-소개-및-가이드"
original_url: "https://memoryhub.tistory.com/95"
tistory_id: 95
draft: false
categories: ["Dev Ops"]
tags: ["Git"]
  hidden: false
cover:
  image: "/images/95-Git-소개-및-가이드/002.png"
  relative: false
  hidden: false
---

![](/images/95-Git-소개-및-가이드/002.png)

Today, let's learn about **Git, the representative version control system**! Git is an essential technology that every developer must know and a core tool for team collaboration. In this article, we'll explore Git from its basic concepts to practical usage step by step.

---

## 1. What is Git?

Git is a Distributed Version Control System (DVCS) that tracks changes to various files including source code and facilitates collaboration.

- **Concept Summary**: A system that records changes to source code, documents, and other files, allowing you to revert to specific points in time or enable multiple people to work simultaneously.
- **Real-World Example**: Imagine you're writing a document and need to revert to a previous version. A regular document editor makes this impossible without manually saving previous versions, but Git automatically tracks changes at every moment, letting you revert anytime.
- **What Problems Does It Solve?**
  - Prevents modifications from becoming tangled or disappearing
  - Efficiently merges source code without conflicts in team projects
  - Provides safe backup and history management

---

## 2. How Does It Work?

### 2.1 Basic Concepts

Git has two basic structures: a Local Repository and a Remote Repository.

- **Local Repository**: The version control space on your computer
- **Remote Repository**: Repositories hosted on servers like GitHub, GitLab, etc.

The version management process generally goes through these stages:

1) **Working Directory**: The directory where actual work occurs (modifications, additions, etc.)  
2) **Staging Area**: A temporary space to gather changes you want to commit  
3) **Local Repository**: Where changes are finally recorded (commit)

```
# Git basic flow
$ git add <filename>  # Add changed files to Staging Area
$ git commit -m "commit message"  # Commit changes to Local Repository
$ git push origin main  # Push to remote repository
```

### 2.2 Practical Application Example

#### Example Scenario

- **Project Initialization**

  ```
  $ git init
  ```

  - A `.git` folder is created in the current directory, initializing a Git repository.
- **File Creation and Modification**

  ```
  # Create file in working directory
  $ echo "Hello Git" > hello.txt
  ```
- **Committing**

  ```
  $ git add hello.txt           # Add to Staging Area
  $ git commit -m "Add hello.txt file"
  ```
- **Connecting to Remote Repository**

  ```
  $ git remote add origin https://github.com/username/repo.git
  $ git push -u origin main
  ```

  - Now the remote repository is connected, enabling collaboration with others.

### How It Works

1. **Modify Locally**: Edit files in your local environment and use add to stage the changes.
2. **Create Snapshot with Commit**: Perform a commit to save "this point in time's changes."
3. **Sync Remote Repository with Push**: Push to remote repositories (GitHub, GitLab, etc.) to share with team members.

---

## 3. Key Advantages

1. **Easy History Tracking and Recovery**: All changes are recorded as commits, allowing you to revert to any specific version anytime.
2. **Distributed Structure**: Storing all history locally means you can manage versions without internet connection and remain safe from server failures.
3. **Optimized for Collaboration**: Multiple people can work simultaneously on independent branches and merge later.

---

## 4. Important Cautions

1. **Conflict Management**: Conflicts occur when multiple people modify the same section. Git can't resolve this automatically—you must manually decide which changes to keep.
2. **Proper Branch Strategy**: As projects scale, you need a strategy for how to use and merge branches (git-flow, GitHub Flow, etc.).
3. **Commit Message Writing Rules**: Without commit message conventions in collaboration, history becomes messy and productivity drops significantly.

---

## 5. Practical Usage Example

Below is a simple example of conducting a simple programming project using Git.

```
# 1. Create and initialize folder
$ mkdir sample-project
$ cd sample-project
$ git init

# 2. Create file
$ echo "print('Hello Git!')" > app.py

# 3. Add and commit
$ git add app.py
$ git commit -m "Initial commit"

# 4. Create and switch to branch
$ git checkout -b feature/add-logging

# 5. Implement logging feature
echo "
import logging

logging.basicConfig(level=logging.INFO)
logging.info('Logging initiated')
" >> app.py

# 6. Commit changes
$ git add app.py
$ git commit -m "Add logging feature"

# 7. Merge to main branch
$ git checkout main
$ git merge feature/add-logging
```

Through this process, you can develop desired features quickly and easily roll back to previous versions if problems arise later.

---

## 6. Conclusion

Git is an **indispensable tool** for **version management** and **collaboration**. It's widely used from personal projects to large-scale team development, and carefully tracking change history provides a great safety net.

Once you master Git, you can transparently manage any code changes and freely return to the past whenever needed.

"Using this technology enables you to **increase collaboration productivity and operate projects stably**!"

---

### References and Sources

- [Git Official Documentation](https://git-scm.com/)
- [Pro Git - Free Book](https://git-scm.com/book/en/v2)
- [GitHub Guides](https://guides.github.com/)

Experience safer and more efficient source code management through Git!
