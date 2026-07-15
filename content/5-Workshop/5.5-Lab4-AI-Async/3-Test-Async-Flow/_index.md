---
title: "3. Test Async Flow"
weight: 3
chapter: false
pre: " <b> 5.5.3. </b> "
---

# 3. Test Asynchronous AI Flow

To fully understand why we utilized BullMQ and Redis, we will test the system practically in this section.

Recap of the Core Flow:
1. **Frontend** sends a Prompt -> **Backend API**.
2. **API** creates a Job, pushes it to **BullMQ (Redis)**, and immediately returns a `jobId` to the Frontend (HTTP 202 Accepted).
3. **Frontend** opens a **Server-Sent Events (SSE)** connection to listen for the status of this `jobId`.
4. In the background, the **AI Worker** pulls the Job from Redis, calls the **Gemini API** to generate JSON, saves it to RDS, and updates the Progress on BullMQ.
5. When the progress hits `100%`, the SSE Stream notifies the Frontend to render the layout.

## Step 1: Open the Genzite UI
1. Access the Frontend application via `localhost` or the CloudFront link.
2. Sign in using the account you created in Lab 2.
3. On the homepage, locate the Prompt input box used to request AI generation.

## Step 2: Monitor Network Traffic
1. Right-click on the webpage and select **Inspect**.
2. Switch to the **Network** tab. It is recommended to filter the display to show **Fetch/XHR** and **EventStream** requests.
3. Enter a sample Prompt: *"Create a Landing Page for a coffee shop with warm brown tones, a product list, and a contact form"*.
4. Click **Generate**.

## Step 3: Observe API Calls and the SSE Stream
1. Immediately, you will see a POST request to the API (e.g., `/api/v1/ai/generate`).
   - Click on this request. In the **Preview** (or **Response**) tab, you will see it returns almost instantly: `{"jobId": "12345"}`.
2. A second request will appear, typically a GET like `/api/v1/ai/stream/12345`.
   - Notice that this request **does not finish immediately** (the status stays Pending).
   - Click on this request and switch to the **EventStream** tab. You will see messages continually pushed from the Server in real-time (e.g., `Progress: 10%`, `Progress: 50%`).
3. Simultaneously, the Genzite UI will display a gradually increasing loading bar, keeping the browser responsive without freezing.
4. Once the AI completes the task, a `100%` message along with the JSON Layout is pushed via SSE, and the web UI immediately renders the preview Canvas.

## Architectural Review
This asynchronous flow resolves the timeout issue. If we used standard synchronous API calls, the request might time out if Gemini took too long (e.g., 30 seconds), causing a 504 Gateway Timeout error on the ALB or CloudFront. The Queue + SSE mechanism guarantees the smoothest user experience.

---
**Congratulations!** Your integrated AI system is functioning flawlessly with high performance. In the final Lab (**Lab 5**), we will explore an even more advanced concept to facilitate Microservices communication: **Event-Driven Architecture using Apache Kafka**.
