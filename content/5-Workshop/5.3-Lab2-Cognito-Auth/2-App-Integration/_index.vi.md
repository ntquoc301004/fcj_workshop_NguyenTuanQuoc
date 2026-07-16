---
title: "2. Tích hợp Ứng dụng"
weight: 2
chapter: false
pre: " <b> 5.3.2. </b> "
---


Sau khi User Pool đã sẵn sàng, bước tiếp theo là lấy các thông số kết nối để đưa vào mã nguồn Frontend (React). AWS cung cấp thư viện `aws-amplify` giúp việc gọi các hàm xác thực (đăng ký/đăng nhập) trở nên vô cùng đơn giản.

## Bước 1: Lấy User Pool ID và Client ID

1. Trong console của **Cognito**, nhấn vào `genzite-user-pool` bạn vừa tạo.
2. Copy **User pool ID** (có dạng `us-east-1_xxxxxxxxx`) và lưu ra một file text tạm.
3. Chuyển sang tab **App integration**.
4. Kéo xuống mục **App client list**, bạn sẽ thấy `genzite-web-app`.
5. Copy **Client ID** (một chuỗi gồm chữ và số khoảng 26 ký tự) và lưu lại.

## Bước 2: Cấu hình biến môi trường ở Frontend

Trong thư mục mã nguồn Frontend của Genzite, tìm file `.env` (tạo file `.env` mới ở thư mục gốc của project nếu chưa có).

Dán các thông tin vừa lấy được vào file này:

![Setup Cognito Environment](/images/5-Workshop/5.3-Lab2-Cognito-Auth/2-App-Integration/5.3.2.1.png)

*(Lưu ý: Thay thế các giá trị bằng User Pool ID và Client ID thực tế của bạn).*

## Bước 3: Cài đặt và Tích hợp AWS Amplify

Để kết nối tới Cognito từ React, dự án sẽ cài đặt thư viện sau:
```bash
npm install aws-amplify
```
![Run terminal Cognito](/images/5-Workshop/5.3-Lab2-Cognito-Auth/2-App-Integration/5.3.2.2.png)

Trong file đầu vào của ứng dụng (ví dụ: `main.tsx` hoặc `App.tsx`), Amplify được cấu hình như sau:

```typescript
import { Amplify } from 'aws-amplify';

Amplify.configure({
  Auth: {
    Cognito: {
      userPoolId: import.meta.env.AWS_COGNITO_USER_POOL_ID,
      userPoolClientId: import.meta.env.AWS_COGNITO_CLIENT_ID,
      signUpVerificationMethod: 'code',
    }
  }
});
```

*(Hoặc nếu bạn đang sử dụng `react-oidc-context`, cấu hình sẽ trông giống như thế này):*

![Cấu hình React OIDC](/images/5-Workshop/5.3-Lab2-Cognito-Auth/2-App-Integration/5.3.2.3.png)

Từ giờ trở đi, mỗi khi người dùng gọi hàm `signIn({ username, password })` từ thư viện Amplify, Frontend sẽ tự động gọi API lên AWS Cognito để xác thực và nhận về **JWT Token**.

---
Việc cấu hình kết nối đã hoàn tất. Trong phần tiếp theo, chúng ta sẽ **Kiểm thử luồng Đăng nhập/Đăng ký** trực tiếp từ giao diện nhé!
