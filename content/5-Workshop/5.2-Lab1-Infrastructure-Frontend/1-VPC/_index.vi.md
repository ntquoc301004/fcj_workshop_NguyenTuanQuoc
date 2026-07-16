---
title: "1. Cáº¥u hÃ¬nh VPC"
weight: 1
chapter: false
pre: " <b> 5.2.1. </b> "
---


Trong pháº§n nÃ y, chÃºng ta sáº½ táº¡o vÃ  cáº¥u hÃ¬nh Virtual Private Cloud (VPC) cho háº¡ táº§ng cá»§a mÃ¬nh. Viá»‡c táº¡o VPC Ä‘Ã³ng vai trÃ² ná»n táº£ng máº¡ng (network foundation) Ä‘á»ƒ triá»ƒn khai cÃ¡c dá»‹ch vá»¥ nhÆ° EC2 má»™t cÃ¡ch an toÃ n.

## Má»¥c tiÃªu
- Táº¡o má»™t VPC tuá»³ chá»‰nh vá»›i dáº£i máº¡ng (CIDR) lÃ  `10.0.0.0/16`.
- Cáº¥u hÃ¬nh 2 Public Subnet vÃ  2 Private Subnet tráº£i rá»™ng trÃªn 2 Availability Zone.
- Thiáº¿t láº­p Internet Gateway (IGW) cho phÃ©p Public Subnet truy cáº­p internet.
- Thiáº¿t láº­p NAT Gateway Ä‘á»ƒ Private Subnet cÃ³ thá»ƒ truy cáº­p ra internet an toÃ n.
- Thiáº¿t láº­p S3 Gateway Endpoint Ä‘á»ƒ truy cáº­p dá»‹ch vá»¥ S3 trá»±c tiáº¿p tá»« VPC mÃ  khÃ´ng qua internet.

## BÆ°á»›c 1: Táº¡o VPC

1. Truy cáº­p vÃ o **AWS Management Console**.
2. TÃ¬m kiáº¿m dá»‹ch vá»¥ **VPC** trÃªn thanh cÃ´ng cá»¥ tÃ¬m kiáº¿m vÃ  chá»n **VPC**.
3. á»ž menu bÃªn trÃ¡i, chá»n **Your VPCs**.
4. Nháº¥n nÃºt **Create VPC** á»Ÿ gÃ³c trÃªn bÃªn pháº£i.
5. Cáº¥u hÃ¬nh cÃ¡c thÃ´ng sá»‘ theo Ä‘Ãºng 2 hÃ¬nh minh hoáº¡ dÆ°á»›i Ä‘Ã¢y:
   - **VPC settings**: Chá»n **VPC and more** (Ä‘á»ƒ táº¡o luÃ´n Subnet, Route Table vÃ  Gateway).
   - **Name tag auto-generation**: Nháº­p tÃªn VPC cá»§a báº¡n lÃ  `genzite`.
   - **IPv4 CIDR block**: `10.0.0.0/16`.

![Create VPC Step 1](/images/5-Workshop/5.2-Lab1-Infrastructure-Frontend/1-VPC/create-vpc-step1.png)

   - **Number of Availability Zones (AZs)**: `2`.
   - **Number of public subnets**: `2`.
   - **Number of private subnets**: `2`.
   - **NAT gateways ($)**: Chá»n **Zonal** vÃ  **In 1 AZ** (Äá»ƒ táº¡o NAT Gateway cho Private Subnet).
   - **VPC endpoints**: Chá»n **S3 Gateway**.
   - **DNS options**: Äáº£m báº£o Ä‘Ã£ tÃ­ch chá»n **Enable DNS hostnames** vÃ  **Enable DNS resolution**.

![Create VPC Step 2](/images/5-Workshop/5.2-Lab1-Infrastructure-Frontend/1-VPC/create-vpc-step2.png)

6. Kiá»ƒm tra láº¡i cáº¥u hÃ¬nh á»Ÿ khung preview bÃªn pháº£i vÃ  nháº¥n nÃºt **Create VPC**.

### Khá»Ÿi táº¡o NAT Gateway
Trong trÆ°á»ng há»£p báº¡n chá»n **None** á»Ÿ pháº§n NAT gateways khi táº¡o VPC (Ä‘á»ƒ tiáº¿t kiá»‡m chi phÃ­ ban Ä‘áº§u) vÃ  muá»‘n táº¡o láº¡i thá»§ cÃ´ng á»Ÿ cÃ¡c Lab sau, hÃ£y lÃ m theo cÃ¡c bÆ°á»›c sau:

