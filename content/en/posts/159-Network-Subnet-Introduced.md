---
title: "Network Subnet Introduced"
date: 2024-05-29T08:02:42+09:00
slug: "159-Network-Subnet-Introduced"
original_url: "https://memoryhub.tistory.com/159"
tistory_id: 159
draft: false
categories: ["Dev Concepts"]
tags: ["Theory Notes"]
---

*A subnet, or subnetwork, is a segmented piece of a larger network that isolates specific groups of devices to improve performance and enhance security.*

### The Big Picture

Imagine you have a large office building with many departments: finance, marketing, IT, etc. To organize and manage them better, you allocate specific floors or sections to each department. Similarly, in a network, a subnet allows you to divide a larger network into smaller, more manageable sections. Each subnet can be tailored to the specific needs of the devices it contains, optimizing network performance and security.

### Core Concepts

1. **Segmentation**: Subnets divide a larger network into smaller, more manageable sections.
2. **Network Address and Subnet Mask**: Defines the range of IP addresses available within a subnet.
3. **Routing**: Determines how data is directed between subnets and the larger network.
4. **Security**: Controls access and enhances security within and between subnets.
5. **Performance**: Improves network efficiency by reducing broadcast traffic.

### Detailed Walkthrough

**1. Segmentation:**  
Subnets allow you to segment a large network into smaller networks. This segmentation helps manage and secure the network more effectively. For instance, devices in one subnet can be isolated from devices in another subnet, preventing unnecessary traffic and enhancing security.

**2. Network Address and Subnet Mask:**  
Each subnet is defined by a network address and a subnet mask. The network address identifies the subnet, while the subnet mask determines the range of IP addresses within that subnet. It's like having a postal code (network address) and a set of street numbers (IP addresses) within that code.

- **Network Address**: Identifies the subnet.
- **Subnet Mask**: Determines the size of the subnet and the range of IP addresses it can contain.

For example, in the subnet `192.168.1.0/24`:

- `192.168.1.0` is the network address.
- `/24` is the subnet mask, indicating that the first 24 bits are the network part, and the remaining bits are for host addresses.

**3. Routing:**  
Routers direct data between subnets and the larger network. Each subnet has its own routing table, which determines how traffic should be forwarded. This ensures that data sent from one subnet to another follows the correct path.

**4. Security:**  
Subnets enhance security by controlling access at the subnet level. Network Access Control Lists (NACLs) and Security Groups can be used to allow or deny traffic to and from specific subnets. This is like having security guards at the entrance of each department, controlling who can enter or leave.

**5. Performance:**  
By reducing the amount of broadcast traffic (traffic sent to all devices in a network), subnets improve network performance. Devices within a subnet only communicate with other devices in the same subnet unless they need to send data to another subnet, reducing overall network congestion.

### Understanding Through an Example

Consider a company with an office network that includes different departments such as HR, Sales, and IT. To manage this network efficiently, the network administrator creates subnets for each department:

- **HR Subnet**: `192.168.1.0/24`
- **Sales Subnet**: `192.168.2.0/24`
- **IT Subnet**: `192.168.3.0/24`

Each subnet is isolated from the others, meaning devices in the HR subnet cannot directly communicate with devices in the Sales or IT subnets without proper routing and permissions. This setup ensures that each department's traffic is contained within its own subnet, enhancing security and performance.

### Conclusion and Summary

A subnet is a crucial component of a network that divides a larger network into smaller, more manageable sections. This segmentation improves performance, enhances security, and simplifies network management by isolating groups of devices. By defining subnets with network addresses and subnet masks, you can effectively control how data flows within and between these segments.

### Test Your Understanding

1. What is the purpose of a subnet in a network?
2. How does a subnet mask define the range of IP addresses in a subnet?
3. Explain how routing works between subnets.
4. Why are subnets important for network security and performance?

### Reference

For further reading and detailed documentation, refer to the [Amazon VPC Subnet Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html).
