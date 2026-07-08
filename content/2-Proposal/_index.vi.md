---
title: "Bản đề xuất"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

Tại phần này, bạn cần tóm tắt các nội dung trong workshop mà bạn **dự tính** sẽ làm.

# Genzite: Nền tảng No-Code tạo ứng dụng bằng AI thế hệ mới
## Giải pháp hạ tầng đám mây AWS Cloud-Native cho việc tạo ứng dụng tự động bằng AI và tích hợp Trí tuệ Tuyển dụng

### 1. Tóm tắt điều hành
Genzite là nền tảng AI No-Code thế hệ mới được thiết kế để hỗ trợ những người dùng không có nền tảng kỹ thuật tự xây dựng, vận hành và quản lý các ứng dụng web hoàn chỉnh thông qua giao tiếp bằng ngôn ngữ tự nhiên. Khác với các công cụ tạo trang web tĩnh thông thường, Genzite có khả năng tự động tạo giao diện Frontend, các API Backend tùy chỉnh, cấu trúc cơ sở dữ liệu động (CMS) và các luồng quy trình nghiệp vụ (workflow). 

Đồng thời, Genzite tích hợp bộ công cụ Trí tuệ Tuyển dụng AI (AI Recruitment Intelligence) bao gồm: Tự động thiết lập CV (Resume Builder), đánh giá độ tương thích giữa CV và mô tả công việc (CV-to-JD Matcher), và mô phỏng phỏng vấn trực tiếp với AI (Mock Interview). Hệ thống được triển khai trên nền tảng AWS bằng kiến trúc monorepo chứa các microservices (NestJS, React 18, Kafka, Redis và BullMQ), sử dụng mô hình cơ sở dữ liệu lai (Relational SQL + PostgreSQL JSONB) và tích hợp các mô hình ngôn ngữ lớn Dual-LLM (Google Gemini & Groq Llama3). Khả năng bảo mật, điều hướng lưu lượng, lưu trữ đệm và mở rộng quy mô được quản lý bởi các dịch vụ AWS như Route 53, CloudFront, Cognito, ALB, EC2, RDS PostgreSQL và ElastiCache.

### 2. Tuyên bố vấn đề
#### Vấn đề hiện tại
Quy trình phát triển phần mềm và xây dựng ứng dụng web tùy chỉnh đòi hỏi kỹ năng lập trình chuyên nghiệp, ngân sách lớn và thời gian phát triển kéo dài. Các công cụ kéo thả hiện nay (như WordPress, Wix) bị giới hạn bởi các mẫu giao diện có sẵn và không hỗ trợ thiết kế database động, tự động viết API backend, thiết lập quy trình nghiệp vụ phức tạp hoặc cung cấp các tính năng AI chuyên sâu (như phân tích CV, phỏng vấn thử). Thêm vào đó, việc thực hiện di chuyển cơ sở dữ liệu (migration) thủ công mỗi khi thay đổi cấu trúc dữ liệu khiến quản trị viên không chuyên gặp nhiều rủi ro và làm gián đoạn hệ thống.

#### Giải pháp
Genzite giải quyết những thách thức này nhờ vào kiến trúc Dual-LLM (sử dụng Google Gemini để suy luận/viết code và Groq Llama3 để kiểm duyệt thiết kế/phản hồi nhanh) nhằm chuyển đổi trực tiếp yêu cầu bằng chữ của người dùng thành các thành phần ứng dụng hoàn chỉnh. Nhằm loại bỏ việc chạy migration database thủ công, hệ thống áp dụng cấu trúc dữ liệu động thông qua cột JSONB của PostgreSQL để lưu trữ cấu trúc CMS và hồ sơ ứng viên một cách linh hoạt theo thời gian thực (runtime).

Để vận hành nền tảng này ổn định, an toàn và tiết kiệm chi phí, Genzite tận dụng các dịch vụ cloud-native của AWS:
- **Phân phối phía Client**: Các tài nguyên tĩnh của ứng dụng React SPA được lưu trữ tại Amazon S3 và phân phối toàn cầu qua Amazon CloudFront CDN.
- **Lớp tính toán (Compute Layer)**: Các microservice NestJS chạy trong mạng con riêng tư (private subnets) trên các máy ảo EC2 đứng sau bộ cân bằng tải Application Load Balancer (ALB).
- **Lớp dữ liệu (Data Layer)**: Dữ liệu quan hệ hệ thống được lưu trong Amazon RDS PostgreSQL, trong khi dữ liệu CMS động sử dụng cột JSONB. Việc lưu trữ cache phiên làm việc, cache mã băm prompt AI và quản lý hàng đợi tác vụ nặng được thực hiện bằng Amazon ElastiCache Redis (BullMQ).
- **Liên kết AI bên ngoài**: Các truy vấn gửi tới Google Gemini và Groq API được định tuyến an toàn ra ngoài internet qua NAT Gateway từ các private subnets.
- **Bảo mật và Phân quyền**: Được kiểm soát chặt chẽ bởi Amazon Cognito nhằm xác thực tài khoản và quản lý vai trò người dùng (RBAC).

