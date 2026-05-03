---
title: "12 Factor App"
date: 2024-06-11T18:16:56+09:00
slug: "270-12-Factor-App"
original_url: "https://memoryhub.tistory.com/270"
tistory_id: 270
draft: false
---

*The Twelve-Factor App methodology offers detailed principles for developing robust, scalable, and maintainable applications, crucial for cloud-native environments.*

### The Big Picture

The Twelve-Factor App outlines a set of best practices for building web applications. These principles ensure that apps are scalable, maintainable, and portable, suitable for deployment on modern cloud platforms.

### Core Concepts

1. **Codebase**: A single codebase tracked in version control with multiple deployments.
2. **Dependencies**: Explicitly declare and isolate dependencies using a dependency manager.
3. **Config**: Store configuration in the environment, separating it from code.
4. **Backing Services**: Treat backing services like databases and caches as attached resources.
5. **Build, Release, Run**: Separate build and run stages to ensure stability and repeatability.
6. **Processes**: Execute the app as one or more stateless processes.
7. **Port Binding**: Export services via port binding, making the app self-contained.
8. **Concurrency**: Scale out via the process model, allowing easy horizontal scaling.
9. **Disposability**: Maximize robustness with fast startup and graceful shutdown.
10. **Dev/Prod Parity**: Keep development, staging, and production as similar as possible.
11. **Logs**: Treat logs as event streams for better monitoring and analysis.
12. **Admin Processes**: Run admin or management tasks as one-off processes.

### Detailed Walkthrough

#### Codebase

- **Concept**: Use a single codebase per app, tracked in a version control system like Git. This codebase can be deployed in multiple environments (e.g., production, staging).
- **Example**: A Git repository with branches for different stages of development.

#### Dependencies

- **Concept**: Declare dependencies explicitly in a dependency declaration file (e.g., `requirements.txt` for Python or `package.json` for Node.js).
- **Example**: A `requirements.txt` file listing all required Python packages ensures anyone can set up the environment quickly.

#### Config

- **Concept**: Store configuration details in the environment, keeping them separate from the codebase.
- **Example**: Using environment variables to store database connection strings and API keys.

#### Backing Services

- **Concept**: Treat services such as databases and message queues as attached resources, which can be swapped without changing the code.
- **Example**: Connecting to a cloud database like AWS RDS using environment variables.

#### Build, Release, Run

- **Concept**: Separate the build, release, and run stages of the deployment process.
- **Example**: Using a CI/CD pipeline to automate the build and deployment process.

#### Processes

- **Concept**: Run the application as one or more stateless processes that share nothing.
- **Example**: A web application running multiple instances of stateless processes on a cloud platform like Heroku.

#### Port Binding

- **Concept**: Export the service via a port, making the app self-contained and easy to run.
- **Example**: A web server listening on a specific port, accessible through a URL.

#### Concurrency

- **Concept**: Scale out the application by running multiple instances of processes.
- **Example**: Using Kubernetes to scale application instances based on traffic.

#### Disposability

- **Concept**: Optimize for fast startup and graceful shutdown to improve resilience.
- **Example**: Using Docker containers that can start quickly and terminate gracefully.

#### Dev/Prod Parity

- **Concept**: Ensure the development, staging, and production environments are as similar as possible.
- **Example**: Using Docker to create consistent development environments.

#### Logs

- **Concept**: Treat logs as event streams that can be aggregated and analyzed.
- **Example**: Sending application logs to a logging service like ELK Stack for centralized analysis.

#### Admin Processes

- **Concept**: Run administrative tasks as one-off processes.
- **Example**: Running database migrations using a command-line tool.

### Understanding Through an Example

Imagine developing a photo-sharing app:

- **Codebase**: Use Git for version control.
- **Dependencies**: Use a `package.json` file for Node.js dependencies.
- **Config**: Store database credentials in environment variables.
- **Backing Services**: Connect to cloud storage services for storing photos.
- **Build, Release, Run**: Use Jenkins for CI/CD pipelines.
- **Processes**: Deploy stateless application processes on AWS Lambda.
- **Port Binding**: Bind the application to port 3000.
- **Concurrency**: Scale the application using AWS Auto Scaling.
- **Disposability**: Use lightweight Docker containers for deployment.
- **Dev/Prod Parity**: Use Docker Compose for local development to mirror production.
- **Logs**: Stream logs to AWS CloudWatch for monitoring.
- **Admin Processes**: Perform database backups using scheduled Lambda functions.

### Conclusion and Summary

The Twelve-Factor App methodology provides a framework for developing applications that are scalable, maintainable, and portable across different environments. By adhering to these principles, developers can build robust and efficient web applications.

### Test Your Understanding

1. Why is it important to separate configuration from code?
2. How does treating backing services as attached resources enhance flexibility?
3. What are the benefits of having stateless processes in an application?

### Reference

For more detailed information, visit the [official Twelve-Factor App website](https://12factor.net/).
