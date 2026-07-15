---
title: "1. Khởi tạo ElastiCache"
weight: 1
chapter: false
pre: " <b> 5.5.1. </b> "
---

# 1. Khởi tạo ElastiCache Redis

Để chạy BullMQ (thư viện xử lý hàng đợi - Message Queue của Node.js), chúng ta cần một server Redis. Trong môi trường AWS, dịch vụ tối ưu nhất là **Amazon ElastiCache for Redis**.

Tương tự như Database, Redis cũng phải được đặt trong **Private Subnet** để đảm bảo tính bảo mật. EC2 Backend sẽ đẩy các "Job" (các yêu cầu tạo web) vào Redis, và AI Worker (chạy trên cùng EC2 hoặc một EC2 khác) sẽ lấy Job ra từ Redis để xử lý.

## Bước 1: Tạo Subnet Group cho Redis

1. Mở dịch vụ **ElastiCache** trên AWS Console.
2. Từ menu bên trái, chọn **Subnet groups** (nằm dưới mục Network and Security).
3. Nhấn **Create subnet group**.
4. **Name**: `genzite-redis-subnet-group`.
5. **Description**: `Subnet group for Redis in Private Subnet`.
6. **VPC ID**: Chọn `genzite-vpc`.
7. Dưới mục **Availability Zones**, chọn các AZ mà bạn đã tạo Subnet ở Lab 1.
8. Dưới mục **Subnets**, đánh dấu tích vào các **Private Subnets** (Hãy cẩn thận kiểm tra IP dải mạng để tránh chọn nhầm Public Subnet).
9. Nhấn **Create**.

## Bước 2: Khởi tạo Redis Cluster

1. Từ menu bên trái, chọn **Redis clusters**.
2. Nhấn **Create Redis cluster**.
3. **Choose a cluster creation method**: Chọn **Design your own cache** và **Cluster cache**.
4. **Cluster mode**: Đảm bảo đang chọn **Disabled** (BullMQ hoạt động tốt nhất trên single-node hoặc master-replica không bật cluster mode).
5. **Cluster info**:
   - **Name**: `genzite-redis`.
   - **Description**: `Redis for BullMQ`.
   - **Location**: Chọn **AWS Cloud** -> **Multi-AZ**: Bỏ chọn (để tiết kiệm chi phí).
6. **Node type**:
   - Chọn loại instance nhỏ nhất như `cache.t4g.micro` hoặc `cache.t3.micro`.
   - **Number of replicas**: `0` (Chạy 1 node duy nhất cho bài Lab MVP).
7. **Subnet group**: 
   - Chọn **Choose an existing subnet group**.
   - Chọn `genzite-redis-subnet-group` bạn vừa tạo.
8. Nhấn **Next**.
9. **Advanced settings** (Trang tiếp theo):
   - **Security**: Chọn VPC Security Group của EC2 `genzite-ec2-sg` (hoặc tạo một SG riêng cho Redis, cho phép port 6379 từ SG của EC2). Để đơn giản, bạn có thể tái sử dụng SG của EC2 nếu Inbound Rules cho phép Custom TCP 6379 nội bộ. *Khuyến nghị tốt nhất: Quay lại EC2 Security Groups, tạo `genzite-redis-sg` cho phép port 6379 từ `genzite-ec2-sg`.*
   - Kéo xuống dưới bỏ chọn **Enable automatic backups** để tối ưu chi phí.
10. Nhấn **Next**, xem lại cấu hình rồi nhấn **Create**.

## Bước 3: Lấy Primary Endpoint

Việc tạo Redis Cluster mất khoảng 3-5 phút.

1. Khi trạng thái chuyển thành `Available`, nhấp vào tên `genzite-redis`.
2. Sao chép địa chỉ ở phần **Primary endpoint** (có dạng `genzite-redis.xxxxxx.0001.use1.cache.amazonaws.com:6379`).

Bạn sẽ cần địa chỉ này để đưa vào biến môi trường của EC2 Backend trong bước tiếp theo.
