---
title: "2. Deploy Backend"
weight: 2
chapter: false
pre: " <b> 5.4.2. </b> "
---


For the Genzite application to process complex requests (generating JSON from prompts, interacting with the Database), we need a Virtual Machine. In AWS, this is the **Amazon Elastic Compute Cloud (EC2)** service.

Based on our design, the EC2 instance will be placed in a **Private Subnet** to hide it from the internet, only allowing traffic routed through the Application Load Balancer (ALB).

## Step 1: Launch the EC2 Instance

1. Open the **EC2** service in the AWS Console.
2. Click **Launch instances**.
3. **Name**: Enter `genzite-backend-ec2`.
4. **Application and OS Images (Amazon Machine Image)**:
   - Select **Amazon Linux 2023 AMI** (Free tier eligible).
   - *Note:* Choose the **64-bit (Arm)** architecture to utilize cost-effective Graviton chips.
5. **Instance type**:
   - Select `t4g.small` (Since running Node.js/NestJS requires decent memory, t4g.small offers better stability than a micro instance).
6. **Key pair (login)**:
   - Select **Proceed without a key pair** (We will use AWS Systems Manager - Session Manager for secure access instead of SSH keys).
7. **Network settings**:
   - Click **Edit**.
   - **VPC**: Select `genzite-vpc`.
   - **Subnet**: Select a **Private Subnet** (e.g., `genzite-private-subnet-1a`).
   - **Auto-assign public IP**: **Disable** (Mandatory to ensure the server is not exposed to the Internet).
   - **Firewall (security groups)**: Choose **Select existing security group**, then select `genzite-ec2-sg` (Created in Lab 1).
8. **Configure storage**:
   - Leave default `8 GiB` gp3.
9. Expand the **Advanced details** section:
   - Scroll down to **IAM instance profile**: Select `genzite-ec2-role` (The role created in Lab 1 allows EC2 to call AWS services and enables Session Manager).
10. Click **Launch instance**.

## Step 2: Connect to EC2 via Session Manager

Because the EC2 is in a Private Subnet without a Public IP, direct SSH is impossible. We will use the Session Manager feature.

1. Wait for the EC2 state to change to **Running** and **Status check** to show *2/2 checks passed*.
2. Check the box next to `genzite-backend-ec2`, and click the **Connect** button at the top.
3. Switch to the **Session Manager** tab.
4. Click **Connect**. A black terminal window will open directly in your browser.

## Step 3: Set up the Environment (Node.js & PM2)

In the Session Manager terminal, execute the following commands to prepare the backend runtime:

```bash
# Update system packages
sudo dnf update -y

# Install Node.js (version 18 or 20)
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo dnf install -y nodejs

# Verify versions
node -v
npm -v

# Install PM2 (Process Manager to keep the app running)
sudo npm install pm2 -g
```

## Step 4: Download Source Code and Configure Environment Variables (.env)

Next, clone the source code (if using git) or create a dummy backend folder:

```bash
# Assuming you clone from github (Replace with your actual repo link)
git clone https://github.com/your-repo/genzite-backend.git
cd genzite-backend

# Or create an empty folder to test if you don't have the source code:
# mkdir genzite-backend && cd genzite-backend && npm init -y && npm install express
```

Create an environment variable file to connect to the RDS Database created in Step 1.

```bash
nano .env
```
Enter the following information (adjust to match your RDS and Cognito details):
```env
# Database RDS
DB_HOST=genzite-db.xxxxxxxxx.us-east-1.rds.amazonaws.com
DB_PORT=5432
DB_USERNAME=postgres
DB_PASSWORD=GenziteDBPass123!
DB_DATABASE=genzite

# AWS Cognito (From Lab 2)
COGNITO_USER_POOL_ID=us-east-1_xxxxxxxxx
COGNITO_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxx
AWS_REGION=us-east-1

# App Port
PORT=3000
```
Press `Ctrl + O` -> `Enter` to save the file, then `Ctrl + X` to exit.

## Step 5: Run the Backend Application

Install necessary libraries and start the API:

```bash
# Install dependencies
npm install

# Build code (If it's a NestJS/TypeScript project)
npm run build

# Run the app in the background with PM2
pm2 start dist/main.js --name "genzite-api"
```

Verify if the app is running correctly on port 3000:
```bash
curl http://localhost:3000/
```
*(If the terminal returns an output or a JSON error message, your application has started successfully).*

---
Currently, the API is running well inside the EC2 server. But how can the Frontend from the public Internet call this API? Let's move to the next step: **Configure the Load Balancer**.
