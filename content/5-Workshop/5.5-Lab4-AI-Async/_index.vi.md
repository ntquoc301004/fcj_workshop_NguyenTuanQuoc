---
title: "Lab 4: Xử lý AI Bất đồng bộ"
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# Lab 4: Xử lý AI Bất đồng bộ

Chào mừng bạn đến với **Lab 4**. Trong phần này, chúng ta sẽ xây dựng luồng xử lý AI bất đồng bộ (Asynchronous Processing) cho ứng dụng Genzite.

## Giới thiệu

Quá trình gọi AI (Google Gemini API) để sinh ra giao diện web hoàn chỉnh từ text prompt thường mất từ vài giây đến hơn mười giây. Nếu thiết kế API theo cơ chế đồng bộ (chờ kết quả rồi mới trả HTTP Response), server rất dễ bị quá tải, nghẽn luồng và kết nối dễ bị timeout.

Để giải quyết bài toán này, kiến trúc Genzite áp dụng mô hình Queue (Hàng đợi) kết hợp với Server-Sent Events (SSE). 

Trong bài lab này, bạn sẽ:
- Triển khai **Amazon ElastiCache (Redis)** làm in-memory datastore và message broker cho BullMQ.
- Tích hợp **Google Gemini API** một cách an toàn trên EC2 (nhận prompt từ Queue, gọi API, lưu kết quả vào RDS).
- Cấu hình luồng thông báo tiến độ theo thời gian thực về Frontend qua cơ chế SSE stream.

## Nội dung chi tiết

Lab 4 được chia làm các bước sau:

- **[1. Khởi tạo ElastiCache Redis](1-elasticache-redis/)**: Thiết lập cluster Redis bảo mật.
- **[2. Tích hợp Gemini API](2-gemini-integration/)**: Tạo API key và cấu hình AI Worker gọi Gemini.
- **[3. Kiểm thử luồng Async](3-test-async-flow/)**: Theo dõi job được đẩy vào queue và nhận kết quả trả về.

---
Bắt đầu ngay với bước: **[Khởi tạo ElastiCache Redis](1-elasticache-redis/)**.
