---
title: "AWS Introduced"
date: 2024-05-28T12:22:44+09:00
slug: "109-AWS-Introduced"
original_url: "https://memoryhub.tistory.com/109"
tistory_id: 109
draft: false
categories: ["Dev AWS"]
---

*AWS, or Amazon Web Services, is like a toolbox full of various tools that help businesses build and run their digital operations on the internet, offering services from storage and computing power to machine learning and artificial intelligence.*

### The Big Picture

Think of AWS (Amazon Web Services) as a giant toolbox filled with various tools and resources that businesses can use to build and manage their digital projects. Instead of having to buy and maintain physical hardware (like servers), companies can rent these resources from AWS and pay only for what they use. This is similar to how you might rent a car when you need it instead of buying one.

### Core Concepts

1. **Cloud Computing**: The delivery of computing services (like servers, storage, databases, networking, software) over the internet ("the cloud").
2. **Scalability**: The ability to easily increase or decrease the amount of resources you use, ensuring you only pay for what you need.
3. **Global Reach**: AWS has data centers all around the world, allowing businesses to serve their customers with low latency, regardless of their location.
4. **Services**: AWS offers a wide range of services categorized into different domains such as computing, storage, databases, networking, analytics, and more.

### Detailed Walkthrough

1. **Compute Services**: These services provide the processing power required to run applications.

   - **Amazon EC2 (Elastic Compute Cloud)**: Virtual servers that can be scaled up or down based on demand.
   - **AWS Lambda**: Run code without provisioning or managing servers, billed only for the actual compute time.
2. **Storage Services**: These services offer various ways to store, access, and manage data.

   - **Amazon S3 (Simple Storage Service)**: Object storage with high durability and availability.
   - **Amazon EBS (Elastic Block Store)**: Persistent block storage volumes for use with EC2 instances.
3. **Database Services**: Managed database services that support different types of databases.

   - **Amazon RDS (Relational Database Service)**: Managed relational databases (like MySQL, PostgreSQL).
   - **Amazon DynamoDB**: NoSQL database service for applications needing high throughput.
4. **Networking Services**: Services that help manage network configurations and security.

   - **Amazon VPC (Virtual Private Cloud)**: Isolated cloud resources in a virtual network.
   - **Amazon Route 53**: Scalable DNS web service.
5. **Machine Learning & AI**: Tools and frameworks to build, train, and deploy machine learning models.

   - **Amazon SageMaker**: A fully managed service to build, train, and deploy machine learning models.
   - **AWS Rekognition**: Image and video analysis.

### Understanding Through an Example

Imagine you're building a web application:

1. **Compute**: Use Amazon EC2 instances to host your application servers.
2. **Storage**: Store user uploads (like images) in Amazon S3.
3. **Database**: Use Amazon RDS to store user information and other relational data.
4. **Networking**: Set up a VPC to control your network environment and use Route 53 for DNS management.
5. **Scaling**: Automatically scale your application based on traffic using AWS Auto Scaling.
6. **Machine Learning**: Incorporate features like image recognition using AWS Rekognition.

### Conclusion and Summary

AWS provides a comprehensive set of tools and services that help businesses run applications and manage data without the need to invest in physical hardware. It's flexible, scalable, and globally accessible, making it an ideal choice for businesses of all sizes.

### Test Your Understanding

1. **What is the main advantage of using AWS over traditional physical servers?**
2. **Can you name two AWS services related to storage and explain their differences?**
3. **How does AWS Lambda differ from Amazon EC2?**

### Reference

For further learning, you can visit the official [AWS documentation](https://aws.amazon.com/documentation/).