#### Lợi ích và hoàn vốn đầu tư (ROI)
Giải pháp Genzite AWS giúp các doanh nghiệp và nhà sáng tạo xây dựng và vận hành các hệ thống chuyên biệt (như trang thương mại điện tử, cổng tuyển dụng, bảng điều khiển nội bộ) chỉ trong vài giây thay vì vài tuần. Cơ chế tải tệp tin đa phương tiện trực tiếp lên Amazon S3 bằng Presigned URL giúp giải phóng hoàn toàn băng thông và tài nguyên tính toán của máy chủ backend.

Về mặt chi phí vận hành hạ tầng, Genzite mang đến hai lộ trình triển khai linh hoạt:
- **Cấu hình thử nghiệm (MVP)**: Phục vụ chạy thử và demo với chi phí tối ưu chỉ từ **~$35–$60/tháng** nhờ sử dụng các máy ảo cấu hình nhỏ Single-AZ, bỏ qua NAT Gateway và cụm Redis dùng riêng.
- **Cấu hình vận hành (Production)**: Có khả năng tự động mở rộng (Auto Scaling), dự phòng Multi-AZ và cô lập mạng lưới an toàn với mức chi phí khoảng **~$150–$350/tháng**.
Thời gian hoàn vốn ước tính đạt từ 3–6 tháng nhờ tối giản nhân sự phát triển và rút ngắn tối đa thời gian đưa sản phẩm ra thị trường.

### 3. Kiến trúc giải pháp
Hệ thống sử dụng thiết kế phân lớp bảo mật trên AWS giúp điều phối lưu lượng truy cập an toàn, tối ưu hóa tốc độ tải trang tĩnh và cô lập hoàn toàn cơ sở dữ liệu và máy chủ ứng dụng khỏi internet công cộng.

#### Dịch vụ AWS sử dụng
- **Amazon Route 53**: Quản lý tên miền tùy chỉnh và điều hướng phân giải DNS tới CDN CloudFront.
- **Amazon CloudFront**: Cache và phân phối React SPA trên toàn cầu, tích hợp chứng chỉ SSL/TLS từ AWS Certificate Manager (ACM). Tỷ lệ cache hit đạt mục tiêu 80-90% giúp giảm tải tối đa cho máy chủ gốc.
- **Amazon S3**: Lưu trữ mã nguồn tĩnh (Frontend Bucket) và bảo mật các tệp tải lên như CV, hình ảnh (Media Bucket) bằng cơ chế Presigned URL có giới hạn thời gian.
- **Amazon Cognito**: Quản lý xác thực người dùng hệ thống và kiểm soát phân quyền truy cập.
- **Application Load Balancer (ALB)**: Tiếp nhận các yêu cầu API `/api/*`, thực hiện giải mã SSL và điều hướng lưu lượng tới các máy ảo EC2 khỏe mạnh trong private subnet.
- **Amazon EC2 Auto Scaling**: Quản lý nhóm máy ảo sử dụng dòng chip Graviton (`t4g.small` đến `t4g.large`) chạy các module NestJS trong các private subnet riêng biệt.
- **Amazon RDS PostgreSQL**: Lưu trữ dữ liệu quan hệ (tài khoản, cài đặt hệ thống) kết hợp các bảng JSONB lưu dữ liệu động của CMS người dùng và lịch sử ứng viên.
- **Amazon ElastiCache Redis**: Tối ưu tốc độ phản hồi qua cache session, cache kết quả prompt AI và quản lý hàng đợi BullMQ cho các tác vụ xử lý AI chạy ngầm.
- **NAT Gateway**: Cho phép máy chủ EC2 trong private subnet kết nối internet một chiều an toàn để gọi các API AI (Gemini/Groq).