1. Truy cáº­p dá»‹ch vá»¥ **VPC**, chá»n **NAT gateways** á»Ÿ menu bÃªn trÃ¡i.
2. Nháº¥n **Create NAT gateway**.
3. Cáº¥u hÃ¬nh theo thÃ´ng sá»‘ sau:
   - **Name**: `genzite-nat-gw`
   - **Availability mode**: `Zonal`
   - **Subnet**: Chá»n Public Subnet cá»§a báº¡n (vÃ­ dá»¥: `genzite-subnet-public1-us-east-1a`)
   - **Connectivity type**: `Public`
   - **Elastic IP allocation ID**: Nháº¥n nÃºt **Allocate Elastic IP**

![Create NAT Gateway](/images/5-Workshop/5.2-Lab1-Infrastructure-Frontend/1-VPC/create-nat-gw.png)

4. Nháº¥n **Create NAT gateway** vÃ  Ä‘á»£i vÃ i phÃºt Ä‘á»ƒ tráº¡ng thÃ¡i chuyá»ƒn sang **Available**.
*(LÆ°u Ã½: Náº¿u táº¡o thá»§ cÃ´ng, báº¡n cáº§n vÃ o Route Table cá»§a Private Subnet vÃ  trá» route `0.0.0.0/0` tá»›i NAT Gateway vá»«a táº¡o).*

## BÆ°á»›c 2: Kiá»ƒm tra láº¡i tÃ i nguyÃªn máº¡ng

QuÃ¡ trÃ¬nh táº¡o sáº½ máº¥t vÃ i phÃºt do AWS cáº§n thá»i gian khá»Ÿi táº¡o tÃ i nguyÃªn. Khi hoÃ n táº¥t, hÃ£y kiá»ƒm tra:

1. **Subnets**: Äi tá»›i má»¥c **Subnets** á»Ÿ menu trÃ¡i vÃ  Ä‘áº£m báº£o báº¡n cÃ³ 2 Public Subnet vÃ  2 Private Subnet Ä‘Æ°á»£c gÃ¡n vá»›i VPC `genzite-vpc`.
2. **Internet Gateways**: Äi tá»›i **Internet Gateways**, Ä‘áº£m báº£o cÃ³ 1 IGW Ä‘ang á»Ÿ tráº¡ng thÃ¡i **Attached** vÃ o VPC `genzite-vpc`.
3. **NAT Gateways**: Äi tá»›i **NAT Gateways**, Ä‘áº£m báº£o cÃ³ 1 NAT Gateway Ä‘ang á»Ÿ tráº¡ng thÃ¡i **Available**.
4. **Route Tables**: Äi tá»›i **Route Tables**.
   - Cáº§n cÃ³ 1 Route Table dÃ nh cho Public Subnet (dÃ¹ng chung cho cáº£ 2 AZ, cÃ³ route `0.0.0.0/0` trá» tá»›i Internet Gateway).
   - Cáº§n cÃ³ 2 Route Table dÃ nh cho Private Subnet (má»—i AZ 1 Route Table, cÃ³ route `0.0.0.0/0` trá» tá»›i NAT Gateway, vÃ  cÃ³ má»™t route Ä‘áº·c biá»‡t trá» tá»›i S3 Gateway Endpoint).

## BÆ°á»›c 3: Báº­t tÃ­nh nÄƒng Auto-assign public IPv4 address

Äá»ƒ cÃ¡c EC2 instance khi Ä‘Æ°á»£c táº¡o trong Public Subnet cÃ³ thá»ƒ tá»± Ä‘á»™ng nháº­n Public IP, ta cáº§n báº­t tÃ­nh nÄƒng auto-assign trÃªn Public Subnet.

1. Táº¡i VPC Dashboard, chá»n má»¥c **Subnets**.
2. TÃ­ch chá»n **Public Subnet** cá»§a báº¡n (vÃ­ dá»¥: `genzite-subnet-public1-us-east-1a`).
3. Nháº¥n vÃ o nÃºt **Actions** -> **Edit subnet settings**.
4. ÄÃ¡nh dáº¥u tÃ­ch vÃ o Ã´ **Enable auto-assign public IPv4 address**.
5. Nháº¥n **Save**.

---
**HoÃ n táº¥t pháº§n 1!** Báº¡n Ä‘Ã£ thiáº¿t láº­p xong máº¡ng cho bÃ i lab. BÆ°á»›c tiáº¿p theo, chÃºng ta sáº½ chuyá»ƒn sang cáº¥u hÃ¬nh Security (IAM Role & Security Group).
