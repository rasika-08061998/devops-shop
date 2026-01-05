🚀 **DevOps Capstone Project – Automated CI/CD on AWS EKS**
📌 **Project Overview**

This project demonstrates a production-grade DevOps CI/CD pipeline where application changes pushed to GitHub are automatically built, containerized, pushed to AWS ECR, and deployed to an AWS EKS cluster with zero-downtime rolling updates.

The application is exposed publicly using a Kubernetes Service (LoadBalancer) on AWS.


🏗️ Architecture:

Developer Push (GitHub)
        |
        v
GitHub Actions (CI/CD)
        |
        |-- Build Docker Image
        |-- Tag with Git Commit SHA
        |-- Push to Amazon ECR
        |-- Update EKS Deployment
        v
AWS EKS (Kubernetes)
        |
        |-- Rolling Update (Zero Downtime)
        v
AWS LoadBalancer (Public DNS)


🧰 Tech Stack

Cloud: AWS
Container Registry: Amazon ECR
Orchestration: Amazon EKS (Kubernetes)
IaC: Terraform
CI/CD: GitHub Actions
Containerization: Docker
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript

⚙️ Key Features

✅ End-to-end CI/CD automation
✅ Docker image tagging using GitHub commit SHA
✅ Zero-downtime Rolling Updates
✅ Secure IAM + Kubernetes RBAC (aws-auth)
✅ No manual kubectl intervention
✅ Public access via AWS LoadBalancer DNS
✅ Infrastructure as Code using Terraform

🔁 CI/CD Workflow (GitHub Actions)

1. On every push to main branch:
2. GitHub Actions builds Docker image
3. Image is tagged with commit SHA
4. Image is pushed to Amazon ECR
5. kubectl set image updates EKS Deployment
6. Kubernetes performs rolling update
7. Pipeline verifies rollout success

📦 Kubernetes Deployment Strategy

Replicas: 2
Strategy: RollingUpdate
maxUnavailable: 1
maxSurge: 1
This ensures zero downtime during deployments.

🌐 Application Access

The application is exposed using:
kubectl get svc devops-shop-service

Output provides an AWS LoadBalancer DNS:
http://<elb-dns-name>

🔐 Security Best Practices

IAM least-privilege policies
No secrets committed to GitHub
Terraform state files excluded via .gitignore
GitHub Actions IAM user mapped via aws-auth

📚 Learning Outcomes

Real-world EKS troubleshooting
CI/CD automation for Kubernetes
IAM & RBAC integration
Production deployment patterns
Infrastructure as Code best practices

👩‍💻 Author

Rasika Deshmukh
DevOps | Cloud | Kubernetes | AWS

