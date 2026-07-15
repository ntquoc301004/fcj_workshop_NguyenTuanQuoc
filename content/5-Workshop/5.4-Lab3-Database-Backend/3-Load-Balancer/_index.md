---
title: "3. Configure Load Balancer"
weight: 3
chapter: false
pre: " <b> 5.4.3. </b> "
---

# 3. Configure Load Balancer (ALB)

Because the EC2 Backend server resides in a **Private Subnet** (with no Public IP), frontend applications from the internet cannot call our APIs directly.

The AWS standard solution is to use an **Application Load Balancer (ALB)** placed in the Public Subnets. The ALB receives HTTP/HTTPS requests from the internet and securely "forwards" them to the EC2 instances inside.

## Step 1: Create a Target Group

A Target Group is a logical group containing the servers (EC2 instances) that the ALB will route traffic to.

1. Open the **EC2** console, scroll down the left menu to **Load Balancing**, and select **Target Groups**.
2. Click **Create target group**.
3. **Choose a target type**: Select **Instances**.
4. **Target group name**: `genzite-backend-tg`.
5. **Protocol**: `HTTP`. **Port**: `3000` (The port where NestJS is running).
6. **VPC**: Select `genzite-vpc`.
7. **Health checks**: Leave the defaults (Protocol: HTTP, Path: `/`).
   *(Note: Ensure your API has a route that returns a 200 status code at the root path `/` for the health check to pass).*
8. Click **Next**.
9. On the **Register targets** screen, select your `genzite-backend-ec2` instance from the list below.
10. Change the port to `3000` and click **Include as pending below**.
11. Scroll down and click **Create target group**.

## Step 2: Initialize the Application Load Balancer

1. In the left menu, select **Load Balancers**.
2. Click **Create load balancer**.
3. Under **Application Load Balancer**, click **Create**.
4. **Load balancer name**: `genzite-alb`.
5. **Scheme**: Select **Internet-facing** (Crucial: Allows the ALB to accept traffic from the internet).
6. **IP address type**: `IPv4`.
7. **Network mapping**:
   - **VPC**: Select `genzite-vpc`.
   - **Mappings**: Select at least 2 **Availability Zones** and their corresponding **Public Subnets** (ALBs must be placed in Public Subnets).
8. **Security groups**:
   - Remove the `default` group.
   - Select `genzite-alb-sg` (Created in Lab 1).
9. **Listeners and routing**:
   - **Protocol**: `HTTP`. **Port**: `80`.
   - **Default action**: Select the `genzite-backend-tg` Target group you just created.
10. Click **Create load balancer**.

## Step 3: Test the API Flow

Provisioning the ALB will take about 3-5 minutes (State changing from `Provisioning` to `Active`).

1. Once the ALB is `Active`, click on the name `genzite-alb`.
2. Copy the **DNS name** of the ALB (e.g., `genzite-alb-123456789.us-east-1.elb.amazonaws.com`).
3. Paste this DNS name into your browser (Make sure to use `http://` instead of `https://`).
4. If the screen returns a JSON response from your API, congratulations! The ALB has successfully routed the request from the Internet straight to the EC2 instance in the Private Subnet.

## Step 4: Update Environment Variables on Frontend

The final step of this Lab is to update the API URL on your Frontend app.

1. Open the `.env` file in your Frontend project.
2. Add a variable containing the ALB URL (Don't forget the `http://`):
   ```env
   VITE_API_BASE_URL=http://genzite-alb-123456789.us-east-1.elb.amazonaws.com
   ```
3. After updating, remember to run `npm run build` and re-deploy the Frontend to S3 if necessary.

---
**Lab 3 Complete!** You now possess a fully functional Backend infrastructure consisting of a secure Database, a protected EC2 server, and an intelligent ALB router. Let's head over to **Lab 4** to integrate artificial intelligence (Gemini API) using an asynchronous mechanism.
