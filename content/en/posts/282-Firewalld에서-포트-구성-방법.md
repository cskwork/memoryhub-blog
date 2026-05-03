---
title: "How to Configure Ports in Firewalld"
date: 2024-06-12T08:43:43+09:00
slug: "282-Firewalld에서-포트-구성-방법"
original_url: "https://memoryhub.tistory.com/282"
tistory_id: 282
draft: false
---

### **Opening Ports**

- **Command**: To open a port in **`firewalld`**, use the following command:
  - ```
    sudo firewall-cmd --add-port={port_number}/tcp --permanent # The --permanent option applies the firewall rule permanently.
    ```
- **Example**: Opening multiple commonly used ports in various applications:
  - ```
    sudo firewall-cmd --add-port=8080/tcp --permanent # Common alternative HTTP port
    sudo firewall-cmd --add-port=3306/tcp --permanent # MySQL/MariaDB
    sudo firewall-cmd --add-port=1521/tcp --permanent # Oracle
    # Continue opening other ports
    sudo firewall-cmd --add-port={8080/tcp,3306/tcp,1521/tcp} --permanent # Add multiple ports at once
    sudo firewall-cmd --reload # Apply changes and activate new rules without restarting firewalld.
    ```
- **Verification**: To confirm that ports are open:
  - ```
    firewall-cmd --list-ports
    ```

### **Common Ports and Their Uses**

- **HTTP and Alternative Ports**: Ports 80 and 8080 are for HTTP services.
- **Database Services**:
  - 3306/tcp: MySQL or MariaDB database server
  - 1521/tcp: Oracle database server
  - 6379/tcp: Redis key-value store service
- **Other Applications**:
  - 5555: Used for various network services.
  - 4444: Frequently used in web applications or development environments.

### **Practical Application Testing**

### **Example URLs and IPs for Connection Testing**

- **Security Notice**: Manage test URLs and IPs so they're not exposed on the internet. After testing is complete, appropriately reset or modify firewall rules.
  - **DB Test**: **`http://127.0.0.1:8082/app`**
  - **App Test**: **`http://127.0.0.1:13120/app2`**
  - **Oracle Connection**: When connecting to databases like Oracle, be careful to log in as **`sys dba`**.

### **Key References**

- [10 Useful firewall-cmd Commands](https://www.linuxcloudvps.com/blog/10-useful-firewall-cmd-commands-in-linux/)
- [Firewalld Official Documentation](https://firewalld.org/documentation/)
- [Using Firewalld in Red Hat Enterprise Linux](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/security_guide/sec-using_firewalls)
