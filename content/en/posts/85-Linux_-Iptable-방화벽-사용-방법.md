---
title: "Linux: How to Use Iptables Firewall"
date: 2024-05-25T17:59:15+09:00
slug: "85-Linux_-Iptable-방화벽-사용-방법"
original_url: "https://memoryhub.tistory.com/85"
tistory_id: 85
draft: false
---

Location: cat /etc/sysconfig/iptables

## Firewall auto-initialization basic script 1

```
#! /bin/bash
iptables -F
iptables -X

echo Allow SSH
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

echo Allow HTTP and HTTPS
iptables -A INPUT -p tcp --dport 80 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

echo Allow POP, IMAP and SMTP
iptables -A INPUT -p tcp --dport 25 -j ACCEPT
iptables -A INPUT -p tcp --dport 465 -j ACCEPT
iptables -A INPUT -p tcp --dport 143 -j ACCEPT
iptables -A INPUT -p tcp --dport 993 -j ACCEPT
iptables -A INPUT -p tcp --dport 587 -j ACCEPT
iptables -A INPUT -p tcp --dport 110 -j ACCEPT
iptables -A INPUT -p tcp --dport 995 -j ACCEPT

echo Allow ICMP
iptables -A INPUT -p icmp -j ACCEPT

echo Allow localhost
iptables -A INPUT -s 127.0.0.1 -j ACCEPT

echo Maintain existing connections
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -m state --state NEW,RELATED,ESTABLISHED -j ACCEPT

echo Reject other traffic
iptables -A INPUT -j REJECT
iptables -A FORWARD -j REJECT

# Save the configuration /sbin/service
iptables save

# Output the configured content
iptables -L -v
```

## Firewall auto-initialization basic script 2

```
#!/bin/bash
# Iptables configuration automation script

# Modify according to your needs
iptables -F
# Allow TCP port 22 for SSH access

# Configure first for remote access
iptables -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT

# Set default policies
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow localhost access
iptables -A INPUT -i lo -j ACCEPT

# Allow established and related connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow Apache port 80
iptables -A INPUT -p tcp --dport 80 -j ACCEPT

# Save the configuration /sbin/service
iptables save

# Output the configured content
iptables -L -v
```

## Firewall auto-initialization advanced script

