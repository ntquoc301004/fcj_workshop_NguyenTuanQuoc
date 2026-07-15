---
title: "Lab 2: Authentication with Cognito"
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# Lab 2: Authentication with Cognito

Welcome to **Lab 2**. In this module, we will build an identity management and access control system for our application users using **Amazon Cognito**.

## Overview

Most real-world applications require features like sign-up, sign-in, and user data security. Instead of building this from scratch (which is time-consuming and prone to security risks), we will leverage Amazon Cognito—a robust Identity as a Service (IDaaS) provider.

In this lab, you will learn how to:
- Provision a user directory (User Pool).
- Configure an App Client to allow Web/Mobile applications to call authentication APIs.
- Retrieve and use JSON Web Tokens (JWT) to authorize user access.

## Step-by-Step Instructions

Lab 2 consists of the following sections. Please follow them in order:

- **[1. Create User Pool](1-create-userpool/)**: Initialize and configure rules for accounts (e.g., email verification, password policies).
- **[2. App Integration](2-app-integration/)**: Create an App Client and insert the parameters into the Frontend code.
- **[3. Test Authentication](3-test-authentication/)**: Execute the Sign-up and Sign-in flows directly on the web interface.

---
Let's get started with the first step: **[Create User Pool](1-create-userpool/)**.
