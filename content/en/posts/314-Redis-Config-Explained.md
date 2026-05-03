---
title: "Redis Config Explained"
date: 2024-06-24T16:19:01+09:00
slug: "314-Redis-Config-Explained"
original_url: "https://memoryhub.tistory.com/314"
tistory_id: 314
draft: false
---

# RedisConfig.java

### Key Components and Their Functions:

1. **Redis Configuration Class (`RedisConfig`):**

   - This class is annotated with `@Configuration` to indicate that it defines beans for Spring's application context.
   - It uses `@RequiredArgsConstructor` to generate a constructor with required arguments, i.e., the dependencies.
2. **Redis Connection Factory (`redisConnectionFactory`):**

   - Determines the type of Redis connection (single, sentinel, cluster) based on properties fetched from the environment or a database.
   - Creates appropriate connection factory objects using `LettuceConnectionFactory`.
3. **Redis Templates (`redisTemplate`, `strRedisTemplate`):**

   - These beans provide Redis operations with different serializers, specifically `StringRedisSerializer` for string serialization.
4. **Redis Message Listener Container (`redisContainer`):**

   - Configures a container for handling pub/sub operations in Redis.
5. **Helper Methods:**

   - `fetchRedisProperties()`, `getPropertyValue()`, `getBooleanPropertyValue()`: Methods to fetch Redis configuration properties.
   - `createSentinelConnectionFactory()`, `createClusterConnectionFactory()`, `createSingleNodeConnectionFactory()`: Methods to create different types of Redis connection factories.
   - `configureSerializers()`: Method to configure serializers for the Redis template.
6. **RedisProperties Inner Class:**

   - A static inner class to encapsulate Redis properties needed for configuration.

### Summary:

The `RedisConfig` class is responsible for configuring Redis connections and templates based on settings fetched from the environment or a database.  
It supports multiple Redis modes (single, sentinel, cluster) and configures the appropriate connection factory for each mode.  
Additionally, it sets up templates for Redis operations and a container for pub/sub messaging, ensuring that the application can interact with Redis efficiently and securely.

### Detailed Explanation: Determining the Type of Redis Connection

The `RedisConfig` class in the provided code determines the type of Redis connection (single, sentinel, cluster) based on properties fetched from either the environment or a database. Here's a more detailed breakdown of how this process works:

1. **Fetching Redis Properties:**

   - The method `fetchRedisProperties()` is responsible for gathering all necessary Redis configuration properties. It uses a combination of environment variables and values stored in a database.
   - Environment variables are accessed through the `Environment` object.
   - Database values are fetched using the `SysPropRepository` to retrieve properties stored in the `SysProp` entity.
2. **Properties Involved:**

   - **`redisMode`**: Determines the mode of Redis (single, sentinel, or cluster).
   - **`addressDelim`**: Delimiter used to separate addresses in the hostPorts string.
   - **`accessDelimType`**: Type of delimiter used (e.g., comma, semicolon).
   - **`hostPorts`**: Contains the host and port information for Redis nodes.
   - **`user`**: Username for Redis authentication.
   - **`password`**: Password for Redis authentication.
   - **`tls`**: Indicates if TLS should be used.
   - **`ssl`**: Indicates if SSL should be used.
3. **Parsing Host and Port Information:**

   - The `hostPorts` string is split into arrays of hosts and ports using the specified delimiter.
   - For example, if `hostPorts` is `host1:6379,host2:6379` and the delimiter is a comma, it will be split into `["host1:6379", "host2:6379"]`.
4. **Creating Connection Factories:**

   - Based on the `redisMode`, different methods are called to create the appropriate connection factory:
     - **Single Node:** If the mode is `single`, the `createSingleNodeConnectionFactory` method is called.
     - **Sentinel Mode:** If the mode is `sentinel`, the `createSentinelConnectionFactory` method is called.
     - **Cluster Mode:** If the mode is `cluster`, the `createClusterConnectionFactory` method is called.
5. **Creating Single Node Connection Factory:**

   - The `createSingleNodeConnectionFactory` method creates a `LettuceConnectionFactory` configured for a single Redis node using the host and port from the `hostPorts` array.
   - Additional properties like `password`, `tls`, and `ssl` are also set.
6. **Creating Sentinel Connection Factory:**

   - The `createSentinelConnectionFactory` method creates a `RedisSentinelConfiguration` and configures it with sentinel nodes from the `hostPorts` array.
   - A `LettuceConnectionFactory` is then created with this sentinel configuration.
