---
title: "Amazon S3 (Simple Storage Service) Complete Guide?"
date: 2024-11-17T09:12:57+09:00
slug: "390-Amazon-S3-Simple-Storage-Service-완벽-가이드"
original_url: "https://memoryhub.tistory.com/390"
tistory_id: 390
draft: false
categories: ["Dev AWS"]
tags: ["S3"]
---

Today, let's explore **Amazon S3 (Simple Storage Service)**! S3, an object storage service provided by Amazon Web Services (AWS), delivers both scalability and reliability, making it suitable for various purposes regardless of enterprise scale. Let's examine S3's core concepts, operational mechanisms, advantages, precautions, and practical use cases.

---

## **1. What is Amazon S3??**

Amazon S3 (Simple Storage Service) is an **object storage service** that allows you to store and retrieve data over the internet. Here, 'object' refers to a unit containing the file itself and metadata describing the file.

- **Concept Summary**:

  - S3 stores data in large containers called 'buckets', and treats each piece of data as an object.
  - An object consists of file + metadata.
  - Objects can be uploaded and downloaded via URL, API, or SDK.
- **Real-Life Example**:

  - Storing image files uploaded by users on photo-sharing websites.
  - Storing media files (videos, music) on video streaming services.
  - Mobile apps uploading user profile or log data to S3 for later analysis.
- **What Problems Does It Solve?**

  1. **Scalability**: Storage capacity automatically scales, allowing data storage without worrying about capacity.
  2. **Availability**: Reliably hosted across multiple regions, ensuring high durability and availability.
  3. **Management Convenience**: No need to build or operate servers directly; manage easily via AWS console or API.

---

## **2. How Does It Work??**

### 1) Basic Concepts

Amazon S3's core operation includes the following:

- **Bucket Creation**: To store data in S3, you must first create a bucket (storage space). Bucket names must be globally unique and you can set the AWS region.
- **Object Upload**: Once a bucket is ready, upload data. When uploading objects, you can set permissions and metadata, and a URL to access that object is automatically generated.
- **Versioning**: If you enable versioning on a bucket, multiple uploads of the same filename are stored as separate versions. This provides safety against unintended deletions or modifications.
- **Object Lifecycle**: S3 offers lifecycle management to automatically move stored data to Glacier or other storage classes after a certain period. This can reduce costs.

Here's a simple example of creating a bucket and uploading an object using AWS CLI.

```
# Create a bucket using AWS CLI
aws s3 mb s3://my-example-bucket --region ap-northeast-2

# Upload a local file to the S3 bucket
aws s3 cp ./testfile.txt s3://my-example-bucket
```

### 2) Practical Application Example (Java Code Example)

Simple code to upload an object to S3 using AWS SDK for Java.

```
import software.amazon.awssdk.auth.credentials.ProfileCredentialsProvider;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.PutObjectRequest;
import java.nio.file.Paths;

public class S3UploadExample {
    public static void main(String[] args) {
        // 1. Create S3 Client
        S3Client s3 = S3Client.builder()
                .region(Region.AP_NORTHEAST_2)
                .credentialsProvider(ProfileCredentialsProvider.create())
                .build();

        // 2. Create PutObjectRequest
        PutObjectRequest putObjectRequest = PutObjectRequest.builder()
                .bucket("my-example-bucket")
                .key("uploaded-file.txt")
                .build();

        // 3. Upload to S3
        s3.putObject(putObjectRequest, Paths.get("local-file.txt"));

        System.out.println("File upload completed!");
    }
}
```

#### How It Works

1. **Bucket Creation**: Create a bucket with a globally unique name. Example: `my-example-bucket`
2. **S3Client Setup**: Use AWS SDK to specify credentials and region for S3 communication.
3. **Object Upload/Download**: Use methods like PutObject and GetObject to upload/download data.
4. **Permission Management**: Control who can access objects and how using AWS IAM policies or S3 bucket policies.

---

## **3. Main Advantages?**

1. **High Scalability**

   - S3 automatically scales, accommodating sudden demand increases. This allows stable service operation even during events or promotions with traffic surges.
2. **High Durability & Availability**

   - S3 Standard Storage guarantees 99.999999999% (eleven nines) durability. Additionally, high availability greatly reduces data loss and service interruption risks.
3. **Security Features**

   - Fine-grained access control is possible through integration with AWS IAM (Identity and Access Management). Bucket policies and object-level ACL (Access Control List) support enable granular permission settings.
   - Provide additional security layers using **Server-Side Encryption** and **Client-Side Encryption** features.
4. **Cost Efficiency**

   - The pay-as-you-go model means virtually no upfront investment costs.
   - Combining storage classes (Standard, Infrequent Access, Glacier, etc.) to your needs minimizes storage costs.

---

## **4. Things to Note ⚠️**

1. **Name Conflicts**

   - Bucket names must be globally unique, so common names risk conflicts. Include company or project-specific identifiers in bucket names.
2. **Increased Costs with Versioning**

   - Enabling versioning stores multiple versions of the same file, increasing storage costs. Set up a good version cleanup policy.
3. **Data Exposure from Permission Mistakes**

   - Accidentally opening public access permissions for S3 buckets and objects can expose data to the entire world. Set bucket policies and access control lists carefully.
4. **Region Selection**

   - Choosing the correct region at bucket creation minimizes latency and transmission costs. Create buckets in regions close to where users primarily operate.

---

## **5. Practical Usage Examples?**

Here we'll explore AWS CLI and simple lifecycle policy configuration examples.

```
# 1. Create a bucket
aws s3 mb s3://my-lifecycle-bucket --region ap-northeast-2

# 2. Create a lifecycle policy file (JSON) (lifecycle.json)
cat <<EOL > lifecycle.json
{
   "Rules": [
      {
         "ID": "TransitionToIA",
         "Prefix": "",
         "Status": "Enabled",
         "Transitions": [
            {
               "Days": 30,
               "StorageClass": "STANDARD_IA"
            }
         ]
      }
   ]
}
EOL

# 3. Apply lifecycle policy
aws s3api put-bucket-lifecycle-configuration --bucket my-lifecycle-bucket --lifecycle-configuration file://lifecycle.json

# 4. Check lifecycle policy
aws s3api get-bucket-lifecycle-configuration --bucket my-lifecycle-bucket
```

1. Create the `my-lifecycle-bucket` bucket.
2. Write a lifecycle policy to automatically transition objects to `STANDARD_IA` (infrequently accessed data storage class) after 30 days.
3. Apply the JSON file to S3 bucket settings.
4. Verify that the policy has been applied.

Through this, objects that are accessed less frequently automatically transition to cheaper storage classes, saving costs.

---

## **6. Closing?**

Amazon S3 is a powerful object storage service with **high availability, high durability, and unlimited scalability**. By strategically utilizing features from simple bucket creation to versioning, lifecycle management, and encryption, you can achieve both **stable data management and cost optimization**. With proper S3 usage, you can flexibly solve various problems including file hosting, backup and recovery, log archiving, static website hosting, and big data analysis staging!

---

### **Reference Materials and Sources**

- [AWS Official Documentation: Amazon S3](https://docs.aws.amazon.com/ko_kr/s3/index.html)
- [AWS CLI Reference](https://docs.aws.amazon.com/cli/latest/reference/s3/)
- [AWS SDK for Java Developer Guide](https://docs.aws.amazon.com/sdk-for-java/index.html)

Use Amazon S3 to easily and conveniently store and manage large volumes of data! Regardless of your project, you'll have a rapidly scalable backend storage infrastructure.
