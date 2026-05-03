---
title: "EC2 Introduced"
date: 2024-05-29T12:23:45+09:00
slug: "110-EC2-Introduced"
original_url: "https://memoryhub.tistory.com/110"
tistory_id: 110
draft: false
---

*Amazon EC2 works by providing scalable virtual servers (instances) that can be configured and managed through a web interface or API, allowing businesses to run applications without owning physical hardware.*

### The Big Picture

Imagine you need a computer to run your applications, but instead of buying and maintaining your own physical hardware, you rent a virtual computer from Amazon. This virtual computer can be configured to meet your specific needs and can be scaled up or down as your requirements change. This is essentially how Amazon EC2 (Elastic Compute Cloud) works.

### Core Concepts

1. **Instances**: Virtual servers that you can rent to run your applications.
2. **AMI (Amazon Machine Image)**: A template that contains the software configuration (operating system, application server, and applications) needed to launch an instance.
3. **Instance Types**: Different configurations of CPU, memory, storage, and networking capacity that you can choose from.
4. **Elasticity**: The ability to scale instances up or down based on demand.
5. **Regions and Availability Zones**: Physical locations around the world where AWS data centers are located, offering redundancy and fault tolerance.

### Detailed Walkthrough

1. **Launching an Instance**:

   - Choose an **AMI**: Select a pre-configured template or create your own with the software you need.
   - Select an **Instance Type**: Choose the hardware configuration that best suits your needs (e.g., general-purpose, compute-optimized, memory-optimized).
   - Configure **Instance Details**: Set parameters like the number of instances, network settings, and monitoring options.
   - Add **Storage**: Attach additional storage volumes if needed, such as EBS (Elastic Block Store).
   - **Tag** your instance: Assign metadata to help organize and manage your instances.
   - Configure **Security Groups**: Set up firewall rules to control traffic to and from your instance.
   - **Launch** the instance: Start the virtual server.
2. **Using an Instance**:

   - **Connect**: Access your instance using SSH (for Linux) or RDP (for Windows).
   - **Deploy Applications**: Install and run your applications on the instance as you would on a physical server.
   - **Monitor and Manage**: Use AWS tools like CloudWatch to monitor performance and make adjustments as needed.
3. **Scaling**:

   - **Auto Scaling**: Automatically adjust the number of instances in response to traffic changes.
   - **Load Balancing**: Distribute incoming traffic across multiple instances using Elastic Load Balancing (ELB).
4. **Termination**:

   - **Stop or Terminate**: When an instance is no longer needed, it can be stopped (to preserve its state) or terminated (deleted permanently).

### Understanding Through an Example

Suppose you're running a web application that experiences varying levels of traffic:

1. **Choose an AMI**: Select an AMI with the web server software (like Apache) and the necessary libraries pre-installed.
2. **Select Instance Type**: Choose a general-purpose instance (like t2.micro) to start with.
3. **Configure Details**: Set up your instance to be in the same region as your users for low latency.
4. **Add Storage**: Attach an EBS volume to store your application's data.
5. **Security Groups**: Configure rules to allow HTTP/HTTPS traffic to your web server.
6. **Launch Instance**: Start the instance and deploy your web application.
7. **Auto Scaling**: Set up auto-scaling to add more instances during peak traffic times and reduce them during low traffic periods.
8. **Load Balancing**: Use an ELB to distribute traffic across multiple instances to ensure high availability.

### Conclusion and Summary

Amazon EC2 allows you to rent virtual servers tailored to your needs, providing flexibility, scalability, and cost-efficiency. You can easily launch, manage, and scale your instances to meet the demands of your applications without the overhead of physical hardware.

### Test Your Understanding

1. **What is an Amazon Machine Image (AMI), and why is it important?**
2. **How does Amazon EC2 provide scalability?**
3. **What is the purpose of a security group in Amazon EC2?**

### Reference

For more detailed information, visit the [Amazon EC2 documentation](https://docs.aws.amazon.com/ec2/index.html).
