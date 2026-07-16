---
title: "2. TÃ­ch há»£p á»¨ng dá»¥ng"
weight: 2
chapter: false
pre: " <b> 5.3.2. </b> "
---


Sau khi User Pool Ä‘Ã£ sáºµn sÃ ng, bÆ°á»›c tiáº¿p theo lÃ  láº¥y cÃ¡c thÃ´ng sá»‘ káº¿t ná»‘i Ä‘á»ƒ Ä‘Æ°a vÃ o mÃ£ nguá»“n Frontend (React). AWS cung cáº¥p thÆ° viá»‡n `aws-amplify` giÃºp viá»‡c gá»i cÃ¡c hÃ m xÃ¡c thá»±c (Ä‘Äƒng kÃ½/Ä‘Äƒng nháº­p) trá»Ÿ nÃªn vÃ´ cÃ¹ng Ä‘Æ¡n giáº£n.

## BÆ°á»›c 1: Láº¥y User Pool ID vÃ  Client ID

1. Trong console cá»§a **Cognito**, nháº¥n vÃ o `genzite-user-pool` báº¡n vá»«a táº¡o.
2. Copy **User pool ID** (cÃ³ dáº¡ng `us-east-1_xxxxxxxxx`) vÃ  lÆ°u ra má»™t file text táº¡m.
3. Chuyá»ƒn sang tab **App integration**.
4. KÃ©o xuá»‘ng má»¥c **App client list**, báº¡n sáº½ tháº¥y `genzite-web-app`.
5. Copy **Client ID** (má»™t chuá»—i gá»“m chá»¯ vÃ  sá»‘ khoáº£ng 26 kÃ½ tá»±) vÃ  lÆ°u láº¡i.

## BÆ°á»›c 2: Cáº¥u hÃ¬nh biáº¿n mÃ´i trÆ°á»ng á»Ÿ Frontend

Trong thÆ° má»¥c mÃ£ nguá»“n Frontend cá»§a Genzite, tÃ¬m file `.env` (táº¡o file `.env` má»›i á»Ÿ thÆ° má»¥c gá»‘c cá»§a project náº¿u chÆ°a cÃ³).

DÃ¡n cÃ¡c thÃ´ng tin vá»«a láº¥y Ä‘Æ°á»£c vÃ o file nÃ y:

![Setup Cognito Environment](/images/5-Workshop/5.3-Lab2-Cognito-Auth/2-App-Integration/5.3.2.1.png)

*(LÆ°u Ã½: Thay tháº¿ cÃ¡c giÃ¡ trá»‹ báº±ng User Pool ID vÃ  Client ID thá»±c táº¿ cá»§a báº¡n).*

## BÆ°á»›c 3: CÃ i Ä‘áº·t vÃ  TÃ­ch há»£p AWS Amplify

Äá»ƒ káº¿t ná»‘i tá»›i Cognito tá»« React, dá»± Ã¡n sáº½ cÃ i Ä‘áº·t thÆ° viá»‡n sau:
```bash
npm install aws-amplify
```
![Run terminal Cognito](/images/5-Workshop/5.3-Lab2-Cognito-Auth/2-App-Integration/5.3.2.2.png)

Trong file Ä‘áº§u vÃ o cá»§a á»©ng dá»¥ng (vÃ­ dá»¥: `main.tsx` hoáº·c `App.tsx`), Amplify Ä‘Æ°á»£c cáº¥u hÃ¬nh nhÆ° sau:

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

*(Hoáº·c náº¿u báº¡n Ä‘ang sá»­ dá»¥ng `react-oidc-context`, cáº¥u hÃ¬nh sáº½ trÃ´ng giá»‘ng nhÆ° tháº¿ nÃ y):*

![Cáº¥u hÃ¬nh React OIDC](/images/5-Workshop/5.3-Lab2-Cognito-Auth/2-App-Integration/5.3.2.3.png)

Tá»« giá» trá»Ÿ Ä‘i, má»—i khi ngÆ°á»i dÃ¹ng gá»i hÃ m `signIn({ username, password })` tá»« thÆ° viá»‡n Amplify, Frontend sáº½ tá»± Ä‘á»™ng gá»i API lÃªn AWS Cognito Ä‘á»ƒ xÃ¡c thá»±c vÃ  nháº­n vá» **JWT Token**.

---
Viá»‡c cáº¥u hÃ¬nh káº¿t ná»‘i Ä‘Ã£ hoÃ n táº¥t. Trong pháº§n tiáº¿p theo, chÃºng ta sáº½ **Kiá»ƒm thá»­ luá»“ng ÄÄƒng nháº­p/ÄÄƒng kÃ½** trá»±c tiáº¿p tá»« giao diá»‡n nhÃ©!
