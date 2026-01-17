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

┌─────────────────────────────────────────────────────────────┐
│                    Client Browser                           │
│              (React Single Page App)                        │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              API Gateway (Node.js/Express)                  │
│  - Authentication & Authorization                           │
│  - Rate Limiting                                            │
│  - Request Routing                                          │
└──────────┬──────────────────────────────┬───────────────────┘
           │                              │
           ▼                              ▼
┌──────────────────┐            ┌─────────────────────┐
│  AI Service      │            │  Django Admin App   │
│  (Python/FastAPI)│            │  (Data Management)  │
│  - ML Model      │            │  - Patient Records  │
│  - Predictions   │            │  - Analytics        │
└─────────┬────────┘            └───────────┬─────────┘
          │                                 │
          ▼                                 ▼
┌─────────────────────────────────────────────────────────────┐
│              PostgreSQL Database (Shared)                   │
│  - Symptoms data                                            │
│  - AI model results                                         │
│  - Patient records                                          │
└─────────────────────────────────────────────────────────────┘

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
