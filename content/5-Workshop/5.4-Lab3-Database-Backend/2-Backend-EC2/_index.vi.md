---
title: "2. Triá»ƒn khai Backend"
weight: 2
chapter: false
pre: " <b> 5.4.2. </b> "
---


Äá»ƒ á»©ng dá»¥ng Genzite xá»­ lÃ½ cÃ¡c request phá»©c táº¡p (sinh JSON tá»« prompt, giao tiáº¿p vá»›i Database), chÃºng ta cáº§n má»™t mÃ¡y chá»§ áº£o (Virtual Machine). Trong AWS, Ä‘Ã³ lÃ  dá»‹ch vá»¥ **Amazon Elastic Compute Cloud (EC2)**.

Dá»±a theo thiáº¿t káº¿, EC2 sáº½ Ä‘Æ°á»£c Ä‘áº·t trong **Private Subnet** Ä‘á»ƒ áº©n khá»i internet, vÃ  chá»‰ cho phÃ©p lÆ°u lÆ°á»£ng truy cáº­p Ä‘i qua Application Load Balancer (ALB).

## BÆ°á»›c 1: Khá»Ÿi táº¡o EC2 Instance

1. Má»Ÿ dá»‹ch vá»¥ **EC2** trÃªn AWS Console.
2. Nháº¥n **Launch instances**.
3. **Name**: Nháº­p `genzite-backend`.
4. **Application and OS Images (Amazon Machine Image)**:
   - Chá»n **Ubuntu**.
   - Chá»n **Ubuntu Server 24.04 LTS**.
5. **Instance type**:
   - Chá»n `t3a.large`.
6. **Key pair (login)**:
   - Chá»n **Create new key pair** vá»›i tÃªn `genzite-key`.
7. **Network settings**:
   - Nháº¥n **Edit**.
   - **VPC**: Chá»n `genzite-vpc`.
   - **Subnet**: Chá»n má»™t **Private Subnet**.
   - **Auto-assign public IP**: **Disable**.
   - **Firewall (security groups)**: Chá»n **Create security group**.
   - **Security group name**: `genzite-sg`.
![Config EC2](/images/5-Workshop/5.4-Lab3-Database-Backend/2-Backend-EC2/5.4.2.1.png)
8. **Configure storage**:
   - TÄƒng dung lÆ°á»£ng tá»« `8` lÃªn `30` GiB.
9. CÃ¡c pháº§n cÃ²n láº¡i giá»¯ nguyÃªn. Nháº¥n **Launch instance**.
![Config EC2](/images/5-Workshop/5.4-Lab3-Database-Backend/2-Backend-EC2/5.4.2.2.png)
## BÆ°á»›c 2: ThÃªm IAM Role cho EC2

1. Quay vá» trang chá»§ **EC2** chá»n **genzite-backend**, chá»n **Actions**,chá»n **Sercurity** rá»“i **Modify IAM role**.
![Config EC2](/images/5-Workshop/5.4-Lab3-Database-Backend/2-Backend-EC2/5.4.2.3.png)
2. Thay Ä‘á»•i IAM role thÃ nh role **genzite-role**.
3. Nháº¥n **Update IAM role**.
![Config EC2](/images/5-Workshop/5.4-Lab3-Database-Backend/2-Backend-EC2/5.4.2.4.png)
4. Quay láº¡i trang **EC2**, Tiáº¿n hÃ nh **Reboot** láº¡i EC2 vÃ  Ä‘á»£i trong giÃ¢y lÃ¡t.
5. NhÆ° váº­y lÃ  Ä‘Ã£ thÃªm quyá»n xong cho EC2.


## BÆ°á»›c 3: Káº¿t ná»‘i vÃ  CÃ i Ä‘áº·t MÃ´i trÆ°á»ng (Docker, Node.js)

1. Sau khi reboot, chá»n láº¡i EC2 vÃ  nháº¥n **Connect**.
2. Chuyá»ƒn qua tab **Session Manager** vÃ  kÃ©o xuá»‘ng chá»n **Connect**.
3. Trong terminal, test thá»­ vá»›i lá»‡nh `whoami` (náº¿u tráº£ vá» `ssm-user` lÃ  chÃ­nh xÃ¡c).
4. Tiáº¿n hÃ nh cháº¡y cÃ¡c lá»‡nh sau Ä‘á»ƒ cáº­p nháº­t há»‡ thá»‘ng vÃ  cÃ i Ä‘áº·t mÃ´i trÆ°á»ng:

```bash
sudo apt update
sudo apt update && sudo apt upgrade -y

# CÃ i Ä‘áº·t Docker
sudo apt install -y docker.io
docker --version
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl status docker
```
*(Nháº¥n `Ctrl + C` Ä‘á»ƒ thoÃ¡t khá»i mÃ n hÃ¬nh status cá»§a Docker)*

Tiáº¿p tá»¥c cÃ i Ä‘áº·t Docker Compose vÃ  Git:
```bash
sudo apt install -y docker-compose-v2
docker compose version

sudo apt install -y git
git --version
```

## BÆ°á»›c 4: Táº£i Source Code vÃ  Cháº¡y á»¨ng Dá»¥ng

Chuyá»ƒn sang quyá»n root Ä‘á»ƒ táº£i code vÃ  cháº¡y dá»± Ã¡n:
```bash
sudo -i
git clone https://github.com/KrisCTer/Genzite
cd Genzite

# CÃ i Ä‘áº·t Node.js 22.x
curl -fsSL https://deb.nodesource.com/setup_22.x | sudo -E bash -
sudo apt install -y nodejs
node -v
npm -v

# CÃ i Ä‘áº·t pnpm
sudo npm install -g pnpm
pnpm install
pnpm run build:packages

# Cáº¥u hÃ¬nh biáº¿n mÃ´i trÆ°á»ng
cd infra
cp .env.example .env

# Khá»Ÿi cháº¡y cÃ¡c dá»‹ch vá»¥ háº¡ táº§ng vá»›i Docker Compose
docker compose up -d db cache zookeeper kafka
cd ..

# Migrate database
pnpm run prisma:migrate

# Khá»Ÿi cháº¡y cÃ¡c microservices cá»§a dá»± Ã¡n (cháº¡y ngáº§m vá»›i nohup)
nohup pnpm run dev:gateway > gateway.log 2>&1 &
nohup pnpm run dev:ai > ai.log 2>&1 &
nohup pnpm run dev:data > data.log 2>&1 &
nohup pnpm run dev:identity > identity.log 2>&1 &
nohup pnpm run dev:media > media.log 2>&1 &
nohup pnpm run dev:site > site.log 2>&1 &
nohup pnpm run dev:notification > notification.log 2>&1 &
nohup pnpm run dev:frontend --host 0.0.0.0 > frontend.log 2>&1 &
```
