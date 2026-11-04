from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.repository import TaskRepository
from app.services import TaskService
from app.schemas import (
    TaskCreate,
    TaskUpdate,
    TaskResponse
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)


def get_task_service(db: Session = Depends(get_db)):
    repository = TaskRepository(db)
    return TaskService(repository)


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    service: TaskService = Depends(get_task_service)
):
    return service.get_all_tasks()


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
)
def create_task(
    task_data: TaskCreate,
    service: TaskService = Depends(get_task_service)
):
    return service.create_task(task_data)


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    try:
        return service.get_task(task_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    service: TaskService = Depends(get_task_service)
):
    try:
        return service.update_task(
            task_id,
            task_data
        )
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    try:
        service.delete_task(task_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )


@router.patch(
    "/{task_id}/complete",
    response_model=TaskResponse
)
def complete_task(
    task_id: int,
    service: TaskService = Depends(get_task_service)
):
    try:
        return service.complete_task(task_id)
    except ValueError:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