#### Thiết kế thành phần
Genzite bao gồm các dịch vụ backend chuyên biệt giao tiếp hiệu quả với nhau:
- **Identity Service**: Đăng ký, đăng nhập, cấp phát mã JWT và quản lý không gian làm việc (workspace).
- **Site Service**: Quản lý thông tin cấu hình trang web, các widget giao diện kéo thả.
- **Data Service**: Động cơ quản lý dữ liệu CMS động, thực hiện đọc/ghi dữ liệu thông qua cấu trúc JSONB.
- **Media Service**: Cấp phát S3 Presigned URL để client tải trực tiếp file lên S3 mà không cần đi qua backend.
- **Notification Service**: Lắng nghe sự kiện từ Kafka để tự động gửi email chào mừng, thông báo kết quả phân tích CV hoặc báo cáo phỏng vấn.
- **AI Service**: Điều phối kết nối đến Gemini/Groq, quản lý hàng đợi BullMQ để phân tích CV, khớp kỹ năng CV-JD và tạo câu hỏi phỏng vấn thử.
- **Commerce Service**: Quản lý giỏ hàng, tạo đơn hàng và kết nối với cổng PayOS để xử lý thanh toán trực tuyến.

---

### 4. Triển khai kỹ thuật
#### Các giai đoạn triển khai
Quy trình thiết lập hệ thống hạ tầng của Genzite trải qua 4 giai đoạn cụ thể:
1. **Giai đoạn 1: Thiết kế kiến trúc và Mô hình hóa (Tháng 0)**
   - Xác định ranh giới giữa các dịch vụ, phác thảo sơ đồ ERD của database và phân bổ địa chỉ IP trong mạng công cộng/riêng tư (VPC).
2. **Giai đoạn 2: Tính toán chi phí và Tính khả thi (Tháng 1)**
   - Sử dụng công cụ AWS Pricing Calculator để lên dự toán chi phí cụ thể và cân bằng ngân sách giữa bản thử nghiệm MVP và bản Production thực tế.
3. **Giai đoạn 3: Thiết lập hạ tầng và Cô lập bảo mật (Tháng 2)**
   - Khởi tạo VPC, cấu hình các luật Security Group (chỉ cho phép EC2 truy cập Database, chỉ cho phép ALB truy cập EC2) và thiết lập chính sách CloudFront OAI truy cập S3 Frontend.
4. **Giai đoạn 4: Triển khai dịch vụ, Tích hợp và Kiểm thử (Tháng 2–3)**
   - Triển khai các container NestJS qua Docker Compose / AWS ECS, thiết lập các Kafka topics, deploy frontend React lên S3/CloudFront và tiến hành kiểm tra tải cho luồng sinh web bằng AI.

#### Yêu cầu kỹ thuật
- **Frontend**: Sử dụng React 18, Vite, TypeScript, Tailwind CSS v4. Hỗ trợ canvas vẽ dynamic widgets và upload file trực tiếp tới S3 qua presigned URL.
- **Backend**: NestJS, Prisma ORM, Kafka (làm event bus truyền tin giữa các dịch vụ), BullMQ kết hợp Redis (để quản lý hàng đợi AI worker).
- **Cơ sở dữ liệu**: PostgreSQL hỗ trợ kiểu dữ liệu JSONB và Redis để lưu trữ cache.
- **AI Engine**: Google Gemini API, Groq Llama3 SDK và Model Context Protocol (MCP) Client/Server.

### 5. Lộ trình & Mốc triển khai
- **Tháng 0 (Chuẩn bị)**: Thiết kế các biểu đồ C4, xây dựng tài liệu đặc tả OpenAPI và chuẩn bị môi trường Docker Compose local cho lập trình viên.
- **Tháng 1 (Giai đoạn 1: Hạ tầng lõi & Xác thực)**: Triển khai Route 53, S3, RDS, và API Gateway trên AWS. Hoàn thành Identity Service (đăng nhập JWT và phân quyền).
- **Tháng 2 (Giai đoạn 2: Trình dựng web & CMS động)**: Triển khai Site Service và Data Service. Hoàn thiện API đọc/ghi JSONB và tính năng cấp Presigned URL tải file của Media Service.
- **Tháng 3 (Giai đoạn 3: Tích hợp AI, Thanh toán & Vận hành)**: Thiết lập hệ thống AI Service ngầm bằng BullMQ. Kết nối Google Gemini API để tự động sinh cấu trúc website. Tích hợp thanh toán PayOS. Tiến hành kiểm thử hệ thống, rà soát Security Group và chính thức vận hành.
- **Sau vận hành (Tháng 4 trở đi)**: Giám sát hiệu năng hệ thống, theo dõi tỷ lệ cache hit của CloudFront và tối ưu hóa chỉ mục (indexing) cơ sở dữ liệu trên các cột JSONB.

### 6. Ước tính ngân sách
Bảng so sánh chi phí hạ tầng hàng tháng giữa cấu hình MVP (Staging/Demo) và cấu hình Production trên AWS:

