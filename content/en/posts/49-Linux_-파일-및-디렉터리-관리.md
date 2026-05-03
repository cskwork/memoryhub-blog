---
title: "Linux: File and Directory Management"
date: 2024-05-25T14:01:12+09:00
slug: "49-Linux_-파일-및-디렉터리-관리"
original_url: "https://memoryhub.tistory.com/49"
tistory_id: 49
draft: false
---

Explains how to find files by specific extension, search for strings in files, combine and sort files, change file and directory permissions, and copy directories.

### Finding Files by Specific Extension

Basic file search:

```
find -name '*.zip'
```

This command searches the entire system for files with a .zip extension.

### Searching for Strings in Files

```
find . -name "*" | xargs grep -n "count"
```

This command searches for the string "count" in all files in the current directory and subdirectories, and prints the line numbers containing that string.

### Combining and Sorting Files

Combining multiple files:

```
cat 1.txt 2.txt 3.txt > 0.txt
```

Combines three text files into 0.txt, using shell redirection (>) to send output to that file.

Combining and sorting files:

```
cat file1 file2 | sort > file3; cat file3
```

Combines file1 and file2, sorts them alphabetically, saves the result to file3. Then prints the contents of file3.

### Changing File and Directory Permissions

Permission setting commands:

```
chmod u+r secure  # Add read permission for owner
chmod ugo-wx secure  # Remove write and execute permissions for all users
chmod ugo+x secure  # Add execute permission for all users
chmod ugo=x secure  # Remove all permissions and grant only execute permission to all users
```

These commands explain how to grant or remove read, write, and execute permissions for specific users or groups.

### Copying Directories

Copy entire directory:

```
mkdir NPKI_BAKTEST
cp -a /usr/local/NPKI/ /usr/local/NPKI_BAKTEST/
# Or
cp -a ~/NPKI/ ~/NPKI_BAKTEST/
```

Creates a new directory and copies the original directory to the new location entirely. The -a option copies while maintaining all file attributes.

### Additional Network Commands Explanation

Network port checking and routing information:

```
netstat -ano | findstr :8080
netstat -nr
```

- The first command shows all network connections using port 8080.
- The second command shows the routing table, used to verify the destination path of network packets.

### References

[Linux find command usage](https://www.blogger.com/blog/post/edit/3936409365620457385/256083815681487595#)
