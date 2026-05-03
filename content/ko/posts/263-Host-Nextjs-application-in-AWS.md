---
title: "Host Nextjs application in AWS"
date: 2024-06-11T15:51:57+09:00
slug: "263-Host-Nextjs-application-in-AWS"
original_url: "https://memoryhub.tistory.com/263"
tistory_id: 263
draft: false
---

*To host a Next.js application on AWS S3, you'll use S3 for static hosting, CloudFront for CDN, and Route 53 for DNS management, ensuring a scalable and performant setup.*

### The Big Picture

Hosting a Next.js application on AWS S3 is akin to setting up a library where books (your static files) are neatly organized for easy access. S3 is the bookshelf storing your files, CloudFront is the librarian who helps distribute books efficiently, and Route 53 is the address sign guiding visitors to the library.

### Core Concepts

1. **S3 (Simple Storage Service)**: Stores and serves static files (HTML, CSS, JS).
2. **CloudFront**: A CDN to deliver content with low latency.
3. **Route 53**: DNS web service to route users to your application.

### Detailed Walkthrough

#### Step 1: Preparing Your Next.js Application

1. **Build Your Next.js Application**:

   - Ensure your `next.config.js` is configured for static export.

     ```
     module.exports = {
       output: 'export',
     }
     ```
   - Build and export your application.

     ```
     npm run build
     npm run export
     ```
2. **Resulting Files**:

   - This will generate a `out` directory containing your static files.

#### Step 2: Setting Up S3

1. **Create an S3 Bucket**:

   - Go to the S3 console.
   - Click "Create bucket" and follow the prompts to create a new bucket. Ensure it is publicly accessible.
2. **Upload Your Files**:

   - Upload the contents of the `out` directory to your S3 bucket.
   - Set proper permissions so the files can be publicly read.
3. **Configure Static Website Hosting**:

   - In your bucket properties, enable static website hosting.
   - Specify the `index.html` as the index document and `404.html` for error documents if needed.

#### Step 3: Configuring CloudFront

1. **Create a CloudFront Distribution**:

   - Go to the CloudFront console.
   - Create a new distribution and set your S3 bucket as the origin.
2. **Distribution Settings**:

   - Ensure the viewer protocol policy is set to redirect HTTP to HTTPS.
   - Configure caching settings according to your needs.
3. **Update S3 Bucket Policy**:

   - Update your S3 bucket policy to allow CloudFront to access your bucket.

#### Step 4: Setting Up Route 53

1. **Create a Hosted Zone**:

   - In Route 53, create a hosted zone for your domain.
2. **Create DNS Records**:

   - Add an A record (or CNAME) pointing to your CloudFront distribution.

### Understanding Through an Example

1. **Build and Export**:

   - Run `npm run build` and `npm run export` in your Next.js project.
   - Ensure all static files are generated in the `out` directory.
2. **Upload to S3**:

   - Create an S3 bucket named `my-nextjs-app`.
   - Upload all files from the `out` directory to the S3 bucket.
3. **CloudFront Distribution**:

   - Create a CloudFront distribution with the origin set to your S3 bucket `my-nextjs-app`.
   - Configure caching and SSL settings.
4. **Route 53 Setup**:

   - Create a hosted zone for `example.com`.
   - Add an A record pointing to the CloudFront distribution.

### Conclusion and Summary

Hosting a Next.js application on AWS S3 involves building and exporting your Next.js project to generate static files, which are then uploaded to an S3 bucket. CloudFront is configured to serve these files efficiently, and Route 53 manages the DNS settings to direct traffic to your application.

### Test Your Understanding

1. What steps are involved in preparing a Next.js application for static hosting?
2. How do you configure CloudFront to serve content from an S3 bucket?
3. What role does Route 53 play in hosting a Next.js application on S3?

### Reference

- [Next.js Static HTML Export](https://nextjs.org/docs/advanced-features/static-html-export)
- [AWS S3 Static Website Hosting](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
- [AWS CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
- [AWS Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html)
