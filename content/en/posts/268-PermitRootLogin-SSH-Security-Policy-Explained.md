---
title: "PermitRootLogin SSH Security Policy Explained"
date: 2024-06-11T17:07:23+09:00
slug: "268-PermitRootLogin-SSH-Security-Policy-Explained"
original_url: "https://memoryhub.tistory.com/268"
tistory_id: 268
draft: false
categories: ["Dev Ops"]
tags: ["Linux"]
---

*The warning indicates that the `PermitRootLogin` directive in the SSH configuration file (`/etc/ssh/sshd_config`) is not explicitly set, which can lead to security vulnerabilities.*

### The Big Picture

Think of `PermitRootLogin` as a security policy for your building (EC2 instance). It determines whether the building's master key (root login) can be used to enter. Not setting this policy leaves the rules unclear, potentially allowing unauthorized access.

### Core Concepts

1. **SSH Configuration File**: The file where SSH server settings are configured.
2. **PermitRootLogin Directive**: Controls if and how the root user can log in via SSH.
3. **Security Implications**: The importance of explicitly setting this directive.

### Detailed Walkthrough

#### Understanding PermitRootLogin

- **Directive**: `PermitRootLogin` specifies if the root user is allowed to log in via SSH. The possible values are:
  - `prohibit-password`: Root login is allowed only with public key authentication.
  - `yes`: Root login is allowed with password or public key.
  - `without-password`: Root login is allowed only with public key (same as `prohibit-password`).
  - `no`: Root login is not allowed.

#### The Warning Explained

- **Commented Out**: The `PermitRootLogin` line in `/etc/ssh/sshd_config` is either commented out or missing. This means the default behavior of the SSH server is used.
- **Default Behavior**: Depending on the SSH server version, the default might allow or disallow root login, potentially posing a security risk.

### Fixing the Warning

#### Step 1: Open the SSH Configuration File

1. **Edit the SSH configuration file**:

```
sudo nano /etc/ssh/sshd_config
```

#### Step 2: Set PermitRootLogin

2. **Uncomment or add the `PermitRootLogin` directive**. For example, to allow root login only with public key authentication:

```
PermitRootLogin prohibit-password
```

#### Step 3: Save and Restart SSH Service

3. **Save the file and exit the editor**.
4. **Restart the SSH service to apply the changes**:

```
sudo systemctl restart sshd
```

### Understanding Through an Example

Imagine you have an EC2 instance and you want to ensure root access is secure:

1. **Open `/etc/ssh/sshd_config`**: This is like reviewing the security policy for building access.
2. **Set `PermitRootLogin prohibit-password`**: This is like specifying that the master key can only be used with additional security measures (public key).
3. **Restart SSH service**: This ensures the new policy is enforced.

### Conclusion and Summary

The warning about `PermitRootLogin` not being set indicates a potential security oversight. To address it, explicitly set `PermitRootLogin` in `/etc/ssh/sshd_config` to ensure root login is controlled and secure. This helps protect your instance from unauthorized access.

### Test Your Understanding

1. What does `PermitRootLogin prohibit-password` do?
2. How can you edit the SSH configuration file to change the `PermitRootLogin` setting?
3. Why is it important to restart the SSH service after making changes to its configuration?

### Reference

For more information on SSH configuration and security best practices, refer to the official [OpenSSH documentation](https://www.openssh.com/manual.html).
