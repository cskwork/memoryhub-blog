---
title: "Amazon VPC Introduced"
date: 2024-05-29T08:01:44+09:00
slug: "158-Amazon-VPC-Introduced"
original_url: "https://memoryhub.tistory.com/158"
tistory_id: 158
draft: false
categories: ["Dev AWS"]
tags: ["VPC"]
---

*Amazon VPC (Virtual Private Cloud) allows you to create a logically isolated section of the AWS cloud where you can launch AWS resources in a virtual network that you define.*

### The Big Picture

Think of Amazon VPC as a private, secure, and customizable house within a large apartment complex (AWS). You get to design the layout of your house, decide how rooms (subnets) are connected, who can enter (security groups and network ACLs), and how your house connects to the outside world (internet gateway or VPN).

### Core Concepts

1. **Subnets**: Segments of your VPC where you can place groups of AWS resources, either in a public or private section.
2. **Internet Gateway (IGW)**: A gateway that allows communication between instances in your VPC and the internet.
3. **NAT Gateway/Instance**: Enables instances in a private subnet to connect to the internet while preventing the internet from initiating connections with those instances.
4. **Route Tables**: Determine how network traffic is directed within your VPC.
5. **Security Groups**: Act as virtual firewalls for your instances to control inbound and outbound traffic.
6. **Network Access Control Lists (NACLs)**: Provide an additional layer of security at the subnet level by controlling inbound and outbound traffic.
7. **VPC Peering**: Allows you to route traffic between VPCs using private IP addresses.
8. **VPN and Direct Connect**: Options for securely connecting your VPC to your on-premises network.

### Detailed Walkthrough

**1. Subnets:**  
Subnets are like rooms in your house, each serving different purposes. Public subnets have access to the internet, suitable for web servers. Private subnets do not have direct internet access and are suitable for databases and application servers. This segmentation helps control traffic and enhance security.

**2. Internet Gateway (IGW):**  
An IGW is like the main door of your house, connecting your private residence (VPC) to the outside world (internet). It allows resources in public subnets to communicate with the internet.

**3. NAT Gateway/Instance:**  
A NAT (Network Address Translation) Gateway or Instance is like a mailroom that lets residents (instances in private subnets) send out mail (connect to the internet) without exposing their private addresses to the outside world. This setup maintains security while allowing necessary outbound communication.

**4. Route Tables:**  
Route tables are like the blueprints of your house's layout, dictating how traffic moves from one room (subnet) to another and to the outside world. Each subnet is associated with a route table that directs traffic based on defined rules.

**5. Security Groups:**  
Security groups are like the security guards at each door, controlling who can enter and leave. They operate at the instance level and allow you to specify which traffic is allowed in or out of your instances.

**6. Network Access Control Lists (NACLs):**  
NACLs are like the security gates at the entrance of each room (subnet), providing an additional layer of security. They control traffic at the subnet level, complementing the security groups.

**7. VPC Peering:**  
VPC peering is like having a private tunnel connecting two houses, allowing seamless communication between them without using the public internet. This is useful for connecting multiple VPCs within or across AWS regions.

**8. VPN and Direct Connect:**  
VPNs (Virtual Private Networks) and AWS Direct Connect are methods to securely connect your VPC to your on-premises data center. A VPN is like a secure tunnel over the internet, while Direct Connect is like a dedicated, private line.

### Understanding Through an Example

Let's say you're building a web application. You create a VPC to host this application securely:

1. **Subnets**: You create a public subnet for your web servers and a private subnet for your database servers.
2. **Internet Gateway**: You attach an IGW to your VPC to allow your web servers to communicate with users over the internet.
3. **NAT Gateway**: You set up a NAT Gateway to allow your database servers in the private subnet to download software updates from the internet without exposing them.
4. **Route Tables**: You configure route tables to direct internet traffic from the public subnet to the IGW and private subnet traffic through the NAT Gateway.
5. **Security Groups**: You create security groups to control access to your web and database servers, allowing only necessary traffic.
6. **NACLs**: You implement NACLs to add another layer of subnet-level security.
7. **VPC Peering**: If you have another VPC running backend services, you set up VPC peering to allow private communication between the VPCs.

### Conclusion and Summary

Amazon VPC enables you to create a secure, isolated section of the AWS cloud tailored to your needs. With features like subnets, security groups, route tables, and more, you have full control over your virtual network environment.

### Test Your Understanding

1. What is the role of subnets in an Amazon VPC?
2. How does an Internet Gateway differ from a NAT Gateway?
3. What are security groups and how do they differ from NACLs?
4. What is VPC peering, and when might you use it?

### Reference

For further reading and detailed documentation, refer to the [Amazon VPC Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html).
