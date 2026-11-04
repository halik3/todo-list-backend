from sqlalchemy.orm import Session

from app.models import Task
from app.schemas import TaskCreate, TaskUpdate


class TaskRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Task).all()

    def get_by_id(self, task_id: int):
        return self.db.query(Task).filter(
            Task.id == task_id
        ).first()

    def create(self, task_data: TaskCreate):
        task = Task(**task_data.model_dump())

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task

    def update(self, task_id: int, task_data: TaskUpdate):
        task = self.get_by_id(task_id)

        if not task:
            return None

        data = task_data.model_dump(
            exclude_unset=True
        )

        for key, value in data.items():
            setattr(task, key, value)

        self.db.commit()
        self.db.refresh(task)

        return task

    def delete(self, task_id: int):
        task = self.get_by_id(task_id)

        if not task:
            return None

        self.db.delete(task)
        self.db.commit()

        return task

    def complete(self, task_id: int):
        task = self.get_by_id(task_id)

        if not task:
            return None

        task.is_completed = True

        self.db.commit()
        self.db.refresh(task)

        return task
