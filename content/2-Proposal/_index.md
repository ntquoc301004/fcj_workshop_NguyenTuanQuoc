---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
{{% notice warning %}}
⚠️ **Note:** The information below is for reference purposes only. Please **do not copy verbatim** for your report, including this warning.
{{% /notice %}}

In this section, you need to summarize the contents of the workshop that you **plan** to conduct.

# Genzite: Next-Generation AI No-Code Application Builder
## A Cloud-Native AWS Infrastructure Solution for AI-Driven App Generation and Recruitment Intelligence

### 1. Executive Summary
Genzite is a next-generation AI No-Code platform designed to empower non-technical users to build, launch, and operate fully functional web applications using simple natural language instructions. Rather than merely creating static landing pages, Genzite automatically generates front-end user interfaces, custom backend APIs, dynamic database collections (CMS), and complex business workflows. 

Furthermore, Genzite embeds AI Recruitment Intelligence modules including a Resume Builder, automated CV-to-JD compatibility matching, and mock conversational interviews. Hosted on AWS using a hybrid database architecture (Relational SQL + PostgreSQL JSONB) and a microservices monorepo setup (NestJS, React 18, Kafka, Redis, and BullMQ), the platform utilizes Google Gemini and Groq (Llama3) for high-speed application generation and analysis. Security, traffic routing, caching, and scalability are managed via Route 53, CloudFront, Cognito, ALB, EC2, RDS PostgreSQL, and ElastiCache.

### 2. Problem Statement
#### What’s the Problem?
Developing custom web applications requires professional programming skills, high budgets, and lengthy development timelines. Existing visual website builders (e.g., WordPress, Wix) are restricted to pre-defined layouts and lack the ability to dynamically design databases, generate functional backend APIs, orchestrate complex business workflows, or provide native AI services (such as mock interviews and CV analysis). Additionally, manual database migrations and deployment setups make expanding dynamic content forms slow and error-prone for non-technical administrators.

#### The Solution
Genzite solves these barriers by integrating a Dual-LLM architecture (Google Gemini for reasoning and coding; Groq Llama3 for high-speed reflection) that translates natural language prompts into structural components. To avoid slow database migrations, Genzite utilizes PostgreSQL JSONB fields to model dynamic CMS collections and resume profiles on the fly. 

To host this platform reliably and cost-effective, Genzite is built as a microservices architecture hosted on AWS:
- **Client Delivery**: React SPA static assets are stored in Amazon S3 and distributed globally through Amazon CloudFront CDN.
- **Compute Layer**: Node.js/NestJS backend microservices run in a private subnet on EC2 instances behind an Application Load Balancer (ALB).
- **Data Layer**: Relational data (users, billing, site configuration) is stored in Amazon RDS PostgreSQL, while dynamic data uses JSONB columns. Caching, sessions, and asynchronous job queues are managed via Amazon ElastiCache Redis (BullMQ).
- **External AI Integration**: Safe outbound calls to Google Gemini and Groq API are routed through a NAT Gateway from the private compute subnets.
- **User Management**: Secured by Amazon Cognito for authentication and role-based access control.

#### Benefits and Return on Investment (ROI)
The Genzite AWS solution enables businesses and creators to launch specialized web systems (e.g., e-commerce, recruitment hubs, dashboards) within seconds instead of weeks. By shifting binary file uploads directly to Amazon S3 via Presigned URLs, the backend compute load is bypassed, saving bandwidth and infrastructure costs. 

For the platform operators, Genzite provides a clear cost-optimized pathway:
- **MVP Cost**: An entry-level staging environment on AWS costs only **~$35–$60/month** by using single-AZ small instance types and skipping NAT Gateways and dedicated Redis setups.
- **Production Cost**: Scalable to **~$150–$350/month** with Multi-AZ redundancy, Auto Scaling Groups (ASG), and isolated networking.
The platform achieves a break-even point in 3–6 months by drastically reducing developer headcount and speeding up application delivery.

### 3. Solution Architecture
The platform utilizes a structured AWS architecture that ensures secure traffic routing, high-performance static delivery, and private network isolation for compute and database servers.

