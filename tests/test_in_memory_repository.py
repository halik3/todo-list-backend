
from app.in_memory_repository import InMemoryTaskRepository
from app.schemas import TaskCreate, TaskUpdate
from app.services import TaskService


def test_in_memory_repository_crud():
    repository = InMemoryTaskRepository()

    # CREATE
    task = repository.create(
        TaskCreate(
            title="Belajar SOLID",
            description="Mempelajari prinsip OCP"
        )
    )

    assert task.id == 1
    assert task.title == "Belajar SOLID"

    # GET ALL
    tasks = repository.get_all()
    assert len(tasks) == 1

    # GET BY ID
    found_task = repository.get_by_id(1)
    assert found_task.title == "Belajar SOLID"

    # UPDATE
    updated_task = repository.update(
        1,
        TaskUpdate(title="Belajar SOLID lebih dalam")
    )

    assert updated_task.title == "Belajar SOLID lebih dalam"

    # COMPLETE
    completed_task = repository.complete(1)
    assert completed_task.is_completed is True

    # DELETE
    deleted_task = repository.delete(1)
    assert deleted_task.id == 1
    assert repository.get_by_id(1) is None


def test_task_service_with_in_memory_repository():
    repository = InMemoryTaskRepository()
    service = TaskService(repository)

    task = service.create_task(
        TaskCreate(title="Testing OCP")
    )

    assert task.title == "Testing OCP"

    retrieved_task = service.get_task(task.id)
    assert retrieved_task.id == task.id

    completed_task = service.complete_task(task.id)
    assert completed_task.is_completed is True


def test_in_memory_repository_missing_task():
    repository = InMemoryTaskRepository()

    assert repository.get_by_id(999) is None
    assert repository.update(999, TaskUpdate(title="Updated")) is None
    assert repository.delete(999) is None
    assert repository.complete(999) is None
