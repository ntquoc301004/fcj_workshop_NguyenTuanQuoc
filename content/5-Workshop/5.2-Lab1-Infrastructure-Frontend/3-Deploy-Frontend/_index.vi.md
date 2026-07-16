---
title: "3. Triá»ƒn khai Frontend"
weight: 23
chapter: false
pre: "<b>5.2.3. </b>"
---

# 5.2.3 Triá»ƒn khai Frontend

Äá»‘i vá»›i cÃ¡c á»©ng dá»¥ng frontend hiá»‡n Ä‘áº¡i (nhÆ° React, Vue, hoáº·c Angular SPA), viá»‡c triá»ƒn khai lÃªn **Amazon S3 Bucket** vÃ  phÃ¢n phá»‘i qua **Amazon CloudFront** lÃ  best practice trong ngÃ nh. NÃ³ cung cáº¥p kháº£ nÄƒng caching á»Ÿ edge location toÃ n cáº§u, kháº£ nÄƒng má»Ÿ rá»™ng khÃ´ng giá»›i háº¡n vÃ  tÃ­nh nÄƒng chá»‘ng DDoS tÃ­ch há»£p.



## HÆ°á»›ng dáº«n tá»«ng bÆ°á»›c

### 1. Build source code Frontend
Äáº§u tiÃªn, hÃ£y build á»©ng dá»¥ng cá»§a báº¡n á»Ÿ local thÃ nh cÃ¡c file tÄ©nh.

```bash
cd frontend
pnpm install
pnpm run build
```
QuÃ¡ trÃ¬nh nÃ y sáº½ sinh ra má»™t thÆ° má»¥c `dist/` hoáº·c `build/` chá»©a cÃ¡c file HTML, CSS vÃ  JS.

### 2. Táº¡o S3 Bucket
1. Truy cáº­p **S3 Console**.
2. Nháº¥n **Create bucket**.
3. **Bucket name**: Chá»n má»™t tÃªn duy nháº¥t trÃªn toÃ n cáº§u (vÃ­ dá»¥: `workshop-frontend-app-12345`).
4. **Block Public Access settings**: Äá»ƒ nguyÃªn tÃ¹y chá»n "Block all public access" (chÃºng ta sáº½ dÃ¹ng CloudFront OAC Ä‘á»ƒ truy cáº­p báº£o máº­t).
5. Nháº¥n **Create bucket**.

![Create Bucket 1](/images/S3_bucket/bucket_fontend/createbucketfontend1.png)
![Create Bucket 2](/images/S3_bucket/bucket_fontend/createbucketfontend2.png)
![Create Bucket 3](/images/S3_bucket/bucket_fontend/createbucketfontend3.png)

### 3. Upload File lÃªn S3
1. Nháº¥n vÃ o bucket vá»«a táº¡o.
2. Nháº¥n **Upload**.
3. Upload toÃ n bá»™ ná»™i dung *bÃªn trong* thÆ° má»¥c `dist/` hoáº·c `build/`.
4. Nháº¥n **Upload**.

### 3b. Táº¡o S3 Media Bucket
Trong há»‡ thá»‘ng Genzite, Media Bucket dÃ¹ng Ä‘á»ƒ lÆ°u trá»¯ áº£nh/video do ngÆ°á»i dÃ¹ng táº£i lÃªn.
1. Quay láº¡i trang chá»§ **S3 Console**.
2. Nháº¥n **Create bucket**.
3. **Bucket name**: Äáº·t tÃªn (vÃ­ dá»¥: `genzite-media-bucket`).
4. **Object Ownership**: Chá»n `ACLs enabled` (náº¿u muá»‘n dÃ¹ng public read).
5. **Block Public Access settings**: Bá» check "Block all public access" Ä‘á»ƒ cho phÃ©p ngÆ°á»i dÃ¹ng xem áº£nh cÃ´ng khai. XÃ¡c nháº­n rá»§i ro.
6. Nháº¥n **Create bucket**.

![Create Media Bucket 1](/images/S3_bucket/bucket_media/createbucketmedia1.png)
![Create Media Bucket 2](/images/S3_bucket/bucket_media/createbucketmedia2.png)
![Create Media Bucket 3](/images/S3_bucket/bucket_media/createbucketmedia3.png)

Cáº¥u hÃ¬nh CORS cho Media Bucket:
1. Má»Ÿ Media Bucket > Tab **Permissions**.
2. Cuá»™n xuá»‘ng pháº§n **Cross-origin resource sharing (CORS)**, nháº¥n Edit.
3. DÃ¡n Ä‘oáº¡n JSON cáº¥u hÃ¬nh CORS sau Ä‘Ã¢y (cho phÃ©p GET, PUT, POST) vÃ  lÆ°u láº¡i:


![Setup CORS Media](/images/S3_bucket/bucket_media/setupCORSmedia.png)

Cáº¥u hÃ¬nh Bucket Policy Ä‘á»ƒ cho phÃ©p Ä‘á»c cÃ´ng khai (Public Read):
1. Váº«n á»Ÿ tab **Permissions**, cuá»™n lÃªn **Bucket policy**, nháº¥n Edit.
2. DÃ¡n policy sau Ä‘Ã¢y Ä‘á»ƒ cho phÃ©p hÃ nh Ä‘á»™ng `s3:GetObject` tá»« má»i nguá»“n `*`. (LÆ°u Ã½: Nhá»› thay `YOUR_BUCKET_NAME` báº±ng tÃªn tháº­t bucket cá»§a báº¡n):