#### AWS Services Used
- **Amazon Route 53**: Manages custom domains and handles DNS routing to the CloudFront CDN distribution.
- **Amazon CloudFront**: Caches and serves the React SPA globally with SSL/TLS certificates generated via AWS Certificate Manager (ACM). It targets an 80-90% cache hit rate, reducing backend origin load.
- **Amazon S3**: Hosts static frontend assets (Frontend Bucket) and secures user-uploaded files, such as PDFs and images (Media Bucket), accessible only via time-limited Presigned URLs.
- **Amazon Cognito**: Secures platform user accounts, authentication sessions, and handles role assignment.
- **Application Load Balancer (ALB)**: Routes incoming `/api/*` traffic to healthy EC2 backend compute targets in private subnets, managing SSL decryption.
- **Amazon EC2 Auto Scaling**: Scales Graviton instances (`t4g.small` to `t4g.large`) running NestJS modules in isolated private subnets.
- **Amazon RDS PostgreSQL**: Stores relational tables for users, RBAC permissions, and site configurations, alongside JSONB tables for flexible user CMS collections.
- **Amazon ElastiCache Redis**: Speeds up performance via session caching, prompt-hash AI caches, and manages heavy BullMQ asynchronous task queues.
- **NAT Gateway**: Provides secure outbound internet access for private EC2 instances to query external LLM APIs (Gemini/Groq).

#### Component Design
Genzite is structured as a series of specialized backend services:
- **Identity Service**: Handles signup, login, JWT issuance, and workspace access control.
- **Site Service**: Manages site pages, canvas UI settings, and layout widgets.
- **Data Service**: The dynamic CMS engine that reads/writes custom collections and records using PostgreSQL JSONB.
- **Media Service**: Issues S3 Presigned URLs for direct client uploads, keeping backend servers free of heavy file traffic.
- **Notification Service**: Consumes Kafka events to trigger automated transactional emails and push notifications.
- **AI Service**: Connects to Gemini/Groq APIs, manages prompt caching, and handles async pipelines for CV matching and mock interview evaluations via BullMQ workers.
- **Commerce Service**: Manages shopping carts, orders, and coordinates with PayOS for merchant payment processing.

---

### 4. Technical Implementation
#### Implementation Phases
The deployment and setup of Genzite's infrastructure follow 4 key phases:
1. **Phase 1: Architecture Design & Infrastructure Mockup (Month 0)**
   - Draft microservice boundaries, establish database ERD schemas, and model public vs. private subnets in AWS.
2. **Phase 2: Feasibility & Cost Calculation (Month 1)**
   - Analyze resources on the AWS Pricing Calculator to balance costs between MVP development and high-availability production architectures.
3. **Phase 3: Security & Network Isolation Setup (Month 2)**
   - Deploy VPC subnets, configure strict Security Group rules (e.g., only allowing DB traffic from EC2 subnets, and only allowing EC2 traffic from the ALB SG), and set up CloudFront OAI policies for S3.
4. **Phase 4: Service Deployment, Integration & Testing (Months 2–3)**
   - Deploy NestJS services using Docker Compose / AWS ECS, establish Kafka communication topics, connect the React SPA hosted on S3/CloudFront, and run end-to-end load tests for the AI generation pipeline.

#### Technical Requirements
- **Frontend**: React 18, Vite, TypeScript, Tailwind CSS v4. Must support dynamic canvas rendering (15+ widgets) and direct S3 uploads.
- **Backend**: NestJS, Prisma ORM, Kafka (event bus for microservice communication), BullMQ + Redis (heavy AI worker queues).
- **Database**: PostgreSQL with JSONB support, Redis for key-value caching.
- **AI Engine**: Google Gemini API, Groq Llama3 SDK, and Model Context Protocol (MCP) integrations.