| Thành phần AWS | Cấu hình MVP (Staging/Demo) | Cấu hình Production |
|---|---|---|
| **Máy chủ (EC2)** | Single `t4g.small` (~$12/tháng) | Nhóm Auto Scaling máy ảo `t4g.medium`/`t4g.large` |
| **Cân bằng tải** | ❌ Không sử dụng (Kết nối trực tiếp EC2) | ✅ ALB hỗ trợ HTTPS và ACM (~$22/tháng) |
| **NAT Gateway** | ❌ Không sử dụng (EC2 ở public subnet để ra mạng) | ✅ NAT Gateway tại public subnet (~$32/tháng + cước truyền tải) |
| **Cơ sở dữ liệu (RDS)** | Single-AZ `db.t4g.micro` (~$13/tháng) | Multi-AZ `db.t4g.small` hoặc `db.t4g.medium` (~$60+/tháng) |
| **Bộ nhớ đệm (Redis)** | ❌ Dùng chung bộ nhớ trong EC2 | ✅ Cụm Amazon ElastiCache Redis độc lập (~$16/tháng) |
| **Lưu trữ S3** | ✅ Standard tier (~$2/tháng) | ✅ Cấu hình quy trình lưu trữ tự động Standard → IA → Glacier (~$10/tháng) |
| **CloudFront CDN** | ✅ Free tier (Tận dụng gói miễn phí) | ✅ CloudFront CDN đầy đủ kết hợp AWS WAF bảo mật (~$20/tháng) |
| **Tổng cộng ước tính** | **~$35–$60 / tháng** | **~$150–$350 / tháng** |

- **Liên kết dự toán chi phí**: Chi tiết cấu hình được xây dựng trên [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=621f38b12a1ef026842ba2ddfe46ff936ed4ab01).

---

### 7. Đánh giá rủi ro
#### Ma trận rủi ro
| Rủi ro phát sinh | Xác suất | Mức ảnh hưởng | Phương án giảm thiểu |
|---|---|---|---|
| **Vượt ngưỡng giới hạn gọi API AI (Rate Limit)** | Cao | Cao | Thiết lập nhóm tài khoản API Key luân phiên theo vòng (round-robin). Sử dụng Redis lưu mã băm prompt để trả về kết quả cũ đối với yêu cầu trùng lặp mà không cần gọi lại LLM. |
| **Suy giảm hiệu năng truy vấn database** | Trung bình | Cao | Giới hạn độ sâu của tệp tin JSONB. Khởi tạo chỉ mục biểu thức (expression index) trên PostgreSQL cho các trường được tìm kiếm nhiều (như `ats_scores` hoặc `site_id` bên trong dữ liệu JSONB). |
| **Tệp tin tải lên S3 độc hại / Quá kích thước** | Trung bình | Trung bình | Kiểm tra đuôi file và kiểu mime-type ngay tại Media Service trước khi phát hành Presigned URL. Cài đặt luật tự động xóa file tạm trên S3. |
| **Độ trễ phản hồi từ API AI cao (10–15 giây)** | Cao | Trung bình | Chuyển đổi toàn bộ luồng tạo AI sang bất đồng bộ. Sử dụng BullMQ để xử lý ngầm và gửi thông báo cập nhật tiến trình qua SSE/Kafka events. |

#### Kế hoạch dự phòng
- Trong trường hợp Google Gemini gặp sự cố, hệ thống sẽ tự động chuyển đổi luồng xử lý sang API dự phòng của Groq (Llama3) hoặc DeepSeek nhằm đảm bảo nền tảng hoạt động liên tục.
- Hệ thống hạ tầng AWS được lưu trữ dưới dạng các tệp cấu hình AWS CloudFormation giúp đội ngũ kỹ thuật có thể khôi phục hoặc tạo mới toàn bộ môi trường staging sạch trong vòng 15 phút nếu có sự cố nghiêm trọng xảy ra.

### 8. Kết quả kỳ vọng
- **Tạo ứng dụng hoàn chỉnh không cần code**: Người dùng có thể khởi tạo một website đa trang đi kèm hệ thống quản lý nội dung (CMS) động hoàn toàn từ mô tả chữ trong vòng 20 giây.
- **Tiết kiệm băng thông máy chủ**: Cơ chế đẩy tệp trực tiếp lên S3 giúp cắt giảm tới 90% dung lượng băng thông tiêu thụ trên máy chủ EC2.
- **Xử lý giao dịch an toàn, tốc độ**: Hệ thống mạng lưới phân lớp bảo mật cao giúp cô lập an toàn dữ liệu khách hàng và tích hợp cổng thanh toán trực tiếp qua PayOS ổn định.
- **Khả năng mở rộng microservices linh hoạt**: Việc tổ chức dự án monorepo với pnpm workspace giúp Genzite duy trì mã nguồn sạch sẽ, sẵn sàng chia tách các module hiện tại thành các container microservice độc lập khi quy mô người dùng tăng trưởng mạnh.