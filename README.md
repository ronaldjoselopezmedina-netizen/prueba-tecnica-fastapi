# Prueba Técnica Backend - FastAPI

## Stack
- Python 3.11
- FastAPI
- PostgreSQL (Docker)
- SQLAlchemy
- JWT

## Setup
```bash
python -m venv venv
.env\Scripts\activate
pip install -r requirements.txt
docker-compose up -d
python create_tables.py
python -m uvicorn app.main:app
```

## Usuario inicial
- username: admin
- password: admin123

## Login
POST /auth/login
