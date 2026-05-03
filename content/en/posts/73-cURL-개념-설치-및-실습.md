---
title: "cURL Concepts, Installation, and Hands-on"
date: 2024-05-25T17:46:02+09:00
slug: "73-cURL-개념-설치-및-실습"
original_url: "https://memoryhub.tistory.com/73"
tistory_id: 73
draft: false
---

## Concepts

**Definition**: cURL (client, URL)

- Client-side program and URL client Request LIB.
- Client program + URL program
- A program that uses URL to download files/data to a client PC
- Uses libcurl library. C API.
- Windows command-line based tool
- Open source
- Developed by Daniel Stenberg with 2500+ developers individually participating and contributing

## Installation

### Linux

```
# Ubuntu, Debian
apt install curl
apt install libcurl4-openssl-dev
# Redhat, CentOS
yum install curl
yum install libcurl-devel
```

### Windows

<https://curl.se/windows/>

### Client-Server Communication Process

1. **Client**
2. URL contains the **host address** to find
3. DNS server converts the address in the name to an IP address
4. Establish connection with **TCP**
5. Choose which connection channel (port) to use (default is 80)
6. After connection and transfer channel are complete, establish trust through TLS (Transport Layer Security) **handshake** for secure communication. Communication begins after TLS handshake is complete
7. Communication proceeds through a set language and format called a **protocol** (HTTP, HTTPS, POP3, TELNET, SMTP, FTP, etc. ++)

## Hands-on

### curl website

```
# -v = verbose
curl -v http://example.com

# Order of options doesn't matter
curl -vL http://example.com
curl http://example.com -Lv
curl -v -L http://example.com

# For long option names, you must use two minus signs --
curl --verbose http://example.com
curl --verbose --location http://example.com
curl --data arbitrary http://example.com

# Remove options using no-
curl --no-verbose http://example.com
```

![](/images/73-cURL-개념-설치-및-실습/img.png)

### Sending Arguments

```
curl -A "I am your father" http://example.com
# Send double quotes
curl -d '{ "name": "Darth" }' http://example.com
```

### SFTP Upload

```
curl sftp://example.com/file.zip -u user
curl sftp://example.com/ -u user
# Authentication
curl -u john:RHvxC6wUA -O scp://ssh.example.com/file.tar.gz
```

![](/images/73-cURL-개념-설치-및-실습/img_1.png)

## Reference

<https://everything.curl.dev/cmdline/urls>  
// Complete collection of curl options  
<https://gist.github.com/eneko/dc2d8edd9a4b25c5b0725dd123f98b10>
