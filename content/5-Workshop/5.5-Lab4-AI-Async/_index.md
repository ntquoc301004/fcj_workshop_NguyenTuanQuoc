---
title: "Lab 4: Asynchronous AI Processing"
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---


Welcome to **Lab 4**. In this module, we will build the asynchronous AI processing flow for the Genzite application.

## Overview

Calling the AI (Google Gemini API) to generate a complete web layout from a text prompt usually takes anywhere from a few seconds to over ten seconds. If we design the API synchronously (waiting for the result before returning the HTTP Response), the server can easily become overloaded, threads may block, and connections can time out.

To solve this, the Genzite architecture applies a Message Queue model combined with Server-Sent Events (SSE).

In this lab, you will:
- Deploy **Amazon ElastiCache (Redis)** to act as an in-memory datastore and message broker for BullMQ.
- Securely integrate the **Google Gemini API** on EC2 (consuming prompts from the Queue, calling the API, and saving results to RDS).
- Configure a real-time progress notification stream to the Frontend using SSE.

## Step-by-Step Instructions

Lab 4 is broken down into the following steps:

- **[1. Initialize ElastiCache Redis](1-elasticache-redis/)**: Set up a secure Redis cluster.
- **[2. Gemini API Integration](2-gemini-integration/)**: Generate an API key and configure the AI Worker to call Gemini.
- **[3. Test Async Flow](3-test-async-flow/)**: Monitor jobs being pushed into the queue and receive the output.

---
Let's get started with: **[Initialize ElastiCache Redis](1-elasticache-redis/)**.
