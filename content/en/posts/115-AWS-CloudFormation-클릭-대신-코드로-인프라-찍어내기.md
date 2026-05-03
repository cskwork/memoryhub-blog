---
title: "AWS CloudFormation: Infrastructure as Code Instead of Clicking"
date: 2024-05-28T12:36:46+09:00
slug: "115-AWS-CloudFormation-클릭-대신-코드로-인프라-찍어내기"
original_url: "https://memoryhub.tistory.com/115"
tistory_id: 115
draft: false
categories: ["Dev AWS"]
tags: ["Cloud Formation"]
---

```
      .--.
    .----' ,-.
    '-.  `'   `
      .'        `.
     /      ☁️     \
    |   { IaC }   |
     \    ➡️     /
      `.   AWS  .'
        `'---'`
```

Ever spent an entire night clicking through the AWS console to set up a single server, configuring EC2, VPC, security groups, IAM roles, and everything else? We've all been there. The problem is that you have to repeat this work for each deployment environment, and it's hard to track who changed what settings. One wrong configuration change can bring down your entire service. Can we automate all of this and ensure it works the same way every time without mistakes?

⚡ **TL;DR:**

- AWS CloudFormation is AWS's flagship service for managing infrastructure as code (IaC).
- With a single template file, you can declare AWS resources like EC2 and S3, and CloudFormation automatically creates and manages them.

## Table of Contents

1. Background: Why should you use CloudFormation?
2. Core concepts: Templates and stacks
3. Practice: Creating an S3 bucket with code
4. Best practices
5. Conclusion and resources

---

## 1. Background: Why should you use CloudFormation?

In the past, developers had to log directly into the AWS console and create resources manually (EC2 instances, databases, etc.). While intuitive, this approach has several critical problems.

- **Slow and repetitive work:** Configuring an scalable web application with Auto Scaling groups, load balancers, and databases is complex and time-consuming.
- **Human error:** Manual work often leads to configuration mistakes or oversights.
- **Lack of consistency:** It's difficult to ensure development, staging, and production environments have identical infrastructure.
- **No change tracking:** It's hard to know who changed what, when, or why.

AWS CloudFormation solves these problems through the **IaC (Infrastructure as Code)** approach. By writing infrastructure configuration as code (templates), you can simplify infrastructure management, quickly replicate environments, easily control and track changes, and reduce errors.

✅ **Terminology Guide**

- **IaC (Infrastructure as Code):** A methodology for managing and provisioning infrastructure using code. CloudFormation is AWS's flagship IaC service.
- **Template:** A design blueprint file that defines all AWS resources and their properties. Can be written in JSON or YAML format.
- **Stack:** A collection of AWS resources created and managed through a template. Stacks are created, updated, and deleted as a single unit.

## 2. Core concepts: Templates and stacks

> **AWS CloudFormation automatically creates and manages AWS infrastructure in a predictable and repeatable manner using design blueprints called templates.**

Developers only need to define all required resources in a **template**. CloudFormation then reads the template, understands resource dependencies, provisions them in the correct order, and creates a **stack**.

Here's a simple YAML template example for creating an S3 bucket:

```
# Template file format version
AWSTemplateFormatVersion: '2010-09-09'
Description: Simple CloudFormation template for creating an S3 bucket

# Values to be provided externally when creating the stack (parameters)
Parameters:
  BucketName:
    Description: Name of the S3 bucket to create
    Type: String

# Actual AWS resources to be created
Resources:
  S3Bucket:
    Type: 'AWS::S3::Bucket' # Resource type: S3 bucket
    Properties:
      BucketName: !Ref BucketName # Use the BucketName parameter as the bucket name

# Values to be output after stack creation
Outputs:
  BucketARN:
    Description: ARN of the created S3 bucket
    Value: !GetAtt S3Bucket.Arn
```

This template is structured with three main sections: `Parameters`, `Resources`, and `Outputs`. The `Resources` section is most important, defining the actual AWS resources to create.

## 3. Practice: Creating an S3 bucket with code

Let's create a stack using the template we wrote above.

**① Prepare the template file**

- Save the YAML code above as a file like `s3-bucket-template.yaml`.

**② Create the stack (AWS Console)**

- Log in to the AWS management console and navigate to CloudFormation.
- Click **'Create Stack'** and select **'Create with new resources (standard)'**.
- In the **'Prepare template'** step, select **'Upload a template file'** and upload the `s3-bucket-template.yaml` file you just saved.
- Enter a **'Stack name'** and provide a `BucketName` in the `Parameters` section.
- Leave other options at their default values and proceed to the end, then click **'Create Stack'**.

**③ Verify creation and cleanup**

- After a few moments, the stack status will change to `CREATE_COMPLETE`, meaning resources were created successfully. You can verify by checking the EC2 or S3 console to see the bucket.
- Deleting a stack removes all resources belonging to that stack in one go, making resource management very convenient.

## 4. Best Practices

Here are some best practices for using CloudFormation more effectively:

| Pattern | Advantages | Cautions |
| --- | --- | --- |
| **Template Modularization (Nested Stacks)** | Breaking down complex infrastructure into smaller units (network, application, etc.) improves reusability and management. | Stack interdependencies can make management complex, so clear design is needed. |
| **Using Parameters and Mappings** | Apply different instance types or AMI IDs for different environments (dev/prod) without modifying the template. | Too many parameters can make template usage more complex rather than simpler. |
| **Using Change Sets** | Review what resources will change and how before updating a stack, preventing unintended resource changes or deletions. | An additional review step is needed before applying changes. |
| **Drift Detection** | Detect differences (drift) between the template-defined configuration and actual resource configuration, helping maintain infrastructure consistency. | Regular drift checking and remediation requires operational effort. |

## 5. Conclusion

Today we learned about CloudFormation, which automatically provisions and manages AWS infrastructure through code.

- Managing infrastructure as code reduces manual work mistakes and maximizes productivity.
- Templates allow you to standardize complex architectures and quickly replicate them in any environment.
- Stack-based management provides clear and safe lifecycle management for all resources, from creation to deletion.

**Real-world tip:** Version-control your CloudFormation templates with Git and integrate them with CI/CD tools like Jenkins or AWS CodePipeline to automate infrastructure changes. This can become a core part of your DevOps pipeline.

If you found today's content helpful, please give it a heart ❤️ and leave a comment! Your small interest is a big help in writing better posts.

---

**References**

- [AWS CloudFormation Official User Guide](https://docs.aws.amazon.com/cloudformation/latest/userguide/)
- [AWS CloudFormation Product Page](https://aws.amazon.com/cloudformation/)