```
#!/bin/bash
# A sample firewall shell script
IPT="/sbin/iptables"
SPAMLIST="blockedip"
SPAMDROPMSG="BLOCKED IP DROP"
SYSCTL="/sbin/sysctl"
BLOCKEDIPS="/root/scripts/blocked.ips.txt"

# Stop certain attacks
echo "Setting sysctl IPv4 settings..."
$SYSCTL net.ipv4.ip_forward=0
$SYSCTL net.ipv4.conf.all.send_redirects=0
$SYSCTL net.ipv4.conf.default.send_redirects=0
$SYSCTL net.ipv4.conf.all.accept_source_route=0
$SYSCTL net.ipv4.conf.all.accept_redirects=0
$SYSCTL net.ipv4.conf.all.secure_redirects=0
$SYSCTL net.ipv4.conf.all.log_martians=1
$SYSCTL net.ipv4.conf.default.accept_source_route=0
$SYSCTL net.ipv4.conf.default.accept_redirects=0
$SYSCTL net.ipv4.conf.default.secure_redirects=0
$SYSCTL net.ipv4.icmp_echo_ignore_broadcasts=1
#$SYSCTL net.ipv4.icmp_ignore_bogus_error_messages=1
$SYSCTL net.ipv4.tcp_syncookies=1
$SYSCTL net.ipv4.conf.all.rp_filter=1
$SYSCTL net.ipv4.conf.default.rp_filter=1
$SYSCTL kernel.exec-shield=1
$SYSCTL kernel.randomize_va_space=1

echo "Starting IPv4 Firewall..."
$IPT -F
$IPT -X
$IPT -t nat -F
$IPT -t nat -X
$IPT -t mangle -F
$IPT -t mangle -X

# load modules
modprobe ip_conntrack

[ -f "$BLOCKEDIPS" ] && BADIPS=$(egrep -v -E "^#|^$" "${BLOCKEDIPS}")

# interface connected to the Internet
PUB_IF="eth0"

#Unlimited traffic for loopback
$IPT -A INPUT -i lo -j ACCEPT
$IPT -A OUTPUT -o lo -j ACCEPT

# DROP all incomming traffic
$IPT -P INPUT DROP
$IPT -P OUTPUT DROP
$IPT -P FORWARD DROP

if [ -f "${BLOCKEDIPS}" ];
then
# create a new iptables list
$IPT -N $SPAMLIST

for ipblock in $BADIPS
do
   $IPT -A $SPAMLIST -s $ipblock -j LOG --log-prefix "$SPAMDROPMSG "
   $IPT -A $SPAMLIST -s $ipblock -j DROP
done

$IPT -I INPUT -j $SPAMLIST
$IPT -I OUTPUT -j $SPAMLIST
$IPT -I FORWARD -j $SPAMLIST
fi

# Block sync
$IPT -A INPUT -i ${PUB_IF} -p tcp ! --syn -m state --state NEW  -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "Drop Sync"
$IPT -A INPUT -i ${PUB_IF} -p tcp ! --syn -m state --state NEW -j DROP

# Block Fragments
$IPT -A INPUT -i ${PUB_IF} -f  -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "Fragments Packets"
$IPT -A INPUT -i ${PUB_IF} -f -j DROP

# Block bad stuff
$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags ALL FIN,URG,PSH -j DROP
$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags ALL ALL -j DROP

$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags ALL NONE -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "NULL Packets"
$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags ALL NONE -j DROP # NULL packets

$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags SYN,RST SYN,RST -j DROP

$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags SYN,FIN SYN,FIN -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "XMAS Packets"
$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags SYN,FIN SYN,FIN -j DROP #XMAS

$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags FIN,ACK FIN -m limit --limit 5/m --limit-burst 7 -j LOG --log-level 4 --log-prefix "Fin Packets Scan"
$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags FIN,ACK FIN -j DROP # FIN packet scans

$IPT  -A INPUT -i ${PUB_IF} -p tcp --tcp-flags ALL SYN,RST,ACK,FIN,URG -j DROP

# Allow full outgoing connection but no incomming stuff
$IPT -A INPUT -i ${PUB_IF} -m state --state ESTABLISHED,RELATED -j ACCEPT
$IPT -A OUTPUT -o ${PUB_IF} -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT

# Allow ssh
$IPT -A INPUT -i ${PUB_IF} -p tcp --destination-port 22 -j ACCEPT

# Allow http / https (open port 80 / 443)
$IPT -A INPUT -i ${PUB_IF} -p tcp --destination-port 80 -j ACCEPT
#$IPT -A INPUT -o ${PUB_IF} -p tcp --destination-port 443 -j ACCEPT

# allow incomming ICMP ping pong stuff
$IPT -A INPUT -i ${PUB_IF} -p icmp --icmp-type 8 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
#$IPT -A OUTPUT -o ${PUB_IF} -p icmp --icmp-type 0 -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow port 53 tcp/udp (DNS Server)
$IPT -A INPUT -i ${PUB_IF} -p udp --dport 53 -m state --state NEW,ESTABLISHED,RELATED -j ACCEPT
#$IPT -A OUTPUT -o ${PUB_IF} -p udp --sport 53 -m state --state ESTABLISHED,RELATED -j ACCEPT

$IPT -A INPUT -i ${PUB_IF} -p tcp --destination-port 53 -m state --state NEW,ESTABLISHED,RELATED  -j ACCEPT
#$IPT -A OUTPUT -o ${PUB_IF} -p tcp --sport 53 -m state --state ESTABLISHED,RELATED -j ACCEPT

# Open port 110 (pop3) / 143
$IPT -A INPUT -i ${PUB_IF} -p tcp --destination-port 110 -j ACCEPT
$IPT -A INPUT -i ${PUB_IF} -p tcp --destination-port 143 -j ACCEPT

##### Add your rules below ######
#
#
##### END your rules ############

# Do not log smb/windows sharing packets - too much logging
$IPT -A INPUT -p tcp -i ${PUB_IF} --dport 137:139 -j REJECT
$IPT -A INPUT -p udp -i ${PUB_IF} --dport 137:139 -j REJECT

# log everything else and drop
$IPT -A INPUT -j LOG
$IPT -A FORWARD -j LOG
$IPT -A INPUT -j DROP

exit 0
```

## Check all current firewall settings

