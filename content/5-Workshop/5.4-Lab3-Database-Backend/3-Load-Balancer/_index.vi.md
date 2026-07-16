---
title: "3. Cáº¥u hÃ¬nh Load Balancer"
weight: 3
chapter: false
pre: " <b> 5.4.3. </b> "
---


VÃ¬ mÃ¡y chá»§ EC2 Backend náº±m trong **Private Subnet** (khÃ´ng cÃ³ Public IP), cÃ¡c á»©ng dá»¥ng Frontend tá»« internet khÃ´ng thá»ƒ gá»i trá»±c tiáº¿p vÃ o API cá»§a chÃºng ta. 

Giáº£i phÃ¡p chuáº©n AWS lÃ  sá»­ dá»¥ng má»™t **Application Load Balancer (ALB)** Ä‘áº·t á»Ÿ Public Subnet. ALB sáº½ nháº­n HTTP/HTTPS request tá»« ngoÃ i internet, sau Ä‘Ã³ "chuyá»ƒn tiáº¿p" (forward) vÃ o cho mÃ¡y chá»§ EC2 á»Ÿ bÃªn trong má»™t cÃ¡ch an toÃ n.

## BÆ°á»›c 1: Táº¡o Target Group

Target Group lÃ  má»™t nhÃ³m chá»©a cÃ¡c mÃ¡y chá»§ (EC2) mÃ  ALB sáº½ Ä‘iá»u phá»‘i traffic tá»›i. ChÃºng ta sáº½ táº¡o 2 Target Group: má»™t cho Backend vÃ  má»™t cho Frontend.

### 1.1. Táº¡o Target Group cho Backend
1. Má»Ÿ dá»‹ch vá»¥ **EC2**, cuá»™n xuá»‘ng menu bÃªn trÃ¡i pháº§n **Load Balancing**, chá»n **Target Groups**.
2. Nháº¥n **Create target group**.
3. **Choose a target type**: Chá»n **Instances**.
4. **Target group name**: `genzite-backend-tg`.
![Config Target group](/images/5-Workshop/5.4-Lab3-Database-Backend/3-Load-Balancer/5.4.3.1.png)
5. **Protocol**: `HTTP`. **Port**: `3000` (Port mÃ  Backend API Ä‘ang cháº¡y).
6. **VPC**: Chá»n `genzite-vpc`.
7. **Health checks**: Äá»ƒ máº·c Ä‘á»‹nh (Protocol: HTTP, Path: `/`).
   *(LÆ°u Ã½: API cáº§n cÃ³ route tráº£ vá» status code 200 á»Ÿ Ä‘Æ°á»ng dáº«n `/` Ä‘á»ƒ Health check bÃ¡o Healthy).*
![Config Target group](/images/5-Workshop/5.4-Lab3-Database-Backend/3-Load-Balancer/5.4.3.2.png)
8. Nháº¥n **Next**.
9. Táº¡i mÃ n hÃ¬nh **Register targets**, chá»n mÃ¡y chá»§ `genzite-backend` á»Ÿ danh sÃ¡ch bÃªn dÆ°á»›i.
10. Sá»­a port thÃ nh `3000` vÃ  nháº¥n **Include as pending below**.
11. Cuá»™n xuá»‘ng vÃ  chá»n **Create target group**.

### 1.2. Táº¡o Target Group cho Frontend
1. Tá»« mÃ n hÃ¬nh **Target Groups**, tiáº¿p tá»¥c nháº¥n **Create target group** vÃ  táº¡o tÆ°Æ¡ng tá»± nhÆ° **genzite-backend-tg**.
2. **Choose a target type**: Chá»n **Instances**.
3. **Target group name**: `frontend-tg`.
4. **Protocol**: `HTTP`. **Port**: `5173` (Port mÃ  Frontend Ä‘ang cháº¡y).
5. **VPC**: Chá»n `genzite-vpc`.
6. **Health checks**: Äá»ƒ máº·c Ä‘á»‹nh (Protocol: HTTP, Path: `/`).
7. Nháº¥n **Next**.
8. Táº¡i mÃ n hÃ¬nh **Register targets**, chá»n mÃ¡y chá»§ `genzite-backend` á»Ÿ danh sÃ¡ch bÃªn dÆ°á»›i.
9. Äáº£m báº£o port lÃ  `5173` vÃ  nháº¥n **Include as pending below**.
10. Cuá»™n xuá»‘ng vÃ  chá»n **Create target group**.