7. **Creating Cluster Connection Factory:**

   - The `createClusterConnectionFactory` method creates a `RedisClusterConfiguration` and configures it with cluster nodes from the `hostPorts` array.
   - A `LettuceConnectionFactory` is then created with this cluster configuration.
   - Additional properties like `password`, `tls`, and `ssl` are also set.

### Example Breakdown

Here's a simplified example to illustrate the process:

- Suppose we have the following properties:
  - `redisMode`: `cluster`
  - `hostPorts`: `host1:6379,host2:6379`
  - `accessDelimType`: `,`
  - `password`: `mypassword`
  - `tls`: `true`
  - `ssl`: `false`

1. **Fetching Properties:**

   - These properties are fetched from the environment or database.
2. **Parsing Host and Port:**

   - `hostPorts` is split into `["host1:6379", "host2:6379"]`.
3. **Creating Cluster Connection Factory:**

   - The `createClusterConnectionFactory` method is called with the parsed host and port arrays.
   - It creates a `RedisClusterConfiguration` and adds nodes `host1:6379` and `host2:6379`.
   - A `LettuceConnectionFactory` is created with the cluster configuration, and properties like `password`, `tls`, and `ssl` are set accordingly.

### Summary

The `RedisConfig` class dynamically determines and configures the type of Redis connection required based on properties. This allows the application to be flexible and adapt to different Redis deployment modes (single, sentinel, cluster) without changing the code, only by updating the configuration properties. This approach ensures scalability and adaptability in different environments.

### Difference Between Single, Sentinel, and Cluster Redis Deployments

Redis can be deployed in different configurations to meet various needs such as availability, fault tolerance, and scalability. The three primary deployment modes are single, sentinel, and cluster. Here's a detailed explanation of each:

#### 1. Single Node Deployment

- **Description**: In a single node deployment, Redis runs on a single server. This is the simplest and most straightforward configuration.
- **Use Case**: Suitable for development, testing, or small applications where high availability and fault tolerance are not critical.
- **Advantages**:
  - Simple to set up and manage.
  - No additional configuration required for replication or clustering.
- **Disadvantages**:
  - Single point of failure: If the server goes down, the Redis service becomes unavailable.
  - Limited scalability: All data is stored on a single server, which may become a bottleneck as the data grows.

#### 2. Sentinel Deployment

- **Description**: Redis Sentinel provides high availability by monitoring Redis instances, promoting a replica to master in case of a failure, and providing automated failover.
- **Components**:
  - **Master**: The main Redis instance that handles all writes.
  - **Slaves**: Replica instances that replicate data from the master.
  - **Sentinels**: Special instances that monitor the master and slaves, detect failures, and initiate failover.
- **Use Case**: Suitable for applications requiring high availability and automatic failover.
- **Advantages**:
  - Automatic failover: If the master goes down, a slave is promoted to master automatically.
  - Monitoring: Sentinels continuously monitor the health of Redis instances.
- **Disadvantages**:
  - Configuration complexity: Requires careful configuration and management of sentinel instances.
  - Limited scalability: Does not support horizontal scaling (sharding) like Redis Cluster.

#### 3. Cluster Deployment

- **Description**: Redis Cluster provides horizontal scaling by partitioning data across multiple Redis nodes (sharding). It also offers high availability through replication and automatic failover.
- **Components**:
  - **Masters**: Nodes that handle specific portions (shards) of the data.
  - **Slaves**: Replica nodes that replicate data from the master nodes.
- **Use Case**: Suitable for applications requiring high availability, fault tolerance, and horizontal scalability.
- **Advantages**:
  - Horizontal scaling: Data is distributed across multiple nodes, allowing the cluster to handle large datasets and high throughput.
  - High availability: Automatic failover with replicas.
  - No single point of failure: Data is distributed, reducing the impact of a single node failure.
- **Disadvantages**:
  - Configuration complexity: More complex to set up and manage compared to single node and sentinel deployments.
  - Operational complexity: Requires careful management of cluster nodes and shards.

### Summary

- **Single Node**: Simple setup, no high availability, suitable for small or development environments.
- **Sentinel**: Provides high availability and automatic failover, suitable for applications needing reliability without the need for horizontal scaling.
- **Cluster**: Offers high availability, fault tolerance, and horizontal scalability, suitable for large-scale applications with high availability and performance requirements.

Each deployment mode serves different needs, and the choice depends on the specific requirements of your application, including availability, fault tolerance, scalability, and complexity of management.
