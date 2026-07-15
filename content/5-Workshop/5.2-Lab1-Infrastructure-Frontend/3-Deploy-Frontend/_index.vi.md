---
title: "3. Triển khai Frontend"
weight: 3
chapter: false
pre: " <b> 5.2.3. </b> "
---


Trong phần này, chúng ta sẽ triển khai ứng dụng frontend (được build bằng React/Vite) lên môi trường AWS một cách tối ưu nhất: sử dụng Amazon S3 để lưu trữ file tĩnh và Amazon CloudFront làm CDN (Mạng phân phối nội dung) nhằm tăng tốc độ tải trang toàn cầu và bảo mật dữ liệu.

## Bước 1: Khởi tạo S3 Bucket

S3 sẽ là nơi lưu trữ toàn bộ source code đã được build (`index.html`, `.js`, `.css`).

1. Mở dịch vụ **S3** trên AWS Console.
2. Nhấn **Create bucket**.
3. **Bucket name**: Đặt một tên duy nhất toàn cầu (ví dụ: `genzite-frontend-bucket-tencuaban`).
4. **AWS Region**: Chọn `us-east-1` (US East N. Virginia).
5. **Object Ownership**: Để mặc định là *ACLs disabled*.
6. **Block Public Access settings for this bucket**: Đánh dấu tích vào **Block all public access**.
   *(Lưu ý: Theo Best Practice, ta không mở public S3 bucket mà sẽ cấp quyền truy cập thông qua CloudFront).*
7. Các thông số khác để mặc định và nhấn **Create bucket**.

## Bước 2: Build và Upload Source Code Frontend

Giả định rằng bạn đã có sẵn mã nguồn Frontend của Genzite trên máy tính.

1. Mở terminal trên máy tính của bạn và đi đến thư mục code Frontend.
2. Chạy lệnh build ứng dụng React/Vite:
   ```bash
   npm install
   npm run build
   ```
3. Sau khi build xong, bạn sẽ có một thư mục `dist` (hoặc `build`).
4. Quay lại giao diện AWS S3, click vào bucket bạn vừa tạo.
5. Nhấn **Upload**, kéo và thả toàn bộ các file/folder **bên trong** thư mục `dist` vào.
6. Nhấn **Upload** và chờ quá trình hoàn tất.

## Bước 3: Cấu hình CloudFront với OAC

Để người dùng có thể truy cập website nhanh chóng, ta sẽ tạo một CloudFront Distribution và cấu hình **Origin Access Control (OAC)**. OAC giúp chỉ có CloudFront mới có quyền đọc file từ S3 bucket.

1. Mở dịch vụ **CloudFront** trên AWS Console.
2. Nhấn **Create a CloudFront distribution**.
3. **Origin domain**: Bấm vào ô này và chọn S3 bucket bạn vừa tạo.
4. **Origin access**: Chọn **Origin access control settings (recommended)**.
   - Nhấn nút **Create control setting** và giữ nguyên cấu hình mặc định, sau đó nhấn **Create**.
5. Kéo xuống phần **Default cache behavior**:
   - **Viewer protocol policy**: Chọn **Redirect HTTP to HTTPS** (để ép buộc dùng kết nối an toàn).
6. Kéo xuống phần **Web Application Firewall (WAF)**:
   - Chọn **Do not enable security protections** (để tiết kiệm chi phí cho bài Lab).
7. Kéo xuống dưới cùng và nhấn **Create distribution**.

## Bước 4: Cập nhật S3 Bucket Policy

Sau khi tạo Distribution, màn hình sẽ hiện một thanh thông báo màu vàng yêu cầu bạn cập nhật S3 bucket policy để cho phép CloudFront OAC truy cập.

1. Nhấn nút **Copy policy**.
2. Click vào link `Go to S3 bucket permissions` ở ngay thông báo đó.
3. Cuộn xuống phần **Bucket policy** và nhấn **Edit**.
4. Dán đoạn JSON vừa copy vào. Trông nó sẽ tương tự như sau:
   ```json
   {
       "Version": "2012-10-17",
       "Statement": {
           "Sid": "AllowCloudFrontServicePrincipalReadOnly",
           "Effect": "Allow",
           "Principal": {
               "Service": "cloudfront.amazonaws.com"
           },
           "Action": "s3:GetObject",
           "Resource": "arn:aws:s3:::genzite-frontend-bucket-tencuaban/*",
           "Condition": {
               "StringEquals": {
                   "AWS:SourceArn": "arn:aws:cloudfront::123456789012:distribution/E1A2B3C4D5E6F7"
               }
           }
       }
   }
   ```
5. Nhấn **Save changes**.

## Bước 5: Kiểm tra kết quả

Quay lại màn hình chi tiết của CloudFront Distribution.
1. Sao chép **Distribution domain name** (có dạng `d1234abcd.cloudfront.net`).
2. Mở trình duyệt web và dán đường link này vào.
3. Chờ vài phút để trạng thái của Distribution chuyển từ `Deploying` sang hoàn thành. Bạn sẽ thấy giao diện web Genzite xuất hiện!

---
**Hoàn thành Lab 1!** Kiến trúc cơ bản của hệ thống đã thành hình. Chúng ta hãy bước tiếp sang Lab 2 để xây dựng tính năng Xác thực đăng nhập (Authentication) cho người dùng.
