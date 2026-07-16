---
title: "1. Táº¡o User Pool"
weight: 1
chapter: false
pre: " <b> 5.3.1. </b> "
---


Trong pháº§n nÃ y, chÃºng ta sáº½ táº¡o má»™t User Pool Ä‘á»ƒ lÆ°u trá»¯ vÃ  quáº£n lÃ½ tÃ i khoáº£n ngÆ°á»i dÃ¹ng an toÃ n.

## BÆ°á»›c 1: Khá»Ÿi táº¡o User Pool
1. Truy cáº­p vÃ o dá»‹ch vá»¥ **Cognito** trÃªn giao diá»‡n AWS Management Console.
2. Äáº£m báº£o báº¡n Ä‘ang á»Ÿ Ä‘Ãºng Region `us-east-1` (US East N. Virginia).
3. Nháº¥n vÃ o nÃºt **Create user pool**.

## BÆ°á»›c 2: Cáº¥u hÃ¬nh tráº£i nghiá»‡m Ä‘Äƒng nháº­p (Sign-in experience)
1. **Cognito user pool sign-in options**: ÄÃ¡nh dáº¥u chá»n vÃ o **Email**. NgÆ°á»i dÃ¹ng sáº½ sá»­ dá»¥ng Ä‘á»‹a chá»‰ email lÃ m tÃªn Ä‘Äƒng nháº­p.
2. Giá»¯ nguyÃªn cÃ¡c thiáº¿t láº­p khÃ¡c vÃ  nháº¥n **Next**.

## BÆ°á»›c 3: Cáº¥u hÃ¬nh yÃªu cáº§u báº£o máº­t (Security requirements)
1. **Password policy**: Äá»ƒ máº·c Ä‘á»‹nh (Cognito defaults) yÃªu cáº§u tá»‘i thiá»ƒu 8 kÃ½ tá»±, cÃ³ sá»‘, kÃ½ tá»± Ä‘áº·c biá»‡t, chá»¯ in hoa, in thÆ°á»ng.
2. **Multi-factor authentication (MFA)**: Chá»n **No MFA** (KhÃ´ng dÃ¹ng xÃ¡c thá»±c 2 bÆ°á»›c Ä‘á»ƒ giá»¯ bÃ i Lab Ä‘Æ¡n giáº£n, dá»… test).
3. **User account recovery**: Chá»n **Email only**.
4. Nháº¥n **Next**.

## BÆ°á»›c 4: Cáº¥u hÃ¬nh tráº£i nghiá»‡m Ä‘Äƒng kÃ½ (Sign-up experience)
1. **Self-service sign-up**: TÃ­ch chá»n **Enable self-registration** (Cho phÃ©p ngÆ°á»i dÃ¹ng tá»± do Ä‘Äƒng kÃ½ tÃ i khoáº£n tá»« web).
2. **Cognito-assisted verification and confirmation**: Äá»ƒ máº·c Ä‘á»‹nh (Allow Cognito to automatically send messages to verify and confirm).
3. **Required attributes**: Chá»n **email** (báº¯t buá»™c cung cáº¥p email khi Ä‘Äƒng kÃ½).
4. Nháº¥n **Next**.

## BÆ°á»›c 5: Cáº¥u hÃ¬nh gá»­i thÃ´ng bÃ¡o (Message delivery)
1. **Email provider**: Chá»n **Send email with Cognito** (ÄÃ¢y lÃ  tuá»³ chá»n miá»…n phÃ­, cho phÃ©p gá»­i tá»‘i Ä‘a 50 email má»—i ngÃ y - hoÃ n toÃ n phÃ¹ há»£p cho má»¥c Ä‘Ã­ch thá»±c hÃ nh).
2. Nháº¥n **Next**.

## BÆ°á»›c 6: TÃ­ch há»£p á»©ng dá»¥ng (Integrate your app)
1. **User pool name**: Nháº­p tÃªn gá»£i nhá»›, vÃ­ dá»¥: `genzite-user-pool`.
2. **Hosted authentication pages**: KhÃ´ng chá»n (ChÃºng ta sáº½ dÃ¹ng giao diá»‡n Ä‘Äƒng nháº­p tá»± code báº±ng React thay vÃ¬ dÃ¹ng Hosted UI cá»§a AWS).
3. **Initial app client**: Chá»n **Public client**.
4. **App client name**: Nháº­p `genzite-web-app`.
5. **Client secret**: Chá»n **Don't generate a client secret** (Ráº¤T QUAN TRá»ŒNG: MÃ´i trÆ°á»ng Frontend nhÆ° React/SPA khÃ´ng báº£o máº­t Ä‘Æ°á»£c client secret, náº¿u táº¡o secret thÃ¬ frontend sáº½ khÃ´ng gá»i API Ä‘Æ°á»£c).
6. Nháº¥n **Next**.

![Create Cognito 1](/images/5-Workshop/5.3-Lab2-Cognito-Auth/1-Create-UserPool/5.3.1.1.png)

![Create Cognito 2](/images/5-Workshop/5.3-Lab2-Cognito-Auth/1-Create-UserPool/5.3.1.2.png)

## BÆ°á»›c 7: Xem láº¡i vÃ  táº¡o
1. Kiá»ƒm tra láº¡i toÃ n bá»™ thÃ´ng tin Ä‘Ã£ cáº¥u hÃ¬nh.
2. KÃ©o xuá»‘ng dÆ°á»›i cÃ¹ng vÃ  nháº¥n **Create user pool**.

---
Váº­y lÃ  báº¡n Ä‘Ã£ cÃ³ má»™t "kho chá»©a" tÃ i khoáº£n ngÆ°á»i dÃ¹ng an toÃ n! HÃ£y chuyá»ƒn sang bÆ°á»›c tiáº¿p theo Ä‘á»ƒ láº¥y thÃ´ng tin káº¿t ná»‘i vÃ  **tÃ­ch há»£p vÃ o mÃ£ nguá»“n Frontend**.
