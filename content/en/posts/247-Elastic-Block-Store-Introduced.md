---
title: "Elastic Block Store Introduced"
date: 2024-06-10T15:08:36+09:00
slug: "247-Elastic-Block-Store-Introduced"
original_url: "https://memoryhub.tistory.com/247"
tistory_id: 247
draft: false
---

*Amazon Elastic Block Store (EBS) is a service that provides persistent block storage volumes for use with Amazon EC2 instances.*

### The Big Picture

Think of Amazon Elastic Block Store (EBS) as a durable and high-performance hard drive attached to your computer (in this case, an EC2 instance in the AWS cloud). Just like your computer's hard drive, EBS provides block-level storage that can be used to store data persistently and retrieve it whenever needed.

### Core Concepts

1. **Block Storage**: Unlike object storage, block storage organizes data into fixed-size blocks, which allows for fast read and write operations.
2. **EBS Volumes**: These are the actual storage units that you attach to your EC2 instances.
3. **Snapshots**: Point-in-time copies of your EBS volumes, useful for backups and data recovery.

### Detailed Walkthrough

#### Block Storage

Block storage is similar to the way your computer's hard drive works. It divides the storage into blocks, each with a unique address, allowing for efficient reading and writing of data. This is different from object storage, which manages data as objects.

#### EBS Volumes

EBS volumes are virtual hard drives that you can attach to your EC2 instances. Here are some key features:

- **Durability**: Data stored in EBS is replicated within its Availability Zone to prevent data loss.
- **Scalability**: You can easily increase the size or performance characteristics of an EBS volume.
- **Flexibility**: EBS volumes can be used as primary storage for data that requires frequent updates, such as the root device of an EC2 instance or for applications that require databases, file systems, or raw block storage.

#### Snapshots

Snapshots are like backup copies of your EBS volumes at a specific point in time. They are stored in Amazon S3, which is a highly durable storage service. You can use snapshots to:

- Create new volumes from an existing snapshot.
- Restore a volume to a previous state.
- Migrate data between regions or accounts.

### Understanding Through an Example

Suppose you are running a web application on an EC2 instance that needs to store and retrieve data quickly and reliably. Here's how you might use EBS:

1. **Create an EBS Volume**: Provision an EBS volume with the desired size and performance characteristics.
2. **Attach to EC2 Instance**: Attach the EBS volume to your EC2 instance.
3. **Mount and Format**: Mount the volume to a directory on your instance and format it with a file system.
4. **Use for Storage**: Use the volume for your application's data storage needs.

Here's a step-by-step example using the AWS Command Line Interface (CLI):

1. **Create an EBS volume**:

`aws ec2 create-volume --size 10 --region us-east-1 --availability-zone us-east-1a --volume-type gp2`

1. **Attach the volume to an EC2 instance**:

`aws ec2 attach-volume --volume-id vol-0123456789abcdef0 --instance-id i-1234567890abcdef0 --device /dev/sdf`

1. **Mount and format the volume**:

`# Connect to your EC2 instance and format the volume`

`ssh ec2-user@your-ec2-instance
sudo mkfs -t ext4 /dev/xvdf
sudo mkdir /data
sudo mount /dev/xvdf /data`

### Conclusion and Summary

Amazon Elastic Block Store (EBS) is a scalable, high-performance block storage service designed for use with Amazon EC2. It provides persistent storage that is replicated within its availability zone for durability and can be easily backed up using snapshots. EBS is ideal for workloads that require frequent read and write access to data.

### Test Your Understanding

1. What are the main benefits of using EBS with EC2 instances?
2. How do EBS snapshots enhance data durability and recovery?
3. Can you explain the difference between block storage and object storage?

### Reference

- [Amazon EBS Documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)
