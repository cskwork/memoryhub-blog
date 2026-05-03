---
title: "Firewalld Port Configuration Method"
date: 2024-05-25T13:39:44+09:00
slug: "47-Firwalld-포트-구성-방법"
original_url: "https://memoryhub.tistory.com/47"
tistory_id: 47
draft: false
categories: ["Dev Ops"]
tags: ["Linux"]
---

### **How to Configure Ports in Firewalld**

### **Opening Ports**

- **Command**: To open a port in **firewalld**, use the following command:

  ```
  sudo firewall-cmd --add-port={port_number}/tcp --permanent # The --permanent option applies the firewall rule permanently.
  ```
- **Example**: Open multiple ports commonly used by various applications:

  ```
  sudo firewall-cmd --add-port=8080/tcp --permanent  # Common alternative HTTP port
  sudo firewall-cmd --add-port=3306/tcp --permanent  # MySQL/MariaDB
  sudo firewall-cmd --add-port=1521/tcp --permanent  # Oracle
  ... (continue opening other ports)

  sudo firewall-cmd --add-port={8080/tcp,3306/tcp,1521/tcp} --permanent # Add multiple ports at once
  sudo firewall-cmd --reload  # Apply changes and enable new rules without restarting firewalld.
  ```
- **Verification**: To verify that the port is open:

  ```
  firewall-cmd --list-ports
  ```

### **Common Ports and Their Uses**

- **HTTP and Alternative Ports**: Ports 80 and 8080 are for HTTP services.
- **Database Services**:
  - 3306/tcp: MySQL or MariaDB database server
  - 1521/tcp: Oracle database server
  - 6379/tcp: Redis key-value storage service
- **Other Applications**:
  - 5555: Used for various network services.
  - 4444: Frequently used in web applications or development environments.

### **Actual Application Testing**

### **Example URLs and IPs for Connection Testing**

- **Security Caution**: Manage test URLs and IPs so they're not exposed to the internet. After testing is complete, appropriately reset or modify firewall rules.

### **Key References**

- [10 Useful firewall-cmd Commands](https://www.blogger.com/blog/post/edit/3936409365620457385/4787240825984491686#)
- [Firewalld Official Documentation](https://www.blogger.com/blog/post/edit/3936409365620457385/4787240825984491686#)
- [Using Firewalld on Red Hat Enterprise Linux](https://www.blogger.com/blog/post/edit/3936409365620457385/4787240825984491686#)