iptables -D INPUT -s [source] --sport [source port] -d [destination] --dport [destination port] -j [policy]

```
iptables -L

# Reset firewall configuration
iptables -F
# Set default policy to ACCEPT
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT

# To list all IPv4 rules :
sudo iptables -S
# To list all IPv6 rules :
sudo ip6tables -S
# To list all tables rules :
sudo iptables -L -v -n | more
# To list all rules for INPUT tables :
sudo iptables -L INPUT -v -n
sudo iptables -S INPUT
```

## Add firewall rules

iptables -D INPUT -s [source] --sport [source port] -d [destination] --dport [destination port] -j [policy]

```
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
## Allow packets on port 22

iptables -A INPUT -s 192.168.0.111 -j DROP
# Block all connections from source IP 192.168.0.111

iptables -A INPUT -p icmp -s 127.0.0.1 -j DROP
# Add a policy to the INPUT chain to reject (-j DROP) ICMP protocol (-p icmp) packets from source address 127.0.0.1 (-s 127.0.0.1)

iptables -A INPUT -p tcp --dport 23 -j DROP
# Add (-A) a rule to reject (-j DROP) TCP protocol (-p tcp) packets with destination port 23 (--dport 23) to INPUT chain

iptables -A INPUT -p tcp --dport :1023 -j DROP
# Add (-A) a rule to reject (-j DROP) TCP protocol (-p tcp) packets with destination ports less than 1023 (--dport :1023) to INPUT chain

iptables -I INPUT -p tcp --dport 21 -j ACCEPT
# Open FTP port

iptables -I INPUT -s 192.168.0.0/255.255.255.0 -p udp --dport 143 -j ACCEPT
# Open IMAP service in firewall

iptables -I INPUT -p tcp --dport 80 -j ACCEPT
# Open web server firewall

iptables -R INPUT 2 -p tcp --dport 8880 -j ACCEPT
# Replace web server port 80 with 8880 (need to change in /etc/services too if changing service port)

cat domain-access_log |awk '{print $1}'|sort |uniq |awk '{print "iptables -A INPUT -s "$1" -j DROP"}'|/bin/bash
# Block all connection ports for all IPs in domain-access_log file (used for DoS attack defense)
```

## Remove firewall rules

```
iptables -D INPUT -s 127.0.0.1 -p icmp -j DROP
## Delete rule
```

## Packet request throttling

