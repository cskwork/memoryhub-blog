---
title: "Amazon CloudFront Introduced"
date: 2024-05-29T08:00:47+09:00
slug: "157-Amazon-CloudFront-Introduced"
original_url: "https://memoryhub.tistory.com/157"
tistory_id: 157
draft: false
---

*Amazon CloudFront is a content delivery network (CDN) service that accelerates the delivery of your web content to users across the globe by caching copies of your content at edge locations closer to them.*

### The Big Picture

Imagine you have a bakery in a small town, and your delicious pastries are popular all over the world. Instead of making everyone travel to your town to get your pastries, you set up small local bakeries in major cities around the world. Each local bakery keeps a stock of your most popular pastries, so customers can get their treats faster without having to wait for shipping from the main bakery. This is essentially what Amazon CloudFront does for your web content.

### Core Concepts

1. **Edge Locations**: Data centers located around the world where CloudFront caches copies of your content.
2. **Distributions**: A distribution is the configuration you set up to tell CloudFront which content to deliver and from where.
3. **Origins**: The source of your content, such as an S3 bucket, an HTTP server, or an Amazon EC2 instance.
4. **Caching**: Temporarily storing copies of your content at edge locations to reduce latency.
5. **Latency**: The delay before a transfer of data begins following an instruction for its transfer.
6. **TTL (Time to Live)**: The duration for which content is cached at edge locations.

### Detailed Walkthrough

**1. Edge Locations:**  
Edge locations are strategically placed data centers around the globe. When a user requests content, CloudFront delivers it from the nearest edge location, reducing latency and improving load times. Think of these as the local bakeries that stock your pastries.

**2. Distributions:**  
A distribution is the setup that defines how to deliver your content. There are two types:

- **Web Distributions**: Used for websites.
- **RTMP Distributions**: Used for streaming media using Adobe Flash Media Server’s RTMP protocol.

**3. Origins:**  
The origin is where CloudFront fetches your original content when it's not in the cache. This could be an S3 bucket, an EC2 instance, or any other web server. This is like your main bakery where all the pastries are initially made.

**4. Caching:**  
CloudFront caches copies of your content at edge locations. When a user requests your content, CloudFront checks if it’s already cached. If it is, CloudFront serves it directly from the edge location, reducing the need to fetch it from the origin server. This speeds up content delivery significantly. It's like having your pastries ready at the local bakery, so customers don’t have to wait for them to be shipped from the main bakery.

**5. Latency:**  
Latency refers to the delay before data begins to transfer. By delivering content from the nearest edge location, CloudFront minimizes latency, much like how having local bakeries reduces the wait time for customers.

**6. TTL (Time to Live):**  
TTL determines how long content is cached at edge locations before CloudFront checks back with the origin server for updates. Setting an appropriate TTL is crucial for balancing freshness of content with performance. It's like deciding how often you need to restock your local bakeries with fresh pastries from the main bakery.

### Understanding Through an Example

Suppose you run a popular e-commerce website. Your site includes images, videos, and static files (like CSS and JavaScript). You use Amazon CloudFront to distribute this content globally. You create a web distribution with your S3 bucket as the origin. When a user in Japan visits your site, CloudFront delivers the content from the nearest edge location in Tokyo, ensuring faster load times. If the content isn’t already cached there, CloudFront fetches it from your S3 bucket and caches it for future requests.

### Conclusion and Summary

Amazon CloudFront is a content delivery network (CDN) that helps speed up the distribution of your web content by caching it at edge locations around the world. By reducing latency and improving load times, CloudFront enhances the user experience for your global audience.

### Test Your Understanding

1. What is an edge location in Amazon CloudFront?
2. Explain the difference between a web distribution and an RTMP distribution.
3. How does caching improve the performance of content delivery?
4. What is TTL, and why is it important in CloudFront?

### Reference

For further reading and detailed documentation, refer to the [Amazon CloudFront Documentation](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html).
