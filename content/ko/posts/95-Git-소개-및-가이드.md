---
title: "Git 소개 및 가이드"
date: 2024-05-26T10:57:15+09:00
slug: "95-Git-소개-및-가이드"
original_url: "https://memoryhub.tistory.com/95"
tistory_id: 95
draft: false
categories: ["데브 옵스"]
tags: ["Git"]
cover:
  image: "images/95-Git-%EC%86%8C%EA%B0%9C-%EB%B0%8F-%EA%B0%80%EC%9D%B4%EB%93%9C/002.png"
  relative: false
  hidden: false
---

![](/images/95-Git-%EC%86%8C%EA%B0%9C-%EB%B0%8F-%EA%B0%80%EC%9D%B4%EB%93%9C/002.png)

오늘은 **버전 관리 시스템의 대표주자 Git**에 대해 알아보겠습니다! Git은 개발자라면 꼭 알아두어야 할 필수 기술이자, 팀 협업의 핵심 도구입니다. 이번 글에서는 Git의 개념부터 실제 사용 방법까지, 단계별로 자세히 알아보겠습니다.

---

## 1. Git이란? ?

Git은 분산 버전 관리 시스템(Distributed Version Control System, DVCS)으로, 소스 코드를 포함한 다양한 파일의 변경 이력을 추적하고 협업을 용이하게 해주는 도구입니다.

- ? **개념 요약**: 소스 코드나 문서 등의 변경 사항을 기록하고, 특정 시점으로 되돌리거나 여러 사람이 동시에 작업할 수 있도록 만들어 주는 시스템입니다.
- ? **실생활 예시**: 문서 작성을 하다가, 이전 버전으로 되돌려야 하는 상황이 있다고 가정해 봅시다. 일반 문서 편집기는 이전 버전을 저장해 두지 않으면 불가능하지만, Git을 사용하면 매 순간 변경 사항을 자동으로 추적하여 되돌릴 수 있습니다.
- ? **어떤 문제를 해결하는지?**
  - 수정 사항이 꼬이거나 사라지는 문제를 해결
  - 팀 프로젝트에서 충돌(Conflict) 없이 소스를 효율적으로 병합(Merge)
  - 안전한 백업 및 히스토리 관리

---

## 2. 어떻게 동작하나요? ?

### 2.1 기본 개념

Git은 로컬 저장소(Local Repository)와 원격 저장소(Remote Repository) 두 가지를 기본 구조로 합니다.

- **로컬 저장소**: 내 컴퓨터에 존재하는 버전 관리 공간
- **원격 저장소**: GitHub, GitLab 등 서버에 호스팅되는 저장소

버전 관리 과정은 크게 다음과 같은 단계를 거칩니다.

1) **Working Directory**: 실제 작업 중인 디렉터리(수정, 추가 등을 수행)  
2) **Staging Area**: 커밋하고 싶은 변경 내용을 임시로 모아두는 공간  
3) **Local Repository**: 최종적으로 기록을 남기는 곳(커밋)

```
# Git 기본 흐름
$ git add <파일명>  # 변경된 파일을 Staging Area에 추가
$ git commit -m "커밋 메시지"  # 변경 사항을 Local Repository에 커밋
$ git push origin main  # 원격 저장소로 푸시
```

### 2.2 실제 적용 예시

#### 예시 시나리오

- **프로젝트 초기화**

  ```
  $ git init
  ```

  - 현재 디렉터리에 `.git` 폴더가 생성되어 Git 저장소가 초기화됩니다.
- **파일 생성 및 수정**

  ```
  # 작업 디렉토리에서 파일 생성
  $ echo "Hello Git" > hello.txt
  ```
- **커밋하기**

  ```
  $ git add hello.txt           # Staging Area로 추가
  $ git commit -m "Add hello.txt file"
  ```
- **원격 저장소에 연결**

  ```
  $ git remote add origin https://github.com/username/repo.git
  $ git push -u origin main
  ```

  - 이제 원격 저장소와 연동되어, 다른 사람과도 협업이 가능합니다.

