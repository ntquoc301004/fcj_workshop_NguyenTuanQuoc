---
title: "1. Khởi tạo RDS"
weight: 1
chapter: false
pre: " <b> 5.4.1. </b> "
---


Hệ thống Genzite cần một nơi lưu trữ dữ liệu có cấu trúc (thông tin User, các Project Web đã tạo, cấu trúc JSON layout). Trong môi trường AWS, dịch vụ tối ưu nhất là **Amazon Relational Database Service (RDS)**. 

Để tiết kiệm chi phí cho bài Lab và đáp ứng cấu hình MVP (Minimum Viable Product), ta sẽ chọn PostgreSQL chạy trên instance `db.t4g.micro` và đặt trong Private Subnet.

## Bước 1: Tạo DB Subnet Group

Trước khi tạo RDS, ta cần nói cho AWS biết Database này được phép nằm trong các Subnet nào. Dựa theo Security Best Practice, ta chỉ đặt DB trong Private Subnet.

1. Mở dịch vụ **RDS** trên AWS Console.
2. Từ menu bên trái, chọn **Subnet groups**.
3. Nhấn **Create DB subnet group**.
4. **Name**: `genzite-db-subnet-group`.
5. **Description**: `Subnet group cho Genzite RDS trong Private Subnet`.
6. **VPC**: Chọn `genzite-vpc`.
7. Kéo xuống phần **Add subnets**:
   - Chọn **Availability Zones**: Chọn các AZ mà bạn đã tạo Subnet ở Lab 1.
   - Chọn **Subnets**: Đánh dấu tích vào các **Private Subnets** (Hãy cẩn thận nhìn vào cột CIDR block để đảm bảo bạn không chọn nhầm Public Subnet).
8. Nhấn **Create**.

## Bước 2: Khởi tạo Database Instance

1. Từ menu bên trái, chọn **Databases** và nhấn **Create database**.
2. **Choose a database creation method**: Chọn **Standard create**.
3. **Engine options**: Chọn **PostgreSQL**.
4. **Templates**: Chọn **Free tier** (Rất quan trọng để không phát sinh chi phí lớn).
5. **Settings**:
   - **DB instance identifier**: `genzite-db`.
   - **Master username**: `postgres` (mặc định).
   - **Master password**: Nhập mật khẩu đủ mạnh (Ví dụ: `GenziteDBPass123!`). Ghi nhớ mật khẩu này.
6. **Instance configuration**:
   - DB instance class: Chọn `db.t4g.micro` (Dòng chip ARM tiết kiệm chi phí).
7. **Storage**:
   - Allocated storage: `20` GB.
   - Bỏ tích **Enable storage autoscaling**.
8. **Connectivity**:
   - **Virtual private cloud (VPC)**: Chọn `genzite-vpc`.
   - **DB Subnet Group**: Chọn `genzite-db-subnet-group` bạn vừa tạo.
   - **Public access**: Chọn **No** (Database không được phép truy cập từ Internet).
   - **VPC security group (firewall)**: Chọn **Choose existing**, loại bỏ thẻ `default`, và chọn `genzite-rds-sg` (Đã tạo ở Lab 1 - Security).
9. **Database authentication**: Để mặc định (Password authentication).
10. Mở rộng phần **Additional configuration**:
    - Nhập **Initial database name**: `genzite`. *(Nếu không nhập ô này, RDS sẽ không tạo sẵn Database cho bạn)*.
    - Kéo xuống bỏ tích **Enable automated backups** (Để tiết kiệm dung lượng lưu trữ cho bài Lab).
11. Kiểm tra lại thông tin, cuộn xuống dưới cùng và nhấn **Create database**.

## Bước 3: Lấy Endpoint kết nối

Quá trình khởi tạo Database có thể mất từ 5-10 phút.

1. Khi trạng thái Database chuyển sang `Available`, hãy nhấn vào tên `genzite-db`.
2. Trong tab **Connectivity & security**, tìm mục **Endpoint**.
3. Sao chép lại đường dẫn **Endpoint** này (ví dụ: `genzite-db.xxxxxxxxx.us-east-1.rds.amazonaws.com`). 

Bạn sẽ cần Endpoint này cùng với Username, Password và Tên database (`genzite`) để cấu hình cho máy chủ Backend EC2 ở bước tiếp theo.
