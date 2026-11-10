from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.repository import TaskRepository
from app.services import TaskService


def get_task_service(db: Session = Depends(get_db)):
    repository = TaskRepository(db)
    return TaskService(repository)
