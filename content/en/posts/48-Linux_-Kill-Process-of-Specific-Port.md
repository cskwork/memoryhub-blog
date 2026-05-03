---
title: "Linux: Kill Process of Specific Port"
date: 2024-05-25T13:40:13+09:00
slug: "48-Linux_-Kill-Process-of-Specific-Port"
original_url: "https://memoryhub.tistory.com/48"
tistory_id: 48
draft: false
categories: ["Dev Ops"]
tags: ["Linux"]
---

Checking active listening ports and killing a process on a specific port.

### **Checking Active Listening Ports**

#### 1. List Listening Ports

To find out which ports are currently open and listening for incoming connections, the lsof command is highly useful. This command lists open files and the corresponding processes. Here's how you use it to filter for listening ports:

```
sudo lsof -i -P -n | grep LISTEN
```

- i: Selects the listing of files whose Internet address matches the specified address.
- P: Inhibits the conversion of port numbers to port names for network files. It shows port numbers instead of names.
- n: Inhibits the conversion of network numbers to host names for network files. It shows IP addresses instead of host names.
- grep LISTEN: Filters results to only show listening ports.

This command provides a snapshot of all applications on your system that are listening for incoming connections.

### **Killing a Process on a Specific Port**

#### 1. Kill Process Using a Port

Occasionally, you may need to terminate a process that is using a specific port. This can be necessary for troubleshooting or restarting a service that is not responding correctly. Here's how to kill a process using port 8000 as an example:

```
sudo kill -9 $(sudo lsof -t -i:8000) # Kill processes on port 8000
```

- sudo lsof -t -i:8000: Finds the process ID (PID) using port 8000. The t option returns the PID without headers.
- sudo kill -9: Forcefully stops the process using signal 9 (SIGKILL). It should be used cautiously as it does not allow for clean-up operations by the process.

**Best Practice Caution:** Using kill -9 (SIGKILL) should be a last resort as it can lead to data corruption or incomplete transactions, particularly in database or file-handling applications. If possible, first try more graceful signals like SIGTERM (signal 15), which allows processes to clean up before exiting:

```
sudo kill -15 $(sudo lsof -t -i:8000)
```

If the process does not terminate after a reasonable time, then consider escalating to kill -9.
