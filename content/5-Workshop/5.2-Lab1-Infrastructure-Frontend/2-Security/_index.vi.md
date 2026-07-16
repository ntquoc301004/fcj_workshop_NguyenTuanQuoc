---
title: "2. Cáº¥u hÃ¬nh Security"
weight: 2
chapter: false
pre: " <b> 5.2.2. </b> "
---


Trong pháº§n nÃ y, chÃºng ta sáº½ thiáº¿t láº­p cÃ¡c lá»›p báº£o máº­t Ä‘á»ƒ Ä‘áº£m báº£o há»‡ thá»‘ng an toÃ n, chá»‰ cho phÃ©p luá»“ng dá»¯ liá»‡u (traffic) há»£p lá»‡ Ä‘i qua vÃ  cáº¥p quyá»n vá»«a Ä‘á»§ (least privilege) cho cÃ¡c dá»‹ch vá»¥.

## BÆ°á»›c 1: Táº¡o IAM Role cho EC2

Äá»ƒ EC2 (Backend) cÃ³ thá»ƒ gá»­i log lÃªn CloudWatch vÃ  tÆ°Æ¡ng tÃ¡c vá»›i cÃ¡c dá»‹ch vá»¥ AWS khÃ¡c má»™t cÃ¡ch an toÃ n mÃ  khÃ´ng cáº§n hardcode API Key, ta sáº½ táº¡o má»™t IAM Role.

1. Má»Ÿ **AWS Management Console** vÃ  tÃ¬m dá»‹ch vá»¥ **IAM**.
2. á»ž menu bÃªn trÃ¡i, chá»n **Roles** vÃ  nháº¥n **Create role**.
3. **Select trusted entity**: Chá»n **AWS service**.
4. **Use case**: Chá»n **EC2** vÃ  nháº¥n **Next**.
5. Trong trang Add permissions, tÃ¬m vÃ  Ä‘Ã¡nh dáº¥u vÃ o cÃ¡c policy sau:
   - `AmazonSSMManagedInstanceCore` (Äá»ƒ dÃ¹ng Session Manager káº¿t ná»‘i vÃ o EC2 thay vÃ¬ má»Ÿ port 22 SSH).
   - `CloudWatchAgentServerPolicy` (Äá»ƒ Ä‘áº©y log lÃªn CloudWatch).
6. Nháº¥n **Next**.
7. **Role name**: Nháº­p `genzite-role` vÃ  nháº¥n **Create role**.

## BÆ°á»›c 2: Táº¡o Security Group cho ALB (Internet Facing)

Application Load Balancer (ALB) sáº½ lÃ  cá»­a ngÃµ giao tiáº¿p trá»±c tiáº¿p vá»›i internet.

1. Chuyá»ƒn sang dá»‹ch vá»¥ **EC2**. á»ž menu bÃªn trÃ¡i kÃ©o xuá»‘ng pháº§n Network & Security, chá»n **Security Groups**.
2. Nháº¥n **Create security group**.
3. **Security group name**: `genzite-alb-sg`.
4. **Description**: `Allow HTTP/HTTPS from Internet`.
5. **VPC**: Chá»n VPC `genzite-vpc` báº¡n Ä‘Ã£ táº¡o á»Ÿ pháº§n trÆ°á»›c.
6. **Inbound rules**:
   - ThÃªm Rule 1: Type `HTTP`, Source `Anywhere-IPv4` (`0.0.0.0/0`).
   - ThÃªm Rule 2: Type `HTTPS`, Source `Anywhere-IPv4` (`0.0.0.0/0`).
7. **Outbound rules**: Giá»¯ nguyÃªn máº·c Ä‘á»‹nh (Allow All Traffic).
8. Nháº¥n **Create security group**.
![SG ALB](/images/5-Workshop/5.2-Lab1-Infrastructure-Frontend/2-Security/5.2.2.1.png)
## BÆ°á»›c 3: Táº¡o Security Group cho EC2 (Backend)

EC2 backend chá»‰ nÃªn nháº­n traffic tá»« ALB vÃ  cho phÃ©p báº¡n SSH vÃ o, khÃ´ng Ä‘Æ°á»£c phÃ©p má»Ÿ káº¿t ná»‘i trá»±c tiáº¿p ra internet Ä‘á»ƒ trÃ¡nh rá»§i ro.

1. TÆ°Æ¡ng tá»±, nháº¥n **Create security group**.
2. **Security group name**: `genzite-sg`.
3. **Description**: Tuá»³ chá»n mÃ´ táº£, vÃ­ dá»¥ `genzite-sg created...`.
4. **VPC**: Chá»n `genzite-vpc`.
5. **Inbound rules**:
   - ThÃªm Rule 1: Type `Custom TCP`, Port Range `3000`, Source chá»n **Custom** vÃ  tÃ¬m kiáº¿m tÃªn SG cá»§a ALB lÃ  `genzite-alb-sg`, Description: `ALB`.
   - ThÃªm Rule 2: Type `SSH`, Port Range `22`, Source chá»n **My IP**, Description: `MyIP`.
   - ThÃªm Rule 3: Type `Custom TCP`, Port Range `5173`, Source chá»n **Custom** vÃ  tÃ¬m kiáº¿m tÃªn SG cá»§a ALB lÃ  `genzite-alb-sg`, Description: `ALB`.
6. **Outbound rules**: Giá»¯ nguyÃªn máº·c Ä‘á»‹nh (Allow All Traffic) Ä‘á»ƒ táº£i thÆ° viá»‡n vÃ  gá»i ra bÃªn ngoÃ i.
7. Nháº¥n **Create security group**.

## BÆ°á»›c 4: Táº¡o Security Group cho RDS (Database)

PostgreSQL Database lÃ  nÆ¡i chá»©a dá»¯ liá»‡u quan trá»ng nÃªn chá»‰ cho phÃ©p duy nháº¥t mÃ¡y chá»§ EC2 káº¿t ná»‘i tá»›i.

1. Nháº¥n **Create security group**.
2. **Security group name**: `genzite-rds-sg`.
3. **Description**: `genzite-rds-sg`.
4. **VPC**: Chá»n `genzite-vpc`.
5. **Inbound rules**:
   - ThÃªm Rule 1: Type `PostgreSQL`, Port Range `5432`, Source chá»n **Custom** vÃ  tÃ¬m kiáº¿m SG cá»§a EC2 lÃ  `genzite-sg`.
6. Nháº¥n **Create security group**.

---