If the same IP makes 10 or more SYN requests to port 80 in 1 second, drop it.  
(This treats it as a web service attack rather than a normal request and discards the request packet so it doesn't respond.)

```
iptables -A INPUT -p tcp --dport 80 -m recent --update --seconds 1 --hitcount 10 --name HTTP -j DROP
```

## Save IPTABLES configuration

```
service iptables save
# Saved in /etc/sysconfig/iptables

1 save
iptables-save > /etc/iptables.rules
2 restore
iptables-restore < /etc/iptables.rules
3 auto restore on boot
cat EOF >> /etc/network/interfaces pre-up iptables-restore < /etc/iptables.rules pst-down iptables-save -c > /etc/iptables.rules EOF
```

## Advanced usage examples

When external HTTP access is requested to 192.168.0.30:80

```
iptables -t mangle -A PREROUTING -i eth0 -j TEE --gateway 192.168.0.1
# Mirror eth0 port 80 incoming content to gateway 192.168.0.1 using TEE in mangle PREROUTING

iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-port 8080
# DNAT in nat PREROUTING to change dport 80 to 8080

iptables -F INPUT
iptables -P DROP
# Default DROP the INPUT chain in filter, then traverse and register entire user-defined chain

iptables -N user-before-input-logging
# user-before-input-logging: create chain only, no rule

iptables -N user-before-input
# user-before-input

iptables -N user-after-input
iptables -N user-after-input-logging
iptables -N user-reject-input
iptables -N user-track-input
iptables -N user-input-skip
iptables -A INPUT -j user-before-input-logging
iptables -A INPUT -j user-before-input
iptables -A INPUT -j user-after-input
iptables -A INPUT -j user-after-input-logging
iptables -A INPUT -j user-reject-input
iptables -A INPUT -j user-track-input

iptables -A user-before-input -m conntrack --ctstate INVALID -j DROP
# Using conntrack, drop connections with INVALID state and log

iptables -A user-before-input -p icmp -j ACCEPT
# Accept ICMP protocol

iptables -A user-before-input -p udp --sport 67 --dport 68 -j ACCEPT
# Accept UDP protocol sport 67 dport 68

iptables -A user-before-input -p tcp -d 235.255.255.250/32 --dport 5353 -j ACCEPT
# Accept TCP protocol dst 235.255.255.250/32 dport 5353

iptables -A user-after-input -p udp --dport 137 -j user-input-skip
# Jump UDP protocol dport 136 to user-input-skip
iptables -A user-after-input -p tcp --dport 139 -j user-input-skip
# Jump TCP protocol dport 139 to user-input-skip
iptables -A user-after-input -m addrtype --dst-type BROADCAST -j user-input-skip
# Jump BROADCAST type to user-input-skip

iptables -A user-after-input-logging -m limit --limit 3/min --limit-burst 10 -j LOG --log-prefix "[USERLIMIT BLOCK]"
iptables -A user-track-input -p tcp -m conntrack --ctstate NEW -j ACCEPT
iptables -A user-track-input -p udp -m conntrack --ctstate NEW -j ACCEPT

iptables -A user-input-skip -j ACCEPT
# user-input-skip, user-output-skip accept all packets
iptables -N user-output-redirect
iptables -N user-output-block
iptables -A user-output-redirect -d 192.168.0.0 -j REDIRECT --to-port 50080
# Redirect dst 192.168.0.0 or dport 8080 to 127.0.0.1:50080

iptables -A user-output-redirect --dport 8080 -j REDIRECT --to-port 50080
iptables -A user-output-block -p icmp -m icmp --icmp-type 11 -j DROP
# Drop if icmp-type is 11

iptables -t mangle -A POSTROUTING -i eth0 -j TEE --gateway 127.0.0.1
# Mirror to local loopback using TEE in mangle POSTROUTING

iptables -t nat -A POSTROUTING -s 127.0.0.1 --sport 80 -o eth1 -j MASQUERADE --to-port 8080
# In nat POSTROUTING, masquerade packets from local loopback with sport 80 to output interface eth1 with src IP and sport 8080
```

## Issue handling

- Chain order is always important. If an IP/port is already blocked above, it won't be applied even if ACCEPT is set. In that case, verify if it was added with -I

## Theory

### Filter table

Linux server: Server hosting websites

- INPUT: From external to Linux server
- FORWARD: Via Linux server to elsewhere
- OUTPUT: From Linux server to external

### State values

ESTABLISHED – Part of existing connection  
NEW – New connection request packet  
RELATED – Belongs to existing connection but new connection request  
INVALID – Nowhere in connection tracking table  
DROP – Marks target as empty. No response. Timeout occurs  
REJECT – ICMP port unreachable response. Use reject in LAN. Reject response occurs

### Add rules

-s (--source) source IP  
-d (--destination) destination IP  
-p (--protocol) specific protocol  
-i (--in-interface) input interface  
-o (--out-interface) output interface  
-t (--table) table to process  
-j (--jump) specify how to handle packets matching the rule

-A (--append) add new rule at bottom  
-I (--insert) add new rule at top  
-P (--policy) change default policy  
-L (--list) output rules  
-D (--delete) delete rule  
-R (--replace) replace new rule  
-F (--flush) delete all rules in chain  
-C (--check) test packet  
-X (--delete-chain) delete empty chain

### Role of NAT table

- PREROUTING: Change IP, port before packet goes to INPUT rule
- INPUT: Works same as filter table but executed first
- OUTPUT: Same as above
- POSTROUTING: Change IP, port after packet comes from OUTPUT rule

### Masquerade

- Linux network function similar to router
- Changes source address of packets going external through gateway to public IP address on gateway

## IPTABLES - CentOS installation and verification

```
# Switch to Root
sudo -i
# Check iptable
cat /etc/sysconfig/iptables
# Install iptable
yum install iptables-services
```

## Source

<https://yurmu.tistory.com/31>  
<https://linuxstory1.tistory.com/entry/iptables-%EA%B8%B0%EB%B3%B8-%EB%AA%85%EB%A0%B9%EC%96%B4-%EB%B0%8F-%EC%98%B5%EC%85%98-%EB%AA%85%EB%A0%B9%EC%96%B4>  
<https://webdir.tistory.com/170>
