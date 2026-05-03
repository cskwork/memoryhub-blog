---
title: "Create a sample AWS Batch"
date: 2024-06-07T21:12:09+09:00
slug: "212-Create-a-sample-AWS-Batch"
original_url: "https://memoryhub.tistory.com/212"
tistory_id: 212
draft: false
categories: ["Dev AWS"]
---

*Here's a detailed example of setting up and submitting a batch processing job in AWS Batch.*

### Setting Up a Sample Batch Processing Job

#### Step 1: Create a Compute Environment

First, you need to create a compute environment where your batch jobs will run.

```
aws batch create-compute-environment \
    --compute-environment-name MyComputeEnvironment \
    --type MANAGED \
    --compute-resources type=EC2,allocationStrategy=BEST_FIT,instanceTypes=m4.large,minvCpus=0,maxvCpus=16,desiredvCpus=8,subnets=subnet-12345678,securityGroupIds=sg-12345678,instanceRole=ecsInstanceRole
```

#### Step 2: Create a Job Queue

Next, create a job queue to hold your batch jobs.

```
aws batch create-job-queue \
    --job-queue-name MyJobQueue \
    --state ENABLED \
    --priority 1 \
    --compute-environment-order order=1,computeEnvironment=MyComputeEnvironment
```

#### Step 3: Create a Job Definition

Define the job properties such as the Docker image to use, vCPU, memory, and the command to execute. This example uses a simple Python script to process data.

**Sample Python Script (`process_data.py`):**

```
# process_data.py
import sys

def process_data():
    # Simulate data processing
    print("Processing data...")
    # Example: read input, process it and produce output
    # Here we'll just print the command line arguments
    print("Arguments passed to the script:", sys.argv[1:])

if __name__ == "__main__":
    process_data()
```

**Dockerfile:**

```
# Dockerfile
FROM python:3.8-slim

# Copy the process_data.py script into the container
COPY process_data.py /usr/src/app/process_data.py

# Set the working directory
WORKDIR /usr/src/app

# Command to run the script
CMD ["python", "process_data.py"]
```

**Build and Push Docker Image:**

```
# Build the Docker image
docker build -t mybatchjob:latest .

# Tag the image for Amazon ECR (Replace  and  with your AWS account ID and region)
docker tag mybatchjob:latest .dkr.ecr..amazonaws.com/mybatchjob:latest

# Push the image to Amazon ECR
$(aws ecr get-login --no-include-email --region )
docker push .dkr.ecr..amazonaws.com/mybatchjob:latest
```

**Register Job Definition:**

```
aws batch register-job-definition \
    --job-definition-name MyJobDefinition \
    --type container \
    --container-properties image=.dkr.ecr..amazonaws.com/mybatchjob:latest,vcpus=2,memory=2000,command=["python","process_data.py","arg1","arg2"]
```

#### Step 4: Submit a Job

Submit the job to the job queue for execution.

```
aws batch submit-job \
    --job-name MyFirstBatchJob \
    --job-queue MyJobQueue \
    --job-definition MyJobDefinition
```

### Monitoring and Managing the Job

You can monitor and manage your job using the AWS Management Console or AWS CLI.

```
# List Jobs in the Queue
aws batch list-jobs --job-queue MyJobQueue --job-status RUNNING

# Describe a Specific Job
aws batch describe-jobs --jobs
```

### Conclusion

This example shows how to set up a simple batch processing job using AWS Batch. You can extend this approach to more complex batch processing tasks by modifying the Python script and Dockerfile accordingly.

### Next Steps

- Explore advanced configurations such as job dependencies and retries.
- Integrate AWS Batch with other AWS services like Amazon S3 for input/output data storage.
- Automate job submission and monitoring using AWS Lambda or other orchestration tools.
