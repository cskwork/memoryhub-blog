---
title: "cURL Practice"
date: 2024-05-25T17:47:01+09:00
slug: "74-cURL-실습"
original_url: "https://memoryhub.tistory.com/74"
tistory_id: 74
draft: false
categories: ["Dev Ops"]
tags: ["Curl"]
cover:
  image: "/images/74-cURL-실습/img.png"
  relative: false
  hidden: false
---

![](/images/74-cURL-실습/img.png)

### Network Check

```
 curl -v telnet://ip:port
```

### JSON POST REQUEST

```
curl -d '{argument={question=management, type=hybridqa}, access_key=000000-000000-000000-000000-000000}' -H 'Content-Type: application/json' http://aiopen.etri.re.kr:8000/WikiQA
```

### Access SFTP Server and Retrieve File List

```
curl -k sftp://ip:port//dirPath/path/ --user "id:pwd"
```

### Upload using curl on SFTP

```
curl  -k "sftp://83.46.38.23:22/CurlPutTest/" --user "testuser:testpassword" -T "C:\test\testfile.xml" --ftp-create-dirs
```

### Download using curl on SFTP

```
curl  -k "sftp://83.46.38.23:22/CurlPutTest/testfile.xml" --user "testuser:testpassword" -o "C:\test\testfile.xml" --ftp-create-dirs

# Directory structure is created automatically without constraints
curl  -k "sftp://83.46.38.23:22/CurlPutTest/testfile.xml" --user "testuser:testpassword" -o "C:\test\testfile.xml" --create-dirs
```

### Rename using curl on SFTP

```
curl  -k "sftp://83.46.38.23:22/CurlPutTest/" --user "testuser:testpassword" -Q "-RENAME
  '/CurlPutTest/testfile.xml'  '/CurlPutTest/testfile.xml.tmp'"   --ftp-create-dirs
```

### Delete using curl on SFTP

```
curl  -k "sftp://83.46.38.23:22/CurlPutTest/ " --user "testuser:testpassword" -Q "–RM /CurlPutTest/testfile.xml" --ftp-create-dirs
```

### Make directory using curl on SFTP

```
curl  -k "sftp://83.46.38.23:22/CurlPutTest/test " --user "testuser:testpassword" -Q "–MKDIR /CurlPutTest/Test" --ftp-create-dirs
```

### Remove directory using curl on SFTP

```
curl  -k "sftp://83.46.38.23:22/CurlPutTest/test " --user "testuser:testpassword" -Q "–RMDIR /CurlPutTest/Test" --ftp-create-dirs
```

### For Multi-line Commands

```
# Use \ for multi-line commands
curl  -k "sftp://ip:port/lookupPath/file.UTF-8" --user "username:pwd" \
-o "C:/downloadPath/file.UTF-8" --ftp-create-dirs
```

While multi-line commands can be entered in Putty and executed, if an sh file is edited on Windows and uploaded, it may not work. A common error is  
'\r': command not found  
In that case, open it with gitbash to convert it:

```
# Convert from DOS to UNIX format
# REPLACE
dos2unix run.sh    

# NEW
dos2unix -n input.txt output.txt
dos2unix --newfile input.txt output.txt

# UNIX TO DOS
unix2dos myfile.txt
```

### Result

![](/images/74-cURL-実習/img_1.png)

### REF

<http://www.mukeshkumar.net/articles/curl/how-to-use-curl-command-line-tool-with-ftp-and-sftp>  
<https://www.cyberciti.biz/faq/howto-unix-linux-convert-dos-newlines-cr-lf-unix-text-format/>
