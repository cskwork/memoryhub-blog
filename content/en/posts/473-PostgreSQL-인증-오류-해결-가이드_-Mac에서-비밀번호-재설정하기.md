---
title: "PostgreSQL Authentication Error Resolution Guide: Password Reset on Mac"
date: 2025-03-15T15:13:42+09:00
slug: "473-PostgreSQL-인증-오류-해결-가이드_-Mac에서-비밀번호-재설정하기"
original_url: "https://memoryhub.tistory.com/473"
tistory_id: 473
draft: false
categories: ["Dev Database"]
tags: ["PostgreSQL"]
---

## Problem Introduction

Have you ever encountered this error message when using PostgreSQL on Mac?

```
connection failed: connection to server at "127.0.0.1", port 5432 failed: FATAL: password authentication failed for user "postgres"
```

Sometimes this error occurs even when you've entered the correct password. It's especially common when using GUI tools like pgAdmin. In this article, let's understand the cause and solution step by step.

## Cause of the Error

Main causes of PostgreSQL authentication errors are:

1. Forgot password or incorrect initial setup
2. PostgreSQL authentication method (scram-sha-256, md5, etc.) doesn't match client configuration
3. pg_hba.conf file has incorrect authentication settings
4. Multiple PostgreSQL instances installed causing confusion

## Verify Your Environment

First, check which version of PostgreSQL is installed and where:

```
which postgres
postgres --version
```

These commands show the location and version of PostgreSQL executable. For example:

```
/Library/PostgreSQL/17/bin/postgres
postgres (PostgreSQL) 17.4
```

## Check PostgreSQL Process

Verify if PostgreSQL is running:

```
ps aux | grep postgres
```

If it's running, multiple processes will be displayed:

```
postgres   13208   0.0  0.1 411076016  21456   ??  Ss    2:55PM   0:00.07 /Library/PostgreSQL/17/bin/postgres -D /Library/PostgreSQL/17/data
postgres   13209   0.0  0.0 410929280   2448   ??  Ss    2:55PM   0:00.00 postgres: logger
...
```

## Solution: Reset PostgreSQL Password

### Step 1: Modify pg_hba.conf File

Change PostgreSQL's authentication settings to temporarily allow passwordless access:

```
sudo nano /Library/PostgreSQL/17/data/pg_hba.conf
```

Find the following settings in the file:

```
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
```

Temporarily change to 'trust' authentication:

```
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust
```

### Step 2: Reload PostgreSQL Configuration

Apply configuration changes:

```
sudo -u postgres /Library/PostgreSQL/17/bin/pg_ctl reload -D /Library/PostgreSQL/17/data
```

### Step 3: Connect Without Password and Set New Password

Now you can connect without password:

```
/Library/PostgreSQL/17/bin/psql -U postgres -h 127.0.0.1
```

After connecting, change the password:

```
ALTER USER postgres WITH PASSWORD 'new_password';
\q
```

### Step 4: Restore Security Settings

Open pg_hba.conf file again and change authentication method back to 'scram-sha-256':

```
sudo nano /Library/PostgreSQL/17/data/pg_hba.conf
```

Edit as follows:

```
# IPv4 local connections:
host    all             all             127.0.0.1/32            scram-sha-256
# IPv6 local connections:
host    all             all             ::1/128                 scram-sha-256
```

### Step 5: Reload Configuration and Verify

```
sudo -u postgres /Library/PostgreSQL/17/bin/pg_ctl reload -D /Library/PostgreSQL/17/data
```

Verify connection with new password:

```
/Library/PostgreSQL/17/bin/psql -U postgres -h 127.0.0.1
```

## Alternative Method: Direct Access as Postgres User

If the above method fails, you can try switching to the postgres system user:

```
sudo su - postgres
/Library/PostgreSQL/17/bin/pg_ctl stop -D /Library/PostgreSQL/17/data
/Library/PostgreSQL/17/bin/postgres --single -D /Library/PostgreSQL/17/data postgres
```

Change password at the prompt:

```
ALTER USER postgres WITH PASSWORD 'new_password';
```

Exit with Ctrl+D then restart the server:

```
/Library/PostgreSQL/17/bin/pg_ctl start -D /Library/PostgreSQL/17/data
```

## Good to Know

1. **Security Caution**: Use 'trust' authentication only temporarily. You must immediately return to the original authentication method after resetting the password.
2. **PostgreSQL 17 Default Authentication Method**: PostgreSQL 17 uses scram-sha-256 authentication by default. This is more secure but may have compatibility issues with some older clients.
3. **pgAdmin Connection Settings**: When connecting in pgAdmin, use the correct hostname (127.0.0.1 or localhost), port (5432), and username (postgres).
4. **Multiple PostgreSQL Instances**: If multiple versions of PostgreSQL are installed on your system, verify you're connecting to the desired instance.
5. **Check Logs**: If problems persist, check log files in the `/Library/PostgreSQL/17/data/log/` directory to understand detailed error messages.

## Conclusion

PostgreSQL password authentication errors are common, but can be easily resolved by following appropriate steps. I hope this guide helps you resolve your PostgreSQL connection issues. If you have additional questions or feedback, please leave a comment!

---

References:

- [PostgreSQL Official Documentation: Client Authentication](https://www.postgresql.org/docs/current/client-authentication.html)
- [PostgreSQL 17 Release Notes](https://www.postgresql.org/docs/17/release-17.html)
