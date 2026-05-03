---
title: "EBS vs ECR"
date: 2024-06-10T15:18:26+09:00
slug: "249-EBS-vs-ECR"
original_url: "https://memoryhub.tistory.com/249"
tistory_id: 249
draft: false
categories: ["Dev AWS"]
---

*Amazon Elastic Block Store (EBS) and Amazon Elastic Container Registry (ECR) are both AWS storage services but serve different purposes: EBS provides block storage for EC2 instances, while ECR is a managed Docker container registry.*

### The Big Picture

Imagine you have a computer. The hard drive in the computer, which stores all your files and data, represents Amazon EBS. Meanwhile, if you think of your computer running various applications packed in containers, the place where these containers are stored and managed would be akin to Amazon ECR.

### Core Concepts

#### Amazon EBS

- **Purpose**: Provides persistent block storage for Amazon EC2 instances.
- **Functionality**: Acts like a hard drive for your virtual servers (EC2), allowing you to store and retrieve data persistently.
- **Use Cases**: Database storage, file systems, or any application requiring high-performance block storage.
- **Persistence**: Data persists independently of the life of the EC2 instance.
- **Snapshots**: You can create snapshots of EBS volumes for backup and disaster recovery.

#### Amazon ECR

- **Purpose**: Stores, manages, and deploys Docker container images.
- **Functionality**: Acts like a repository for your Docker images, enabling you to push, pull, and manage images.
- **Use Cases**: Storing container images for applications deployed in Amazon ECS, EKS, or other container orchestration platforms.
- **Integration**: Works seamlessly with container services like Amazon ECS and EKS.
- **Security**: Provides secure access to container images using AWS IAM policies.

### Detailed Walkthrough

#### Amazon EBS

1. **Create an EBS Volume**:

   ```
   aws ec2 create-volume --size 20 --region us-east-1 --availability-zone us-east-1a --volume-type gp2
   ```
2. **Attach to an EC2 Instance**:

   ```
   aws ec2 attach-volume --volume-id vol-0123456789abcdef0 --instance-id i-1234567890abcdef0 --device /dev/sdf
   ```
3. **Use the Volume**:

   ```
   ssh ec2-user@your-ec2-instance
   sudo mkfs -t ext4 /dev/xvdf
   sudo mkdir /data
   sudo mount /dev/xvdf /data
   ```

#### Amazon ECR

1. **Authenticate Docker to ECR**:

   ```
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com
   ```
2. **Push a Docker Image to ECR**:

   ```
   docker tag my-web-app:latest <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/my-web-app:latest
   docker push <aws_account_id>.dkr.ecr.us-east-1.amazonaws.com/my-web-app:latest
   ```
3. **Deploy from ECR**: Use AWS ECS or EKS to deploy the Docker image to your containers.

### Comparison

- **Storage Type**:

  - **EBS**: Block storage for individual instances.
  - **ECR**: Container image storage for deployment in container orchestration services.
- **Persistence**:

  - **EBS**: Persistent storage for data volumes.
  - **ECR**: Persistent storage for Docker images.
- **Use Cases**:

  - **EBS**: Databases, file systems, application data storage.
  - **ECR**: Containerized application deployment, CI/CD pipelines.
- **Management**:

  - **EBS**: Managed like a traditional hard drive, with options for snapshotting and volume resizing.
  - **ECR**: Managed like a Docker registry, with options for image versioning and repository management.

### Conclusion and Summary

Amazon EBS and Amazon ECR are essential AWS storage services designed for different purposes. EBS provides high-performance, scalable block storage for EC2 instances, making it ideal for applications needing persistent storage. In contrast, ECR is a managed Docker container registry, enabling the storage, management, and deployment of container images, ideal for modern containerized application workflows.

### Test Your Understanding

1. What are the primary differences between EBS and ECR in terms of storage type and use cases?
2. How does ECR enhance the deployment of containerized applications?
3. Can you describe a scenario where you would use EBS over ECR and vice versa?

### Reference

- [Amazon EBS Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
- [Amazon ECR Documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