## BÆ°á»›c 2: Khá»Ÿi táº¡o Application Load Balancer

1. Truy cáº­p dá»‹ch vá»¥ **EC2**, á»Ÿ menu bÃªn trÃ¡i chá»n **Load Balancers**.
2. Nháº¥n **Create load balancer**.
3. Chá»n **Application Load Balancer** vÃ  nháº¥n **Create**.
4. **Load balancer name**: `genzite-alb`.
5. **Scheme**: Chá»n **Internet-facing**.
![Config Target group](/images/5-Workshop/5.4-Lab3-Database-Backend/3-Load-Balancer/5.4.3.5.png)
6. **Network mapping**:
   - **VPC**: Chá»n `genzite-vpc`.
   - **Mappings**: Chá»n 2 **Availability Zones** vÃ  tÆ°Æ¡ng á»©ng chá»n 2 **Public Subnets**.
![Config Target group](/images/5-Workshop/5.4-Lab3-Database-Backend/3-Load-Balancer/5.4.3.6.png)
7. **Security groups**:
   - Chá»n `genzite-alb-sg`. (Cáº¥u hÃ¬nh Inbound rule cho phÃ©p truy cáº­p HTTP/HTTPS).
8. **Listeners and routing**:
   - **Protocol**: `HTTP`. **Port**: `80`.
   - **Default action**: Chá»n Target group `frontend-tg` (Ä‘á»ƒ dáº«n vÃ o Frontend).
   ![Config Target group](/images/5-Workshop/5.4-Lab3-Database-Backend/3-Load-Balancer/5.4.3.7.png)
9. CÃ¡c pháº§n cÃ²n láº¡i giá»¯ nguyÃªn vÃ  nháº¥n **Create load balancer**.

## BÆ°á»›c 3: Cáº¥u hÃ¬nh Rule chuyá»ƒn tiáº¿p API

Äá»ƒ cÃ¡c request gá»i tá»›i `/api/*` Ä‘Æ°á»£c chuyá»ƒn vÃ o Backend thay vÃ¬ Frontend, ta sáº½ thÃªm má»™t Rule cho ALB.

1. Chá»n vÃ o Load Balancer `genzite-alb` vá»«a táº¡o.
2. á»ž tab **Listeners and rules**, click vÃ o pháº§n `1 rule` (hoáº·c nháº¥n trá»±c tiáº¿p vÃ o listener HTTP:80).
3. Chá»n vÃ o rule **Default** vÃ  báº¥m **Add rule**.
4. Táº¡i pháº§n **Conditions**, báº¥m **Add condition**, chá»n **Path** vÃ  Ä‘iá»n giÃ¡ trá»‹ lÃ  `/api/*`.
5. KÃ©o xuá»‘ng pháº§n **Actions**, chá»n **Forward to** vÃ  chá»n Target group `genzite-backend-tg`.
6. Táº¡i **Rule priority**, Ä‘áº·t Priority lÃ  `1`.
7. Báº¥m **Add rule** Ä‘á»ƒ lÆ°u.
   ![Config Target group](/images/5-Workshop/5.4-Lab3-Database-Backend/3-Load-Balancer/5.4.3.8.png)

Sau khi táº¡o thÃ nh cÃ´ng, ALB cá»§a báº¡n Ä‘Ã£ sáºµn sÃ ng Ä‘iá»u hÆ°á»›ng cÃ¡c truy cáº­p giao diá»‡n vÃ o Frontend, vÃ  cÃ¡c truy cáº­p dá»¯ liá»‡u vÃ o Backend!

---
**HoÃ n thÃ nh Lab 3!** Báº¡n Ä‘Ã£ sá»Ÿ há»¯u má»™t háº¡ táº§ng Backend hoÃ n chá»‰nh gá»“m Database an toÃ n, mÃ¡y chá»§ EC2 báº£o máº­t vÃ  ALB Ä‘iá»u phá»‘i thÃ´ng minh. HÃ£y chuyá»ƒn sang **Lab 4** Ä‘á»ƒ tÃ­ch há»£p trÃ­ tuá»‡ nhÃ¢n táº¡o (Gemini API).
