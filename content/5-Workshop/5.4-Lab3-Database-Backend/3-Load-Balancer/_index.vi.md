---
title: "3. Cấu hình Load Balancer"
weight: 3
chapter: false
pre: " <b> 5.4.3. </b> "
---

# 3. Cấu hình Load Balancer (ALB)

Vì máy chủ EC2 Backend nằm trong **Private Subnet** (không có Public IP), các ứng dụng Frontend từ internet không thể gọi trực tiếp vào API của chúng ta. 

Giải pháp chuẩn AWS là sử dụng một **Application Load Balancer (ALB)** đặt ở Public Subnet. ALB sẽ nhận HTTP/HTTPS request từ ngoài internet, sau đó "chuyển tiếp" (forward) vào cho máy chủ EC2 ở bên trong một cách an toàn.

## Bước 1: Tạo Target Group

Target Group là một nhóm chứa các máy chủ (EC2) mà ALB sẽ điều phối traffic tới.

1. Mở dịch vụ **EC2**, cuộn xuống menu bên trái phần **Load Balancing**, chọn **Target Groups**.
2. Nhấn **Create target group**.
3. **Choose a target type**: Chọn **Instances**.
4. **Target group name**: `genzite-backend-tg`.
5. **Protocol**: `HTTP`. **Port**: `3000` (Port mà NestJS đang chạy).
6. **VPC**: Chọn `genzite-vpc`.
7. **Health checks**: Để mặc định (Protocol: HTTP, Path: `/`).
   *(Lưu ý: Bạn phải đảm bảo API của mình có route trả về status code 200 ở đường dẫn `/` để Health check pass).*
8. Nhấn **Next**.
9. Tại màn hình **Register targets**, chọn máy chủ `genzite-backend-ec2` ở danh sách bên dưới.
10. Sửa port thành `3000` và nhấn **Include as pending below**.
11. Cuộn xuống nhấn **Create target group**.

## Bước 2: Khởi tạo Application Load Balancer

1. Ở menu bên trái, chọn **Load Balancers**.
2. Nhấn **Create load balancer**.
3. Tại phần **Application Load Balancer**, nhấn **Create**.
4. **Load balancer name**: `genzite-alb`.
5. **Scheme**: Chọn **Internet-facing** (Quan trọng: Để ALB có thể nhận traffic từ internet).
6. **IP address type**: `IPv4`.
7. **Network mapping**:
   - **VPC**: Chọn `genzite-vpc`.
   - **Mappings**: Chọn ít nhất 2 **Availability Zones** và chọn các **Public Subnets** tương ứng (ALB bắt buộc phải ở Public Subnet).
8. **Security groups**:
   - Xoá group `default`.
   - Chọn `genzite-alb-sg` (Đã tạo ở Lab 1).
9. **Listeners and routing**:
   - **Protocol**: `HTTP`. **Port**: `80`.
   - **Default action**: Chọn Target group `genzite-backend-tg` bạn vừa tạo.
10. Nhấn **Create load balancer**.

## Bước 3: Kiểm tra luồng gọi API

Việc khởi tạo ALB sẽ mất khoảng 3-5 phút (Trạng thái chuyển từ `Provisioning` sang `Active`).

1. Khi ALB ở trạng thái `Active`, click vào tên `genzite-alb`.
2. Sao chép **DNS name** của ALB (ví dụ: `genzite-alb-123456789.us-east-1.elb.amazonaws.com`).
3. Dán địa chỉ DNS này lên trình duyệt (Nhớ dùng `http://` thay vì `https://`).
4. Nếu màn hình trả về kết quả JSON từ API của bạn, xin chúc mừng! ALB đã định tuyến thành công request từ Internet vào thẳng máy chủ EC2 ở Private Subnet.

## Bước 4: Cập nhật biến môi trường trên Frontend

Bước cuối cùng của Lab này là cập nhật lại URL API trên Frontend.

1. Mở lại file `.env` ở dự án Frontend.
2. Thêm biến chứa URL của ALB (Đừng quên thêm `http://`):
   ```env
   VITE_API_BASE_URL=http://genzite-alb-123456789.us-east-1.elb.amazonaws.com
   ```
3. Sau khi cập nhật, hãy nhớ `npm run build` và deploy lại Frontend lên S3 nếu cần.

---
**Hoàn thành Lab 3!** Bạn đã sở hữu một hạ tầng Backend hoàn chỉnh gồm Database an toàn, máy chủ EC2 bảo mật và ALB điều phối thông minh. Hãy chuyển sang **Lab 4** để tích hợp trí tuệ nhân tạo (Gemini API) với cơ chế bất đồng bộ nhé.
