from fastapi import FastAPI
from app.api import auth, tasks
from app.database import SessionLocal
from app.core.init_db import create_initial_user

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(tasks.router, prefix="/tasks", tags=["Tasks"])

@app.on_event("startup")
def startup():
    db = SessionLocal()
    create_initial_user(db)
    db.close()
