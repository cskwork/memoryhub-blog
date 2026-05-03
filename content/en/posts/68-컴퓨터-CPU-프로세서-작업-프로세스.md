---
title: "Computer CPU (Processor) Task Process"
date: 2024-05-25T14:53:35+09:00
slug: "68-컴퓨터-CPU-프로세서-작업-프로세스"
original_url: "https://memoryhub.tistory.com/68"
tistory_id: 68
draft: false
categories: ["Dev Concepts"]
tags: ["Info Processing Cert"]
cover:
  image: "/images/68-컴퓨터-CPU-프로세서-작업-프로세스/img.png"
  relative: false
  hidden: false
---

## Computer CPU (Processor) Task Process

A program processed by the processor (CPU).  
Also called a task or job.

### Process State Transition

The state change that occurs while a process is in the system.

### PCB (Process Control Block)

- HAS address, state, time, id

![](/images/68-컴퓨터-CPU-프로세서-작업-프로세스/img.png)

### Process State Transition

![](/images/68-컴퓨터-CPU-프로세서-작업-프로세스/img_1.png)

- Submitted: State where a job is submitted to the system
- Accepted: State where a submitted job is stored on disk
- Ready: State where the process is waiting before being allocated to the processor. Job scheduler transitions from accepted to ready state.
- Running: State where the process is running with processor allocated.
- Waiting: If input/output is required for the process, the currently running process is suspended and waits until the input/output is complete.
- Terminated: State where the process execution is complete and the process allocation is released.

#### Windows

- Managed through Task Manager, priority assignment possible

#### Linux

- Confirmed with ps command and can be checked by moving to the directory corresponding to PID in the proc directory (virtual directory where data stored in RAM can be verified)
- Current system CPU and RAM usage can be monitored with top command.
- Process can be terminated with kill command.

### References

- 2020 Sina Gong Information Processing Engineer Practical Basics
