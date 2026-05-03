---
title: "Creating an API with Next.js that connects to an RDBMS in AWS"
date: 2024-06-12T13:27:29+09:00
slug: "284-Creating-an-API-with-Next-js-that-connects-to-an-RDBMS-in-AWS"
original_url: "https://memoryhub.tistory.com/284"
tistory_id: 284
draft: false
---

*Creating an API with Next.js that connects to an RDBMS in AWS and is packaged to deploy on an AWS EC2 instance involves several steps, including setting up the project, connecting to the database, and deploying the application.*

---

### The Big Picture

Imagine you’re building a vending machine (your Next.js API) that needs to connect to a warehouse (your RDBMS in AWS) to check stock and prices. Once the vending machine is ready, you want to place it in a public location (deploy on AWS EC2) so people can use it.

---

### Core Concepts

1. **Next.js Setup**: Setting up a Next.js project to handle API requests.
2. **Database Integration**: Connecting the Next.js project to an AWS RDBMS.
3. **Deployment Preparation**: Packaging the application for deployment.
4. **AWS EC2 Deployment**: Deploying the application on an AWS EC2 instance.

---

### Detailed Walkthrough

#### 1. Next.js Setup

1. **Initialize Next.js Project**:

   - Open your terminal and run:

     ```
     npx create-next-app@latest my-api
     cd my-api
     ```
2. **Create API Routes**:

   - In your Next.js project, create a folder named `api` under `pages`:

     ```
     my-api
     └── pages
         └── api
     ```
   - Add an example API route by creating a file `hello.js` in the `api` folder:

     ```
     // pages/api/hello.js
     export default function handler(req, res) {
       res.status(200).json({ message: 'Hello, World!' });
     }
     ```

#### 2. Database Integration

1. **Set Up AWS RDS (Relational Database Service)**:

   - Go to the AWS Management Console and create a new RDS instance (e.g., MySQL, PostgreSQL).
   - Note the connection details: endpoint, username, password, and database name.
2. **Install Database Client**:

   - Depending on your database, install the corresponding client library:

     ```
     npm install mysql2  # For MySQL
     npm install pg  # For PostgreSQL
     ```
3. **Connect to the Database**:

   - Create a utility file to manage the database connection:

     ```
     // lib/db.js
     import mysql from 'mysql2/promise';
     // or for PostgreSQL: import { Pool } from 'pg';

     const pool = mysql.createPool({
       host: process.env.DB_HOST,
       user: process.env.DB_USER,
       password: process.env.DB_PASSWORD,
       database: process.env.DB_NAME,
     });

     export default pool;
     ```
   - Update your `.env.local` file with your database credentials:

     ```
     DB_HOST=your-db-endpoint
     DB_USER=your-db-username
     DB_PASSWORD=your-db-password
     DB_NAME=your-db-name
     ```
   - Modify an API route to query the database:

     ```
     // pages/api/hello.js
     import pool from '../../lib/db';

     export default async function handler(req, res) {
       const [rows] = await pool.query('SELECT * FROM your_table');
       res.status(200).json(rows);
     }
     ```

#### 3. Deployment Preparation

1. **Build the Application**:

   - Ensure your application is production-ready:

     ```
     npm run build
     ```
2. **Dockerize the Application (Optional but recommended)**:

   - Create a `Dockerfile` in the root of your project:

     ```
     # Use the official Next.js image
     FROM vercel/next:latest

     # Set working directory
     WORKDIR /app

     # Copy the project files
     COPY . .

     # Install dependencies
     RUN npm install

     # Build the project
     RUN npm run build

     # Expose the port the app runs on
     EXPOSE 3000

     # Start the application
     CMD ["npm", "start"]
     ```
   - Build the Docker image:

     ```
     docker build -t my-api .
     ```

#### 4. AWS EC2 Deployment

1. **Set Up an EC2 Instance**:

   - Go to the AWS Management Console, navigate to EC2, and launch a new instance.
   - Choose an appropriate Amazon Machine Image (AMI), e.g., Ubuntu.
   - Configure instance details, add storage, and configure security group to allow HTTP/HTTPS traffic.
2. **Install Docker on EC2**:

   - SSH into your EC2 instance and install Docker:

     ```
     sudo apt-get update
     sudo apt-get install docker.io
     ```
3. **Deploy the Docker Container**:

   - Transfer your Docker image to the EC2 instance (you can use Docker Hub or SCP for this).
   - Run your Docker container:

     ```
     sudo docker run -d -p 80:3000 my-api
     ```

---

### Understanding Through an Example

Let’s say your vending machine (API) needs to check if a snack (data) is in stock. Here’s how the process works:

1. **Customer Requests**: A user sends a request to the vending machine (Next.js API).
2. **Warehouse Check**: The vending machine queries the warehouse (AWS RDBMS) to check stock levels.
3. **Response**: The vending machine responds to the user with the availability of the snack.

---

### Conclusion and Summary

In summary, creating an API with Next.js that connects to an RDBMS in AWS and deploying it to an AWS EC2 instance involves:

1. Setting up the Next.js project with API routes.
2. Connecting the project to an AWS-hosted RDBMS.
3. Preparing the project for deployment, optionally using Docker.
4. Deploying the project on an AWS EC2 instance.

---

### Test Your Understanding

1. What command is used to initialize a new Next.js project?
2. How would you connect a Next.js API route to a PostgreSQL database hosted on AWS?
3. What are the benefits of Dockerizing your Next.js application before deployment?
4. What steps are necessary to deploy a Docker container on an AWS EC2 instance?

---

### Reference

- [Next.js Documentation](https://nextjs.org/docs)
- [AWS RDS Documentation](https://docs.aws.amazon.com/rds/index.html)
- [Docker Documentation](https://docs.docker.com/)
- [AWS EC2 Documentation](https://docs.aws.amazon.com/ec2/index.html)
