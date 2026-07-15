---
title: "2. Gemini Integration"
weight: 2
chapter: false
pre: " <b> 5.5.2. </b> "
---


The heart of Genzite is its ability to generate layouts from text (text-to-layout). We will use the Google Gemini 2.0 Flash API (or equivalent) because of its extremely fast response times and ability to accurately output JSON formats.

## Step 1: Obtain an API Key from Google AI Studio

1. Go to the website: [Google AI Studio](https://aistudio.google.com/).
2. Sign in with your Google account.
3. In the left menu, click on **Get API key**.
4. Click the **Create API key** button. (If prompted, create a new Google Cloud project).
5. Copy the generated API Key (usually starts with `AIza...`).
   *(Note: The API Key is a secret credential, never commit it to Github).*

## Step 2: Update EC2 Backend Configuration

We need to update the Backend server (EC2) configuration so the application can connect to Redis (created in step 1) and utilize the Gemini API.

1. Go back to **EC2**, and use **Session Manager** to open the terminal for `genzite-backend-ec2`.
2. Navigate to the backend source code directory:
   ```bash
   cd genzite-backend
   ```
3. Edit the environment variable file:
   ```bash
   nano .env
   ```
4. Append the following variables:
   ```env
   # ... (keep the existing DB_ and COGNITO_ variables) ...

   # Redis Configuration (BullMQ)
   REDIS_HOST=genzite-redis.xxxxxx.0001.use1.cache.amazonaws.com
   REDIS_PORT=6379

   # Gemini API Key
   GEMINI_API_KEY=AIzaSyA_XXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```
   *(Replace `REDIS_HOST` with the Primary Endpoint retrieved in step 1, and `GEMINI_API_KEY` with your copied key).*
5. Press `Ctrl + O` -> `Enter` to save, and `Ctrl + X` to exit.

## Step 3: Restart the AI Worker

In the Genzite system, the "AI Worker" is the process responsible for continuously pulling Jobs from BullMQ (on Redis) and calling the Gemini API. Depending on the architecture, this Worker might run within the main API or as an independent process.

Restart the entire application using PM2 to pick up the new environment variables:

```bash
# Restart the backend
pm2 restart all

# Or if the Worker runs independently:
# pm2 start dist/worker.js --name "genzite-worker"

# Check the logs to ensure there are no Redis connection errors
pm2 logs
```

If the log displays a message like `Connected to Redis` or `Worker is ready`, the integration is successful!

---
Let's move on to the next section to **Test the Asynchronous Flow** and see how the text-to-web generation process actually works in real-time.
