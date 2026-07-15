---
title: "3. Deploy Frontend"
weight: 3
chapter: false
pre: " <b> 5.2.3. </b> "
---

# 3. Deploy Frontend (S3 & CloudFront)

In this section, we will deploy the frontend application (built with React/Vite) to AWS in an optimized manner: using Amazon S3 to store static files and Amazon CloudFront as a CDN (Content Delivery Network) to accelerate global load times and secure the data.

## Step 1: Initialize S3 Bucket

S3 will store the compiled source code (`index.html`, `.js`, `.css`).

1. Open the **S3** service in the AWS Console.
2. Click **Create bucket**.
3. **Bucket name**: Enter a globally unique name (e.g., `genzite-frontend-bucket-yourname`).
4. **AWS Region**: Select `us-east-1` (US East N. Virginia).
5. **Object Ownership**: Leave it as *ACLs disabled*.
6. **Block Public Access settings for this bucket**: Keep **Block all public access** checked.
   *(Note: Following Best Practices, we do not make the S3 bucket public; instead, we grant access exclusively via CloudFront).*
7. Leave other settings as default and click **Create bucket**.

## Step 2: Build and Upload Frontend Source Code

Assuming you have the Genzite Frontend source code ready on your local machine.

1. Open a terminal and navigate to the Frontend code directory.
2. Run the build command for the React/Vite app:
   ```bash
   npm install
   npm run build
   ```
3. Once completed, a `dist` (or `build`) folder will be generated.
4. Go back to the AWS S3 console, and click on your newly created bucket.
5. Click **Upload**, then drag and drop all files/folders **inside** the `dist` directory.
6. Click **Upload** and wait for the process to finish.

## Step 3: Configure CloudFront with OAC

To allow users to access the website quickly, we will create a CloudFront Distribution and configure **Origin Access Control (OAC)**. OAC ensures that only CloudFront has permission to read files from the S3 bucket.

1. Open the **CloudFront** service in the AWS Console.
2. Click **Create a CloudFront distribution**.
3. **Origin domain**: Click the input box and select your newly created S3 bucket.
4. **Origin access**: Select **Origin access control settings (recommended)**.
   - Click the **Create control setting** button, keep the default configuration, and click **Create**.
5. Scroll down to the **Default cache behavior** section:
   - **Viewer protocol policy**: Select **Redirect HTTP to HTTPS** (to enforce secure connections).
6. Scroll down to the **Web Application Firewall (WAF)** section:
   - Select **Do not enable security protections** (to save costs for this Lab).
7. Scroll to the bottom and click **Create distribution**.

## Step 4: Update S3 Bucket Policy

After creating the Distribution, a yellow banner will appear prompting you to update the S3 bucket policy to allow CloudFront OAC access.

1. Click the **Copy policy** button.
2. Click the link `Go to S3 bucket permissions` provided in the banner.
3. Scroll down to the **Bucket policy** section and click **Edit**.
4. Paste the JSON you just copied. It should look something like this:
   ```json
   {
       "Version": "2012-10-17",
       "Statement": {
           "Sid": "AllowCloudFrontServicePrincipalReadOnly",
           "Effect": "Allow",
           "Principal": {
               "Service": "cloudfront.amazonaws.com"
           },
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::genzite-frontend-bucket-yourname/*",
           "Condition": {
               "StringEquals": {
                   "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7"
               }
           }
       }
   }
   ```
5. Click **Save changes**.

## Step 5: Verify the Result

Return to the CloudFront Distribution details page.
1. Copy the **Distribution domain name** (it looks like `d1234abcd.cloudfront.net`).
2. Open a web browser and paste this link.
3. Wait a few minutes for the Distribution status to change from `Deploying` to complete. You should then see the Genzite web interface!

---
**Lab 1 Complete!** The fundamental infrastructure of our system is now in place. Let's move on to Lab 2 to build the Authentication features for our users.