### ? 동작 원리

1. **Local에서 수정**: 로컬 환경에서 파일을 수정하고 add를 통해 변경 내용을 Stage에 올립니다.
2. **Commit으로 스냅샷 생성**: “이 시점의 변경 사항을 저장하겠다”는 의미로 커밋을 수행합니다.
3. **Push로 원격 저장소 동기화**: 원격 저장소(GitHub, GitLab 등)에 푸시하여 팀원들과 공유합니다.

---

## 3. 주요 장점 ?

1. **이력 추적과 복구 용이**: 모든 변경 사항이 커밋(Commit)으로 기록되어, 언제든지 특정 버전으로 되돌릴 수 있습니다.
2. **분산 구조**: 로컬에 모든 히스토리를 보관하기 때문에, 인터넷 연결이 없어도 버전 관리를 할 수 있고, 서버 장애에도 안전합니다.
3. **협업에 최적화**: 여러 사람이 동시에 작업해도 각자의 브랜치에서 독립적으로 진행할 수 있고, 나중에 병합(Merge) 가능합니다.

---

## 4. 주의할 점 ⚠️

1. **충돌(Conflict) 관리**: 여러 사람이 같은 부분을 수정하면 충돌이 발생할 수 있습니다. 충돌이 발생하면, Git이 스스로 해결해 주지 못하므로 수동으로 어떤 변경 사항을 살릴지 결정해야 합니다.
2. **올바른 브랜치 전략**: 프로젝트 규모가 커지면 브랜치를 어떻게 사용하고 병합할지에 대한 전략이 필요합니다(git-flow, GitHub Flow 등).
3. **커밋 메시지 작성 규칙**: 협업에서 커밋 메시지 규칙이 없으면 이력이 지저분해지고, 협업 생산성이 크게 떨어집니다.

---

## 5. 실제 사용 예시 ?

아래는 Git을 사용해 간단한 프로그래밍 프로젝트를 진행하는 간단한 예제입니다.

```
# 1. 폴더 생성 및 초기화
$ mkdir sample-project
$ cd sample-project
$ git init

# 2. 파일 생성
$ echo "print('Hello Git!')" > app.py

# 3. add 및 commit
$ git add app.py
$ git commit -m "Initial commit"

# 4. 브랜치 생성 및 이동
$ git checkout -b feature/add-logging

# 5. 로그 추가 기능 구현
echo "
import logging

logging.basicConfig(level=logging.INFO)
logging.info('Logging initiated')
" >> app.py

# 6. 변경 사항 커밋
$ git add app.py
$ git commit -m "Add logging feature"

# 7. 메인 브랜치로 병합
$ git checkout main
$ git merge feature/add-logging
```

이 과정을 통해 원하는 기능을 빠르게 개발하고, 나중에 문제가 생기면 이전 버전으로 쉽게 롤백이 가능합니다.

---

## 6. 마치며 ?

Git은 **버전 관리**와 **협업**에서 없어서는 안 될 도구입니다. 개인 프로젝트에서부터 대규모 팀 개발까지 폭넓게 활용되며, 변경 이력을 꼼꼼히 추적할 수 있어 큰 안전망이 되어 줍니다.  
여러분이 Git을 숙달하면, 어떠한 코드 변경 사항도 투명하게 관리하고 필요할 때 자유롭게 과거로 돌아갈 수 있습니다.  
"이 기술을 사용하면 **협업 생산성을 높이고, 프로젝트를 안정적으로 운영**할 수 있습니다!"

---

### 참고 자료 및 출처

- [Git 공식 문서](https://git-scm.com/)
- [Pro Git - Free Book](https://git-scm.com/book/en/v2)
- [GitHub Guides](https://guides.github.com/)

Git을 통해 더욱 안전하고 효율적인 소스 코드 관리를 경험해 보세요!
