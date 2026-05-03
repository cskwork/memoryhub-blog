---
title: "Java Native Memory Tracking (JCMD) Memory Monitoring Tool"
date: 2024-05-25T14:01:34+09:00
slug: "50-Java-Native-Memory-Tracking-JCMD-메모리-모니터링-툴"
original_url: "https://memoryhub.tistory.com/50"
tistory_id: 50
draft: false
categories: ["Dev Language"]
tags: ["Java"]
---

Today, we'll learn how to more efficiently monitor JVM environments using the **JCMD** tool. JCMD is a powerful command-line tool provided since Oracle Java 7, enabling easy inspection and management of JVM application process information, heap dumps, thread dumps, VM system information, and GC statistics.

## **1. What is JCMD?**

JCMD is basically a **"Swiss Army knife for JVM monitoring"** tool. You can identify Java processes, generate heap dumps, check thread states, and obtain various analysis information.

- **Concept Summary**:
  - Easily check JVM process IDs, heap dumps, thread dumps, VM system information, GC statistics, etc. from command line
  - Available from Oracle Java 7 version onwards
  - Useful for Java application performance tuning and problem solving
- **Real-world Example**:
  - When a running Tomcat server suddenly runs out of memory or experiences high CPU usage, you can immediately use jcmd command to identify which process has issues and instantly dump heap or thread-related information to analyze the cause.
- **What problems does it solve?**
  - It helps quickly identify various JVM-related performance issues, from process identification to memory leaks, thread deadlocks, and abnormal GC behavior.

## **2. How Does It Work?**

### 1) Basic Concepts

JCMD's work can be summarized as follows:

- **Process Identification**: Check currently running Java process list
- **Command Execution**: Execute various commands like VM.native_memory, GC.heap_dump, Thread.print for specific processes
- **Provide Analysis Results**: Monitor and diagnose problems by checking command results in real-time

```
# Identify Java processes
$ jcmd
1234 org.apache.catalina.startup.Bootstrap
5678 com.example.MyApplication

# Detailed Java process list check
$ jcmd -l
1234 org.apache.catalina.startup.Bootstrap /usr/local/tomcat/...
5678 com.example.MyApplication /usr/local/app/...
```

### 2) Practical Application Examples

#### Example: Tomcat Server Monitoring

1. **Start Tomcat Server**
   - Assume Tomcat is running normally. (Example: PID=1234)
2. **Check Process Information**

   ```
   $ jcmd -l
   1234 org.apache.catalina.startup.Bootstrap /usr/local/tomcat/bin/bootstrap.jar
   ```
3. **Check Thread Dump and Other Needed Information**

   ```
   $ jcmd 1234 Thread.print
   # Print thread stack trace
   ```
4. **Generate GC Heap Dump**

   ```
   $ jcmd 1234 GC.heap_dump /path/to/dump.hprof
   # Create JVM heap dump file
   ```

### 3) How It Works

1. **Command Issuance Phase**: Pass specific commands to JVM process in the form jcmd <pid> <command>.
2. **JVM Internal Processing**: The JVM of the corresponding process interprets the command and collects heap/thread dumps, GC statistics as needed.
3. **Return Results**: Print collected information to console or save as files (e.g., heap dump).

## **3. Key Advantages**

1. **Comprehensive Feature Set**: Provides various commands including process identification, thread dump, heap dump, GC information, native memory tracking in one tool.
2. **Intuitive Command Usage**: Intuitive command format enables quick diagnosis and monitoring of JVM-related issues.
3. **Native Memory Tracking (NMT) Support**: Can track native memory areas, enabling identification of complex issues like memory leaks.

## **4. Important Notes ⚠️**

1. **Production Environment Impact**: Thread dump or heap dump can momentarily affect application performance, so it's best to use them during low-traffic hours or after prior notice.
2. **Security Issues**: Since internal structure and memory information can be viewed in detail, access control is important.
3. **File Path and Permissions**: When exporting heap dump as files, ensure the JVM process has access permissions to the directory.

## **5. Native Memory Tracking (NMT) Usage Example**

Native Memory Tracking (NMT) **tracks native memory used within the JVM**, helping diagnose memory leaks that can occur outside Java Heap areas.

### 1) Configuration Method

1. **Add JVM Option**
   - Enable with -XX:NativeMemoryTracking=summary or -XX:NativeMemoryTracking=detail option
2. **Tomcat Example**
   - Add to CATALINA_OPTS or JAVA_OPTS as follows:

   ```
   # Linux (setenv.sh)
   export CATALINA_OPTS="$CATALINA_OPTS -XX:NativeMemoryTracking=summary"
   ```

   - Similar configuration for Windows (setenv.bat):

   ```
   set CATALINA_OPTS=%CATALINA_OPTS% -XX:NativeMemoryTracking=summary
   ```
3. **Restart Server**
   - Tomcat server must be restarted after modifying configuration files.

### 2) Baseline Setting and Monitoring

#### (1) Initial Baseline Setup

Measuring the **initial memory state** in development/production environments makes comparative analysis easier when changes occur.

```
# Assume Tomcat process PID is 1234
$ jcmd 1234 VM.native_memory baseline
```

#### (2) Memory Change Monitoring

Running the following command later shows which areas have increased/decreased memory compared to baseline:

```
$ jcmd 1234 VM.native_memory detail.diff
```

- **"+" symbol** indicates memory increase
- **"-" symbol** indicates memory decrease

### 3) NMT Report Key Items

1. **Total Memory (Reserved/Committed)**:
   - Memory reserved from operating system and actually in use by JVM
2. **Java Heap**:
   - Memory area where Java objects are stored
3. **Class**:
   - Memory used by class loading and metadata
4. **Thread**:
   - Memory used by native stacks and structures per thread
5. **Code**:
   - Memory occupied by machine code generated through JIT compilation

Below is a simplified example of detail.diff report:

```
Native Memory Tracking:

Total: reserved=1234KB, committed=567KB
                ...
Class: reserved=200KB (+20KB), committed=150KB (+10KB)
Thread: reserved=300KB (-10KB), committed=250KB (+5KB)
Code: reserved=180KB (+30KB), committed=120KB (+15KB)
```

- Class section shows +20KB / +10KB increase, suggesting possible memory growth due to class loading.
- Thread shows reduced reserved memory but slight increase in committed memory.

## **6. Conclusion**

JCMD is a **very useful tool** for diagnosing and monitoring JVM process status. Particularly through **Native Memory Tracking (NMT)** features, you can track memory leaks in native memory areas beyond Java Heap, greatly helping resolve complex memory issues. When application performance problems occur in production environments, actively use JCMD and NMT reports! This enables you to **quickly identify process memory usage and GC status**, easily resolving **memory leaks, thread issues**, and more.

---

### **References and Sources**

- [Oracle Official Documentation - Java Native Memory Tracking](https://docs.oracle.com/javase/8/docs/technotes/guides/troubleshoot/nmt-summary.html)
- [Oracle Official Documentation - JCMD Usage Guide](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jcmd.html)

Referring to the above resources enables you to **learn JCMD and NMT more deeply** and perform effective monitoring and problem-solving in actual production environments.
