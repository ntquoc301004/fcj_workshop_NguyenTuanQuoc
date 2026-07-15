---
title: "2. Tích hợp Gemini API"
weight: 2
chapter: false
pre: " <b> 5.5.2. </b> "
---

# 2. Tích hợp Google Gemini API

Trái tim của Genzite là khả năng sinh giao diện từ văn bản (text-to-layout). Chúng ta sẽ sử dụng API của Google Gemini 2.0 Flash (hoặc phiên bản tương đương) vì tốc độ phản hồi cực nhanh và khả năng trả về định dạng JSON chính xác.

## Bước 1: Lấy API Key từ Google AI Studio

1. Truy cập vào trang web: [Google AI Studio](https://aistudio.google.com/).
2. Đăng nhập bằng tài khoản Google của bạn.
3. Ở menu bên trái, nhấn vào **Get API key**.
4. Nhấn nút **Create API key**. (Nếu được hỏi, hãy tạo một project Google Cloud mới).
5. Sao chép đoạn mã API Key vừa được tạo (bắt đầu bằng `AIza...`). 
   *(Lưu ý: API Key là thông tin bảo mật, tuyệt đối không commit lên Github).*

## Bước 2: Cập nhật cấu hình EC2 Backend

Chúng ta cần cập nhật cấu hình cho máy chủ Backend (EC2) để ứng dụng có thể kết nối với Redis (đã tạo ở bước 1) và sử dụng Gemini API.

1. Truy cập lại **EC2**, dùng **Session Manager** để mở terminal của `genzite-backend-ec2`.
2. Di chuyển đến thư mục chứa mã nguồn backend:
   ```bash
   cd genzite-backend
   ```
3. Mở file biến môi trường:
   ```bash
   nano .env
   ```
4. Bổ sung thêm các biến sau:
   ```env
   # ... (giữ nguyên các biến DB_ và COGNITO_ cũ) ...

   # Redis Configuration (BullMQ)
   REDIS_HOST=genzite-redis.xxxxxx.0001.use1.cache.amazonaws.com
   REDIS_PORT=6379

   # Gemini API Key
   GEMINI_API_KEY=AIzaSyA_XXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```
   *(Thay `REDIS_HOST` bằng Primary Endpoint bạn lấy ở bước 1, thay `GEMINI_API_KEY` bằng key bạn vừa copy).*
5. Nhấn `Ctrl + O` -> `Enter` để lưu, và `Ctrl + X` để thoát.

## Bước 3: Khởi động lại AI Worker

Trong hệ thống Genzite, "AI Worker" là tiến trình có nhiệm vụ liên tục lấy Job từ BullMQ (trên Redis) và gọi ra Gemini API. Tùy thuộc vào kiến trúc, Worker này có thể chạy chung với API chính hoặc chạy thành một tiến trình (process) độc lập.

Khởi động lại toàn bộ ứng dụng bằng PM2 để nhận biến môi trường mới:

```bash
# Restart lại backend
pm2 restart all

# Hoặc nếu Worker chạy riêng:
# pm2 start dist/worker.js --name "genzite-worker"

# Xem log để đảm bảo không có lỗi kết nối Redis
pm2 logs
```

Nếu trong file log hiển thị thông báo `Connected to Redis` hoặc `Worker is ready`, quá trình tích hợp đã thành công!

---
Hãy chuyển sang phần tiếp theo để **Kiểm thử luồng chạy bất đồng bộ (Async Flow)** xem quá trình sinh web từ văn bản hoạt động ra sao.
