---
title: "3. Kiểm thử Xác thực"
weight: 3
chapter: false
pre: " <b> 5.3.3. </b> "
---


Trong phần này, chúng ta sẽ chạy ứng dụng Frontend ở môi trường local (hoặc truy cập qua domain S3/CloudFront) để xác minh xem kết nối đến Amazon Cognito đã hoạt động chính xác hay chưa.

## Bước 1: Khởi chạy Frontend
Nếu bạn đang chạy ứng dụng ở môi trường local, hãy mở terminal và thực thi:
```bash
npm run dev
```
Trình duyệt sẽ tự động mở tại `http://localhost:5173`.
*(Lưu ý: Nếu bạn truy cập qua link CloudFront từ bài Lab trước, hãy sử dụng link đó).*

## Bước 2: Tạo tài khoản mới (Sign-up)
1. Trên giao diện Genzite, nhấn nút **Sign Up** (Đăng ký).
2. Nhập một địa chỉ email hợp lệ (mà bạn có thể kiểm tra hộp thư) và mật khẩu (đảm bảo tuân thủ chính sách bảo mật: 8 ký tự, có số, chữ hoa, chữ thường).
3. Nhấn **Create Account**.

## Bước 3: Xác thực Email (Verification)
1. Sau khi nhấn tạo tài khoản, giao diện sẽ chuyển sang màn hình **OTP Verification**.
2. Kiểm tra Hộp thư đến (Inbox) của email bạn vừa đăng ký. Mở email có tiêu đề "Your verification code" được gửi từ Cognito.
3. Nhập mã code gồm 6 chữ số vào ô nhập liệu trên màn hình.
4. Nhấn **Verify**.

![Test Mail Verify 1](/images/5-Workshop/5.3-Lab2-Cognito-Auth/3-Test-Authentication/5.3.3.1.png)

## Bước 4: Đăng nhập và Kiểm tra Token
1. Sau khi xác thực thành công, giao diện sẽ tự động chuyển hướng về trang chủ hoặc màn hình **Sign In**.
2. Nhập email và mật khẩu bạn vừa đăng ký.
3. Nhấn **Login**.
4. **Kiểm tra JWT Tokens**:
   - Click chuột phải trên trang web và chọn **Inspect** (Kiểm tra) để mở Developer Tools của trình duyệt.
   - Chuyển sang tab **Application** (hoặc Storage).
   - Mở mục **Local Storage**, bạn sẽ thấy các key lưu trữ của Cognito bắt đầu bằng `CognitoIdentityServiceProvider...`.
   - Nhấn vào key có chứa `accessToken` hoặc `idToken`, bạn sẽ thấy một chuỗi rất dài (đó chính là JWT Token).

## Bước 5: Xác minh trên AWS Console
Để chắc chắn rằng người dùng đã được tạo thành công trên hệ thống:
1. Quay lại AWS Management Console và mở dịch vụ **Cognito**.
2. Nhấn vào `genzite-user-pool`.
3. Trong tab **Users**, bạn sẽ thấy địa chỉ email vừa tạo có trạng thái là **CONFIRMED**.

![Test Account Cognito](/images/5-Workshop/5.3-Lab2-Cognito-Auth/3-Test-Authentication/5.3.3.2.png)

---
**Chúc mừng!** Tính năng đăng ký/đăng nhập của ứng dụng đã hoạt động trơn tru. Với JWT token này, người dùng đã có thể bắt đầu sử dụng các tính năng tạo website bằng AI của hệ thống.

Hãy chuyển sang **Lab 3** để xây dựng "bộ não" của Genzite: **Database và Backend API**.
