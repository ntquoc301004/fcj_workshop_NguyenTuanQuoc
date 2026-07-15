---
title: "2. Triển khai Backend"
weight: 2
chapter: false
pre: " <b> 5.4.2. </b> "
---


Để ứng dụng Genzite xử lý các request phức tạp (sinh JSON từ prompt, giao tiếp với Database), chúng ta cần một máy chủ ảo (Virtual Machine). Trong AWS, đó là dịch vụ **Amazon Elastic Compute Cloud (EC2)**.

Dựa theo thiết kế, EC2 sẽ được đặt trong **Private Subnet** để ẩn khỏi internet, và chỉ cho phép lưu lượng truy cập đi qua Application Load Balancer (ALB).

## Bước 1: Khởi tạo EC2 Instance

1. Mở dịch vụ **EC2** trên AWS Console.
2. Nhấn **Launch instances**.
3. **Name**: Nhập `genzite-backend-ec2`.
4. **Application and OS Images (Amazon Machine Image)**:
   - Chọn **Amazon Linux 2023 AMI** (Free tier eligible).
   - *Lưu ý:* Chọn kiến trúc **64-bit (Arm)** để dùng chip Graviton tiết kiệm chi phí.
5. **Instance type**:
   - Chọn `t4g.small` (Vì yêu cầu chạy Node.js và NestJS, t4g.small sẽ cho hiệu năng ổn định hơn t4g.micro).
6. **Key pair (login)**:
   - Chọn **Proceed without a key pair** (Chúng ta sẽ dùng AWS Systems Manager - Session Manager để truy cập an toàn thay vì dùng SSH Key).
7. **Network settings**:
   - Nhấn **Edit**.
   - **VPC**: Chọn `genzite-vpc`.
   - **Subnet**: Chọn một **Private Subnet** (Ví dụ: `genzite-private-subnet-1a`).
   - **Auto-assign public IP**: **Disable** (Bắt buộc vô hiệu hoá để đảm bảo máy chủ không bị lộ ra Internet).
   - **Firewall (security groups)**: Chọn **Select existing security group**, sau đó chọn `genzite-ec2-sg` (Đã tạo ở Lab 1).
8. **Configure storage**:
   - Để mặc định `8 GiB` gp3.
9. Mở rộng phần **Advanced details**:
   - Kéo xuống mục **IAM instance profile**: Chọn `genzite-ec2-role` (Role đã tạo ở Lab 1 giúp EC2 gọi AWS services và cho phép dùng Session Manager).
10. Nhấn **Launch instance**.

## Bước 2: Kết nối vào EC2 thông qua Session Manager

Vì EC2 nằm trong Private Subnet và không có Public IP, bạn không thể SSH trực tiếp. Chúng ta sẽ dùng tính năng Session Manager.

1. Chờ trạng thái EC2 chuyển sang **Running** và **Status check** là *2/2 checks passed*.
2. Đánh dấu chọn vào EC2 instance `genzite-backend-ec2`, nhấn nút **Connect** ở góc trên cùng.
3. Chuyển sang tab **Session Manager**.
4. Nhấn **Connect**. Một cửa sổ terminal đen sẽ mở ra ngay trên trình duyệt.

## Bước 3: Cài đặt Môi trường (Node.js & PM2)

Trong terminal của Session Manager, chạy các lệnh sau để chuẩn bị môi trường chạy backend:

```bash
# Cập nhật hệ thống
sudo dnf update -y

# Cài đặt Node.js (phiên bản 18 hoặc 20)
curl -fsSL https://rpm.nodesource.com/setup_20.x | sudo bash -
sudo dnf install -y nodejs

# Kiểm tra version
node -v
npm -v

# Cài đặt PM2 (Process Manager để giữ app luôn chạy)
sudo npm install pm2 -g
```

## Bước 4: Tải Source Code và Cấu hình Biến môi trường (.env)

Tiếp theo, clone source code (nếu dùng git) hoặc tạo thư mục backend giả định:

```bash
# Giả sử clone code từ github (Thay bằng link repo thực tế của bạn nếu có)
git clone https://github.com/your-repo/genzite-backend.git
cd genzite-backend

# Hoặc tạo thư mục trống để test nếu bạn không có source code:
# mkdir genzite-backend && cd genzite-backend && npm init -y && npm install express
```

Tạo file biến môi trường để kết nối với RDS Database đã tạo ở Bước 1.

```bash
nano .env
```
Nhập các thông tin sau (chỉnh sửa lại cho khớp với RDS và Cognito của bạn):
```env
# Database RDS
DB_HOST=genzite-db.xxxxxxxxx.us-east-1.rds.amazonaws.com
DB_PORT=5432
DB_USERNAME=postgres
DB_PASSWORD=GenziteDBPass123!
DB_DATABASE=genzite

# AWS Cognito (Lấy từ Lab 2)
COGNITO_USER_POOL_ID=us-east-1_xxxxxxxxx
COGNITO_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxx
AWS_REGION=us-east-1

# Port chạy app
PORT=3000
```
Nhấn `Ctrl + O` -> `Enter` để lưu file, rồi `Ctrl + X` để thoát.

## Bước 5: Chạy ứng dụng Backend

Cài đặt các thư viện cần thiết và chạy API:

```bash
# Cài đặt dependencies
npm install

# Build code (Nếu là dự án NestJS/TypeScript)
npm run build

# Chạy ứng dụng ngầm với PM2
pm2 start dist/main.js --name "genzite-api"
```

Kiểm tra xem app đã chạy đúng trên port 3000 chưa:
```bash
curl http://localhost:3000/
```
*(Nếu terminal trả về kết quả hoặc thông báo lỗi JSON, ứng dụng của bạn đã chạy thành công).*

---
Hiện tại API đang chạy tốt trong máy chủ EC2. Nhưng làm sao để Frontend từ bên ngoài Internet có thể gọi vào API này? Hãy chuyển sang bước tiếp theo: **Cấu hình Load Balancer**.
