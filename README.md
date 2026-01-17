# 🏥 Healthcare AI Symptom Checker Platform

[![React](https://img.shields.io/badge/React-18-61DAFB)](https://reactjs.org/)
[![Node.js](https://img.shields.io/badge/Node.js-18-339933)](https://nodejs.org/)
[![Python](https://img.shields.io/badge/Python-3.9-3776AB)](https://python.org/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED)](https://docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-326CE5)](https://kubernetes.io/)
[![IBM Cloud](https://img.shields.io/badge/IBM%20Cloud-Deployed-054ADA)](https://cloud.ibm.com)

**Capstone Project for IBM Full Stack Application Developer Certification**

AI-powered healthcare platform that analyzes symptoms and provides risk assessments using microservices architecture, containerization, and cloud-native deployment.

## 🎯 Demonstrated Skills (9/9 Courses)

| Course | Technologies Implemented |
|--------|-------------------------|
| **Cloud Computing** | Public cloud deployment, auto-scaling, load balancing |
| **HTML/CSS/JS** | React SPA, responsive UI, ES6+ features |
| **Git/GitHub** | CI/CD pipelines, branching strategy, version control |
| **React** | Hooks, Context API, component architecture |
| **Node.js/Express** | RESTful API, middleware, JWT auth |
| **Python** | AI/ML model, data preprocessing, FastAPI |
| **Django/SQL** | Admin panel, PostgreSQL, ORM |
| **Docker/K8s** | Containerization, orchestration, OpenShift |
| **Microservices** | Service mesh, serverless functions, API gateway |

## 🚀 Live Demo

**Frontend:** https://healthcare-ai.yourdomain.com  
**Django Admin:** https://admin-healthcare-ai.yourdomain.com  
**API Docs:** https://api-healthcare-ai.yourdomain.com/docs

## 📊 Architecture

## 📊 Architecture

graph TB
    subgraph "Client Layer"
        UI[React Frontend<br/>Port 3000]
        UI --> |HTTP/HTTPS| APIGW
    end

    subgraph "API Gateway Layer"
        APIGW[Node.js API Gateway<br/>Express.js<br/>Port 3000]
        APIGW --> |JWT Auth| AUTH[Authentication<br/>Middleware]
        APIGW --> |Routes Requests| AI_SERVICE
        APIGW --> |Routes Requests| DJANGO
    end

    subgraph "Microservices Layer"
        AI_SERVICE[Python AI Service<br/>FastAPI<br/>Port 8000]
        DJANGO[Django Admin Panel<br/>Port 8001]
        AI_SERVICE --> |Store Results| DB
        DJANGO --> |CRUD Operations| DB
    end

    subgraph "Data Layer"
        DB[(PostgreSQL Database<br/>Port 5432)]
    end

    subgraph "Infrastructure Layer"
        K8S[Kubernetes Cluster]
        DOCKER[(Docker Containers)]
        IBM[IBM Cloud Code Engine]
    end

    subgraph "DevOps & Monitoring"
        GITHUB[GitHub Actions<br/>CI/CD Pipeline]
        DOCKER_HUB[Docker Hub<br/>Image Registry]
        MONITOR[Prometheus & Grafana]
    end

    UI --> |User Input| SYMPTOMS[Symptoms Text]
    AI_SERVICE --> |ML Prediction| MODEL[scikit-learn Model]
    AI_SERVICE --> |Trigger| SERVERLESS[IBM Cloud Function<br/>Notifications]
    GITHUB --> |Auto Deploy| IBM
    IBM --> |Orchestrate| K8S
    K8S --> |Manage| DOCKER
    MONITOR --> |Health Checks| ALL_SERVICES[All Services]

## 🔧 Quick Start

```bash
# Clone repository
git clone https://github.com/MosesKiprono/healthcare-ai-platform.git
cd healthcare-ai-platform

# Option 1: Docker Compose (Local)
docker-compose up --build

# Option 2: Kubernetes (Production)
kubectl apply -f k8s/

# Option 3: IBM Cloud Code Engine
ibmcloud ce app create --name ai-service --image moseskiprono/ai-service:latest