### 5. Timeline & Milestones
- **Month 0 (Pre-implementation)**: Design C4 models, write OpenAPI schemas, and prepare the local development Docker Compose environment.
- **Month 1 (Phase 1: Core Infra & Identity)**: Deploy Route 53, S3, RDS, and API Gateway. Complete the Identity Service (JWT authentication and RBAC roles).
- **Month 2 (Phase 2: Application Canvas & Dynamic CMS)**: Deploy Site Service and Data Service. Implement PostgreSQL JSONB operations, and establish S3 Media Presigned URL generation.
- **Month 3 (Phase 3: AI Engine, Commerce & Launch)**: Build the AI Service queue using BullMQ. Connect Google Gemini API for site generation. Integrate PayOS in the Commerce Service. Conduct integration testing, audit security groups, and officially go live.
- **Post-Launch (Months 4+)**: Monitor system usage, analyze CloudFront cache rates, and optimize database indexing for JSONB fields.

### 6. Budget Estimation
Below is Genzite's detailed cost comparison for MVP mode (Staging/Demo) vs. Production mode on AWS:

| AWS Component | MVP Mode (Staging/Demo) | Production Mode |
|---|---|---|
| **Compute (EC2)** | Single `t4g.small` (~$12/month) | Auto Scaling Group `t4g.medium` or `t4g.large` |
| **Load Balancer** | ❌ None (Direct EC2 routing) | ✅ ALB with HTTPS and ACM (~$22/month) |
| **NAT Gateway** | ❌ None (EC2 in public subnet for outbound) | ✅ NAT Gateway in public subnet (~$32/month + data) |
| **RDS PostgreSQL** | Single-AZ `db.t4g.micro` (~$13/month) | Multi-AZ `db.t4g.small` or `db.t4g.medium` (~$60+/month) |
| **ElastiCache Redis** | ❌ None (In-memory caching/BullMQ in EC2) | ✅ Dedicated ElastiCache Redis cluster (~$16/month) |
| **S3 Storage & Media** | ✅ Standard tier (~$2/month) | ✅ Standard + IA + Glacier Lifecycle Rules (~$10/month) |
| **CloudFront CDN** | ✅ Free tier (Low traffic) | ✅ Full CDN + Custom WAF policies (~$20/month) |
| **Estimated Total** | **~$35–$60 / month** | **~$150–$350 / month** |

- **Estimated Budget Link**: Detailed configurations are available on the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=621f38b12a1ef026842ba2ddfe46ff936ed4ab01).

---

### 7. Risk Assessment
#### Risk Matrix
| Risk | Probability | Impact | Mitigation Strategy |
|---|---|---|---|
| **AI API Key Rate Limits** | High | High | Implement a round-robin multi-API key load balancing pool. Cache identical prompt results using Redis hashing to bypass LLM calls. |
| **Database Performance Degradation** | Medium | High | Limit JSONB depth. Create expression indexes on heavily-queried JSONB paths (e.g., index `ats_scores` or `site_id` inside dynamic tables). |
| **Security / Malicious S3 Uploads** | Medium | Medium | Validate file extensions and mime-types in the Media Service prior to issuing Presigned URLs. Configure S3 lifecycle rules to auto-delete temporary files. |
| **High LLM Call Latency (10–15s)** | High | Medium | Execute all heavy AI operations asynchronously. Use BullMQ workers to process requests and update status via SSE/Kafka events. |

#### Contingency Plans
- If Google Gemini experiences outages, the system automatically falls back to Groq Llama3 or DeepSeek APIs to prevent platform downtime.
- If AWS services fail, the system is backed up using AWS CloudFormation templates, allowing developers to spin up a duplicate staging environment within 15 minutes.

### 8. Expected Outcomes
- **Zero-Code Full-Stack Application Generation**: Users can generate a multi-page website with a functional dynamic CMS within 20 seconds.
- **Cost-Optimized Backend Operations**: The direct S3 upload mechanism reduces EC2 bandwidth consumption by up to 90%.
- **Secure, High-Speed Data Transactions**: Secure separation of compute/database subnets and encrypted customer transactions using PayOS API.
- **Microservices Monorepo Scalability**: Codebases are structured inside a clean pnpm workspace monorepo, facilitating smooth future migration from a modular monolith to independent containerized services.