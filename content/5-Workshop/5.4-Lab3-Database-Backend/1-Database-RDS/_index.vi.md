---
title: "1. Khá»Ÿi táº¡o RDS"
weight: 1
chapter: false
pre: " <b> 5.4.1. </b> "
---


Há»‡ thá»‘ng Genzite cáº§n má»™t nÆ¡i lÆ°u trá»¯ dá»¯ liá»‡u cÃ³ cáº¥u trÃºc (thÃ´ng tin User, cÃ¡c Project Web Ä‘Ã£ táº¡o, cáº¥u trÃºc JSON layout). Trong mÃ´i trÆ°á»ng AWS, dá»‹ch vá»¥ tá»‘i Æ°u nháº¥t lÃ  **Amazon Relational Database Service (RDS)**. 

Äá»ƒ tiáº¿t kiá»‡m chi phÃ­ cho bÃ i Lab vÃ  Ä‘Ã¡p á»©ng cáº¥u hÃ¬nh MVP (Minimum Viable Product), ta sáº½ chá»n PostgreSQL cháº¡y trÃªn instance `db.t4g.micro` vÃ  Ä‘áº·t trong Private Subnet.

## BÆ°á»›c 1: Táº¡o DB Subnet Group

TrÆ°á»›c khi táº¡o RDS, ta cáº§n nÃ³i cho AWS biáº¿t Database nÃ y Ä‘Æ°á»£c phÃ©p náº±m trong cÃ¡c Subnet nÃ o. Dá»±a theo Security Best Practice, ta chá»‰ Ä‘áº·t DB trong Private Subnet.

1. Má»Ÿ dá»‹ch vá»¥ **RDS** trÃªn AWS Console.
2. Tá»« menu bÃªn trÃ¡i, chá»n **Subnet groups**.
3. Nháº¥n **Create DB subnet group**.
4. **Name**: `genzite-subnet-rds`.
5. **Description**: `genzite-subnet-rds`.
6. **VPC**: Chá»n `genzite-vpc`.
![Create Subnet Group](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.1.png)
7. KÃ©o xuá»‘ng pháº§n **Add subnets**:
   - Chá»n **Availability Zones**: Chá»n `us-east-1a` vÃ  `us-east-1b`.
   - Chá»n **Subnets**: Chá»n 2 **Private Subnets**
![Subnet Group](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.2.png)
8. Nháº¥n **Create**.
![Create Done](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.3.png)
## BÆ°á»›c 2: Khá»Ÿi táº¡o Database Instance

1. Tá»« menu bÃªn trÃ¡i, chá»n **Databases** vÃ  nháº¥n **Create database** vÃ  chá»n **Full Configuration**
![Create RDS](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.4.png)
2. **Engine options**: Chá»n **PostgreSQL** (PhiÃªn báº£n `PostgreSQL 16.14-R2`).
4. **Templates**: Chá»n **Sand box**
5. **Settings**:
   - **DB instance identifier**: `genzitedb`.
   - **Master username**: `genzite_admin`.
   - **Credentials management**: Chá»n **Self managed**.
   - **Master password**: Nháº­p máº­t kháº©u Ä‘á»§ máº¡nh vÃ  xÃ¡c nháº­n láº¡i á»Ÿ Ã´ **Confirm master password**.
![Credentials](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.6.png)
![Authentication](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.7.png)

6. **Instance configuration**:
   - Instance type: Chá»n `db.t3.micro`.
7. **Storage**:
   - **Storage type**: Chá»n **General Purpose SSD (gp2)**.
   - **Allocated storage**: `30` GiB.
   - Bá» tÃ­ch **Enable storage autoscaling** (trong pháº§n Additional storage configuration náº¿u cÃ³).

8. **Connectivity**:
   - **Compute resource**: Chá»n **Don't connect to an EC2 compute resource**.
   - **Network type**: Chá»n **IPv4**. 
![Storage & Connectivity](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.8.png)
   - **Virtual private cloud (VPC)**: Chá»n `genzite-vpc`.
   - **DB Subnet Group**: Chá»n `genzite-subnet-rds`.
   - **Public access**: Chá»n **No** (Database khÃ´ng Ä‘Æ°á»£c phÃ©p truy cáº­p tá»« Internet).
    - **VPC security group (firewall)**: Chá»n **Choose existing**, loáº¡i bá» tháº» `default`, vÃ  chá»n `genzite-rds-sg` (ÄÃ£ táº¡o á»Ÿ Lab 1 - Security).
   ![Public Access](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.5.png)

9. **Database authentication**: Chá»n **Password authentication**.
10. **Monitoring**:
    - **Database Insights**: Chá»n **Database Insights - Standard**.
    - **Performance Insights**: Bá» tÃ­ch **Enable Performance Insights**.
    - **Enhanced Monitoring**: Bá» tÃ­ch **Enable Enhanced monitoring**.
![Monitoring](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.9.png)

11. Má»Ÿ rá»™ng pháº§n **Additional configuration**:
    - **Database options**:
      - Nháº­p **Initial database name**: `genzite`. *(Náº¿u khÃ´ng nháº­p Ã´ nÃ y, RDS sáº½ khÃ´ng táº¡o sáºµn Database cho báº¡n)*.
      - **DB parameter group**: Chá»n `default.postgres16`.
    - **Encryption**: Bá» tÃ­ch **Enable encryption**.
    - **Backup**:
      - TÃ­ch chá»n **Enable automated backup**.
      - **Backup retention period**: Chá»n `1 day`.
![Additional configuration](/images/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/5.4.1.10.png)

12. Kiá»ƒm tra láº¡i thÃ´ng tin, cuá»™n xuá»‘ng dÆ°á»›i cÃ¹ng vÃ  nháº¥n **Create database**.

## BÆ°á»›c 3: Láº¥y Endpoint káº¿t ná»‘i

QuÃ¡ trÃ¬nh khá»Ÿi táº¡o Database cÃ³ thá»ƒ máº¥t tá»« 5-10 phÃºt.

1. Khi tráº¡ng thÃ¡i Database chuyá»ƒn sang `Available`, hÃ£y nháº¥n vÃ o tÃªn `genzite-db`.
2. Trong tab **Connectivity & security**, tÃ¬m má»¥c **Endpoint**.
3. Sao chÃ©p láº¡i Ä‘Æ°á»ng dáº«n **Endpoint** nÃ y (vÃ­ dá»¥: `genzite-db.xxxxxxxxx.us-east-1.rds.amazonaws.com`). 

Báº¡n sáº½ cáº§n Endpoint nÃ y cÃ¹ng vá»›i Username, Password vÃ  TÃªn database (`genzite`) Ä‘á»ƒ cáº¥u hÃ¬nh cho mÃ¡y chá»§ Backend EC2 á»Ÿ bÆ°á»›c tiáº¿p theo.
