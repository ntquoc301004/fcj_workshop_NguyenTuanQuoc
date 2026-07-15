---
title: "Lab 2: Xác thực với Cognito"
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# Lab 2: Xác thực với Cognito (Authentication)

Chào mừng bạn đến với **Lab 2**. Trong phần này, chúng ta sẽ xây dựng hệ thống quản lý danh tính và kiểm soát quyền truy cập cho người dùng ứng dụng bằng **Amazon Cognito**.

## Giới thiệu

Hầu hết các ứng dụng thực tế đều yêu cầu tính năng đăng ký, đăng nhập và bảo mật thông tin người dùng. Thay vì tự xây dựng từ đầu (tốn thời gian và rủi ro bảo mật), chúng ta sẽ tận dụng Amazon Cognito - một dịch vụ quản lý danh tính (Identity as a Service - IDaaS) mạnh mẽ.

Trong bài lab này, bạn sẽ học cách:
- Khởi tạo hệ thống lưu trữ tài khoản (User Pool).
- Cấu hình App Client để các ứng dụng Web/Mobile có thể gọi API.
- Lấy và sử dụng JSON Web Tokens (JWT) để ủy quyền truy cập cho người dùng.

## Nội dung chi tiết

Lab 2 bao gồm các phần sau. Hãy lần lượt thực hiện theo thứ tự:

- **[1. Tạo User Pool](1-create-userpool/)**: Khởi tạo và thiết lập các quy tắc cho tài khoản (email, mật khẩu).
- **[2. Tích hợp Ứng dụng](2-app-integration/)**: Tạo App Client và chèn các thông số vào code Frontend.
- **[3. Kiểm thử Xác thực](3-test-authentication/)**: Thực hành luồng Sign-up và Sign-in trực tiếp trên giao diện web.

---
Hãy bắt đầu bước đầu tiên: **[Tạo User Pool](1-create-userpool/)**.
