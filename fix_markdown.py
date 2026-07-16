import os
import re

files = [
    "content/5-Workshop/5.2-Lab1-Infrastructure-Frontend/1-VPC/_index.md",
    "content/5-Workshop/5.2-Lab1-Infrastructure-Frontend/1-VPC/_index.vi.md",
    "content/5-Workshop/5.2-Lab1-Infrastructure-Frontend/2-Security/_index.md",
    "content/5-Workshop/5.2-Lab1-Infrastructure-Frontend/2-Security/_index.vi.md",
    "content/5-Workshop/5.2-Lab1-Infrastructure-Frontend/3-Deploy-Frontend/_index.md",
    "content/5-Workshop/5.2-Lab1-Infrastructure-Frontend/3-Deploy-Frontend/_index.vi.md",
    "content/5-Workshop/5.3-Lab2-Cognito-Auth/1-Create-UserPool/_index.md",
    "content/5-Workshop/5.3-Lab2-Cognito-Auth/1-Create-UserPool/_index.vi.md",
    "content/5-Workshop/5.3-Lab2-Cognito-Auth/2-App-Integration/_index.md",
    "content/5-Workshop/5.3-Lab2-Cognito-Auth/2-App-Integration/_index.vi.md",
    "content/5-Workshop/5.3-Lab2-Cognito-Auth/3-Test-Authentication/_index.md",
    "content/5-Workshop/5.3-Lab2-Cognito-Auth/3-Test-Authentication/_index.vi.md",
    "content/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/_index.md",
    "content/5-Workshop/5.4-Lab3-Database-Backend/1-Database-RDS/_index.vi.md",
    "content/5-Workshop/5.4-Lab3-Database-Backend/2-Backend-EC2/_index.md",
    "content/5-Workshop/5.4-Lab3-Database-Backend/2-Backend-EC2/_index.vi.md",
    "content/5-Workshop/5.4-Lab3-Database-Backend/3-Load-Balancer/_index.md",
    "content/5-Workshop/5.4-Lab3-Database-Backend/3-Load-Balancer/_index.vi.md"
]

for fpath in files:
    if os.path.exists(fpath):
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        rel_dir = os.path.dirname(fpath).replace("content/", "").replace("\\", "/")
        replacement = f"/images/{rel_dir}/"
        
        # Replace image URLs safely
        content = re.sub(r"(?<!/)(\./)?\bimage[s]?/", replacement, content)
        
        with open(fpath, "w", encoding="utf-8", newline='\n') as f:
            f.write(content)
        
        print(f"Processed {fpath}")
