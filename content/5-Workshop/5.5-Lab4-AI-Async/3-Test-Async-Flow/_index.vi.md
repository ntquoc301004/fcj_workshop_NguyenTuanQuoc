---
title: "3. Kiểm thử luồng Async"
weight: 3
chapter: false
pre: " <b> 5.5.3. </b> "
---

# 3. Kiểm thử luồng AI Bất đồng bộ (Async Flow)

Để hiểu rõ tại sao chúng ta lại dùng BullMQ và Redis, ở phần này ta sẽ kiểm thử thực tế.

Nhắc lại luồng hoạt động (Core Flow):
1. **Frontend** gửi Prompt -> **Backend API**.
2. **API** tạo 1 Job đẩy vào **BullMQ (Redis)** và trả về ngay `jobId` cho Frontend (HTTP 202 Accepted).
3. **Frontend** mở một kết nối **Server-Sent Events (SSE)** lắng nghe trạng thái của `jobId` này.
4. Ở dưới nền (Background), **AI Worker** lấy Job từ Redis, gọi **Gemini API** sinh JSON, lưu vào RDS và cập nhật tiến độ (Progress) trên BullMQ.
5. Khi tiến độ đạt `100%`, SSE Stream báo về Frontend để hiển thị giao diện.

## Bước 1: Mở giao diện Genzite
1. Truy cập vào ứng dụng Frontend qua `localhost` hoặc link CloudFront.
2. Đăng nhập bằng tài khoản bạn đã tạo ở Lab 2.
3. Ở trang chủ, tìm ô nhập Prompt để yêu cầu AI tạo web.

## Bước 2: Theo dõi luồng Network
1. Chuột phải lên trang web, chọn **Inspect** (Kiểm tra).
2. Chuyển sang tab **Network** (Mạng). Khuyến nghị lọc hiển thị các request **Fetch/XHR** và **EventStream**.
3. Nhập một câu Prompt ví dụ: *"Tạo cho tôi một trang Landing Page bán cà phê tông màu nâu ấm, có danh sách sản phẩm và form liên hệ"*.
4. Nhấn **Generate** (Tạo).

## Bước 3: Quan sát API Call và SSE Stream
1. Ngay lập tức, bạn sẽ thấy một request POST gọi đến API (ví dụ: `/api/v1/ai/generate`).
   - Click vào request này, ở tab **Preview** (hoặc **Response**), bạn sẽ thấy kết quả trả về gần như lập tức: `{"jobId": "12345"}`.
2. Một request thứ hai sẽ xuất hiện, thường có dạng GET `/api/v1/ai/stream/12345`.
   - Lưu ý rằng request này sẽ **không kết thúc ngay** (trạng thái là Pending).
   - Click vào request này, chuyển sang tab **EventStream**. Bạn sẽ thấy các tin nhắn được trả về liên tục từ Server theo thời gian thực (ví dụ: `Progress: 10%`, `Progress: 50%`).
3. Đồng thời, trên giao diện Genzite sẽ hiển thị thanh loading tăng dần thay vì bị "treo" (đơ) trình duyệt.
4. Khi AI xử lý xong, thông báo `100%` kèm theo JSON Layout được đẩy về qua SSE, giao diện web lập tức hiển thị bản xem trước (Canvas).

## Nhìn lại Kiến trúc
Luồng xử lý này giải quyết được vấn đề timeout. Nếu chúng ta dùng cơ chế gọi API đồng bộ thông thường, request có thể bị quá thời gian cho phép (timeout) khi Gemini xử lý chậm (ví dụ mất 30 giây), gây ra lỗi 504 Gateway Timeout trên ALB hoặc CloudFront. Cơ chế Queue + SSE đảm bảo trải nghiệm người dùng mượt mà nhất.

---
**Chúc mừng!** Hệ thống AI tích hợp của bạn đã hoạt động hoàn hảo với hiệu năng cao. Ở bài Lab cuối cùng (**Lab 5**), ta sẽ làm quen với một khái niệm nâng cao hơn nữa để giúp các Microservices giao tiếp: **Kiến trúc Hướng sự kiện (Event-Driven) với Apache Kafka**.
