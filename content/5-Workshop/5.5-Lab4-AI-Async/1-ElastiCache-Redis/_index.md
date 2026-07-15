---
title: "1. Initialize ElastiCache"
weight: 1
chapter: false
pre: " <b> 5.5.1. </b> "
---

# 1. Initialize ElastiCache Redis

To run BullMQ (a robust Message Queue library for Node.js), we need a Redis server. In the AWS ecosystem, the most optimal service is **Amazon ElastiCache for Redis**.

Similar to the Database, Redis must also be placed securely in a **Private Subnet**. The EC2 Backend will push "Jobs" (website generation requests) into Redis, and the AI Worker (running on the same EC2 or a different one) will pull Jobs from Redis for processing.

## Step 1: Create a Subnet Group for Redis

1. Open the **ElastiCache** service in the AWS Console.
2. From the left menu under Network and Security, select **Subnet groups**.
3. Click **Create subnet group**.
4. **Name**: `genzite-redis-subnet-group`.
5. **Description**: `Subnet group for Redis in Private Subnet`.
6. **VPC ID**: Select `genzite-vpc`.
7. Under **Availability Zones**, choose the AZs you used in Lab 1.
8. Under **Subnets**, check the boxes for the **Private Subnets** (Carefully check the CIDR blocks to avoid selecting Public Subnets).
9. Click **Create**.

## Step 2: Provision Redis Cluster

1. From the left menu, select **Redis clusters**.
2. Click **Create Redis cluster**.
3. **Choose a cluster creation method**: Select **Design your own cache** and **Cluster cache**.
4. **Cluster mode**: Ensure **Disabled** is selected (BullMQ works best on single-node or master-replica setups without cluster mode enabled).
5. **Cluster info**:
   - **Name**: `genzite-redis`.
   - **Description**: `Redis for BullMQ`.
   - **Location**: Select **AWS Cloud** -> **Multi-AZ**: Uncheck (to save costs for the lab).
6. **Node type**:
   - Select the smallest instance type available, such as `cache.t4g.micro` or `cache.t3.micro`.
   - **Number of replicas**: `0` (Run a single node for this MVP Lab).
7. **Subnet group**:
   - Choose **Choose an existing subnet group**.
   - Select the `genzite-redis-subnet-group` you just created.
8. Click **Next**.
9. **Advanced settings** (Next page):
   - **Security**: Select the VPC Security Group of the EC2 `genzite-ec2-sg` (or preferably, create a dedicated SG for Redis that allows port 6379 from the EC2's SG). *Best Practice: Go to EC2 Security Groups, create `genzite-redis-sg` allowing port 6379 from `genzite-ec2-sg`.*
   - Scroll down and uncheck **Enable automatic backups** to optimize costs.
10. Click **Next**, review the configuration, and click **Create**.

## Step 3: Retrieve the Primary Endpoint

Creating the Redis Cluster takes about 3-5 minutes.

1. Once the status changes to `Available`, click on the name `genzite-redis`.
2. Copy the address under **Primary endpoint** (e.g., `genzite-redis.xxxxxx.0001.use1.cache.amazonaws.com:6379`).

You will need this address to add to the environment variables of the EC2 Backend in the next step.
