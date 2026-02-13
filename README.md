# container-daily-driver-demo

# 🚀 FastAPI + MongoDB + MinIO using Docker Compose

This project demonstrates how Docker and Docker Compose can be used for daily development by running a Python FastAPI application together with MongoDB and S3-compatible object storage (MinIO).

---

## Architecture Overview

Client -> FastAPI -> MongoDB  
Client -> FastAPI -> MinIO (S3)

---

## Prerequisites

- Docker
- Docker Compose

Verify:

```
docker --version  
docker compose version
```
---

## Clone Repository

```
git clone https://github.com/your-org/container-daily-driver-demo.git
```

```
cd container-daily-driver-demo
```

---

## Start Application

```
docker compose up --build
```

---

## Verify

```
docker compose ps
```
You should see:
```
app running  
mongo running  
minio running  
```
---

## Access

FastAPI: http://localhost:8000  
Swagger: http://localhost:8000/docs  
MinIO Console: http://localhost:9001  

Login:  
minioadmin / minioadmin

---

## Upload File

Use `POST` /upload from Swagger UI

---

## Check Mongo

```
docker exec -it mongo mongosh -u myuser -p mypass
```
```
use file_db  
db.files.find()
```
---

## Stop
```
docker compose down
```
Delete data:
```
docker compose down -v
```
---

## Useful Commands
```
docker ps  
docker compose logs app  
docker compose exec app sh  
docker volume ls  
docker system prune  
```
---

One command runs everything:
```
docker compose up
```