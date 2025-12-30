from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskOut

router = APIRouter()

@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    obj = Task(**task.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@router.get("/", response_model=list[TaskOut])
def list_tasks(page: int = 1, page_size: int = 10, db: Session = Depends(get_db)):
    offset = (page-1)*page_size
    return db.query(Task).offset(offset).limit(page_size).all()