![Setup Bucket Policy Media](/images/S3_bucket/bucket_media/setupbucketpolicymedia.png)

![Test Media](/images/S3_bucket/bucket_media/test_media_db.png)

### 4. Táº¡o CloudFront Distribution
1. Truy cáº­p **CloudFront Console**.
2. Nháº¥n **Create Distribution**.
3. **Origin domain**: Chá»n S3 bucket cá»§a báº¡n.
4. **Origin access**: Chá»n **Origin access control settings (recommended)**.
   - Nháº¥n **Create control setting** vÃ  lÆ°u láº¡i.
5. **Default cache behavior**:
   - **Viewer protocol policy**: Chá»n Redirect HTTP to HTTPS.
6. **Web Application Firewall (WAF)**: Chá»n "Do not enable security protections" (Ä‘á»ƒ tiáº¿t kiá»‡m chi phÃ­).
7. **Default root object**: Nháº­p `index.html`.
8. Nháº¥n **Create distribution**.

### 5. Cáº­p nháº­t S3 Bucket Policy
CloudFront sáº½ tá»± Ä‘á»™ng sinh ra má»™t Ä‘oáº¡n policy cho S3 bucket Ä‘á»ƒ cáº¥p quyá»n Ä‘á»c. 
1. Táº¡i giao diá»‡n phÃ¢n phá»‘i CloudFront, sau khi táº¡o xong, báº¡n sáº½ tháº¥y thÃ´ng bÃ¡o cáº­p nháº­t policy, hÃ£y nháº¥n **Copy policy**.
2. Quay láº¡i S3 bucket (Frontend) cá»§a báº¡n > tab **Permissions**.
3. Chá»‰nh sá»­a **Bucket policy**, dÃ¡n Ä‘oáº¡n JSON vÃ o vÃ  lÆ°u láº¡i. Äoáº¡n policy Ä‘Ã³ sáº½ cÃ³ cáº¥u trÃºc nhÆ° sau (chá»‰ cho phÃ©p CloudFront Ä‘á»c dá»¯ liá»‡u):


![Setup Bucket Policy Frontend](/images/S3_bucket/bucket_fontend/setupbucketpolicyfontend.png)

### 6. Kiá»ƒm tra á»©ng dá»¥ng Frontend
Khi CloudFront distribution chuyá»ƒn tráº¡ng thÃ¡i Deploy hoÃ n táº¥t, hÃ£y copy **Distribution domain name** (vÃ­ dá»¥: `d12345.cloudfront.net`) vÃ  dÃ¡n vÃ o trÃ¬nh duyá»‡t. á»¨ng dá»¥ng frontend cá»§a báº¡n Ä‘Ã£ hoáº¡t Ä‘á»™ng!

![Test Frontend](/images/S3_bucket/bucket_fontend/test_fontend_db.png)

### 7. Cáº¥u hÃ¬nh Custom Domain vá»›i Route 53 vÃ  ACM (TÃ¹y chá»n)

Äá»ƒ sá»­ dá»¥ng tÃªn miá»n riÃªng (Custom Domain) cho á»©ng dá»¥ng thay vÃ¬ domain máº·c Ä‘á»‹nh cá»§a CloudFront, báº¡n cáº§n cáº¥u hÃ¬nh chá»©ng chá»‰ báº£o máº­t báº±ng **AWS Certificate Manager (ACM)** vÃ  trá» báº£n ghi DNS báº±ng **Amazon Route 53**.

1. **Xin cáº¥p chá»©ng chá»‰ ACM**: 
   - Truy cáº­p giao diá»‡n **ACM Console** vÃ  yÃªu cáº§u cáº¥p chá»©ng chá»‰ public (Request public certificate) cho tÃªn miá»n cá»§a báº¡n.
   - *LÆ°u Ã½ quan trá»ng: Chá»©ng chá»‰ dÃ¹ng cho CloudFront báº¯t buá»™c pháº£i Ä‘Æ°á»£c táº¡o á»Ÿ Region **us-east-1 (N. Virginia)**.*

![Cáº¥u hÃ¬nh ACM](/images/5-Workshop/5.2-Lab1-Infrastructure-Frontend/3-Deploy-Frontend/acm.png)

2. **Cáº­p nháº­t CloudFront**: 
   - Má»Ÿ CloudFront Distribution cá»§a báº¡n, pháº§n **Settings** chá»n Edit. 
   - ThÃªm tÃªn miá»n cá»§a báº¡n vÃ o **Alternate domain name (CNAME)** vÃ  chá»n Custom SSL certificate mÃ  báº¡n vá»«a táº¡o á»Ÿ ACM.

3. **Táº¡o báº£n ghi Route 53**: 
   - Truy cáº­p **Route 53**, má»Ÿ Hosted Zone cá»§a tÃªn miá»n. 
   - Táº¡o má»™t báº£n ghi má»›i (Create record), loáº¡i **A record**, báº­t cÃ´ng táº¯c **Alias** vÃ  trá» (Route traffic to) tá»›i CloudFront distribution cá»§a báº¡n.

![Cáº¥u hÃ¬nh Route 53](/images/5-Workshop/5.2-Lab1-Infrastructure-Frontend/3-Deploy-Frontend/route53.png)
