---
title: "Linux: 파일 및 디렉터리 관리"
date: 2024-05-25T14:01:12+09:00
slug: "49-Linux_-파일-및-디렉터리-관리"
original_url: "https://memoryhub.tistory.com/49"
tistory_id: 49
draft: false
categories: ["데브 옵스"]
tags: ["Linux"]
---

특정 확장자로 파일을 찾고, 파일 내 문자열을 검색하며, 파일을 합치고 정렬하고, 파일 및 디렉터리 권한을 변경하고, 디렉터리를 복사하는 방법을 설명합니다.

### 특정 확장자로 파일 찾기

기본 파일 검색:

```
find -name '*.zip'
```

이 명령어는 시스템 전체에서 .zip 확장자를 가진 파일을 검색합니다.

### 파일 내 문자열 검색

```
find . -name "*" | xargs grep -n "count"
```

이 명령어는 현재 디렉터리 및 하위 디렉터리의 모든 파일에서 "count"라는 문자열을 검색하고, 해당 문자열이 포함된 줄의 번호를 출력합니다.

### 파일 합치기 및 정렬

여러 파일 합치기:

```
cat 1.txt 2.txt 3.txt > 0.txt
```

세 개의 텍스트 파일을 0.txt로 합치며, 쉘 리다이렉션(>)을 사용하여 출력을 해당 파일로 보냅니다.

파일 합치기 및 정렬:

```
cat file1 file2 | sort > file3; cat file3
```

file1과 file2를 합치고 알파벳 순으로 정렬한 후, 결과를 file3에 저장합니다. 그리고 file3의 내용을 출력합니다.

### 파일 및 디렉터리 권한 변경

권한 설정 명령어:

```
chmod u+r secure  # 소유자에게 읽기 권한 추가
chmod ugo-wx secure  # 모든 사용자의 쓰기 및 실행 권한 제거
chmod ugo+x secure  # 모든 사용자에게 실행 권한 추가
chmod ugo=x secure  # 모든 사용자의 권한을 제거하고 실행 권한만 부여
```

이 명령어들은 읽기, 쓰기, 실행 권한을 특정 사용자 또는 그룹에게 부여하거나 제거하는 방법을 설명합니다.

### 디렉터리 복사

디렉터리 전체 복사:

```
mkdir NPKI_BAKTEST
cp -a /usr/local/NPKI/ /usr/local/NPKI_BAKTEST/
# 또는
cp -a ~/NPKI/ ~/NPKI_BAKTEST/
```

새 디렉터리를 생성하고, 원본 디렉터리를 새 위치로 전체 복사합니다. -a 옵션은 모든 파일 속성을 유지하면서 복사합니다.

### 네트워크 명령어 추가 설명

네트워크 포트 검사 및 라우팅 정보:

```
netstat -ano | findstr :8080
netstat -nr
```

- 첫 번째 명령어는 8080 포트를 사용하는 모든 네트워크 연결을 보여줍니다.
- 두 번째 명령어는 라우팅 테이블을 보여주며, 네트워크 패킷의 목적지 경로를 확인하는 데 사용됩니다.

### 참고

[리눅스 find 명령어 사용법](https://www.blogger.com/blog/post/edit/3936409365620457385/256083815681487595#)
