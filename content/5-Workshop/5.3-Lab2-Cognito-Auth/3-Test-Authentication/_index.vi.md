---
title: "3. Kiá»ƒm thá»­ XÃ¡c thá»±c"
weight: 3
chapter: false
pre: " <b> 5.3.3. </b> "
---


Trong pháº§n nÃ y, chÃºng ta sáº½ cháº¡y á»©ng dá»¥ng Frontend á»Ÿ mÃ´i trÆ°á»ng local (hoáº·c truy cáº­p qua domain S3/CloudFront) Ä‘á»ƒ xÃ¡c minh xem káº¿t ná»‘i Ä‘áº¿n Amazon Cognito Ä‘Ã£ hoáº¡t Ä‘á»™ng chÃ­nh xÃ¡c hay chÆ°a.

## BÆ°á»›c 1: Khá»Ÿi cháº¡y Frontend
Náº¿u báº¡n Ä‘ang cháº¡y á»©ng dá»¥ng á»Ÿ mÃ´i trÆ°á»ng local, hÃ£y má»Ÿ terminal vÃ  thá»±c thi:
```bash
npm run dev
```
TrÃ¬nh duyá»‡t sáº½ tá»± Ä‘á»™ng má»Ÿ táº¡i `http://localhost:5173`.
*(LÆ°u Ã½: Náº¿u báº¡n truy cáº­p qua link CloudFront tá»« bÃ i Lab trÆ°á»›c, hÃ£y sá»­ dá»¥ng link Ä‘Ã³).*

## BÆ°á»›c 2: Táº¡o tÃ i khoáº£n má»›i (Sign-up)
1. TrÃªn giao diá»‡n Genzite, nháº¥n nÃºt **Sign Up** (ÄÄƒng kÃ½).
2. Nháº­p má»™t Ä‘á»‹a chá»‰ email há»£p lá»‡ (mÃ  báº¡n cÃ³ thá»ƒ kiá»ƒm tra há»™p thÆ°) vÃ  máº­t kháº©u (Ä‘áº£m báº£o tuÃ¢n thá»§ chÃ­nh sÃ¡ch báº£o máº­t: 8 kÃ½ tá»±, cÃ³ sá»‘, chá»¯ hoa, chá»¯ thÆ°á»ng).
3. Nháº¥n **Create Account**.

## BÆ°á»›c 3: XÃ¡c thá»±c Email (Verification)
1. Sau khi nháº¥n táº¡o tÃ i khoáº£n, giao diá»‡n sáº½ chuyá»ƒn sang mÃ n hÃ¬nh **OTP Verification**.
2. Kiá»ƒm tra Há»™p thÆ° Ä‘áº¿n (Inbox) cá»§a email báº¡n vá»«a Ä‘Äƒng kÃ½. Má»Ÿ email cÃ³ tiÃªu Ä‘á» "Your verification code" Ä‘Æ°á»£c gá»­i tá»« Cognito.
3. Nháº­p mÃ£ code gá»“m 6 chá»¯ sá»‘ vÃ o Ã´ nháº­p liá»‡u trÃªn mÃ n hÃ¬nh.
4. Nháº¥n **Verify**.

![Test Mail Verify 1](/images/5-Workshop/5.3-Lab2-Cognito-Auth/3-Test-Authentication/5.3.3.1.png)

## BÆ°á»›c 4: ÄÄƒng nháº­p vÃ  Kiá»ƒm tra Token
1. Sau khi xÃ¡c thá»±c thÃ nh cÃ´ng, giao diá»‡n sáº½ tá»± Ä‘á»™ng chuyá»ƒn hÆ°á»›ng vá» trang chá»§ hoáº·c mÃ n hÃ¬nh **Sign In**.
2. Nháº­p email vÃ  máº­t kháº©u báº¡n vá»«a Ä‘Äƒng kÃ½.
3. Nháº¥n **Login**.
4. **Kiá»ƒm tra JWT Tokens**:
   - Click chuá»™t pháº£i trÃªn trang web vÃ  chá»n **Inspect** (Kiá»ƒm tra) Ä‘á»ƒ má»Ÿ Developer Tools cá»§a trÃ¬nh duyá»‡t.
   - Chuyá»ƒn sang tab **Application** (hoáº·c Storage).
   - Má»Ÿ má»¥c **Local Storage**, báº¡n sáº½ tháº¥y cÃ¡c key lÆ°u trá»¯ cá»§a Cognito báº¯t Ä‘áº§u báº±ng `CognitoIdentityServiceProvider...`.
   - Nháº¥n vÃ o key cÃ³ chá»©a `accessToken` hoáº·c `idToken`, báº¡n sáº½ tháº¥y má»™t chuá»—i ráº¥t dÃ i (Ä‘Ã³ chÃ­nh lÃ  JWT Token).

## BÆ°á»›c 5: XÃ¡c minh trÃªn AWS Console
Äá»ƒ cháº¯c cháº¯n ráº±ng ngÆ°á»i dÃ¹ng Ä‘Ã£ Ä‘Æ°á»£c táº¡o thÃ nh cÃ´ng trÃªn há»‡ thá»‘ng:
1. Quay láº¡i AWS Management Console vÃ  má»Ÿ dá»‹ch vá»¥ **Cognito**.
2. Nháº¥n vÃ o `genzite-user-pool`.
3. Trong tab **Users**, báº¡n sáº½ tháº¥y Ä‘á»‹a chá»‰ email vá»«a táº¡o cÃ³ tráº¡ng thÃ¡i lÃ  **CONFIRMED**.

![Test Account Cognito](/images/5-Workshop/5.3-Lab2-Cognito-Auth/3-Test-Authentication/5.3.3.2.png)

---
**ChÃºc má»«ng!** TÃ­nh nÄƒng Ä‘Äƒng kÃ½/Ä‘Äƒng nháº­p cá»§a á»©ng dá»¥ng Ä‘Ã£ hoáº¡t Ä‘á»™ng trÆ¡n tru. Vá»›i JWT token nÃ y, ngÆ°á»i dÃ¹ng Ä‘Ã£ cÃ³ thá»ƒ báº¯t Ä‘áº§u sá»­ dá»¥ng cÃ¡c tÃ­nh nÄƒng táº¡o website báº±ng AI cá»§a há»‡ thá»‘ng.

HÃ£y chuyá»ƒn sang **Lab 3** Ä‘á»ƒ xÃ¢y dá»±ng "bá»™ nÃ£o" cá»§a Genzite: **Database vÃ  Backend API**.
